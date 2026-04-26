# S1 Rationale — Reasoning Behind Key Commitments

**Section:** S1 — Ontological Foundations
**Purpose:** Internal document. Explains *why* specific choices were made in `claim.md`. Audience: Wisdom and future session agents picking up the work.

---

## CC-1: Why Option A Only (and Why C Is Ruled Out, Not Deferred)

The plan originally framed CC-1 as "commit to A for the coherence paper, flag C as future direction." Wisdom's 2026-04-23 formalization of the Axiom of Indivisibility changes this materially. The axiom argues from pure logic: a particle with internal state has parts, therefore is not indivisible. Since GCM's T1 claims "one truly fundamental, indivisible particle," the only internally consistent reading is one with no intrinsic variability — no spin, no chirality, no charge, nothing but mass and position.

This rules out Option C categorically, not strategically. It is not the case that C is inconvenient or adds formal cost; it is the case that C contradicts T1. A graviton with internal state is a compound entity in disguise.

The price is steep: the escape hatch for parity violation is closed. The weak force's maximal left-right asymmetry cannot be explained by adding graviton-intrinsic chirality. It must emerge configurationally — from the arrangement of gravitons, not from their individual properties. This is a harder derivation problem, but it is the honest one. Section S8 (Structural Challenges) will name parity violation as the single deepest open problem and flag configurational chirality emergence as the path forward.

Option B (discrete spacetime excitation / lattice node) remains formally interesting. It is not ruled out by the Axiom, because a lattice node need not have "internal state" — it is defined by its position in the lattice. However, B adds ontological complexity (the lattice itself must be specified, and the lattice dynamics become part of the theory), and the parity problem persists regardless. For the coherence paper, Option A is the right starting point: it matches the written tenets, it is simplest, and if parity violation turns out to require additional structure, that addition should be argued for explicitly, not assumed.

---

## T3 Softening: Why "Roughly Nuclear Scale" Rather Than "Exactly Neutron Density"

Version 1 of the theory stated the maximum graviton packing density as exactly the neutron star density ($\rho_n \approx 10^{18}$ kg/m³). This was always an assumption, not a derivation. The Consistency Auditor (OQ-2) flagged it: Planck density is approximately 78 orders of magnitude higher ($\rho_P \approx 5.15 \times 10^{96}$ kg/m³); the choice of $\rho_n$ has no first-principles justification and causes the graviton mass $m_g$ to scale linearly with whatever density bound is chosen.

The softening to "at roughly nuclear scale — specific value provisional (OQ-2)" preserves the structural claim (there exists a maximum packing density; it is somewhere in the vicinity of nuclear-scale densities) while being honest about the provisionality of the specific value. This also honestly reflects Wisdom's intuition (from the 2026-04-23 speech): neutrons "are much closer to the kind of maximal density" — a structural claim, not a precise one.

Two consequences of this softening: (1) the graviton mass estimate $m_g \approx 4.22 \times 10^{-87}$ kg carries implicit uncertainty scaling with the density bound; (2) the comparison "neutrons are near-maximum packing, protons are not" becomes a qualitative claim about relative density proximity, not a precise number. Both are more defensible positions.

---

## T4 Restatement: Why "Real Gradient" Rather Than "Gradient"

The original T4 says "wave-particle duality reflects real gradient distributions, not probability amplitudes." This is correct but under-specified. The restatement in `claim.md` adds the distinction between epistemic and ontic interpretations of probability in QM, and maps it clearly: GCM's reading is ontic. The apparent stochasticity of quantum measurement is not fundamental — it reflects our ignorance of the exact microstate of the graviton distribution. The distribution itself is real.

This distinction matters for the realism-locality discussion: if the "probability amplitude" is ontic (the standard Copenhagen reading), then it is not clear what "graviton density distribution" adds. GCM must argue that the wave function's apparent probability structure is a computational shorthand for a real density field that has definite values at every point, even though we cannot measure them without perturbing the system. This is the hidden-variable realist position, and it is what makes the superdeterministic path available.

The v2 document already says "boundaries are real and gradual, not probabilistic" — this restatement just makes the philosophical register explicit.

---

## Epistemic Posture: Why Name These Limits at the Start

Section S8 (Structural Challenges) is meant to earn physicist respect by naming problems openly. But the epistemic posture needs to appear in S1, not only in S8 — otherwise a reader encountering S2 through S7 develops a confidence not warranted by S1's actual claim level. Front-loading the honesty standards means that every claim in the subsequent sections is read in the right register from the start.

The specific items flagged — no Lean 4, simulation not run to completion, Claude-era label provenance, consonance-not-deduction relationship — are the same items in STATUS.md. S1 is the first place a new reader encounters the paper; it must import the honesty markers immediately, not point to STATUS.md as a footnote.
