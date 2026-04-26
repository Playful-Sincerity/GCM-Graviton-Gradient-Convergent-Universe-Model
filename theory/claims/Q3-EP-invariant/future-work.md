# Q3 — Future Work / Paper-1 Status

**Paper-1 decision:** EXCLUDE from paper-1. High numerology risk.
**Source:** `theory/claims/audit-2026-04-24.md` (Q3 row + "we agreed to ourselves" section).

## Why excluded

$\lim_{n \to \infty} (13.6/n^2)(10n^2 + 2) = 136$ eV is an algebraic limit of a rational function. SymPy and Wolfram both compute it correctly — it's a high-school limit done by two CAS. The "asymptote = 10 × Rydberg" coincidence is forced by common $n^2$ scaling in both input formulas (Bohr $\propto 1/n^2$ and FCC shell $\propto n^2$). This is a coincidence of compatible exponents, not a mechanistic relationship.

Q3 itself (claim.md) is epistemically honest: "near-invariance is exactly what the two input formulas imply" and "numerical observation, not derivation of hydrogen quantization from shell packing." The direction "shell packing *produces* $1/n^2$ scaling" is explicitly aspirational (Q6 territory) and open.

**Why this matters for paper-1:** including Q3 alongside genuine structural claims risks reviewer perception of post-hoc numerology. A physicist reading "$E_n P_n \to 10$ Ry" in a coherence paper will either ask "so what?" or "is this evidence or decoration?" and the honest answer is "decoration." Better to omit than to invite the question.

## Origin note worth preserving

Q3 originated as the *fix* to a falsified earlier formulation — the Mar-2026 Consistency Auditor's CRITICAL-2 caught that H7's "$\Delta E_n \propto \Delta P_n$" was incompatible (linear vs cubic-inverse ratio dropping 100× across $n=2$ to $n=5$). The switch to "$E_n \cdot P_n \approx \text{const}$" was a real correction. **That origin story is a strength of the project's epistemic method** — but Q3 itself, as a standalone claim, doesn't test GCM physics.

## What would promote Q3 to INCLUDE

A derivation showing that graviton-substrate dynamics *produce* the $1/n^2$ Bohr scaling as an emergent consequence of shell stability — not a numerical observation that two known $n^2$ formulas multiply to roughly constant. This is Q6's aspirational goal; once Q6 produces the Rydberg energy from first principles, Q3 becomes the *verification* that the derivation recovers the known Bohr structure. At that point Q3 is a real test.

Until then, Q3 is a pattern-match without mechanism.

## Where this lives going forward

- **Paper-1:** omit. Do not reference.
- **Verification folder preserved:** 4/4 tally is arithmetically accurate; leave as archive.
- **Future work:** gated on Q6's stability-calculation derivation.

## See
- `theory/claims/audit-2026-04-24.md` — Q3 row and "we agreed to ourselves" section
- `theory/claims/Q6-discrete-charge/future-work.md` (linked aspirational direction)
- `research/findings/consistency_report.md` — CRITICAL-2, the origin of Q3
