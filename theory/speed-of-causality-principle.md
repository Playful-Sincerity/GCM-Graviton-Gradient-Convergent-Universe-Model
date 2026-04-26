# Principle — Speed of Light ≠ Speed of Causality

**Status:** Core working principle. System-wide convention.
**Established:** 2026-04-23 (Wisdom, during Session E R6 review).
**Applies to:** All GCM artifacts — theory files, claims, paper drafts, outreach, executive summaries, public-facing descriptions.

---

## The Principle

In GCM, **the speed of light is not the speed of causality.** They are different things.

- **c** (the speed of causality) is the fundamental cosmic speed limit — the maximum rate at which any influence, interaction, or information can propagate in the graviton substrate. Nothing in the universe can ever move at exactly $c$ or faster.
- **Photon speed** $v$ is the speed at which actual light (a composite graviton-cluster structure with nonzero rest mass) travels. Because a photon is a real thing with mass, it is forbidden by GCM's own internal logic from reaching $c$. It moves at $v < c$ by a tiny but structurally required amount.

The two speeds are related by:

$$v = c - 0_x$$

where, in IVNA notation, $0_x$ is a specific **indexed infinitesimal** — a labeled, energy-dependent near-zero quantity. The index $x$ tracks which energy regime the photon is in. Different photons have different $0_x$ values (higher-energy photons have smaller $0_x$; they are closer to $c$ but never reach it).

Equivalently, from L2 (massive photon):

$$v = c \cdot \sqrt{1 - \left(\frac{m_\gamma c^2}{E}\right)^2}$$

The factor $\sqrt{1 - (m_\gamma c^2 / E)^2}$ is strictly less than 1 for any finite-energy photon with $m_\gamma > 0$. GCM commits to $m_\gamma > 0$ (L1). Therefore $v < c$ is not a numerical approximation — it is a structural consequence of GCM's ontology.

---

## The Rule for All GCM Artifacts

**Never** write, say, or imply that light travels at $c$ in a GCM context. Always write one of:

- "Light travels at $v \approx c$, with $v < c$ strictly."
- "Photons travel at $v = c - 0_x$ (IVNA indexed infinitesimal, energy-dependent)."
- "The photon's speed is below the causality limit $c$ by a tiny amount."
- "$c$ is the cosmic speed limit; photons move at just under $c$ because they have mass."

When writing equations where "$c$" appeared in standard physics for "speed of light," use "$v$" (photon speed) instead, and let $c$ denote the causality limit exclusively.

---

## Why This Matters

**Internal consistency.** GCM commits to $m_\gamma > 0$ (L1) and therefore to $v < c$ (L2). Any artifact that says "light moves at $c$" contradicts GCM's own claims. The distinction is not cosmetic — it is load-bearing.

**Epistemic positioning.** Standard physics conflates "speed of light" and "speed of causality" because the photon is treated as massless. GCM's unique contribution — a massive photon whose speed is *almost* but not quite the causality limit — is lost if we use the two terms interchangeably. This is a point where GCM genuinely departs from the standard picture; suppressing the departure weakens the theory's signature.

**Connection to IVNA.** The "$c - 0_x$" formulation brings IVNA's indexed-infinitesimal algebra into GCM as the natural notation for "the deviation matters but is tracked." The deviation is not a generic "$\varepsilon$" — it is a specific labeled quantity whose index depends on the photon's energy. This is the first concrete IVNA/GCM bridge: where standard physics would wave hands ("approximately $c$"), GCM + IVNA carry the distinction through.

**Ethos consonance.** "Nothing in the universe can ever move at $c$" — there is something that is forever unreachable, approached but not attained. That is consonant with gravity-as-convergence: the final coming-together is an asymptotic destination, not a state that gets fully realized. The same geometric limit structure appears in both physics and ethos.

---

## Numerical Note

The deviation from $c$ is astronomically small. For a photon with the GCM rest mass $m_\gamma \approx 5.6 \times 10^{-19}$ eV/c² and visible-light energy $E \approx 1$ eV:

$$\left(\frac{m_\gamma c^2}{E}\right)^2 \approx \left(\frac{5.6 \times 10^{-19}}{1}\right)^2 \approx 3 \times 10^{-37}$$

so $v / c \approx 1 - 1.5 \times 10^{-37}$. The deviation from $c$ is below any experimental sensitivity by many orders of magnitude. But conceptually — and for R6's chain of argument — GCM's position is that $v \neq c$, not that $v = c$ to some approximation.

---

## Scope

This principle applies everywhere GCM talks about photons, light, or information propagation. It does NOT apply to discussions of the graviton itself — gravitons, as dimensionless points interacting locally with their neighbors, propagate influence at $c$ (the graviton-to-graviton interaction speed IS the causality limit, by GCM's construction). The principle is specifically about composite light-structures, not about the substrate's interactions.

---

## Cross-References

- [L1 claim](claims/L1-photon-mass/claim.md) — commits to $m_\gamma > 0$.
- [L2 claim](claims/L2-photon-speed/) (Session B) — gives the explicit formula $v = c \sqrt{1 - (m_\gamma c^2 / E)^2}$.
- [R6 derivation](claims/R6-photon-time-dilation/derivation.md) — uses this principle in the information-propagation step.
- IVNA project — provides the $0_x$ indexed-infinitesimal notation.
