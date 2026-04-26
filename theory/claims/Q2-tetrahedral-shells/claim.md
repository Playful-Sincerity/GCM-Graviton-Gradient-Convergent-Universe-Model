# Q2 — Shell Populations for Symmetric Graviton Packing

**Claim code:** Q2
**Epistemic tier:** 🟢 Green — derivable from first principles; numerically verified for first five shells; robust across candidate close-packed geometries.
**Status:** Derived and verified.
**Sessions:** D (2026-04-23, v1 cuboctahedral-assumed) → D-reframe (2026-04-23, v2 principle-first).

> **Revision note (2026-04-23):** The v1 framing assumed cuboctahedral/FCC packing up front. v2 (this file) leads with the physical principle — uniform graviton attraction selects densest packing — and shows that the shell formula is robust across the candidate close-packed geometries, so we don't have to arbitrarily pick one. The math is unchanged; the reasoning chain is cleaner.

---

## The Principle

If gravitons attract each other uniformly (Tenet T2), the stable equilibrium for a cluster of identical gravitons around a center is the **densest possible packing**. In three dimensions, the maximum density sphere packing has **12 nearest neighbors** — this is Kepler's conjecture, proved by Hales (2005).

Any 12-coordinate close-packed symmetric cluster has shell populations:

$$P_n = 10n^2 + 2 \quad (n \geq 1)$$

---

## Why This Doesn't Depend on Picking a Specific Crystal

Multiple geometrically distinct close-packings give the *same* shell populations:

| Geometry | First-shell symmetry | Tiles 3-space? | Shells 1–5 |
|---|---|---|---|
| **FCC / cuboctahedral** | $O_h$ (cuboctahedron) | Yes (with octahedral voids) | 12, 42, 92, 162, 252 |
| **HCP** | $D_{3h}$ (anticuboctahedron / twinned) | Yes | 12, 42, 92, 162, 252 |
| **Icosahedral / Mackay** | $I_h$ (icosahedron) | No (quasicrystalline beyond) | 12, 42, 92, 162, 252 |

All three are 12-coordinate; all three give $P_n = 10n^2 + 2$. The formula is a consequence of 12-fold close-packing, not of any specific crystallographic structure.

**This matters for GCM:** we don't need to commit to "gravitons occupy an FCC lattice" or "gravitons occupy an icosahedral cluster." The weaker and more defensible claim is "gravitons settle into *some* 12-coordinate close-packed configuration" — and the shell formula follows regardless of which one.

---

## The Derivation in One Paragraph

Take the center plus its 12 nearest neighbors — the first shell. In a cuboctahedral cluster (one concrete realization), these 12 neighbors sit at the vertices of a cuboctahedron. Building the $n$th shell by expanding this cuboctahedron outward: **12 vertex positions** always, **$24(n-1)$ edge-interior sites**, **$8 \cdot \frac{(n-1)(n-2)}{2}$ triangular face-interior sites**, and **$6(n-1)^2$ square face-interior sites**. Summing and simplifying yields $P_n = 10n^2 + 2$. Full worked expansion in `derivation.md`; the same total follows from the icosahedral/Mackay construction by a different decomposition (see `verification.md` Check 5).

---

## Verified Values

| $n$ | $P_n$ (formula) | Geometric count (cuboctahedral) | Mackay icosahedral count |
|---|---|---|---|
| 1 | 12 | 12 | 12 |
| 2 | 42 | 42 | 42 |
| 3 | 92 | 92 | 92 |
| 4 | 162 | 162 | 162 |
| 5 | 252 | 252 | 252 |

---

## What This Does and Doesn't Prove

**Does:**
- Establishes that *if* gravitons settle into a densely packed symmetric cluster around a center, the shell population follows a clean, first-principles formula.
- Shows the formula is robust — not an artifact of arbitrarily choosing cuboctahedral geometry.
- Supplies the geometric substrate for the Q3 ($E_n \cdot P_n$ invariant) observation and the Q6 (discrete charge) plausibility argument.

**Does not:**
- Prove that gravitons actually do settle into 12-coordinate close-packing. This still requires a stability calculation from graviton dynamics that GCM doesn't yet have. (Same missing piece as Q6 — and noted there.)
- Distinguish *which* close-packing geometry nature picks. FCC, HCP, and icosahedral all give the same shells but different internal structure (crystalline vs. quasicrystalline), and that distinction matters for further claims.
- Derive hydrogen quantization from shell geometry. The $E_n \cdot P_n$ near-invariance (Q3) is a numerical observation; the claim that shell packing *produces* hydrogen-like $1/n^2$ scaling is aspirational (Q6).

---

## Convention note — $P_0 = 2$

The formula gives $P_0 = 10(0)^2 + 2 = 2$. This is a mathematical artifact. The central site of a cluster is one graviton, not two. The formula is defined for $n \geq 1$. The $P_0 = 2$ output does not correspond to "origin plus inversion partner" or any physically meaningful pair. See `caveats.md`.

---

## Standard References

- **Kepler's conjecture / densest sphere packing:** Hales, T. C. (2005). *A proof of the Kepler conjecture*. Annals of Mathematics, 162(3), 1065–1185.
- **Cuboctahedral cluster shells:** Conway, J. H. & Sloane, N. J. A. (1999). *Sphere Packings, Lattices and Groups* (3rd ed., Springer), §1.4 and Appendix A.
- **Mackay icosahedral clusters:** Mackay, A. L. (1962). *A dense non-crystallographic packing of equal spheres*. Acta Crystallographica, 15, 916–918. (Original paper showing Mackay icosahedra of order $n$ have surface shells of $10n^2 + 2$ atoms.)
- **OEIS A005901:** Shell populations for cuboctahedral / Mackay clusters — tabulates 12, 42, 92, 162, 252, ....
- **Cluster physics survey:** Marks, L. D. (1994). *Experimental studies of small particle structures*. Reports on Progress in Physics, 57(6), 603–649.
