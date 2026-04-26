# GCM — Graviton Gradient Convergent Universe Model

**Lead**: Wisdom Happy (乐恒智)
**Started**: 2026-03-21
**Goal**: Develop a fully rigorous, mathematically consistent, experimentally predictive unified physics theory from four core tenets.

The physics half of **Gravitationalism**. The philosophical/ethos half lives at `../Spiritual Ethos/`.

---

## Core Tenets

1. **One fundamental particle** — the graviton — composes all matter and energy.
2. **Gravity is the only fundamental force** — EM, Strong, and Weak are emergent manifestations of gravitational density gradient interactions at different scales.
3. **The universe is converging, not expanding** — current cosmological evidence (accelerating expansion) is being misinterpreted.
4. **All existence is dimensions of change** — space, time, matter, and energy are all configurations of and changes in the graviton substrate.

See `theory/core_tenets.md` for the full statement.

---

## Development Phases

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Philosophical framework — coherent conceptual system | In Progress |
| 2 | Theoretical document — self-consistent, claims derived | Not Started |
| 3 | Publishable academic paper — full math, prior literature, experiments | Not Started |

---

## Project Structure

```
GCM/
├── README.md                     ← this file
├── CLAUDE.md                     ← Claude context
├── roadmap.md                    ← phase-by-phase plan
├── requirements.txt              ← Python deps
├── test_smoke.py                 ← smoke tests
├── theory/
│   ├── core_tenets.md            ← the four axioms
│   ├── overview.md               ← plain-language overview
│   ├── minimal_model.md          ← simplest testable version
│   ├── derivation_sketch.md      ← math derivation attempts
│   ├── source_notes.md           ← notes from physics literature
│   └── versions/                 ← versioned drafts of the paper
├── agents/
│   ├── agent_structure.md        ← team design and roles
│   └── prompts/                  ← saved prompt for each agent
├── simulation/
│   └── gcm_nbody.py              ← N-body simulation
├── research/
│   ├── open-questions.md
│   └── findings/
│       ├── literature_report.md  ← output from Literature Scout
│       └── consistency_report.md ← output from Consistency Auditor
├── debates/
│   └── 2026-04-03-gcm-framework/ ← PRO/CON × 3 + Opus synthesis
├── chronicle/                    ← daily semantic log
├── ideas/                        ← captures, build queue
├── outreach/                     ← outreach material
├── play/                         ← exploration outputs
└── archive/                      ← deprecated material (incl. rename record)
```

---

## Navigation

- **What needs doing next?** → `roadmap.md`
- **Who are the agents and what do they do?** → `agents/agent_structure.md`
- **What has been found so far?** → `research/findings/`
- **Current theory state?** → `theory/versions/`
- **The ethos side of the project?** → `../Spiritual Ethos/`
