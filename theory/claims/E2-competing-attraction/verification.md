# E2 — Verification Record

**Tally:** 6/6 checks passed.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory. Constants in [`verification/inputs.json`](verification/inputs.json). Every check runnable as `python3 verification/check_NN_*.py` or `wolframscript -file verification/check_NN_*.wls`.

## Result summary

The qualitative claim — **competing gravitational attraction in an asymmetric 3-body configuration produces an apparent inter-electron repulsion with the correct sign** — is confirmed by independent numerical computation (mpmath at 30 dps) and symbolic computation (SymPy and Wolfram Engine agree on the closed form $\ddot{r} = Gm_p[1/d^2 - 1/(d+r)^2] - 2Gm_e/r^2$). A control case (proton *between* the electrons) gives the opposite sign, confirming geometry-dependence.

The quantitative claim — magnitude — fails. The ratio $F_{\rm effective}/F_{\rm Coulomb}$ at $d=r=a_0$ is:
- **Python/mpmath:** $1.651068\times 10^{-40}$
- **Wolfram Engine:**  $1.651068\times 10^{-40}$
- **Analytical estimate** from fundamental coupling $Gm_em_p/(k_Ce^2)$: $4.409\times 10^{-40}$, modulated by an $O(1)$ geometric factor of $0.374$.

Cross-tool agreement is exact to 15+ significant figures. The $\sim 10^{40}$ gap is a physical feature, not a calculation artifact.

## Per-check detail

### Check 01 — Dimensional analysis
- **Tool:** Python + Pint 0.25
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** $Gm_em_p/r^2$, $k_Ce^2/r^2$, and $\mu\ddot{r}$ all verified as newtons.

### Check 02 — Asymmetric-config numerical simulation (the load-bearer)
- **Tool:** Python + mpmath 1.3.0 at 30-digit precision
- **Script:** [`verification/check_02_asymmetric_config.py`](verification/check_02_asymmetric_config.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Reproduces the Session C toy-model numerical table. 8 out of 8 reference values match (after a provenance update — see "Honesty flags" below). Sign check (apparent repulsion) confirmed.

### Check 03 — Symmetric-config control
- **Tool:** Python + mpmath
- **Script:** [`verification/check_03_symmetric_control.py`](verification/check_03_symmetric_control.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** Confirms that placing the proton *between* the electrons gives $\ddot{r} < 0$ (apparent attraction), the opposite of the asymmetric case. Demonstrates that E2's sign is geometry-dependent, not intrinsic.

### Check 04 — Analytical ratio to fundamental gravity-EM coupling
- **Tool:** Python + mpmath
- **Script:** [`verification/check_04_ratio_analytical.py`](verification/check_04_ratio_analytical.py)
- **Output:** [`verification/outputs/check_04.txt`](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** The measured $F_{\rm eff}/F_{\rm Coulomb} = 1.65\times 10^{-40}$ agrees with the fundamental coupling ratio $Gm_em_p/(k_Ce^2) = 4.41\times 10^{-40}$ modulo an $O(1)$ geometric factor of 0.374. Confirms the $\sim 10^{40}$ gap is intrinsic to the gravity-vs-EM hierarchy, not an artifact of the specific toy geometry.

### Check 05 — Symbolic derivation of $\ddot{r}$ (SymPy)
- **Tool:** SymPy 1.14
- **Script:** [`verification/check_05_sympy_symbolic.py`](verification/check_05_sympy_symbolic.py)
- **Output:** [`verification/outputs/check_05.txt`](verification/outputs/check_05.txt)
- **Result:** PASS
- **Notes:** Symbolically derives $\ddot{r} = Gm_p(1/d^2 - 1/(d+r)^2) - 2Gm_e/r^2$. At $d=r=a_0$, the proton-gradient term dominates the inter-electron term by a factor $3m_p/(8m_e) \approx 688$.

### Check 06 — Wolfram Engine cross-verification
- **Tool:** Wolfram Engine via `wolframscript`
- **Script:** [`verification/check_06_wolfram.wls`](verification/check_06_wolfram.wls)
- **Output:** [`verification/outputs/check_06_wolfram.txt`](verification/outputs/check_06_wolfram.txt)
- **Result:** PASS
- **Notes:** Independent CAS verifies the symbolic form of $\ddot{r}$ matches the expected decomposition (`TrueQ` == True). Numerical values at SI parameters agree with mpmath to 15+ digits: $a_{E_1} = -3.985137882\times 10^{-17}\,\mathrm{m/s^2}$, $\ddot{r} = +2.986139694\times 10^{-17}\,\mathrm{m/s^2}$, $F_{\rm eff}/F_{\rm Coulomb} = 1.651068\times 10^{-40}$. Sign check passes.

## Cross-tool agreement

- Python/mpmath (30 dps) and Wolfram Engine agree to 15+ sig figs on every numerical quantity tested.
- SymPy and Wolfram agree symbolically on the closed-form $\ddot{r}$ expression.
- Analytical estimate from fundamental coupling agrees with numerical result to within an $O(1)$ geometric factor (0.374).

No tool disagreements remain.

## Honesty flags

**Discrepancy caught and resolved:** First-pass Check 02 flagged a $\sim 0.07\%$ mismatch between the computed values and the Session C reference values. Investigation revealed that Session C's `derivation.md` used a truncated Bohr radius `a_0 = 5.29e-11 m`, while `inputs.json` now uses the full CODATA value `5.29177210903e-11 m`. The ratio $F_{\rm eff}/F_{\rm Coulomb}$ is insensitive to this (the $a_0^2$ factor cancels; both give $1.651\times 10^{-40}$), but the absolute force values shift by $\approx 0.07\%$. The reference values in `inputs.json` have been updated to the higher-precision CODATA computation, verified by both Python and Wolfram independently. The claim's qualitative conclusions are unaffected.

This is exactly the kind of audit issue the retrofit was designed to surface: a minor numerical drift between the prose-narrative numbers and the rigorous-computation numbers, now caught and documented with provenance.

## Tier assignment

- **🟢 Green** for the calculation: sign-correct apparent repulsion reproduced by Python + Wolfram + analytical scaling; all three tools agree.
- **🟡 Yellow** for the structural compatibility claim: sign is correct in asymmetric geometries only.
- **🔴 Red** for the quantitative claim that competing attraction reproduces Coulomb-scale repulsion: off by $\sim 10^{40}$. This is the load-bearing structural gap identified in Session C; the 2026-04-23 `/debate` converged on relocating E2's narrative from S3 to S8 of the coherence paper (see `debates/2026-04-23-e2-downgrade/synthesis.md`).

## TODOs / Known gaps

- Wolfram MCP unavailable in this session — the Wolfram check was run via local `wolframscript` / Wolfram Engine. If a Wolfram-MCP session becomes available, re-running check_06 through MCP would provide audit parity across the ecosystem.
- No check exists for an *isotropic-background* version (e.g., 12 protons arranged icosahedrally around the electron pair). Per `caveats.md`, Gauss's-theorem reasoning predicts zero net background force and hence no repulsion. A numerical confirmation would strengthen the geometry-dependence claim.
