# R3 — Future Work / Paper-1 Status

**Paper-1 decision:** DEFER. One-paragraph menu mention in §6 only, explicitly red.
**Source:** `theory/claims/audit-2026-04-24.md` (R3 row).

## Current state (after 2026-04-24 reconciliation)

The verification retrofit caught a **30× gradient error** in plausibility.md: original claimed $2 \times 10^{-8}$ m/s² required gradient; correct value is $cH_0 \approx 6.8 \times 10^{-10}$ m/s². Corrected in `plausibility.md` and `claim.md`.

**Side-result worth preserving:** the corrected gradient is within ~5× of MOND's acceleration scale $a_0 \approx 1.2 \times 10^{-10}$ m/s² (Milgrom 1983). This is a genuine coincidence worth flagging, not a derivation.

R3 stays RED on empirical grounds: **no observed cosmological potential anisotropy matches the required gradient**. CMB anisotropies at $10^{-5}$ level (after dipole subtraction attributed to peculiar velocity) constrain R3 hard.

## Why it earns a menu mention despite being red

R3 has a unique virtue: **gravitational redshift automatically produces time dilation** (via GR equivalence principle), so R3 does not need an R6 companion. This makes R3 the one mechanism in the R-menu that avoids the R6-cascade dependency.

The MOND coincidence ($cH_0$ within 5× of $a_0$) is independently interesting and worth flagging for future work.

## What would promote R3 to INCLUDE

1. **Locate the convergence center.** R3's mechanism requires a specific cosmological gravitational anisotropy in a specific direction. GCM convergence dynamics should predict *where* the center is. Candidate observational hooks: Secrest et al. 2021 radio-galaxy-vs-CMB dipole misalignment at 4.9σ.
2. **Precision anisotropy test.** A targeted cosmological anisotropy measurement aligned with GCM's predicted direction. Would be distinguishable from standard isotropy at high precision.
3. **Connect MOND coincidence to a derivation.** If R3's required gradient naturally emerges at MOND scale, there might be a deeper substrate-gradient story. Current: coincidence, not mechanism.

## Where this lives going forward

- **Paper-1 §6:** one-paragraph menu mention — corrected gradient, MOND coincidence flagged, empirical status explicit.
- **Verification folder preserved:** the 30× correction is one of the audit's exemplary "verification caught a real error" cases.
- **Future work:** OQ-R3-anisotropy in `research/open-questions.md`.

## See
- `theory/claims/audit-2026-04-24.md` — R3 row
- `research/open-questions.md` — OQ-R3-anisotropy
- `plausibility.md` — corrected gradient derivation
- Milgrom 1983 for MOND $a_0$; Secrest et al. 2021 for dipole anisotropy
