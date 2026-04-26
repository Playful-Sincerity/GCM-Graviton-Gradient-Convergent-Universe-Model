# GCM Coherence Case — Deep Plan

**Filename per skill convention:** `plan-coherence-case.md` (the deep version Wisdom asked for as "plan-deep", with a descriptive slug).
**Generated:** 2026-04-23
**Generator:** `/plan-deep` skill invocation over the GCM repo + the original GDGM LaTeX paper + two parallel research agents (adjacent physics programs, redshift empirical constraints).
**Predecessor:** [`plan.md`](plan.md) — the shallow first-pass plan. This plan supersedes it for execution purposes; the shallow plan remains as a quick-reference surface.
**Mode:** Plan only. No section work or paper drafting executed in this pass.

---

## Environment Health

**Verdict: CLEAN.** Repo was restructured earlier this session (README, STATUS, HISTORY, archive-highlights, LICENSE, umbrella archive-inventory, `GCM/research/sources/catalog.md`, `GCM/chronicle/2026-04-23.md` all landed). No injection patterns detected in CLAUDE.md or rules. Git remote is `WisdomPatienceHappy/GDGM.git` (pre-rename); flagged previously. No blockers.

---

## Assumptions (stated explicitly, correct any)

1. **Target audience is dual:** Anthropic research contacts (Sohil, Wes, Kiel, Hakkei) and Stefano Profumo (UCSC), with the Alembic circle (Erik Davis, Michael Taft, Kathryn Devaney) for the ethos half. Physicists get the coherence case; the Alembic circle reads `Spiritual Ethos/`.
2. **Success is coherence, not proof.** The plan produces artifacts strong enough to engage rigorously, not artifacts that claim truth.
3. **Bandwidth is scarce.** Revenue is Wisdom's #1 priority through April/May 2026. Plan must be honest about what fits in 1-hour, 4-hour, and 8-hour chunks.
4. **No Lean 4 work.** Lean formalization is aspirational through this planning horizon; named as future direction, not commitment.
5. **No diagrams.** Per Wisdom's instruction. Plan lives in prose + tables.
6. **Wisdom's self-assessed math fluency:** not deep. The plan and its downstream artifacts must be legible to him, not only to physicists.

Correct any of these before approving the plan.

---

## Pre-Step Research Findings (grounding)

Two parallel agents produced raw-data files in `research/sources/`:

### [`2026-04-23-adjacent-programs.md`](research/sources/2026-04-23-adjacent-programs.md) — 8 programs surveyed

**The three high-leverage comparisons:**

1. **Wiltshire timescape.** Seifert et al. 2025 (MNRAS Letters 537, L55) found **Bayesian evidence ln B > 5 for timescape over ΛCDM** on the full Pantheon+ sample (1,535 SNe Ia) — very strong statistical support. Timescape eliminates dark energy by attributing apparent acceleration to clock-rate variation between dense walls (slow clocks) and underdense voids (fast clocks, ~35% faster). **GCM's positioning move:** provide the *force-unification explanation for why* timescape's clock-rate structure arises. Timescape phenomenology + GCM mechanism.
2. **Verlinde entropic gravity.** SciPost 2017, ~460 citations. Active community. Shares: gravity-as-substrate, no DM particle. Diverges: entanglement-thermodynamic rather than density-gradient; accepts expansion; accepts massless photon. Legible audience for GCM's claims even if they'd push back on parts.
3. **LQG and causal sets.** Most mature discrete-spacetime toolkits. LQG's 4-simplex structure already anticipates 3D tetrahedral boundary — GCM's tetrahedral-packing claim can borrow formal vocabulary. Shared open problem: the semiclassical limit (neither program has fully recovered smooth GR yet; GCM will face the same challenge).

**Other programs worth naming:**

- **Padmanabhan emergent gravity** (250+ papers) — gravity as thermodynamic; treats cosmological constant as integration constant. Structural sympathy with GCM's "substrate emerges force" claim. Padmanabhan's program specifies neither the substrate atoms nor addresses DM.
- **Profumo PBH-as-DM** — active through 2025. JWST Population-III-star anomalies partly explained by massive PBHs. Asteroid-mass PBH window (~10¹⁷–10²³ g) is least-constrained. **PBHs could be a subset of GCM's "matter whose light doesn't reach us."** Profumo is our outreach target; this connection is strategic.
- **Kaluza-Klein** — geometry-as-unification lineage. LHC-ruled-out large extra dimensions in 2010. Lesson for GCM: every added structure needs a testable signature.
- **Preon models** — 1980s peak; waning after LHC null results. **GCM is structurally a preon program** (gravitons as preons). Inherits preon failure modes: hypercolor confinement, wrong masses. This is a constraint to acknowledge.
- **Tired light** — definitively falsified. DES 2024 (arXiv:2406.05050) at ~200σ against any non-time-dilating model. Measured `(1+z)^1.003 ± 0.005`. **GCM's R6 mechanism must produce (1+z) time dilation, not just redshift.** Getting this wrong falsifies GCM.

### [`2026-04-23-redshift-empirics.md`](research/sources/2026-04-23-redshift-empirics.md) — 7 empirical constraints ranked

| Rank | Constraint | Severity for GCM |
|---|---|---|
| 1 | SNe Ia light-curve time dilation `(1+z)^1.003±0.005` (DES 2024) | **Highest** — R6 must produce this exactly |
| 2 | ISW void-growth tension | **High** — growing voids produce the ISW signal that standard cosmology attributes to DE |
| 3 | BAO 150 Mpc acoustic standard ruler | High — robust early-universe prediction |
| 4 | BBN primordial nucleosynthesis | Medium-high — element abundances need early-universe physics |
| 5 | CMB blackbody preservation | Medium-high — adiabatic cooling is standard; non-expansion needs alternative |
| 6 | Tolman surface brightness | Medium — galaxy-evolution corrections make it debated |
| 7 | DESI DR2 (2025) weakening DE | Low — supports GCM's no-DE, doesn't prove it |

**Photon mass bound from FRB dispersion (Wang et al. 2023, JCAP):** `m_γ ≤ 2.1 × 10⁻¹⁵ eV/c²`. GCM's ~`10⁻⁵⁴ kg` ≈ `5.6 × 10⁻¹⁹ eV/c²` — **28 orders below the bound. Not ruled out. Safe.**

---

## Cross-Cutting Concerns (Step 0)

These decisions span every section. Lock them in before decomposition; parallel section-planning will make conflicting assumptions otherwise.

### CC-1. Core ontology (what IS a graviton?)

Three possible formal commitments, each with different downstream math:

| Option | Description | Upside | Downside |
|---|---|---|---|
| **A — Classical point particle** | Dimensionless point with scalar mass in 3+1D Minkowski | Simplest; matches the paper | Immediately faces the parity-violation wall (scalar field, no pseudovector structure) |
| **B — Discrete spacetime excitation** | Node of a tetrahedral lattice; "particle" is a stable density cluster on the lattice | Natural home for shell-packing quantization (Q2); parallels LQG 4-simplex | Must specify lattice dynamics; parity problem still live |
| **C — Field-theoretic with internal state** | Graviton carries small internal state (spin-like, chirality-like) | Opens path to parity violation | Adds structure; violates T1's "dimensionless point" reading |

**Recommendation:** Commit to **A for the coherence paper**, flag **C as future direction** when parity is confronted. B is middle ground, formally appealing but adds cost. Wisdom should pick — this choice propagates.

### CC-2. Epistemic tier system

Every claim in the program gets one tag:

- 🟢 **Green** — verifiable now with existing math; standalone derivable in 1–3 pages.
- 🟡 **Yellow** — 1–3 weeks of derivation + literature survey gets us to a credible "this is how it would have to work" treatment.
- 🔴 **Red** — structural gap, needs new formalism or confronts a hard empirical/theoretical objection.

**Tiers are not promises of correctness.** Green means "we can write rigorously about it"; yellow means "we can make a plausibility argument"; red means "we name it as an open challenge."

### CC-3. Formalism commitments

The coherence paper uses:

- **Math:** standard calculus, dimensional analysis, elementary Bohr QM. No Lagrangian/path-integral formulation (insufficient maturity). No Lean 4 (aspirational only).
- **Notation:** SI units throughout. Use the v2 document's symbol table (`GCM/theory/versions/gcm_v2.md` Appendix) as canonical.
- **Claim codes:** M1, E2, R2, Q3, etc. — preserved from the shallow plan. Sections map to code prefixes.
- **Citations:** peer-reviewed physics literature for adjacent comparisons (Verlinde, Wiltshire, Profumo, DES, Wang); internal citations to `GCM/theory/`, `GCM/research/sources/`.

### CC-4. Honesty standards (non-negotiable, inherited from STATUS.md)

- No Lean 4 overclaim. The LinkedIn line stays flagged until Wisdom updates it.
- Every yellow claim carries a "what would make this green" note.
- Every red claim explicitly names the objection and its severity.
- The N-body cluster-formation simulation has not been reported to completion; until it is, it is a *promised* test, not a *passed* one.
- Labels "Four Remembrances," "Anchor Line," "consonance not deduction" are Claude-era (April 2026) consolidations of 2–4-year-old content. This provenance note appears wherever these labels are used outside the family of artifacts.

### CC-5. "Coherence passes" criterion

The program's equivalent of a test suite. The coherence case passes if all of these hold in the final paper:

1. Four tenets stated cleanly and internally consistent.
2. At least five green-tier formal pieces derived rigorously.
3. At least one cosmological redshift mechanism committed to, with empirical constraints addressed (including the `(1+z)^1.003` time-dilation constraint).
4. At least one unification claim argued concretely (competing attraction for electron repulsion is the candidate).
5. Known structural challenges named explicitly (parity violation, Bell, ISW tension, semiclassical limit).
6. At least three positioning paragraphs comparing GCM to peer-reviewed programs (Wiltshire, Verlinde, Padmanabhan or Profumo).
7. No overclaim anywhere. Honesty markers preserved.

Each of these becomes a check against the final paper draft.

### CC-5. The Axiom of Indivisibility (Wisdom's 2026-04-23 formalization)

**Axiom (formal statement).** A truly fundamental, indivisible particle has no internal variability. All of its qualities — save its identity as a participant in the one fundamental interaction — must emerge from its relationships to other fundamental particles. The graviton therefore has only position and its identity as a gravitating point; it cannot possess intrinsic spin, chirality, charge, or internal state. Apparent non-gravitational properties of composite particles (electrons, photons, protons) arise entirely from structural relationships among their constituent gravitons.

**Philosophical ground.** An "indivisible" particle with internal structure is a contradiction: the "internal" implies divisibility. Therefore the only coherent reading of "fundamental indivisible particle" is one with no intrinsic variability. Wisdom (2026-04-23): *"That's just pure logic. That's the only way you can actually have an indivisible thing in the first place."*

**Immediate consequence — CC-1 hardens from A-with-C-flagged to A-only.** Option C (graviton with internal state) is *ruled out* by the Axiom, not merely deferred. The escape hatch for parity violation that C would have provided is closed. Parity violation must be addressed *configurationally* — handedness emerging from graviton arrangement — not by adding graviton-intrinsic structure.

**Consequence for S8 (Structural Challenges).** The parity-violation problem becomes harder, not easier. The path is: show that certain graviton configurations produce emergent chirality, and that weak interactions are interactions that select chiral configurations. This is a configurational-emergence argument, not a trivial one. It's the price of philosophical cleanliness.

### CC-5.5. Realism and Locality — the Local-Realist Path via Superdeterminism

GCM commits to **realism**: actual graviton density distributions, not probability amplitudes. T4 is read strongly — what we call "probability distributions" in standard QM are, in GCM's framing, real distributions of graviton structure whose measurement-apparent stochasticity reflects our ignorance of microstate, not fundamental indeterminism. Wave-particle duality is real gradient structure, not Copenhagen superposition.

**GCM also commits to locality.** Wisdom (2026-04-23): *"Local realism. Not non-local."* This is a strong commitment — naïve local realism (local hidden variables) is experimentally ruled out by Bell-inequality violations. GCM must therefore take the one path that preserves both locality and realism: **superdeterminism**.

**The superdeterministic reading.** Bell's theorem rules out local hidden variables *under the assumption of measurement independence* — that an experimenter's choice of measurement settings is uncorrelated with the particles' hidden variables. Superdeterminism denies this assumption: in a fully deterministic universe, measurement choices and particle states are both consequences of the same initial conditions, so their correlations are a matter of common history, not nonlocal connection.

**Why this fits GCM naturally.** GCM's minimal model is purely deterministic. Given all graviton positions and velocities at some time t=0, all future states are fixed. Bell-violating correlations in quantum experiments are explained as common-history correlations in this fully deterministic flow — not as FTL signals, not as fundamental randomness.

**Nearest-neighbor precedent.** Gerard 't Hooft's *Cellular Automaton Interpretation of Quantum Mechanics* (2016, Nobel laureate) is the most developed superdeterministic-realist program. Sabine Hossenfelder has also defended superdeterminism publicly (2020+). This is a minority view in foundations of physics, but not a crackpot one.

**For the paper's audience.** When the paper claims "local realism," it MUST immediately qualify: *"real, local, deterministic, with measurement-independence denied (superdeterministic reading, following 't Hooft)."* Physicists encountering "local realism" as a standalone phrase will dismiss on Bell grounds within seconds. The qualification is load-bearing — not a technicality, but the difference between a defensible position and an immediately-dismissible one.

**What superdeterminism costs.** It denies "free will" in the measurement-setting sense, which is philosophically uncomfortable for many readers. GCM's response: in a universe-is-converging, we-are-the-universe framing, "free will" is anyway a local illusion overlaid on a deeper deterministic flow. The ethos already commits to this at the spiritual level ("nothing needs to happen — the universe converges regardless"). The physics and ethos are consonant here.

### CC-6. Balance across physics domains (Wisdom's 2026-04-23 addendum)

The coherence paper must touch, at minimum, these physics domains with real content:

- **Particle physics** — graviton as constituent; one-particle ontology; charge and mass from density structure. (S3, S4)
- **Cosmology** — convergence, redshift, dark matter/energy reframes. (S6)
- **Quantum mechanics** — tetrahedral shells, discrete charge, wave-particle as real distribution, realism + nonlocality. (S4, CC-5.5)
- **Thermodynamics** — release theory of heat; black body as graviton-release equilibrium; equipartition recovery. (S7 — currently thin; expand)
- **Classical physics & relativity** — Newtonian gravity as limit; Lorentz force reproduction (UNSPEC-4); Lorentz invariance emergence (OQ-3); SR as natural consequence of graviton density wave alignment (per `1物理25` 21/5/25 note). (S8 + new S5.5)
- **Quantum field theory** (aspirational) — how does the standard model emerge in a limit? (Red-tier; S8)

**Action on S7 (Thermodynamics).** Expand from conceptual-only to yellow-tier: pull the release-theory claim into an honest sketch showing (a) release of excess graviton density on a toroidal cycle, (b) directional divergence principle rather than random diffusion, (c) approach to blackbody as graviton-release equilibrium. Compare to Verlinde's entropic framework (shared substrate-thermodynamic lineage).

**New sub-section S5.5 — Classical & Relativistic Limits.** Short treatment of:
- How Newtonian gravity emerges in the low-density, large-distance limit of the minimal-model equation.
- Special relativity as consequence of graviton-density-wave propagation (per `1物理25`).
- Why Lorentz invariance is compatible with (not derived from) GCM at present — and where future work would need to go to derive it.

**Status update — Session F completed 2026-04-23.**
- **H2 (Release Theory of Heat)** upgraded from conceptual to yellow-tier. Outputs at [`theory/claims/H2-release-heat/`](theory/claims/H2-release-heat/): claim.md, derivation.md, verification.md, caveats.md. Three green passes (directionality of heat flow, Newton's cooling ODE functional form, Fourier heat equation structure); two open red-tier gaps explicitly flagged (equipartition, Planck's law — UNSPEC-5). Comparison to Verlinde's entropic framework included.
- **H1 (Toroidal Magnetism)** stated as yellow sketch with UNSPEC-4 (exact Lorentz force reproduction) flagged as out of scope. Outputs at [`theory/claims/H1-toroidal-magnetism/`](theory/claims/H1-toroidal-magnetism/): claim.md, derivation.md, verification.md, caveats.md. Geometric consistency (radial flow + linear drift → toroidal streamlines), right-hand rule emergence, and absence of monopoles all pass qualitatively; quantitative reproduction of Maxwell/Lorentz is honestly deferred.
- **S5.5 (Classical and Relativistic Limits)** produced with three sub-claims. Outputs at [`theory/claims/S5_5-classical-limits/`](theory/claims/S5_5-classical-limits/):
  - **(a) Newtonian limit — 🟢 Green.** Hand derivation of $F = Gm_1m_2/r^2$ from the minimal-model equation in the large-separation, many-graviton limit. 4/4 verification checks pass (dimensional, Earth-Moon numerical substitution $\sim 1.98 \times 10^{20}$ N, limit cases, Wolfram Alpha cross-check).
  - **(b) Special relativity — 🟡 Yellow.** Consistency argument via Robertson (1949): substrate with universal signal speed $c$ produces Lorentz transformations. OQ-3 (derive $c$ from graviton dynamics) named as the remaining gap.
  - **(c) Local realism via superdeterminism — 🟡 Yellow framing.** Clean for physicist audience. Cross-references CC-5.5. Required phrasing given: "local realism" must always appear with the qualifier "deterministic, with measurement-independence denied, following 't Hooft (2016)" — never as a bare term.

### CC-6. Scope boundary

Three distinct targets, one plan:

- **Coherence case** (this plan's target) — a posting-worthy document demonstrating the research program is non-trivial. ~12–20 pages.
- **Quantitative theory** (distant) — a version that actually reproduces numerical predictions (Coulomb from graviton dynamics, SNe Ia light curves from R6, rotation curves from gradient effects). Not this plan's target.
- **Published physics paper** (further) — peer-reviewed venue submission. Not this plan's target.

Conflating these inflates scope and generates false stakes. The plan below targets only the coherence case.

### CC-7. Testing convention (for derivations) — the IVNA Methodology

Follows the pattern that validated IVNA at 489 checks, 0 failures (see `feedback_ivna_system_lessons.md`). **Every numerical claim gets verified by multiple independent methods, AND the verification methods themselves get cross-checked.** This is load-bearing per Wisdom's 2026-04-23 instruction: *"if we ever make a claim make sure things work... verify our verification methods as well."*

**Per-claim verification stack (in order of application):**

1. **Dimensional analysis** — every formula checked for unit consistency by hand.
2. **Numerical substitution** — arithmetic results checked with physical constants, by hand.
3. **Wolfram Alpha / WolframCloud computation** — same calculation performed independently via the `wolfram-alpha-llm` MCP (if available) or via web query. Result compared to hand calculation.
4. **Python / SymPy** — for derivations involving calculus or algebraic manipulation, independently verify with SymPy. Result compared to hand derivation.
5. **Consistency with published bounds** — compare against LIGO (graviton mass), FRB dispersion (photon mass), DES 2024 (SNe Ia time dilation), Seifert 2025 (timescape), etc.
6. **Limit cases** — where a formula reduces to classical physics in a known limit, verify the reduction happens correctly.

**Cross-verification of verification methods:** if two verification tools agree with each other but disagree with the hand calculation, the hand calculation is likely wrong. If two tools disagree, resolve before proceeding — the disagreement is the signal.

**Tally pattern (per IVNA):** track verification tallies per claim — `M1: 5/5 checks passed`, etc. If any check fails, the claim is not green-tier. A claim with `3/5 checks passed` is yellow-tier with "verification incomplete" as the honesty note.

**Tools to use** (from the repo's connected MCP surface):
- Wolfram Alpha or WolframCloud (for arithmetic and unit-consistency checks)
- Python3 + SymPy (for symbolic derivations)
- WebSearch / WebFetch (for bound-checking against published papers)
- Dimensional-analysis by-hand (always — this is the foundation)

**What this is NOT:** the N-body simulation's smoke-test suite. That validates Python scaffold, not theory claims. The IVNA methodology validates the *claims*, not the implementation.

**Verification record lives at:** `theory/claims/<code>/verification.md` per claim. Format: each check named, its result, its tool, its date. Gives a clear per-claim audit trail.

---

## Meta-Plan (Step 1)

### Goal

Produce a **coherence case** for GCM strong enough that a serious physicist (Profumo, Kiel Howe) or Anthropic researcher (Sohil, Wes) can engage with the work rigorously rather than dismiss it. The case does not claim truth; it claims non-trivial internal consistency, reasoned positioning against peer-reviewed alternatives, and honest acknowledgment of structural challenges. The final artifact is a 12–20 page document plus a `claims/` sub-directory supporting each claim with its own rigorously-derived 1–3 page note.

### Sections (10)

**S1 — Ontological Foundations**
Tenets T1–T4 cleanly stated; CC-1 commitment made (graviton as classical point, with flag to future structure); vacuum graviton density ρ₀ named explicitly as open question OQ-4; max density bound T3 softened from "exactly neutron density" to "roughly nuclear scale."
*Complexity: S* | *Risk: Low — largely editorial over existing tenets.* | *Acceptance:* T1–T4 restated; CC-1 resolved; `ρ₀` and max-density-bound uncertainty named honestly.

**S2 — Verifiable Math Spine**
Five green-tier formal pieces. Each 1–3 pages with starting point, derivation, verification, caveats.
*Complexity: M* | *Risk: Low (math is solid) to Medium (framing must be careful).* | *Acceptance:* Five notes land in `theory/claims/` subfolders; each passes CC-7 checks; each has explicit "what this does and doesn't prove."

**S3 — Unification Mechanics**
The central claim: all forces emerge from graviton density gradients. Treatment of competing attraction (E2), density-gradient overlap for local-strength (E4), Van der Waals as universal attraction (E3), and charge-flow asymmetry (E1).
*Complexity: L* | *Risk: High — downgraded after Session C (see "Session C Results" subsection below). The E2 toy model produces sign-correct apparent repulsion but is $\sim 10^{40}$ too weak quantitatively; E4's "amplification" reading fails; E3's "direct overlap → $1/r^6$" fails. Structural gap named honestly; unification case is yellow-tier structural compatibility, not green-tier derivation.* | *Acceptance (revised 2026-04-23):* E2 toy model demonstrates sign-correct apparent repulsion in asymmetric geometry (✅); magnitude flagged as requiring unspecified short-range amplification (❌, honestly named); E4 overlap integral computed exactly, amplification reading falsified but regularization finding is a positive side-result (✅+); E3 preserved as framing co-optation with rigorous-derivation flagged as future work; E1 stated as yellow-tier hypothesis with flow equation. **All four claim folders complete (claim + derivation + verification + caveats).**

**S4 — Quantum Structure**
Tetrahedral shell packing `P_n = 10n² + 2` derived from first principles (FCC geometry); the `E_n · P_n ≈ 136–163 eV` invariant computed and discussed; discrete-charge claim Q6 connected to shell stability; wave-particle as gradient named as conceptual-only.
*Complexity: M* | *Risk: Medium — the `E·P` invariant is numerically real, but the "this is why hydrogen quantizes" claim is aspirational and must be framed as observation not derivation.* | *Acceptance:* FCC shell derivation done; E·P table and asymptote discussion clean; Q6 linked to shell stability without overclaiming.

**S5 — Light and Photon Physics**
Photon massive-photon speed formula (L2); `~10⁻⁵⁴ kg` rest mass consistent with FRB dispersion bound `≤ 2.1 × 10⁻¹⁵ eV/c²`; wavelength ∝ graviton-cluster spacing (L3); photon-structure time dilation R6 as the GCM answer to the SNe Ia time-dilation test.
*Complexity: M* | *Risk: Medium-High — R6 must argue it produces `(1+z)^1.003 ± 0.005` time dilation, not just redshift. This is the single constraint that can falsify GCM's cosmology.* | *Acceptance:* L2 and L3 derived; R6 argued at structural level with explicit tie to `(1+z)` dependence; consistency with Wang 2023 photon-mass bound shown.

**S6 — Cosmological Redshift and Dark Matter**
Commit to one or two of the six R mechanisms; formalize R6 time-dilation companion; address the ISW tension head-on; position GCM alongside Wiltshire timescape as complementary (GCM provides force-unification substrate for timescape phenomenology); treat D1 (no DM particle) via connection to Profumo PBH program; address BAO, CMB, Tolman empirical constraints honestly.
*Complexity: L* | *Risk: Very High — this is the section most likely to be dismissed by physicists. ISW tension and (1+z) time-dilation are both real and both must be addressed.* | *Acceptance:* One primary R mechanism chosen with commitment; R6 paired as time-dilation companion; ISW tension named and partial resolution attempted; D1 positioned against PBH program; all seven empirical constraints from the redshift-empirics research addressed (even if the address is "this remains open").

**S7 — Magnetism and Thermodynamics**
Toroidal alignment (H1); release theory of heat (H2); ferromagnetism (H3); black body (H4); equipartition (H5). These are the thinnest-grounded claims and will be treated as conceptual with honest provability notes.
*Complexity: M* | *Risk: Medium — low math density but high "claim surface area" to be honest about.* | *Acceptance:* Each claim stated, plausibility argued, "what would make this green" noted; no false derivations.

**S7 status — Session F completed 2026-04-23.** Two load-bearing claims upgraded from conceptual to yellow:
- **H2 (release theory of heat)** — yellow-tier sketch lives at [`theory/claims/H2-release-heat/`](theory/claims/H2-release-heat/). Verification tally: 3/6 green passes (directional heat flow, Newton's cooling, Fourier heat equation), 1/6 qualitative analogy (blackbody spectrum), 2/6 red-tier open gaps (equipartition, Planck's law — UNSPEC-5). Verlinde comparison included.
- **H1 (toroidal magnetism)** — yellow sketch lives at [`theory/claims/H1-toroidal-magnetism/`](theory/claims/H1-toroidal-magnetism/). Verification tally: 4/6 qualitative passes (toroidal geometry from superposition, right-hand rule emergence, dimensional consistency, monopole absence), 2/6 open gaps (Lorentz force reproduction, Maxwell's equations — both UNSPEC-4). UNSPEC-4 remains out of scope for the coherence paper; treated in S8.

H3 (ferromagnetism), H4 (black body as graviton-release equilibrium), H5 (equipartition as release statistics) remain conceptual-only for now. H3 and H4 plausibility is absorbed into H1's and H2's sketches respectively; H5 is explicitly an open problem (UNSPEC-5). A future session can elevate any of these individually if needed.

**S7 paper length target (updated).** Originally 500 words. With H1 and H2 now yellow-tier, a 700-900 word range is more realistic — enough to present both claims' plausibility arguments plus the Verlinde comparison plus the UNSPEC-4/5 flags, without inflating conceptual material into derivations. If length pressure forces compression, H1 can go to a single paragraph and H2 can keep its multi-paragraph treatment (H2 is the more load-bearing of the two).

**S8 — Structural Challenges (the honesty section)**
The single most credibility-earning section. Named structural challenges:
- **Parity violation** — scalar-graviton-cannot-encode-handedness. Current ontology's wall; CC-1 Option C (internal state) is the future direction.
- **Bell's theorem** — navigable via nonlocal realism (Bohmian), not via local hidden variables.
- **Lorentz force reproduction** — UNSPEC-4 from v2; must be numerical, not analogical.
- **ISW void-growth tension** — the redshift mechanism implies growing voids which produce the ISW signal the standard model attributes to dark energy. GCM must either commit to static voids (losing R2) or accept the ISW signal and explain it mechanistically.
- **Semiclassical GR limit** — how does GCM recover smooth-spacetime GR in limits where we know it works (gravitational wave propagation, perihelion precession)? LQG has this problem; GCM inherits it.
- **Preon failure modes** — if GCM is a preon program, it inherits hypercolor-confinement and wrong-mass objections.

*Complexity: M* | *Risk: Paradoxically low — naming these openly is what earns physicist respect.* | *Acceptance:* Each challenge stated, its severity ranked, and the direction future work would take.

**S9 — Literature Positioning**
Three positioning paragraphs: GCM vs. Wiltshire timescape (complementary — GCM provides mechanism for timescape phenomenology), GCM vs. Verlinde entropic gravity (both treat gravity as substrate but via different formalisms), GCM vs. PBH dark matter (PBHs could be a subset of "matter whose light doesn't reach us"). Also name the Kaluza-Klein lesson and the preon ancestry.
*Complexity: S* | *Risk: Low.* | *Acceptance:* Three positioning paragraphs land; Seifert 2025, Verlinde 2017, Profumo 2025 papers cited accurately.

**S10 — Coherence Paper Architecture**
Document structure for the final paper: which claims go in the main body (the green pieces and the strongest yellow ones), which go in appendices, section order, length targets per section. Not the paper itself — the *architecture* of the paper.
*Complexity: S* | *Risk: Low — bookkeeping.* | *Acceptance:* A specific 12–20 page layout with word targets per section; ordered reading path named; what-to-cut-if-time-pressured noted.

### Acceptance Tests (meta-level)

End-to-end checks that verify the coherence case as a whole:

- **Cold-read test.** Give the final document to someone who has never seen GCM. Do they understand what's being claimed, at what epistemic level, by the end of the first two pages? (If no, S1 needs revision.)
- **Adversary test.** Give the final document to a skeptical physicist. Do they have anything to engage with beyond "this is wrong"? (If no, S3 and S6 are insufficient.)
- **Provenance test.** Can every numerical claim in the paper be traced through `claims/` subfolders to the primary derivation? (If no, CC-7 wasn't satisfied.)
- **Honesty test.** Is every red-tier claim labeled as such? Is the Lean-4 non-existence stated? Are the structural challenges S8 visible in the main body, not buried? (If no, CC-4 wasn't satisfied.)

### Dependency Graph

```
S1 (Ontology) ──┬──> S2 (Math Spine) ──┐
                ├──> S3 (Unification) ──┤
                ├──> S4 (Quantum) ──────┤
                ├──> S5 (Light) ────────┤
                └──> S7 (Mag/Thermo) ───┤
                                        ├──> S10 (Architecture) ──> Coherence Paper draft
S5 ──> S6 (Redshift/DM) ────────────────┤
                                        │
S3 ──> S8 (Structural Challenges) ──────┤
S6 ──> S8 (adds ISW tension)            │
                                        │
All of S1–S8 ──> S9 (Literature Positioning)
```

- S1 is the foundation. Nothing else plans until S1's CC-1 choice is made.
- S2, S3, S4, S5, S7 can proceed in parallel once S1 is done.
- S6 depends on S5 (the R6 mechanism).
- S8 depends on S3 (unification's parity wall) and S6 (ISW tension).
- S9 reads everything else.
- S10 is the final composition step.

### Parallel vs. Series Map

```
SERIES (foundation)
═══════════════════════════════════════
  S1

PARALLEL (after S1)
═══════════════════════════════════════
  S2    S3    S4    S5    S7

SERIES (depends on S5)
═══════════════════════════════════════
  S6

PARALLEL (after S3 and S6)
═══════════════════════════════════════
  S8    S9

SERIES (composition)
═══════════════════════════════════════
  S10 ──> Coherence paper draft
```

| Session | Sections | Prerequisites | Can Start | Estimated Bandwidth |
|---|---|---|---|---|
| **A — Foundations & CC-1** | S1 + cross-cutting lock-in | None | Immediately | 2 hrs |
| **B — Math Spine** | S2 (five green notes) | A | After A | 4 hrs (one sitting) |
| **C — Unification** | S3 (including E2 toy model) | A | **DONE 2026-04-23** | 8 hrs executed |
| **D — Quantum Structure** | S4 | A | After A | 4 hrs |
| **E — Light Physics** | S5 | A | After A | 3 hrs |
| **F — Mag/Thermo** | S7 | A | After A | 2 hrs (short because conceptual-only) |
| **G — Redshift & DM** | S6 | E | After E | 8 hrs (reading-heavy) |
| **H — Structural Challenges** | S8 | C, G | After C and G | 3 hrs |
| **I — Literature Positioning** | S9 | All above | After H | 2 hrs |
| **J — Paper Architecture + Composition** | S10 + write paper | All above | After I | 8–12 hrs |

**Total bandwidth estimate:** ~46–50 hours of focused work to reach a posting-worthy coherence case. If done at ~4 hrs/session, that's 11–13 sessions. Realistic for ~1 month at 2–3 sessions/week.

**Critical path:** A → C → H → I → J. C (unification) and G (redshift) are both hard; either could extend.

---

## Section Plans (Step 2 — draft form)

Each section gets a mini-plan below. These are drafts in the master document — if a section proves to need a dedicated planning pass, a plan-section-[name].md file spawns from that session's work.

### S1 — Ontological Foundations

**Session A complete (2026-04-23).** Outputs: `GCM/theory/claims/S1-foundations/claim.md`, `rationale.md`, `indivisibility-axiom.md`, `indivisibility-formal.md`, `realism-locality.md`. Key decisions locked: (1) CC-1 hardened to A-only — Option C ruled out by Axiom of Indivisibility, not deferred; (2) T3 softened to "roughly nuclear scale, specific value provisional (OQ-2)"; (3) local realism via superdeterminism adopted (following 't Hooft 2016), superseding the Bohmian-nonlocal-realism path identified in the 2026-04-03 debate synthesis; (4) epistemic posture front-loaded in claim.md per CC-4 honesty standards. Sessions B–J unblocked.

**Objective.** Produce a clean 1–2 page foundational statement of what GCM IS: tenets, ontological commitments, epistemic posture. This replaces no existing file; it becomes the opening of the coherence paper.

**Key decisions to make inside S1:**
- **CC-1 commitment:** A, B, or C. Recommended A with C flagged as future direction.
- **T3 softening:** restate as "maximum density at roughly nuclear scale" with ρ₀ (vacuum density) and ρ_max both named as open.
- **T4 restatement:** make "dimensions of change" precise — space is graviton distance, time is the process of those distances changing, matter is density, energy is rate of change.

**Reference material:** `theory/core_tenets.md` (existing), `theory/overview.md`, `theory/versions/gcm_v2.md` Part I.

**Acceptance:** Section opens the paper. Someone unfamiliar with GCM can read this alone and know what the program claims at the level of tenets without encountering overclaim.

**Breaks if:** CC-1 commitment is never made — every downstream section makes independent assumptions.

---

### S2 — Verifiable Math Spine (five green pieces)

> **Session B complete (2026-04-23).** All five notes drafted at `theory/claims/{M1-graviton-mass, E7-charge-mass-compensation, Q3-EP-invariant, L2-photon-speed, M3-planck-cell-count}/` with `claim.md`, `derivation.md`, `verification.md`, `caveats.md` each.
>
> **Per-claim verification tally:**
> - **M1 (graviton mass):** 4/5 checks passed. Check 5 (Planck-density limit should stay LIGO-consistent) fails — but the failure is expected on physical grounds: the formula $\rho \cdot \ell_P^3$ at Planck density necessarily yields the Planck mass, which GCM never claims. The LIGO bound converts into a constraint on $\rho_\text{bound}$ ($\lesssim 4 \times 10^{45}$ kg/m³), which nuclear density satisfies by 27 orders of magnitude. **Recommend: retain green tier with caveat, or downgrade to yellow by strict reading of CC-5 — Wisdom's call.**
> - **E7 (charge-mass compensation):** 5/5 checks passed. **Green confirmed.**
> - **Q3 (E·P invariant):** 5/5 checks passed. **Green confirmed.**
> - **L2 (photon speed):** 5/5 checks passed. **Green confirmed.** Floating-point note: direct double-precision evaluation of $v = c\sqrt{1 - \varepsilon^2}$ returns $v = c$ identically because $\varepsilon^2 \sim 10^{-37}$ is below machine epsilon; Taylor expansion recovers the correct $\Delta v \approx 4.72 \times 10^{-29}$ m/s (0.4% below the brief's stated $4.74 \times 10^{-29}$).
> - **M3 (Planck-cell count):** 4/4 checks passed (brief specified only 4 checks). **Green confirmed.**
>
> **Honesty flags surfaced:**
> - M1 check 5 is a framing fail, not a physics fail. The claim is solid at nuclear-scale density.
> - Wolfram Alpha verification was not run in this session (only Python). Cross-tool redundancy check is flagged as TODO for all five claims.
> - SymPy was not installable in this environment; E7's symbolic derivation was done by hand with finite-difference numerical confirmation instead. Equivalent in content, different tool.
>
> **Downstream impact:** S2 is complete as a math spine. S3 (Unification) can proceed. The load-bearing claims for the coherence paper are five independently-derived, independently-verified results.

**Objective.** Five short formal notes, each standalone and independently verifiable. Together they are the paper's math backbone. Each lives at `theory/claims/<code>/` with `claim.md`, `derivation.md`, `verification.md`, `caveats.md`.

**The five:**

**M1 — Graviton mass from Planck scale and density bound.**
- Derivation: `m_g = ρ_bound · ℓ_P³ = ρ_bound · (ℏG/c³)^(3/2)`
- Numerical (using ρ_neutron ≈ 10¹⁸ kg/m³): `m_g ≈ 4.22 × 10⁻⁸⁷ kg`
- N_g ≈ 4 × 10⁵⁹ gravitons per neutron (arithmetic consequence)
- Verification: check dimensions (kg); compare against LIGO bound `m_g < 1.78 × 10⁻⁵⁹ kg` (GCM's value is 28 orders below — passes)
- Caveat: the `ρ_bound = ρ_neutron` choice is provisional (OQ-2). The *structural* claim `m_g ~ ρ_bound · ℓ_P³` is load-bearing; the specific value scales linearly with the bound.

**E7 — Charge-mass compensation constraint.**
- Starting point: Bohr ground state `E₁ = −m_e k² e⁴ / (2ℏ²)`
- Derivation: `∂E₁/∂e · Δe + ∂E₁/∂m_e · Δm_e = 0` yields `Δm_e/m_e = −4 · Δe/e`
- Verification: partial derivatives and algebra independently reproducible
- **Framing (critical):** this is a *consistency constraint* on emergent-charge-and-mass theories, not a prediction of fluctuations. Any unified theory treating e and m_e as co-emergent must satisfy this ratio to preserve hydrogen spectroscopy (measured to parts-per-billion).
- Caveats: non-relativistic Bohr only; QED corrections dominate at precision where Δe ~ 10⁻³⁵ C matters; e and m_e aren't cleanly separable in full QFT.

**Q3 — `E_n · P_n ≈ constant` approximate invariant.**
- Tabulation:

| n | P_n = 10n² + 2 | E_n = −13.6/n² (eV) | E_n · P_n (eV) |
|---|---|---|---|
| 1 | 12 | 13.600 | 163.2 |
| 2 | 42 | 3.400 | 142.8 |
| 3 | 92 | 1.511 | 139.0 |
| 4 | 162 | 0.850 | 137.7 |
| 5 | 252 | 0.544 | 137.1 |

- Variation ~20% across n=1–5; clear asymptote at ~136 eV = 10 × 13.6 eV (the Rydberg constant).
- Verification: independently computable.
- Framing: this is an observed numerical near-invariance, not a derivation of hydrogen quantization from shell packing. The direction "shell packing *produces* `1/n²` scaling" is Q6 — aspirational.

**L2 — Photon speed from rest mass.**
- Standard energy-momentum: `v = c · √(1 − (m₀c²/E)²)`
- Worked example for `m₀ = 10⁻⁵⁴ kg`, `E = 1 eV`: `Δv ≈ 4.74 × 10⁻²⁹ m/s`
- Verification: standard relativity algebra.
- Cross-check against Wang et al. 2023 FRB dispersion bound: `m_γ ≤ 2.1 × 10⁻¹⁵ eV/c²`. GCM's claimed mass ~`5.6 × 10⁻¹⁹ eV/c²` is 4 orders below the bound. Safe.
- Framing: this shows what a small photon mass would produce, not that the photon has it.

**M3 — Universe Planck-cell count.**
- Observable universe sphere `R_H ≈ 4.4 × 10²⁶ m`; Planck volume `V_P = ℓ_P³`.
- `N = (4/3)π R_H³ / V_P ≈ 8.5 × 10¹⁸⁴ ≈ 10¹⁸⁵`
- Dimensional estimate. Framing: "if space is Planck-quantized and uniformly packed, this is the graviton count."

**Acceptance:** five notes land; all pass CC-7 verification; each explicitly states what it proves and what it doesn't.

**Breaks if:** any derivation is presented as proof of GCM rather than as a consistent mathematical object compatible with GCM.

---

### S3 — Unification Mechanics (the load-bearer)

**Objective.** The central coherence claim: all forces emerge from graviton density gradients. S3 is THE section a physicist will attack hardest.

**Sub-sections:**

**E2 — Competing attraction for electron "repulsion."**
- Need: a worked two-body toy model showing that two electrons in a background of protons experience net *repulsion* from competing attraction (each electron being more strongly pulled toward distant protons than toward the other).
- Format: explicit force integral over a distribution of background protons; show net inter-electron force has the correct sign and (approximately) the correct magnitude scaling.
- Difficulty: significant. This is the claim that determines whether "all forces are gravity" is rescue-able or dismissible. If the toy model doesn't produce recognizable repulsion, S3 fails and the coherence case weakens.
- Comparable existing work: none that we know of. This is novel mathematical territory for GCM.
- Yellow tier (aspirational); promote to green only if toy model produces the right scaling.

**E3 — Van der Waals as universal attraction.**
- Observation: VdW is already a universal weak attraction between all particles. GCM doesn't add something new here — it *co-opts* an existing accepted mechanism.
- Framing move: standard VdW arises from correlated dipole fluctuations with `1/r⁶` dependence. GCM claim: the correlations arise from graviton-density-gradient fluctuations, and the `1/r⁶` dependence follows from gradient-overlap geometry. Same end state, different grounding.
- Required: sketch that gradient-overlap reproduces `1/r⁶` (or shows why it doesn't).

**E4 — Density-gradient overlap for "strong enough" local gravity.**
- Argument: particles aren't points; they are extended density distributions. When two particles are close, their density gradients overlap. The effective gravitational interaction is over this overlap volume, not the particle-center distance.
- Required: worked integral showing that for two overlapping density distributions at small separation, the effective interaction strength is much larger than the center-to-center `1/r²` estimate would suggest. This is how GCM accounts for the scale hierarchy problem (EM vs. gravity ratio ≈ 10³⁶).
- Honest note: reproducing the exact 10³⁶ ratio requires specific density-distribution forms; we can show order-of-magnitude but not precision.

**E1 — Charge as graviton flow asymmetry.**
- State as a hypothesis (yellow). Electrons: `∇·J_g > 0` (net outflow). Protons: `∇·J_g < 0` (net inflow). Neutrons: `∇·J_g = 0` (balanced).
- Required: at minimum, a flow equation `J_g = −D∇ρ_g + v_g · ρ_g` and a note that UNSPEC-1 (why electron configurations produce outflow) remains open.

**Acceptance:** E2 toy model produces recognizable repulsion or is honestly labeled as open; E3 and E4 scale arguments land; E1 is stated as hypothesis with flow equation.

**Breaks if:** the competing-attraction toy model cannot be built at any level (even qualitative). This is the single biggest unknown in the whole program's formal viability.

**Suggestion:** run `/debate` on E2 before committing to the section. If a skeptic can't find a fatal flaw in the toy-model direction, proceed; if they can, revise.

---

#### Session C Results (2026-04-23) — executed end-to-end

Session C (8 hours planned) was executed. All four claim folders produced in full (claim + derivation + verification + caveats). Headline result: **E2 qualitatively succeeds (sign) but quantitatively fails (magnitude) by ~$10^{40}$; E4's "amplification" reading fails directly; E3's "direct overlap → $1/r^6$" reading fails directly; E1 is a clean yellow-tier scaffold.** The unification case is downgraded but not destroyed. Detailed below.

**E4 — Gradient overlap:** Computed $U(R) = -(Gm^2/R)\,\mathrm{erf}(R/2\sigma)$ exactly with SymPy. The force $F(R) \to 0$ linearly in $R$ as $R \to 0$ — **regularized, not amplified**. At $R = 0.01\sigma$, the overlap force is 8 orders of magnitude *weaker* than the naive $Gm^2/R^2$. The "overlap amplifies short-range gravity" reading proposed in Wisdom's 2026-04-23 speech **fails as computed in standard Newtonian gravity**. A *positive* secondary finding: the regularization eliminates point-mass self-energy divergences (bounded $U(0) = -Gm^2/(\sigma\sqrt\pi)$) — worth featuring in the paper as a free consequence of extended-particle ontology. Files: `theory/claims/E4-gradient-overlap/{claim, derivation, verification, caveats}.md`.

**E2 — Competing attraction (the load-bearer):** Built Python toy model with proton at origin and two electrons both at $+x$ (at $a_0, 2a_0$). Asymmetric geometry produces $\ddot r > 0$ (apparent inter-electron repulsion) with correct sign. Magnitude: ~$10^{-47}$ N versus Coulomb's ~$10^{-8}$ N — **off by $\sim 6\times 10^{39}$**. Control case (proton between the electrons) produces apparent *attraction* — confirming geometry-dependence. With E4 amplification gone (see above), there is no mechanism presently in GCM to close the magnitude gap. **S3's "all forces are gravity" unification case is now honestly yellow-tier as a structural compatibility statement, not a green-tier derivation.** Files: `theory/claims/E2-competing-attraction/{claim, derivation, verification, caveats}.md`.

**E3 — VdW as universal attraction:** Computed the gradient-gradient correlation of two Gaussians: $C(R) = m^2(6\sigma^2 - R^2)\exp(-R^2/4\sigma^2)/(32\pi^{3/2}\sigma^7)$. Exponentially suppressed at large $R$, changes sign at $R = \sigma\sqrt 6$, **does not produce $1/R^6$**. The naive reading fails. E3 is preserved as a *framing co-optation* claim (yellow): GCM predicts universal weak attraction between neutral bodies, and VdW is that attraction empirically; a rigorous graviton-substrate derivation would require specifying a fluctuation spectrum, a gravitational polarizability, and porting the Casimir-Polder calculation — none built. Files: `theory/claims/E3-vdw-universal/{claim, derivation, verification, caveats}.md`.

**E1 — Charge flow asymmetry:** Stated as hypothesis with minimal flow equation $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ and the three-sign mapping ($\Phi_g > 0$ for electrons, $< 0$ for protons, $= 0$ for neutrons). Verification flagged a concern: in GCM's deterministic substrate, the Fokker-Planck form may need to become pure Vlasov ($D = 0$, drift only). UNSPEC-1 is unchanged — an action principle + stability analysis is required to derive the sign from the dynamics. E1 is a clean yellow-tier scaffold. Files: `theory/claims/E1-flow-asymmetry/{claim, derivation, verification, caveats}.md`.

**Implications for the coherence paper (S10 architecture):**

1. **S3 no longer derives electron repulsion quantitatively.** Present E2 as "competing attraction reproduces the sign of electron repulsion in asymmetric geometries, but reproducing Coulomb magnitudes requires a short-range gravitational amplification mechanism not yet specified." This is honest, publishable, and non-trivial.
2. **The structural gap is now localized and named.** The hard theoretical work for the program is *specifying a principled short-range amplification mechanism* (density-dependent $G$, non-linear graviton coupling, contact interactions, etc.). Naming this explicitly is more valuable than claiming to have solved it.
3. **E4 has a positive second-order result to advertise:** extended-particle ontology regularizes the Newtonian self-energy divergence for free. This is a *win* for GCM, even though the amplification version failed.
4. **E3 should lead with the framing argument (universal weak attraction exists; GCM predicts it; VdW is it) rather than with a claim to derive $1/r^6$ from gradient overlap.**

**Recommended next action:** run `/debate` on the E2 downgrade — specifically, stress-test whether the "yellow-tier structural compatibility" framing is defensible, or whether E2 should be demoted further. Also stress-test whether E4's regularization finding is strong enough to anchor a paper section on its own (it plausibly is).

**Files produced in Session C:**
- `theory/claims/E4-gradient-overlap/claim.md`, `derivation.md`, `verification.md`, `caveats.md`
- `theory/claims/E2-competing-attraction/claim.md`, `derivation.md`, `verification.md`, `caveats.md`
- `theory/claims/E3-vdw-universal/claim.md`, `derivation.md`, `verification.md`, `caveats.md`
- `theory/claims/E1-flow-asymmetry/claim.md`, `derivation.md`, `verification.md`, `caveats.md`

---

### S4 — Quantum Structure

**Objective.** Treat the quantization claims with the math we have and name the rest aspirational.

**Q2 — Derive `P_n = 10n² + 2` from first principles.**
- Known result for face-centered cubic (FCC) / tetrahedrally-close-packed lattice with 12 nearest neighbors. Standard crystallography.
- Present the derivation or cite the standard reference; show the first few shells.

**Q3 — `E_n · P_n` invariant.** Already green, covered in S2.

**Q6 — Single discrete charge from stable shell packings.**
- Argument: if gravitons pack into stable tetrahedral shells, and if charge is a property of the shell structure (not the individual graviton), then stable packings produce quantized charges. Multiple shells could yield multiple charges (2e, 3e, ...) if they existed, but if only `P_1 = 12` and its simple multiples are stable, the fundamental charge e appears.
- Honest note: this is *aspirational* — we haven't shown that only certain packings are stable or that those packings produce exactly one unit of charge. It's a plausibility argument, not a derivation.

**Q4 — Wave-particle duality as real gradient distributions.**
- State as reformulation: probability amplitudes replaced by real density structures.
- Red-tier: requires reformulating QM, which is not in scope. Named as conceptual only.

**Acceptance:** Q2 FCC derivation; Q3 E·P table; Q6 stated as plausibility-argument yellow; Q4 honestly red.

**Breaks if:** the FCC claim `P_n = 10n² + 2` is wrong for the assumed packing (should be verified against standard crystallography references).

#### Session D Results (2026-04-23)

Session D produced three claim directories under `theory/claims/`. Status tally below; raw artifacts are the primary record, this subsection is the summary.

**Q2 — `theory/claims/Q2-tetrahedral-shells/`** (four files: `claim.md`, `derivation.md`, `verification.md`, `caveats.md`). Status: 🟢 **Green**. **Reframed in-place on 2026-04-23 (mid-session, on Wisdom's direction)** from v1 "assume cuboctahedral packing" to v2 "principle-first": gravitons attract uniformly → densest packing → 12 nearest neighbors (Kepler's conjecture, Hales 2005) → $P_n = 10n^2 + 2$. The formula is **robust across candidate 12-coordinate close-packings** — FCC cuboctahedral, HCP, and icosahedral Mackay clusters all give the same shell populations via *different* geometric decompositions (cuboctahedral: 12 vertices + $24(n-1)$ edges + $8 \cdot \frac{(n-1)(n-2)}{2}$ tri-face + $6(n-1)^2$ sq-face sites; Mackay: 12 vertices + $30(n-1)$ edges + $10(n-1)(n-2)$ tri-face sites — both sum to $10n^2+2$). Numerical check passes 5/5 in both decompositions (values: 12, 42, 92, 162, 252). CC-7 verification stack: 5/6 checks passed + 1 noted + 1 pending (Check 4 SymPy has code ready to run; Bash was not available in-session). Cross-references: Conway & Sloane (1999), Mackay (1962, *Acta Crystallographica* 15:916 — original icosahedral derivation), Hales (2005), OEIS A005901. **Convention flag:** $P_0 = 2$ is a mathematical artifact; formula valid for $n \geq 1$. **New open question flagged (OQ-Q2a):** which of FCC / HCP / icosahedral gravitons actually adopt — the shell populations don't distinguish, but the between-particle substrate structure does; matters for S3 / S6 / S7 (what the graviton medium between particles looks like). **Why the reframe matters:** v1 quietly assumed a specific geometry; v2 states the upstream physical principle (uniform attraction → densest packing), which is both more defensible and reveals that the shell formula is more general than a single crystal choice.

**Q6 — `theory/claims/Q6-discrete-charge/`** (two files: `claim.md`, `caveats.md`). Status: 🟡 **Yellow (plausibility argument only)**. The argument: charge is configurational (from CC-5), graviton packings form in cuboctahedral shells (Q2), if only certain shell counts are gravitationally stable (magic-number analogy) then charge would be quantized by that set. Explicitly flagged: we have *not* shown which packings are stable, nor that stable packings carry exactly $\pm e$. Fractional quark charges (UNSPEC-2) unaddressed. The section lists what would upgrade Q6 to green (stability criterion + discrete spectrum + mapping to charge values + agreement with observation). Presented as "direction a future derivation would take," not as a result.

**Q4 — `theory/claims/Q4-wave-particle/`** (two files: `claim.md`, `caveats.md`). Status: 🔴 **Red (conceptual only)**. States GCM's three-part commitment: realism (graviton distributions are real), locality (no FTL), superdeterminism (measurement independence denied; correlations from common history). Nearest-neighbor precedent: 't Hooft, *Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016). Hossenfelder cited as public defender. The superdeterministic qualifier is called out as **load-bearing** — "local realism" without the qualifier reads as instantly-dismissible to a Bell-literate physicist. Section lists what a full treatment would require (derive Schrödinger, derive Born rule, explain double-slit, explain entanglement, recover QFT in a limit) — none accomplished; all flagged as out of scope for the coherence paper. Explicit guidance to the paper drafter on what to say and what to avoid.

**Acceptance check against the S4 criteria above:**

| Criterion | Status |
|---|---|
| Q2 FCC derivation clean, verified, cited | ✅ |
| Q6 plausibility argument honest about its status | ✅ |
| Q4 cross-linked to CC-5.5; physicist cannot dismiss as naïve | ✅ |

**Surprises / honesty flags worth noting:**

1. **Q2 reframe surfaced mid-session.** v1 asserted cuboctahedral packing without argument. Wisdom pushed: "the point is whatever the shells would be of graviton clusters packing symmetrically, not a specific mathematical object." Checking this revealed that $P_n = 10n^2 + 2$ is actually robust across *all* 12-coordinate close-packings (FCC, HCP, Mackay icosahedral), so the formula is a consequence of the physical principle (uniform attraction → densest packing) rather than of arbitrarily picking a crystal. This is a stronger position than v1 delivered. v2 in place.
2. **The P_n formula is a cluster formula, not an infinite-lattice coordination sequence.** gcm_v2.md H7 is ambiguous about which. For the coherence paper, the cluster framing is the correct and intended one for GCM's particle-internal geometry, but the distinction should be stated so a crystallography-literate reader doesn't flag it.
3. **Q4's risk management:** Even with the superdeterministic qualifier, some readers will dismiss on sight. Caveat 9 in Q4/caveats.md recommends not centering the paper on Q4 — keep weight on Q2/Q3 (green) and S3 unification.
4. **Q6 is thinner than I'd hoped.** The magic-number analogy is a framing device, not a derivation. Q6 contributes to coherence (it shows GCM's ontology is compatible with discrete charge) but does not contribute to a quantitative theory case.
5. **New downstream open question (OQ-Q2a):** which specific close-packing gravitons actually adopt. Shell populations don't distinguish; between-particle substrate structure does. Matters for S3 / S6 / S7, not for Q2.

**Pending:** Close Check 4 of Q2 verification by running the included Python/SymPy snippet (Bash was not available in-session).

---

### S5 — Light and Photon Physics

**Objective.** Photon mass hypothesis + time-dilation mechanism for redshift.

**Status: Session E complete (2026-04-23).** All three Session E claims have full `theory/claims/<code>/` folders (claim / derivation / verification / caveats). Summary of results follows; see claim folders for full treatment.

**L1 (M5) — Photon has small rest mass.** 🟡 Yellow.
- Bound: Wang et al. 2023 FRB dispersion constrains `m_γ ≤ 2.1 × 10⁻¹⁵ eV/c²`.
- GCM claim: `10⁻⁵⁴ kg` ≈ `5.61 × 10⁻¹⁹ eV/c²` (precise hand-conversion verified).
- Margin vs. Wang: **~3,740× below bound ≈ 3.6 orders of magnitude.** The plan's earlier "4 orders" is a slight overstatement — flagged in `L1-photon-mass/derivation.md`.
- Margin vs. tighter PDG-style bounds (~10⁻¹⁸ eV/c²): only ~1.8×. Thin but passes. Tracked as falsification condition.
- Verification: 4/5 CC-7 checks passed; Wolfram/SymPy check pending (Python was unavailable in Session E — should be completed before L1 is promoted to main body of coherence paper).
- See `theory/claims/L1-photon-mass/`.

**L2 — Speed from mass.** Covered in Session B. (No change.)

**L3 — Wavelength proportional to internal graviton-cluster spacing.** 🟡 Yellow.
- Identification: `λ = N · d`, with `N` a fixed structural parameter (dimensionally clean; `N` currently undetermined — see caveats).
- Redshift cascade: if `N` is constant across emission and observation, `d_obs = (1+z) · d_emit` — cluster spacing scales linearly with wavelength.
- Compatibility with standard EM phenomenology (diffraction, Doppler, interference, photon energy): unaffected.
- Nature of claim: reframing of wave geometry in terms of graviton density peaks — not a derivation of wave structure from graviton dynamics. Yellow-tier by construction.
- See `theory/claims/L3-wavelength-spacing/`.

**R6 — Photon-structure geometric time dilation.** 🟡 Yellow. **Critical gate: PASSED.**
- Argument (from L3 + information-propagation-at-c):
  1. `d_obs / d_emit = (1+z)` (by L3).
  2. Inter-cluster arrival time `Δt = d/c`.
  3. Therefore `Δt_obs / Δt_emit = (1+z)`.
- **R6 produces `(1+z)^1.000` exactly.** DES 2024 measures `(1+z)^(1.003 ± 0.005)`. R6 lies within 1σ of DES (0.6σ from the central value). Consistent.
- Decisively passes the 200σ tired-light falsification gate (tired light predicts `α = 0`; R6 predicts `α = 1`).
- Structural, not coincidental — follows directly from L3's wavelength-spacing identification plus information-at-c.
- **R6 attaches cleanly to ANY redshift mechanism** (R1–R5) that stretches wavelength by `(1+z)`. GCM's cosmology is therefore not excluded by the tired-light falsification, regardless of which R mechanism S6 eventually commits to.
- Cross-check against Timescape: both produce `(1+z)` scaling via structurally distinct mechanisms (Timescape = clock-rate structure across voids/walls; R6 = photon internal structure). Compatible, could coexist.
- Falsification watch: if future precision measurements tighten DES and exclude `α = 1.000` at >3σ (e.g., `α = 1.010 ± 0.002` from LSST), R6 would face revision.
- See `theory/claims/R6-photon-time-dilation/`.

**Acceptance:** L1 constraint satisfied ✓; L2 clean (Session B) ✓; L3 dimensional argument clean ✓; R6 produces `(1+z)` structurally ✓. All four Session E acceptance criteria met.

**Session G dependency:** UNCHANGED. R6 succeeds, so the S6 plan does **not** need to degrade to "Timescape plus force unification." Any R1–R5 mechanism can proceed in S6 with R6 as the inherited time-dilation companion.

**Honesty flags raised in Session E:**
1. The plan's original "4 orders of margin" (vs. Wang 2023) is actually **~3.6 orders**. Minor, but flagged.
2. GCM's photon mass is only ~1.8× below the tightest PDG-style bounds (~10⁻¹⁸ eV/c²) — thin margin against the full bound suite, not "well below" all bounds.
3. Wolfram/SymPy check (Check 3 of CC-7) is pending for L1. Should be completed before L1 is promoted into the main body of the coherence paper.
4. R6 predicts exactly `(1+z)^1.000`; DES measures `(1+z)^1.003`. The difference is not statistically meaningful (0.6σ), but R6 does not currently explain the `0.003` — could be noise, systematics, or a real small deviation future GCM should address.

**Breaks if:** R6's argument had failed — the cosmology would have had to fall back to Timescape as the time-dilation backbone. This did not occur.

---

### S6 — Cosmological Redshift and Dark Matter

**Objective.** The most critical section. Commit to a redshift mechanism, address all seven empirical constraints, position against Wiltshire and Profumo.

**The commitment.**

Of the six R mechanisms:
- **R1 (space friction)** — structurally simple but must reproduce z-distance and evade the SNe Ia time-dilation death. R6 provides the time-dilation companion.
- **R2 (void decompression)** — structurally consistent with convergence, but the ISW tension is severe (growing voids → ISW signal that standard cosmology attributes to DE).
- **R3 (non-central position)** — requires a specific anisotropy that's not measured.
- **R4 (light-pressure sensitivity)** — no quantitative form.
- **R5 (selection effect — "light doesn't reach us because we're small")** — structurally different; avoids tired-light pitfalls because it's not a physics claim about photons, it's about what we measure. *This is Wisdom's intuition.*
- **R6 (photon-structure time dilation)** — not a redshift mechanism itself; it's the time-dilation companion that any R1–R5 needs to survive SNe Ia.

**Recommended commitment:**
Primary: **R2 + R6** (void decompression as the physical mechanism; R6 as its time-dilation companion). Align with **Wiltshire timescape** as the closest peer-reviewed relative.
Flagged as backup: **R5** (selection-effect). Label as genuinely different epistemic commitment; it may become the primary if R2's ISW tension is not resolvable.

**Addressing all seven empirical constraints:**

| Constraint | GCM Response |
|---|---|
| SNe Ia `(1+z)^1.003` time dilation | R6 argued to produce this scaling structurally; if R6 argument fails, the whole cosmology fails |
| ISW tension | **Explicitly named as open structural challenge.** Partial resolution: interpret observed ISW signal as evidence of graviton-density-gradient evolution, not dark energy. Requires quantitative model not yet built. |
| BAO 150 Mpc ruler | Acknowledge as hard constraint; the acoustic peak is from early-universe sound crossing and survives to today. GCM must explain why the same sound horizon appears at different redshifts without invoking expansion. Flag as unresolved. |
| CMB blackbody | Adiabatic cooling from expansion is standard. GCM alternative: blackbody as equilibrium state of graviton-density fluctuations at cosmological scale. Flag as conceptual. |
| Tolman surface brightness | Debated due to galaxy evolution; less sharp constraint. Acknowledge. |
| BBN | Requires early-universe physics; GCM's treatment is not yet specified. Flag as open. |
| DESI DR2 weakening DE | Supportive — DE is weakening/evolving, consistent with no-DE. |

**D1 — No dark matter particle.**
- Claim: what's inferred as dark matter is ordinary matter whose light doesn't reach us (absorbed, scattered, shifted out of detection).
- Connection to Profumo PBH: PBHs as a specific candidate form of this "matter we can't see" — they emit no light of their own and can concentrate mass invisibly. Profumo's active asteroid-mass PBH window (10¹⁷–10²³ g) is unconstrained and could account for a significant fraction.
- Testable prediction: galactic rotation curves should correlate with line-of-sight optical depth / stellar-obscuration maps, not with some mysterious halo profile. Flag as future-work test.

**D2 — No dark energy.**
- Inferred expansion acceleration is a misreading of the correct redshift mechanism. DESI DR2's evolving DE weakens the canonical interpretation; Wiltshire timescape fits Pantheon+ better than ΛCDM at ln B > 5.
- Position GCM as: timescape's phenomenology is right, GCM's force-unification provides the substrate.

**Acceptance:** one primary R mechanism committed; R6 companion argued; all seven constraints addressed (with "unresolved" being a valid address); D1 linked to PBH; D2 linked to timescape.

**Breaks if:** the ISW tension is argued away dishonestly (it can't be hand-waved), or BAO is ignored.

#### Session G Results (2026-04-23)

**Executed end-to-end per session brief `sessions/session-g-redshift-menu.md`.** Per Wisdom's 2026-04-23 instruction (Fork 2 above), S6 is reframed as a **menu of candidate mechanisms** with honest epistemic tiers, not a single-commitment section. This is more honest than over-committing to one mechanism we can't yet rigorously defend.

**Output:** eight claim folders at `theory/claims/R-redshift-menu/` — one per mechanism plus dark sector. Each folder contains `claim.md`, `plausibility.md`, `empirical-check.md`, `status.md`.

**Tier assignments (honest):**

| Mechanism | Tier | Central strength | Central weakness |
|---|---|---|---|
| R1 — space friction | 🟡 | Structural simplicity; compatible with GCM ontology (photons as graviton structures in graviton medium) | No first-principles derivation of friction coefficient $\alpha$; CMB blackbody preservation demands frequency-independent friction to FIRAS precision (50 ppm) |
| R2 — void decompression | 🟡 | Strongest peer-reviewed analog (Wiltshire/Seifert 2025 ln B > 5 on 1,535 Pantheon+ SNe Ia); ISW addressed as reinterpretation of observed signal, not elimination | No GCM-specific quantitative $\mu(z)$ fit; quantitative ISW shape prediction is future work |
| R3 — non-central position | 🔴 | Automatic $(1+z)$ time dilation via GR equivalence principle (no R6 needed); Secrest 2021 quasar-vs-CMB dipole 4.9σ misalignment is suggestive | Required cosmological potential anisotropy has not been measured; tension with CMB near-isotropy; no quantitative convergence-center model |
| R4 — light-pressure sensitivity | 🔴 | Conceptually distinguishable from other mechanisms; photons-respond-to-local-substrate is natural in GCM | No quantitative pressure-frequency relation; not clearly distinguishable from R2 as currently specified |
| R5 — selection effect | 🟡 | ISW-clean; blackbody-compatible (geometric version); structurally distinct from tired light (no energy-loss-in-transit claim); Wisdom's "we're small" intuition | Selection effects don't stretch time → R5 cannot produce SNe Ia time dilation on its own; needs R6 companion; no specific microscopic mechanism |
| R6 — photon-structure time dilation | 🟢 structural / 🟡 formal | Cascade argument is clean: $\lambda \propto (1+z) \to d_{\text{internal}} \propto (1+z) \to \tau \propto (1+z)$; matches DES 2024 within 1σ; required companion for R1/R2/R4/R5 | No specific photon internal-structure model; L3 (wavelength-spacing correspondence) is itself yellow; Session E not yet run |

**Dark sector:**

| Claim | Tier | Central strength | Central weakness |
|---|---|---|---|
| D1 — no dark matter particle | 🟡 | Structurally consistent with GCM ontology; Profumo PBH-as-DM program (asteroid-mass window 10¹⁷–10²³ g) is active peer-reviewed support; empirically plausible at order-of-magnitude (~10²⁵ asteroid-mass PBHs in Milky Way halo); WIMP null results supportive | No specific halo density profile from GCM; no GCM-specific CMB power-spectrum fit; PBH program is not GCM-specific work |
| D2 — no dark energy | 🟡 | Timescape (Seifert 2025 ln B > 5) is empirically strongest non-$\Lambda$ alternative; DESI DR2 evolving $w(z)$ at 2.8–4.2σ is supportive; $H_0$ and $\sigma_8$ tensions weaken $\Lambda$CDM | No GCM-specific $\mu(z)$ fit; inherits R2's ISW tension; BAO and CMB power spectrum undeveloped in GCM framework |

**ISW tension explicit treatment (per session brief success criterion):** R2's position is that the observed ISW signal is *reinterpreted*, not eliminated. The signal is real; the mechanism producing it is graviton-density-gradient evolution as matter converges into walls, not $\Lambda$-driven potential decay. The honest caveat is that the *quantitative shape* of the R2 ISW prediction has not been computed; this is named as the load-bearing open problem. Not hand-waved.

**Strategic positioning:**
- **R2 + R6** is the primary candidate of the menu, aligned with Wiltshire timescape.
- **R5 + R6** is the secondary candidate, flagged as the alternative if R2's ISW tension proves unresolvable.
- **R3** is the backup that becomes attractive only if R6 itself fails (R3 has auto time dilation).
- **R4** is retained for completeness but recommended to be mentioned only briefly in the coherence paper.
- **R1 + R6** remains valid as a tired-light-adjacent mechanism but is not primary.
- **D1 + D2** together form the "no dark sector new particles" package; alliance with Profumo (for D1) and timescape (for D2) is strategic backbone.

**Session brief success criteria (all met):**
- [x] Six mechanism briefs produced with clear status tags.
- [x] ISW tension for R2 explicitly addressed, not hand-waved.
- [x] D1 quantitatively positioned against PBH program (order-of-magnitude argument with $\sim 10^{25}$ asteroid-mass PBHs in Milky Way halo at $10^{20}$ g).
- [x] D2 positioned against Wiltshire (ally, same ISW problem, same "apparent acceleration is misreading" move).
- [x] R6 companion made explicit for every mechanism that needs it.
- [x] No mechanism given "viable" status that can't survive the gauntlet — R3, R4 honestly labeled red.

**Honesty flags recorded in Session G chronicle (2026-04-23):**
1. Session E (R6 detailed treatment) has not run. R6 brief derived from this plan's S5 specification. Once Session E runs, R6-photon-structure brief should be superseded or enriched.
2. No quantitative $\mu(z)$ fits for any mechanism. All are at structural plausibility level.
3. Dimensional checks performed for R1 friction coefficient and R2 void-decompression rate. No symbolic-derivation verification beyond order-of-magnitude.
4. Secrest et al. 2021 radio-galaxy vs. CMB dipole anomaly noted in R3 as suggestive but not quantitatively matched; R3 remains red.
5. Session C E2 result (magnitude off by ~10⁴⁰ for two-electron repulsion) is a reminder that structural plausibility does not guarantee quantitative fit. Same caution applies to R2, R5 — they are structurally plausible, but quantitative $\mu(z)$ work is unfinished.

---

### S7 — Magnetism and Thermodynamics

**Objective.** Conceptual-only; keep honest.

Each of H1–H5 stated with: the claim; why it's plausible aspirationally; what would make it green; nearest-neighbor existing physics.

**Length target: 1–2 pages total for the whole section.** Don't inflate conceptual claims.

---

### S8 — Structural Challenges

**Objective.** Name six things GCM cannot currently explain, ranked by severity.

1. **Parity violation** (per 2026-04-03 debate) — scalar-graviton cannot encode handedness. CC-1 Option C (internal state) is the future direction. Severity: structural. Current GCM cannot accommodate the weak force.
2. **ISW void-growth tension** (new, from redshift-empirics research) — the cosmological redshift mechanism implies void growth, which produces the ISW signal standard cosmology attributes to dark energy. GCM must explain this coherently. Severity: high.
3. **Lorentz force precision** (UNSPEC-4) — magnetism analogies must become exact numerical reproductions of `F = q(E + v×B)`. Severity: medium (well-known path, just not done).
4. **Bell's theorem** — competing attraction is locally realistic; Bell rules out local hidden variables. Escape: nonlocal realism (Bohmian type), well-known viable path, reshapes how "graviton" has to be read but survivable. Severity: medium.
5. **Semiclassical GR limit** — GCM's tetrahedral graviton lattice must recover smooth-spacetime GR in limits where GR is well-tested. LQG has this problem; GCM inherits it. Severity: high.
6. **Preon failure modes** — GCM is structurally a preon program. Inherits hypercolor confinement objection (why don't we see GCM's preonic DOFs at LHC energies?) and wrong-mass objection. Severity: medium.

**Each gets one paragraph with the objection, the severity, and the direction future work would take.**

**Acceptance:** six challenges named, ranked, and directions sketched. This is the section that most distinguishes GCM from dismissible speculative unification programs — naming failures openly is credibility-earning.

---

### S9 — Literature Positioning

**Three paragraphs, plus two shorter ones.**

1. **GCM vs. Wiltshire timescape.** Timescape fits Pantheon+ better than ΛCDM at ln B > 5 (Seifert et al. 2025, MNRAS Letters 537, L55). GCM's cosmological claims (no DE, void/wall structure, `(1+z)` time dilation via R6) overlap heavily with timescape's phenomenology. **GCM's positioning:** we provide a force-unification mechanism for *why* matter organizes into the void/wall structure timescape takes as given. Complementary, not competitive.

2. **GCM vs. Verlinde entropic gravity.** Verlinde's 2017 SciPost paper (~460 citations) treats gravity as emergent from entanglement entropy on holographic screens, producing a "dark gravity" force that mimics dark matter. Shared commitment: gravity-as-substrate, no DM particle. Divergence: Verlinde's framework is entanglement-thermodynamic and accepts expansion; GCM is density-gradient and rejects expansion. Both are credible as alternative-gravity programs.

3. **GCM vs. Profumo PBH dark matter.** PBH-as-DM accepts standard cosmology but eliminates the DM particle, as GCM does. **GCM's D1 claim (matter whose light doesn't reach us) is structurally generalized-PBH.** PBHs are a specific candidate form. Profumo's 2025 asteroid-mass-window work (~10¹⁷–10²³ g) is least-constrained and supports the "there's plenty of room for invisible ordinary matter" position. Outreach to Profumo can leverage this alignment.

4. **Short: Kaluza-Klein lineage.** GCM is geometry-as-unification, inheriting the lineage's positive lesson (geometry can unify) and cautionary one (every added structure needs a testable signature). GCM avoids KK's failure mode (extra dimensions not observed) by staying in 3+1D.

5. **Short: Preon ancestry.** GCM is structurally a preon program. Inherits both the unification ambition and the failure-mode objections (hypercolor, wrong masses). Named as ancestry, not denied.

**Acceptance:** three main positioning paragraphs + two short connective ones. All citations verified against the research output.

---

### S10 — Coherence Paper Architecture

**Target:** 12–20 pages, organized as follows. Word counts are targets, not limits.

1. **Abstract** (200 words). The four tenets in one paragraph; the central claim (all forces from graviton density gradients, universe converging); the epistemic posture (coherence case, not proof); honest acknowledgment of structural challenges.
2. **Introduction & Tenets** (S1) — 500 words.
3. **The Verifiable Math Spine** (S2) — 2,000 words (five green pieces).
4. **Unification Mechanics** (S3) — 2,500 words. E2 toy model is the centerpiece.
5. **Quantum Structure** (S4) — 1,200 words.
6. **Light & Photon Physics** (S5) — 1,200 words.
7. **Cosmological Redshift and Dark Matter** (S6) — 2,500 words. The hardest.
8. **Magnetism and Thermodynamics** (S7) — 500 words (conceptual, keep short).
9. **Structural Challenges** (S8) — 1,500 words. The honesty section.
10. **Literature Positioning** (S9) — 1,000 words.
11. **Conclusions and Future Directions** — 500 words.
12. **Appendices** — derivations too long for main body; references the `claims/` subfolder.

**Total: ~13,600 words = ~15 pages single-column.** Fits the target.

**What to cut if time-pressured:**
- S7 can shrink to one paragraph.
- S4's Q4 can be cut entirely (conceptual only).
- S5 can drop L3 (keep L1, L2, R6).
- S3's E1 flow-asymmetry can be flagged as future work rather than sub-sectioned.

**What is non-negotiable:**
- S8 (structural challenges) stays at full length. Cutting it cuts credibility.
- S3's E2 toy model stays. It's the load-bearer.
- S6's commitment to a redshift mechanism stays. Without commitment, no cosmology case.

---

## Forks Defaulted (per Wisdom's "go autonomous" instruction, 2026-04-23)

Wisdom read the three forks below as confusion-inducing overhead rather than useful gates. Defaulting them so nothing blocks. He can redirect if any default is wrong.

### Fork 1 — What IS a graviton, formally? **HARDENED to A. C is ruled out by the Axiom of Indivisibility.**

Wisdom's 2026-04-23 clarification converts this from a default-with-flag into a hard commitment. The Axiom of Indivisibility (CC-5) rules out Option C entirely — a truly indivisible particle cannot have internal variability, so any "internal state" escape hatch is philosophically incoherent.

- **A. Classical point particle.** Position + identity-as-gravitating-point + unit mass. Nothing else. **This is the commitment.**
- **B. Discrete lattice excitation.** Open question (does the graviton move, or is it fixed on a lattice?) — this is orthogonal to the Axiom; doesn't add or subtract intrinsic properties. Remains open and is worth exploring in a separate claim.
- **C. Classical point with internal state.** **Ruled out** by the Axiom.

**Consequence:** the parity-violation challenge in S8 gets harder, not easier. The escape path is configurational (handedness from graviton arrangement), not graviton-intrinsic. This is the price of philosophical cleanliness, and Wisdom accepts it.

### Fork 2 — Primary cosmological redshift mechanism? **Defaulted to "menu approach" per Wisdom's preference.**

Original framing forced a single commitment (R2+R6, or R5+R6, etc.). Wisdom's response, paraphrased from 2026-04-23: *"it's probably an amalgamation of a number of different systems... bring up things that say hey these are our claims but look like it's possible that they could work."*

**Revised approach: present a menu.** S6 (Cosmological Redshift) treats R1 through R6 as a family of candidate mechanisms, each with: the claim, the math (where available), the nearest-neighbor physics program (Wiltshire for R2, tired-light critiques for R1, etc.), and a plausibility + empirical-constraint discussion. R6 (photon-structure time dilation) remains the required companion to any mechanism, because `(1+z)^1.003±0.005` SNe Ia time dilation must be produced structurally.

This is *more* honest than committing to one mechanism we can't yet rigorously defend. It's also closer to how GCM actually thinks about the problem: convergence produces multiple effects on light propagation, and disentangling them is future work.

**Trade-off accepted:** the paper won't have a single committed redshift mechanism. Physicists may push back on this. Answer: "We're presenting candidate mechanisms with honest evaluation, not defending a specific one. The claim is the *structural* story — light doesn't reach us fully because of multiple convergence-related effects — not a specific formula for redshift vs. distance." This is defensible as a coherence case, less defensible as a quantitative theory (which we're explicitly not claiming).

### Fork 3 — Paper length and audience calibration? **Defaulted to 15-page coherence + 3-page exec summary.**

The 15-page version lives at `paper/coherence-paper.md` (written in Session J). The 3-page executive summary lives at `paper/executive-summary.md` — derivation-free, plain-language, suitable for LinkedIn posting or outreach cold-pings. Both target the same claims; the exec summary strips math and lives closer to Wisdom's voice.

If length becomes an issue during Session J, the cut-list from S10 activates: S7 shrinks to one paragraph, S4.Q4 cuts, S5.L3 cuts, S3.E1 becomes flagged-only.

---

## Reconciliation (Step 3)

Conflicts between sections, unmet dependencies, fragility cross-references, remaining questions.

### Conflicts identified

1. **R2 (void decompression) vs. S8.ISW-tension.** Same mechanism: growing voids are needed for R2 but produce the ISW signal GCM attributes away from dark energy. **Resolution:** address explicitly in S6 and S8. GCM's position becomes: "the observed ISW signal reflects graviton-density-gradient evolution at cosmological scale, not dark energy expansion." This is a promise, not a derivation — but it's honest.

2. **R5 (selection effect) vs. R2 (void decompression).** Different epistemic types: R2 is a physics claim about photons; R5 is a claim about what we measure. They can coexist but shouldn't be presented as the same kind of mechanism. **Resolution:** S6 treats R2+R6 as the primary commitment, R5 as an alternative framing that may become primary if R2's ISW tension is unresolvable.

3. **E2 competing attraction vs. U4 parity violation.** E2's toy model uses scalar density attraction. U4 notes a scalar graviton cannot encode handedness. **Not a direct conflict** — E2 is about magnitude of force between particles, U4 is about the weak force's internal structure — but *related*: both are consequences of the scalar-graviton commitment (CC-1 A). **Resolution:** S1 names CC-1 A as the current commitment with C (internal state) as the future direction that would resolve U4 but would require revisiting S3 to check what E2 still says.

4. **L1 photon mass (10⁻⁵⁴ kg) vs. experimental bounds.** Bounds are strict (FRB dispersion `≤ 2.1 × 10⁻¹⁵ eV/c²`). GCM's ~`5.6 × 10⁻¹⁹ eV/c²` is safely below. **No conflict.** Flag for update: if future bounds tighten by 4+ orders of magnitude, GCM would face a choice.

5. **D1 (no DM particle) vs. observed rotation curves.** GCM claims rotation curves come from ordinary-matter-we-can't-see. Standard halo-inferred DM has specific radial profiles. **Tension:** can "matter we can't see" produce these specific profiles? **Resolution:** flag as S6 future-work; GCM doesn't have a quantitative rotation-curve model yet. This is a coherence gap to name honestly.

6. **D2 (no DE) vs. DESI DR2.** DESI sees weakening/evolving DE, not no-DE. **Partial support, not full.** GCM's position: "DE is weakening because it was always an artifact of redshift misinterpretation; as data improves, the artifact fades." Testable: if future measurements continue to weaken DE, support grows.

### Unmet dependencies

- **S3.E2 depends on having E4 (gradient-overlap) worked out** — they reinforce each other. If E4 can't produce the right scale hierarchy (`10³⁶` EM/gravity ratio, at least to order of magnitude), E2's competing-attraction argument is harder to make. Plan for E3 and E4 to be worked in parallel.
- **S6.R6 depends on S5.L3** (wavelength ∝ graviton-cluster spacing). If L3 can't be dimensionally grounded, R6 loses its mechanism.
- **S8 depends on having the full S6 cosmological commitment** to know which structural challenges to name.

### Fragility cross-references (critical)

Each section's "breaks if" conditions compared against sibling commitments:

- S1 breaks if CC-1 commitment is never made → sibling sections assume differently and reconcile badly. **Mitigation:** S1 is Session A and precedes all others.
- S3 breaks if E2 toy model can't be built → whole unification case weakens. **Mitigation:** run `/debate` or a focused exploration session before committing to the paper's E2 section.
- S5 breaks if R6's `(1+z)` argument fails → the cosmology section loses its time-dilation companion. **Mitigation:** have R5 (selection effect) and timescape's-mechanism as backups.
- S6 breaks if ISW tension is unresolvable → have backup position of "GCM as timescape with force-unification mechanism" ready.

### Open questions (for Wisdom)

Three genuine forks where human judgment is needed:

1. **CC-1 commitment.** A (classical point), B (lattice excitation), or C (field with internal state)? Recommendation: A for coherence paper, C flagged as future direction. Do you agree, or do you want to commit to C now even though it complicates S1?

2. **Primary redshift mechanism commitment.** R2+R6 (closest to Wiltshire; strongest peer-reviewed alignment; has ISW tension) or R5+R6 (Wisdom's selection-effect intuition; no ISW problem because not about void growth; less peer-reviewed precedent)? Recommendation: R2+R6 for the coherence paper; R5 as flagged alternative. Agree?

3. **Paper length and audience calibration.** 15 pages targeting Profumo + Anthropic + Alembic is one object. A 5-page "pre-print summary" suitable for LinkedIn posting is another. A 25-page rigorous draft with appendices is a third. Which is the primary deliverable? Recommendation: 15-page coherence case as primary, with a ~3-page "executive summary" version for outreach. Agree?

### Verdict

**MINOR FIXES** — plan is executable. Three forks (above) need Wisdom's judgment before Session A launches.

---

## Session Brief Decomposition (Step 1.7)

When Wisdom is ready to start execution (after the three forks above are settled), the sessions below become session brief files under `~/sessions/gcm-coherence-case/`:

### SESSION-A: Foundations (2 hrs, start immediately after Wisdom's approval)

**Prerequisites:** None.
**Task:** Lock in CC-1 ontology commitment; restate T1–T4 cleanly; soften T3; produce the 1-page foundational statement.
**Output:** `theory/claims/S1-foundations/` with `claim.md` and `rationale.md`.
**Success criterion:** someone unfamiliar with GCM reads the foundational statement alone and understands what's being claimed at what epistemic level.

### SESSION-B: Math Spine (4 hrs)

**Prerequisites:** Session A.
**Task:** Write the five green-tier notes (M1, E7, Q3, L2, M3) in `theory/claims/` subfolders following the raw-data-preservation + claim.md/derivation.md/verification.md/caveats.md structure.
**Output:** Five subfolders, each with four files. ~10 pages total content.
**Success criterion:** each derivation passes CC-7 (dimensional check, numerical verification, comparison to published bounds, limit cases where applicable). Each note has explicit "what this proves and doesn't prove."

### SESSION-C: Unification Mechanics (8 hrs — possibly split into two sittings)

**Prerequisites:** Session A.
**Task:** S3 detailed work. E2 toy model (the centerpiece), E3 VdW comparison, E4 gradient-overlap integral, E1 flow-equation sketch.
**Output:** `theory/claims/E2-competing-attraction/`, `E3-vdw-universal/`, `E4-gradient-overlap/`, `E1-flow-asymmetry/`.
**Success criterion:** E2 toy model produces recognizable repulsion-from-competing-attraction at correct sign and order-of-magnitude scaling, OR is honestly labeled as open structural gap.
**Consider:** running `/debate` on E2 before committing, as suggested in reconciliation.

### SESSION-D: Quantum Structure (4 hrs)

**Prerequisites:** Session A.
**Task:** S4 detailed work. Q2 FCC derivation, Q3 tabulation, Q6 plausibility argument, Q4 honest conceptual-only framing.
**Output:** `theory/claims/Q2-tetrahedral-shells/`, `Q3-EP-invariant/` (already partly done in v2), `Q6-discrete-charge/`.

### SESSION-E: Light Physics (3 hrs)

**Prerequisites:** Session A.
**Task:** S5 detailed work. L1 (photon mass vs. FRB bound), L2 massive-photon speed, L3 wavelength-spacing dimensional argument, R6 time-dilation structural argument.
**Output:** `theory/claims/L1-photon-mass/`, `L2-photon-speed/`, `L3-wavelength-spacing/`, `R6-photon-time-dilation/`.
**Critical:** R6 must produce `(1+z)^1.003±0.005` structurally.

### SESSION-F: Magnetism and Thermodynamics (2 hrs)

**Prerequisites:** Session A.
**Task:** S7 detailed work. Keep conceptual. H1–H5 stated with plausibility + honest provability notes.
**Output:** `theory/claims/H1-toroidal-alignment/` through `H5-equipartition/`.

### SESSION-G: Cosmological Redshift and Dark Matter (8 hrs — reading-heavy)

**Prerequisites:** Session E.
**Task:** S6 detailed work. Commit to primary R mechanism; R6 companion argued; all seven empirical constraints addressed; D1 positioned against PBH; D2 positioned against DESI DR2 and Wiltshire.
**Output:** `theory/claims/R-redshift/` (with subfolders per mechanism), `D1-no-DM-particle/`, `D2-no-DE/`.
**Deep reading:** Seifert 2025 timescape paper, DES 2024 SNe Ia time-dilation paper, Wang 2023 FRB photon-mass bound, Profumo 2025 PBH papers.

### SESSION-H: Structural Challenges (3 hrs)

**Prerequisites:** Sessions C and G.
**Task:** S8 detailed work. Six challenges named, ranked, directions sketched.
**Output:** `theory/claims/structural-challenges.md`.

### SESSION-I: Literature Positioning (2 hrs)

**Prerequisites:** Sessions A–H (reads everything).
**Task:** S9 three positioning paragraphs + two short ones.
**Output:** `theory/claims/literature-positioning.md`.

### SESSION-J: Paper Architecture and Composition (8–12 hrs)

**Prerequisites:** All above.
**Task:** Compose `paper/coherence-paper.md` from claims. Write introduction, abstract, stitch, edit.
**Output:** The coherence paper itself.

### Execution order recommendation

- **Immediately after plan approval:** Session A (2 hrs) — unblocks everything.
- **Next week:** Sessions B, D, E in parallel (11 hrs total; could be 3 days at 4 hrs each, or one long weekend).
- **Following week:** Session C (the hard one — reserve a full day).
- **Following week:** Session F (short) + Session G (the hard cosmology day).
- **Final stretch:** Sessions H, I, J.

Total ~46–50 hours over ~4 weeks at a sustainable pace.

---

## What This Plan Is NOT

- **Not a quantitative GCM theory.** The coherence paper is plausibility + positioning + honest challenge-naming, not numerical prediction.
- **Not a published physics paper.** The coherence paper is posting-worthy, not journal-submission-ready. A journal version is a distant target needing orders-of-magnitude more work.
- **Not a Lean 4 formalization.** No Lean work in this plan. Aspirational future direction only.
- **Not a community practice build.** The Spiritual Ethos half has its own plan (not this document). Community infrastructure for the ethos is future work.
- **Not a commitment to any ontology.** CC-1 is a recommendation; Wisdom can redirect.

---

## Distinctions That Matter

Three different targets that are often conflated but shouldn't be:

1. **Coherence case** (this plan) — "Take GCM seriously; here's why it's non-trivial; here's what engagement would look like." Target audience: sophisticated interlocutors willing to engage pre-formal work.
2. **Quantitative theory** (distant) — "Here are numerical predictions that distinguish GCM from ΛCDM / SM." Target audience: experimentalists and precision-physics referees.
3. **Published physics paper** (further still) — "Here's peer-reviewed work in a credible venue." Target audience: the broader physics community.

The coherence case is a sufficient deliverable for the Anthropic application, the Profumo outreach, and the Alembic-circle sharing. Don't inflate it into a quantitative theory; don't deflate it into a sketchy speculation post.

---

## Next Action

1. **Wisdom reads this plan.** Especially: the three open questions in Reconciliation.
2. **Wisdom approves or redirects.** Three forks to close:
   - CC-1 commitment (A/B/C)
   - Primary redshift mechanism (R2+R6 or R5+R6)
   - Paper length/audience calibration (15-page coherence + 3-page exec summary, or different)
3. **Once approved:** Session A launches. 2 hours. Unblocks Sessions B–J.
4. **Plan updates** in place as sessions complete and deviations surface. This is a living document.

---

## Plan Metadata

- **Plan file:** `plan-coherence-case.md` (this)
- **Research sources consulted:** [`research/sources/2026-04-23-adjacent-programs.md`](research/sources/2026-04-23-adjacent-programs.md), [`research/sources/2026-04-23-redshift-empirics.md`](research/sources/2026-04-23-redshift-empirics.md), plus all existing `2026-04-23-*.md` research agent outputs.
- **Speech source:** [`knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md`](knowledge/sources/wisdom-speech/2026-04-23-gravitationalism-aspirational-lens.md)
- **Supersedes:** [`plan.md`](plan.md) (kept as surface-level quick reference).
- **Referenced peer-reviewed work:** Seifert et al. 2025 MNRAS Letters 537, L55 (timescape Pantheon+); Verlinde 2017 SciPost (entropic gravity); Wang et al. 2023 JCAP (FRB photon mass bound); DES 2024 arXiv:2406.05050 (SNe Ia time dilation).

*Living document. Updated as sessions complete and forks are closed.*
