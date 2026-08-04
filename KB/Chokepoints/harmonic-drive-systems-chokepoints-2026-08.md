---
Title: Harmonic Drive Systems — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, Humanoid Robotics & Physical AI, Precision Reducers (Strain Wave), 6324.T
---

# Harmonic Drive Systems — upstream chokepoint map

**Ticker:** 6324.T · **Sector:** Humanoid Robotics & Physical AI · **Sub-segment:** Precision Reducers (Strain Wave) · **Jurisdiction:** Japan

**Supply chain role:** Strain wave gear manufacturer

**Chokepoint hypothesis:** Classic mechanical chokepoint — strain wave gear precision manufacturing concentrated among a handful of global makers.

4 mapped chokepoints. Tier 1 sits directly upstream of Harmonic Drive Systems; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## Gear grinding - CNC control and measurement layer (not the machine)

`HD-C1` · **Tier 1** · Severity **Critical** · Evidence **REPORTED** — trade press or third-party report

**Named suppliers:** Machine: Qinchuan 000837.SZ, Zhongda Chuangyuan, Shanghai Xinghe, Chongqing Machine Tool, Reishauer, Kapp Niles, Gleason, Klingelnberg | CNC: FANUC, Siemens, Mitsubishi, Heidenhain, Huazhong CNC 300161.SZ | Scales: Heidenhain, Renishaw

**Non-listed / low-disclosure:** Heidenhain (NON-LISTED, Germany) - appears at TWO depths of this map: robot joint encoders AND linear scales inside the machines that grind the reducers. Reishauer, Kapp Niles (NON-LISTED). Shanghai Xinghe, Zhongda Chuangyuan (NON-LISTED China, domestically dominant, no English coverage).

**Concentration:** THREE-LAYER STRUCTURE, resolved Jul 2026. MACHINE LAYER - China is dominant, not dependent: Qinchuan ~60% domestic share with sub-1-micron profile deviation, already supplying BYD and Tesla reducer lines; Zhongda Chuangyuan is the world's THIRD company able to build five-axis fully-CNC spiral bevel gear grinders, breaking the Gleason/Klingelnberg duopoly; Shanghai Xinghe reaches accuracy grade 1 approaching grade 0 and has internalised spindles, indexing shafts, dressing shafts and servo tailstocks. CONTROL LAYER - this is the chokepoint: high-end CNC systems are ~6% domestic, the lowest single link in the chain; FANUC, Siemens, Mitsubishi and Heidenhain hold 75-80% globally, 90%+ including white-label. MEASUREMENT LAYER - Heidenhain plus Renishaw hold close to 90% of global high-end linear scales.

**Substitutability and lead time:** The binding constraint is NOT the machine and NOT any single part. It is the integrated system: an incumbent machine is calibrated at the factory using Heidenhain scales and Siemens CNCs, with error-compensation algorithms co-developed across all three engineering teams. Buying equivalent components does not buy that integration. Chinese sources independently describe linear scales as the hardest upstream link to break.

**Geographic concentration:** Switzerland, Germany, USA

**Watch for:** Primary trigger: a domestic machine + domestic CNC + domestic linear scale combination achieving certified top-grade accuracy. Secondary: Huazhong CNC share rising above ~15% in high-end 5-axis. Tertiary: MIIT 2025-2027 programme milestone, or any export restriction on CNC systems or linear scales to China - which would bite far harder than a machine-level curb.

**Basis / source:** Chinese trade press, securities research and company sources, Jul 2026. Machine-layer shares and CNC localisation rates as cited. 'Ecosystem trust gap' framing contributed by Doug (USINO).


## Chinese cost competition (demand-side erosion)

`HD-C4` · **Tier 1** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Leaderdrive, Beijing CTKM, Hengfengtai, Zhejiang Laifu

**Non-listed / low-disclosure:** Several Chinese reducer makers below listed tier

**Concentration:** Leaderdrive holds 30-40% of China's harmonic reducer market

**Substitutability and lead time:** N/A — this is share loss, not supply failure. Chinese product at 20-40% lower price

**Geographic concentration:** China

**Watch for:** Chinese reducer design-win at a global humanoid OEM

**Basis / source:** Market reports / humanoid.guide 2026


## Ultra-clean melt practice for flexspline fatigue steel (not the alloy grade)

`HD-C2` · **Tier 2** · Severity **Medium** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Daido Steel, Sanyo Special Steel, Aichi Steel

**Non-listed / low-disclosure:** Japanese special steel makers have thin non-Japanese coverage

**Concentration:** RESTATED 31 Jul 2026: the chokepoint is not the alloy. Flexsplines use high-strength alloy or maraging steel; the binding constraint is melt cleanliness - non-metallic inclusion size and distribution - plus fatigue qualification, because the flexspline is cyclically deformed for its whole service life. Concentration at that cleanliness class is asserted, not measured

**Substitutability and lead time:** Low. Fatigue-critical, long qualification. But 'low substitutability' here rests on the cleanliness claim, which is unverified

**Geographic concentration:** Japan

**Watch for:** Special steel lead time (reported 6-9mo for some precision grades) - figure itself unverified

**Basis / source:** NOT VERIFIED. English web sources give flexspline material class (alloy / maraging steel, per Harmonic Drive technology pages and ScienceDirect composite-flexspline paper) but NO supplier-share data for Daido / Sanyo / Aichi into Harmonic Drive. Searched 31 Jul 2026 - results were steel-stockist SEO. Needs Harmonic Drive Systems 有価証券報告書 and Daido/Sanyo segment reporting. DOUG (Japanese sources)


## Cross-roller bearings

`HD-C3` · **Tier 2** · Severity **Medium** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** THK (RB/RE/RU/RA ultra-thin/XR-J series, used in robotics and humanoids), NSK, SKF, Schaeffler/INA; IKO (Nippon Thompson), Nachi-Fujikoshi, Kaydon, Rotek, RBC in niches

**Non-listed / low-disclosure:** IKO/Nippon Thompson is comparatively thinly covered

**Concentration:** THK + NSK + SKF + Schaeffler ~58-62% of the global crossed-roller-bearing market. That is moderate concentration across four suppliers, not a chokepoint - hence severity lowered. The open question is whether harmonic-reducer-grade thin-section P4/P2 supply is materially narrower than the overall market

**Substitutability and lead time:** Low at reducer-grade precision; moderate at standard grades

**Geographic concentration:** Japan, Sweden, Germany

**Watch for:** Evidence that reducer-grade thin-section crossed-roller supply is narrower than the overall market

**Basis / source:** HTF Market Intelligence and Dataintelo crossed-roller-bearing reports (top-four ~58-62%), IKO International product pages, 31 Jul 2026. Secondary/aggregator quality. SEVERITY LOWERED - four suppliers at ~60% does not support High


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.