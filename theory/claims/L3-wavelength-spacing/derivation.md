# L3 — Derivation: Dimensional Argument

**Claim code:** L3
**Date:** 2026-04-23

---

## Setup

In GCM, a photon is a traveling density-structure of gravitons. The structure has:
- Total extent along the direction of propagation: the photon's wavelength $\lambda$ (meters)
- Internal periodicity: successive density peaks ("graviton clusters") separated by spacing $d$ (meters)
- Number of cluster periods per wavelength: $N$ (dimensionless integer)

The relationship, by construction:

$$\lambda = N \cdot d$$

Equivalently:

$$d = \frac{\lambda}{N}$$

---

## Dimensional Check

Both $\lambda$ and $d$ have units of length [m]. $N$ is dimensionless. The equation $\lambda = N \cdot d$ is dimensionally consistent:

$$[\lambda] = [\text{m}], \quad [N] = [1], \quad [N \cdot d] = [1] \cdot [\text{m}] = [\text{m}] ✓$$

---

## What Scales Proportionally

**Case A: $N$ is a fixed structural constant.** If the graviton cluster structure of a photon is invariant — every photon has the same number of clusters per wavelength, independent of wavelength — then $N$ does not change when $\lambda$ changes, and $d$ scales linearly with $\lambda$:

$$\frac{d_{\text{obs}}}{d_{\text{emit}}} = \frac{\lambda_{\text{obs}}}{\lambda_{\text{emit}}}$$

This is what R6 requires.

**Case B: $N$ depends on wavelength.** If $N = N(\lambda)$, then $d = \lambda / N(\lambda)$ and the scaling is not linear. R6's argument fails in this case, since the time-dilation factor would inherit $N(\lambda)$'s functional dependence.

**GCM commits to Case A as the minimal assumption.** No mechanism in GCM introduces a wavelength-dependent cluster count. The photon's internal structure is built once at emission and persists (modulo stretching/compression from redshift/blueshift) during propagation. This is the simplest hypothesis consistent with GCM's ontology.

---

## Constructing Other Length Scales (Sanity Check)

Could $d$ be set by something other than $\lambda$? Using the available dimensional inputs — $\lambda$, $m_g$ (graviton mass), $c$ (speed of light), $\hbar$ (Planck's constant) — the candidate length scales are:

| Candidate | Expression | Value (using $m_g \sim 10^{-87}$ kg) |
|-----------|-----------|--------------------------------------|
| Photon wavelength | $\lambda$ | 400–700 nm (visible) |
| Graviton Compton length | $\hbar / (m_g c)$ | $\sim 10^{41}$ m (larger than the universe) |
| Planck length | $\sqrt{\hbar G / c^3}$ | $\sim 10^{-35}$ m |
| Graviton mass scale | $m_g^{1/3}$ (if treated as volume$^{1/3}$, not a true length) | — |

Of these, only $\lambda$ is both of the right magnitude and tied to the photon's identity. The Compton wavelength of the graviton is cosmologically large — orders of magnitude greater than any photon wavelength — so it cannot set the internal cluster spacing. The Planck length is far smaller than optical wavelengths and would demand an enormous $N$ (e.g., $N \sim \lambda / \ell_P \sim 10^{28}$ for visible light), which is possible but unconstrained.

**Conclusion:** The only dimensionally natural length scale for the cluster spacing, given the photon's known wavelength, is $\lambda$ itself (possibly divided by an integer $N$). The claim $d \propto \lambda$ is dimensionally clean; the proportionality constant $1/N$ is currently unspecified.

---

## Consistency with Standard EM Theory

Standard electromagnetic theory treats $\lambda$ as a geometric property of the wave: the distance between successive field maxima. GCM does not contradict this — it re-identifies what "field maximum" refers to. In GCM, a field maximum is a graviton-density peak; the distance between peaks is $d$; and $d$ is either $\lambda$ itself (if $N = 1$) or $\lambda / N$ (if there are multiple density peaks per full optical cycle).

**GCM and standard EM produce the same $\lambda$.** They disagree on what the wave is made of, not on how long it is.

Phenomenological predictions that depend only on $\lambda$ (Snell's law, Bragg scattering, diffraction, Doppler shifts on individual wavelengths) are unaffected.

Phenomenological predictions that depend on the photon's internal structure (e.g., does a photon redshifted by $(1+z)$ have its internal information-carrying structure stretched in time?) **are** affected. This is the entry point for R6.

---

## The Redshift Cascade

Given GCM's commitment to Case A ($N$ constant):

1. By standard redshift: $\lambda_{\text{obs}} = (1+z) \cdot \lambda_{\text{emit}}$.
2. By L3 with $N$ constant: $d_{\text{obs}} = \lambda_{\text{obs}} / N = (1+z) \cdot \lambda_{\text{emit}} / N = (1+z) \cdot d_{\text{emit}}$.
3. Therefore $d_{\text{obs}} = (1+z) \cdot d_{\text{emit}}$ — the internal cluster spacing scales linearly with $(1+z)$, just as the wavelength does.

This result is the direct input to R6. It is a geometric consequence of the L3 identification, not an additional assumption.

---

## What the Derivation Does Not Do

- Does not compute the value of $N$.
- Does not derive the photon's wave equation from graviton dynamics.
- Does not show that gravitons would naturally arrange into periodic density structures.
- Does not explain the photon's polarization or helicity in terms of graviton-cluster geometry.

These are open questions. The derivation shows only that **if** L3's identification holds, **then** cluster spacing and wavelength scale together, and R6 inherits a clean $(1+z)$ scaling from standard redshift.
