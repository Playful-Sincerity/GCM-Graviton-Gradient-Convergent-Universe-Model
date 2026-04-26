# M1 — Graviton Mass from Planck Scale and Density Bound

**Claim code:** M1
**Epistemic tier:** Yellow (4/5 verification checks pass; check 5 reveals a boundary constraint — see verification.md)
**Section:** S2 — Verifiable Math Spine
**Source:** `GCM/theory/versions/gcm_v2.md` §H1; `GCM/plan-coherence-case.md` §S2
**Verified:** 2026-04-23

---

## The Claim

Given that gravitons are the fundamental substrate of space, and that the maximum graviton packing density at roughly nuclear scale is $\rho_\text{bound} \approx 10^{18}$ kg/m³, each graviton occupies approximately one Planck volume $\ell_P^3$. Therefore:

$$m_g = \rho_\text{bound} \cdot \ell_P^3$$

With $\rho_\text{bound} = 10^{18}$ kg/m³ and $\ell_P = 1.616 \times 10^{-35}$ m:

$$m_g \approx 4.22 \times 10^{-87} \text{ kg}$$

This is approximately 28 orders of magnitude below the LIGO graviton mass bound ($m_g < 1.78 \times 10^{-59}$ kg). The number of gravitons per neutron follows:

$$N_g = \frac{m_\text{neutron}}{m_g} \approx \frac{1.675 \times 10^{-27}}{4.22 \times 10^{-87}} \approx 4 \times 10^{59}$$

---

## What This Claim Is

A dimensional estimate of the graviton mass scale, using the Planck length as the natural unit of graviton extent and nuclear density as the provisional maximum packing density. It establishes that GCM's graviton mass is consistent with the tightest observational bound available (LIGO, 2023).

## What This Claim Is Not

- Not a derivation of $m_g$ from first principles. The choice $\rho_\text{bound} = \rho_\text{nuclear}$ is provisional (open question OQ-2).
- Not a claim that gravitons are distributed at nuclear density throughout the universe. The estimate applies locally, at the maximum packing scale.
- Not a prediction of a measurable graviton mass. At $4.22 \times 10^{-87}$ kg, this is 28 orders below detectability.

---

## Provenance

The estimate originates in `gcm_v2.md` §H1 using $\rho_\text{neutron} \approx 4 \times 10^{17}$ kg/m³ (yielding $m_g \approx 1.69 \times 10^{-87}$ kg). The session brief uses the rounder nuclear-scale bound $10^{18}$ kg/m³, giving $4.22 \times 10^{-87}$ kg. Both are consistent to within one order; the session-brief value is used here. The LIGO margin is 27–28 orders in either case.
