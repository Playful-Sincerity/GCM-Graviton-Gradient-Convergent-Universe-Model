# H1 — Future Work / Paper-1 Status

**Paper-1 decision:** INCLUDE_WITH_CAVEATS — one-paragraph plausibility sketch in §7 (Magnetism and Thermodynamics).
**Source:** `theory/claims/audit-2026-04-24.md` (H1 row).

## Current state

Qualitative consistency via SymPy + Wolfram:
- Dimensional coupling: $(\nabla \cdot \mathbf{J}_g) \cdot v$ → Tesla with units $m^2/A$ (pre-audit error $m^2 \cdot A$ falsified in-script).
- Radial + uniform flow superposition is curl-free; stagnation at $-\sqrt{q/v_0}$.

**Honesty finding surfaced by Check 02:** pure static superposition is curl-free → "toroidal streamlines" are *topological, not vortical.* UNSPEC-4's missing piece is the time-dependent oscillation dynamics, not just the static geometry. Sharpens UNSPEC-4; does not close it.

## What would promote H1 to green

1. **Specification of time-dependent oscillation dynamics** for the graviton density gradient that produces toroidal vortical structure. Current minimal model has no oscillatory bound states; a richer foundation is needed (see §8 minimal-model-poverty).
2. **Lorentz force reproduction:** derive $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ from graviton dynamics, not by analogy. UNSPEC-4.
3. **Maxwell's equations** as emergent field equations — deeply ambitious, currently out of scope.

## Where this lives going forward

- **Paper-1 §7:** one paragraph — toroidal streamlines as topological consistency, UNSPEC-4 explicitly flagged.
- **Verification folder preserved:** useful for the static-geometry and right-hand-rule-emergence observations.
- **Future work:** time-dependent oscillation dynamics needed; linked to minimal-model-enrichment decision.

## See
- `theory/claims/audit-2026-04-24.md` — H1 row
- `research/open-questions.md` — UNSPEC-4 (Lorentz force)
- Cross-reference `theory/claims/E1-flow-asymmetry/` (flow-equation form)
