# S5.5 — Classical and Relativistic Limits

**Section code:** S5.5 (new, per CC-6 2026-04-23 addendum)
**Session:** F (Thermodynamics, Classical & Relativistic Limits)
**Epistemic tier:** 🟢 Green for (a) Newtonian limit; 🟡 Yellow for (b) SR consistency and (c) local realism framing.
**Date:** 2026-04-23

---

## Purpose

GCM claims that all fundamental physics reduces to a substrate of gravitons interacting by gravity alone. This claim is meaningful only if GCM recovers the well-tested classical and relativistic laws in their appropriate limits. S5.5 demonstrates three such recoveries:

- **(a) Newtonian gravity** emerges from the minimal-model equation in the low-density, large-distance limit, for many-graviton composite particles. 🟢 Green.
- **(b) Special relativity** is consistent with GCM when gravitons propagate effects at a universal speed $c$. Lorentz invariance is compatible with GCM's minimal model (not yet *derived* from it). 🟡 Yellow.
- **(c) Local realism via superdeterminism** — GCM's commitment that graviton distributions are real, local, and deterministic, with Bell-violating correlations explained as common-history artifacts (CC-5.5). 🟡 Yellow framing.

Each sub-claim has its own file. This document is the overview.

---

## The Minimal-Model Equation

The starting point for both (a) and (b) is GCM's minimal model equation for $N$ gravitons:

$$\ddot{\mathbf{x}}_i = \sum_{j\neq i} \frac{G\,m_g}{\max(r_{ij},\,\ell_{\min})^2}\,\hat{r}_{ij}$$

where $r_{ij} = |\mathbf{x}_i - \mathbf{x}_j|$, $\hat{r}_{ij} = (\mathbf{x}_j - \mathbf{x}_i)/r_{ij}$ is the unit vector from $i$ toward $j$, and $\ell_{\min}$ is a minimum-separation floor to prevent singularities (plausibly at or near Planck scale, per T3).

This equation is the entire "force law" of GCM at the fundamental level. Everything else (Newtonian gravity, special relativity, electromagnetism, quantum mechanics) must emerge as limits or structural consequences.

---

## (a) Newtonian Gravity as a Limit — 🟢 Green

**Summary claim.** For two composite particles (each made of many gravitons) at distances much larger than their extent, with density distributions that are locally smooth, the minimal-model equation reduces to Newton's law of universal gravitation:

$$F_{12} = G\,\frac{m_1 m_2}{r^2}$$

where $m_i = m_g \xi_i$ is the composite mass (from H6 in v2), $r$ is the center-of-mass separation, and $G$ is the Newtonian gravitational constant appearing already in the minimal-model equation.

**Why this is green.** The derivation is a straightforward linear superposition argument (full details in `a-newtonian-limit.md`): the force on particle 1 is the sum over all pairwise $G m_g^2/r_{ij}^2$ terms, which, when $r$ dominates the particle extents, factors as $G \cdot (m_g \xi_1) \cdot (m_g \xi_2)/r^2 = G m_1 m_2/r^2$. Verification: hand derivation + dimensional check + limit-case check.

See [a-newtonian-limit.md](a-newtonian-limit.md).

---

## (b) Special Relativity as Graviton-Density-Wave Propagation — 🟡 Yellow

**Summary claim.** If gravitons propagate effects through the substrate at a universal speed $c$, then the Lorentz transformations — and thus all of special relativity — are natural descriptions of how observers moving through that substrate measure each other's clocks and rulers. Lorentz invariance is *consistent* with GCM's minimal model; it is not yet *derived* from it.

**Why yellow, not green.** A full derivation would require showing that:
1. The universal speed $c$ emerges from graviton dynamics (OQ-3), and
2. The minimal-model equation, applied to perturbations propagating through a substrate, produces a wave equation with signal speed $c$ in all inertial frames.

Neither is done. What *is* done: the compatibility argument, based on Wisdom's note "21/5/25 — Everything is gravity. Einstein relativity is this." The Robertson (1949) derivation of Lorentz transformations from substrate-with-signal-speed-$c$ is referenced as the conceptual scaffolding.

See [b-special-relativity.md](b-special-relativity.md).

---

## (c) Local Realism via Superdeterminism — 🟡 Yellow framing, clean for physicist audience

**Summary claim.** GCM commits to real graviton distributions + local propagation + determinism. Bell-violating correlations in quantum experiments are common-history artifacts in a fully deterministic graviton flow, not faster-than-light signals. Measurement independence is what GCM denies; locality and realism are preserved.

**Nearest-neighbor precedent:** 't Hooft's *Cellular Automaton Interpretation of Quantum Mechanics* (2016); Sabine Hossenfelder's recent advocacy (2020+). Superdeterminism is a minority position in foundations of physics but not a crackpot one.

**For the paper audience.** Any use of "local realism" *must* be qualified with "(deterministic, with measurement-independence denied — superdeterministic reading, following 't Hooft)." The qualification is load-bearing — bare "local realism" will be dismissed on Bell grounds within seconds. This is the clean framing S5.5(c) provides.

See [c-local-realism.md](c-local-realism.md).

---

## Verification (Rollup)

| Sub-claim | Method | Verification Tier | Tally |
|---|---|---|---|
| (a) Newtonian limit | Hand derivation + dimensional check + Wolfram verification + limit case | 🟢 Green | 4/4 checks passed |
| (b) SR consistency | Conceptual framing, reference to Robertson (1949) | 🟡 Yellow | Consistent, not derived |
| (c) Local realism framing | Conceptual, cross-reference CC-5.5 | 🟡 Yellow | Framing is clean |

No overclaim: (a) is the only green claim in S5.5; (b) and (c) are framings.

---

## Success Criteria (from session brief)

- [x] Newtonian limit derivation passes verification — green
- [x] SR framing clear for physicist audience — audience-ready
- [x] Local realism framing clear and honest about superdeterminism — audience-ready
- [x] No overclaim anywhere; every conceptual piece flagged as such — explicit

All criteria met.
