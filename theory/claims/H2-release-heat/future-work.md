# H2 — Future Work / Paper-1 Status

**Paper-1 decision:** DEFER. One-paragraph reference in §7 (Magnetism and Thermodynamics), not a standalone claim.
**Source:** `theory/claims/audit-2026-04-24.md` (H2 row).

## Why deferred

The verification structurally verifies that Newton's cooling ODE + Fourier PDE *forms* reproduce. SymPy `dsolve` and Wolfram `DSolve` both solve $d\rho/dt = -\lambda(\rho - \rho_0)$ to exponential decay. **Solving a first-order linear ODE was never going to fail** — both tools implement the same textbook method. This is in the "we agreed to ourselves" category.

The load-bearing thermodynamic content — **equipartition derivation** and **Planck's law blackbody spectrum** — remain UNSPEC-5, red. The H2 mapping $T \propto \rho_g - \rho_0$ is asserted, not derived. Structural ODE-form agreement is not evidence for GCM's thermodynamic claims.

**Also a minimal-model problem:** collisionless gravitating systems do NOT thermalize. H2's "release theory of heat" implicitly assumes a thermalization mechanism not present in S1's minimal model.

## What would promote H2 to INCLUDE

1. **Equipartition derivation from GCM dynamics.** Show that graviton-substrate ensemble statistics produce $\langle E \rangle = (k_B T / 2)$ per degree of freedom. Requires either adding stochastic noise to the minimal model or identifying an emergent-ensemble thermalization mechanism from deterministic graviton dynamics.
2. **Planck's law derivation.** Recover the blackbody spectrum $\rho(\nu, T) \propto \nu^3 / (e^{h\nu/k_B T} - 1)$ from graviton-release equilibrium. Would require a specific photon-graviton-coupling model and ensemble-statistical treatment.

These are hard. They are paper-2+ work.

## Where this lives going forward

- **Paper-1 §7:** brief reference only; UNSPEC-5 named.
- **Verification folder preserved:** keeps the structural ODE-form consistency check.
- **Future work:** equipartition + Planck derivations; linked to minimal-model enrichment.

## See
- `theory/claims/audit-2026-04-24.md` — H2 row and "we agreed to ourselves" section
- `research/open-questions.md` — UNSPEC-5 (equipartition + Planck)
- Compare to Verlinde's entropic-gravity thermodynamic framework (shared substrate lineage)
