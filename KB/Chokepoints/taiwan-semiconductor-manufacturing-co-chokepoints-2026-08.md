---
Title: Taiwan Semiconductor Manufacturing Co. — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, AI Chips & Compute, Foundry / Advanced Packaging, TSM
---

# Taiwan Semiconductor Manufacturing Co. — upstream chokepoint map

**Ticker:** TSM · **Sector:** AI Chips & Compute · **Sub-segment:** Foundry / Advanced Packaging · **Jurisdiction:** Taiwan

**Supply chain role:** Leading-edge foundry + CoWoS packaging

**Chokepoint hypothesis:** Foundry + advanced packaging chokepoint — near-monopoly on leading-edge nodes and CoWoS capacity; single point of failure for the entire AI accelerator stack.

6 mapped chokepoints. Tier 1 sits directly upstream of Taiwan Semiconductor Manufacturing Co.; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## EUV / High-NA scanners

`TS-C1` · **Tier 1** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** ASML

**Concentration:** Sole global supplier

**Substitutability and lead time:** None

**Geographic concentration:** Netherlands

**Watch for:** ASML shipment guidance revision

**Basis / source:** Public monopoly; well documented


## EUV optical columns (mirrors, illuminators, collectors)

`TS-C2` · **Tier 2** · Severity **Critical** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** Carl Zeiss SMT

**Non-listed / low-disclosure:** Carl Zeiss SMT — NOT separately listed (Carl Zeiss Foundation owned). ASML's sole supplier; ASML states it would 'effectively cease to be able to conduct our business' without it

**Concentration:** Sole source. Only two production sites worldwide (Oberkochen, Wetzlar)

**Substitutability and lead time:** None. ASML's own scanner output is capped by Zeiss SMT capacity

**Geographic concentration:** Germany — two sites

**Watch for:** Zeiss SMT capacity expansion milestone or delay

**Basis / source:** ASML annual report / SEC 6-K; Tom's Hardware 2026 on Oberkochen expansion


## EUV photoresist

`TS-C3` · **Tier 2** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** JSR, Tokyo Ohka Kogyo, Shin-Etsu Chemical

**Concentration:** Top 3 >90% of EUV segment; Japan ~95% of high-end EUV resist

**Substitutability and lead time:** Very low. At sub-7nm Japan is effectively the only supply base

**Geographic concentration:** Japan

**Watch for:** METI export-control list change; resist qualification event

**Basis / source:** Multiple secondary sources; METI Nov 2025 export-control listing


## EUV drive laser (high-power pulsed CO2)

`TS-C4` · **Tier 2** · Severity **Critical** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Trumpf

**Non-listed / low-disclosure:** Trumpf SE — NON-LISTED, German family-owned. Makes the world's most powerful pulsed industrial laser required for EUV

**Concentration:** Sole source for the EUV drive laser

**Substitutability and lead time:** None identified

**Geographic concentration:** Germany

**Watch for:** Trumpf capacity or delivery commentary

**Basis / source:** ASML/Trumpf partnership widely documented


## 300mm silicon wafers

`TS-C5` · **Tier 3** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Shin-Etsu, SUMCO, GlobalWafers, Siltronic

**Concentration:** Top 4 hold the large majority of 300mm supply

**Substitutability and lead time:** Low-Medium. New wafer capacity 24-36mo

**Geographic concentration:** Japan, Taiwan, Germany

**Watch for:** Wafer LTA pricing or capacity announcement

**Basis / source:** Established industry structure


## Zero-expansion substrate for EUV optics

`TSM-C6` · **Tier 3** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

> ⛔ **DO NOT PUBLISH.** CONVERGENCE CLAIM WITHDRAWN 31 Jul 2026 - do not publish "one foundation behind both the chip and robotics chokepoints". See Methodology.

**Named suppliers:** Schott AG (Zerodur), Corning (ULE), Ohara (Clearceram)

**Non-listed / low-disclosure:** Schott AG - NON-LISTED, Carl Zeiss Foundation. Corning is LISTED (NYSE: GLW). Ohara is LISTED (5218.T). Only one of the three is low-disclosure.

**Concentration:** ANSWERED 31 Jul 2026 - and it removes the convergence claim. Zeiss SMT does not disclose its production substrate, and its own patents list ULE, Zerodur AND Clearceram interchangeably as acceptable materials. Zeiss patent EP1664933A1 goes further: it covers a projection lens deliberately combining mirrors made from materials with OPPOSITE-SIGN temperature dependence of CTE - which is precisely the Zerodur / ULE relationship. So Zeiss may use both BY DESIGN. Three qualified specialty suppliers exist, two of them listed. This is a narrow specialty-materials layer, not a single source and NOT a Carl Zeiss Foundation chokepoint.

**Substitutability and lead time:** Low but not absent - three qualified suppliers across three countries (Germany, USA, Japan). Materials are exotic and slow to qualify, but no single owner controls the layer.

**Geographic concentration:** Germany, USA, Japan

**Watch for:** Schott, Corning or Ohara disclosure on lithography-grade substrate supply

**Basis / source:** RESOLVED 31 Jul 2026. Zeiss SMT patents US8711332B2 and EP1664933A1 (substrate materials listed as ULE, Zerodur or Clearceram; opposite-sign CTE combination claimed) - PRIMARY. Corning ULE product literature and Corning/Hrdina EUVL Symposium paper on ULE for EUV. Prior basis was analyst inference that Zerodur was "a prime candidate", which was then carried as a probable Zeiss Foundation convergence. It is not supportable. SEVERITY LOWERED High -> Medium.


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.