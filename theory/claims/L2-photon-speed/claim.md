# L2 — Photon Speed from Small Rest Mass

**Claim code:** L2
**Epistemic tier:** Green (5/5 verification checks pass).
**Section:** S2 — Verifiable Math Spine (cross-referenced in S5 — Light and Photon Physics)
**Source:** Standard special-relativistic energy-momentum relation; GCM photon-mass hypothesis from `gcm_v2.md`.
**Verified:** 2026-04-23

---

## The Claim

A photon with small rest mass $m_0$ and total energy $E$ propagates at a speed

$$v = c \cdot \sqrt{1 - \left( \frac{m_0 c^2}{E} \right)^2}$$

which, for $m_0 c^2 \ll E$, reduces to:

$$v \approx c \left( 1 - \frac{1}{2}\left(\frac{m_0 c^2}{E}\right)^2 \right), \quad \Delta v \equiv c - v \approx \frac{1}{2} c \left( \frac{m_0 c^2}{E} \right)^2$$

**Numerical example (from session brief).** For GCM's photon mass hypothesis $m_0 \approx 10^{-54}$ kg and a 1 eV photon ($E = 1.602 \times 10^{-19}$ J):

$$\Delta v \approx 4.72 \times 10^{-29} \text{ m/s}$$

(Session brief's stated value: $\approx 4.74 \times 10^{-29}$ m/s. Our precise computation: $4.717 \times 10^{-29}$ m/s. Agreement within rounding of the stated inputs.)

**Cross-check against the Wang et al. 2023 FRB dispersion bound.** Converting $m_0 = 10^{-54}$ kg to eV/$c^2$:

$$m_0 = 10^{-54} \text{ kg} / (1.783 \times 10^{-36} \text{ kg/(eV/}c^2\text{)}) \approx 5.6 \times 10^{-19} \text{ eV}/c^2$$

The FRB bound (Wang et al. 2023, JCAP) is $m_\gamma \leq 2.1 \times 10^{-15}$ eV/$c^2$. GCM's value is $\sim 4$ orders of magnitude below the bound. **Safe.**

## Framing

L2 shows what a small photon rest mass would *produce* — a vanishingly small departure from $c$ that is far below any conceivable measurement — and is consistent with the current tightest bound. It is **not** a claim that the photon has been measured to have mass, nor a prediction distinguishable from the standard-model massless photon in practice.

---

## What This Claim Is

- A standard special-relativistic result applied to GCM's small-photon-mass hypothesis.
- A cross-check that the hypothesis is compatible with the tightest observational bound.

## What This Claim Is Not

- Not a prediction of measurable dispersion from GCM specifically. The dispersion implied by $m_0 = 10^{-54}$ kg is $\sim 10^{-37}$ fractionally, orders of magnitude below any conceivable measurement.
- Not a derivation of $m_0$ from GCM first principles. The value $10^{-54}$ kg is a placeholder quoted in `gcm_v2.md` that lies safely below known bounds; it is not the output of a calculation.

---

## Provenance

- The formula $v = c \sqrt{1 - (m_0 c^2 / E)^2}$ is standard SR, from the energy-momentum relation $E^2 = (pc)^2 + (m_0 c^2)^2$ and $v = pc^2/E$.
- The photon-mass value $m_0 \approx 10^{-54}$ kg is from `gcm_v2.md` §L-family / session brief.
- The FRB bound is from Wang et al. 2023, JCAP (quoted via `plan-coherence-case.md`).
