# R5 — Verification Record

**Tally:** N/A — no tool-verifiable numerical claims unique to R5.
**Last run:** 2026-04-24 (inspection only)
**Tools:** N/A.
**Honesty note:** R5's structural argument is genuinely different from the other menu mechanisms (epistemic, not photon-physics). That difference is valuable, but it also means R5 currently has no closed-form numerical scaffolding to verify.

---

## Why No Scripts

R5's plausibility.md has exactly one numerical sketch:

> "If the selection fraction $f(d) \propto e^{-\beta d}$ and the energy-bias $\propto e^{-\gamma d}$, then $1+z \sim e^{\gamma d}$. For $z=1$ at Hubble scale, $\gamma \sim H_0/c \approx 2.3 \times 10^{-27}$ m⁻¹."

This is arithmetically equivalent to R1's friction-coefficient argument. Whatever is true of R1's $\alpha$ is true of R5's $\gamma$ — including the labelling issue. See [R1/verification.md Check 1](../R1-space-friction/verification.md#check-1--hubble-radius-and-alpha--h_0c).

## What's Actually Novel in R5

R5's novelty is **not in a formula**; it is in an **epistemic move**: the observed redshift is a selection effect on what reaches us, not a physical transformation of photons in transit.

This epistemic move is verifiable in principle by:
1. Comparing R5's predicted angular correlations in Hubble-diagram residuals (from intervening matter's selection bias) against observed residuals.
2. Comparing R5's predicted chromatic signatures in deep-field photometry.

Neither has been computed. The plausibility.md explicitly flags this as open.

## The Time-Dilation Gap (Honest)

R5 alone cannot produce $(1+z)$ time dilation — selection effects don't stretch time. R5 requires R6 as a companion mechanism to survive DES 2024 SNe Ia constraints.

R5 + R6's time-dilation story is the same as R1 + R6, R2 + R6, R4 + R6: photon internal structure stretches with wavelength, producing geometric time dilation. That cascade is verified in [R6/verification/check_02](../R6-photon-structure/verification.md#check-2--cascade-exponent--1-and-consistency-with-des-2024-time-dilation-measurement).

## Inherited Checks

From R1/R6:
- Order-of-magnitude scale for $\gamma$ (or any redshift coefficient): $H_0/c \sim 10^{-27}$ m⁻¹ (subject to the factor-3.3 labelling issue R1 surfaced).
- Time-dilation exponent = 1 via R6.

R5 does not add unique numerical content beyond these.

## What Would Change This

To get a verification stack specific to R5, one would need:
1. A concrete microscopic model: gravitational-lensing bias, absorption-scattering bias, or geometric-aperture bias — pick one and derive the corresponding $f(d, E)$.
2. Compute $z(d)$ from this filter.
3. Compute the predicted angular correlations in Hubble-diagram residuals from intervening structure.
4. Check against Pantheon+ residual maps.

This would likely promote R5 from 🟡 Yellow to 🟢 Green structurally if successful. None of it exists yet.

## TODOs

1. **Derive a specific microscopic mechanism for R5.** Without this, R5 is a "type" of candidate, not a defined mechanism.
2. **Once derived, add verification scripts** for the filter function and its Hubble-diagram predictions.
3. **Wolfram MCP.** Still unavailable.

## Honesty Summary

R5's "we're small" intuition is real — encoding "what we observe is biased by what reaches us" is a valid epistemic move with genuine explanatory power. But intuitions don't verify; only formulas do. R5 needs a microscopic mechanism before any real verification is possible.

R5 stays **🟡 Yellow** — structurally distinct from tired light, ISW-clean, but requires R6 companion and lacks a concrete derivation.
