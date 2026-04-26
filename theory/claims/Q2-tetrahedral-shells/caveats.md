# Q2 — Caveats and Boundary Conditions

---

## 1. Finite cluster vs. infinite lattice

The formula $P_n = 10n^2 + 2$ is the shell population for a **finite 12-coordinate close-packed cluster** — successive layers of symmetrically arranged gravitons around a central site. This is the relevant geometry for GCM: a particle's internal graviton structure is a finite, bounded arrangement around a center, not an embedding in a bulk crystal.

The formula is *not* the same as the coordination-sphere sequence of an infinite FCC lattice, which follows a different pattern (12, 6, 24, 12, 24, 8, ..., OEIS A004015) that does not simplify to $10n^2 + 2$.

**What to say in the coherence paper:** "Gravitons attract uniformly, which selects densest packing; in 3D this means 12 nearest neighbors (Kepler / Hales 2005). The $n$th shell of any 12-coordinate close-packed finite cluster — cuboctahedral (FCC), icosahedral (Mackay), or HCP — has population $P_n = 10n^2 + 2$."

---

## 1b. Which close-packing does nature pick? (Downstream open question)

The shell populations are the same across FCC cuboctahedral, HCP, and icosahedral Mackay clusters, so Q2's numerical result doesn't depend on which one gravitons actually adopt. But the choice still matters for later claims:

- **FCC cuboctahedral** — crystalline, tiles 3-space (with octahedral voids). Supports a spatially extended crystalline graviton substrate.
- **HCP** — crystalline, tiles 3-space, different stacking. Physically close to FCC.
- **Icosahedral Mackay** — higher first-shell symmetry (pure 20 tetrahedra around each center), but cannot tile 3-space beyond a few shells. Would imply particles are local quasicrystalline "islands" in a substrate whose between-particle geometry is distinct.

**For later sections (S3 unification, S6 cosmology, S7 magnetism):** which packing is adopted affects what the substrate *between* particles looks like. This is an open question for GCM, flagged here as OQ-Q2a. Q2 itself doesn't need to resolve it; the shell populations are robust either way.

---

## 2. The $P_0 = 2$ convention issue

Plugging $n = 0$ into the formula gives $P_0 = 2$. Geometrically, the center of a cluster is a single atom (or a single graviton in GCM's language) — not two. There is no crystallographic convention under which $n = 0$ yields 2 particles.

The formula is correctly defined for $n \geq 1$ only. The $n = 0$ artifact arises from the algebraic form and has no physical content. It does *not* represent "the origin point and its inversion partner" or any other physically meaningful pair.

**What to say in the coherence paper:** "The formula is defined for $n \geq 1$; the central atom corresponds to $n = 0$ with shell population 1 (the atom itself), not 2 as the formula would suggest. The formula's $P_0 = 2$ output is a mathematical artifact without geometric meaning."

---

## 3. What this derivation proves vs. what it does not

**Proves:** The cuboctahedral shell population formula is correctly derived from first principles (vertex, edge, face counting on the expanded cuboctahedron) and numerically verified for the first five shells.

**Does not prove:**
- That particles *actually* have cuboctahedral graviton structure. This is H7 (GCM's hypothesis), not a derivation.
- That the energy levels of hydrogen follow from shell populations. The $E_n \cdot P_n$ approximate invariance (Q3) is a numerical observation, not a derivation.
- That only certain shell sizes are gravitationally stable, or that stable packings correspond to charge quanta. That is Q6 (aspirational, yellow-tier).

---

## 4. Connection to Q3 and Q6

- **Q3 ($E_n \cdot P_n$ invariant):** Q2 is the geometric input. Q3 observes that $|E_n| \cdot P_n \approx 136$–$163$ eV across hydrogen levels — a ~20% variation that constitutes a strong numerical near-invariance but not a derivation.
- **Q6 (discrete charge from stable packings):** Q2 provides the shell sizes. Q6 asks whether *only certain shell sizes are gravitationally stable* and whether those correspond to charge quanta. Q6 is aspirational (yellow-to-red tier). Q2 doesn't help with Q6 beyond supplying the relevant numbers.

---

## 5. LQG vocabulary parallel

Loop Quantum Gravity's 4-simplex structure anticipates three-dimensional tetrahedral boundary geometry in a formally different but structurally resonant way. GCM's cuboctahedral shells can borrow LQG's formal vocabulary of discrete spacetime cells without inheriting LQG's full machinery. This is a positioning resource for the coherence paper (S9), not a mathematical connection.
