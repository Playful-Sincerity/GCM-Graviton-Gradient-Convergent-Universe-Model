# E4 — Verification Record

**Tally:** 7/7 checks passed.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory. All constants in [`verification/inputs.json`](verification/inputs.json). Every check is `python3 verification/check_NN_*.py` or `wolframscript -file verification/check_NN_*.wls`.

## Result summary

- $U(R) = -(Gm^2/R)\,\mathrm{erf}(R/(2\sigma))$ confirmed symbolically (SymPy) and independently (Wolfram).
- All four limits match exactly: $U(0) = -Gm^2/(\sigma\sqrt{\pi})$; $F(0) = 0$ linear; $R\,U(R)\to -Gm^2$; $R^2 F(R) \to Gm^2$.
- Numerical sweep $R/\sigma \in [0.01, 20]$ confirmed at **50-digit precision** (mpmath) and cross-verified by Wolfram at 25-digit; the two agree to machine precision (e.g. 0.08110858834532414 at $R=\sigma$ in both tools).
- Closed-form $U(R)$ cross-validated by **independent scipy double-integration** of the original double integral (max rel.\ error $6\times 10^{-8}$).
- Closed-form single-Gaussian potential cross-validated by **Gauss's-law derivation from $\rho(r)$** (max rel.\ error $7.6\times 10^{-24}$ via mpmath quadrature to 30 digits).

## Per-check detail

### Check 01 — Dimensional analysis
- **Tool:** Python + Pint 0.25 (with SymPy fallback path retained)
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** Confirms $[Gm^2/R] = \mathrm{J}$, $[Gm^2/R^2] = \mathrm{N}$, and that $\mathrm{erf}$ and $\exp$ arguments are dimensionless.

### Check 02 — SymPy symbolic derivation
- **Tool:** SymPy 1.14
- **Script:** [`verification/check_02_sympy_derivation.py`](verification/check_02_sympy_derivation.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Full symbolic derivation of $U(R)$, series expansions, $U(R=0)$ and $\lim R\,U(R)$ both match expected forms.

### Check 03 — High-precision numerical sweep (mpmath)
- **Tool:** mpmath 1.3.0 at 50-digit precision
- **Script:** [`verification/check_03_numerical_mpmath.py`](verification/check_03_numerical_mpmath.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** Ratios at $R/\sigma = 0.01, 0.1, 0.5, 1, 2, 5, 10, 20$ confirmed. At $R/\sigma = 0.01$: ratio = $9.4030\times 10^{-8}$ (matches `derivation.md` to 5 decimals). At $R/\sigma = 20$: ratio = 1 to $< 10^{-40}$ (exponential recovery of point-mass law).

### Check 04 — Limit cases (SymPy)
- **Tool:** SymPy 1.14
- **Script:** [`verification/check_04_limits_sympy.py`](verification/check_04_limits_sympy.py)
- **Output:** [`verification/outputs/check_04.txt`](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** All four limits symbolically verified. Coefficient of $R^1$ in small-$R$ expansion of $F(R)$ is $Gm^2/(6\sqrt{\pi}\,\sigma^3)$ — confirms spring-like linear behavior near origin.

### Check 05 — Gauss-law cross-check of textbook Gaussian potential
- **Tool:** mpmath 30-digit quadrature
- **Script:** [`verification/check_05_textbook_crosscheck.py`](verification/check_05_textbook_crosscheck.py)
- **Output:** [`verification/outputs/check_05.txt`](verification/outputs/check_05.txt)
- **Result:** PASS
- **Notes:** Derives $\Phi(r)$ from scratch by (i) integrating $4\pi r'^2\rho(r')$ for enclosed mass, (ii) outward-integrating $GM(r')/r'^2$ with analytical tail correction. Max relative error vs textbook erf-formula: $7.6\times 10^{-24}$. Also confirms total mass conservation $M_{\mathrm{enc}}(10\sigma) = m$ to $10^{-10}$.

### Check 06 — Independent scipy double-integration
- **Tool:** scipy.integrate.dblquad 1.17
- **Script:** [`verification/check_06_scipy_numerical_integration.py`](verification/check_06_scipy_numerical_integration.py)
- **Output:** [`verification/outputs/check_06.txt`](verification/outputs/check_06.txt)
- **Result:** PASS
- **Notes:** Computes $U(R)$ directly from the 6D double integral (collapsed to 2D by spherical symmetry) at $R/\sigma \in \{0.1, 0.5, 1, 2, 5\}$, compares to closed form. Max relative error: $6.0\times 10^{-8}$ (quadrature-limited).

### Check 07 — Wolfram Engine cross-verification
- **Tool:** Wolfram Engine via wolframscript (Wolfram 14.x)
- **Script:** [`verification/check_07_wolfram.wls`](verification/check_07_wolfram.wls)
- **Output:** [`verification/outputs/check_07_wolfram.txt`](verification/outputs/check_07_wolfram.txt)
- **Result:** PASS
- **Notes:** Independent computer-algebra system verifies all four limits symbolically (`TrueQ` returns True for each) and reproduces the numerical sweep bit-for-bit identical to mpmath (e.g. ratio at $R=\sigma$: `0.08110858834532414` in both).

## Cross-tool agreement

- mpmath 50-digit and Wolfram 25-digit numerical values agree to at least 14 significant figures on every row of the sweep.
- SymPy and Wolfram symbolic limits agree on all four limit forms.
- scipy quadrature and closed form agree to $6\times 10^{-8}$ (quadrature floor).
- Gauss-law derivation and closed-form agree to $10^{-23}$ (mpmath floor).

No tool disagreements found.

## Tier assignment

- **🟢 Green** for the calculation itself — the overlap integral is exactly computed and verified by four independent methods.
- **🔴 Red** for the *amplification* reading originally proposed. The calculation falsifies that reading: the overlap integral reduces short-range force relative to the point-mass estimate rather than amplifying it. This is an honest failure of the aspirational claim, not a calculation error. See `claim.md` and `caveats.md` for implications.

## TODOs / Known gaps

- Wolfram MCP unavailable in this session; the Wolfram check was run via `wolframscript` (local Wolfram Engine) instead. If a Wolfram-MCP session becomes available, the check could be re-run through the MCP surface for audit parity.
- The SymPy simplification inside check_05 could not reduce the Ei/expint-form integral to the erf closed form by symbolic manipulation alone; the cross-check was therefore performed numerically rather than symbolically. The numerical agreement (rel.\ error $10^{-24}$) is definitive.
