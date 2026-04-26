# H1 — Toroidal Magnetism

**Claim code:** H1
**Session:** F (Thermodynamics, Classical & Relativistic Limits)
**Epistemic tier:** 🟡 Yellow — plausibility sketch. No derivation. UNSPEC-4 (exact reproduction of Lorentz force) is explicitly out of scope for the coherence paper.
**Date:** 2026-04-23
**Status:** Pre-formal. Mechanism stated at the structural level only. Quantitative agreement with $F = q(E + v\times B)$ is a future-work requirement.

---

## The Claim

Magnetic fields arise from **coherent toroidal oscillation of graviton density** in configurations where charge is in motion. In GCM's framing, charge itself is a graviton-flow asymmetry (H2 in v2 notation: $\nabla\cdot J_g > 0$ for electron-like, $< 0$ for proton-like). When such a charge moves, the flow asymmetry couples to the directional motion and produces a torus-shaped oscillation of the surrounding graviton density. When multiple such oscillations align, the aligned pattern is what we measure as a magnetic field.

More precisely:

> A moving charge carries a directional graviton-flow asymmetry through the substrate. The motion superimposes a linear displacement on the radial inflow/outflow pattern, producing a toroidal geometry: the graviton-density oscillation loops around the direction of motion. Neighboring oscillations with the same orientation reinforce one another; mis-aligned oscillations cancel. Large-scale magnetic fields are the statistical residue of this toroidal alignment across many carriers.

**Connection to standard observations:**
- Straight current through a wire produces a circular magnetic field around the wire (right-hand rule) — GCM reading: the electron flow down the wire carries a directional asymmetry; the resulting toroidal oscillation loops the wire.
- Permanent magnets have aligned internal toroidal oscillations (ferromagnetic domains) — GCM reading: stable alignment of the underlying toroidal graviton patterns; "static light moving slightly along field lines" per source notes.
- A magnetic monopole would require a non-toroidal (purely radial) oscillation pattern that GCM's topology does not permit — consistent with the empirical absence of monopoles.

---

## What This Claim IS

A structural plausibility argument: there is a geometric pattern (toroidal graviton density oscillation) that, *if* it could be rigorously derived from the GCM substrate equations, would produce something recognizable as a magnetic field. The right-hand rule, the circular geometry around current-carrying wires, and the dipole character of permanent magnets all have natural geometric analogs in this picture.

## What This Claim IS NOT

A derivation. The Lorentz force law $F = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ is verified to extraordinary precision (parts in $10^{15}$ in penning-trap experiments). GCM cannot currently reproduce this formula from graviton substrate dynamics. The claim is honest about this: it is a plausibility sketch, a direction for future work, not a formal theory of magnetism.

This is **UNSPEC-4** from v2, explicitly carried forward.

---

## UNSPEC-4 (Carried Forward, Expanded)

From `theory/versions/gcm_v2.md`:

> **UNSPEC-4 (Urgent)**: The Lorentz force law $F = q(E + v\times B)$ is verified to extraordinary precision. GCM must reproduce the **identical numerical result** from toroidal alignment dynamics — not just describe the analogy.

**Status for the coherence paper (S7):** Out of scope. The coherence case presents H1 as a structural analogy only. The quantitative reproduction of the Lorentz force is named as a future-work requirement and treated in S8 (Structural Challenges) as a medium-severity open problem — medium because the direction (derive electromagnetic force laws from graviton flow + toroidal oscillation) is well-specified, even if the execution is non-trivial.

**What would close UNSPEC-4:**
1. A formal wave equation for toroidal graviton-density oscillation
2. A derivation showing that two such toroidal oscillations, in relative motion, produce a cross-product force with the correct sign and magnitude
3. A demonstration that the emergent coupling constant matches the Biot-Savart / Lorentz force constants ($\mu_0$, $c$) numerically

None of these exist. UNSPEC-4 is deep.

---

## Adjacency to Existing Physics

**Maxwell's equations on a substrate.** There is a long tradition of treating Maxwell's equations as properties of an underlying medium (the historical ether, the modern vacuum). GCM's graviton substrate is a specific commitment within this tradition: the substrate is a gas of gravitons, and electromagnetic phenomena are collective behaviors of this gas. The tradition has an obvious problem (the Michelson-Morley null result and subsequent SR developments) that GCM addresses via S5.5(b) — Lorentz invariance is consistent with a substrate where signals propagate at $c$.

**Lattice-gauge intuition.** In lattice gauge theory, electromagnetism emerges on a discrete lattice as the continuum limit of a $U(1)$ gauge field. GCM's toroidal oscillation picture is structurally analogous: a local phase (toroidal orientation) that couples to a local current (graviton-flow asymmetry). Whether GCM can actually produce $U(1)$ gauge invariance as an emergent property is an open question well outside the coherence paper's scope.

**Preon ancestry.** GCM is structurally a preon program (gravitons as preons), and preon programs have historically struggled to reproduce electromagnetism from compositeness. GCM inherits this challenge. Naming it openly is part of the honesty standard.

---

## Relationship to Other GCM Claims

- **Depends on H2 (v2 numbering: charge as graviton flow asymmetry).** Without $\nabla\cdot J_g$ being the source of charge, there is no moving-flow-asymmetry to twist into a torus. H1 is downstream.
- **Depends on the Axiom of Indivisibility (CC-5).** Since the graviton has no intrinsic spin or magnetic moment, magnetism must be configurational. The toroidal geometry is the configuration that gives handedness without adding graviton-intrinsic structure.
- **Connected to H3 (Pauli exclusion, v2).** Toroidal oscillation is also claimed to underlie Pauli exclusion. If H3 is correct, the same geometric primitive underlies two different quantum phenomena — parsimony for GCM.

---

## What This Establishes

- A geometric mechanism (toroidal density oscillation in the presence of charge motion) that produces the qualitative structure of magnetic fields (circulation, dipole character, handedness)
- A natural home for the empirical absence of magnetic monopoles (GCM's topology doesn't permit them)
- A consistent place for this claim within GCM's ontology (configurational, not graviton-intrinsic, per the Axiom of Indivisibility)
- An honest flag of UNSPEC-4 as the quantitative gap that must be closed before GCM can claim a theory of magnetism
