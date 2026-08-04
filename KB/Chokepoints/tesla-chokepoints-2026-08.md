---
Title: Tesla — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, Humanoid Robotics & Physical AI, Humanoid OEM / Integrator, TSLA
---

# Tesla — upstream chokepoint map

**Ticker:** TSLA · **Sector:** Humanoid Robotics & Physical AI · **Sub-segment:** Humanoid OEM / Integrator · **Jurisdiction:** USA

**Supply chain role:** Vertically integrated OEM (Optimus)

**Chokepoint hypothesis:** Demand-side anchor; upstream exposure runs through actuator/gear/sensor suppliers mapped under this program.

6 mapped chokepoints. Tier 1 sits directly upstream of Tesla; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## Planetary roller screws

`T-C1` · **Tier 1** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

> ⛔ **DO NOT PUBLISH.** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md.

**Named suppliers:** SKF, Rollvis, Ewellix (Schaeffler Group), GSA (Swiss), Bosch Rexroth

**Non-listed / low-disclosure:** Rollvis SA (NON-LISTED, Swiss); Ewellix (Schaeffler Group - NO LONGER non-listed; SKF carve-out to Triton 2018, acquired by Schaeffler AG, completed 3 Jan 2023, EUR582m); Bosch Rexroth (Bosch is non-listed). Reported ~80% combined share across Rollvis/GSA (Swiss)/Rexroth/Ewellix

**Concentration:** Only a handful of firms can make these at scale UNIT COUNT AND COST, added 31 Jul 2026 (Thread A): Optimus uses 14 planetary roller screws - the linear actuators only. Tesla-disclosed via RE-001: ~42 actuators total, 28 rotary + 14 linear, and only the linear ones take screws. Wuzhou Xinchun's own placement maths implies ~12 per robot, corroborating 14. Named part GSA RGTI 12.8 at ~$1,350-2,700 each, roughly 19% of total robot cost. ATTRIBUTION: teardown and trade analysis, NOT Tesla-stated. GSA is SWISS, not German.

**Substitutability and lead time:** Very low. Grinding machines run $2-5m each with ~18-month lead times; Optimus lead times reported at 26 weeks in 2023 MECHANISM LINK (added 31 Jul 2026): the binding constraint is the PROCESS tier, not the firm count. Sub-5-micron precision thread grinding and controlled heat treatment - reportedly concentrated at Nippon Thompson and Rollvis, near capacity - is the capability that produces C3-and-finer grade. See Non-Listed Targets row 19 (United Grinding / Studer, precision cylindrical grinding machines) and row 5 (Rollvis SA). C3 is the output spec; grinding and heat treatment are the cause. PRICE-TIER TENSION, flagged 31 Jul 2026: UR-C4 carries an aggregator figure of ~US$277.78 per set (1,551,060 sets, 2025). Tesla's GSA screws are put at $1,350-2,700 each - 5 to 10x higher. Either the aggregator is pricing a commodity tier while GSA prices the C3 tier, which would be direct EVIDENCE FOR the two-tier thesis, or one figure is wrong. Do not cite both without resolving. This is a cheap, high-value check.

**Geographic concentration:** Switzerland, Sweden, Germany

**Watch for:** Roller screw lead-time change; new entrant qualification

**Basis / source:** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md. || Trade press (Fast Company, IntelMarketResearch, KGG) — secondary; strong candidate for primary verification


## NdFeB magnets containing dysprosium/terbium

`T-C2` · **Tier 1** · Severity **High** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** JL Mag, Ningbo Yunsheng, Zhenghai, Shin-Etsu, Proterial, TDK

**Non-listed / low-disclosure:** Multiple Chinese magnet makers with thin English-language disclosure

**Concentration:** China controls >90% of global magnet manufacturing; export licence required for Dy/Tb-containing magnets

**Substitutability and lead time:** Very low. Optimus needs ~3.5kg of high-performance NdFeB per unit; 40+ servo motors at 50-100g each SUBSTITUTION LOCK, verified 30 Jul 2026: high-performance servo magnets need Dy/Tb for coercivity (standard NdFeB loses ~0.65%/degC; Dy lifts the ceiling from ~80degC to >220degC). Industry route is GRAIN BOUNDARY DIFFUSION (GBD) - 70-80% less heavy rare earth, remanence preserved. MOFCOM Announcement No. 56 (suspended by No. 70 to 10 Nov 2026) CONTROLS GBD EQUIPMENT BY NAME, plus strip casters, hydrogen decrepitation furnaces, jet mills, forming presses, vacuum sintering furnaces and cutting/grinding - 26 equipment categories. So the regime is layered: MATERIAL (No. 18, LIVE) / EQUIPMENT (No. 56, suspended) / TECHNOLOGY (No. 62, suspended) / FINISHED GOODS (No. 61, suspended) / TOOLING (No. 55, suspended). Only the material layer is live. Building magnet capacity outside China is the escape route today, and No. 56 is what closes it. Over a 2-year horizon Nos. 56 and 62 matter MORE than No. 18. CAVEAT: the lock assumes no ready non-Chinese GBD/magnet-line equipment supply - asserted, not yet verified (open item 13).

**Geographic concentration:** China

**Watch for:** FIRED RE-001 30 Jul 2026 (AMBER). See ALERT_SPEC_rare_earth.md Channel A/B.

**Basis / source:** SCMP / Global Times Apr 2025 (Optimus explicitly impacted). REGIME VERIFIED against primary Chinese text 30 Jul 2026: MOFCOM Announcement 18 (2025) covering Sm/Gd/Tb/Dy/Lu/Sc/Y and their metals, oxides, alloys, compounds and magnet materials was NEVER suspended - licensing continuous since 4 Apr 2025, and since EXPANDED by later measures. Chokepoint is LIVE, not dormant. Announcements 61 & 62 are suspended 7 Nov 2025 to 10 Nov 2026 INCLUSIVE; resumption, if any, 11 Nov 2026. The Ho/Er/Tm/Eu/Yb measure (which covers equipment and technology, not just materials) is ALREADY IN FORCE and suspended on the same terms and date - it does NOT commence on 10 Nov as previously recorded. 11 Nov 2026 is therefore a single conditional cliff-edge on which the whole suspended package can resume. Resumption is not automatic: the suspension is one half of a mutual stand-down with the US BIS Affiliates Rule. | SEVERITY REVISED Critical->High 30 Jul 2026: inside the perimeter as a magnet buyer, but the ~3.5kg Optimus figure is Apr-2025 press, not a Tesla disclosure (under verification). PERIMETER VERIFIED 30 Jul 2026: No. 18 controls raw/intermediate materials only; magnets limited to samarium-cobalt and Tb/Dy-containing NdFeB. General NdFeB NOT controlled. MOFCOM Sept 2025 clarifications EXEMPT motor components (rotors, stators, sensors), assembled products, consumer goods, catalysts, phosphors. Suspended by Announcement No. 70 (7 Nov 2025) through 10 Nov 2026 inclusive: Nos. 55, 56, 57, 58, 61, 62. No. 57 = Ho/Er/Tm/Eu/Yb. No. 61 = >=0.1% de minimis on FOREIGN-MADE goods. No. 62 = technology. KEY: No. 61 is what closes the finished-goods exemption. Exposure ordering under the live perimeter is near-inverse to the ordering if No. 61 resumes on 11 Nov 2026. Rate names on IMPORTED Tb/Dy-grade input, never on magnet usage. PROVENANCE VERIFIED 30 Jul 2026: the '~3.5kg NdFeB per Optimus, 40+ servo motors at 50-100g' claim is a PRESS-INFERRED ESTIMATE, not Tesla-stated and not teardown-verified. Traced to Global Times 23 Apr 2025 citing Securities Times: a generic 2-4kg humanoid range with the midpoint applied to Optimus illustratively (40 x 87.5g = 3.5kg exactly). No public teardown has weighed Optimus magnet content; Tesla has never published a BOM. SOLID COMPONENT: ~42 actuators (28 rotary + 14 linear) is Tesla-disclosed, so '40+ servo motors' stands. STRONGER EVIDENCE FOR THE EXPOSURE ITSELF: Musk stated on a 2025 earnings call that Optimus production was impacted by the 'magnet issue' and that Tesla was working with China to secure rare-earth export licences - primary, company-sourced, and it establishes the dependency better than any estimated tonnage. PRESENTATION RULE: lead with the Tesla-stated dependency and disclosed actuator count; use ~3.5kg only when flagged as a press estimate; never present it as a BOM fact.


## Rare-earth separation & refining

`T-C3` · **Tier 2** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** China Northern Rare Earth, Shenghe, Lynas, MP Materials

**Non-listed / low-disclosure:** Chinese separation capacity is the true chokepoint and is opaque

**Concentration:** China holds roughly 90% of global separation/refining capacity

**Substitutability and lead time:** Very low. Built over 40 years; not replicable within a price cycle. EU spot dysprosium oxide rose $700 to $1,100/kg in 2H25; terbium oxide $2,000 to $4,000

**Geographic concentration:** China

**Watch for:** Channel B: RED at +20% rolling 30d or FOB/ex-works > 1.35x; AMBER at +10%. Evaluated ONLY on the bound reference series (Dy2O3 99.5% ex-works China, SMM primary / CTIA cross-check). NOT BREACHED as at 30 Jul 2026 - the earlier RED was a false positive from mixing price bases and has been withdrawn. See ALERT_LOG.md.

**Basis / source:** Rare Earth Exchanges / Oceanwall 2025-26. PRICE CLAIM CORRECTED 30 Jul 2026: an earlier note here recorded Dy +25.4% during Jul 2026 to ~USD 262/kg. FALSIFIED on verification - no such move on any consistent series. Reference series is dysprosium OXIDE (Dy2O3 99.5% min), EX-WORKS CHINA: USD 191/kg 6 Mar 2026 (SMM), USD 201.41/kg 16 Jul 2026 (CTIA) - about +5% over four months, with March negative. The three figures originally cited were three different products on three different bases (ex-works China oxide, a Northeast Asia regional benchmark, and one figure that could not be relocated). Tb carried at USD 1,179.54/kg domestic and USD 1,483/kg FOB, MEDIUM confidence only - single source, identical to the humanoid index baseline, so not independently corroborated.


## Harmonic and planetary reducers

`T-C4` · **Tier 2** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Harmonic Drive Systems, Nabtesco, Leaderdrive

**Non-listed / low-disclosure:** Chinese reducer makers below the listed tier

**Concentration:** HDS/Nabtesco/Wittenstein/Schaeffler ~55-60% of global harmonic drive revenue

**Substitutability and lead time:** Low. Precision gear capacity expands slowly

**Geographic concentration:** Japan, China

**Watch for:** Reducer capacity or pricing announcement

**Basis / source:** Dataintelo / market reports 2025-26 (secondary)


## Hollow-cup (coreless) motors for dexterous hands

`T-C5` · **Tier 2** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Maxon, Faulhaber (min. diameter 1.9mm), Portescap; Chinese entrants Dingzhi Technology / 鼎智 (automated winding, min. 8mm, to 80,000 rpm), Mingzhi Electric, Hechuan Technology, Topband

**Non-listed / low-disclosure:** Maxon Motor (NON-LISTED, Swiss, ~28% of global revenue share 2024); Faulhaber (NON-LISTED, German family-owned, coreless diagonal winding since 1958); Dingzhi Technology and Mingzhi Electric (China). NAME CORRECTION 31 Jul 2026: previously listed 'Aoyi, Mige' - sources name Dingzhi, Mingzhi and Hechuan

**Concentration:** Two Western private firms lead the high end, but the market splits cleanly by capability: Europe high-end precision, Japan ultra-miniature, China high-volume. Hollow-cup motors are ~47.9% of dexterous-hand module cost, so this is the dominant cost item in the hand

**Substitutability and lead time:** Medium and improving fast - which is why severity is lowered. Chinese entrants report ~Y100/unit against Y4,000+ for German equivalents, and Dingzhi has automated winding production. Market $810m (2025) to $1,505m (2031), 8.7% CAGR

**Geographic concentration:** Switzerland, Germany, China

**Watch for:** A Western humanoid OEM stating it cannot second-source hollow-cup motors; or a Chinese coreless motor passing qualification at a Western OEM

**Basis / source:** IntelMarketResearch coreless-motor-for-dexterous-hand report 2025-32; Yicai Global on domestic substitution; TechBuzzChina 'State of Robot Hands in China'. Secondary. SEVERITY LOWERED 31 Jul 2026: a chokepoint with a rapidly closing 40x cost gap and active domestic substitution is not High


## High-energy-density lithium cells (>=300 Wh/kg) - next-generation upgrade path

`T-C6` · **Tier 2** · Severity **Low** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** CATL (300750.SZ), Farasis (688567.SH), WeLion (unlisted); semi-solid and all-solid-state developers

**Concentration:** China dominant in advanced cell chemistry. CATL all-solid-state for humanoid robots ~450 Wh/kg; Farasis sulfide ASSB up to 520 Wh/kg

**Substitutability and lead time:** Not binding TODAY - mainstream humanoid cells run 250-300 Wh/kg (Optimus, Unitree H1, UBTECH Walker X), just BELOW the threshold. Humanoids prioritise POWER density (3C-5C continuous, 10C-20C peak) over energy density, which is why the current generation sits where it does. BUT the industry upgrade path runs straight through the threshold: semi-solid 350-400 Wh/kg, CATL ASSB ~450, Farasis ~520. MOFCOM No. 58 applies at BOTH cell and pack level (电芯和电池组), verified 30 Jul 2026 - so the cell threshold is what binds, since packs always trail cells. TESLA HEDGE: Optimus runs Tesla 4680 cells from Tesla own supply chain - genuine vertical-integration buffer, the opposite of its magnet position.

**Geographic concentration:** China

**Watch for:** Resumption of No. 58 on 11 Nov 2026; or any humanoid platform adopting >=300 Wh/kg cells, which moves it from forward watch to live exposure. Covered by RE alert family Channel C.

**Basis / source:** MOFCOM Announcement No. 58 (9 Oct 2025) - Li batteries >=300 Wh/kg, manufacturing equipment, cathode precursors (NCM/NCA hydroxides, LFP), artificial graphite anode. SUSPENDED by Announcement No. 70 (7 Nov 2025) through 10 Nov 2026 inclusive; conditional resumption 11 Nov 2026. Threshold confirmed to apply at both cell and pack level, MOFCOM text, verified 30 Jul 2026. STRUCTURAL PATTERN: like No. 56 with grain boundary diffusion equipment, this control captures the UPGRADE ROUTE rather than the current state. ASYMMETRY: CATL and Farasis are Chinese, so Chinese humanoid makers retain access to next-generation cells while others face licensing on the transition. NOT a live constraint - forward watch only while suspended.


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.