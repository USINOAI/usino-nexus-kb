# GRAPH — the USINO supply chain knowledge graph

One row per supplier relationship. `check_graph.py` validates these files.

    python3 check_graph.py GRAPH/*.csv
    python3 check_graph.py GRAPH/*.csv --merge GRAPH/dependencies.csv

## Files

| File | What it holds |
|---|---|
| `chokepoint-map-2026-08-04.csv` | 526 edges across 33 watchlist companies. Seeded from the Physical AI Chokepoint Map |
| `_quarantine-do-not-publish.csv` | 46 edges from rows carrying a DO NOT PUBLISH flag. Never load these into NEXUS |

## The confidence field is evidence grade, not analyst opinion

| Value | Means |
|---|---|
| `ACTUAL` | Filing, company release, or regulator text |
| `GUIDANCE` | Company guidance or forecast |
| `REPORTED` | Trade press or third-party report |
| `INFERRED` | No named source recorded |

Current seed: **16% ACTUAL · 14% REPORTED · 70% INFERRED.**

That 70% is the honest state of the map, and it is the number to drive down. It is not a
reason to distrust the graph — it is the graph telling you where to work.

**Why this matters.** In July 2026 nine chokepoint entries rated High *confidence* were
stress-tested and roughly half the substantive claims needed correction. Confidence recorded
how sure the analyst felt; it did not record whether anything had been checked. This field
replaces it with something a machine can act on.

## The triage rule

Eight errors found in July shared one shape: **a quantity with no primary source.** Firm
counts, market shares, unit counts — all traceable to trade press or commercial market
research, where a headline number is the product being sold.

The tell: when a concentration claim is true, a primary source exists to prove it. Mitsui
genuinely is the sole EUV pellicle maker, and both Mitsui and ASML say so in their own
releases. **Absence of a primary source for a number is itself the warning sign.**

So:

- `ACTUAL` — publishable
- `REPORTED` or `INFERRED` **carrying a number** — never goes client-facing. Usable internally as a lead
- `REPORTED` or `INFERRED` **structural or qualitative** — usable with the sourcing stated plainly

## For the collector agent

New extractions append here as dated CSVs, then `check_graph.py --merge` folds them into a
single deduplicated file. The merge keeps the highest-graded row for each
`(company, depends_on, supplier_name)`, so a later ACTUAL always supersedes an earlier
INFERRED. That is the mechanism by which the graph improves rather than just growing.

Two rules for anything the collector writes:

1. Grade from the source, never from how confident the extraction sounds.
2. When a source justifies a chokepoint with a firm count or a share, ask what the constraint
   actually is. Five times out of six in this map the real answer was a **process tier**, a
   **grade class**, or a **qualification lock** — not a headcount.
