# GCM — Aspirational Research Program Plan

**Date:** 2026-04-23
**Status:** Provisional. Living document. Updated as claims clarify and math lands.
**Source speech:** [`../knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md`](../knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md)
**Purpose:** Map of every GCM claim, organized by domain, with an honest per-claim assessment of what math we can actually show, what's conceptual only, and what's structurally out of reach. Serves as the navigation document for the coherence-case paper and any future multi-session decomposition.

---

## 0. Framing — the aspirational lens

The repo's public-facing artifacts (`README.md`, `STATUS.md`, `archive-highlights.md`) hold GCM as pre-formal and speculative. That honesty standard still governs what we *claim*. But for the purposes of this plan, we adopt the lens Wisdom named in the 2026-04-23 speech:

> *"Taking an aspirational lens that this could actually be possible. I know there's a lot of things pushing against that, but just from the basic core tenants we've gone down to the base right everything's explainable by gravity, all forces are explainable by gravity, there's one fundamental particle, everything else is made up of that, and all of reality is composed of those things — so you have to be able to explain every fundamental force from that."*

Method: assume T1–T4 could be right, work out what math would have to hold for the picture to be coherent, then name what we can show rigorously vs. what remains conceptual. The success criterion for this document is not *"GCM is true"* but *"the case for coherence is strong enough that serious physicists will engage rather than dismiss."*

The tenets in full:

1. **One fundamental particle** — the graviton (dimensionless point).
2. **One fundamental force** — gravity. All other forces are emergent.
3. **Maximum density principle** — there is a universal density ceiling at roughly nuclear scale. The exact value is open (may be slightly above or below ρ_neutron); the *existence* of the bound is the structural claim.
4. **All existence is dimensions of change** in the graviton substrate. Space = graviton distances. Time = process of those distances changing. Matter = regions of high graviton density. Energy = rate of pattern shift.

From `GCM/theory/core_tenets.md`.

---

## 1. How to read this plan

Every claim below is tagged with:

- A **code** (e.g., M1, E7, R2) for cross-reference
- A **tier:** 🟢 Green = verifiable now with existing math; 🟡 Yellow = small derivation or literature survey gets us there (1–3 weeks); 🔴 Red = structural gap, needs new formalism or confronts a hard objection
- A **one-line claim**
- A **what would make it real** note

The green tier is what we write formally first. The yellow tier is what the coherence paper includes at the "here's how this would have to work" level, without claiming proof. The red tier gets named explicitly in the STATUS section as what we cannot yet address — the honesty markers.

---

## 2. The claim map

### I. Fundamental ontology (tenets held as constitution)

| Code | Claim | Tier |
|---|---|---|
| T1 | One fundamental particle: the graviton | 🟢 definitional |
| T2 | One fundamental force: gravity | 🟢 definitional |
| T3 | Maximum density at roughly nuclear scale | 🟡 argued, not derived |
| T4 | Existence = dimensions of change in graviton substrate | 🟢 definitional |

These are the axioms; they don't require proof, they require consistency with everything below.

### II. Mass and scale

| Code | Claim | Tier |
|---|---|---|
| M1 | Graviton mass from Planck length + nuclear density: `m_g = ρ_bound · ℓ_P³ ≈ 4.2 × 10⁻⁸⁷ kg` | 🟢 dimensional + arithmetic |
| M2 | Gravitons per neutron: `N_g = m_n / m_g ≈ 4 × 10⁵⁹` | 🟢 arithmetic consequence |
| M3 | Total graviton count in observable universe: ~10¹⁸⁵ | 🟢 Planck-cell dimensional estimate |
| M4 | Inertial mass as graviton density (corrected from v1's broken formula: `m = m_g · ξ`) | 🟢 dimensional |
| M5 | Light has rest mass (~10⁻⁵⁴ kg order) | 🟡 consistent with LIGO, needs independent bound argument |

*What "green" means here:* the arithmetic is independently reproducible. A physicist can compute `m_g = 10¹⁸ × (1.616 × 10⁻³⁵)³` and confirm it in 30 seconds. What the arithmetic does NOT prove is that `ρ_neutron` is the correct bound — only that IF something at nuclear density is the bound, THEN `m_g` takes that value.

### III. Charge and electromagnetism

| Code | Claim | Tier |
|---|---|---|
| E1 | Charge is graviton flow asymmetry: electrons outflow, protons inflow, neutrons balanced | 🔴 needs a flow equation and a derivation of why these configurations are stable |
| E2 | "Repulsion" is competing attraction — like-charges don't repel, they're each preferentially attracted elsewhere | 🟡 needs a worked toy model (two-body + environment) to show the observed force emerges |
| E3 | Van der Waals IS the universal gravitational attraction between density-gradient overlaps | 🟡 needs comparison of `1/r⁶` VdW with gradient-overlap geometry |
| E4 | Density-gradient overlap explains why gravity can be "strong enough": particles aren't points, they're extended distributions that massively overlap | 🟡 needs a worked overlap integral |
| E5 | Lorentz force `F = q(E + v×B)` reproduced from toroidal-oscillation alignment | 🔴 urgent UNSPEC-4 from v2; must reproduce exactly, not just analogically |
| E6 | Temperature modulates charge behavior via ambient graviton density (explains ionization thresholds) | 🔴 conceptual only |
| E7 | Charge-mass compensation constraint: `Δm_e/m_e = −4 · Δe/e` preserves hydrogen Bohr energy | 🟢 clean calculus derivation |

*The key one here is E2.* If competing-attraction can be shown in a clean two-body + background-field model — two electrons in a bath of protons, showing the net force matches the observed "repulsion" — that would be the strongest unification argument in the whole plan. It's the load-bearing claim for "all forces are gravity."

### IV. Quantum structure

| Code | Claim | Tier |
|---|---|---|
| Q1 | Pauli exclusion from toroidal oscillation interference | 🔴 needs a wave equation for toroidal oscillations |
| Q2 | Tetrahedral shell geometry: `P_n = 10n² + 2` (FCC/tetrahedral lattice, 12 nearest neighbors) | 🟡 known geometric result for FCC packing; we need to derive it from first principles |
| Q3 | `E_n · P_n ≈ 136–163 eV` across hydrogen levels n=1–5 (approximate invariant; corrected from v1) | 🟢 direct computation |
| Q4 | Discrete charge = stable shell packings under gravitational symmetry | 🟡 needs geometric argument; links to Q2 |
| Q5 | Wave-particle duality as real gradient distributions, not probability amplitudes | 🔴 conceptual only; requires reformulating QM |
| Q6 | Why electrons have a single discrete charge: stable shell packings favor specific graviton counts | 🟡 connects Q2 to charge quantization |

*Q3 is already done and lives in `theory/versions/gcm_v2.md` Part III, H7.* Worth writing up as a standalone note — it's the strongest numerical result in the project.

### V. Magnetism and thermodynamics

| Code | Claim | Tier |
|---|---|---|
| H1 | Magnetism from toroidal-oscillation alignment under charge motion | 🔴 conceptual |
| H2 | Release Theory of Heat: thermal radiation is graviton shedding | 🔴 conceptual |
| H3 | Ferromagnetism from coherent oscillation across domains | 🔴 conceptual |
| H4 | Black body spectrum from collective graviton release | 🔴 needs derivation reproducing Planck's law |
| H5 | Equipartition (`CV = 3/2 kT`) and Fourier's law reproduced | 🔴 UNSPEC-5 from v2 |

These are the weakest tier for formalization. They're plausible framings in the aspirational lens but would each require years of work to formalize. For the coherence paper: state them, flag them honestly, don't try to prove them yet.

### VI. Light and redshift — the critical cluster

This is the most important domain for the coherence case. Wisdom explicitly asked to map it.

| Code | Claim | Tier |
|---|---|---|
| L1 | Photon speed deviation from `c` given small rest mass: `v = c√(1 − (m₀c²/E)²)` | 🟢 standard relativity |
| L2 | Photon redshift produces geometric time dilation: as wavelength increases, internal graviton-cluster spacing increases, delaying information | 🟡 needs to show SNe Ia light-curve stretching factor emerges correctly |
| L3 | Light wavelength ∝ internal graviton-cluster spacing | 🟡 dimensional argument needed |

### VII. Cosmological redshift mechanisms — the menu

The repo's largest open gap (OQ-1). Multiple candidates exist; the coherence paper must commit to at least one.

| Code | Mechanism | Source | Tier | Key strength | Key weakness |
|---|---|---|---|---|---|
| R1 | **Space friction** — light loses energy to graviton friction along path | v2 source notes | 🔴 | Mechanistically simple | Must reproduce z vs. distance exactly without contradicting CMB |
| R2 | **Void decompression** — voids between collapsing clusters expand as matter falls inward; light stretched in transit | Wisdom's speech 2026-04-23: *"distant galaxies when they compress they actually expand the space in between them"* | 🟡 | Structurally consistent with convergence | Con debate surfaced internal tension: in a converging universe, where does net void growth come from? |
| R3 | **Non-central position** — Earth is not at the gravitational center; distant light is preferentially attracted elsewhere, arrives at lower energy | v2 source notes | 🟡 | Explains isotropy and distance dependence | Requires a specific anisotropy that hasn't been measured |
| R4 | **Light-pressure sensitivity** — light lowers frequency in low graviton-density regions | v2 source notes | 🔴 | Plausible mechanistic feel | No quantitative form |
| R5 | **Selection effect** — "light just doesn't get to us because we're small"; we sample a biased subset of emitted light; what arrives is the low-energy tail | Wisdom's speech 2026-04-23 | 🟡 | Structurally different from tired-light; sidesteps the time-dilation objection entirely | Needs a rigorous scattering model |
| R6 | **Photon-structure time dilation** — as a photon redshifts, the internal distance between its graviton clusters increases, producing geometric time dilation without invoking Lorentz dilation | 2022 物理 Outline, preserved through v2 | 🟡 | This is GCM's structural answer to the classical tired-light death (SNe Ia light-curve stretching). Already in the notebooks since 2022. | Needs quantitative coupling to R1–R5 |

**R2 and R5 are the strongest candidates for the coherence paper.** R2 is empirically testable (void expansion rates should follow specific scaling with cluster collapse rates) and has structural sympathy with convergence. R5 avoids the tired-light pitfalls entirely because it's not a physics claim about photons — it's a selection claim about what we measure.

**R6 is not a redshift mechanism; it's the answer to a specific objection** against redshift mechanisms (the SNe Ia light-curve death of classical tired light). Worth keeping separate.

### VIII. Dark matter and dark energy

| Code | Claim | Tier |
|---|---|---|
| D1 | No dark matter particle. What's inferred as dark matter is ordinary matter whose light doesn't reach us | 🟡 |
| D2 | No dark energy. The accelerating-expansion inference misreads one of R1–R5 | 🟡 |
| D3 | Galactic rotation curves explainable without extra matter, using graviton density gradients at scale | 🔴 UNSPEC; needs to reproduce `v(r)` at large radii |
| D4 | Gravitational lensing as expected from ordinary matter + gradient effects | 🔴 needs to reproduce observed lensing profiles |

*D1 is one of GCM's cleanest claims and it aligns directly with mainstream heterodoxy (Profumo's "waning of the WIMP," primordial-black-hole-as-DM programs).* The coherence paper should lead with D1 as the most rhetorically defensible external claim — it doesn't require new physics to explain the absence of a particle; it requires honest bookkeeping about photon propagation.

### IX. Unification — how the other forces emerge

| Code | Claim | Tier |
|---|---|---|
| U1 | Strong force from density-gradient confinement at extreme densities (hadrons) | 🔴 conceptual |
| U2 | Weak force from density-gradient instability / rearrangement (decay) | 🔴 conceptual |
| U3 | Why the four forces have different symmetries: emerges from the density regime in which they operate | 🔴 conceptual |
| U4 | **Parity violation** — the weak force couples exclusively to left-handed fermions | 🔴 **structural wall** (per 2026-04-03 debate) |

*U4 is THE hardest problem.* A scalar, isotropic graviton cannot encode handedness. For the coherence paper, this must be named explicitly as a known structural challenge, not hidden. Accommodating it would require adding structure to the graviton — moving from strict point particles to something with internal state. That's a frame-changing extension we're not making in the coherence paper but is flagged as the direction v3+ would have to go.

### X. Philosophical implications (the ethos bridge)

| Code | Claim | Tier |
|---|---|---|
| P1 | The ethos is consonant with, but not deduced from, the physics | ✓ established (2026-04-03 debate) |
| P2 | "God is Gravity" as structural, not metaphorical — gravity is the universal organizing principle, and love/connection are local instantiations | ✓ framing, not empirical claim |
| P3 | Consciousness as meta-gravitational: compression-of-compression (per 2026-04-09 play session) | 🟡 conceptually rich, mathematically speculative |

These live in `../Spiritual Ethos/` and are not part of the physics paper. Included here only to maintain the two-halved repo structure.

---

## 3. Verifiable math pieces — what to write first (🟢 tier)

Five short formal notes. Each ~1–2 pages. Together they form the rigorous spine of the coherence paper.

### 3.1. Graviton mass from Planck scale (M1, M2)

**Starting point:** Planck length `ℓ_P = √(ℏG/c³)`; universal density bound `ρ_bound` (approximately nuclear scale).

**Derivation:**
```
V_P = ℓ_P³ ≈ 4.22 × 10⁻¹⁰⁵ m³
m_g = ρ_bound · V_P
    ≈ 10¹⁸ kg/m³ · 4.22 × 10⁻¹⁰⁵ m³
    ≈ 4.22 × 10⁻⁸⁷ kg
```

**Verification:** pure arithmetic; any reader can reproduce.

**LIGO bound:** `m_g < 1.78 × 10⁻⁵⁹ kg`. Our estimate is 28 orders below. Theory passes the constraint.

**What this shows:** if there IS a max density and space IS quantized at the Planck scale, this is the graviton mass that follows. The result is *scale-robust*: a 10× different `ρ_bound` changes `m_g` by 10×, nothing else. The *structural* claim `m_g ∝ ρ_bound · ℓ_P³` is what's load-bearing.

**What this doesn't show:** that the bound IS nuclear density (open question OQ-2). The specific value of `m_g` is provisional.

### 3.2. Charge-mass compensation constraint (E7)

**Starting point:** Bohr ground-state energy `E₁ = −m_e k² e⁴ / (2ℏ²)`.

**Derivation:** set `∂E₁/∂e · Δe + ∂E₁/∂m_e · Δm_e = 0`.
```
∂E₁/∂e = −2m_e k² e³/ℏ²
∂E₁/∂m_e = −k² e⁴/(2ℏ²)

⇒ Δm_e/m_e = −4 · Δe/e
```

**What this shows:** if any unified theory treats `e` and `m_e` as emergent from a common substrate, their co-variation must satisfy this ratio to preserve hydrogen spectroscopy (which is measured to parts-per-billion precision). It's a **consistency constraint** on emergent-charge-and-mass theories, not a prediction of fluctuations.

**What this doesn't show:** that fluctuations actually happen. Framed as constraint, not prediction.

**Caveats to name:** uses non-relativistic Bohr; QED corrections (Lamb shift) dominate at the precision where `Δe ~ 10⁻³⁵ C` would matter; `e` and `m_e` aren't cleanly separable in QFT (electron mass absorbs EM self-energy).

### 3.3. `E_n · P_n ≈ constant` invariant (Q3)

**Starting point:** Bohr energy levels `E_n = −13.6 eV / n²`; tetrahedral shell populations `P_n = 10n² + 2`.

**Computation:**

| n | P_n | E_n (eV) | E_n · P_n (eV) |
|---|---|---|---|
| 1 | 12 | 13.600 | 163.2 |
| 2 | 42 | 3.400 | 142.8 |
| 3 | 92 | 1.511 | 139.0 |
| 4 | 162 | 0.850 | 137.7 |
| 5 | 252 | 0.544 | 137.1 |

**What this shows:** the product `E_n · P_n` varies by ~20% across n=1–5, with clear asymptote at ~136 eV ≈ 10 × 13.6 eV. Approximate invariant.

**What this doesn't show:** that the FCC/tetrahedral shell structure *produces* the Bohr spectrum. We're observing a numerical coincidence, not deriving one from the other. The direction of "this is why hydrogen quantizes" requires showing the shell populations emerge from the graviton packing AND the energy associated with each shell configuration matches `1/n²` scaling.

### 3.4. Photon speed given small rest mass (L1)

**Starting point:** energy-momentum relation `E² = (pc)² + (m₀c²)²`.

**Derivation:** `v = c · √(1 − (m₀c²/E)²)`.

**Example:** `m₀ = 10⁻⁵⁴ kg`, `E = 1 eV` ⇒ `Δv ≈ 4.74 × 10⁻²⁹ m/s`.

**What this shows:** a small photon rest mass produces a deviation from `c` that is far below current experimental resolution. Not contradicted.

**What this doesn't show:** that the photon HAS rest mass. Only that if it did, at this scale, it'd be consistent with observation.

### 3.5. Universe Planck-cell count (M3)

**Starting point:** observable universe sphere `R_H ≈ 4.4 × 10²⁶ m`; Planck volume `V_P = ℓ_P³`.

**Derivation:**
```
N = (4/3)π R_H³ / ℓ_P³ ≈ 8.5 × 10¹⁸⁴ ≈ 10¹⁸⁵
```

**What this shows:** if space is quantized at Planck scale and is uniformly packed, this is the total graviton count.

**What this doesn't show:** that space is so packed. Dimensional estimate only.

---

## 4. Conceptual pieces — the 🟡 yellow tier

For the coherence paper, each of these gets a 1-page treatment: the claim, the plausibility argument, the nearest-neighbor physics, and an honest "here's what closing this rigorously would require."

**Priority yellow claims for the paper:**

1. **E2: Competing attraction** — most important. Need a toy model (two electrons + proton + background) showing the observed repulsion emerges as net competing attraction. This is the unification load-bearer.
2. **E3: Van der Waals as universal attraction** — leverage existing physics (VdW IS already a universal weak attraction); show the GCM picture is continuous with this rather than adding something new.
3. **E4: Density-gradient overlap** — explains how gravity can be both universally weak and locally strong. Needs a worked gradient-overlap integral.
4. **R2: Void decompression redshift** + **R5: Selection-effect redshift** — pick one (or both) as GCM's commitment. Survey observational data.
5. **R6: Photon-structure time dilation** — kill the classical-tired-light death by showing the time dilation emerges geometrically.
6. **D1: No dark matter** — one of the cleanest claims; rhetorically strongest. Connect to Profumo's mainstream heterodoxy.
7. **Q2/Q6: Shell-packing quantization** — derive `P_n = 10n² + 2` from FCC geometry; discuss why discrete packings produce discrete charges.
8. **M5: Light has mass** — state consistent with LIGO + ties to L1.

---

## 5. Red-tier claims — honest name, don't fake the math

For the coherence paper, these appear in a "Known Structural Challenges" section:

- **U4: Parity violation** — the scalar-graviton / left-handed-fermion vocabulary problem. Must be named explicitly. Future work direction: adding internal graviton state (frame-changing).
- **E5: Exact Lorentz force reproduction** — UNSPEC-4 urgent.
- **H4/H5: Black body spectrum, equipartition** — must reproduce to not embarrass the framework.
- **Q1: Pauli exclusion wave equation** — UNSPEC-3.
- **Bell's theorem (navigable but deep)** — requires commitment to nonlocal realism (Bohmian-type).

Naming these is what earns physicists' respect. Hiding them is what earns their dismissal.

---

## 6. Proposed folder structure

Current `GCM/theory/` has the axioms and v2 document. The plan proposes adding a `claims/` subfolder so each claim gets its own working directory. That lets future sessions build verification work claim-by-claim without touching the parent documents.

```
GCM/
├── plan.md                        ← this file (the map)
├── theory/
│   ├── core_tenets.md             ← existing
│   ├── overview.md                ← existing
│   ├── minimal_model.md           ← existing
│   ├── derivation_sketch.md       ← existing
│   ├── source_notes.md            ← existing
│   ├── versions/                  ← existing (gcm_v2.md)
│   └── claims/                    ← NEW
│       ├── README.md              ← claim index with tier tags
│       ├── M1-graviton-mass/
│       │   ├── claim.md           ← short statement
│       │   ├── derivation.md      ← rigorous math
│       │   ├── verification.md    ← independent check
│       │   └── caveats.md         ← what it doesn't prove
│       ├── E2-competing-attraction/
│       │   ├── claim.md
│       │   ├── toy-model.md       ← the core work
│       │   └── sources.md
│       ├── E7-charge-mass-compensation/
│       ├── Q3-EP-invariant/
│       ├── L1-photon-speed-massive/
│       ├── L2-photon-structure-time-dilation/
│       ├── R-redshift-mechanisms/
│       │   ├── README.md          ← menu
│       │   ├── R1-space-friction.md
│       │   ├── R2-void-decompression.md
│       │   ├── R3-non-central.md
│       │   ├── R4-light-pressure.md
│       │   ├── R5-selection-effect.md
│       │   └── R6-photon-time-dilation.md
│       ├── D1-no-dark-matter/
│       ├── Q2-tetrahedral-shells/
│       └── E3-E4-vdw-gradient-overlap/
├── paper/                         ← NEW: the coherence paper
│   ├── README.md
│   ├── coherence-paper.md         ← master document
│   └── figures/                   ← (we said no diagrams for now, but leaves room)
└── [existing: agents/, simulation/, debates/, chronicle/, outreach/, etc.]
```

*Rationale:* one directory per claim keeps the research granular — each claim can evolve independently, gather its own sources, accumulate its own verification work. The `paper/` subfolder is the composite document that cites from `claims/`.

---

## 7. Multi-session decomposition candidates (for later)

These are *not* tasks for this session. They're candidates for future session briefs when Wisdom is ready to decompose.

| Session | Scope | Dependencies |
|---|---|---|
| A | Write the five 🟢 formal notes under `theory/claims/` | none; can start immediately |
| B | Competing-attraction toy model (E2) | Session A complete; needed to ground unification argument |
| C | Redshift-mechanism deep dive — survey literature on Wiltshire timescape, DESI DR2, tired-light variants; select best candidate | can run in parallel with A |
| D | Density-gradient overlap mechanism (E3, E4) — worked integral for weak-gravity-locally-strong argument | benefits from B |
| E | Tetrahedral shell packing geometry (Q2) — derive `P_n` from first principles | mostly independent |
| F | Parity-violation and Bell stress-test — formal `/debate` round + written response | must precede paper submission to physicists |
| G | Draft the coherence paper — compose from `claims/` subfolder + debates + structural challenges section | depends on A, B, C, F |

**Dependency graph:** A, C, E, D can run in parallel; B depends on A; F can run parallel with A–E; G is the composition target.

Recommended session order when Wisdom has bandwidth: **A first (quick wins, confidence), then C and E in parallel (research depth), then B and D (core unification work), then F (stress test), then G (compose).**

Rough bandwidth estimate: A = 1 session (~4 hrs); B, C, D, E = 1–2 sessions each; F = 1 session; G = 2–3 sessions. Total ~10–15 sessions for a publishable coherence paper. Not trivial, not a lifetime.

---

## 8. What this plan is NOT doing

- **Not proving GCM.** The success criterion is coherence, not correctness.
- **Not replacing standard physics.** GCM positions as alternative interpretation at specific points (redshift, dark matter, force unification), while accepting the empirical bedrock everywhere else.
- **Not claiming quantitative predictions** where the math isn't there. Every prediction gets an honesty tier.
- **Not starting Lean formalization.** Proof targets aren't mature enough. Lean is for later; named in STATUS as aspirational.
- **Not building community practice infrastructure.** That lives in `Spiritual Ethos/` and is a separate track.

---

## 9. The order of attack (immediate)

1. **Write the five 🟢 formal notes.** Each 1–2 pages. Together they are the rigorous spine. (~4 hrs, one session)
2. **Build the `claims/` subfolder** with one-page `claim.md` summaries for each of the top 8 🟡 claims (E2, E3, E4, R2, R5, R6, D1, Q2). (~4 hrs, one session)
3. **Redshift mechanism deep dive.** Pick one commit-to mechanism. Write it up with observational support and known gaps. (~8 hrs, one session with background literature)
4. **Competing-attraction toy model.** The single hardest green-adjacent piece. (~8 hrs)
5. **Draft the coherence paper.** Pull from the above.

This plan is the map. It gets updated as work lands.

---

## 10. What would make this "publishable" for the right audience

Not *Physical Review Letters*. Not yet, maybe not ever. But credible enough to post on arXiv or share with specific physicists (Profumo, Howe) and Anthropic contacts without embarrassment. The markers:

- **Four tenets clearly stated** — done (from `core_tenets.md`)
- **Five green-tier formal pieces rigorously derived** — Session A target
- **Top 8 yellow-tier claims mapped with honest provability status** — Session A+B target
- **One committed cosmological redshift mechanism** with observational comparison — Session C target
- **Competing-attraction toy model** — Session B target
- **Known structural challenges named** (parity, Bell) — paper's honesty section
- **Concrete experiments proposed** — pull from v2 Part V
- **Two or three "this is where GCM makes contact with mainstream heterodoxy" connections** (Profumo's waning WIMP, Wiltshire timescape, DESI DR2) — paper's positioning
- **Acknowledgment of what the theory cannot currently do** — the thing that earns respect

The last point is the asymmetric weapon. Most speculative unification repos don't acknowledge their failures. Ours will.

---

*Updated: 2026-04-23. Living document. Cross-references: [`theory/core_tenets.md`](theory/core_tenets.md), [`theory/versions/gcm_v2.md`](theory/versions/gcm_v2.md), [`debates/2026-04-03-gcm-framework/synthesis.md`](debates/2026-04-03-gcm-framework/synthesis.md), [`../STATUS.md`](../STATUS.md), [`../history/HISTORY.md`](../history/HISTORY.md), [`../knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md`](../knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md).*
