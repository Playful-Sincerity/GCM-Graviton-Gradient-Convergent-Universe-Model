# E7 — Future Work / Paper-1 Status

**Paper-1 decision:** DEFER. Do not include in paper-1.
**Source:** `theory/claims/audit-2026-04-24.md` (E7 row).

## Why deferred

The claim $\partial \ln E_1 / \partial \ln e = 4$ is a Bohr-formula identity. SymPy and Wolfram both implement the same $E_1 = -m_e k^2 e^4 / (2\hbar^2)$ and both correctly differentiate to $-4$. The agreement is evidence that two CAS tools do partial derivatives correctly — not evidence about graviton physics.

E7 is explicitly a *consistency constraint on any emergent-parameter theory* (claim.md line 21). It is a constraint every such theory must satisfy — empty as GCM-specific evidence.

In the audit's "we agreed to ourselves" list, E7 is the single starkest example of "verifies standard math, not physics." Including it risks the perception of padding the paper's apparent rigor with items that don't actually test GCM.

## What would promote E7 to INCLUDE

Once GCM has a mechanism producing emergent $e$ AND emergent $m_e$ from graviton-substrate dynamics, E7 becomes a real compatibility check: *does the mechanism respect the Bohr-constraint ratio of $-4$?* At that point E7 is an actual test.

Until then, E7 tests nothing about GCM and should not be presented as verification.

## Where this lives going forward

- **Paper-1:** omit.
- **Verification folder preserved:** 5/5 tally is arithmetically accurate; leave as archive with a pointer noting the "test nothing about GCM until emergent $e, m_e$ exist" caveat.
- **Future work:** becomes a test once UNSPEC-2 (charge-quantization mechanism) is addressed.

## See
- `theory/claims/audit-2026-04-24.md` — E7 row and "we agreed to ourselves" failure-mode section
- Cross-reference `E1-flow-asymmetry/` (UNSPEC-1, UNSPEC-2)
