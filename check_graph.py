#!/usr/bin/env python3
"""
USINO supply chain graph — consistency checker and merger.

Usage:
    python3 check_graph.py GRAPH/*.csv
    python3 check_graph.py GRAPH/*.csv --merge GRAPH/dependencies.csv

Stdlib only. No installs needed.
"""

import csv
import sys
import re
from collections import defaultdict

COLUMNS = [
    "company", "ticker", "depends_on", "dependency_type", "supplier_name",
    "supplier_listed", "supplier_ticker", "country", "tier", "confidence",
    "source", "date_added",
]

VALID_TYPE = {"component", "material", "equipment", "assembly", "logistics"}
VALID_CONF = {"ACTUAL", "GUIDANCE", "REPORTED", "INFERRED"}
VALID_TIER = {"1", "2", "3"}
VALID_LISTED = {"Y", "N"}

# NVDA / 2330.TW / 005930.KS / 0700.HK / 001308.SZ / 4587.T
TICKER_RE = re.compile(r"^[A-Z0-9]{1,6}(\.[A-Z]{1,2})?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def norm(s):
    return (s or "").strip()


def key(s):
    """Loose key for spotting the same thing spelled differently."""
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def load(paths):
    rows = []
    for p in paths:
        try:
            with open(p, newline="", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
                if missing:
                    print(f"  !! {p}: missing columns: {', '.join(missing)}")
                    continue
                for i, r in enumerate(reader, start=2):
                    r["_file"] = p
                    r["_line"] = i
                    rows.append(r)
        except FileNotFoundError:
            print(f"  !! {p}: file not found")
    return rows


def check(rows):
    problems = defaultdict(list)

    # field-level validation
    for r in rows:
        where = f"{r['_file']}:{r['_line']}"
        if not norm(r["company"]):
            problems["Missing company"].append(where)
        if not norm(r["depends_on"]):
            problems["Missing depends_on"].append(where)
        if not norm(r["source"]):
            problems["Missing source"].append(f"{where}  {norm(r['company'])} -> {norm(r['depends_on'])}")

        t = norm(r["dependency_type"]).lower()
        if t and t not in VALID_TYPE:
            problems["Bad dependency_type"].append(f"{where}  '{t}'")

        c = norm(r["confidence"]).upper()
        if c and c not in VALID_CONF:
            problems["Bad confidence"].append(f"{where}  '{c}'")

        if norm(r["tier"]) and norm(r["tier"]) not in VALID_TIER:
            problems["Bad tier"].append(f"{where}  '{norm(r['tier'])}'")

        li = norm(r["supplier_listed"]).upper()
        if li and li not in VALID_LISTED:
            problems["Bad supplier_listed"].append(f"{where}  '{li}'")

        for col in ("ticker", "supplier_ticker"):
            v = norm(r[col])
            if v and not TICKER_RE.match(v):
                problems[f"Odd {col} format"].append(f"{where}  '{v}'")

        if li == "Y" and not norm(r["supplier_ticker"]):
            problems["Listed supplier with no ticker"].append(f"{where}  {norm(r['supplier_name'])}")

        d = norm(r["date_added"])
        if d and not DATE_RE.match(d):
            problems["Bad date_added"].append(f"{where}  '{d}'")

    # one company name -> many tickers, and vice versa
    name_to_tickers = defaultdict(set)
    ticker_to_names = defaultdict(set)
    for r in rows:
        for name_col, tick_col in (("company", "ticker"), ("supplier_name", "supplier_ticker")):
            n, t = norm(r[name_col]), norm(r[tick_col])
            if n and t:
                name_to_tickers[key(n)].add(t)
                ticker_to_names[t].add(n)

    for k, tickers in name_to_tickers.items():
        if len(tickers) > 1:
            problems["Same company, different tickers"].append(f"{k}: {', '.join(sorted(tickers))}")
    for t, names in ticker_to_names.items():
        if len(names) > 1:
            problems["Same ticker, different spellings"].append(f"{t}: {' | '.join(sorted(names))}")

    # inconsistent spelling of the same chokepoint
    dep_spellings = defaultdict(set)
    for r in rows:
        d = norm(r["depends_on"])
        if d:
            dep_spellings[key(d)].add(d)
    for k, spellings in dep_spellings.items():
        if len(spellings) > 1:
            problems["Same chokepoint, different spellings"].append(" | ".join(sorted(spellings)))

    # duplicates
    seen = defaultdict(list)
    for r in rows:
        k = (key(r["company"]), key(r["depends_on"]), key(r["supplier_name"]))
        seen[k].append(f"{r['_file']}:{r['_line']}")
    for k, locs in seen.items():
        if len(locs) > 1:
            problems["Duplicate relationship"].append(f"{k[0]} -> {k[1]}  ({', '.join(locs)})")

    return problems


def summarise(rows):
    conf = defaultdict(int)
    companies = set()
    for r in rows:
        conf[norm(r["confidence"]).upper() or "(blank)"] += 1
        if norm(r["company"]):
            companies.add(key(r["company"]))
    print(f"\n  {len(rows)} rows across {len(companies)} companies")
    for c in ("ACTUAL", "GUIDANCE", "REPORTED", "INFERRED"):
        if conf.get(c):
            pct = 100 * conf[c] / len(rows)
            print(f"    {c:<9} {conf[c]:>4}  ({pct:.0f}%)")
    other = {k: v for k, v in conf.items() if k not in VALID_CONF}
    for k, v in other.items():
        print(f"    {k:<9} {v:>4}")


def merge(rows, out):
    best = {}
    rank = {"ACTUAL": 4, "GUIDANCE": 3, "REPORTED": 2, "INFERRED": 1}
    for r in rows:
        k = (key(r["company"]), key(r["depends_on"]), key(r["supplier_name"]))
        cur = best.get(k)
        if cur is None or rank.get(norm(r["confidence"]).upper(), 0) > rank.get(norm(cur["confidence"]).upper(), 0):
            best[k] = r
    ordered = sorted(best.values(), key=lambda r: (norm(r["company"]).lower(), norm(r["depends_on"]).lower()))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in ordered:
            w.writerow({c: norm(r[c]) for c in COLUMNS})
    print(f"\n  Merged {len(rows)} rows -> {len(ordered)} unique, written to {out}")


def main():
    args = [a for a in sys.argv[1:]]
    out = None
    if "--merge" in args:
        i = args.index("--merge")
        try:
            out = args[i + 1]
        except IndexError:
            print("  !! --merge needs an output filename")
            return
        args = args[:i] + args[i + 2:]

    if not args:
        print(__doc__)
        return

    print(f"\nChecking {len(args)} file(s)...")
    rows = load(args)
    if not rows:
        print("  No readable rows found.")
        return

    summarise(rows)
    problems = check(rows)

    if not problems:
        print("\n  No problems found.\n")
    else:
        total = sum(len(v) for v in problems.values())
        print(f"\n  {total} thing(s) to look at:\n")
        for label in sorted(problems):
            items = problems[label]
            print(f"  {label}  ({len(items)})")
            for it in items[:12]:
                print(f"      {it}")
            if len(items) > 12:
                print(f"      ... and {len(items) - 12} more")
            print()

    if out:
        merge(rows, out)


if __name__ == "__main__":
    main()
