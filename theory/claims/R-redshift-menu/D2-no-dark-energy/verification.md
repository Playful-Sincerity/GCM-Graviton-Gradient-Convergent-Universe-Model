# D2 — Verification Record

**Tally:** 1/1 — one citation-level check (DES 2024 consistency) passed via R6.
**Last run:** 2026-04-24
**Reproducible:** Yes — citations live in inputs.json in sibling claim folders.
**Tools:** Python 3.14 + wolframscript (for the inherited checks). Wolfram MCP unavailable; local wolframscript substituted.
**Honesty note:** D2 is primarily a *positioning claim* relative to peer-reviewed alternatives (Wiltshire timescape + DESI DR2), not a GCM-specific derivation. Verification is correspondingly at the citation-and-alliance level, not at the derive-from-first-principles level.

---

## Check 1 — DES 2024 time-dilation consistency (inherited via R6)

- **Tool:** Wolfram symbolic + Python numerical sigma comparison (via R6)
- **Script:** [R6/verification/check_02_DES_consistency.py](../R6-photon-structure/verification/check_02_DES_consistency.py)
- **Output:** [R6/verification/outputs/check_02.txt](../R6-photon-structure/verification/outputs/check_02.txt)
- **Result:** **PASS.** R6 structural prediction (exponent = 1) is consistent with DES 2024 measurement $(1+z)^{1.003 \pm 0.005 \pm 0.010}$ at $0.27\sigma$ combined uncertainty.
- **Significance for D2:** any mechanism producing SNe Ia observations without $\Lambda$ must reproduce the measured time-dilation. R6 (GCM-internal) does this; timescape (Wiltshire, via metric clock-rate structure) does this too. D2's alliance with timescape is empirically well-supported at this level.

## Citation Checks (meta-level)

D2's key citations, all verifiable but not computed here:

| Claim | Citation | Status |
|-------|----------|--------|
| Timescape wins Pantheon+ at ln B > 5 | Seifert et al. 2025, MNRAS Lett. 537, L55, on 1,535 SNe Ia | Published; citation accurate; numerical ln B value not re-derived here |
| DESI DR2 evolving $w(z)$ at 2.8–4.2σ | DESI Collaboration DR2 results (2025) | Published; significance level cited in `2026-04-23-redshift-empirics.md` research source |
| $H_0$ tension at 5σ | SH0ES (Riess et al.) vs Planck 2018 | Well-established in literature |
| $\sigma_8$ tension | Various late-time LSS vs Planck | Well-established |

## What This Verification Does NOT Cover

**D2 does not have GCM-specific:**

1. $\mu(z)$ prediction — no GCM model produces Pantheon+-fittable distance moduli yet.
2. ISW shape prediction — no quantitative computation in GCM's framework.
3. $H_0$ tension resolution mechanism — D2 claims "$H_0$ isn't a fundamental expansion rate" but doesn't produce the tension resolution quantitatively.

Any of these would require substantial derivation work beyond the coherence-case scope.

## Cross-Tool Disagreements

None at the level of this check — the single verified check is inherited from R6, which has clean cross-tool agreement.

## TODOs

1. **Quantitative $\mu(z)$ fit.** When GCM specifies a cosmology model, fit Pantheon+ and compare Bayesian evidence against $\Lambda$CDM and timescape. Target: ln B > 1 over $\Lambda$CDM at minimum.
2. **Quantitative ISW shape from R2.** Compute the predicted ISW signal in a converging universe with void decompression.
3. **Wolfram MCP.** Still unavailable.

## Honesty Summary

D2 is a positioning claim, not a derivation. Its verification is a one-line check that the time-dilation consistency (which D2 inherits from R6) holds. The substantive empirical support for D2 comes from timescape's peer-reviewed success and DESI DR2's observational trends — both of which are *outside* GCM and cited by D2 as allies.

D2 stays at **🟡 Yellow.** The alliance with timescape is real and empirically strong; GCM hasn't yet added its own quantitative value to the dark-energy-replacement program.
