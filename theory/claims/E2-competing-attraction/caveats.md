# E2 — Caveats

## What the toy model proves and does not prove

### Proves
- In a specific geometric configuration (heavy attractor off to one side of the electron pair), standard Newtonian gravity alone produces a relative acceleration that increases the inter-electron separation.
- The sign of the apparent repulsion is correct.
- A symmetric background configuration produces the opposite sign (apparent attraction); the sign is a property of the geometry, not of the underlying forces.

### Does not prove
- That "electron repulsion is really competing attraction" in any meaningful sense beyond sign.
- That the mechanism scales to the observed magnitude of Coulomb repulsion (it is off by ~40 orders).
- That the mechanism produces isotropic repulsion in realistic multi-body backgrounds.
- That GCM's unification case (all forces from gravity) is viable.

## The magnitude gap

The toy model fails quantitatively by $\sim 10^{40}$. The attempted rescue — E4's density-overlap amplification — also fails (see `../E4-gradient-overlap/`): the overlap integral *reduces* the effective short-range force rather than amplifying it. The structural gap is therefore real and currently unbridged.

**This is the single largest theoretical gap in the GCM unification case.** A physically principled mechanism for short-range amplification of gravitational interaction (density-dependent $G$, non-linear graviton coupling, contact-only interactions, etc.) must be found before E2 is quantitatively viable.

## Geometry dependence

The "competing attraction produces repulsion" result holds only when:
1. The heavy attractor is asymmetrically placed (off to one side of the electron pair).
2. The line from the attractor to the electron pair makes a non-trivial angle with the electron-electron axis, *or* the attractor lies along that axis on the side of the pair.

For a spherically symmetric background of heavy positive charges surrounding the electron pair, Gauss's theorem guarantees zero net force from the background on each electron. Only the direct inter-electron gravitational attraction remains. That is: **the competing-attraction mechanism gives apparent repulsion only in anisotropic environments, and apparent attraction or nothing in isotropic environments.**

Real electron-electron repulsion is observed to be isotropic (measured e.g. in collision cross sections, independent of lab orientation). Competing attraction in isolation cannot reproduce this. The coherence paper must either:
- Argue that all real environments where electron repulsion is measured are sufficiently anisotropic for competing attraction to work (unlikely given isotropic scattering experiments), or
- Demote competing attraction from *the* mechanism of electron repulsion to *a compatible reformulation* that coexists with some yet-unspecified mechanism producing the isotropic part.

## Toy-model simplifications

1. **1D geometry.** The real calculation must be 3D, where vector force components matter. In 3D, symmetric backgrounds cancel more fully; asymmetric backgrounds produce forces in directions that the 1D calculation cannot show.
2. **Point masses.** Real electrons and protons are extended distributions. The E4 overlap mechanics apply here, but as shown, they reduce rather than amplify the short-range force.
3. **Newtonian gravity.** Strong-field GR, relativistic corrections, and radiation reaction are ignored. At the tiny scales considered ($a_0$), these would at best contribute corrections of order $(v/c)^2$ or $(r_s/r)$, both tiny for slow non-relativistic electrons, so this is a safe simplification for magnitude checks.
4. **Static instantaneous forces.** No propagation delay or retardation. Valid in the slow-motion limit.
5. **Two electrons plus one proton only.** Real chemistry has many-body Coulomb repulsion with all electrons feeling all protons simultaneously. The toy model can be extended but is not in this session.

## Ignored but potentially important effects

1. **Quantum mechanical exchange interaction / Pauli exclusion.** Real electron-electron repulsion at close range is dominated by exchange effects (wavefunction antisymmetrization), not pure Coulomb. GCM currently has no framework for exchange interactions.
2. **Zero-point motion.** Electrons in atoms have zero-point energies of order electronvolts; the competing-attraction classical toy model has no analogue.
3. **Screening.** In a many-electron system, each electron is partially screened by other charges. Competing attraction has no built-in screening mechanism.

## Alternative interpretations to consider

In debate-style framing, competing attraction could be reread as:

**"A structural compatibility statement, not a mechanism."** The claim becomes: *in GCM's one-force ontology, every apparent repulsion must be reducible to a configuration where bodies are more attracted elsewhere than to each other. This is logically forced by T2. The 'mechanism' of electron repulsion at the level of graviton dynamics remains open — competing attraction is the general shape that any such mechanism must take, not itself a specific mechanism.*

Under this reading, E2 is a **consistency check**: it verifies that apparent inter-body repulsion can emerge from purely attractive fundamental forces in the right geometry, without yet specifying the physics that produces the observed Coulomb strength.

This is the most honest reading of what the toy model actually shows. The coherence paper might consider adopting it explicitly rather than defending E2 as a quantitative explanation of Coulomb repulsion.

## Recommendation

The coherence paper should present E2 as a **yellow-tier structural compatibility result**:

- **Green** at the level: "apparent repulsion can arise from competing attraction in asymmetric geometries" (a clean demonstration).
- **Red** at the level: "competing attraction explains observed electron repulsion" (off by $10^{40}$, geometry-dependent).

Then explicitly name the structural gap, note that closing it requires a mechanism not presently specified, and flag this as the single largest theoretical task for the GCM program.

Running `/debate` on whether this downgrade is the right move — versus trying to commit to a specific short-range amplification mechanism — is the next step suggested by the plan.
