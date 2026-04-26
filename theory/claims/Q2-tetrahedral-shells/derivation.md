# Q2 — Derivation: $P_n = 10n^2 + 2$ (Cuboctahedral Worked Example)

**Type:** Hand derivation from first principles
**Starting point:** The geometry of a cuboctahedral close-packed cluster (one of three equivalent realizations — see `claim.md` for the principle that selects 12-coordinate close-packing in the first place)
**Why cuboctahedral for this derivation:** It's the realization that satisfies Fuller's "vector equilibrium" condition — the only 12-coordinate arrangement where center-to-vertex distance exactly equals vertex-to-vertex distance. The arithmetic is cleanest here. The same final formula follows from the icosahedral/Mackay or HCP constructions via different but equivalent decompositions; see `verification.md` Check 5.
**Verified by:** Hand arithmetic (this file) + cross-geometry robustness check + Python/SymPy snippet (see `verification.md`)

---

## Step 1 — The Cuboctahedron as First Shell

In a close-packed arrangement where each sphere has 12 nearest neighbors, the first coordination shell ($n = 1$) is a **cuboctahedron** — an Archimedean solid with:

- 12 vertices
- 24 edges
- 14 faces: **8 equilateral triangular** faces + **6 square** faces

All 12 vertices are equidistant from the center, and equidistant from each other (nearest-neighbor distance $d$). This is the unique geometry of 12-fold close-packing with FCC/HCP symmetry.

$P_1 = 12$ (the 12 vertices of the first-shell cuboctahedron). ✓

This matches: $P_1 = 10(1)^2 + 2 = 12$.

---

## Step 2 — Building the nth Shell

For $n \geq 2$, the $n$th coordination shell is built by **expanding** the cuboctahedron outward — placing new lattice sites at:

1. **12 vertex positions** — one at each "corner direction" of the cuboctahedron (one per vertex type, always 12 regardless of $n$).

2. **Edge-interior positions** — along each of the 24 edges of the expanded cuboctahedron. For the $n$th shell, each edge contributes $n - 1$ interior lattice sites.

   $$N_{\text{edge}} = 24(n - 1)$$

3. **Triangular face-interior positions** — each of the 8 triangular faces contributes interior points whose count is the $(n-1)$th triangular number $T_{n-1} = \frac{(n-1)(n-2)}{2}$.

   $$N_{\text{tri}} = 8 \cdot \frac{(n-1)(n-2)}{2} = 4(n-1)(n-2)$$

4. **Square face-interior positions** — each of the 6 square faces contributes $(n-1)^2$ interior lattice sites (a square grid of side $n-1$).

   $$N_{\text{sq}} = 6(n-1)^2$$

---

## Step 3 — Summing the Contributions

$$P_n = 12 + 24(n-1) + 4(n-1)(n-2) + 6(n-1)^2$$

Expand, with $m = n - 1$ for clarity:

$$P_n = 12 + 24m + 4m(m-1) + 6m^2$$
$$= 12 + 24m + 4m^2 - 4m + 6m^2$$
$$= 12 + 20m + 10m^2$$

Substitute back $m = n - 1$:

$$P_n = 10(n-1)^2 + 20(n-1) + 12$$
$$= 10(n^2 - 2n + 1) + 20n - 20 + 12$$
$$= 10n^2 - 20n + 10 + 20n - 20 + 12$$

$$\boxed{P_n = 10n^2 + 2}$$

---

## Step 4 — Numerical Check (by hand)

| $n$ | Vertices | Edge atoms | Tri-face atoms | Sq-face atoms | Total | Formula $10n^2+2$ |
|---|---|---|---|---|---|---|
| 1 | 12 | $24(0)=0$ | $4(0)(-1) = 0$ | $6(0)^2 = 0$ | **12** | **12** ✓ |
| 2 | 12 | $24(1)=24$ | $4(1)(0) = 0$ | $6(1)^2 = 6$ | **42** | **42** ✓ |
| 3 | 12 | $24(2)=48$ | $4(2)(1) = 8$ | $6(2)^2 = 24$ | **92** | **92** ✓ |
| 4 | 12 | $24(3)=72$ | $4(3)(2) = 24$ | $6(3)^2 = 54$ | **162** | **162** ✓ |
| 5 | 12 | $24(4)=96$ | $4(4)(3) = 48$ | $6(4)^2 = 96$ | **252** | **252** ✓ |

All five checks pass. 5/5. ✓

---

## Step 5 — Shell Difference Check

The difference between successive shells is:

$$\Delta P_n = P_n - P_{n-1} = 10n^2 + 2 - 10(n-1)^2 - 2 = 10(2n - 1) = 20n - 10$$

This gives $\Delta P_n = 10, 30, 50, 70, 90$ for $n = 1, 2, 3, 4, 5$. Shell growth is **linear in $n$**, not quadratic. This matters for the Q6 discrete-charge argument: each successive shell is larger than the last by a fixed linear increment, making inner shells genuinely more compact and structurally distinct.

---

## What the Derivation Assumes

- **The physical assumption** (upstream, stated in `claim.md`): gravitons attract uniformly and settle into 12-coordinate close-packing.
- **The geometric assumption in this derivation**: among the three candidate 12-coordinate close-packings (FCC cuboctahedral, HCP, icosahedral Mackay), we use cuboctahedral for the worked example because its arithmetic is cleanest. The final shell formula is the same in all three — that robustness is the point of the reframe.
- "Shell $n$" means the $n$th concentric layer of sites around the central graviton.
- The derivation treats a **finite cluster**, not the infinite FCC lattice. In the infinite FCC lattice, the coordination-sphere sequence is different (12, 6, 24, 12, 24, ...). The formula $10n^2 + 2$ is the cluster formula, which is the relevant geometry for GCM's particle-internal model — a finite graviton structure with a well-defined center.

---

## Why the Same Formula Holds for Icosahedral / Mackay Clusters

A Mackay icosahedron of order $n$ has outer-shell atoms at vertex, edge, and face positions of an *icosahedron* expanded to size $n$ — not of a cuboctahedron. The decomposition is different: 12 vertices (always), 30 edges contributing $30(n-1)$ edge sites, and 20 triangular faces contributing $20 \cdot \frac{(n-1)(n-2)}{2}$ face-interior sites. Summing: $12 + 30(n-1) + 10(n-1)(n-2) = 10n^2 + 2$. Same formula, different geometry. (Mackay 1962 is the original result.)

The HCP case is structurally identical to FCC shell-by-shell (twinning differs but shell populations match).

---

## Standard References

- Conway & Sloane, *Sphere Packings, Lattices and Groups* (3rd ed., 1999), §1.4 and Appendix A. Cuboctahedral cluster sequence.
- Mackay, A. L. (1962), *Acta Crystallographica* 15, 916–918. Original Mackay-icosahedron shell derivation.
- OEIS A005901. $1, 12, 42, 92, 162, 252, \ldots$
