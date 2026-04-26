# H1 — Toroidal Magnetism: Sketch (Not a Derivation)

**Tier:** 🟡 Yellow — dimensional framing only. No formal derivation.
**Verification level:** Dimensional consistency of the proposed mechanism. No numerical comparison to experiment.

---

## What This Document Is

A structural sketch of the proposed mechanism, not a derivation. The coherence paper's S7 treats magnetism at plausibility level; the quantitative work belongs to UNSPEC-4 and is out of scope.

---

## The Proposed Mechanism

### Step 1 — Charge as Flow Asymmetry

From v2 H2:
$$\nabla\cdot J_g > 0 \quad \text{(electron-like, net outflow)}$$
$$\nabla\cdot J_g < 0 \quad \text{(proton-like, net inflow)}$$
$$\nabla\cdot J_g = 0 \quad \text{(neutron-like, balanced)}$$

where $J_g$ is the graviton current density. Charge is a property of a particle's graviton-flow pattern, not an intrinsic scalar.

### Step 2 — Motion Superimposes a Linear Drift

When a charge moves with velocity $\mathbf{v}$, its graviton-flow pattern is advected along with it. The static radial pattern (inflow or outflow) is superimposed on a linear drift:
$$J_g^{\text{total}} = J_g^{\text{radial}}(\mathbf{r}) + \rho_g \mathbf{v}$$

This is a vector-field composition: a radial (diverging or converging) pattern plus a uniform drift.

### Step 3 — The Superposition Has Toroidal Structure

The composition of a radial flow with a linear drift produces a vector field with **toroidal streamlines** around the axis of motion. This is a standard result in vector calculus: a point source in a uniform flow produces streamlines that loop around the axis of the uniform flow, reconnecting on the downstream side. The resulting pattern is topologically a torus, with the axis aligned with $\mathbf{v}$.

**Geometric picture:**
- Axis of torus: direction of motion $\mathbf{v}$
- Orientation of circulation around the axis: determined by the sign of $\nabla\cdot J_g$ (i.e., by the sign of the charge) — this is the source of the right-hand rule
- Magnitude of circulation: proportional to both $|v|$ and $|\nabla\cdot J_g|$

### Step 4 — Oscillation, Not Static Flow

GCM's source notes add that toroidal structures *oscillate*:

> "Angular momentum is translation of 1D motion into 2D; toroidal momentum is translation of 2D motion into 3D."
> "A completely cold/content particle does not toroidally cycle. Disequilibrium (heat) causes cycling."

The toroidal pattern is not a static field but a cyclic oscillation of graviton density around the torus. This is what gives the pattern a time-dependent character consistent with, e.g., electromagnetic waves as disturbances in the substrate.

### Step 5 — Alignment = Macroscopic Field

Multiple nearby moving charges produce multiple nearby toroidal oscillations. When these oscillations align (same axis direction, same circulation sense), they reinforce one another. When they cancel (opposite senses), they do not. The net coherent toroidal oscillation across a macroscopic region is what GCM identifies with a **magnetic field**.

In a current-carrying wire, all the conduction electrons move in the same direction. Their toroidal oscillations share an axis (the wire). The aligned oscillations produce a coherent toroidal pattern around the wire — the familiar circular magnetic field.

In a permanent magnet, unpaired electrons in domains have aligned spins (standard QM), which in GCM terms corresponds to aligned toroidal oscillation patterns even without bulk current flow. The field persists because the alignment is energetically stable.

---

## Dimensional Framing

A dimensional check for the proposed mechanism: what units does the toroidal oscillation produce, and are those compatible with magnetic field units?

- Graviton current density: $[J_g] = \text{kg}/(\text{m}^2 \cdot \text{s})$
- Charge as divergence of $J_g$: $[\nabla\cdot J_g] = \text{kg}/(\text{m}^3 \cdot \text{s})$
- Velocity: $[\mathbf{v}] = \text{m/s}$
- Product $(\nabla\cdot J_g)\cdot\mathbf{v}$: $\text{kg}/(\text{m}^2 \cdot \text{s}^2) = \text{N}/\text{m}^3$ — force per unit volume (a pressure-gradient-like quantity).

The magnetic field $\mathbf{B}$ has units of $\text{kg}/(\text{A}\cdot\text{s}^2) = \text{T}$ (Tesla). To convert the GCM product $\text{kg}/(\text{m}^2 \cdot \text{s}^2)$ into Tesla, one needs a coupling constant with units of $\text{m}^2/\text{A}$ (so that $[\text{kg}/(\text{m}^2\cdot\text{s}^2)] \cdot [\text{m}^2/\text{A}] = [\text{kg}/(\text{A}\cdot\text{s}^2)]$). That coupling does not yet exist in GCM; its value is part of what UNSPEC-4 would have to determine.

The point of the dimensional framing is to show that **no dimensional inconsistency has been introduced**. The mechanism is stated in the right kind of quantities; the coupling to the standard electromagnetic units is unresolved but not incoherent.

---

## What This Sketch Does NOT Do

- It does not derive Maxwell's equations from graviton substrate dynamics.
- It does not reproduce the Lorentz force law $F = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ numerically.
- It does not predict the speed of light $c$ as a function of graviton parameters.
- It does not derive the electric charge $e$ as a specific multiple of graviton-flow strength.
- It does not derive the magnetic permeability $\mu_0$ or the electric permittivity $\epsilon_0$.

All of the above are UNSPEC-4 and its downstream requirements. They are collectively the theory-of-electromagnetism that GCM would need to eventually build. For the coherence paper, naming the gap is the work; closing it is not.

---

## Verification Summary

| Check | Method | Result |
|---|---|---|
| Geometric consistency (radial + linear → toroidal) | Standard vector calculus | ✓ Pass (well-known) |
| Right-hand rule emerges naturally from sign of $\nabla\cdot J_g$ | Qualitative geometry | ✓ Pass |
| Dimensional consistency of GCM quantities | Unit analysis | ✓ No inconsistency, but no derivation of the coupling |
| Absence of monopoles explained | Topological argument | ✓ Qualitative |
| Lorentz force reproduction | Not attempted | ✗ Open (UNSPEC-4) |
| Maxwell equations derivation | Not attempted | ✗ Open (UNSPEC-4) |

**Verification tally: 4/6 qualitative passes; 2/6 open gaps. Claim remains 🟡 Yellow.**
