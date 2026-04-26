# R1 — Verification Record

**Tally:** 1/3 PASS, 2/3 INCONCLUSIVE (real findings surfaced — not failures, but plausibility.md numbers need revision).
**Last run:** 2026-04-24
**Reproducible:** Yes — see `verification/` directory.
**Tools:** Python 3.14 (stdlib `decimal`, prec=50) + Wolfram Engine via `wolframscript`. Wolfram MCP unavailable in this session (only firecrawl/figma/google-calendar/n8n/Drive MCPs are loaded). `mpmath` and `sympy` not installed system-wide; symbolic work done in Wolfram.
**Honesty note:** These scripts are *new forward-verification added 2026-04-24*, not a retrofit of prior Python runs. On 2026-04-23 (Session G), no verification tools were run; the plausibility.md numbers were stated as mental arithmetic. This was disclosed before the retrofit began.

---

## Check 1 — Hubble radius and $\alpha = H_0/c$

- **Tool:** Python `decimal` + Wolfram (independent cross-check)
- **Script (Python):** [verification/check_01_hubble_radius_and_alpha.py](verification/check_01_hubble_radius_and_alpha.py)
- **Script (Wolfram):** [verification/check_01_hubble_radius_and_alpha.wls](verification/check_01_hubble_radius_and_alpha.wls)
- **Output (Python):** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Output (Wolfram):** [verification/outputs/check_01_wolfram.txt](verification/outputs/check_01_wolfram.txt)
- **Result:** **INCONCLUSIVE — real labelling error caught.**
- **Finding:** plausibility.md says "Hubble radius $R_H \approx 4.4 \times 10^{26}$ m" AND "$\alpha \sim H_0/c \approx 2.3 \times 10^{-27}$ m⁻¹". Both tools independently confirm these are inconsistent by a factor ~3.3:
  - $c/H_0$ at $H_0 = 70$ km/s/Mpc is **1.32e26 m**, not 4.4e26.
  - $H_0/c$ at $H_0 = 70$ is **7.57e-27 m⁻¹**, not 2.3e-27.
  - 4.4e26 m is actually the **observable-universe particle horizon** (~46 Gly), and 2.3e-27 m⁻¹ ≈ 1/(4.4e26 m).
- **Structural claim preserved:** $\alpha$ of order inverse cosmological length scale is correct. Only the specific numerical-value-plus-label is wrong.
- **Fix needed in plausibility.md:** either (a) relabel 4.4e26 m as "observable-universe radius" and drop the "$\alpha \sim H_0/c$" framing; or (b) use $R_H = 1.32 \times 10^{26}$ m and $\alpha = 7.57 \times 10^{-27}$ m⁻¹ consistently with $H_0/c$.

## Check 2 — Graviton number density and per-graviton cross-section

- **Tool:** Python `decimal` + Wolfram independent cross-check
- **Script (Python):** [verification/check_02_graviton_density_and_cross_section.py](verification/check_02_graviton_density_and_cross_section.py)
- **Script (Wolfram):** [verification/check_02_graviton_density_and_cross_section.wls](verification/check_02_graviton_density_and_cross_section.wls)
- **Output (Python):** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Output (Wolfram):** [verification/outputs/check_02_wolfram.txt](verification/outputs/check_02_wolfram.txt)
- **Result:** **INCONCLUSIVE — two arithmetic errors in plausibility.md surfaced.**
- **Finding 1:** plausibility.md says $n_g \sim 10^{185}/V_{\text{universe}} \approx 10^{106}$ m⁻³. Correct computation gives $V_{\text{obs}} = (4/3)\pi R_{\text{obs}}^3 \approx 3.57 \times 10^{80}$ m³ (using $R_{\text{obs}} = 4.4 \times 10^{26}$ m), so $n_g \approx 2.8 \times 10^{104}$ m⁻³. **Plausibility.md is off by ~2 orders of magnitude.**
- **Finding 2:** With self-consistent $\alpha = H_0/c = 7.57 \times 10^{-27}$ m⁻¹ and $n_g = 2.8 \times 10^{104}$ m⁻³, the implied cross-section is $\sigma_g \approx 2.7 \times 10^{-131}$ m², **not** $10^{-133}$ m² as plausibility.md states. Off by ~2 orders.
- **Supplementary result confirmed:** $V_{\text{obs}}/\ell_P^3 \approx 8.5 \times 10^{184} \approx 10^{185}$. The M3 claim (Planck-cell count of observable universe) is consistent.
- **Structural claim preserved:** $\sigma_g$ is an extraordinarily small per-graviton cross-section. The specific exponent in plausibility.md is unreliable.

## Check 3 — Exponential energy-loss law collapses to linear redshift at small $z$

- **Tool:** Python `decimal` (numerical) + Wolfram (symbolic DSolve + Series)
- **Script (Python):** [verification/check_03_exponential_to_linear.py](verification/check_03_exponential_to_linear.py)
- **Script (Wolfram):** [verification/check_03_symbolic.wls](verification/check_03_symbolic.wls)
- **Output (Python):** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Output (Wolfram):** [verification/outputs/check_03_wolfram.txt](verification/outputs/check_03_wolfram.txt)
- **Result:** **PASS** (both tools).
- **Finding:** Wolfram `DSolve[{en'[r] == -alpha en[r], en[0] == E0}, en[r], r]` yields $E(r) = E_0 e^{-\alpha r}$. Observed $1+z = E_0/E(r) = e^{\alpha r}$. Taylor series: $z \approx \alpha r + (\alpha r)^2/2 + (\alpha r)^3/6 + \ldots$. Leading term is the Hubble-like linear law.
- **Caveat surfaced by numerical check:** the linear approximation is accurate to ~0.5% for $\alpha r < 0.01$, ~5% for $\alpha r = 0.1$, ~15% for $\alpha r = 0.3$, and ~37% for $\alpha r = \ln 2$ (i.e. $z = 1$). R1 must use the full exponential $z = e^{\alpha r} - 1$ (not the linear approximation) when fitting Pantheon+ data at $z \gtrsim 0.1$.

## Cross-Tool Disagreements

**None.** Python and Wolfram agree on every numerical quantity across all three checks. Where disagreement exists, it is between the verification tools (agreed) and plausibility.md (out of date / arithmetically wrong). This is exactly the value-add of the retrofit.

## TODOs

1. **Revise plausibility.md.** Two options, Wisdom to choose:
   (a) Keep $R_{\text{obs}} = 4.4 \times 10^{26}$ m but relabel it "observable universe radius (particle horizon)", then drop "$\alpha \sim H_0/c$" framing and use $\alpha \sim 1/R_{\text{obs}} = 2.3 \times 10^{-27}$ m⁻¹.
   (b) Use the Hubble-radius framing properly: $R_H = c/H_0 = 1.32 \times 10^{26}$ m, $\alpha = H_0/c = 7.57 \times 10^{-27}$ m⁻¹.
   Either is internally consistent. The original text mixes them.
2. **Update $n_g$ and $\sigma_g$.** With $R_{\text{obs}} = 4.4 \times 10^{26}$ m interpretation: $n_g \approx 2.8 \times 10^{104}$ m⁻³, $\sigma_g \approx \alpha/n_g$ depends on which $\alpha$ is used — needs joint revision.
3. **Wolfram MCP.** Add a Wolfram MCP server to the Claude Code configuration and re-run with it as the authoritative third independent tool. `wolframscript` locally-installed worked well as a substitute.
4. **SymPy/mpmath install.** If future claim folders need richer symbolic work, install `sympy` + `mpmath` in a project venv (`GCM/.venv/`) so Python checks can do symbolic algebra natively instead of round-tripping through Wolfram.

## Honesty Summary

This claim's numerical scaffolding in plausibility.md has three arithmetic/labelling errors, all of which change exponents by 1–2 orders of magnitude. The errors were not visible from the markdown narrative alone; the retrofit caught them. The *structural* claims (friction coefficient of order the inverse cosmological length scale; cross-section per graviton extraordinarily small; exponential energy-loss law → linear Hubble law at small z) are correct and tool-confirmed.

R1's overall tier remains **🟡 Yellow** — the structural story stands; the specific numerics need correction. The tier would have been inflated to "plausible with specific numerical support" without these checks; it is now honestly "plausible structurally; specific numerics are retrofit-in-progress."
