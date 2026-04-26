# R3 — Plausibility

## Structural Argument

GCM's T3 claims the universe is converging. Convergence implies a center (or centers) of gravitational attraction. If we are not at that center, we sit in a gravitational potential different from the center's, and light from sources at different distances and directions arrives with different gravitational redshift contributions.

The simplest version: assume a single cosmological convergence center at position $\vec{r}_c$. Our position is at $\vec{r}_o$, distance $d_o = |\vec{r}_o - \vec{r}_c|$ from the center. A source at position $\vec{r}_s$, distance $d_s = |\vec{r}_s - \vec{r}_c|$. The potential difference between source and observer determines the gravitational redshift:

$$1 + z = \frac{1 + \Phi(\vec{r}_s)/c^2}{1 + \Phi(\vec{r}_o)/c^2} \approx 1 + \frac{\Delta\Phi}{c^2}$$

If $\Phi$ decreases with distance from the center (sources far from the center sit in shallower wells than we do), then $\Delta\Phi > 0$ and distant sources appear redshifted.

## Why Gravitational Redshift is Attractive

Gravitational redshift is a textbook GR effect. It automatically comes with time dilation — a photon emitted at potential $\Phi_s$ and observed at $\Phi_o$ arrives with both its wavelength stretched by $(1 + \Delta\Phi/c^2)$ and its temporal structure stretched by the same factor. This addresses the SNe Ia $(1+z)^{1.003}$ time-dilation constraint naturally.

In contrast, R1, R2, R4, R5 all require a separate time-dilation mechanism (R6). R3 does not. This is R3's structural advantage.

## The Hard Requirements

For R3 to reproduce the observed Hubble relation:

1. **Anisotropy.** The cosmological potential must have a specific gradient direction. Sources in one direction should be differently redshifted than sources in another.
2. **Magnitude.** The gradient must be of order $cH_0 \approx 6.8 \times 10^{-10}$ m/s² at the Hubble scale (verified in `verification/check_01_gradient_magnitude.py` + `.wls`). **Suggestively, this is within a factor ~5 of the MOND acceleration scale $a_0 \approx 1.2 \times 10^{-10}$ m/s²** (Milgrom 1983, the threshold below which galaxy rotation curves deviate from Newtonian predictions). The "Hubble coincidence" between $cH_0$ and MOND's $a_0$ is well-known in the modified-gravity literature and hints at possible overlap between R3's required cosmological anisotropy and MOND-scale phenomenology — worth exploring if R3 is developed further.
3. **Structure.** The potential shape must reproduce the linear Hubble relation $z \propto d$ at low $z$ and the observed nonlinear departures at high $z$.

## The Isotropy Problem

The observed universe is isotropic to very high precision:

- **CMB temperature anisotropies** are at the $10^{-5}$ level (after subtracting the dipole).
- **Large-scale structure** surveys show no statistically significant preferred direction beyond known local effects (Great Attractor, local flow).
- **SNe Ia Hubble diagram residuals** are consistent with isotropy within current precision.

For R3 to survive, either:
(a) The convergence center is very far away, and we are in a region where the potential is approximately flat locally — but then the gradient is small and R3 cannot produce the observed Hubble redshift.
(b) The anisotropy is there but subtle, hidden within what is currently attributed to peculiar velocities and local structure.
(c) We are *very close* to the convergence center, in which case the anisotropy is small in our local patch but grows at cosmological scales.

None of these is a comfortable position. (a) contradicts R3's purpose; (b) requires finding a signal that has been missed; (c) is an anthropic coincidence (why are we near the center?).

## The CMB Dipole

The CMB dipole (3.36 mK) is the dominant CMB anisotropy. It is currently attributed to our peculiar velocity (~369 km/s relative to the CMB rest frame) — i.e., a kinematic Doppler effect. Standard analysis subtracts this dipole before studying higher-$\ell$ anisotropies.

If R3 is correct, part of this dipole is *gravitational* (the line of sight toward the convergence center has a different gravitational potential than the line of sight away from it). The kinematic interpretation would need to be revised. This is testable in principle: the gravitational dipole has a different frequency dependence than the kinematic one.

**Recent result to check:** In 2021, Secrest et al. found the dipole in quasar and galaxy counts does not align with the CMB dipole at the expected magnitude — a 4.9σ discrepancy. This is unresolved in standard cosmology. Whether R3 can explain this is an open question, but the existence of the anomaly is suggestive.

## Where Plausibility Falls Off

- **No quantitative model of the convergence center.** Where is it? How far are we from it? What does the potential structure look like? None of these has been specified in GCM.
- **No measurement of the predicted gravitational anisotropy.** The anisotropy needed to reproduce $H_0$ has not been found in any current survey.
- **Strong isotropy constraints.** Current observational bounds on large-scale anisotropy are stringent. R3 must fit within them.
- **Fine-tuning problem.** Why should the convergence center happen to be positioned such that the potential gradient gives exactly $H_0$ at our location?

The honest statement: R3 is a coherent *type* of mechanism but lacks the specificity needed to evaluate quantitatively. It is a placeholder for a family of possibilities, not a defined mechanism.
