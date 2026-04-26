# E1 — Future Work / Paper-1 Status

**Paper-1 decision:** INCLUDE_WITH_CAVEATS — in paper-1 §4 (Substrate Compatibility with Force Phenomena), framed as **scaffold only**.
**Source:** `theory/claims/audit-2026-04-24.md` (E1 row + §8 framing).

## Current state (honest)

E1 posits: *charge = net divergence of graviton-number current*, $\nabla \cdot \mathbf{J}_g$. Electron (net outflow, $+$ div), proton (net inflow, $-$ div), neutron (balanced, 0 div).

**What's verified:** Pint dimensional consistency of the Fokker-Planck flow equation; sign-mapping for 5 particle species; SymPy/sympy.vector divergence identity; Fokker-Planck-minus-Vlasov difference (= $-D \nabla^2 \rho_g$, Vlasov recommended for deterministic substrate).

**What's not verified (UNSPEC):**
- **UNSPEC-1:** no derivation of stable density configurations producing the required flux signs for electron vs proton
- **UNSPEC-2:** no quantization mechanism for $\pm e$ (nor for fractional quark charges)

The scaffold states a shape for what a mechanism would look like. It does not provide the mechanism.

## Structural tensions worth flagging up-front

1. **Fokker-Planck form vs deterministic minimal model.** E1's flow equation includes a stochastic diffusion term $-D \nabla \rho_g$. The minimal model (S1) is purely deterministic. E1's caveats flag this; Vlasov form (deterministic, collisionless) is the cleaner fit — but then the statistical-ensemble meaning of "flux sign" needs a different justification.
2. **Source/sink picture vs graviton conservation.** "Electrons shed gravitons outward; protons absorb gravitons inward" at the surface-integrated level — this reads as non-conservation. E1's caveats reframe it as topological feature of velocity field without net graviton non-conservation; the cleaner reading is incompatible with the sign-of-divergence statement in claim.md.
3. **Q6 vs E1 tension** (surfaced by 2026-04-24 audit). Q6's symmetric closed-shell stability mechanism + E1's asymmetric divergence-flux mechanism are incompatible by the divergence theorem. Symmetric configurations give zero net divergence.

## Why INCLUDE in paper-1 despite all this

E1 is the *named research direction* for charge emergence. Omitting it leaves the paper without any account — even scaffolded — of how charge fits the one-particle ontology. Including it **explicitly as scaffold + honest UNSPEC flags + named tensions** is the coherence-case move.

The paper's §4 title must NOT contain "unification." Suggested: "Substrate Compatibility with Force Phenomena" or "Toward a Force-Emergence Mechanism."

## What would promote E1 to green

1. **Close UNSPEC-1:** show that some graviton density configuration is stable AND produces the flux signs matching observed particle charges. This is the primary unification rescue.
2. **Close UNSPEC-2:** quantization mechanism for $\pm e$ (and fractional $\pm e/3$, $\pm 2e/3$ for quarks).
3. **Resolve Q6 vs E1 tension:** specify how shell-stable configurations can be flux-asymmetric.
4. **Commit to Fokker-Planck or Vlasov form** and justify from the minimal model (or honestly enrich the minimal model to include stochastic noise, which changes the whole framework).

These are major research problems. E1's resolution would be a significant physics result — paper-3+ level work.

## Where this lives going forward

- **Paper-1 §4:** scaffold-only presentation; UNSPEC-1 and UNSPEC-2 named up-front; Fokker-Planck-vs-Vlasov choice flagged.
- **Paper-1 §8:** Q6 vs E1 tension named as structural challenge.
- **Verification folder preserved:** structural consistency checks (dimensional, sign-mapping, divergence identity, Mathematica underscore-pattern bug caught) are useful scaffold.
- **Future work:** UNSPEC-1, UNSPEC-2 are major research directions.

## See
- `theory/claims/audit-2026-04-24.md` — E1 row and §8 framing
- `theory/claims/Q6-discrete-charge/future-work.md` — paired tension
- `research/open-questions.md` — UNSPEC-1, UNSPEC-2
- `theory/claims/E1-flow-asymmetry/caveats.md` — project's own caveat flags
