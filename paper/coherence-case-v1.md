---
title: "A Coherence Case for the Graviton Gradient Convergent Universe Model"
author: "Wisdom Happy — Playful Sincerity Research"
date: "Draft v1 — 2026-04-25"
abstract: |
  We present a *coherence case* for the Graviton Gradient Convergent Universe Model (GCM): a single-substrate ontology in which one fundamental particle (the graviton) interacting through gravity alone is proposed as the underlying mechanism for matter, energy, and the four fundamental forces, with the long-term cosmological trajectory framed as convergence rather than expansion. We do not claim that GCM derives the Standard Model from first principles, nor that any GCM-specific testable prediction has been independently verified. We claim something narrower and, we believe, useful: that the framework's internal scaffolding is non-trivial, that its load-bearing open derivations are nameable and bounded, and that its cosmological positioning aligns with peer-reviewed alternatives to the standard cosmological model in ways that warrant engagement rather than dismissal. We present four ontological tenets, structural relations consistent with known physics, a candidate menu of cosmological redshift mechanisms with one committed primary, ten named structural challenges, and the methodology under which our claims have been internally audited (including the corrections that audit produced). The paper's distinguishing feature is that it tries to be precise about what is shown and what is not.
geometry: margin=1in
fontsize: 11pt
linkcolor: blue
urlcolor: blue
header-includes:
  - \usepackage{amsmath, amssymb, amsfonts}
  - \usepackage{microtype}
  - \usepackage{booktabs}
  - \usepackage[hang,small]{caption}
  - \setlength{\parskip}{0.5em}
  - \setlength{\parindent}{0pt}
---

## §1 Introduction

The Graviton Gradient Convergent Universe Model (GCM) is a single-substrate program. It proposes that exactly one type of fundamental particle — the graviton, taken as a dimensionless point with unit mass $m_g$ and no intrinsic structure — composes all matter and energy, that exactly one fundamental force (gravity) gives rise to all observed force phenomena via density-gradient configurations, and that the long-term trajectory of the universe is gravitational convergence rather than accelerating expansion.

This paper does not claim that GCM is true. It does not claim that any of the Standard Model's force laws have been derived from graviton dynamics. It does not claim a finished cosmological model. It claims that the framework, taken as a research program, has reached a state of internal coherence sufficient to merit engagement: ontological commitments are stated cleanly, structural relations consistent with known physics are scaffolded, a primary cosmological mechanism is committed to, structural challenges are named honestly, and verification methodology has produced specific corrections to specific errors. A reviewer should be able to engage with the program, not because we have shown it is right, but because we have tried to be precise about where it currently stands.

The paper is organized as follows. Section 2 states the four tenets and the philosophical commitments (the Axiom of Indivisibility; local realism via superdeterminism). Section 3 presents structural relations within the framework that are consistent with established physics. Section 4 introduces the substrate-compatibility scaffold for force phenomena. Sections 5 through 7 cover quantum structure, cosmology and the dark sector, and magnetism with thermodynamics, respectively. Section 8 — the section we believe earns the paper its credibility — names the structural challenges the program faces, ten of them, with concrete localization. Section 9 positions the program against peer-reviewed alternatives. Section 10 describes the verification methodology and the corrections it has produced. Section 11 presents the program's open questions. Section 12 concludes.

A companion repository (`theory/claims/`) contains, for each numerically substantiated claim in this paper, its derivation, its verification record, its caveats, and the runnable scripts used to verify it. The paper references the repository rather than reproducing derivations.

---

## §2 Ontological Foundations

GCM rests on four tenets, one axiom, and one foundational philosophical commitment. We state them explicitly so that disagreement with the program can be located precisely.

**T1 — One fundamental particle.** There is exactly one type of fundamental particle: the *graviton*. It is dimensionless (a point) with unit mass $m_g$. All matter, energy, space, and time are configurations of gravitons. Electrons, quarks, photons, and protons are stable density patterns in the graviton substrate, not distinct substances. A composite particle with $\xi$ gravitons in a packing volume $V$ has mass $m = m_g\xi$ and density $\rho_g = m_g\xi/V$.

**T2 — Gravity is the only fundamental force.** The graviton attracts all other gravitons. This is the one fundamental interaction. Electromagnetism, the strong force, and the weak force are emergent patterns in graviton density gradients. Repulsion is not a fundamental force; it is *competing attraction* — a configuration in which two bodies are each attracted more strongly elsewhere than toward each other, producing a net separating effect in a given reference frame.

**T3 — The universe is converging.** The long-term trajectory of the universe is gravitational convergence. The cosmological interpretation of accelerating expansion is, on our reading, a misinterpretation of redshift and luminosity data — or, in a softer reading, an artifact of our observational position relative to the universe's gravitational center. Dark energy as currently conceived is not required by GCM. The observed redshift–distance relation is to be accounted for by structural mechanisms reviewed in §6. We note up front that this commitment imposes significant empirical burden.

**T4 — All existence is dimensions of change.** The graviton substrate is in constant flux. Space is the set of distances between gravitons; time is the process of those distances changing; matter is graviton density; energy is the rate of change of density. What standard quantum mechanics calls a "probability distribution" is, on our reading, a real distribution of graviton density structure with measurement-apparent stochasticity reflecting our ignorance of microstate, not fundamental indeterminism.

**The Axiom of Indivisibility.** A truly fundamental, indivisible particle has no internal variability. All of its qualities — save its identity as a participant in the one fundamental interaction — must emerge from its relationships to other fundamental particles. The graviton therefore has only position and its identity as a gravitating point; it cannot possess intrinsic spin, chirality, charge, or internal state. Apparent non-gravitational properties of composite particles arise entirely from structural relationships among their constituent gravitons. The axiom is presented as a constraint on what an indivisible fundamental can coherently be: an "indivisible" particle with internal structure is, in our reading, a contradiction in terms. We acknowledge that the most contestable load-bearing premise is the move from "indivisible" to "no intrinsic variability"; the bare-particular objection (that an entity may have qualitative individuation independent of its relations) is a serious challenge that we do not resolve here.

**Local realism via superdeterminism.** GCM commits to *realism* — graviton density distributions are real physical structures, not bookkeeping for measurement probabilities. GCM also commits to *locality* — no faster-than-light signals, no action at a distance beyond what propagation through the graviton substrate permits. The combination of realism and locality is, under standard assumptions, ruled out by Bell-inequality experiments. GCM therefore takes the path that preserves both at the cost of *measurement independence*: the superdeterministic reading, in which the hidden variables of quantum particles and the settings chosen by experimenters are both consequences of the same prior conditions, so their correlations reflect common history rather than nonlocal connection. This position is a minority view in foundations of physics. It is not, however, an unsupported one: 't Hooft's *Cellular Automaton Interpretation of Quantum Mechanics* (2016) is the most developed superdeterministic-realist program, and Hossenfelder (2020 onward) has defended the reading publicly. We adopt this commitment because it is the one combination of realism, locality, and consistency with quantum experiments compatible with GCM's deterministic minimal model. The philosophical cost — that "free will" in the measurement-setting sense becomes a local illusion — is real and named.

The tenets, axiom, and philosophical commitment together define a research program. Their internal-consistency verification (encoded as first-order logic and checked via SymPy SAT/UNSAT, with a Lean 4 stub providing type-level confirmation) is recorded in `theory/claims/S1-foundations/`. We note that the Lean component is currently a `sorry`-typed stub providing structural confirmation only; a full Lean proof is aspirational and is not yet implemented.

---

## §3 Structural Relations Consistent with Known Physics

We present five structural relations within the GCM framework that are consistent with established physics. We are explicit that these are not derivations of new results from graviton-substrate first principles. They are consistency demonstrations: that the standard mathematical relations of known physics can be cast in GCM-compatible forms without contradiction. Each is supported by a verification record (Python with SymPy, mpmath, and `wolframscript` cross-checking; see corresponding folder under `theory/claims/`).

### 3.1 Photon mass (L1)

GCM's one-particle ontology forbids a strictly massless photon: photons are graviton-cluster structures, and any structure of massive gravitons has nonzero rest mass. The estimate $m_\gamma \approx 10^{-54}$ kg, equivalently $m_\gamma c^2 \approx 5.61 \times 10^{-19}$ eV, is presented as a *parametric* value consistent with experimental upper bounds, not as a derivation. The Wang et al. (2023) [VERIFY] FRB-dispersion bound of $m_\gamma \leq 2.1 \times 10^{-15}$ eV/c² is satisfied with approximately 3.57 orders of magnitude of margin; the Particle Data Group bound (2022) [VERIFY current PDG value before submission] is satisfied with approximately a factor of 1.78. We flag the PDG margin as thin and note that an improved direct experimental bound at the $10^{-19}$ eV level would directly test GCM's parametric estimate.

### 3.2 Photon speed (L2)

Given $m_\gamma > 0$, the relativistic energy–momentum relation yields a propagation speed $v < c$ for any photon of finite energy. The deviation $\Delta v = c - v$ for an optical-frequency photon at the GCM-estimated mass is approximately $10^{-29}$ m/s, far below current measurement precision. This is a consequence of L1, not an independent prediction. Its inclusion serves to make explicit that GCM accommodates a strictly subluminal photon without violating any current observation. The careful treatment requires arbitrary-precision arithmetic; standard double-precision floating point silently truncates the deviation to zero.

### 3.3 Wavelength as graviton-cluster spacing (L3)

GCM identifies a photon's wavelength $\lambda$ with the internal spacing $d$ between graviton clusters in the photon's structure: $\lambda = N \cdot d$ for a structural parameter $N$ (the number of clusters per photon, treated as fixed under any redshift mechanism). Symbolic verification confirms that under this identification, the observed-to-emitted spacing ratio satisfies $d_{\text{obs}}/d_{\text{emit}} = 1+z$. We are explicit that L3 is a *reframing*, not a derivation: we are choosing to identify $\lambda$ with $d$ rather than deriving a wave equation for graviton-cluster structures. The structural parameter $N$ is undetermined in the present treatment; closing this gap requires a concrete model of photon internal structure (named as open question OQ-R6-photon-model).

### 3.4 Graviton mass (M1)

A parametric estimate for the graviton mass is obtained from $m_g = \rho_{\text{bound}} \cdot \ell_P^3$, where $\rho_{\text{bound}}$ is the maximum graviton packing density and $\ell_P$ is the Planck length. Adopting $\rho_{\text{bound}} \approx \rho_{\text{nuclear}} \approx 10^{18}$ kg/m³ as a working value yields $m_g \approx 4.22 \times 10^{-87}$ kg, implying approximately $4 \times 10^{59}$ gravitons per neutron. We emphasize that this is a *parametric expression*, not a derivation: the choice $\rho_{\text{bound}} = \rho_{\text{nuclear}}$ is a working assumption (named as open question OQ-2), and the resulting $m_g$ scales with $\rho_{\text{bound}}^1$. Cross-tool verification confirms only that the arithmetic is correct given the inputs. The constraint from LIGO observations places $\rho_{\text{bound}} \leq 4.22 \times 10^{45}$ kg/m³, leaving the assumption with approximately 27 orders of magnitude of upper headroom; the *value* is anchored only by the nuclear-density choice.

### 3.5 Graviton-shell populations (Q2)

If graviton clusters around a center settle into a maximally dense packing, the close-packed structure has 12 nearest neighbors (Kepler's conjecture, proved by Hales 2005). The shell populations follow the formula $P_n = 10n^2 + 2$ (cataloged in OEIS as sequence A005901), giving 12, 42, 92, 162, 252, ... for the first five shells. Three geometrically distinct close-packings (FCC/cuboctahedral, HCP, icosahedral/Mackay) all yield the same shell populations, so the formula does not require committing to a specific crystallographic structure. The mathematics of close-packed shells is established (Conway and Sloane, *Sphere Packings, Lattices and Groups* [VERIFY citation]; Mackay 1962 for icosahedral case). The GCM-specific content is the *step before* the formula: the claim that uniform graviton attraction selects densest packing as the stable equilibrium for a cluster. That step is intuitive but not derived from explicit stability calculation; we note it as open work toward Q6.

We note that we have *omitted* from this section several relations that we have computationally verified. These include the Bohr-formula partial derivative ratio $\partial \ln E_1 / \partial \ln e = 4$ (E7), the Hubble-volume Planck-cell count $V_{\text{Hubble}}/\ell_P^3 \sim 10^{185}$ (M3), and the asymptotic invariant $\lim_{n\to\infty} E_n \cdot P_n = 10\,\text{Ry} = 136$ eV (Q3). These are computationally correct but their physical content is not GCM-specific; we discuss this distinction in §10.

---

## §4 Substrate Compatibility with Force Phenomena

The most ambitious claim of GCM is that the four fundamental forces emerge from configurations of gravitons interacting through gravity alone. We are unable to derive this in the present work. What we can do is present the *scaffold* for charge as graviton-flow asymmetry — the form a derivation would take — together with explicit naming of what remains to be derived.

**Charge as graviton-flow asymmetry (E1).** We posit that electric charge is a macroscopic label for the net divergence of graviton-number current in a particle's density gradient. An electron, on this reading, has a stable density configuration with $\nabla \cdot \mathbf{J}_g > 0$ at its surface (net outflow of graviton flux); a proton has the inverse ($\nabla \cdot \mathbf{J}_g < 0$, net inflow); a neutron has $\nabla \cdot \mathbf{J}_g = 0$. The minimal flow equation considered is

$$\mathbf{J}_g = -D\,\nabla\rho_g + \mathbf{v}_g\,\rho_g,$$

with the continuity condition $\partial_t \rho_g + \nabla \cdot \mathbf{J}_g = 0$. Dimensional consistency, sign-mapping across five particle species, and the divergence identity in vector calculus are all internally consistent and verified.

What is *not* derived: which graviton density configurations are stable and produce the required flux signs (open: UNSPEC-1); the quantization mechanism for $\pm e$ and for the fractional quark charges (open: UNSPEC-2). We also note two structural tensions that we discuss further in §8: the Fokker–Planck form of the flow equation includes a stochastic diffusion term inconsistent with the deterministic minimal model of T1, and a symmetric stability mechanism for shell-packed configurations is in tension with an asymmetric divergence-flux mechanism for charge sign.

We emphasize that the present treatment of E1 is a scaffold — a statement of the shape a derivation would take — not the derivation itself. We have not shown that gravity gives rise to electromagnetism. We have shown that the GCM framework permits a precise statement of what such a derivation would have to produce.

---

## §5 Quantum Structure

GCM commits to a realist reading of quantum mechanics: the wave function $\psi$ projects onto a real distribution of graviton density structure, not a probability amplitude over potential outcomes. Wave–particle duality is the natural appearance of an extended density gradient with a sharp center and a gradual real boundary; measurement-apparent stochasticity reflects our ignorance of the full graviton microstate. Combined with the local-realism-via-superdeterminism commitment of §2, this places GCM on the local-realist–superdeterminist path to quantum foundations, following 't Hooft (2016).

A full reformulation of quantum mechanics from graviton-substrate dynamics — derivation of the Schrödinger equation from a graviton-density-wave equation, derivation of the Born rule as an emergent ensemble statistic over deterministic microstates, recovery of double-slit interference as a real density-gradient propagation, and recovery of standard QED as a continuum limit — is out of scope for this paper. We name it as a long-horizon component of the research program and do not present partial results.

We note one additional structural claim. If discrete charge is to emerge from stable graviton-shell packings, the analogy with chemical magic numbers (2, 8, 18, 36, ...) and nuclear magic numbers (2, 8, 20, 28, 50, 82, 126) suggests a corresponding set of stable graviton counts $\{N_1, N_2, N_3, ...\}$. We have not performed the stability calculation that would identify the set, nor have we shown that stable packings carry exactly $\pm e$ rather than some other amount. The plausibility argument is included for completeness; the derivation is open.

---

## §6 Cosmology and the Dark Sector

GCM's cosmological commitment is convergence (T3): the long-term trajectory of the universe is gravitational coming-together, not accelerating expansion. This places the program in the company of peer-reviewed alternatives to the standard cosmological model — most prominently the Wiltshire timescape program (Seifert et al., 2025, *MNRAS Letters* 537, L55 [VERIFY citation details]), which finds Bayesian evidence $\ln B > 5$ for timescape over $\Lambda$CDM on the full Pantheon+ sample of 1535 SNe Ia, and which we discuss as a complementary program in §9. Recent DESI DR2 results (2025) [VERIFY] reporting evolving dark-energy equation-of-state $w(z)$ at 2.8–4.2$\sigma$ inconsistent with a simple cosmological constant are supportive context for the broader question of whether the standard $\Lambda$ model is correct.

We organize our cosmological treatment around the following structure: a primary mechanism for the observed cosmological redshift, a companion mechanism for the time-dilation constraint, and reframings of dark matter and dark energy.

### 6.1 Primary redshift mechanism: void decompression (R2)

We commit, for this paper, to **void decompression** as the primary GCM-compatible cosmological redshift mechanism. As matter gravitationally collapses into filaments, walls, and clusters, the graviton density in intervening voids decreases. Light traveling through decompressing voids undergoes wavelength stretching because the local graviton-density-gradient structure — which sets the effective metric in GCM's framing — relaxes as the photon transits. The structural form (not yet a derivation) is

$$\frac{d\lambda}{\lambda} \approx \int_{\text{path}} \frac{\partial \rho_g^{-1}}{\partial t}\,d\ell,$$

with the observed Hubble relation emerging as the line-of-sight average of void-decompression rates across cosmological paths. R2 has natural alignment with Wiltshire timescape: both attribute apparent acceleration to inhomogeneous-universe effects rather than to a true cosmological constant. The mechanisms differ in detail (timescape posits clock-rate differential between voids and walls; R2 posits substrate-density-gradient relaxation), but they are complementary readings of the same observational territory rather than competitors.

We do not claim a quantitative $\mu(z)$ fit. Producing one — comparing R2+R6 against Pantheon+ at the Bayesian-evidence level achieved by timescape — is named as open question OQ-R2-$\mu$(z) and is the most concrete near-term empirical engagement available to the program.

### 6.2 Time-dilation companion: photon-structure geometric dilation (R6)

The DES 2024 [VERIFY] measurement of SNe Ia light-curve time dilation at $(1+z)^{1.003 \pm 0.005}$ is the single sharpest empirical constraint on non-expansion cosmology. Any redshift mechanism that produces wavelength stretching without producing the corresponding $(1+z)$ time dilation is classical "tired light" and is ruled out at approximately 200$\sigma$.

GCM addresses this with a *companion* mechanism: photon-structure geometric time dilation (R6). The structural argument runs as follows. A photon is a traveling graviton-cluster structure. Its wavelength reflects the internal spacing between graviton clusters (L3). When a photon is redshifted by any primary mechanism (here: R2 void decompression), its wavelength increases by $(1+z)$, and so by L3 does the internal cluster spacing $d$. Increased internal spacing means longer paths for information to propagate within the photon structure. The photon's intrinsic clock — the rate at which its internal structure evolves from our observer-frame perspective — therefore ticks more slowly by the same factor:

$$\tau_{\text{obs}} = (1+z) \cdot \tau_{\text{emit}}.$$

We are direct about what this argument is and is not. It is a *structural cascade* from the L3 identification (wavelength as cluster spacing) through a propagation premise (internal information delays scale linearly with spacing) to a $(1+z)$ time-dilation prediction. The cascade is symbolically clean given its premises. The premises themselves are the open work: L3 is a reframing rather than a derivation, and the propagation premise has not been independently justified. R6 is not, in the present treatment, an independent derivation of cosmological time dilation; it is a statement that *if* the L3 identification is correct *and* internal-propagation scales as proposed, *then* the observed $(1+z)$ time dilation follows. In comparison, Wiltshire timescape derives time dilation from a non-trivial general-relativistic backreaction calculation; R6's status is structurally weaker and we do not claim parity with timescape's evidence.

What R6 does provide is sufficient escape from the tired-light falsification: GCM is not a model that predicts wavelength stretching with no time dilation. This places GCM in the same epistemic status as several other non-$\Lambda$ alternatives (timescape, certain modified-gravity programs) — a model that requires further development to compete on Bayesian evidence, but one that survives the sharpest immediate empirical disqualifier.

### 6.3 Other candidate mechanisms

We briefly note three additional candidate mechanisms for the cosmological redshift, included for menu completeness rather than as load-bearing pieces of the present argument.

- **Space friction (R1).** Photons lose energy to friction with the graviton substrate as they propagate, with energy-loss law $dE/dr = -\alpha E$. The friction coefficient $\alpha$ has no first-principles derivation in the present treatment. As a standalone mechanism, R1 is classical tired light and is falsified; combined with R6, it survives the time-dilation constraint. R1 is presented as a compatible secondary, not a primary commitment.

- **Selection effect (R5).** What we observe as cosmological redshift may, in part, be a sampling bias: at greater distances, a smaller fraction of emitted photons reaches us, and those that do may be systematically the lower-energy tail of the emission distribution. This reading is structurally distinct from in-transit mechanisms and avoids the tired-light pitfall (it makes no claim about individual photon physics). It does not, however, produce time dilation on its own; it requires an R6-like companion. R5 has no specific microscopic mechanism in the present treatment.

- **Non-central position (R3).** If we are not at the gravitational center of a converging universe, light arriving from distant sources has traversed a gravitational potential gradient and lost energy by gravitational redshift — which automatically produces $(1+z)$ time dilation, removing the need for an R6 companion. The required cosmological potential gradient is approximately $cH_0 \approx 6.8 \times 10^{-10}$ m/s² at the Hubble scale; we note as an unexplained coincidence that this is within a factor of approximately five of the MOND acceleration scale $a_0 \approx 1.2 \times 10^{-10}$ m/s² (Milgrom, 1983 [VERIFY]). However: no anisotropy of the cosmological gravitational potential at the required scale has been measured. The CMB is isotropic to $10^{-5}$ after subtraction of the dipole attributed to peculiar motion. R3 is therefore included for completeness but is currently disfavored by observation.

### 6.4 No dark matter (D1)

GCM does not introduce a new dark-matter particle. What is observationally inferred as dark matter — from galactic rotation curves, gravitational lensing, the CMB power spectrum, large-scale structure — is, on the GCM reading, ordinary matter whose electromagnetic radiation does not reach us. Primordial black holes (PBHs) in the asteroid-mass window ($10^{17}$ – $10^{23}$ g) are a specific candidate class consistent with current observational constraints. This window is the least-constrained PBH region: microlensing surveys (EROS, MACHO, OGLE, HSC/Subaru) are not sensitive to the sub-second crossing timescales of asteroid-mass PBHs, and Hawking radiation, while extremely hot for asteroid-mass black holes ($T_H \approx 1.2 \times 10^6$ K at $10^{17}$ kg), is undetectable at cosmic distances because the Schwarzschild radius is only $\sim 10^{-10}$ m, giving total Hawking luminosity of approximately 36 mW per PBH. This PBH framing is not original to GCM; it aligns with the program developed by Profumo (UCSC) and collaborators [VERIFY recent Profumo PBH paper], who treat PBHs as a serious dark-matter candidate without invoking new physics.

We acknowledge that GCM does not at present derive a halo density profile from first principles — the standard NFW or Einasto profiles consistent with rotation curves are not yet a GCM result. This is named as open question OQ-D1-halo-profile.

We note that during preparation of this paper, our internal verification process surfaced a 12-orders-of-magnitude error in the Hawking temperature initially recorded for asteroid-mass PBHs (originally written as $\sim 10^{-7}$ K, far below the CMB; correctly $\sim 10^6$ K, far above it). The observational conclusion (asteroid-mass PBHs are observationally hidden at cosmic distances) is preserved via a corrected mechanism (negligible total Hawking luminosity from the small Schwarzschild surface), but the original physical reasoning was wrong. We discuss this and similar corrections in §10.

### 6.5 No dark energy (D2)

GCM does not require dark energy. The observations standardly interpreted as evidence for accelerating expansion — SNe Ia dimming, BAO scale evolution, CMB peak structure — are, on the GCM reading, joint consequences of redshift, time dilation, and geometric dilution under a non-expansion mechanism (R2 being our committed primary). The recent Bayesian evidence in favor of timescape (Seifert et al. 2025) and the DESI DR2 evolving-$w(z)$ tension at 2.8–4.2$\sigma$ are consistent with the broader hypothesis that the standard $\Lambda$ model is incorrect. We do not claim independent evidence; we claim alliance with a peer-reviewed program already accumulating it.

We acknowledge the integrated Sachs–Wolfe (ISW) tension explicitly: a non-$\Lambda$ cosmology with growing voids should produce the ISW signal that the standard model attributes to dark-energy-driven late-time decay of large-scale potentials. R2 owes a quantitative ISW shape prediction comparable to Planck ISW–Lensing × eBOSS cross-correlation observations. This is named as open question OQ-R2-ISW and is not addressed in the present work.

---

## §7 Magnetism and Thermodynamics

We treat magnetism and thermodynamics briefly, as the present development is at plausibility level only.

**Toroidal magnetism (H1).** A working sketch posits that a graviton-density-gradient configuration with superposed radial flow and uniform drift produces toroidal streamlines, with the right-hand-rule of magnetism emerging as a topological consequence of the flow geometry, and the absence of magnetic monopoles emerging from the structural impossibility of an isolated source-divergent flow in the same picture. Dimensional consistency of the proposed coupling is verified. We note an honest finding from the verification process: pure static superposition of radial and uniform flows is curl-free, so the toroidal streamlines are *topological* rather than vortical. The missing piece for a Lorentz-force reproduction is therefore time-dependent oscillation dynamics, not just the static geometry. We name this as a sharpening of the open work (UNSPEC-4) rather than a closure.

**Release theory of heat (H2).** The structural form of Newton's law of cooling and Fourier's heat equation is reproducible within a release framework in which graviton density above a local equilibrium "releases" toward the equilibrium with linear-response dynamics. The structural reproduction is verified. The load-bearing thermodynamic content — derivation of the equipartition theorem and recovery of the Planck blackbody spectrum from graviton-release statistics — is *not* derived in the present work and is named as open work (UNSPEC-5). We also note that GCM's deterministic minimal model does not naturally produce thermalization in collisionless gravitating systems; an extension or reinterpretation is required for any genuine thermodynamic derivation.

We deliberately keep this section short. The plausibility-level status of H1 and H2 is named, not papered over.

---

## §8 Structural Challenges

This section is the section we believe most earns the paper's standing. We name ten structural challenges to GCM, each with concrete localization. Some are challenges we have raised against ourselves through the verification process; others are inherent to the program's commitments. We name them explicitly so that engagement with the program can proceed from a shared map of where it currently stands, rather than from a contest of unstated assumptions.

**1. The competing-attraction magnitude gap (E2).** GCM's account of electron–electron repulsion as competing attraction reproduces the *sign* of the observed force in an asymmetric three-body geometry. Verified across SymPy, Wolfram, mpmath, and an analytical ratio-to-fundamental-coupling check: the magnitude of the GCM-predicted apparent repulsion is approximately $10^{40}$ times weaker than the observed Coulomb force. The gap is the well-known gravity-versus-electromagnetism hierarchy and is not a toy-geometry artifact. Closing it would require an unspecified short-range amplification mechanism. We have none. Without one, GCM does not reproduce the magnitude of electromagnetism, only its sign-relation in a specific configuration.

**2. The Van der Waals functional-form falsification (E3).** A naïve reading of GCM in which atom–atom Van der Waals attraction would arise from direct overlap of graviton density gradients was tested by symbolic computation. The closed-form result for the gradient-overlap potential is exponential, not the observed $1/R^6$ power-law. The naïve reading is therefore falsified at the level of functional form. The framing co-optation — that a universal-attraction substrate is *compatible* with observed Van der Waals behavior in the way QED's Casimir–Polder calculation produces $1/R^6$ — survives. The direct derivation does not.

**3. The gradient-overlap amplification falsification (E4).** A separate proposal — that overlapping density gradients between particles would amplify the local gravitational coupling, potentially closing the E2 gap — was tested by computing the overlap potential in closed form. The result is $U(R) = -(Gm^2/R)\,\mathrm{erf}(R/2\sigma)$. This *regularizes* (the Newtonian $1/r$ singularity is softened to a finite value at $R \to 0$) but does *not amplify*. The amplification reading is falsified. The regularization observation is a positive structural side-result, but it does not address the E2 magnitude gap.

**4. The Q6–E1 stability–asymmetry tension.** Our charge-quantization sketch (Q6) posits that stable graviton configurations are symmetric closed shells, with the magnitude of the elementary charge $e$ to be derived from the smallest stable non-neutral packing. Our charge-sign mechanism (E1) requires asymmetric divergence of graviton-number current at the particle's surface. By the divergence theorem, symmetric configurations give zero net surface flux. The two mechanisms are therefore in direct tension: the same configuration cannot simultaneously be symmetric (for stability) and divergence-asymmetric (for charge sign). We do not resolve this tension in the present work; we name it.

**5. Minimal-model poverty.** The minimal model from which GCM derives its dynamics is

$$\ddot{\mathbf{x}}_i = \sum_{j\neq i} \frac{Gm_g}{\max(r_{ij},\ell_{\min})^2}\,\hat{\mathbf{r}}_{ij}$$

— pure deterministic Newtonian point-mass gravity. Several downstream claims invoke phenomena that this minimal model cannot produce: stochastic diffusion (the Fokker–Planck term in E1), thermalization (the equipartition aspiration in H2; collisionless gravitating systems are known not to thermalize), oscillatory bound states (the photon-structure picture underlying L3 and R6), and continuum-field substrate dynamics (the "graviton substrate" invoked throughout the cosmology and light sections). Either the minimal model needs to be enriched — adding fields, a Lagrangian formulation, or stochastic noise — or each downstream claim must add the qualifier that a richer foundation is required. We are committed to making this transparent rather than papering over it.

**6. Parity violation.** The Axiom of Indivisibility forbids intrinsic graviton chirality. Weak interactions' observed left-handedness must therefore emerge configurationally — handedness as a property of certain graviton arrangements, with weak interactions selecting chiral configurations. We have no derivation of emergent chirality. This is the structural cost of philosophical cleanliness on the indivisibility commitment.

**7. The semiclassical general-relativistic limit.** GCM should recover smooth-spacetime general relativity in limits where GR is well-tested: gravitational wave propagation, perihelion precession, frame dragging, gravitational lensing geometry. We have not demonstrated this recovery. Loop quantum gravity inherits an analogous problem; we name the inheritance honestly.

**8. The integrated Sachs–Wolfe tension.** Already noted in §6.5; included here for completeness as part of the structural-challenge map.

**9. The L3 → R6 cascade fragility.** The cosmological time-dilation rescue from the DES 2024 falsification depends on the L3 wavelength-spacing identification (a reframing) and on a propagation premise (internal information delays scale linearly with cluster spacing). The cascade is symbolically clean but the premises are conjectural. A specific photon-internal-structure model would be needed to upgrade R6 from "consistent with" to "derived from." We name this as open work (OQ-R6-photon-model).

**10. Bell-theorem testability cost.** The local-realism-via-superdeterminism commitment denies measurement independence. This is philosophically uncomfortable for many readers, and it is empirically difficult to distinguish from nonlocal correlations or fundamental randomness. 't Hooft (2016) and Hossenfelder have argued that superdeterminism is a respectable position; we adopt the argument without claiming a novel experimental test would resolve the choice in GCM's favor.

We also acknowledge a meta-level point: the very fact that we can produce this list — that the program's gaps are localizable at the level of specific mechanisms, configurations, and derivations rather than at the level of "the whole thing is unclear" — is part of what we believe makes the program worth engaging with. A research program whose challenges can be named is in a different epistemic state from one whose challenges cannot.

---

## §9 Literature Positioning

We position GCM relative to several existing programs. In each case, the relationship is *complementary* rather than competitive: GCM proposes a substrate-level mechanism that, if developed, would underpin the phenomenology that other programs treat at a higher level of abstraction.

**Wiltshire timescape cosmology.** The most directly aligned peer-reviewed program. Timescape, in its current state (Seifert et al., 2025 [VERIFY]), achieves Bayesian evidence $\ln B > 5$ in favor of itself over $\Lambda$CDM on the full Pantheon+ SNe Ia sample. The program attributes the apparent acceleration to clock-rate differentials between voids and galaxy walls in an inhomogeneous universe. GCM's R2 (void decompression) provides a candidate substrate-level mechanism for the same observed phenomenology: timescape posits the clock-rate effect; GCM posits a graviton-density-gradient relaxation in voids that would produce the clock-rate effect from below. We do not claim that GCM derives timescape; we claim that the two programs are compatible and would, if both correct, reinforce one another.

**Verlinde entropic gravity.** Verlinde (2017) [VERIFY paper details] treats gravity as an emergent thermodynamic phenomenon arising from information geometry of an underlying substrate. The substrate-thermodynamic lineage is shared with GCM: both treat the gravitational interaction as a consequence of substrate behavior rather than as a fundamental field. The formalisms differ — Verlinde works in a holographic/entropic formalism, GCM in a particulate/density-gradient formalism — but the broad class of approach (gravity as substrate consequence, not fundamental force in the standard sense) is common. We treat Verlinde as a thematic ancestor and do not claim independence from this lineage.

**Profumo PBH-as-dark-matter.** Profumo's program (UCSC) treats primordial black holes as a serious dark matter candidate, focusing in particular on the asteroid-mass window where current observational constraints are weakest [VERIFY recent Profumo paper]. GCM's D1 inherits this candidacy. The astrophysics is Profumo's; GCM's contribution is the ontological framing in which "ordinary matter we cannot see" is the natural answer to the dark-matter question, with PBHs as one specific class of such matter.

**'t Hooft cellular automaton interpretation.** 't Hooft (2016) developed the most extensive defense of a deterministic, superdeterministic-realist interpretation of quantum mechanics. GCM's commitment to local realism via superdeterminism is consonant with 't Hooft's program. We do not propose a cellular-automaton substrate; the graviton substrate is the GCM-specific structure. The shared philosophical commitment is the relevant alliance.

**Padmanabhan's emergent gravity.** Padmanabhan's program treats gravity as an emergent thermodynamic limit of a microscopic substrate [VERIFY relevant Padmanabhan citation]. The thematic ancestor relationship is similar to that with Verlinde. We name the lineage.

**The preon ancestry.** GCM is, in one reading, a preon program: it proposes that observed particles are composite structures of a single underlying constituent (the graviton). Constitutional preon programs (Harari, Pati–Salam, others) failed for specific reasons — hypercolor confinement, wrong predicted masses, parity-violation difficulties. GCM's commitment to a single, intrinsically structureless graviton with only positional content is specifically designed to avoid the preon-specific pitfalls: there is no internal preon structure to confine, no hypercolor charges to assign, no constituent-mass calculation required. Whether this design move actually succeeds in avoiding the failure modes is a question we treat with appropriate humility; the design intent is at least clear.

**The Kaluza–Klein lesson.** Historical unification programs that posited additional structure (extra dimensions, in Kaluza–Klein) have a long and instructive failure record. We name this lesson and accept the cautionary lineage.

We do not claim novelty against any of these programs. We claim a specific position within them: a substrate-level proposal that, if developed, would underpin the phenomenology several of them describe at higher levels of abstraction.

---

## §10 Verification Methodology and Errors Found

This section describes how the claims in this paper have been internally checked and what those checks have produced. We lead with errors caught rather than checks passed, because the errors are what most clearly demonstrate that the verification has done real work.

**Methodology.** Each numerically substantiated claim in this paper has, in the companion repository (`theory/claims/<claim_id>/verification/`), an inputs file specifying every numerical input with its source and a set of computational scripts (in Python with SymPy and mpmath, and in Wolfram Language via `wolframscript`) that compute the claim's content. Outputs are captured to text files with a header recording the run date, tool versions, and pass/fail status. Each claim's verification record (`verification.md`) summarizes the checks and links to the scripts and outputs. The methodology follows the pattern that we previously developed and validated on the Indexed Virtual Number Algebra (IVNA) project (~500 checks, 0 failures, multi-tool cross-checking).

**Cross-tool agreement is necessary but not sufficient.** We are explicit about the limits of multi-tool computational verification. When two independent computer-algebra systems compute the same algebraic quantity and agree to many digits, this is strong evidence that the *arithmetic* is correctly performed in both tools, and that no transcription bug has corrupted the calculation. It is not, by itself, evidence about the *physical content* of the underlying claim, because the claim's physical content is in the choice of equation to compute, not in the computation itself. Several of our verified claims (the Bohr-formula partial derivative E7, the sphere-volume-over-cube ratio M3, the algebraic limit Q3, the Newtonian-gravity recovery S5.5(a)) reduce to standard textbook calculations whose form is independent of GCM. Their cross-tool verification confirms that the standard calculations are correctly carried out; it does not constitute GCM-specific evidence. We have flagged these distinctions in the per-claim records and have introduced a separation in our internal ledger between "computational checks passed" and "physics-content tier." We mention this here so that a reader of the verification records does not over-interpret a green-tier tally as automatic GCM-specific support.

**Errors caught.** The verification process surfaced four substantial corrections during the most recent retrofit pass.

1. *The Hawking temperature error in D1.* The original `plausibility.md` for the no-dark-matter argument recorded the Hawking temperature of an asteroid-mass PBH as $T_H \approx 6 \times 10^{-7}$ K, far below the CMB temperature, and inferred from this that asteroid-mass PBHs would be observationally hidden. The verification re-derivation gave $T_H \approx 1.2 \times 10^6$ K — twelve orders of magnitude in the opposite direction, far above the CMB. The observational conclusion (asteroid-mass PBHs are hidden at cosmic distances) survives, but via a corrected mechanism: the Schwarzschild radius is approximately $10^{-10}$ m, giving total Hawking luminosity per PBH of approximately 36 mW, which is undetectable at cosmic distances regardless of temperature. The corrected reasoning is in the current `claim.md`; the error in the original plausibility note has been retained in the chronicle so that the correction trail is auditable.

2. *The R3 gradient error.* The required cosmological gravitational potential gradient for the non-central-position redshift mechanism was originally given as approximately $2 \times 10^{-8}$ m/s². The correct value is $cH_0 \approx 6.8 \times 10^{-10}$ m/s² — a factor-of-30 error. The corrected value is what makes visible the unexplained coincidence with the MOND acceleration scale, which we report in §6.3.

3. *R1 labelling and parameter errors.* The space-friction mechanism's plausibility note contained two-orders-of-magnitude arithmetic errors in the graviton number density $n_g$ and in the substrate-coupling cross-section $\sigma_g$, together with an implicit confusion between the Hubble radius and the observable-universe radius. These were corrected and the convention was made explicit.

4. *L1 photon-mass margin overstatement.* The original margin between the GCM photon-mass estimate and the Wang et al. (2023) FRB bound was stated as "4 orders of magnitude." The corrected value is 3.57 orders. This is a small correction by absolute magnitude but it preserves margin honesty and the practice of reporting derived quantities to declared precision.

We also caught several toolchain-specific bugs: a Wolfram `Solve` over-constraint pattern that silently returns an empty solution set (caught twice, in L3 and R6); an mpmath binary-precision rounding behavior that converted a $5\sigma$ test result into a $3\sigma$ printed verdict; Mathematica's underscore-as-pattern-delimiter convention silently failing variable assignments. We mention these because they illustrate the cross-tool verification's practical value: the bugs are tool-specific and would not have been caught by single-tool verification or by hand calculation.

**The corrections matter for paper-reading.** A reviewer should be aware that these errors existed in earlier drafts of the GCM materials and that they were caught by our own verification methodology before reaching this paper. The records of the corrections are in the chronicle and per-claim history. The paper-as-presented has been audited against the corrections.

---

## §11 Open Research Questions and Empirical Hooks

We name the open questions that the program currently faces. Each is recorded in the companion repository (`research/open-questions.md`) with a "what would close it" criterion. The list below is not exhaustive but covers the load-bearing items.

**Foundational.** OQ-2: derive the maximum graviton packing density $\rho_{\text{bound}}$ from first principles, rather than assuming nuclear density. OQ-3: derive the universal signal speed $c$ from graviton-substrate dynamics rather than postulating it. OQ-4: derive the vacuum graviton density $\rho_0$. UNSPEC-1, UNSPEC-2: derivations of stable graviton density configurations producing the observed charge species and the quantization at $\pm e$. UNSPEC-3, UNSPEC-4, UNSPEC-5: parity-violation mechanism, Lorentz force reproduction from time-dependent toroidal flow, and equipartition + Planck's-law derivations.

**Cosmological.** OQ-R2-$\mu$(z): produce a quantitative GCM cosmology fit against Pantheon+ at the Bayesian-evidence level, comparing against $\Lambda$CDM and timescape. OQ-R2-ISW: produce a quantitative ISW signal shape prediction comparable to Planck-ISW × eBOSS observations. OQ-cosmology-early: produce a GCM treatment of the early universe (BAO sound horizon, BBN element abundances, CMB acoustic peak structure). OQ-D1-halo-profile: produce a GCM-derived galactic halo density profile comparable to NFW or Einasto. OQ-D1-PBH-mass-function: derive the asteroid-mass PBH window from GCM early-universe dynamics, or honestly note that D1 is mass-function-agnostic and depends on the window staying observationally open.

**Empirical hooks.** The program's strongest near-term empirical engagements, as we currently see them, are: (a) producing the OQ-R2-$\mu$(z) Bayesian fit, which is an immediately tractable analysis on existing Pantheon+ data; (b) producing the OQ-R2-ISW signal shape, which is similarly an analysis question rather than a new observation; (c) tightening the photon-mass bound at the $10^{-19}$ eV/c² level, which would directly test the L1 parametric estimate, plausibly via improved FRB dispersion-measure analyses extending Wang et al. (2023); (d) high-cadence asteroid-mass PBH microlensing surveys (e.g., Subaru HSC continuations) constraining the D1 candidate. We are not in a position to design a definitive single experiment that would discriminate GCM from $\Lambda$CDM — the program is not at the stage where a single experiment can be designed against it. But the empirical hooks above are concrete and several are immediately actionable.

A more comprehensive treatment of the program's experimental and observational future is beyond the scope of this paper. We anticipate developing it as a separate piece of work, in coordination with researchers whose expertise is in the specific empirical areas (cosmological observations, FRB analyses, microlensing surveys, and the foundational-physics community).

---

## §12 Conclusion

This paper has presented a coherence case for the Graviton Gradient Convergent Universe Model. We have stated four ontological tenets, an axiom of indivisibility, and the local-realism-via-superdeterminism commitment that together define the program. We have presented structural relations within the framework consistent with established physics, taking care to mark which are genuinely new GCM content and which are textbook calculations cast in GCM-compatible form. We have committed to a primary cosmological redshift mechanism (R2, void decompression, allied with Wiltshire timescape) and named its time-dilation companion (R6) along with the dependencies that make R6 a structural cascade rather than an independent derivation. We have presented our reframing of dark matter (D1, allied with Profumo's PBH program) and dark energy (D2, allied with timescape and supported by the recent DESI DR2 evidence for evolving $w(z)$). We have named ten structural challenges to the program, including challenges raised against ourselves by our own verification process. We have positioned the program against existing peer-reviewed work, claiming complementarity rather than novelty. We have described the verification methodology under which the present claims have been audited and have led with the four substantial corrections that audit produced.

We do not claim that GCM is true. We do not claim that any GCM-specific testable prediction has been experimentally verified. We do not claim a derivation of the Standard Model. We claim that the framework, taken as a research program, has reached a state of internal coherence sufficient to merit engagement.

GCM is not yet a theory. It is a research program whose internal consistency we have tried to establish honestly, whose structural challenges we have named concretely, and whose open questions we believe are worth the work. We invite engagement on either ground: the substantive program, or the methodology by which we have tried to make it auditable.

---

## Acknowledgments

The development of GCM, the verification infrastructure, and the audit underlying this paper was conducted in collaboration with the Playful Sincerity Digital Core (PSDC), an AI methodology layer built on Claude (Anthropic) that has served as a research and writing partner throughout. The methodology shares a lineage with our prior work on Indexed Virtual Number Algebra (IVNA). Discussions with Stefano Profumo, Kiel Howe, and members of the Frontier Tower AI reading club informed several of the literature-positioning paragraphs and the framing of structural challenges. All errors are the author's; the corrections to the errors are described in §10.

---

## References

*The reference list below is the working set assembled during paper preparation. Several entries are marked [VERIFY] and require live confirmation against current literature before submission.*

- Conway, J. H., and Sloane, N. J. A. *Sphere Packings, Lattices and Groups*, 3rd edition, Springer, 1999. [VERIFY edition]
- DESI Collaboration, *DESI 2025 Results: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations*, 2025. [VERIFY exact title and arxiv]
- Dark Energy Survey Collaboration, *Time Dilation in Type Ia Supernovae from the Dark Energy Survey*, 2024. [VERIFY citation]
- Hales, T. C. *A proof of the Kepler conjecture*, Annals of Mathematics 162 (2005), 1065–1185.
- Harari, H. *A schematic model of quarks and leptons*, Physics Letters B 86, 1979. [VERIFY]
- Hossenfelder, S. *Superdeterminism: A Guide for the Perplexed*, 2020. [VERIFY exact venue]
- Jacobson, T. *Thermodynamics of Spacetime: The Einstein Equation of State*, Physical Review Letters 75, 1995, 1260–1263.
- Mackay, A. L. *A dense non-crystallographic packing of equal spheres*, Acta Crystallographica 15, 1962, 916–918.
- Milgrom, M. *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis*, Astrophysical Journal 270, 1983, 365–370.
- OEIS Foundation Inc. *Sequence A005901*, *The On-Line Encyclopedia of Integer Sequences*, 2026.
- Padmanabhan, T. *Thermodynamical aspects of gravity: New insights*, Reports on Progress in Physics 73, 2010, 046901. [VERIFY]
- Particle Data Group, *Review of Particle Physics*, 2022 edition. [VERIFY current PDG photon mass bound]
- Pati, J. C., and Salam, A. *Lepton number as the fourth color*, Physical Review D 10, 1974, 275.
- Profumo, S. (et al.), *Primordial Black Holes as Dark Matter*, recent paper [VERIFY exact citation; UCSC group, 2024 or 2025].
- Robertson, H. P. *Postulate versus observation in the special theory of relativity*, Reviews of Modern Physics 21, 1949, 378.
- Seifert, A., et al., *Bayesian evidence for the timescape cosmology*, Monthly Notices of the Royal Astronomical Society Letters 537, 2025, L55. [VERIFY exact authors and pagination]
- 't Hooft, G. *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer, 2016.
- Verlinde, E. P. *Emergent Gravity and the Dark Universe*, SciPost Physics 2, 2017, 016. [VERIFY exact venue]
- Wang, X., et al. *Constraints on the photon mass from fast radio bursts*, 2023. [VERIFY exact authors and venue]

*Companion repository (claims, derivations, verification records): `https://github.com/Playful-Sincerity/...` [TODO: confirm public repository URL before submission, or include zenodo DOI for archived snapshot.]*

---

*Draft v1, 2026-04-25. Status: ready for citation pass and sentence-level audit. Companion documents: `theory/claims/audit-2026-04-24.md` (per-claim audit), `theory/claims/ledger.md` (verification record), `concept-paper/paper-1-plan.md` (writing plan), `research/open-questions.md` (full OQ list).*
