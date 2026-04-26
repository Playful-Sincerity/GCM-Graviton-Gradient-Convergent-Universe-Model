# R6 — Verification Record

**Tally:** 2/2 PASS (both checks PASS on both tools).
**Last run:** 2026-04-24
**Reproducible:** Yes — see `verification/` directory.
**Tools:** Python 3.14 (stdlib `decimal`, prec=50) + Wolfram Engine via `wolframscript`. Wolfram MCP unavailable in this session. `sympy`/`mpmath` not installed; Wolfram used for all symbolic work.
**Session E status:** Session E (which would be the authoritative R6 derivation) has not run as of 2026-04-24. This retrofit only verifies R6's *internal* numerical claims; when Session E produces a richer treatment, this verification/ folder should be extended (not replaced — the current checks are still valid).
**Honesty note:** These scripts were added 2026-04-24 as new forward-verification, not retrofit of prior runs. On 2026-04-23, R6 was written from the plan specification without running any tools.

---

## Check 1 — Photon mass in eV/c² and ratio to Wang 2023 FRB bound

- **Tool:** Python `decimal` (prec=50) + Wolfram independent cross-check
- **Script (Python):** [verification/check_01_photon_mass_kg_to_eV.py](verification/check_01_photon_mass_kg_to_eV.py)
- **Script (Wolfram):** [verification/check_01_photon_mass_kg_to_eV.wls](verification/check_01_photon_mass_kg_to_eV.wls)
- **Output (Python):** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Output (Wolfram):** [verification/outputs/check_01_wolfram.txt](verification/outputs/check_01_wolfram.txt)
- **Result:** **PASS** on both tools.
- **Computed:** GCM's claimed $m_\gamma = 10^{-54}$ kg corresponds to $5.61 \times 10^{-19}$ eV/c² rest energy. plausibility.md's stated $5.6 \times 10^{-19}$ eV/c² is correct to 0.2%.
- **Comparison:** Wang et al. 2023 FRB bound is $m_\gamma \leq 2.1 \times 10^{-15}$ eV/c². Ratio Wang/GCM = $3.74 \times 10^3$, so GCM value is **3.57 orders below the bound**. plausibility.md/adjacent-programs.md claim "~4 orders below" is correct to 0.5 order.
- **Cross-tool agreement:** Python and Wolfram agree to 15+ digits on the ratio.
- **Clarification caught:** Some GCM material previously stated "28 orders below the bound" — that is correct for the **graviton** mass vs. LIGO bound (plan S2 M1), NOT the photon mass vs. FRB bound. The two "orders below" claims are for different particles and should not be conflated.

## Check 2 — Cascade exponent = 1 and consistency with DES 2024 time-dilation measurement

- **Tool:** Wolfram (symbolic algebra, `Exponent[]`) + Python (numerical sigma comparison)
- **Script (Wolfram, symbolic):** [verification/check_02_cascade_exponent.wls](verification/check_02_cascade_exponent.wls)
- **Script (Python, consistency):** [verification/check_02_DES_consistency.py](verification/check_02_DES_consistency.py)
- **Output (Wolfram):** [verification/outputs/check_02_wolfram.txt](verification/outputs/check_02_wolfram.txt)
- **Output (Python):** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** **PASS** on both tools.
- **Symbolic finding (Wolfram):** The R6 cascade $\lambda_{\text{obs}} = (1+z)\lambda_{\text{emit}}$ → $d_{\text{internal}} \propto \lambda$ (L3) → $\tau \propto d_{\text{internal}}$ yields $\tau_{\text{obs}}/\tau_{\text{emit}} = (1+z)^1$ with exponent exactly 1 (Wolfram `Exponent[1+z, 1+z] = 1`).
- **Observational comparison (Python):** DES 2024 measures $(1+z)^{1.003 \pm 0.005 \,(\text{stat}) \pm 0.010 \,(\text{sys})}$. R6 prediction (exponent = 1) differs from measurement by:
  - $0.60\sigma$ using statistical uncertainty alone
  - $0.30\sigma$ using systematic uncertainty alone
  - $0.27\sigma$ using combined uncertainty ($\sigma_{\text{tot}} = \sqrt{0.005^2 + 0.010^2} = 0.0112$)
- **Verdict:** R6 prediction is consistent with DES 2024 at well within 1σ.

## Cross-Tool Disagreements

**None.** Python and Wolfram agree on every numerical quantity in both checks.

## What Is NOT Verified Here

R6's load-bearing structural claims — (a) L3 wavelength-spacing correspondence, (b) substrate-independent internal-propagation speed — are **not** verified by these scripts. They are yellow-tier assumptions whose rigor is deferred to Session E. This verification folder only confirms:

1. The conversion from kg to eV/c² is arithmetically correct.
2. The "4 orders below Wang bound" claim is correct (actual: 3.57 orders).
3. If the cascade assumptions hold, the exponent is exactly 1 by symbolic algebra.
4. Exponent = 1 is consistent with DES 2024 data to well within 1σ.

**Falsification conditions** (for Session E or future measurements to check):
- If L3 fails (wavelength not linearly tied to internal spacing), the cascade breaks.
- If sub-percent SNe Ia measurements (LSST, Euclid, Roman) tighten the time-dilation exponent to $1.00 \pm 0.001$ and the central value is not 1.000 at $>3\sigma$, R6 is falsified.

## TODOs

1. **Wolfram MCP.** Currently unavailable in this session; local `wolframscript` substituted. When Wolfram MCP is added, re-run for tool-call-traced verification.
2. **Session E.** Once Session E runs, it should specify the photon's internal graviton-cluster model concretely. At that point, add checks for (a) L3 derivation from GCM dynamics, (b) internal-propagation-speed substrate-independence bound.
3. **Pantheon+ and/or DES 5-year final** — when newer precision measurements of the time-dilation exponent appear, update check_02 with the new central value and uncertainty and re-run. Expected: R6 prediction (exponent = 1) remains consistent.

## Honesty Summary

R6's one genuine quantitative claim (photon mass vs. Wang bound) is arithmetically correct to 0.2% and 0.5 order. The other key quantity (cascade exponent = 1) is a symbolic consequence of the stated premises, not a derivation from first principles — the premises themselves (L3, substrate-independent propagation speed) remain yellow-tier. R6 passes the checks that exist for it at this epistemic level; it does not yet have checks for the deeper structural premises.
