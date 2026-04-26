# H2 — Verification Record

**Tally:** 4/4 runnable checks passed; 2 open gaps (equipartition, Planck's law) remain honestly flagged as red-tier UNSPEC-5.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory.

---

## Claim Summary

H2 is a **structural/symbolic** claim: the release-of-excess-graviton-density mechanism reproduces the *form* of Newton's law of cooling and of Fourier heat conduction. It does **not** reproduce equipartition ($C_V = \tfrac{3}{2}k_B T$) or Planck's law quantitatively; those remain red-tier UNSPEC-5 open problems.

The checks below verify the structural claim — that the ODE and PDE forms emerge correctly from the release / diffusion assumptions. They do not verify the underlying physical assumptions (proportional-release, density-temperature mapping) from first principles.

---

## Check 01 — Newton's cooling ODE solution via SymPy
- **Tool:** SymPy 1.14.0 `dsolve`
- **Script:** [`verification/check_01_cooling_ode_sympy.py`](verification/check_01_cooling_ode_sympy.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** SymPy solves $d\rho_g/dt = -\lambda(\rho_g - \rho_0)$ with IC $\rho_g(0) = \rho_{\text{init}}$ and returns exactly the claimed closed form $\rho_g(t) = \rho_0 + (\rho_{\text{init}} - \rho_0)e^{-\lambda t}$. Excess form and $t\to\infty$ equilibrium limit also verify.

## Check 02 — Fourier heat equation structure via SymPy vector calculus
- **Tool:** SymPy 1.14.0 `sympy.vector` (CoordSys3D, divergence, gradient)
- **Script:** [`verification/check_02_fourier_pde_sympy.py`](verification/check_02_fourier_pde_sympy.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Starting from continuity $\partial_t \rho_g = -\nabla\cdot J_g$ and the diffusive flux $J_g = -D\nabla\rho_g$, SymPy's symbolic `divergence` produces exactly $D\,\nabla^2\rho_g = D(\partial_x^2 + \partial_y^2 + \partial_z^2)\rho_g$. The Fourier heat equation emerges as claimed.

## Check 03 — Numerical exponential cooling (mpmath)
- **Tool:** mpmath 1.3.0 at 40-digit precision
- **Script:** [`verification/check_03_cooling_numerical.py`](verification/check_03_cooling_numerical.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** With synthetic inputs ($\rho_0=1$, $\rho_{\text{init}}=5$, $\lambda=0.5$), confirms excess ratio at sample times matches $e^{-\lambda t}$ to 30+ digits. At $t = \tau = 1/\lambda = 2$, excess equals initial excess × $e^{-1}$ (= 1.4715...) exactly. Monotonic decay verified across 6 sample times.

## Check 04 — Wolfram Engine independent cross-check
- **Tool:** Wolfram Language Engine 14.3.0 (local `wolframscript`)
- **Script:** [`verification/check_04_wolfram.wls`](verification/check_04_wolfram.wls)
- **Output:** [`verification/outputs/check_04_wolfram.txt`](verification/outputs/check_04_wolfram.txt)
- **Result:** PASS (3 sub-checks: ODE form, asymptotic limit under λ>0 and real-valued assumptions, PDE derivation)
- **Notes:** Wolfram's `DSolve` returns the same closed form as SymPy; `Limit[..., t -> Infinity]` → 0 under `λ > 0, ρ_0, ρ_init ∈ Reals`; the PDE reduction from continuity + diffusive flux to $D\nabla^2\rho$ matches exactly.

**Cross-tool agreement:** SymPy (`dsolve`) and Wolfram (`DSolve`) return identical symbolic solutions. SymPy and Wolfram vector-calculus PDE derivations agree. No cross-tool disagreement.

---

## Honesty Flags (Open — unchanged by this retrofit)

These were already red-tier in the original claim and remain so. Verification of these does NOT apply because they are explicitly outside H2's scope:

- **Equipartition $C_V = \tfrac{3}{2}k_B T$** — NOT derived from graviton-release statistics. Open (UNSPEC-5).
- **Planck distribution $B(\nu, T) = \frac{2h\nu^3/c^2}{e^{h\nu/kT}-1}$** — NOT derived. Only a qualitative directional-consistency analogy. Open (UNSPEC-5).
- **Density-temperature mapping $T \propto \rho_g - \rho_0$** — asserted, not derived. Structural consistency of the ODE/PDE forms assumes this mapping.
- **Rate constant $\lambda$ and thermal diffusivity $D$** — not derived from graviton properties.

The 4/4 passing checks confirm the *structural consistency* of the release mechanism with Newton's cooling and Fourier heat conduction; they do NOT promote the claim beyond yellow-tier plausibility.

## TODOs

- When a graviton-release statistics model is developed, an equipartition-reproduction check becomes possible and H2 could move toward green.
- Blackbody spectrum reproduction (Planck's law from graviton dynamics) is a larger open program.

---

## Running the Full Suite

```bash
cd verification
../../_verification-env/venv/bin/python check_01_cooling_ode_sympy.py   | tee outputs/check_01.txt
../../_verification-env/venv/bin/python check_02_fourier_pde_sympy.py   | tee outputs/check_02.txt
../../_verification-env/venv/bin/python check_03_cooling_numerical.py   | tee outputs/check_03.txt
wolframscript -file check_04_wolfram.wls                                | tee outputs/check_04_wolfram.txt
```

Constants and synthetic inputs live in [`verification/inputs.json`](verification/inputs.json).
