---
Title: Tuopu Group — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, Humanoid Robotics & Physical AI, Mechanical Motion Assembly, 601689.SH
---

# Tuopu Group — upstream chokepoint map

**Ticker:** 601689.SH · **Sector:** Humanoid Robotics & Physical AI · **Sub-segment:** Mechanical Motion Assembly · **Jurisdiction:** China

**Supply chain role:** Integrated actuator/assembly supplier

**Chokepoint hypothesis:** Emerging assembly-level chokepoint — integrated motion modules reduce OEM sourcing options to fewer suppliers.

4 mapped chokepoints. Tier 1 sits directly upstream of Tuopu Group; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## Planetary roller screws

`TG-C1` · **Tier 1** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

> ⛔ **DO NOT PUBLISH.** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md.

**Named suppliers:** Domestic Chinese + Rollvis/Ewellix (Schaeffler Group)/SKF

**Non-listed / low-disclosure:** Non-listed Swiss/Swedish specialists at the high end

**Concentration:** Few global suppliers at scale

**Substitutability and lead time:** Very low MECHANISM LINK (added 31 Jul 2026): the binding constraint is the PROCESS tier, not the firm count. Sub-5-micron precision thread grinding and controlled heat treatment - reportedly concentrated at Nippon Thompson and Rollvis, near capacity - is the capability that produces C3-and-finer grade. See Non-Listed Targets row 19 (United Grinding / Studer, precision cylindrical grinding machines) and row 5 (Rollvis SA). C3 is the output spec; grinding and heat treatment are the cause.

**Geographic concentration:** Switzerland, Sweden, China

**Watch for:** Screw supply or domestic qualification news

**Basis / source:** DO NOT PUBLISH - roller screw concentration figure falsified 31 Jul 2026, under reverification. See VERIFICATION_P1_findings.md. || Trade press (secondary)


## NdFeB magnets

`TG-C2` · **Tier 1** · Severity **Medium** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Chinese magnet makers

**Non-listed / low-disclosure:** Opaque below listed tier

**Concentration:** China >90%

**Substitutability and lead time:** Very low SUBSTITUTION LOCK, verified 30 Jul 2026: high-performance servo magnets need Dy/Tb for coercivity (standard NdFeB loses ~0.65%/degC; Dy lifts the ceiling from ~80degC to >220degC). Industry route is GRAIN BOUNDARY DIFFUSION (GBD) - 70-80% less heavy rare earth, remanence preserved. MOFCOM Announcement No. 56 (suspended by No. 70 to 10 Nov 2026) CONTROLS GBD EQUIPMENT BY NAME, plus strip casters, hydrogen decrepitation furnaces, jet mills, forming presses, vacuum sintering furnaces and cutting/grinding - 26 equipment categories. So the regime is layered: MATERIAL (No. 18, LIVE) / EQUIPMENT (No. 56, suspended) / TECHNOLOGY (No. 62, suspended) / FINISHED GOODS (No. 61, suspended) / TOOLING (No. 55, suspended). Only the material layer is live. Building magnet capacity outside China is the escape route today, and No. 56 is what closes it. Over a 2-year horizon Nos. 56 and 62 matter MORE than No. 18. CAVEAT: the lock assumes no ready non-Chinese GBD/magnet-line equipment supply - asserted, not yet verified (open item 13).

**Geographic concentration:** China

**Watch for:** Licence regime change. Covered by RE alert family.

**Basis / source:** MOFCOM regime. Note 30 Jul 2026: Announcement 18 live since Apr 2025. China-domiciled - RELATIVELY ADVANTAGED by tightening. | SEVERITY REVISED High->Medium 30 Jul 2026: OUTSIDE the live perimeter, same reasoning as Sanhua. PERIMETER VERIFIED 30 Jul 2026: No. 18 controls raw/intermediate materials only; magnets limited to samarium-cobalt and Tb/Dy-containing NdFeB. General NdFeB NOT controlled. MOFCOM Sept 2025 clarifications EXEMPT motor components (rotors, stators, sensors), assembled products, consumer goods, catalysts, phosphors. Suspended by Announcement No. 70 (7 Nov 2025) through 10 Nov 2026 inclusive: Nos. 55, 56, 57, 58, 61, 62. No. 57 = Ho/Er/Tm/Eu/Yb. No. 61 = >=0.1% de minimis on FOREIGN-MADE goods. No. 62 = technology. KEY: No. 61 is what closes the finished-goods exemption. Exposure ordering under the live perimeter is near-inverse to the ordering if No. 61 resumes on 11 Nov 2026. Rate names on IMPORTED Tb/Dy-grade input, never on magnet usage.


## Customer concentration

`TG-C4` · **Tier 1** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Tesla and Chinese humanoid OEMs

**Concentration:** Concentrated order book

**Substitutability and lead time:** N/A

**Geographic concentration:** USA, China

**Watch for:** Order book disclosure

**Basis / source:** Analyst hypothesis


## Gear grinding - CNC control and measurement layer (not the machine)

`TG-C3` · **Tier 2** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

**Named suppliers:** Machine: Qinchuan 000837.SZ, Zhongda Chuangyuan, Shanghai Xinghe, Chongqing Machine Tool, Reishauer, Kapp Niles, Gleason, Klingelnberg | CNC: FANUC, Siemens, Mitsubishi, Heidenhain, Huazhong CNC 300161.SZ | Scales: Heidenhain, Renishaw

**Non-listed / low-disclosure:** Heidenhain (NON-LISTED, Germany) - appears at TWO depths of this map: robot joint encoders AND linear scales inside the machines that grind the reducers. Reishauer, Kapp Niles (NON-LISTED). Shanghai Xinghe, Zhongda Chuangyuan (NON-LISTED China, domestically dominant, no English coverage).

**Concentration:** THREE-LAYER STRUCTURE, resolved Jul 2026. MACHINE LAYER - China is dominant, not dependent: Qinchuan ~60% domestic share with sub-1-micron profile deviation, already supplying BYD and Tesla reducer lines; Zhongda Chuangyuan is the world's THIRD company able to build five-axis fully-CNC spiral bevel gear grinders, breaking the Gleason/Klingelnberg duopoly; Shanghai Xinghe reaches accuracy grade 1 approaching grade 0 and has internalised spindles, indexing shafts, dressing shafts and servo tailstocks. CONTROL LAYER - this is the chokepoint: high-end CNC systems are ~6% domestic, the lowest single link in the chain; FANUC, Siemens, Mitsubishi and Heidenhain hold 75-80% globally, 90%+ including white-label. MEASUREMENT LAYER - Heidenhain plus Renishaw hold close to 90% of global high-end linear scales.

**Substitutability and lead time:** The binding constraint is NOT the machine and NOT any single part. It is the integrated system: an incumbent machine is calibrated at the factory using Heidenhain scales and Siemens CNCs, with error-compensation algorithms co-developed across all three engineering teams. Buying equivalent components does not buy that integration. Chinese sources independently describe linear scales as the hardest upstream link to break.

**Geographic concentration:** Switzerland, Germany, Italy

**Watch for:** Primary trigger: a domestic machine + domestic CNC + domestic linear scale combination achieving certified top-grade accuracy. Secondary: Huazhong CNC share rising above ~15% in high-end 5-axis. Tertiary: MIIT 2025-2027 programme milestone, or any export restriction on CNC systems or linear scales to China - which would bite far harder than a machine-level curb.

**Basis / source:** Chinese trade press, securities research and company sources, Jul 2026. Machine-layer shares and CNC localisation rates as cited. 'Ecosystem trust gap' framing contributed by Doug (USINO).


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.