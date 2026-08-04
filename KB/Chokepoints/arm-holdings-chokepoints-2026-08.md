---
Title: Arm Holdings — upstream chokepoint map
Date: 2026-08-04
Category/Tags: chokepoint map, supply chain, AI Chips & Compute, CPU/IP Architecture, ARM
---

# Arm Holdings — upstream chokepoint map

**Ticker:** ARM · **Sector:** AI Chips & Compute · **Sub-segment:** CPU/IP Architecture · **Jurisdiction:** UK

**Supply chain role:** IP/architecture licensor

**Chokepoint hypothesis:** IP chokepoint — near-universal architecture dependency for power-efficient edge/robotics inference silicon.

4 mapped chokepoints. Tier 1 sits directly upstream of Arm Holdings; Tier 2 and Tier 3 sit above that.

> **How to read the evidence grade.** ACTUAL means the claim rests on a filing, company release or
> regulator text. REPORTED means trade press. INFERRED means no named source was recorded — treat it
> as a lead to verify, not a fact. Roughly 70% of this map is INFERRED. A stress test of nine
> High-confidence entries in July 2026 found about half the substantive claims needed correction, so
> evidence grade, not confidence, is what governs use.


## EDA toolchain

`ARM-C1` · **Tier 1** · Severity **High** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Synopsys, Cadence, Siemens EDA

**Concentration:** Three-firm oligopoly controls essentially all advanced design flow

**Substitutability and lead time:** None. No credible alternative toolchain

**Geographic concentration:** USA, Germany

**Watch for:** EDA export-control action

**Basis / source:** Well-established market structure


## Foundry implementation partners

`ARM-C2` · **Tier 2** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** TSMC, Samsung Foundry

**Concentration:** Concentrated at leading edge

**Substitutability and lead time:** Low

**Geographic concentration:** Taiwan, Korea

**Watch for:** Node availability

**Basis / source:** Established


## Export-control / licensing regime for China

`ARM-C3` · **Tier 2** · Severity **High** · Evidence **ACTUAL** — primary source (filing, company release, or regulator text)

**Named suppliers:** US BIS and UK export-control policy; Wassenaar Arrangement dual-use listing

**Concentration:** Policy-set. Technical trigger is specific and checkable: Wassenaar controls at a 256-bit datapath threshold; Neoverse V-series runs 2x256-bit and is therefore caught

**Substitutability and lead time:** CORRECTED 31 Jul 2026 - not binary, and already partly in force. Bifurcated by product line: Arm declined to sell Neoverse V-series to Alibaba T-Head expecting US/UK licences would not be granted, while continuing to sell lower-tier IP into China. In 2026 Arm is selling its AGI CPU into China even though the V3 cores behind it cannot be licensed to Chinese CPU developers. Substitution route is RISC-V, and China hosts ~40% of the world's Arm-based servers

**Geographic concentration:** UK, USA, China

**Watch for:** Any Arm licence grant of V-series or successor to a Chinese entity; Wassenaar threshold revision; new BIS rule naming CPU IP

**Basis / source:** PRIMARY: Arm's own SEC filing risk factors flag Neoverse export-licence exposure (reported via eeNews Europe). Secondary: Tom's Hardware on the Wassenaar 256-bit threshold and the Alibaba/T-Head decision; TechPowerUp on China's ~40% share of Arm servers. Arm China joint-venture governance NOT examined - separate question


## Customer concentration in edge/robotics inference

`ARM-C4` · **Tier 3** · Severity **Medium** · Evidence **INFERRED** — no named source — analyst inference

**Named suppliers:** Qualcomm, MediaTek, NVIDIA, Chinese SoC vendors

**Concentration:** Revenue concentrated in a handful of large licensees

**Substitutability and lead time:** Medium

**Geographic concentration:** Global

**Watch for:** Major licensee architecture switch (e.g. RISC-V)

**Basis / source:** Analyst hypothesis


---

Source: USINO Physical AI Watchlist & Chokepoint Map, v1.6, 4 August 2026.
Market intelligence research only. Not investment advice.