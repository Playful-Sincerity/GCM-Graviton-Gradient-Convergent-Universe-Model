# GDGM Derivation Sketch — From Axioms Up
**Date**: 2026-03-21
**Purpose**: Start from nothing but the two core axioms and ask what must logically follow. Keep it simple. Flag every fork where a choice must be made or an experiment is needed.

---

## The Two Axioms We're Working From

**A1**: There exist point-particles (gravitons) with mass mg.
**A2**: Any two gravitons attract each other.

That's it for now. T3 (convergence) and T4 (everything is change) will fall out as consequences if A1 and A2 are right.

---

## Step 1: What Is Space?

If gravitons are the only thing that exists, then space cannot be a pre-existing container. Space must be *defined by* the gravitons.

The simplest definition: **space is the set of distances between gravitons.**

Call the distance between graviton i and graviton j: r_ij.

That's your geometry. No background. No grid. Just a distance matrix.

**What follows immediately**:
- "Empty space" is not empty — it is a region with some baseline graviton density ρ₀.
- "Distance" between two macroscopic objects is actually the aggregate of all the graviton-to-graviton distances between them.
- If gravitons cluster together, the distances compress — that region of space gets "smaller." This is gravitational time dilation and length contraction without needing to postulate them separately.

---

## Step 2: What Is Time?

From A2, gravitons attract. So distances r_ij decrease.

**Time is the process of distances decreasing.**

This is not a metaphor — it's the only thing that can happen if A2 is true. Change = distances changing. No change = no time.

**What follows**:
- Time has a direction (toward convergence). This gives time's arrow for free — no need for entropy arguments.
- The rate of time depends on local graviton density. Dense regions = distances change faster = faster dynamics = slower clock from outside (gravitational time dilation).

---

## Step 3: What Is the Force Law?

A2 says gravitons attract. It does not say *how strongly* or by what law.

This is the first place we need to make a choice — or run an experiment.

The simplest possible law:

```
F(r) = G · mg² / r²
```

This is Newton's law applied at the graviton scale. It has one free parameter: G (or equivalently, G·mg²).

**Could the law be different at short range?** Yes, and probably must be — otherwise two gravitons at r→0 would attract with infinite force, which either means instant total collapse or requires a floor distance.

**First fork**:
- Is there a minimum distance (quantization of space)?
- Or does the force law soften at short range?

The Planck length ℓP = 1.616 × 10⁻³⁵ m is the natural candidate for a minimum distance — it's the scale at which quantum gravitational effects become significant. In GDGM, it may simply be the physical size of a graviton's "exclusion zone."

**Experiment needed**: Any measurement that constrains gravity at sub-micron scales (torsion balance experiments at short range) gives us the force law in the regime where GDGM differs from GR.

---

## Step 4: The Stability Problem

Here is the first real obstacle.

If all gravitons attract all other gravitons, and no other forces exist, everything should collapse to a single point. Why does stable structure exist at all?

**This must be resolved before building further.** There are three logical possibilities:

**Option A — Minimum distance**
Gravitons cannot get closer than some ℓ_min. At minimum distance, force saturates or reverses. This gives a ground state configuration: a close-packed lattice of gravitons. "Empty space" is this lattice at baseline density ρ₀. Particles are regions of over-density or particular lattice patterns. This is the most structurally clean option.

**Option B — Topological stability**
Certain configurations of gravitons are topologically locked — they can't collapse without passing through a higher-energy intermediate state. Like a knot you can't untie without cutting the rope. This requires the graviton substrate to have topological properties, which means it's not just points but points with some orientation or winding number.

**Option C — Competing attraction**
A cluster of gravitons is in a metastable state when each graviton inside the cluster is pulled equally in all directions by gravitons outside. The interior gravitons are not collapsing because the pull from all sides cancels. This is essentially hydrostatic equilibrium — and it's how stars work in standard physics. Particles are stable graviton clusters because they're in hydrostatic equilibrium within the larger graviton field.

**Most likely answer**: some combination of A and C. Option A (minimum distance) handles the ultraviolet problem (why no point singularities). Option C (equilibrium) handles why structures at larger scales are stable.

---

## Step 5: What Is a Particle?

Given Option C above, a particle is:

> A region where graviton density significantly exceeds the background ρ₀, held in a stable configuration by the balance of attraction from within and without.

The simplest model: think of a particle as a self-gravitating clump. Like a small gravitational well that is self-sustaining because the gravitons at its edge are more attracted inward (toward the denser center) than outward (toward the sparser vacuum).

This gives a natural **density profile** for each particle — a gradient that falls off from the center. The shape of that gradient determines the particle's properties (charge, spin, etc.).

**What determines the profile shape?**
The equilibrium condition: at every radius r from the center, the inward pull from the core must balance the outward pull from the surrounding vacuum.

This is a differential equation of the form:

```
dP/dr = -ρ_g(r) · g(r)
```

...where P is the local "graviton pressure" (tendency to stay put), ρ_g is local density, and g(r) is the local gravitational acceleration. This is the equation of stellar hydrostatic equilibrium — but applied at the particle scale.

**The core insight**: different stable solutions to this equation = different particles. Electron, proton, neutron are different stable density profiles, not different substances.

---

## Step 6: What Is Mass?

From Step 5: a particle is a cluster of ξ gravitons.

Total mass: `m = mg · ξ`

This gives inertia naturally. To accelerate a particle, you are asking all ξ gravitons to reorganize their density distribution. More gravitons = more reorganization required = more inertia.

Energy follows: `E = mg · ξ · c²`
(This is just E = mc² where m = mg·ξ. No new assumption needed — c is the maximum speed at which the graviton field can propagate changes.)

**Where does c come from in GDGM?**
If space = graviton distances, then the speed of light is the maximum rate at which a disturbance in graviton density can propagate. It's set by the local graviton density ρ₀ and the force law. c is not fundamental — it's an emergent property of the vacuum state.

This is testable in principle: in regions of different graviton density (near massive objects), c should vary — which is exactly gravitational lensing and time dilation. GDGM gets this right automatically.

---

## Step 7: What Is Charge?

We have particles with density profiles. What distinguishes an electron from a proton?

The density profile has a **center** and an **edge**. The edge can be:
- Leaking outward (net graviton flow outward) → negative charge
- Drawing inward (net graviton flow inward) → positive charge
- Balanced → neutral

Charge is a property of the *direction* of the density gradient at the particle boundary, not a new substance.

**What enforces quantization of charge?**
A density profile is either stable or it's not. There are only discrete stable solutions to the hydrostatic equation (like how there are only discrete stable orbits in quantum mechanics). Each stable solution has a specific net flow direction and rate. Charge comes in discrete units because only discrete density profiles are stable.

**Why ±1 and 0, not continuous?**
This is the next hard mathematical step — we need to solve the equilibrium equation and show it has only discrete solutions. This is analogous to solving the Schrödinger equation for a hydrogen atom and finding discrete energy levels. The math likely involves boundary conditions at r=0 (minimum distance) and r=∞ (matching to vacuum ρ₀).

---

## Step 8: What Is Force Between Particles?

Two particles (two density clumps) near each other.

At the coarse level: they attract gravitationally (F = GMm/r²). This is just the aggregate of all graviton-to-graviton attractions.

But the density profiles overlap and interact. The specific way the profiles overlap determines what we call the "electromagnetic force," "strong force," etc.

**The core claim**: All these apparent forces are just gravity at the scale where density profiles interact directly — where r is so small that the 1/r² force is enormous. "EM is gravity at atomic scales."

To show this, we need to:
1. Solve for the density profile of an electron
2. Solve for the density profile of a proton
3. Calculate the force when their profiles approach each other
4. Show the result matches the Coulomb force law at the right scale

This is the key mathematical program of GDGM. It hasn't been done yet.

---

## What the Math Program Looks Like

In order, simplest to hardest:

| Step | Task | What It Proves |
|------|------|----------------|
| 1 | Choose force law F(r) at graviton scale | Foundation for everything |
| 2 | Solve equilibrium equation for minimum-energy density profile | What a "ground state" particle looks like |
| 3 | Show discrete stable profiles exist | Quantization of charge and mass |
| 4 | Calculate force between two profiles | EM as gravity at short range |
| 5 | Show force law matches Coulomb at atomic scales | Contact with experiment |
| 6 | Extend to N-body graviton dynamics | Quantum mechanics as graviton statistics |
| 7 | Take cosmological limit | Convergence / T3 |

---

## What Experiments Are Needed First

Before the math can be completed, two things must be measured or bounded:

**1. mg — the graviton mass**
Sets the energy scale for everything. The LIGO bound (< 1.78 × 10⁻⁵⁹ kg) is an upper bound, not a measurement. We need either: a direct detection, or a derivation from a measurable quantity (like the fine structure constant, or G).

**2. ρ₀ — the vacuum graviton density**
Sets the baseline field against which all density gradients are defined. Without this, we can't write down the equilibrium equation in Step 2 above. This may be related to the cosmological constant, or to the Casimir effect (which already measures vacuum energy density).

**These two numbers are the entry points. Everything else is derivable in principle once they're known.**

---

## Summary — The Simplest Logical Chain

```
A1 + A2
   ↓
Space = distance matrix
Time = distances decreasing
   ↓
Stability requires: min distance OR equilibrium
   ↓
Stable density profiles = particles
   ↓
Profile mass = mg · ξ   →   E = mc²
Profile flow direction = charge
Profile shape = all quantum numbers
   ↓
Force between profiles = all "fundamental forces"
   ↓
Cosmological limit = convergence (T3)
```

Everything hangs on solving Step 4 (density profile equilibrium). That's the mathematical heart of the theory.
