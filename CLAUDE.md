# GDGM — Graviton Density Gradient Mechanics

## Overview
Unified physics theory project attempting to derive all fundamental forces from gravity (graviton density gradients). Part of the broader Gravitationalist philosophical framework.

## Development Phases
1. **Philosophical framework** (current) — Establishing conceptual foundations
2. **Theoretical document** — Mathematical formalization
3. **Publishable paper** — Academic-ready version

## Project Structure
```
GCM/
├── CLAUDE.md                    # This file
├── GDGM.code-workspace         # VSCode workspace
├── test_smoke.py                # Smoke tests (syntax, functions, energy, clusters)
└── gdgm/
    ├── README.md                # Comprehensive project guide
    ├── roadmap.md               # Phase-by-phase development plan
    ├── theory/
    │   ├── core_tenets.md       # Foundational principles
    │   ├── source_notes.md      # Notes from physics literature
    │   ├── derivation_sketch.md # Mathematical derivation attempts
    │   ├── minimal_model.md     # Simplest testable version
    │   └── versions/
    │       └── gdgm_v2.md       # Version 2 of the theory document
    ├── agents/
    │   ├── agent_structure.md   # How agent team is organized
    │   └── prompts/
    │       ├── literature_scout.md     # Searches for relevant papers
    │       └── consistency_auditor.md  # Checks internal consistency
    ├── findings/
    │   ├── literature_report.md  # Agent output: literature survey (~20KB)
    │   └── consistency_report.md # Agent output: consistency analysis (~8KB)
    └── simulation/
        └── gdgm_nbody.py        # N-body simulation (Python, ~10KB)
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
- `simulation/gdgm_nbody.py` — Python N-body simulation implementing graviton density gradient mechanics
- Run with: `python3 gdgm/simulation/gdgm_nbody.py`
- No external dependencies declared yet (likely needs numpy — check imports before running)

## Tests
- Smoke tests: `python3 -m pytest test_smoke.py -v` (or `python3 test_smoke.py -v`)
- Tests validate: syntax, core function shapes/outputs, energy conservation, cluster detection, requirements.txt
- Tests extract functions from the simulation file without running the full simulation
- Dependencies: numpy (same as simulation)

## Working Conventions
- Distinguish clearly between philosophical intuition and mathematical claim
- All assertions must eventually map to testable predictions
- Use standard physics notation where applicable
- Reference existing literature honestly — note where GDGM agrees and diverges
- The Gravitationalist Ethos provides philosophical motivation but is separate from the physics

## Verification
- Run Consistency Auditor agent after any theory changes
- Check `findings/consistency_report.md` for unresolved issues
- Cross-reference claims against `theory/source_notes.md`
- Simulation output should be sanity-checked against known gravitational behavior

## Gotchas
- This is speculative theoretical work — maintain intellectual honesty about what is established vs. conjectured
- Engage with counterarguments seriously, don't dismiss them
- Phase 1 focus: get the philosophical framing right before attempting rigorous math
- The `gdgm/` subdirectory contains all the real work — root level is just workspace config
- Literature report is large (~20KB) — search within it rather than reading entirely
