---
Title: Broadcom — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, AI Chips & Compute, Custom ASIC / Networking, AVGO
---

# Broadcom — upstream chokepoint map

**Ticker:** AVGO · **Sector:** AI Chips & Compute · **Sub-segment:** Custom ASIC / Networking · **Jurisdiction:** USA

**Supply chain role:** Fabless ASIC designer, scale-out networking silicon

**Chokepoint hypothesis:** Demand-side anchor; chokepoint exposure runs through the same TSMC/advanced-packaging layer as Nvidia.

5 mapped chokepoints. Tier 1 sits directly upstream of Broadcom; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## CoWoS / advanced packaging

`B-C1` · **Tier 1** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

**Named suppliers:** TSMC, Amkor, ASE/SPIL

**Concentration:** Shares the same constrained pool as NVIDIA

**Substitutability and lead time:** Very low

**Geographic concentration:** Taiwan

**Watch for:** Custom ASIC customer loses packaging allocation

**Basis / source:** TrendForce Dec 2025


## HBM supply for XPU designs

`B-C2` · **Tier 1** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** SK Hynix, Samsung, Micron

**Concentration:** Three suppliers

**Substitutability and lead time:** Low

**Geographic concentration:** Korea/USA

**Watch for:** HBM allocation shift toward merchant GPU vendors

**Basis / source:** Standard supplier set


## EML / DFB laser chips for optical interconnect

`B-C3` · **Tier 2** · Severity **Critical** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Lumentum (only volume supplier of 200G/lane EML), Coherent (6in InP line, Sherman TX), Sumitomo Electric, Mitsubishi Electric, Broadcom in-house

**Non-listed / low-disclosure:** EML epitaxy capacity is concentrated and thinly disclosed

**Concentration:** 200G/lane EML: effectively single-source (Lumentum). NVIDIA has locked Lumentum + Coherent EML capacity under LTAs through CY2027 via a reported ~$4bn commitment. 800G transceiver output running 40-60% below demand through 2027

**Substitutability and lead time:** Very low to 2027. InP epitaxy is capex- and yield-constrained (reported 15-50% wafer yield by generation). No qualified second source at 200G/lane; double-digit 200G EML price increases expected in 2026

**Geographic concentration:** Japan, USA

**Watch for:** 200G/lane EML LTA terms or pricing in Lumentum/Coherent quarterly results; any second-source qualification announcement

**Basis / source:** TrendForce press release 8 Dec 2025 (laser shortage / NVIDIA lock-in); EE Times Asia and SDxCentral coverage of same; Chipstrat 'Lumentum and the Laser Bottleneck'. Secondary but named, dated and mutually corroborating. NOT yet checked against Lumentum/Coherent 10-K LTA disclosure


## ABF substrate + build-up dielectric film

`B-C5` · **Tier 2** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

> ⛔ **DO NOT PUBLISH.** NEW AND PARTLY UNVERIFIED - do not publish until Broadcom-specific substrate suppliers are confirmed.

**Named suppliers:** Unimicron, Ibiden, Shinko, AT&S, Nan Ya PCB (industry-standard set - Broadcom-specific attribution NOT verified)

**Non-listed / low-disclosure:** Ajinomoto Fine-Techno (unlisted subsidiary of Ajinomoto Co.) at the film layer. Dominant; >95% reported (press, not filing). Sekisui Chemical is the only qualified alternative in volume production.

**Concentration:** Top 3 substrate makers ~75%. At the film layer: two suppliers in volume production worldwide, Ajinomoto overwhelmingly dominant. Duopoly, not monopoly.

**Substitutability and lead time:** Very low at the film layer. OPEN: whether Sekisui is qualified at leading-edge layer counts or only networking-tier - the same open question that governs N-C3 and AMD-C4.

**Geographic concentration:** Japan (film), Taiwan/Japan/Austria (substrate)

**Watch for:** Substrate or ABF film lead-time move; Broadcom packaging commentary

**Basis / source:** NEW ROW added 31 Jul 2026 at Doug's instruction. GAP identified by Thread A: Non-Listed Targets row 4 already lists Broadcom among the names Ajinomoto Fine-Techno sits behind, yet Broadcom had no substrate row - the exposure was asserted on the entity tab and absent from the chokepoint map. Film-layer exposure is inferred from that plus Broadcom's FC-BGA custom-ASIC packaging. Broadcom's NAMED substrate suppliers are NOT verified - the set above is the industry-standard one, not a Broadcom disclosure. Confidence deliberately Medium, one notch below N-C3 and AMD-C4. FALSIFIER: any Broadcom disclosure or package teardown showing its XPU/ASIC substrates do not use ABF-class build-up film.


## Low-loss copper-clad laminate (high-speed PCB)

`B-C4` · **Tier 3** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Panasonic (Megtron), Rogers, EMC Taiwan, Shengyi

**Concentration:** Concentrated in top 4 for M8/M9-grade material

**Substitutability and lead time:** Medium. Qualification 6-12mo

**Geographic concentration:** Japan, Taiwan, China

**Watch for:** CCL price or allocation move

**Basis / source:** Analyst hypothesis


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.