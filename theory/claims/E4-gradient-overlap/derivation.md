# E4 — Derivation: Overlap Integral for Two Gaussian Mass Distributions

## Setup

Two identical isotropic Gaussian mass distributions, each of total mass $m$ and characteristic width $\sigma$, centered at $\mathbf{r} = \mathbf{0}$ and $\mathbf{r} = \mathbf{R}$ respectively:

$$\rho_1(\mathbf{r}) = \frac{m}{(2\pi\sigma^2)^{3/2}}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma^2}\right), \qquad \rho_2(\mathbf{r}) = \rho_1(\mathbf{r} - \mathbf{R}).$$

Newtonian gravitational interaction energy between the two distributions:

$$U(R) = -G \int\int \frac{\rho_1(\mathbf{r}_1)\,\rho_2(\mathbf{r}_2)}{|\mathbf{r}_1 - \mathbf{r}_2|}\,d^3r_1\,d^3r_2 \,.$$

## Step 1 — Gravitational potential of a single Gaussian

The gravitational potential at distance $r$ from the center of a single Gaussian mass distribution is a standard result (Gauss's law applied in spherical coordinates, then integrating the enclosed-mass function):

$$\Phi(r) = -\frac{Gm}{r}\,\mathrm{erf}\!\left(\frac{r}{\sigma\sqrt{2}}\right).$$

Sanity checks (confirmed symbolically):
- $\Phi(r \to 0) = -\dfrac{\sqrt{2}\,Gm}{\sigma\sqrt{\pi}}$ (finite)
- $\Phi(r \to \infty) = -\dfrac{Gm}{r}$ (recovers point-mass potential)

## Step 2 — Interaction energy as potential integrated against second mass

$$U(R) = \int \rho_2(\mathbf{r})\,\Phi(\mathbf{r})\,d^3r = \int \rho_1(\mathbf{r}-\mathbf{R})\,\Phi(\mathbf{r})\,d^3r.$$

Exploiting the convolution property of Gaussians, the product of two Gaussians of width $\sigma$ is proportional to a Gaussian of width $\sigma\sqrt{2}$. After the standard calculation (see e.g. Cygankiewicz & Zurek for the Gaussian–Gaussian gravitational energy, or Gradshteyn & Ryzhik 3.321.3 for the underlying integral), the result simplifies to

$$\boxed{\,U(R) = -\frac{Gm^2}{R}\,\mathrm{erf}\!\left(\frac{R}{2\sigma}\right).\,}$$

The characteristic scale inside the error function is $2\sigma$ (not $\sigma\sqrt{2}$) because the convolution of two $\sigma$-Gaussians has width $\sigma\sqrt{2}$, and the erf argument then carries a factor $1/\sqrt{2}$ from the potential formula, yielding $2\sigma$ in the denominator.

## Step 3 — Limiting behaviour

**Small $R$ (deep overlap).** Taylor-expand $\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}}(x - x^3/3 + \ldots)$:

$$U(R) = -\frac{Gm^2}{\sigma\sqrt{\pi}}\left(1 - \frac{R^2}{12\sigma^2} + O(R^4)\right), \qquad R \ll \sigma.$$

This is bounded: $U(0) = -Gm^2/(\sigma\sqrt{\pi})$. The $1/R$ divergence of the point-mass potential is removed by the extended-mass structure.

**Large $R$ (well-separated).** $\mathrm{erf}(R/2\sigma) \to 1$, so

$$U(R) \to -\frac{Gm^2}{R}, \qquad R \gg \sigma.$$

Point-mass behaviour is recovered, as required for a self-consistent extended-particle theory.

## Step 4 — Force

$$F(R) = -\frac{dU}{dR} = \frac{Gm^2}{R^2}\,\mathrm{erf}\!\left(\frac{R}{2\sigma}\right) - \frac{Gm^2}{R\,\sigma\sqrt{\pi}}\,\exp\!\left(-\frac{R^2}{4\sigma^2}\right).$$

(Here $F$ is the magnitude of the attractive force between the two distributions, along the line joining their centers; sign convention: positive $F$ means attractive.)

**Small $R$ expansion.** Using Taylor expansions in the formulae above,

$$F(R) = \frac{Gm^2}{\sigma^3\sqrt{\pi}}\left(\frac{R}{6} - \frac{R^3}{40\sigma^2} + O(R^5)\right), \qquad R \ll \sigma.$$

So $F(R)$ is **linear in $R$ for small $R$** — it *vanishes* as the two distributions become concentric, rather than diverging as the point-mass formula $Gm^2/R^2$ would suggest. This is the regularization of the short-range singularity.

**Large $R$ behaviour.** $F(R) \to Gm^2/R^2$, recovering Newton's law.

## Step 5 — Ratio to naive point-particle force

Let $F_{\rm pt}(R) = Gm^2/R^2$ be the naive point-particle force.

$$\frac{F(R)}{F_{\rm pt}(R)} = \mathrm{erf}\!\left(\frac{R}{2\sigma}\right) - \frac{R}{\sigma\sqrt{\pi}}\exp\!\left(-\frac{R^2}{4\sigma^2}\right).$$

Numerical values (computed in `verification.md`) for $G = m = \sigma = 1$:

| $R/\sigma$ | $F(R)$ | $F_{\rm pt}(R)$ | $F/F_{\rm pt}$ |
|---:|---:|---:|---:|
| 0.01 | $9.40\times 10^{-4}$ | $1.00\times 10^{4}$ | $9.40\times 10^{-8}$ |
| 0.10 | $9.39\times 10^{-3}$ | $1.00\times 10^{2}$ | $9.39\times 10^{-5}$ |
| 0.50 | $4.53\times 10^{-2}$ | $4.00$ | $1.13\times 10^{-2}$ |
| 1.00 | $8.11\times 10^{-2}$ | $1.00$ | $8.11\times 10^{-2}$ |
| 2.00 | $1.07\times 10^{-1}$ | $2.50\times 10^{-1}$ | $4.28\times 10^{-1}$ |
| 5.00 | $3.98\times 10^{-2}$ | $4.00\times 10^{-2}$ | $9.94\times 10^{-1}$ |
| 10.0 | $1.00\times 10^{-2}$ | $1.00\times 10^{-2}$ | $1.00$ |

At $R = 0.01\sigma$ the overlap force is **eight orders of magnitude weaker** than the naive point-particle force; at $R = 10\sigma$ the two agree to 1 part in $10^3$.

## Physical interpretation

The integral over the overlap region *does* involve many graviton–graviton pairs interacting at near-zero separation. But those pair interactions are **isotropic** inside the overlap region: every pair at small separation $s$ contributes a force $Gm_g^2/s^2$ pointing in a direction that — when summed over all pairs symmetric about the overlap center — produces zero net force on the center of mass. The short-range contributions bind the distributions (they show up as increased *binding energy*, i.e. more-negative $U$) but cancel as a net center-to-center force. This is Newton's shell theorem generalized to continuous distributions.

Translated to GCM: overlap produces strong *internal* binding within the overlap region (of order $-Gm^2/(\sigma\sqrt{\pi})$, which is substantial), but it does not amplify the *external* force one object exerts on the other's center of mass. The hoped-for $10^{36}$ amplification of the inter-particle force cannot come from this mechanism.

## The structural gap, precisely named

The E4 claim *as originally proposed in Wisdom's 2026-04-23 speech* — that overlap makes "gravity as weak as it is" locally produce "meaningful grounds for attraction" of the magnitude observed in EM — requires that the **effective force between two overlapping extended masses exceed the point-mass estimate** at short range. The exact calculation for Newtonian gravity + Gaussian densities shows it **falls below** the point-mass estimate at short range. The gap is not a quantitative tuning issue; it is the wrong sign of the overlap effect for the claim.

Closing this gap requires one of:

1. **A nonlinear coupling.** E.g. replace $F \propto \rho_1\rho_2$ in the integrand with $F \propto f(\rho_1,\rho_2)$ where $f$ grows faster than linearly in each density. No first-principles GCM derivation for this is in hand.
2. **A contact-only interaction.** If gravitons interact only when adjacent (zero range), the interaction energy scales as the overlap integral $\int \rho_1\rho_2\,dV$ without the $1/|r_1-r_2|$ kernel. At $R \ll \sigma$ this is indeed large (~$m^2/\sigma^3$). But this breaks long-range Newtonian gravity — the $1/R^2$ force would not emerge at $R \gg \sigma$. Inconsistent with T2 as currently read.
3. **A substrate-density-dependent $G$.** If $G \to G(\rho_{\rm local})$ with $G$ growing at high local density, overlap regions see stronger coupling. No GCM machinery to specify $G(\rho)$ yet.

All three are future-work directions. None are presently available. The coherence paper must flag this honestly.
