# E4 — Caveats

## What the calculation does and does not prove

### What it does prove
- The Newtonian gravitational interaction energy between two identical Gaussian mass distributions is exactly $U(R) = -(Gm^2/R)\,\mathrm{erf}(R/2\sigma)$.
- Extended-mass distributions regularize the $1/R$ singularity of the point-mass potential. Interaction energy is bounded at $R=0$.
- At $R \ll \sigma$, the inter-center force is *smaller*, not larger, than the point-particle estimate $Gm^2/R^2$.
- At $R \gg \sigma$, the point-particle result is recovered to high accuracy.

### What it does not prove
- **It does not prove that GCM's unification of forces fails.** GCM may have mechanisms outside the strictly Newtonian regime (non-linear graviton coupling, density-dependent $G$, contact-only interactions) that produce the hoped-for short-range amplification. The calculation only shows that the *simplest* reading of E4, using standard Newtonian gravity applied to extended densities, does not amplify.
- **It does not specify the particle width $\sigma$.** GCM has no derivation of $\sigma_{e}$, $\sigma_{p}$, or $\sigma_{\gamma}$ from first principles. Without $\sigma$, the numerical regime $R/\sigma$ is undetermined.
- **It does not address real particle shapes.** Real quantum particles are not Gaussians. Electron clouds in atoms have complicated radial and angular structure; protons have quark substructure. The Gaussian is a toy model to demonstrate the *functional behavior* of overlap integrals.

## Limitations of the Gaussian model

1. **Gaussians have no hard edge.** Real density distributions may fall off faster (exponential) or slower (power-law); this changes the asymptotic force. For distributions falling as $\rho \sim e^{-r/\lambda}/r$ (hydrogen-like), the overlap integral has different short-range behavior.
2. **Spherical symmetry is assumed.** Non-spherical distributions (any particle with intrinsic angular momentum, quadrupole moment, polarization) produce angle-dependent forces that the Gaussian model misses.
3. **Two-body only.** Many-body overlap regions (e.g. inside a nucleus) have interactions that cannot be reduced to pairwise Gaussian overlaps. Coulombic screening analogs may further modify the short-range force.

## Limitations of the Newtonian reading

1. **GR effects ignored.** At high density, general-relativistic corrections become important. Standard Newtonian gravity is an approximation; the overlap integral in a GR-consistent theory is not trivially the same as what we computed.
2. **Graviton-graviton coupling assumed linear.** If gravitons couple non-linearly (e.g. each graviton's mass modifies the local metric which modifies the coupling of nearby gravitons), the overlap integral takes a different form. GCM has not specified this coupling.
3. **No propagation delay.** Newtonian gravity acts instantaneously. In a realistic graviton-field theory, propagation has finite speed; near-overlap dynamics could involve retardation effects.

## Known mismatches with Wisdom's 2026-04-23 speech

Wisdom's speech said: "*if everything is just real distributions of gravitons of point particles right then those particle those particle distributions are going to overlap and they're going to be touching and so gravity can be as weak as it is but you have pieces of each particle like massively overlapping and touching which would be meaningful grounds for attraction right*."

The calculation shows:
- The "pieces overlapping and touching" contribute to *binding* (increased negative interaction energy, bounded at $U(0) = -Gm^2/(\sigma\sqrt\pi)$).
- They do not contribute to the *net inter-center force*, which is in fact reduced by the overlap.
- The intuition "pieces overlapping produces meaningful attraction" is correct for *binding energy* (a true positive result) but incorrect for *force-magnitude amplification at short range* (the problematic reading).

This is not a trivial difference. The coherence paper should state the positive result (binding energies are substantial and could provide stable-configuration energetics) and separately name the failed amplification reading.

## Honesty notes for the paper

1. The GCM "unification via overlap amplification" argument, as originally framed, requires a mechanism outside Newtonian gravity + extended densities. This gap is now *localized and named*, not hand-waved.
2. The regularization result (bounded $U$ at overlap) is a *positive* consequence of GCM's extended-particle ontology. It eliminates one species of infinity (self-energy divergence of point masses) for free. This is worth claiming.
3. The linear growth of $F(R)$ at small $R$ (harmonic-oscillator-like near $R = 0$) is interesting: it means overlapping Gaussian distributions behave like a spring at small separation. This could plausibly matter for nuclear-scale physics where densities are maximal.

## Future work required to rescue the amplification reading

One of the following must be done:

1. **Specify a density-dependent $G$.** Derive $G(\rho)$ from GCM's graviton substrate. Natural candidate: $G(\rho) \propto \rho^{n}/\rho_{\max}^{n}$ for $\rho \leq \rho_{\max}$, producing short-range amplification. Requires principled derivation from T1–T4.
2. **Specify a non-linear gravitational-force law.** Replace $F \propto \rho_1\rho_2/r^2$ with $F \propto (\rho_1\rho_2)^{\alpha}/r^{\beta}$ for some $\alpha, \beta$. Derive from the graviton substrate.
3. **Specify a contact interaction component.** Decompose the total force as long-range $1/r^2$ plus short-range contact-like, with the contact term producing the needed amplification. Show consistency with observed Newtonian gravity at all macroscopic scales.

Until one of these is specified, E2 (competing attraction as electron repulsion) cannot be quantitatively viable with gravitational interaction alone.
