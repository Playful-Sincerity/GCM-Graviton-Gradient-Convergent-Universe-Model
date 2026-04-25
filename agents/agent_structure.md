# GDGM Agent Team Structure

## Philosophy

The development proceeds in waves. Each wave runs agents in parallel where possible,
then synthesizes before the next wave. No agent skips ahead of its dependencies.

---

## Wave 1 — Foundation (Current)

Run in parallel. Their outputs feed everything downstream.

### Agent 1: Literature Scout
**Role**: Map the existing landscape — what's been tried, what's ruled out, what's open
**Covers**: Preon theories, emergent gravity, force unification, cosmological expansion alternatives
**Output**: `findings/literature_report.md`
**Status**: Running (launched 2026-03-21)

### Agent 2: Consistency Auditor
**Role**: Go through the current GDGM paper (v1) and catalog every mathematical/logical issue
**Covers**: Dimensional analysis, circular reasoning, unsupported assertions, numerical errors
**Output**: `findings/consistency_report.md`
**Status**: Running (launched 2026-03-21)

---

## Wave 2 — Core Development (After Wave 1)

### Agent 3: Cosmology Architect
**Role**: Build the cosmological pillar — why universe is converging, reinterpret expansion evidence
**Dependencies**: Literature Scout findings (cosmology section)
**Output**: `theory/cosmology_framework.md`

### Agent 4: Particle Physics Architect
**Role**: Build the particle physics pillar — derive particle properties from graviton density gradients
**Dependencies**: Literature Scout findings (particle section), Consistency Auditor report
**Output**: `theory/particle_framework.md`

### Agent 5: Symmetry Problem Solver
**Role**: Attack the hardest problem: why do forces have different symmetries if one substrate?
**Dependencies**: Wave 1 complete
**Output**: `theory/symmetry_emergence.md`

---

## Wave 3 — Derivation and Validation

### Agent 6: Derivation Workshop
**Role**: Attempt to formally derive known results from GDGM math (Coulomb scaling, Bohr levels, Van der Waals)
**Dependencies**: Wave 2 complete

### Agent 7: Prediction Generator
**Role**: What does GDGM predict that differs from Standard Model + ΛCDM? Design experiments.
**Dependencies**: Wave 2 complete

---

## Wave 4 — Synthesis

### Agent 8: Paper Writer
**Role**: Synthesize all findings into a draft academic paper with full citations
**Dependencies**: Wave 3 complete

### Agent 9: Peer Critic
**Role**: Attack the paper from the perspective of a skeptical physicist. Find every hole.
**Dependencies**: Draft paper

---

## Coordination Log

| Date | Wave | Agent | Status | Notes |
|------|------|-------|--------|-------|
| 2026-03-21 | 1 | Literature Scout | **Complete** | findings/literature_report.md |
| 2026-03-21 | 1 | Consistency Auditor | **Complete** | findings/consistency_report.md |
| TBD | 2 | Cosmology Architect | Pending | Design redshift mechanism; align with Wiltshire/DESI |
| TBD | 2 | Particle Physics Architect | Pending | Derive charge, Pauli, magnetism from graviton field |
| TBD | 2 | Vacuum State Definer | Pending | Define baseline graviton density (OQ-4, foundational) |
