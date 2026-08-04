---
Title: UBTECH Robotics — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, Humanoid Robotics & Physical AI, Humanoid OEM, 9880.HK
---

# UBTECH Robotics — upstream chokepoint map

**Ticker:** 9880.HK · **Sector:** Humanoid Robotics & Physical AI · **Sub-segment:** Humanoid OEM · **Jurisdiction:** China

**Supply chain role:** Pure-play humanoid manufacturer

**Chokepoint hypothesis:** Demand-side anchor; China-listed pure-play, useful lens on the domestic humanoid supply base.

5 mapped chokepoints. Tier 1 sits directly upstream of UBTECH Robotics; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## Harmonic/RV reducers

`UR-C1` · **Tier 1** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Leaderdrive, Harmonic Drive Systems, Zhongda Leader

**Non-listed / low-disclosure:** Chinese reducer supply base below listed tier

**Concentration:** Leaderdrive 30-40% of the China market

**Substitutability and lead time:** Low

**Geographic concentration:** China, Japan

**Watch for:** Reducer allocation or pricing

**Basis / source:** humanoid.guide / market reports 2026


## NdFeB magnets

`UR-C2` · **Tier 1** · Severity **Low** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Chinese magnet makers

**Non-listed / low-disclosure:** Opaque below listed tier

**Concentration:** China dominant — domestic advantage, but export exposure for shipped robots

**Substitutability and lead time:** Low domestically; export-licensed outbound SUBSTITUTION LOCK, verified 30 Jul 2026: high-performance servo magnets need Dy/Tb for coercivity (standard NdFeB loses ~0.65%/degC; Dy lifts the ceiling from ~80degC to >220degC). Industry route is GRAIN BOUNDARY DIFFUSION (GBD) - 70-80% less heavy rare earth, remanence preserved. MOFCOM Announcement No. 56 (suspended by No. 70 to 10 Nov 2026) CONTROLS GBD EQUIPMENT BY NAME, plus strip casters, hydrogen decrepitation furnaces, jet mills, forming presses, vacuum sintering furnaces and cutting/grinding - 26 equipment categories. So the regime is layered: MATERIAL (No. 18, LIVE) / EQUIPMENT (No. 56, suspended) / TECHNOLOGY (No. 62, suspended) / FINISHED GOODS (No. 61, suspended) / TOOLING (No. 55, suspended). Only the material layer is live. Building magnet capacity outside China is the escape route today, and No. 56 is what closes it. Over a 2-year horizon Nos. 56 and 62 matter MORE than No. 18. CAVEAT: the lock assumes no ready non-Chinese GBD/magnet-line equipment supply - asserted, not yet verified (open item 13).

**Geographic concentration:** China

**Watch for:** Export licence for robots containing Dy/Tb magnets. Covered by RE alert family.

**Basis / source:** MOFCOM regime. Note 30 Jul 2026: key escalation path is licensing extended to FINISHED GOODS containing Dy/Tb magnets above a content threshold - would capture shipped robots directly. Listed as a RED escalation condition in the RE spec. | SEVERITY REVISED Medium->Low 30 Jul 2026. ERROR CORRECTED: this entry previously claimed export-licence exposure on shipped robots containing Dy/Tb magnets. WRONG - assembled products are EXPLICITLY EXEMPT under MOFCOM's Sept 2025 clarifications. Shipped robots are NOT captured under the live perimeter. BUT this is precisely where No. 61 bites: a >=0.1% de minimis rule on foreign-made goods would capture finished robots, moving UBTECH from Low to Critical in one step. Highest regime-sensitivity of the seven. PERIMETER VERIFIED 30 Jul 2026: No. 18 controls raw/intermediate materials only; magnets limited to samarium-cobalt and Tb/Dy-containing NdFeB. General NdFeB NOT controlled. MOFCOM Sept 2025 clarifications EXEMPT motor components (rotors, stators, sensors), assembled products, consumer goods, catalysts, phosphors. Suspended by Announcement No. 70 (7 Nov 2025) through 10 Nov 2026 inclusive: Nos. 55, 56, 57, 58, 61, 62. No. 57 = Ho/Er/Tm/Eu/Yb. No. 61 = >=0.1% de minimis on FOREIGN-MADE goods. No. 62 = technology. KEY: No. 61 is what closes the finished-goods exemption. Exposure ordering under the live perimeter is near-inverse to the ordering if No. 61 resumes on 11 Nov 2026. Rate names on IMPORTED Tb/Dy-grade input, never on magnet usage.


## AI compute (edge inference)

`UR-C3` · **Tier 1** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** NVIDIA (Jetson/Thor), domestic Chinese SoCs

**Concentration:** US export controls restrict advanced AI compute into China

**Substitutability and lead time:** Medium. Domestic substitutes improving but behind

**Geographic concentration:** USA, China, Taiwan

**Watch for:** BIS rule change on edge AI compute to China

**Basis / source:** Public export-control record


## Planetary roller screws

`UR-C4` · **Tier 2** · Severity **High** · Evidence **REPORTED** — trade press or third-party report

> ⛔ **DO NOT PUBLISH.** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md.

**Named suppliers:** SKF, Rollvis, Ewellix (Schaeffler Group), GSA (Swiss), Creative Motion Control, Moog, Bosch Rexroth, August Steinmeyer, Power Jacks, Nook Industries; KGG and domestic Chinese entrants

**Non-listed / low-disclosure:** Rollvis SA - NON-LISTED (Swiss). Ewellix is NOT non-listed: now Schaeffler Group (SKF carve-out to Triton 2018, Schaeffler completed 3 Jan 2023).

**Concentration:** SUPPLIER SET WIDENED 31 Jul 2026, concentration figure NOT changed - Thread A owns that claim. Two things worth flagging to Thread A: (1) an aggregator source gives 'GSA, Rollvis, Ewellix and others >70% combined', which is a different cut from the map's '3-4 firms, ~80%'; (2) the named-supplier set above is much wider than 3-4 firms, which is evidence AGAINST the P1 claim as currently worded. The narrower real constraint may be process, not firms: sub-5-micron precision grinding and heat treatment reportedly concentrated at Nippon Thompson and Rollvis, running near capacity

**Substitutability and lead time:** Very low at high precision. Inverted planetary roller screws for humanoids: ~1,551,060 sets globally in 2025 at ~US$277.78 average MECHANISM LINK (added 31 Jul 2026): the binding constraint is the PROCESS tier, not the firm count. Sub-5-micron precision thread grinding and controlled heat treatment - reportedly concentrated at Nippon Thompson and Rollvis, near capacity - is the capability that produces C3-and-finer grade. See Non-Listed Targets row 19 (United Grinding / Studer, precision cylindrical grinding machines) and row 5 (Rollvis SA). C3 is the output spec; grinding and heat treatment are the cause. PRICE-TIER TENSION, flagged 31 Jul 2026: UR-C4 carries an aggregator figure of ~US$277.78 per set (1,551,060 sets, 2025). Tesla's GSA screws are put at $1,350-2,700 each - 5 to 10x higher. Either the aggregator is pricing a commodity tier while GSA prices the C3 tier, which would be direct EVIDENCE FOR the two-tier thesis, or one figure is wrong. Do not cite both without resolving. This is a cheap, high-value check.

**Geographic concentration:** Switzerland, Sweden, China

**Watch for:** Domestic Chinese screw qualification at a humanoid OEM; sub-5-micron grinding capacity addition

**Basis / source:** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md. || PW Consulting and IntelMarketResearch planetary-roller-screw reports 2026; openPR release on inverted PRS for humanoids, 31 Jul 2026. All aggregator quality. CROSS-REF: Thread A Verification Queue P1 item 2 owns the concentration claim - this row deliberately does not resolve it


## High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path

`UR-C5` · **Tier 2** · Severity **Medium** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** CATL (300750.SZ), Farasis (688567.SH), WeLion (unlisted); semi-solid and all-solid-state developers

**Concentration:** China dominant in advanced cell chemistry. CATL all-solid-state for humanoid robots ~450 Wh/kg; Farasis sulfide ASSB up to 520 Wh/kg

**Substitutability and lead time:** Not binding TODAY - mainstream humanoid cells run 250-300 Wh/kg (Optimus, Unitree H1, UBTECH Walker X), just BELOW the threshold. Humanoids prioritise POWER density (3C-5C continuous, 10C-20C peak) over energy density, which is why the current generation sits where it does. BUT the industry upgrade path runs straight through the threshold: semi-solid 350-400 Wh/kg, CATL ASSB ~450, Farasis ~520. MOFCOM No. 58 applies at BOTH cell and pack level (电芯和电池组), verified 30 Jul 2026 - so the cell threshold is what binds, since packs always trail cells.

**Geographic concentration:** China

**Watch for:** Resumption of No. 58 on 11 Nov 2026; or any humanoid platform adopting >=300 Wh/kg cells, which moves it from forward watch to live exposure. Covered by RE alert family Channel C.

**Basis / source:** MOFCOM Announcement No. 58 (9 Oct 2025) - Li batteries >=300 Wh/kg, manufacturing equipment, cathode precursors (NCM/NCA hydroxides, LFP), artificial graphite anode. SUSPENDED by Announcement No. 70 (7 Nov 2025) through 10 Nov 2026 inclusive; conditional resumption 11 Nov 2026. Threshold confirmed to apply at both cell and pack level, MOFCOM text, verified 30 Jul 2026. STRUCTURAL PATTERN: like No. 56 with grain boundary diffusion equipment, this control captures the UPGRADE ROUTE rather than the current state. ASYMMETRY: CATL and Farasis are Chinese, so Chinese humanoid makers retain access to next-generation cells while others face licensing on the transition. NOT a live constraint - forward watch only while suspended.


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.