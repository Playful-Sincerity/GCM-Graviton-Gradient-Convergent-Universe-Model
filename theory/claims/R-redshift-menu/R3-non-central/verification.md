# R3 — Verification Record

**Tally:** 0/1 PASS, 1/1 INCONCLUSIVE (real error caught).
**Last run:** 2026-04-24
**Reproducible:** Yes — see `verification/` directory.
**Tools:** Python 3.14 (stdlib `decimal`, prec=50) + Wolfram Engine via `wolframscript`.
**Honesty note:** New forward-verification 2026-04-24, not retrofit. R3 is tier-🔴 red overall; this verification folder has a single check because R3 has a single numerical claim worth checking.

---

## Check 1 — Required cosmological gravitational potential gradient

- **Tool:** Python `decimal` prec=50 + Wolfram independent cross-check
- **Script (Python):** [verification/check_01_gradient_magnitude.py](verification/check_01_gradient_magnitude.py)
- **Script (Wolfram):** [verification/check_01_gradient_magnitude.wls](verification/check_01_gradient_magnitude.wls)
- **Output (Python):** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Output (Wolfram):** [verification/outputs/check_01_wolfram.txt](verification/outputs/check_01_wolfram.txt)
- **Result:** **INCONCLUSIVE — arithmetic error in plausibility.md caught.**
- **Derivation:** Gravitational redshift is $z = \Delta\Phi/c^2$. If R3 reproduces $z = H_0 d / c$ at low $z$, then $\Delta\Phi = c H_0 d$, so $d\Phi/dr = c H_0$.
- **Computed:** $c H_0 = 6.80 \times 10^{-10}$ m/s² at $H_0 = 70$ km/s/Mpc (both tools agree to 15 digits).
- **Claimed in plausibility.md:** $\sim 2 \times 10^{-8}$ m/s². **Off by factor ~30.** Correct value is ~30× smaller than claimed.
- **Structural claim preserved:** "required gradient is of order $c H_0$" is correct. Specific number was wrong.

## Notable side-finding

The correct value $c H_0 \approx 6.8 \times 10^{-10}$ m/s² is within a factor ~5 of the **MOND acceleration scale** $a_0 \approx 1.2 \times 10^{-10}$ m/s². This "Hubble coincidence" is well-known in the modified-gravity literature (Milgrom 1983 and following). For R3's yellow-ification effort, this coincidence is a hook — the required R3 gradient is in the same neighborhood as the scale where galaxy rotation curves deviate from Newtonian predictions, which suggests a possible connection between R3's cosmological anisotropy and MOND-like phenomenology. Not chased here; flagged for plausibility.md revision if R3 gets further development.

## Cross-Tool Disagreements

**None.** Python and Wolfram agree to 15 digits on $c H_0$. The disagreement is between tools (agreed) and plausibility.md (wrong).

## TODOs

1. **Revise R3/plausibility.md.** Replace "$\sim 2 \times 10^{-8}$ m/s²" with "$\sim 6.8 \times 10^{-10}$ m/s² (at $H_0 = 70$ km/s/Mpc), intriguingly close to the MOND acceleration scale $a_0 \sim 1.2 \times 10^{-10}$ m/s²."
2. **Wolfram MCP.** Still unavailable; local wolframscript substituted.

## Honesty Summary

R3 is red because the required cosmological potential anisotropy has not been measured; this verification does not change that. The verification does catch a 30× arithmetic error in the specific numerical value of the required gradient. The correction happens to point toward a non-trivial connection with modified-gravity literature (MOND $a_0$) that was not explored in the original plausibility.md.

R3 tier remains **🔴 Red.** The verification improves the claim's internal numerical hygiene but does not close its central empirical gap (undetected anisotropy).
