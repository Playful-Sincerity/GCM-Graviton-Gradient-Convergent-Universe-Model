# R2 — Verification Record

**Tally:** 0/1 checks PASS directly (1 check defers to R1).
**Last run:** 2026-04-24
**Reproducible:** Yes — see below. This claim's single numerical scaffolding ($H_0 / c$ and $H_0$ scale) was already verified under R1's check_01 — this verification.md is a pointer, not a duplicate.
**Tools:** Python 3.14 (`decimal` prec=50) + Wolfram Engine via `wolframscript`. Wolfram MCP unavailable; local wolframscript substituted.
**Honesty note:** New forward-verification 2026-04-24. R2 has no unique numerical claims beyond what R1 already checks; the shared scaffolding is the Hubble-scale order-of-magnitude.

---

## Check 1 — Void decompression rate $\sim H_0$

- **Tool:** defers to [R1's check_01](../R1-space-friction/verification/check_01_hubble_radius_and_alpha.py) + [R1 Wolfram cross-check](../R1-space-friction/verification/check_01_hubble_radius_and_alpha.wls)
- **Result:** **INCONCLUSIVE** — same labelling issue as R1. plausibility.md says "for the observed $H_0 \approx 70$ km/s/Mpc, the required fractional wavelength growth per unit distance is $\sim H_0 / c \approx 2.3 \times 10^{-27}$ m⁻¹" — but that numerical value ($2.3 \times 10^{-27}$ m⁻¹) is actually $1 / R_{\text{observable}}$, not $H_0/c$ (which is $7.57 \times 10^{-27}$ m⁻¹). Same 3.3× factor as R1.
- **Fix needed in plausibility.md:** same as R1 — choose the Hubble-radius convention ($R_H = 1.32 \times 10^{26}$ m, rate = $7.57 \times 10^{-27}$ m⁻¹) or the observable-universe convention ($R_{\text{obs}} = 4.4 \times 10^{26}$ m, rate = $2.27 \times 10^{-27}$ m⁻¹), and use it consistently.

## What This Verification Does NOT Cover

R2's main structural claims are *not* numerical:
- **Void decompression in a converging universe as the redshift mechanism.** Not a formula, so no check.
- **Alliance with Wiltshire timescape (Seifert 2025, ln B > 5 on 1,535 Pantheon+ SNe Ia).** Citation-level; no GCM-specific computation to verify.
- **ISW tension reinterpretation.** Quantitative shape prediction is future work (flagged as load-bearing open problem in status.md).

A proper R2 verification folder would require:
1. A GCM-specific cosmology model producing $\mu(z)$ and ISW signal shape.
2. A fit to Pantheon+ data with Bayesian evidence comparison against $\Lambda$CDM and timescape.
3. Compared-and-contrasted ISW predictions between GCM-R2 and $\Lambda$CDM.

None of these exist yet. R2 stays at **🟡 Yellow** structural plausibility, pending the quantitative work.

## TODOs

1. **Fix the $H_0/c$ labelling** (same as R1).
2. **Quantitative $\mu(z)$ fit** — substantial research program; not in the coherence-case scope.
3. **Quantitative ISW prediction** — requires a void-boundary dynamics model.
4. **Wolfram MCP.** Still unavailable.

## Honesty Summary

R2's verification footprint is small because R2's claims are mostly structural/strategic rather than numerical. The one numerical claim it shares with R1 has the same labelling issue; otherwise, R2 inherits from Wiltshire's empirical success rather than producing its own. This is honest positioning — overclaiming a GCM-specific fit to Pantheon+ would be wrong.
