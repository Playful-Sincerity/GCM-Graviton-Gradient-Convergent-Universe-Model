# GCM — Graviton Gradient Convergent Universe Model

## Overview
Unified physics theory project attempting to derive all fundamental forces from gravity (graviton density gradients). The physics half of **Gravitationalism**; the philosophical/ethos half lives at `../Spiritual Ethos/`.

## Development Phases
1. **Philosophical framework** (current) — Establishing conceptual foundations
2. **Theoretical document** — Mathematical formalization
3. **Publishable paper** — Academic-ready version

## Project Structure
```
GCM/
├── CLAUDE.md                    # This file
├── README.md                    # Comprehensive project guide (human-facing)
├── GCM.code-workspace           # VSCode workspace
├── roadmap.md                   # Phase-by-phase development plan
├── requirements.txt             # Python dependencies
├── test_smoke.py                # Smoke tests (syntax, functions, energy, clusters)
├── theory/
│   ├── core_tenets.md           # Foundational principles
│   ├── source_notes.md          # Notes from physics literature
│   ├── derivation_sketch.md     # Mathematical derivation attempts
│   ├── minimal_model.md         # Simplest testable version
│   ├── overview.md              # Plain-language overview
│   └── versions/
│       └── gcm_v2.md            # Version 2 of the theory document
├── agents/
│   ├── agent_structure.md       # How the agent team is organized
│   └── prompts/
│       ├── literature_scout.md
│       └── consistency_auditor.md
├── simulation/
│   └── gcm_nbody.py             # N-body simulation (Python, ~10KB)
├── research/
│   ├── open-questions.md
│   └── findings/                # Agent outputs
│       ├── literature_report.md # Literature survey (~20KB)
│       └── consistency_report.md
├── debates/                     # Framework debates
│   └── 2026-04-03-gcm-framework/  # PRO vs CON × 3 rounds + Opus synthesis
├── chronicle/                   # Daily semantic log
├── ideas/                       # Captures, build queue
├── outreach/                    # Outreach-related material
├── play/                        # Exploration outputs
└── archive/                     # Deprecated material (includes rename record)
```

## Key Concepts
- Graviton density gradients as the unified field mechanism
- Emergence of electromagnetic, strong, and weak forces from gravitational substrate
- Connection to dark matter/dark energy phenomena
- Space itself as a graviton medium with varying density

## Agent Team
Two research agents support the theory development:
- **Literature Scout** (`agents/prompts/literature_scout.md`) — Searches for relevant papers, prior art, and potential connections
- **Consistency Auditor** (`agents/prompts/consistency_auditor.md`) — Reviews the theory for internal contradictions and logical gaps

## Simulation
- `simulation/gcm_nbody.py` — Python N-body simulation implementing graviton density gradient mechanics
- Run with: `python3 simulation/gcm_nbody.py`
- Dependencies: numpy (see `requirements.txt`)

## Tests
- Smoke tests: `python3 -m pytest test_smoke.py -v` (or `python3 test_smoke.py -v`)
- Tests validate: syntax, core function shapes/outputs, energy conservation, cluster detection, requirements.txt
- Tests extract functions from the simulation file without running the full simulation
- Dependencies: numpy (same as simulation)

## Working Conventions
- Distinguish clearly between philosophical intuition and mathematical claim
- All assertions must eventually map to testable predictions
- Use standard physics notation where applicable
- Reference existing literature honestly — note where GCM agrees and diverges
- The Gravitationalist Ethos (`../Spiritual Ethos/`) provides philosophical motivation but is separate from the physics — don't conflate them
- **Speed of light ≠ speed of causality.** Never write, say, or imply that light moves at $c$ in a GCM context. $c$ is the causality limit; photons move at $v = c - 0_x$ (IVNA indexed infinitesimal, energy-dependent), strictly less than $c$. This is load-bearing for GCM's claim that the photon is massive. See [`theory/speed-of-causality-principle.md`](theory/speed-of-causality-principle.md) for the full convention.

## Verification
- Run Consistency Auditor agent after any theory changes
- Check `research/findings/consistency_report.md` for unresolved issues
- Cross-reference claims against `theory/source_notes.md`
- Simulation output should be sanity-checked against known gravitational behavior

## Gotchas
- This is speculative theoretical work — maintain intellectual honesty about what is established vs. conjectured
- Engage with counterarguments seriously, don't dismiss them
- Phase 1 focus: get the philosophical framing right before attempting rigorous math
- Literature report is large (~20KB) — search within it rather than reading entirely
- Project was renamed from GDGM on 2026-04-21; see `archive/old-gdgm-naming.md` for context
