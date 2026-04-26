# E3 — Derivation: Gradient-Gradient Correlation and Its Relation to VdW

## What this derivation sets out to do

**Test whether** the direct gradient-gradient correlation between two Gaussian density distributions reproduces the $1/R^6$ scaling of the Van der Waals (London dispersion) force at long range.

**Result:** It does not. The correlation is exponentially suppressed. The original naïve reading of E3 fails. A full GCM derivation of VdW requires an analog of the standard polarizability / fluctuating-dipole machinery; that has not been constructed.

This derivation documents the failure and clarifies what would be needed to make the claim rigorous.

## Gradient-gradient correlation — setup

Two identical isotropic Gaussian mass (or graviton-number) density distributions,
$$\rho_1(\mathbf{r}) = \frac{m}{(2\pi\sigma^2)^{3/2}}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma^2}\right), \qquad \rho_2(\mathbf{r}) = \rho_1(\mathbf{r}-\mathbf{R}).$$

The "gradient overlap" integral is
$$C(R) \equiv \int \nabla\rho_1(\mathbf{r}) \cdot \nabla\rho_2(\mathbf{r}-\mathbf{R})\,d^3r.$$

This is meant as the simplest operationalization of "graviton-density-gradient overlap" between two bodies. If this overlap carried the VdW physics, we would expect it to reproduce $C(R) \propto -1/R^6$ at long $R$.

## Computing $C(R)$

The cleanest approach is Fourier. Using
$$\rho(\mathbf{r}) = \int\frac{d^3k}{(2\pi)^3}\,\hat{\rho}(\mathbf{k})\,e^{i\mathbf{k}\cdot\mathbf{r}}, \qquad \hat{\rho}(\mathbf{k}) = m\,e^{-k^2\sigma^2/2},$$

gradients pick up a factor of $i\mathbf{k}$:
$$\widehat{\nabla\rho}(\mathbf{k}) = i\mathbf{k}\,\hat{\rho}(\mathbf{k}).$$

The gradient-gradient correlation becomes
$$C(R) = \int\frac{d^3k}{(2\pi)^3}\,|\mathbf{k}|^2\,|\hat{\rho}(\mathbf{k})|^2\,e^{-i\mathbf{k}\cdot\mathbf{R}}.$$

Since $|\hat{\rho}(\mathbf{k})|^2 = m^2 e^{-k^2\sigma^2}$, we have
$$C(R) = m^2\int\frac{d^3k}{(2\pi)^3}\,k^2\,e^{-k^2\sigma^2}\,e^{-i\mathbf{k}\cdot\mathbf{R}}.$$

Recognize this as a Laplacian of an inverse Fourier transform:
$$C(R) = -m^2\,\nabla_R^2\int\frac{d^3k}{(2\pi)^3}\,e^{-k^2\sigma^2}\,e^{-i\mathbf{k}\cdot\mathbf{R}} = -m^2\,\nabla_R^2\left[(4\pi\sigma^2)^{-3/2}\,e^{-R^2/(4\sigma^2)}\right].$$

Applying the 3D radial Laplacian to a Gaussian in $R$ gives
$$\nabla^2\,e^{-R^2/(4\sigma^2)} = \frac{R^2 - 6\sigma^2}{4\sigma^4}\,e^{-R^2/(4\sigma^2)}.$$

Therefore
$$\boxed{\,C(R) = \frac{m^2\,(6\sigma^2 - R^2)}{32\pi^{3/2}\,\sigma^7}\,\exp\!\left(-\frac{R^2}{4\sigma^2}\right).\,}$$

## Asymptotic behaviour

**Large $R$ ($R \gg \sigma$):** The Gaussian envelope dominates. $C(R)$ is exponentially suppressed: $C(R) \sim R^2\,e^{-R^2/(4\sigma^2)}$ up to constants.

**Zero-crossing:** $C(R) = 0$ at $R = \sigma\sqrt{6} \approx 2.449\,\sigma$. At larger $R$ the correlation becomes negative before decaying to zero.

**Small $R$ ($R \ll \sigma$):** $C(R) \approx \frac{6\,m^2}{32\pi^{3/2}\,\sigma^5} = \frac{3\,m^2}{16\pi^{3/2}\,\sigma^5}$. Constant at leading order, in the overlap regime.

## Numerical comparison to $1/R^6$ (from SymPy/NumPy)

For $m = \sigma = 1$:

| $R/\sigma$ | $C(R)$ | $1/R^6$ | $C(R)\,/\,(1/R^6)$ |
|---:|---:|---:|---:|
| 0.5 | $+3.031\times 10^{-2}$ | $64.0$ | $4.74\times 10^{-4}$ |
| 1.0 | $+2.185\times 10^{-2}$ | $1.000$ | $2.19\times 10^{-2}$ |
| 2.0 | $+4.129\times 10^{-3}$ | $1.56\times 10^{-2}$ | $0.264$ |
| 5.0 | $-2.058\times 10^{-4}$ | $6.40\times 10^{-5}$ | $-3.22$ |
| 10.0 | $-7.326\times 10^{-12}$ | $1.00\times 10^{-6}$ | $-7.33\times 10^{-6}$ |

- At $R = \sigma$, $C$ and $1/R^6$ differ by a factor of ~45.
- By $R = 10\sigma$, $C/(1/R^6) \sim 10^{-5}$ — the correlation has vanished exponentially while the VdW power-law is still substantial.
- The correlation also changes sign at $R \approx 2.45\sigma$; a true $1/R^6$ attraction never changes sign.

## What this shows

Gradient-gradient correlation of Gaussian density distributions does not, by itself, produce the VdW long-range $1/R^6$ attraction. The exponential decay plus sign change make the Gaussian correlation a fundamentally different object from the $1/R^6$ dispersion force.

## Why the naive reading fails

Looking back, this is not surprising. VdW-London dispersion is a **long-range** effect that depends on:

1. **Dipole fields falling off as $1/r^3$ in the Coulomb potential** — a power-law tail in the underlying interaction. Gaussians do not have power-law tails; they have Gaussian tails. The field from a Gaussian mass distribution at large distance is dominated by the monopole moment (total mass), and the dipole moment of an isotropic Gaussian is zero. So there is no dipole-field interaction at long range for symmetric Gaussians.
2. **Polarizability** — the distant body must respond to applied fields. Our correlation integral assumes both distributions are static and undeformed, with no response dynamics.
3. **Time-averaged fluctuations** — VdW at leading order arises from quantum zero-point fluctuations of the charge density. Our integral is static.

The naive gradient-overlap calculation misses all three ingredients.

## What a proper GCM derivation of VdW would look like

To actually derive VdW from GCM's graviton substrate, one would need to:

**Step 1 — Specify the fluctuation spectrum of the graviton density.** In GCM, every particle is a nucleated density pattern in a background substrate. Fluctuations around the mean pattern are the GCM analog of quantum zero-point motion. This requires specifying either (a) a noise spectrum for $\rho_g$ at each point, or (b) the commutation relations analog for graviton-field operators. Neither is done in the current GCM formalism.

**Step 2 — Define graviton-substrate polarizability.** In the presence of a gravitational gradient from body 2, body 1's density distribution should distort. The ratio of distortion to applied gradient is the gravitational polarizability $\alpha_g$. For a Gaussian distribution this is in principle computable (it's a variational problem: minimize the energy of the density distribution in the presence of an external field), but has not been done.

**Step 3 — Port the Casimir-Polder / London calculation.** With a fluctuation spectrum (step 1) and a polarizability (step 2), the standard derivation of $-C_6/r^6$ proceeds: fluctuation at body 1 creates a gradient field at body 2, polarizes body 2, and the resulting induced-dipole interaction with the source gives $1/r^6$ after time averaging. The structure is universal; only the numerical constants depend on the specifics.

**Step 4 — Verify coefficient.** The coefficient $C_6$ in GCM's derivation must match observed VdW coefficients (measured for many molecular pairs to few-percent accuracy). This would be a stringent test.

None of these four steps is presently complete. Step 1 in particular requires a theory of quantum-like fluctuations in GCM's deterministic substrate — which connects to superdeterminism and the T4 reinterpretation of "probability distribution" as real density. There is structural consonance in principle; execution is future work.

## Summary

- $C(R)$ for Gaussians: derived exactly.
- VdW $1/R^6$: *not* reproduced by direct gradient-gradient overlap.
- Proper derivation: requires fluctuation spectrum, polarizability, and Casimir-Polder machinery — none built in GCM.
- Honest E3 status: framing co-optation (yellow); derivation (red, pending step 1-4).

The coherence paper must state this gap transparently.
