#!/usr/bin/env python3
"""
USINO supply chain graph — repair the supplier_name column.

WHY THIS EXISTS
    The extractor wrote comma-separated prose into supplier_name, and the CSV
    writer then split it across rows. So

        "Tamagawa Seiki — NON-LISTED Japanese specialist, strong in precision
         robotics and semiconductor equipment"

    became three supplier rows: a real company, then "strong in precision
    robotics", then "semiconductor equipment". Loaded into the ontology those
    fragments become fake companies sitting in the supply chain.

WHAT IT DOES — three different repairs, because these are three problems:

    1. ANNOTATION SUFFIX — "Carl Zeiss SMT — NON-LISTED" is a real supplier
       carrying a note. The name is cleaned, the note moves to `source`, and
       supplier_listed is set to N. The row is KEPT.

    2. CONTINUATION FRAGMENT — "family-owned", ">95% reported", "EML epitaxy
       capacity is concentrated". These are the tail of the previous row's
       prose. The text is appended to the PREVIOUS row's `source` so nothing is
       lost, and the row is DROPPED.

    3. CATEGORY DESCRIPTOR — "Chinese magnet makers", "Chinese SoC vendors".
       These are deliberate stand-ins for non-listed groups the analyst chose
       not to name. They are LEFT ALONE. Distinguishing these from fragments is
       the whole point of this script: a fragment contains a finite verb, a
       descriptor is a plain noun phrase.

USAGE
    python3 repair_graph_csv.py GRAPH/chokepoint-map-2026-08-04.csv --dry-run
    python3 repair_graph_csv.py GRAPH/chokepoint-map-2026-08-04.csv

    The original is backed up alongside as .bak-<date> and a full report of every
    change is written to GRAPH/_repair-report-<date>.md. Nothing is deleted
    without being recorded there.

This never touches _quarantine-do-not-publish.csv.
"""

import argparse
import csv
import re
import shutil
import sys
from datetime import date
from pathlib import Path

COLUMNS = [
    "company", "ticker", "depends_on", "dependency_type", "supplier_name",
    "supplier_listed", "supplier_ticker", "country", "tier", "confidence",
    "source", "date_added",
]

# " — NON-LISTED Japanese specialist" and friends.
ANNOTATION_RE = re.compile(
    r"\s+[—–]+\s+(?P<note>(?:NON[\s-]?LISTED|NOT\s+separately\s+listed|NOT\s+listed|"
    r"unlisted|private|state[\s-]?owned|family[\s-]?owned)\b.*)$",
    re.IGNORECASE,
)

# A finite verb means it is a sentence fragment, not a name.
FRAGMENT_VERB_RE = re.compile(
    r"\b(is|are|was|were|has|have|had|remains?|becomes?|improving|improved|"
    r"exceeds?|includes?|reported|disclosed|covered|concentrated|dominates?)\b",
    re.IGNORECASE,
)

# Not a name under any reading.
NON_ENTITY_RE = re.compile(
    r"^\s*(?:[<>≥≤~]|\d|not\b|no\b|none\b|n/?a\b|unknown\b|tbd\b|approx\b)",
    re.IGNORECASE,
)


def norm(s) -> str:
    return (s or "").strip()


def classify(name: str) -> str:
    """One of: ok | annotation | fragment | descriptor."""
    n = norm(name)
    if len(n) < 2 or "%" in n or NON_ENTITY_RE.match(n):
        return "fragment"

    starts_upper = n[0].isupper() or "一" <= n[0] <= "鿿"
    if not starts_upper:
        # Lowercase single token is a brand (onsemi, imec, ams).
        # Lowercase phrase is prose.
        return "fragment" if re.search(r"[\s\-]", n) else "ok"

    if ANNOTATION_RE.search(n):
        return "annotation"
    if FRAGMENT_VERB_RE.search(n):
        return "fragment"
    return "ok"


def main() -> None:
    ap = argparse.ArgumentParser(description="Repair supplier_name in a graph CSV.")
    ap.add_argument("csv_path")
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing")
    args = ap.parse_args()

    path = Path(args.csv_path)
    if "quarantine" in path.name.lower():
        sys.exit("Refusing to touch the quarantine file.")
    if not path.is_file():
        sys.exit(f"Not found: {path}")

    with path.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    out, cleaned, dropped = [], [], []

    for row in rows:
        name = norm(row.get("supplier_name"))
        kind = classify(name)

        if kind == "annotation":
            m = ANNOTATION_RE.search(name)
            clean = ANNOTATION_RE.sub("", name).strip(" ,;·-—–")
            note = m.group("note").strip()
            cleaned.append((row.get("company"), name, clean, note))
            row["supplier_name"] = clean
            if not norm(row.get("supplier_listed")):
                row["supplier_listed"] = "N"
            row["source"] = f"{norm(row.get('source'))} || supplier note: {note}".strip(" |")
            out.append(row)
            continue

        if kind == "fragment":
            # Fold the text back into the row it was split away from, so the
            # observation survives even though the fake supplier does not.
            if out:
                prev = out[-1]
                same_context = (
                    prev.get("company") == row.get("company")
                    and prev.get("depends_on") == row.get("depends_on")
                )
                target = prev if same_context else None
            else:
                target = None
            if target is not None:
                target["source"] = (
                    f"{norm(target.get('source'))} || split fragment recovered: {name}"
                ).strip(" |")
                dropped.append((row.get("company"), row.get("depends_on"), name, "merged into previous row"))
            else:
                dropped.append((row.get("company"), row.get("depends_on"), name, "no matching previous row — text preserved in report only"))
            continue

        out.append(row)

    # 4. DEDUPE. Cleaning the annotations collapses "Carl Zeiss SMT — NON-LISTED"
    #    onto the plain "Carl Zeiss SMT" row that already existed, so the same
    #    relationship is now stated twice. Merge those, keeping the best-sourced
    #    grade and concatenating the citations. Rows that differ on tier are NOT
    #    merged: the same supplier legitimately sits at different tiers depending
    #    on which company you measure from.
    STRENGTH = {"ACTUAL": 3, "GUIDANCE": 2, "REPORTED": 1, "INFERRED": 0}
    merged: dict = {}
    order: list = []
    duplicates = []
    for row in out:
        key = (
            norm(row.get("company")).lower(),
            norm(row.get("depends_on")).lower(),
            norm(row.get("supplier_name")).lower(),
            norm(row.get("tier")),
        )
        if key in merged:
            first = merged[key]
            duplicates.append((row.get("company"), row.get("depends_on"), row.get("supplier_name")))
            src_a, src_b = norm(first.get("source")), norm(row.get("source"))
            if src_b and src_b not in src_a:
                first["source"] = f"{src_a} || {src_b}".strip(" |")
            if STRENGTH.get(norm(row.get("confidence")).upper(), 0) > STRENGTH.get(
                norm(first.get("confidence")).upper(), 0
            ):
                first["confidence"] = row.get("confidence")
            for col in ("supplier_ticker", "supplier_listed", "country"):
                if not norm(first.get(col)) and norm(row.get(col)):
                    first[col] = row.get(col)
            continue
        merged[key] = row
        order.append(key)
    out = [merged[k] for k in order]

    print(f"rows in:      {len(rows)}")
    print(f"rows out:     {len(out)}")
    print(f"names cleaned: {len(cleaned)}")
    print(f"rows dropped:  {len(dropped)}")
    print(f"duplicates merged: {len(duplicates)}")

    if args.dry_run:
        print("\n--- would clean ---")
        for co, before, after, note in cleaned:
            print(f"  {co}: {before!r} -> {after!r}   [{note}]")
        print("\n--- would drop ---")
        for co, dep, name, how in dropped:
            print(f"  {co} / {dep}: {name!r}  ({how})")
        print("\nDry run. Nothing written.")
        return

    stamp = date.today().isoformat()
    backup = path.with_suffix(path.suffix + f".bak-{stamp}")
    shutil.copy2(path, backup)

    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        for row in out:
            w.writerow({k: row.get(k, "") for k in COLUMNS})

    report = path.parent / f"_repair-report-{stamp}.md"
    lines = [
        f"# Graph CSV repair — {stamp}",
        "",
        f"Source file: `{path.name}`  ",
        f"Backup: `{backup.name}`",
        "",
        f"- rows before: **{len(rows)}**",
        f"- rows after: **{len(out)}**",
        f"- supplier names cleaned: **{len(cleaned)}**",
        f"- rows dropped: **{len(dropped)}**",
        "",
        "Cause: comma-separated prose was written into `supplier_name` and then split",
        "across rows by the CSV writer, turning descriptive text into fake suppliers.",
        "",
        "## Names cleaned (row kept)",
        "",
        "| Company | Before | After | Note moved to source |",
        "|---|---|---|---|",
    ]
    for co, before, after, note in cleaned:
        lines.append(f"| {co} | {before} | {after} | {note} |")
    lines += [
        "",
        "## Rows dropped (text preserved in the preceding row's source)",
        "",
        "| Company | Chokepoint | Dropped text | Disposition |",
        "|---|---|---|---|",
    ]
    for co, dep, name, how in dropped:
        lines.append(f"| {co} | {dep} | {name} | {how} |")
    lines += [
        "",
        "## Duplicate relationships merged",
        "",
        "Cleaning the annotations collapsed rows like `Carl Zeiss SMT — NON-LISTED`",
        "onto the plain `Carl Zeiss SMT` row that already existed. Citations were",
        "concatenated and the best-sourced evidence grade kept.",
        "",
        "| Company | Chokepoint | Supplier |",
        "|---|---|---|",
    ]
    for co, dep, sup in duplicates:
        lines.append(f"| {co} | {dep} | {sup} |")
    lines += [
        "",
        "## Left deliberately alone",
        "",
        "Category descriptors such as \"Chinese magnet makers\" and \"Chinese SoC vendors\"",
        "are intentional stand-ins for non-listed groups and were not modified.",
        "",
    ]
    report.write_text("\n".join(lines), encoding="utf-8")

    print(f"\nwrote  {path}")
    print(f"backup {backup}")
    print(f"report {report}")


if __name__ == "__main__":
    main()
