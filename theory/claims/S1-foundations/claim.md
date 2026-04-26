# S1 — Ontological Foundations

**Section:** S1 of the GCM Coherence Case
**Status:** Pre-formal. This is a coherence case, not a proof. Claims are stated at the level of tenets and ontological commitments, not derived predictions.
**Epistemic tier:** Green (tenets cleanly stated, commitments made) to Yellow (T3, T4 interpretive readings).

---

## What GCM Claims

The Graviton Gradient Convergent Universe Model (GCM) is a speculative unification program making four foundational claims, two ontological commitments, and one epistemic stance. Read together, they define a research program — not a finished theory.

The program's success criterion at this stage is **coherence**: that the claims are internally consistent, that they engage non-trivially with existing physics, and that they name their structural challenges honestly. The standard of *proof* — reproducing numerical predictions to experimental precision — belongs to a later phase.

---

## The Four Tenets

**T1 — One fundamental particle.** There is exactly one type of fundamental particle: the **graviton**. It is a dimensionless point with unit mass $m_g$ (kg). All matter, energy, space, and time are configurations of gravitons. Electrons, quarks, photons, and protons are stable density patterns in the graviton substrate, not distinct substances.

*Light math annotation:* A composite particle with $\xi$ gravitons and local packing volume $V$ has density $\rho_g = m_g \cdot \xi / V$. The particle's mass is $m = m_g \cdot \xi$.

**T2 — Gravity is the only fundamental force.** The graviton attracts all other gravitons. This is the one fundamental interaction. Electromagnetism, the strong force, and the weak force are emergent patterns in graviton density gradients. Repulsion is not a fundamental force; it is **competing attraction** — a configuration in which two bodies are each attracted more strongly elsewhere than toward each other, producing a net separating effect in a given reference frame.

*Light math annotation:* The minimal model equation of motion is $\ddot{\mathbf{x}}_i = \sum_{j \neq i} \frac{G m_g}{\max(r_{ij}, \ell_{\min})^2} \hat{r}_{ij}$, with a minimum-distance floor $\ell_{\min}$ to prevent singularities. This single equation, applied to a substrate of $\sim 10^{185}$ gravitons, is the claim's generative mechanism.

**T3 — The universe is converging.** The long-term trajectory of the universe is gravitational convergence. The cosmological interpretation of accelerating expansion is a misinterpretation of redshift and luminosity data — or an artifact of our observational position. Dark energy, as currently conceived, is not required.

*Epistemic flag (CC-4):* T3 is an axiom, not a derived prediction. The claim becomes scientific — in the Popperian sense — only when GCM specifies a quantitative redshift law and tests it against the four hardest empirical constraints: SNe Ia light-curve time dilation $(1+z)^{1.003 \pm 0.005}$ (DES 2024), ISW void-growth signal, BAO 150 Mpc ruler, and CMB blackbody preservation. This is the program's largest open empirical gap (OQ-1). **The maximum density bound ("roughly nuclear scale") is provisional.** The specific claim that maximum packing density equals neutron density ($\rho_n \approx 10^{18}$ kg/m³) is an assumption (OQ-2), not a derivation. The structural claim — that a maximum graviton packing density exists at roughly nuclear scale — is retained; the specific value scales with this choice and will be revised as OQ-2 is resolved.

**T4 — All existence is dimensions of change.** The graviton substrate is in constant flux. Space is the set of distances between gravitons. Time is the process of those distances changing. Matter is graviton density. Energy is the rate of change of density. What quantum mechanics calls a "probability distribution" is, in GCM's reading, a real distribution of graviton density structure — wave-particle duality is not epistemic (a reflection of measurement limits) but ontic (a real extended gradient structure with a sharp center and a gradual boundary).

---

## The Axiom of Indivisibility

GCM's ontological commitment to T1 is grounded by the following axiom:

> **Axiom of Indivisibility:** A truly fundamental, indivisible particle has no internal variability. All of its qualities — save its identity as a participant in the one fundamental interaction — must emerge from its relationships to other fundamental particles. Therefore the graviton has only: (i) a position in space, and (ii) its identity as a gravitating point. It cannot possess intrinsic spin, chirality, charge, or any other internal state.

This is not a preference; it is a logical consequence of "indivisible." A particle with internal structure has parts — and therefore is not indivisible. The only coherent reading of "truly fundamental, indivisible particle" is one with no intrinsic variability whatsoever.

**CC-1 commitment: Option A only.** The graviton is a classical point particle (dimensionless, scalar mass, no internal state) in 3+1D space. Option C — a graviton with small internal state (spin-like or chirality-like) — is ruled out by the Axiom, not merely deferred. This hardens the parity-violation challenge: handedness cannot be added to the graviton; it must emerge configurationally. See Section S8 for the structural challenge this creates.

---

## Realism and Locality

GCM commits to **realism**: graviton density distributions are real physical structures, not probability amplitudes. T4 is read strongly — apparent quantum stochasticity reflects our ignorance of graviton microstate, not fundamental indeterminism.

GCM also commits to **locality**: no faster-than-light signals, no action at a distance beyond what graviton-to-graviton contact (or propagation through a dense substrate) permits.

These two commitments together require a response to Bell's theorem, which rules out local hidden variables under the standard assumption of measurement independence. GCM's response is **superdeterminism**: in a fully deterministic universe, measurement choices and particle states are both consequences of the same prior conditions, so their correlations reflect common history, not nonlocal signaling. This is not a new move — it is the position of Gerard 't Hooft's *Cellular Automaton Interpretation of Quantum Mechanics* (2016). See Section S1-`realism-locality.md` for the full treatment.

**Caution:** The debate synthesis of 2026-04-03 identified "nonlocal realism (Bohmian mechanics)" as GCM's Bell escape hatch. This has been superseded by Wisdom's 2026-04-23 local-realist commitment. Bohmian mechanics remains a valid position in the broader physics landscape; GCM no longer adopts it.

---

## Epistemic Posture

This document is a **coherence case** for a speculative physics program. It inherits from `STATUS.md` the following honesty standards, non-negotiable throughout:

1. No Lean 4 formalization exists. Any prior description claiming otherwise is incorrect.
2. The N-body simulation (`GCM/simulation/gcm_nbody.py`) has not been reported as run to cluster-formation completion. Smoke tests validate Python structure, not GCM predictions.
3. Labels "Four Remembrances," "Anchor Line," and "consonance, not deduction" are Claude-era (April 2026) consolidations of content 2–4 years older. The labels are weeks old; the substance is years old.
4. The relationship between the physics and the spiritual ethos is **consonance, not deduction**. The physics does not prove the ethos; a physics of universal attraction is consonant with an ethics of connection in a way that a physics of random decay would not be.

The program's goal at this stage: demonstrate that GCM is non-trivially internally consistent, engages seriously with peer-reviewed alternatives, and names its structural challenges with clarity. That is the bar for the coherence case. Truth claims come later.
