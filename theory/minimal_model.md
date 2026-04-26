# GCM Minimal Mathematical Model
**Date**: 2026-03-21
**Purpose**: The simplest complete mathematical statement of GCM. Everything else is built on top of this.

---

## Setup

**N gravitons**, each a dimensionless point with mass mg, at positions:

```
x₁, x₂, ..., xN   ∈ ℝ³
```

That's the entire universe. Nothing else exists.

---

## The One Rule (from T2)

Every pair of gravitons attracts. The force on graviton i from graviton j is:

```
F_ij = G·mg² / r_ij²  ·  r̂_ij
```

where:
- `r_ij = |xⱼ - xᵢ|`         — distance between them
- `r̂_ij = (xⱼ - xᵢ) / r_ij`  — unit vector pointing from i toward j

The total force on graviton i is the sum over all other gravitons:

```
mg · ẍᵢ = Σⱼ≠ᵢ  G·mg² / r_ij²  ·  r̂_ij
```

Divide both sides by mg:

```
ẍᵢ = Σⱼ≠ᵢ  (G·mg) / r_ij²  ·  r̂_ij
```

**This is the equation of motion. One line. Everything in GCM follows from it.**

Note: the acceleration depends on G·mg — the product of Newton's constant and graviton mass. This is the single fundamental coupling constant of the theory. It has units m³/s².

---

## The Minimum Distance (from T1 — dimensionless point implies a floor)

If r_ij could reach zero, two gravitons would occupy the same point — a singularity. A dimensionless point has no physical size, but we assume a minimum separation ℓ_min exists (likely the Planck length, 1.616 × 10⁻³⁵ m). The modified equation of motion:

```
ẍᵢ = Σⱼ≠ᵢ  (G·mg) / r*_ij²  ·  r̂_ij

where  r*_ij = max(r_ij, ℓ_min)
```

When two gravitons reach ℓ_min, the force saturates. They stop accelerating toward each other. This prevents singularities during collapse.

---

## Conservation Laws

These follow automatically from the equations of motion (no additional assumptions):

**Energy** (conserved exactly):
```
E = (1/2)·mg·Σᵢ |ẋᵢ|²  −  G·mg²·Σᵢ<ⱼ  1/r*_ij
    \___ kinetic ___/          \___ potential ___/
```

**Momentum** (conserved exactly):
```
P = mg · Σᵢ ẋᵢ  =  constant
```

**Angular momentum** (conserved exactly):
```
L = mg · Σᵢ xᵢ × ẋᵢ  =  constant
```

---

## Initial Conditions

GCM says the universe started with gravitons separated (for reasons not yet specified) and has been collapsing ever since. The simplest starting state:

```
xᵢ(0) ~ uniform distribution over a large volume V₀
ẋᵢ(0) = 0   (or small random perturbations)
```

Gravity then does everything. No other input needed.

The total energy of this initial state is negative (pure gravitational potential, no kinetic energy):
```
E₀ = − G·mg²·Σᵢ<ⱼ  1/r_ij(0)  <  0
```

A negative total energy means the system is bound — it will collapse. T3 (convergence) is not an axiom; it's a **consequence** of A1 + A2 + this initial condition.

---

## What Is a "Particle"?

In this model, a particle is a **bound sub-cluster**: a set S of gravitons whose internal energy is negative:

```
E_S = (1/2)·mg·Σᵢ∈S |ẋᵢ - v̄_S|²  −  G·mg²·Σᵢ<ⱼ, i,j∈S  1/r*_ij  <  0
```

where v̄_S is the center-of-mass velocity of the cluster.

A bound sub-cluster holds together while the rest of the universe collapses around it. It is stable because its internal gravitational binding energy exceeds the kinetic energy of its members.

Particles are not put in by hand — they either form spontaneously during collapse or they don't. The simulation will tell us which.

---

## The Dimensionless Form (Key Insight)

Non-dimensionalize using:
- Length unit: ℓ_min
- Time unit: τ = √(ℓ_min³ / G·mg)   ← the free-fall time at minimum distance

Define dimensionless position ξᵢ = xᵢ / ℓ_min, dimensionless time s = t / τ.

The equation of motion becomes:

```
d²ξᵢ/ds² = Σⱼ≠ᵢ  (ξⱼ − ξᵢ) / max(|ξⱼ − ξᵢ|, 1)³
```

**There are no free parameters in this equation.**

G, mg, and ℓ_min only set the physical scale of the solution — they don't change its shape. Whatever patterns form in the dimensionless simulation are universal: they describe the geometry of GCM particles regardless of the specific values of the fundamental constants.

This means: we can run the simulation now, before knowing mg or ℓ_min, and the pattern geometry will already be meaningful.

---

## The Two Free Parameters

To connect simulation results to physical units, two numbers are needed:

| Parameter | Meaning | Current bound |
|-----------|---------|---------------|
| G·mg | Fundamental coupling (acceleration per unit mass per unit distance²) | mg < 1.78 × 10⁻⁵⁹ kg (LIGO) |
| ℓ_min | Minimum graviton separation | Likely ~ ℓ_Planck = 1.616 × 10⁻³⁵ m |

Everything else — particle sizes, masses, force strengths — follows from these two numbers plus the geometry of the stable patterns.

---

## What the Simulation Will Answer

1. **Do bound clusters spontaneously form?** (Does GCM produce particles at all?)
2. **What geometries are stable?** (Spherical? Toroidal? Filamentary?)
3. **Are there discrete stable sizes?** (Quantization of mass?)
4. **What is the force law between two nearby clusters?** (Does it look like Coulomb at short range?)
5. **What fraction of gravitons end up in clusters vs. diffuse background?** (What is ρ₀?)

---

## Summary

The entire theory reduces to:

```
ẍᵢ = Σⱼ≠ᵢ  (G·mg) / max(r_ij, ℓ_min)²  ·  r̂_ij
```

with N gravitons, random initial positions, zero initial velocity.

That's GCM. Everything else is interpretation of what this equation does.
