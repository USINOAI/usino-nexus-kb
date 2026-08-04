---
Title: NVIDIA — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, AI Chips & Compute, GPU / AI Accelerators, NVDA
---

# NVIDIA — upstream chokepoint map

**Ticker:** NVDA · **Sector:** AI Chips & Compute · **Sub-segment:** GPU / AI Accelerators · **Jurisdiction:** USA

**Supply chain role:** Fabless AI accelerator designer

**Chokepoint hypothesis:** Not itself a chokepoint — sits downstream of TSMC CoWoS packaging and SK Hynix/Micron HBM supply; CUDA software lock-in is the demand-side moat.

5 mapped chokepoints. Tier 1 sits directly upstream of NVIDIA; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## CoWoS advanced packaging capacity

`N-C1` · **Tier 1** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

**Named suppliers:** TSMC (primary); Amkor, ASE/SPIL (outsourced)

**Concentration:** TSMC dominant; NVIDIA reported to hold >60% of available CoWoS capacity; sold out through 2026

**Substitutability and lead time:** Very low. New packaging lines are 18-24mo + heavy capex

**Geographic concentration:** Taiwan (primary), Arizona/Korea partial

**Watch for:** CoWoS allocation reshuffle or OSAT outsourcing share change

**Basis / source:** TrendForce Dec 2025; Digitimes Dec 2025


## HBM3e/HBM4 supply

`N-C2` · **Tier 1** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** SK Hynix, Samsung, Micron

**Concentration:** Three global suppliers only

**Substitutability and lead time:** Low. Qualification cycles 9-18mo per stack generation

**Geographic concentration:** South Korea, USA, Japan (materials)

**Watch for:** HBM4 qualification pass/fail at any of the three

**Basis / source:** Industry-standard supplier set


## Leading-edge foundry (N3/N2)

`N-C4` · **Tier 1** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** TSMC

**Concentration:** Effective monopoly at leading edge for AI accelerators

**Substitutability and lead time:** None near-term. Samsung/Intel not qualified at volume for this workload

**Geographic concentration:** Taiwan

**Watch for:** N2 ramp slip; Taiwan geopolitical event

**Basis / source:** Well-established; TSMC 2026 allocation reported sold out


## ABF substrate + ABF film

`N-C3` · **Tier 2** · Severity **High** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Unimicron (~22%), Ibiden, Shinko, AT&S, Nan Ya PCB

**Non-listed / low-disclosure:** Ajinomoto Fine-Techno (unlisted subsidiary of Ajinomoto Co.). Dominant at the film layer; >95% reported (press, not filing). Sekisui Chemical is the only qualified alternative in volume production. Duopoly, not monopoly.

**Concentration:** Top 3 substrate makers ~75%. At the film layer: two suppliers in volume production worldwide - Ajinomoto overwhelmingly dominant, Sekisui Chemical the only qualified alternative. CORRECTED 31 Jul 2026 from 'near-single-source', which the P1-A verification superseded.

**Substitutability and lead time:** Very low at the film layer. A qualified alternative DOES exist (Sekisui NX04H at HVM, customers TOPPAN and Nan Ya PCB), so 'no qualified substitute' is too strong. OPEN: whether Sekisui is qualified at leading-edge layer counts / NVIDIA-AMD-class packages, or only networking-tier. That question decides severity for all six affected names.

**Geographic concentration:** Japan (film), Taiwan/Japan/Austria (substrate)

**Watch for:** Ajinomoto capacity announcement; substrate maker capex or yield disclosure

**Basis / source:** SEVERITY LOWERED Critical -> High, 31 Jul 2026 (Doug). A qualified alternative in volume production means this is not a single-source chokepoint. Elsewhere in this map Critical is reserved for effectively single-source layers - Lumentum 200G EML, Mitsui EUV pellicle, Namics MR-MUF, China ~90% of RE refining. ABF does not meet that bar. It also brings N-C3 into line with AMD-C4, the same chokepoint at the same tier, already rated High. || REFRAMED 31 Jul 2026 (Thread A P1-A). Ajinomoto ASV Report 2025 ('top runner', no share disclosed) - PRIMARY. TrendForce 8 May 2026 citing Ajinomoto press release and TV Asahi (>95%). Sekisui Chemical HPPC product page (only alternative in mass production; HVM status; TOPPAN and Nan Ya PCB named) - PRIMARY. Prior basis was QYResearch/IntelMarketResearch, whose reports are titled 'Ajinomoto Build-up Film Market' - i.e. sizing one firm's product line then reporting its share of it. Circular; do not rely on.


## HBM TC bonder equipment

`N-C5` · **Tier 2** · Severity **High** · Evidence **REPORTED** — trade press or third-party report

**Named suppliers:** Hanmi Semiconductor (~71% share Q3 2025), Hanwha, ASMPT

**Concentration:** Single supplier >70% of TC bonder market

**Substitutability and lead time:** Low. Hybrid bonding transition not commercialised; Hanmi 2nd-gen HB slated 2027

**Geographic concentration:** South Korea

**Watch for:** Hanmi order book or hybrid-bonder delivery slip

**Basis / source:** Hanmi/TechInsights via Semiconductor Digest & TrendForce 2026


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.