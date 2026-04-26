# E3 — Verification Record

**Tally:** 5/5 checks passed.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory. Constants in [`verification/inputs.json`](verification/inputs.json).

## Result summary

The claim's computational core — the gradient-gradient correlation of two Gaussian mass distributions — is
$$C(R) = \frac{m^2(6\sigma^2 - R^2)}{32\pi^{3/2}\sigma^7}\exp\!\left(-\frac{R^2}{4\sigma^2}\right).$$
SymPy and Wolfram Engine both derive this identically. The zero crossing at $R = \sigma\sqrt{6}$ is confirmed symbolically and numerically. Three independent numerical methods (mpmath at 50 dps, scipy 3D quadrature, Wolfram Engine) agree on values across the sweep $R/\sigma \in [0.5, 20]$ to quadrature precision.

**The headline E3 claim is a negative result:** $C(R)$ is *not* a power law. Large-$R$ behavior is exponential ($\sim R^2 e^{-R^2/4\sigma^2}$), so it cannot reproduce the $1/R^6$ scaling of the London dispersion force. At $R = 20\sigma$, $R^6\,C(R) \sim 5\times 10^{-36}$ (vanishingly small), while a power-law tail would give a finite constant. The asymptotic shape is definitively exponential. This rules out the naïve "gradient overlap reproduces VdW" reading — exactly the outcome documented in the claim.

## Per-check detail

### Check 01 — Dimensional analysis
- **Tool:** Python + Pint 0.25
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** Confirms $C(R)$ has units of $[\rho]^2 \cdot \text{length} = \mathrm{kg}^2/\mathrm{m}^5$. Also clarifies that this is *dimensionally distinct* from the VdW coefficient $C_6$ (units $\mathrm{J\,m}^6$), so the "$C(R)$ vs $1/R^6$" comparison is a *shape* comparison, not a dimensional match — exactly as the claim states.

### Check 02 — Symbolic derivation of $C(R)$ (SymPy)
- **Tool:** SymPy 1.14
- **Script:** [`verification/check_02_sympy_correlation.py`](verification/check_02_sympy_correlation.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Derives $C(R)$ via the Fourier identity $C = -\nabla^2(\rho_1 * \rho_2)$. The auto-convolution is Gaussian of width $\sigma\sqrt 2$; applying the 3D radial Laplacian reproduces the expected closed form exactly (symbolic difference = 0). Zero crossing at $R = \sigma\sqrt 6$ confirmed.

### Check 03 — High-precision numerical sweep (mpmath)
- **Tool:** mpmath 1.3.0 at 50-digit precision
- **Script:** [`verification/check_03_numerical_mpmath.py`](verification/check_03_numerical_mpmath.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** Reproduces Session C numerical table exactly. At $R/\sigma = 1$: $C = 2.18535\times 10^{-2}$. At $R = \sqrt{6}\,\sigma$: $C = 0$ to $< 10^{-40}$. At $R = 20\sigma$: $C/(1/R^6) \approx 5\times 10^{-36}$ (effectively zero — exponential wins over polynomial). Sign flip at $R = \sigma\sqrt 6$ verified.

### Check 04 — Direct 3D integration (scipy)
- **Tool:** scipy.integrate.dblquad 1.17
- **Script:** [`verification/check_04_scipy_direct_integration.py`](verification/check_04_scipy_direct_integration.py)
- **Output:** [`verification/outputs/check_04.txt`](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** Numerically integrates $\int\nabla\rho_1 \cdot \nabla\rho_2\,d^3r$ directly (via cylindrical-coordinate reduction exploiting axial symmetry), avoiding the Fourier-trick. Agrees with the closed form to max rel.\ error $8.3\times 10^{-5}$. The threshold is set at $10^{-3}$ because gradient-gradient integrands have near-cancellation in the overlap region (both grads point along similar directions); tighter precision requires specialized integration methods. Three orders of magnitude of agreement is still definitive for a cancelling integral.

### Check 05 — Wolfram Engine cross-verification
- **Tool:** Wolfram Engine via `wolframscript`
- **Script:** [`verification/check_05_wolfram.wls`](verification/check_05_wolfram.wls)
- **Output:** [`verification/outputs/check_05_wolfram.txt`](verification/outputs/check_05_wolfram.txt)
- **Result:** PASS
- **Notes:** Independent CAS reproduces the closed form ($\mathtt{FullSimplify[Cclosed - expected]} = 0$ under $\sigma > 0$ assumption). Numerical sweep matches mpmath exactly (e.g., $C(1) = 0.021853529896971834$ in both). The asymptotic shape check $R^6\,C(R)$ at $R = 20$ returns $-5.26\times 10^{-36}$, confirming exponential (not power-law) decay.

## Cross-tool agreement

- **Symbolic:** SymPy and Wolfram both produce the same closed form, bit-for-bit identical after simplification with $\sigma > 0$.
- **Numerical:** mpmath and Wolfram sweep values agree to 15+ significant figures (e.g., $C(1) = 0.021853529896971834$ in both).
- **Direct integration:** scipy dblquad reproduces the closed form to within quadrature precision (cancellation-limited, $8\times 10^{-5}$ at worst).

No tool disagreements found.

## Honesty flag — what this verification does NOT confirm

The verification confirms that $C(R)$ as computed (the Fourier-trick derivation of gradient-gradient correlation for two Gaussian distributions) is exactly the closed form in `derivation.md`, and that its asymptotic behavior is exponential rather than $1/R^6$. **That is the negative result.**

What the verification does NOT do — and cannot do until substantial new physics is specified — is verify a *positive* graviton-substrate derivation of VdW. The four steps listed in `caveats.md` (fluctuation spectrum, gravitational polarizability, Casimir-Polder analog, numerical $C_6$ match) are all future work. No scripts exist for them.

## Tier assignment

- **🟢 Green for the computation itself.** The gradient-gradient correlation is exactly computed; its asymptotic shape is definitively exponential.
- **🔴 Red for the "direct overlap reproduces $1/R^6$" reading.** Falsified at the level of functional form, not just numerical value. Exponential $\neq$ power law at any $R$.
- **🟡 Yellow for the framing co-optation.** The claim "GCM's universal attraction ontology is consistent with observed VdW universality" remains a compatibility statement that survives the negative result — the failure of the naïve derivation does not refute the framing. See `claim.md` for the honest reading.

## TODOs / Known gaps

- Wolfram MCP unavailable in this session; Wolfram check ran via local `wolframscript`.
- No script for the positive direction (graviton fluctuation spectrum → polarizability → Casimir-Polder $C_6$). This would require GCM-specific machinery (quantum-like fluctuation theory in a deterministic substrate, Gaussian polarizability under applied tidal gradient) that has not been built.
