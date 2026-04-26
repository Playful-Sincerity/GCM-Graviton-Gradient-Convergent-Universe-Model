# GCM Coherence-Case Paper-1 — Writing Plan
**Date:** 2026-04-24
**Target submission:** ~2026-04-25 (tomorrow)
**Lead:** Wisdom Happy
**Plan author:** PSDC, informed by `theory/claims/audit-2026-04-24.md`
**Companion:** `concept-paper/2026-04-23-gdgm-concept.md` (Gravitationalism-umbrella positioning; different audience, different document)

---

## Position statement — what this paper IS and IS NOT

**Is:** a *coherence case* — a map showing that a graviton-density-gradient single-substrate framework is *non-trivial enough not to dismiss*. Conceptually intuitive, structurally scaffolded, honest about what's done and what isn't.

**Is not:** a derivation of the standard model from graviton dynamics. Not a proof. Not claiming any individual testable prediction has been verified. Not claiming unification works; claiming that the structure *could* support unification if the named open questions are closed.

**One-sentence thesis:** *GCM proposes that all matter and the four fundamental forces emerge from configurations of a single fundamental particle (the graviton) interacting through gravity alone — and this document presents the internal-consistency map, the structural scaffolds, and the named open derivations that together establish the program as worth engaging with rigorously.*

**The framing that does the work:** the paper's distinguishing feature is *honesty about what's been verified vs what hasn't.* A hostile reader who reaches page 3 should be unable to accuse the paper of overclaiming. A sympathetic reader should find concrete hooks for engagement.

---

## Target audience and length

**Audience:** serious physicists (Profumo, Kiel Howe, Stefano Profumo lineage, Verlinde readers), Anthropic researchers (Sohil, Wes), and researchers open to non-mainstream programs (Wiltshire, 't Hooft, Padmanabhan).

**Length:** 15-20 pages in normal density. No appendix bloat. The `theory/claims/` subfolder is the receipt; the paper itself references it rather than reproducing derivations.

**Tone:** warm + precise, no marketing language, no padding. Follow PS brand voice where appropriate but this is a physics paper, not a manifesto — keep claims precise.

---

## Section outline

### §1 — Introduction (~1 page)

**Content:**
- What GCM is (one sentence)
- What this paper is (coherence case, not proof)
- What this paper is not (no unification derivation, no testable prediction verified)
- Roadmap (§2 onward)
- One paragraph: *why a coherence case is worth reading* — unification programs are ambitious and most are dismissed at first glance; this paper makes the program legible and auditable, so that engagement is possible.

**Framing language to use:** "coherence case," "research program," "structural scaffold," "open derivation," "named gap."
**Framing language to avoid:** "unifies," "derives," "proves," "explains," "shows."

---

### §2 — Ontological Foundations (~2 pages)

**Content:**
- T1–T4 (the four tenets, cleanly stated)
- The Axiom of Indivisibility (CC-5; Wisdom's formalization)
- Local realism via superdeterminism (CC-5.5; cite 't Hooft 2016, Hossenfelder 2020+)
- Honest flag: P5 ("brute primitive ⟹ non-physical") is the contestable load-bearing premise; bare-particular objection named.

**Source claims:** S1-foundations (indivisibility-formal.md, realism-locality.md)

**What to reference, not reproduce:** the SymPy SAT/UNSAT verification of FOL encoding and Bell-structure escape routes — cite subfolder.

**Honest tally correction:** S1-AX-1-F currently shown as 4/5 PASS; honest is 3 substantive Python + 1 Lean `sorry`-stub + 1 TODO.

---

### §3 — Structural Scaffolds Compatible with Known Physics (~3 pages)

**Former title:** "Verifiable Math Spine"
**Revised title:** "Structural Relations in the Graviton-Substrate Framework"

This section is five pieces showing that *standard physics can be recast in GCM-compatible forms*. Not claiming novelty of the math; claiming the framework accommodates known results without contradiction.

**Pieces to include (five total, picked from the audit INCLUDE set):**

1. **L1 photon mass** — $m_\gamma \approx 10^{-54}$ kg as a parametric estimate (explicit: not derived); consistent with PDG and Wang 2023 FRB bounds. *Must live-check PDG bound before submission.*
2. **L2 photon speed** — $v < c$ consequence of $m_\gamma > 0$; deviation at $\sim 10^{-37}$, below measurement.
3. **L3 wavelength-spacing identification** — $\lambda$ identified with internal graviton-cluster spacing; caveat: reframing, not derivation; $N$ (cluster count per photon) undetermined.
4. **M1 graviton mass** — $m_g \approx 4 \times 10^{-87}$ kg as a *parametric expression scaling with $\rho_{bound}$*, not a number. OQ-2 named: max packing density = nuclear density is assumption, not result.
5. **Q2 tetrahedral shells** — $P_n = 10n^2 + 2$ as the geometric consequence of 12-coordinate close packing. **Cite Hales (2005), Conway-Sloane, Mackay (1962), OEIS A005901.** Not GCM-original math; the GCM-specific piece is "uniform attraction ⟹ densest packing" which is the *step before* the formula.

**What this section does NOT include:** E7 (Bohr partial derivative is not GCM-specific; defer to future paper when emergent $e, m_e$ exist); M3 Planck-cell count ($V_{obs}/\ell_P^3$ is sphere over cube, not load-bearing); Q3 asymptote ($E_n P_n \to 136$ eV is algebraic coincidence, numerology risk).

**Framing language:** "consistent with," "compatible with," "GCM can accommodate," "structural relation," "parametric."

---

### §4 — Substrate Compatibility with Force Phenomena (~1 page)

**Former title:** "Unification Mechanics"
**Revised title:** must NOT contain the word "unification" in the title.
**Suggested title:** "Substrate Compatibility with Force Phenomena" or "Toward a Force-Emergence Mechanism"

**Content:**
- E1 flow-asymmetry scaffold only (charge as $\nabla \cdot \mathbf{J}_g$)
- Explicit UNSPEC-1, UNSPEC-2 flags up-front
- Fokker-Planck form acknowledged as *reframing of the research question,* not derivation of charge
- Honest: *no force unification has been derived in GCM to date.* The scaffold names the shape of what would be needed.
- Pointer to §8 where E2, E3, E4 are discussed as structural challenges

**What this section does NOT include:** E2, E3, E4, E7 — all relocated.

---

### §5 — Quantum Structure (~1 page)

**Content:**
- Q2 already covered in §3
- Q4 wave-particle as 2-paragraph *conceptual commitment* only (cite 't Hooft 2016 for the realism reading; explicit: full reformulation of QM is out of scope and is future work)
- Q6 mention in 1 paragraph — plausibility argument only; explicit that no stability calculation has been done

**What this section does NOT include:** Q3 (excluded as numerology); any claim of deriving QM from GCM.

---

### §6 — Cosmological Redshift and Dark Sector (~3-4 pages)

**The load-bearing section for GCM's empirical engagement.**

**Content:**
- **Commit to one primary R mechanism.** Recommendation: **R2 (void decompression)** as primary; it has the strongest peer-reviewed alliance (Wiltshire timescape, Seifert et al. 2025 MNRAS Letters 537 L55, ln B > 5 over ΛCDM on 1,535 Pantheon+ SNe Ia). R1 (space friction) as compatible secondary. R5 (selection effect) as epistemically distinct framing.
- **R6 photon-structure time dilation** as the load-bearing companion that escapes the DES 2024 tired-light falsification ($(1+z)^{1.003 \pm 0.005}$). **Explicit caveat:** R6's derivation chain $\lambda \to d \to \tau$ reduces to an L3 definitional identity + an internal-propagation assumption; the cascade is symbolically clean given premises; the premises are conjectural. This is the honest statement.
- **R3 non-central position** as one-paragraph menu mention with the corrected gradient ($cH_0 \approx 6.8 \times 10^{-10}$ m/s²) and the MOND coincidence (within 5× of $a_0 = 1.2 \times 10^{-10}$ m/s²); explicit that R3 is red on empirical grounds.
- **R4 light-pressure** excluded — "concept without a mathematical body."
- **D1 no dark matter** — lead with Profumo PBH-as-DM program; GCM inherits its observational viability. **The 12-order Hawking T correction caught by verification retrofit is a concrete exemplar of verification doing real work.** Halo profile and CMB power spectrum gaps named (OQ-D1-halo-profile).
- **D2 no dark energy** — lead with Wiltshire alliance + DESI DR2 (2025) evolving $w(z)$ at 2.8-4.2σ. Acknowledge ISW tension head-on.
- **ISW tension:** name it, acknowledge it, point to future work (OQ-R2-ISW).

**Source claims:** R-redshift-menu/R1, R2, R3, R5, R6; R6-photon-time-dilation (standalone, 7-check version is authoritative).

**Framing language:** "candidate mechanism," "companion to escape tired-light falsification," "consistent with but does not derive," "Wiltshire alliance," "Profumo alliance."

---

### §7 — Magnetism and Thermodynamics (~1 page)

**Content:**
- H1 toroidal magnetism — plausibility sketch only (radial + uniform superposition → toroidal streamlines; right-hand-rule emergence). Explicit: UNSPEC-4 (Lorentz force reproduction) remains red, sharpened by verification to "missing time-dependent oscillation dynamics."
- H2 one-paragraph reference — Newton's cooling form reproduces; equipartition + Planck (UNSPEC-5) red. Short.

**Framing language:** "plausibility," "qualitative consistency with," "configurational sketch."

---

### §8 — Structural Challenges ⭐ (~2 pages — MAKE THIS A STRENGTH)

**This is the section that will earn physicist respect.** Every named challenge is a concrete hook for engagement.

**Content (concrete named challenges, each 1 short paragraph):**

1. **E2 magnitude gap** — Newtonian competing-attraction reproduces the SIGN of electron repulsion but is $10^{40}$ too weak; this is an intrinsic gravity-vs-Coulomb hierarchy, not a toy-geometry artifact. An unspecified short-range amplification mechanism would be required.
2. **E3 functional-form falsification** — naïve direct-overlap reading of Van der Waals predicts exponential tail, not the observed $1/R^6$. Framing co-optation survives (universal attraction compatible with observed VdW); the direct derivation does not.
3. **E4 amplification falsification / regularization observation** — closed-form Gauss-law overlap is $U(R) = -(Gm^2/R)\,\mathrm{erf}(R/2\sigma)$. Gradient overlap *regularizes* Newtonian attraction at short range; it does not amplify. Positive side-result: the Newtonian singularity is resolved in the overlap limit.
4. **Q6 vs E1 tension** (newly identified by 2026-04-24 audit) — Q6 posits stable symmetric shell packings as the charge-quantization mechanism; E1 posits asymmetric divergence of graviton current as the charge-sign mechanism. Symmetric configurations give zero divergence by the divergence theorem. Neither claim resolves this.
5. **Minimal-model poverty** (newly identified by 2026-04-24 audit) — S1's deterministic Newtonian minimal model ($\ddot{x}_i = \sum G m_g / r_{ij}^2$) cannot produce the stochastic, thermalizing, oscillatory, or continuum-field phenomena that downstream claims invoke. A richer foundation (fields, Lagrangian, or stochastic noise) is required.
6. **Parity violation** — Indivisibility Axiom rules out intrinsic graviton chirality; weak interactions' left-handedness must emerge configurationally. Path: show certain graviton configurations produce emergent chirality.
7. **Semiclassical GR limit** — how does GCM recover gravitational-wave propagation, perihelion precession, frame dragging? LQG has this problem; GCM inherits it.
8. **ISW tension** — the redshift mechanism implies growing voids which produce the ISW signal the standard model attributes to dark energy; GCM must either commit to static voids (losing R2) or explain the ISW signal mechanistically. Quantitative shape prediction is future work.
9. **Preon ancestry** — if GCM is a preon program, it inherits hypercolor-confinement and wrong-mass objections; lesson is constitutional preons failed and GCM's "indivisible graviton with only position" position is specifically designed to avoid preon-specific pitfalls.
10. **Bell / superdeterminism testability cost** — the local-realism-via-superdeterminism commitment denies measurement independence; philosophically uncomfortable, empirically difficult to distinguish from nonlocality or randomness.

**Framing language:** "named open challenge," "gap requires closing," "current state admits," "would require."

---

### §9 — Literature Positioning (~1-2 pages)

**Content:** 3-5 positioning paragraphs — 1 per major program.

1. **Wiltshire timescape** — complementary, not competing. GCM provides graviton-density-gradient mechanism for timescape's phenomenology. Cite Seifert et al. 2025.
2. **Verlinde entropic gravity** — shared substrate-thermodynamic lineage; different formalisms. Cite Verlinde 2017.
3. **Profumo PBH-as-DM** — concrete alliance for D1. Cite Profumo's recent PBH program.
4. **'t Hooft cellular automaton** — precedent for superdeterministic-realist programs. Cite 't Hooft 2016.
5. **Padmanabhan emergent gravity** — thematic ancestor for "gravity as substrate" programs. Cite Padmanabhan.
6. **Preon ancestry** — Harari, Pati-Salam; honest acknowledgment of constitutional-preon failure modes and how GCM's single-indivisible-graviton position avoids them.
7. **Kaluza-Klein lesson** — elegant unification that failed; cautionary lineage.

**Research pass needed before submission:** verify each citation is current and correctly represented. See `research/findings/literature_report.md` for existing coverage.

---

### §10 — Verification Methodology and Errors Caught ⭐ (~1-2 pages)

**Lead with errors caught, not checks passed.** This is the methodological distinguisher and what will earn reviewer respect.

**Content:**
- Brief methodology: the CC-7 multi-tool verification stack (Wolfram + SymPy + mpmath + Python).
- **The four largest corrections the verification retrofit surfaced:**
  1. **D1 Hawking temperature:** pre-audit `plausibility.md` had $T_H \approx 6 \times 10^{-7}$ K (far below CMB); verification re-derivation gave $T_H \approx 1.2 \times 10^6$ K (far above CMB). 12-orders-of-magnitude error. Observational conclusion (asteroid-mass PBHs hidden at cosmic distances) survives via corrected mechanism (negligible luminosity from tiny Schwarzschild surface), but the original physical reasoning was wrong.
  2. **R3 gradient:** plausibility had $2 \times 10^{-8}$ m/s² for the required cosmological potential gradient; correct is $cH_0 \approx 6.8 \times 10^{-10}$ m/s² — 30× error. Surfaced the MOND $a_0$ proximity coincidence as downstream side-result.
  3. **R1 labelling and parameters:** $n_g$ corrected $10^{106} \to 2.8 \times 10^{104}$; $\sigma_g$ corrected $10^{-133} \to 8 \times 10^{-132}$; Hubble-vs-observable convention made explicit.
  4. **L1 photon mass bound margin:** claim said "4 orders below Wang bound"; actual is 3.57 orders — 0.43-OOM overstatement. PDG margin is thin (~1.78×) — live-check before submission.
- **Toolchain bugs caught:** Wolfram `Solve` silently returning `{}` on over-constrained systems (caught twice: L3, R6); mpmath binary-precision rounding 5σ to print as 3σ; Mathematica underscore-as-pattern-delimiter silent assignment failures.
- Honest caveat: the verification stack is excellent at catching arithmetic and transcription errors. It does not validate the underlying physical premises fed to the symbolic algebra — several "green-tier" verifications (E7, M3, Q2, Q3, S5.5(a)) reduce to "two CAS tools confirming standard math." The ledger separates "computational checks" from "physics-content tier" to track this distinction.
- Pointer to `theory/claims/<CLAIM_ID>/verification/` subfolders for full check scripts and outputs.

**Framing language:** "the verification caught real errors," "cross-tool agreement is necessary but not sufficient," "computational check vs. physics-content check."

---

### §11 — Research Program and Open Questions (~1 page)

**Content:**
- Brief: the program is a research program, not a finished theory.
- The named open questions (from `research/open-questions.md`):
  - OQ-1: quantitative redshift law (R-menu commitment + empirical fits)
  - OQ-2: max packing density / $\rho_{bound}$
  - OQ-3: derive $c$ from graviton dynamics
  - OQ-4: vacuum graviton density
  - OQ-R1-α, OQ-R2-μ(z), OQ-R2-ISW, OQ-R6-photon-model, OQ-D1-halo-profile, OQ-D1-PBH-mass-function, OQ-cosmology-early, OQ-R3-anisotropy, OQ-R5-mechanism
  - UNSPEC-1 through UNSPEC-5
- Each OQ has a "what would close it" criterion in the source file; paper gives one-line summary + pointer.
- Experimental program: what observations would distinguish GCM from mainstream physics? (Mostly thin at this stage; name what would help.)

---

### §12 — Conclusion (~0.5 page)

**Content:**
- One paragraph: restate what the paper claims (coherence) and what it does not (proof, derivation).
- One paragraph: why the framework is worth engaging with despite being research-program-stage.
- One paragraph: invitation to engagement — the claims/ subfolders are available for audit; the open questions are available for collaboration.

**Last sentence:** something like *"GCM is not yet a theory. It is a research program whose internal consistency we have tried to establish honestly, whose structural challenges we have named concretely, and whose open questions we believe are worth the work."*

---

## Citation pass checklist (before submission)

- [ ] Seifert et al. 2025 MNRAS Letters 537 L55 (Wiltshire timescape, ln B > 5)
- [ ] Wang 2023 FRB photon-mass bound (primary paper, current value)
- [ ] PDG 2022 photon mass bound (or most recent) — live-check
- [ ] DES 2024 SNe Ia time-dilation measurement $(1+z)^{1.003 \pm 0.005}$
- [ ] DESI DR2 (2025) evolving $w(z)$ at 2.8-4.2σ
- [ ] Profumo PBH-as-DM program (recent paper; UCSC)
- [ ] 't Hooft 2016, *Cellular Automaton Interpretation of QM*
- [ ] Hossenfelder 2020+ superdeterminism defense
- [ ] Verlinde 2017 entropic gravity
- [ ] Padmanabhan emergent gravity
- [ ] Hales 2005 Kepler conjecture proof (for Q2 citation)
- [ ] Conway-Sloane (sphere packings) + Mackay 1962 (icosahedral shells) for Q2
- [ ] OEIS A005901 for shell formula
- [ ] Robertson 1949 for SR consistency framing (S5.5(b))
- [ ] Milgrom 1983 for MOND $a_0$ (R3 side-note)
- [ ] Jacobson 1995 for gravity-not-fundamental lineage
- [ ] Standard Bohr model reference for L1, Q3, E7

Research pass: use `research/findings/literature_report.md` as starting point; spawn research subagents to fill gaps if any citation is unverified.

---

## Pre-submission task list

1. ✅ **Audit complete** (2026-04-24)
2. 🔲 **Update claim folders for DEFER/EXCLUDE/RETHINK items** with `future-work.md` notes (in-progress today)
3. 🔲 **Update ledger** with pointer to audit + new columns proposal
4. 🔲 **Draft paper sections §1–§12** using this plan
5. 🔲 **Citation pass** (live-check each citation; verify Wang 2023, PDG current, DES 2024, Seifert 2025)
6. 🔲 **Sentence-level prose audit** — every "GCM derives X" → "GCM is consistent with X" / "GCM proposes a structure such that X would follow if Y." No word "unifies" in cluster titles or claims.
7. 🔲 **Pre-submission `/debate --adversarial`** on the L3 → R6 cascade (optional but recommended)
8. 🔲 **Re-tally S1-AX-1-F** as 3 substantive + 1 Lean stub + 1 TODO
9. 🔲 **Final read-through** for CC-5 7-item passes criterion:
   - [ ] Four tenets stated cleanly
   - [ ] Five green-tier formal pieces (§3: L1, L2, L3, M1, Q2)
   - [ ] One R mechanism committed (§6: R2 primary; R6 companion)
   - [ ] One unification *scaffold* argued concretely (§4: E1; §8 names gaps)
   - [ ] Structural challenges named (§8)
   - [ ] ≥3 positioning paragraphs (§9)
   - [ ] No overclaim — prose audited

---

## Length budget

| Section | Target |
|---------|--------|
| §1 Introduction | 1 page |
| §2 Ontological Foundations | 2 pages |
| §3 Structural Scaffolds | 3 pages |
| §4 Substrate Compatibility (E1 scaffold) | 1 page |
| §5 Quantum Structure | 1 page |
| §6 Cosmology + Dark Sector | 3-4 pages |
| §7 Magnetism and Thermodynamics | 1 page |
| §8 Structural Challenges ⭐ | 2 pages |
| §9 Literature Positioning | 1-2 pages |
| §10 Verification Methodology + Errors Caught ⭐ | 1-2 pages |
| §11 Research Program + Open Questions | 1 page |
| §12 Conclusion | 0.5 page |
| **Total** | **17-21 pages** |

If length pressure forces cut: §7 (magnetism/thermo) → ½ page; §9 (positioning) → 1 page; §11 (open questions) → can reference source file inline and drop its own section.

**Do not cut:** §8 (structural challenges) or §10 (errors caught). Those are the paper's distinguishers.

---

## Writing order recommendation

Don't write §1 first. Write in this order:
1. **§8 Structural Challenges** — because this is the paper's strongest section; writing it first anchors the honest-framing voice.
2. **§2 Ontological Foundations** — the philosophical spine.
3. **§3 Structural Scaffolds** — the five math pieces.
4. **§6 Cosmology** — the heaviest technical section.
5. **§10 Verification Methodology + Errors Caught** — distills what the verification did.
6. **§4, §5, §7** — the shorter technical sections.
7. **§9 Literature Positioning** — needs the rest to anchor.
8. **§11, §12** — summary and open questions.
9. **§1 Introduction** — written last so it accurately describes what follows.

---

## What this plan is NOT

- Not the paper itself. The paper is still to be drafted.
- Not a commitment to every section — length pressure may force cuts.
- Not a verification audit — that's `theory/claims/audit-2026-04-24.md`.
- Not a substitute for sentence-level prose discipline. The framing risk lives in chapter-level claims; per-section writing must hold the line.

---

*Companion documents:*
- `theory/claims/audit-2026-04-24.md` — the per-claim audit that informs this plan
- `theory/claims/ledger.md` — the verification status record
- `research/open-questions.md` — the named OQs
- `research/findings/literature_report.md` — existing literature coverage
- `research/findings/consistency_report.md` — early consistency audit (H6, H7, LIGO bound fixes)
- `concept-paper/2026-04-23-gdgm-concept.md` — the Gravitationalism-umbrella concept document (different audience)
