# R1 — Plausibility

## Structural Argument

In GCM's ontology, space is not a passive backdrop — it is a graviton substrate with density $\rho_g$ and internal dynamics. A photon is a traveling graviton-cluster structure. Any traveling structure in a medium with internal dynamics will couple to that medium at some level; the question is the strength of the coupling.

Space friction is the hypothesis that this coupling produces energy loss. The energy loss per unit distance is small (otherwise we would see distortions in nearby laboratory light), but accumulates over cosmological distances.

## Dimensional Constraint

For $z \sim 1$ at distances of order the observable-universe radius $R_{\text{obs}} \approx 4.4 \times 10^{26}$ m (the particle horizon), the required friction coefficient is:

$$\alpha \sim \frac{1}{R_{\text{obs}}} \approx 2.3 \times 10^{-27} \text{ m}^{-1}$$

Note: $c/H_0 \approx 1.32 \times 10^{26}$ m (the Hubble radius) is a factor ~3.3 smaller than the particle horizon. Correspondingly $H_0/c \approx 7.57 \times 10^{-27}$ m⁻¹ differs from $1/R_{\text{obs}}$ by the same factor. Both are legitimate "cosmological length scales"; R1 is parametrized at the observable-universe scale here, but any Hubble-law fit to data over the full cosmological range will distinguish the two conventions and pin the correct length scale from data. Verified in `verification/check_01_hubble_radius_and_alpha.py` + `.wls`.

**Order-of-magnitude sketch (not a derivation):**

If the coupling is per-graviton-encounter with cross-section $\sigma_g$ and the graviton number density in vacuum is $n_g$, then $\alpha \sim n_g \cdot \sigma_g$. Using the observable-universe Planck-cell count from M3: $V_{\text{obs}} = (4/3)\pi R_{\text{obs}}^3 \approx 3.57 \times 10^{80}$ m³ and $N_{\text{gravitons}} \sim 10^{185}$, so $n_g \approx 2.8 \times 10^{104}$ m⁻³. Then $\sigma_g \sim \alpha / n_g \approx 8 \times 10^{-132}$ m² per graviton. This is an extraordinarily small cross-section — but not obviously unphysical given the graviton's postulated unit mass at the Planck scale. Verified in `verification/check_02_graviton_density_and_cross_section.py` + `.wls`.

This is a *consistency check*, not a derivation. An actual derivation would need to specify the coupling mechanism between a photon-cluster and the surrounding substrate.

## The Time-Dilation Companion (R6)

R1 alone would reproduce classical tired light — ruled out at ~200σ by DES 2024. R1 requires R6 (photon-structure geometric time dilation) to survive the SNe Ia $(1+z)^{1.003 \pm 0.005}$ constraint.

The R6 argument: as energy decreases, the photon's internal graviton-cluster spacing increases proportionally (by GCM's wavelength-spacing correspondence, L3). Increased spacing means longer internal information-propagation times. The photon's intrinsic clock ticks slower. If $\lambda \propto (1+z)$ and internal spacing $\propto \lambda$, then time dilation $\propto (1+z)$. This is the same cascade that any R1–R5 mechanism uses for time dilation.

**R1 + R6 is not tired light.** Tired light predicts no time dilation. R1 + R6 predicts $(1+z)$ time dilation via a geometric mechanism that does not depend on friction producing the dilation — the friction produces the energy loss; the resulting structural change produces the dilation.

## Where Plausibility Falls Off

- **No specific coupling mechanism.** The friction coefficient is dimensionally fixable but not derived. "Coupling to the substrate" is a placeholder for physics that has not been written down.
- **Homogeneity assumption.** Space friction implicitly assumes a homogeneous graviton density. But in GCM, matter = density structure, so the substrate is not homogeneous. If $\alpha$ depends on local density, redshift becomes path-dependent, which would produce scatter in the Hubble diagram. This is a constraint, not a disqualifier.
- **Spectral distortion risk.** Friction that couples photons to the substrate is likely to produce frequency-dependent effects. A pure $\alpha \cdot E$ friction is frequency-independent; a coupling that depends on photon wavelength would distort blackbody spectra. See `empirical-check.md`.
