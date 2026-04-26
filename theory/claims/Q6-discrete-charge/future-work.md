# Q6 — Future Work / Paper-1 Status

**Paper-1 decision:** DEFER. One-paragraph mention in §5 only, as plausibility direction.
**Source:** `theory/claims/audit-2026-04-24.md` (Q6 row).

## Current state

Yellow-tier plausibility argument only:
- Gravitons pack into shells with $P_n = 10n^2 + 2$ (Q2)
- Analogous to chemical magic numbers (2, 8, 18, 36, ...) and nuclear magic numbers (2, 8, 20, 28, 50, 82, 126), GCM posits a discrete set of graviton counts corresponds to stable closed-shell configurations
- **Not shown:** which graviton counts are stable; that stable packings produce exactly one charge unit per packing; why $e$ has the value it does.

Claim.md explicitly admits: *"We have not shown that only certain packings are stable, or that those packings produce exactly one charge unit."*

## Structural tension with E1 (newly identified by 2026-04-24 audit)

**Q6 posits symmetric closed-shell stability. E1 posits asymmetric divergence-flux as the charge mechanism.**

By the divergence theorem, symmetric configurations give zero net surface flux — i.e., zero "charge" in E1's mechanism. This is a direct structural incompatibility. Either:
- Q6's stability mechanism is asymmetric (closed-shell-like but with broken symmetry), in which case magic-number analogy weakens
- E1's charge mechanism is something other than divergence-flux sign (e.g., orientation of internal flow structure without net divergence)
- Or the two pictures need to be unified in a richer mechanism that has neither alone

**Neither claim currently addresses this.** Paper-1 should flag the tension in §8 (Structural Challenges), not hide it in either Q6 or E1.

## What would promote Q6 to INCLUDE

1. **Stability calculation.** A potential-well analysis, eigenvalue problem, or minimization-over-configurations that identifies which graviton counts are stable. This is a significant many-body problem.
2. **Charge-per-stable-packing argument.** Show that each stable packing carries $\pm e$ rather than some other amount. Needs a coupling-strength connection from shell count to emergent charge.
3. **Resolution of Q6-E1 tension.** Specify how shell-stable configurations can also be flux-asymmetric (or how E1's charge-sign mechanism works without net divergence).
4. **Prediction of $e$.** Connect the magnitude of $e \approx 1.602 \times 10^{-19}$ C to specific graviton-substrate parameters.

These are major research problems. Q6 is a paper-2+ direction.

## Where this lives going forward

- **Paper-1 §5:** one paragraph — plausibility direction only; cite magic-number analogy; explicit "no stability calculation performed."
- **Paper-1 §8:** flag the Q6-E1 tension as named challenge.
- **Verification folder preserved:** minimal content (no numerical verification applies to plausibility argument); note rules.
- **Future work:** stability calculation + charge-per-packing argument; linked to UNSPEC-1, UNSPEC-2 resolution.

## See
- `theory/claims/audit-2026-04-24.md` — Q6 row and Q6 vs E1 cross-cutting finding
- `theory/claims/E1-flow-asymmetry/future-work.md` — paired tension
- `theory/claims/Q2-tetrahedral-shells/` — the shell formula
- `research/open-questions.md` — UNSPEC-2 (charge quantization)
