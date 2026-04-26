# R-redshift-menu Reconciliation Punch-List

**Created:** 2026-04-24
**Trigger:** Session G verification retrofit caught 6 specific numerical errors + 1 chronicle error. Findings are tracked per-claim in `verification.md` and centrally in `theory/claims/ledger.md`; this file consolidates what still needs to be *applied* to the source markdown.

**Status codes:**
- ⬜ pending — finding surfaced, fix not yet applied
- 🔧 in-progress — fix being applied this session
- ✅ done — fix applied and checked into markdown
- ⏸️ needs-user — waiting on Wisdom's judgment call

**Pass 1 reconciliation completed 2026-04-24 16:00 PDT.** All items below marked ✅ have been applied. One item (X.1 plan-coherence-case.md S6) turned out to be unnecessary — the plan already had the correct 10^25 number; the "10^18" error was only in the 2026-04-23 chronicle entry. Convention flag at the bottom is still waiting on Wisdom's confirmation.

**Convention choice up front (autonomous default):** Observable-universe radius ($R_{\text{obs}} = 4.4 \times 10^{26}$ m, the particle horizon) rather than Hubble radius ($c/H_0 = 1.32 \times 10^{26}$ m). Reason: the number 4.4e26 is baked into R1, R2, and the M3 graviton-count claim, and it matches the physical intent (observed SNe Ia extend to the observable-universe scale, not just the Hubble-radius scale). Flipping to the Hubble convention would require edits in more places and shrink several claims by factor 3.3 with no physics gain. **Flagged for Wisdom's confirmation.** If he prefers Hubble convention, the edits below flip trivially.

---

## R1 — Space Friction

### ✅ R1.1 Relabel 4.4e26 m as "observable universe radius" (not Hubble radius)
- **File:** `R1-space-friction/plausibility.md`
- **Current:** "For $z \sim 1$ at distances of order the Hubble radius $R_H \approx 4.4 \times 10^{26}$ m"
- **Replace with:** "For $z \sim 1$ at distances of order the observable-universe radius $R_{\text{obs}} \approx 4.4 \times 10^{26}$ m (the particle horizon; $c/H_0 = 1.32 \times 10^{26}$ m is the Hubble radius, a factor 3.3 smaller)"
- **Source:** `R1-space-friction/verification/check_01_hubble_radius_and_alpha.py` + `.wls`

### ✅ R1.2 Relabel α framing — "inverse observable-universe length" not "H_0/c"
- **File:** `R1-space-friction/plausibility.md` + `claim.md`
- **Current (plausibility):** "$\alpha \sim H_0/c \approx 2.3 \times 10^{-27}$ m⁻¹"
- **Replace with:** "$\alpha \sim 1/R_{\text{obs}} \approx 2.3 \times 10^{-27}$ m⁻¹. Note: $H_0/c = 7.57 \times 10^{-27}$ m⁻¹ is a different quantity, a factor of 3.3 larger; any Hubble-law fit to data at moderate $z$ will distinguish these."
- **Source:** same check as R1.1

### ✅ R1.3 Correct n_g (10^104, not 10^106)
- **File:** `R1-space-friction/plausibility.md`
- **Current:** "$n_g \sim 10^{185} / V_{\text{universe}} \approx 10^{106}$ m⁻³"
- **Replace with:** "$n_g \sim 10^{185} / V_{\text{obs}} \approx 2.8 \times 10^{104}$ m⁻³" (with $V_{\text{obs}} = (4/3)\pi R_{\text{obs}}^3 \approx 3.57 \times 10^{80}$ m³)
- **Source:** `R1-space-friction/verification/check_02_graviton_density_and_cross_section.py` + `.wls`

### ✅ R1.4 Correct σ_g back-solve (~10^-131, not 10^-133)
- **File:** `R1-space-friction/plausibility.md`
- **Current:** "$\sigma_g$ would need to be of order $10^{-133}$ m² per graviton"
- **Replace with:** "$\sigma_g \sim \alpha / n_g \approx 8 \times 10^{-132}$ m² per graviton (using the corrected $\alpha = 2.3 \times 10^{-27}$ m⁻¹ and $n_g = 2.8 \times 10^{104}$ m⁻³)"
- **Source:** same check as R1.3

---

## R2 — Void Decompression

### ✅ R2.1 Relabel H_0/c to match R1's convention
- **File:** `R2-void-decompression/plausibility.md`
- **Current:** "the required fractional wavelength growth per unit distance is $\frac{1}{\lambda} \frac{d\lambda}{dr} \sim \frac{H_0}{c} \approx 2.3 \times 10^{-27}$ m⁻¹"
- **Replace with:** "the required fractional wavelength growth per unit distance is $\sim 1/R_{\text{obs}} \approx 2.3 \times 10^{-27}$ m⁻¹ at the observable-universe scale. (Equivalently this is of order $H_0/c = 7.57 \times 10^{-27}$ m⁻¹ at the Hubble-radius scale; the two differ by a factor of 3.3 depending on which cosmological length is used.)"
- **Source:** inherits R1 check_01

---

## R3 — Non-Central Position

### ✅ R3.1 Correct gradient value (6.8e-10, not 2e-8)
- **File:** `R3-non-central/plausibility.md` + `claim.md`
- **Current (plausibility):** "$\frac{d\Phi}{dr} \sim c \cdot H_0 \approx 2 \times 10^{-8}$ m/s²"
- **Current (claim.md):** "the cosmological potential gradient must be: $\frac{d\Phi}{dr} \sim c \cdot H_0 \approx 2 \times 10^{-8}$ m/s²"
- **Replace with (both):** "$\frac{d\Phi}{dr} \sim c H_0 \approx 6.8 \times 10^{-10}$ m/s² (at $H_0 = 70$ km/s/Mpc). Suggestively, this is within a factor ~5 of the MOND acceleration scale $a_0 \sim 1.2 \times 10^{-10}$ m/s² (Milgrom 1983), a coincidence known in the modified-gravity literature. This suggests possible overlap between R3's required anisotropy and MOND-scale phenomenology, worth exploring if R3 is developed further."
- **Source:** `R3-non-central/verification/check_01_gradient_magnitude.py` + `.wls`

---

## D1 — No Dark Matter

### ✅ D1.1 Rewrite Hawking-temperature paragraph (high T, not low T)
- **File:** `D1-no-dark-matter/plausibility.md`
- **Current:** "Hawking radiation: Hawking temperature for a $10^{20}$ g PBH is $T_H \sim 10^{-5}$ K, far below CMB (2.725 K). Hawking radiation is undetectable."
- **Replace with:** "Hawking radiation: at $M = 10^{17}$ kg, Hawking temperature is actually $T_H \approx 1.2 \times 10^6$ K — a million Kelvin, far above CMB. But the Schwarzschild radius is only $r_s = 2GM/c^2 \approx 1.5 \times 10^{-10}$ m (atomic scale), so emitting area is $\sim 10^{-19}$ m² and Stefan-Boltzmann luminosity is only $\sim 36$ mW per PBH. At cosmic inter-PBH spacing (~2000 AU) and given the rarity of close encounters, this radiation is entirely undetectable. Asteroid-mass PBHs are observationally hidden by negligible luminosity, not by low temperature."
- **Source:** `D1-no-dark-matter/verification/check_03_hawking_temperature.py` + `.wls`

### ✅ D1.2 Soften "emit no light of their own" in claim.md
- **File:** `D1-no-dark-matter/claim.md`
- **Current:** "they emit no light of their own (asteroid-mass PBHs emit Hawking radiation at $T_H \approx 6 \times 10^{-7}$ K, far below the CMB)"
- **Replace with:** "they emit negligible detectable radiation at any plausible observer distance (Hawking $T_H \approx 10^6$ K at $10^{17}$ kg, but Schwarzschild radius $\sim 10^{-10}$ m gives total Hawking luminosity $\sim 36$ mW per PBH — undetectable at cosmic distances)"
- **Source:** same check as D1.1

---

## Cross-Cutting — "10^18 PBHs" Error

This error was in my 2026-04-23 chronicle/summary text. claim.md was always correct at 10²⁵. Fix wherever the wrong number leaked:

### ✅ X.1 plan-coherence-case.md S6 Session G Results — **ALREADY CORRECT**
- **File:** `GCM/plan-coherence-case.md` lines 675 and 691
- **Verified 2026-04-24 16:00:** plan already has "$\sim 10^{25}$ asteroid-mass PBHs" — no edit needed. The "10^18" error was only in my chronicle summary, not in the plan.

### ✅ X.2 Fix chronicle 2026-04-23 Session G summary entry
- **File:** `GCM/chronicle/2026-04-23.md`
- **Current:** "~10^18 asteroid-mass PBHs in Milky Way halo at 10^20 g"
- **Replace with:** Not overwriting past entry (speech preservation principle) — instead add a correction marker at the end of the 2026-04-23 chronicle pointing to today's retrofit finding.

---

## Ledger Updates After Fixes Applied

Once the above fixes land, ledger rows should reflect the updated tally:

- **R1:** stays amber (fixes close 2 INCONCLUSIVE, but structural TODO about deriving α from GCM dynamics is still open; no change in tier).
- **R2:** stays amber (single-check row unaffected by R1 relabel; R2 still lacks its own GCM-specific quantitative fit).
- **R3:** stays red (gradient number fix doesn't close the undetected-anisotropy gap, which is the reason for red).
- **D1:** fixes close 1 FAIL → tally moves from 2/3 to 3/3, status can move amber→green (**within D1's scope**; doesn't change tier from yellow).

---

## What's NOT Getting Fixed In This Pass

- **Wolfram MCP installation** — infrastructure change, not a markdown edit. Needs update-config skill invocation; flagged separately.
- **GCM venv with sympy/mpmath/numpy** — same, infrastructure. Python 3.14 system has none of these.
- **Quantitative $\mu(z)$ fits, ISW shape predictions, GCM early-universe physics** — not in Session G scope at all; these are Session J+ or future papers.

---

## Convention Flag — RESOLVED 2026-04-24

✅ **Locked in: observable-universe convention.** Wisdom (2026-04-24): "I don't really have a preference either way, so you can just leave it." Default applied in the Pass 1 reconciliation is the final choice. Both conventions remain explicitly named in `plausibility.md` so physicist readers aren't surprised.

Reason for the default: $4.4 \times 10^{26}$ m (observable universe radius / particle horizon) was already baked into R1, R2, and M3; matches the physical intent of mechanisms acting over the full light-travel distance; requires fewer downstream edits. Both are legitimate cosmological length scales — the observable-universe one is what R1/R2 implicitly use.

## Infrastructure TODOs — RESOLVED 2026-04-24

✅ **Wolfram MCP install:** dropped. `wolframscript` local install worked for all symbolic/numeric work needed. Wisdom (2026-04-24): "we don't need the MCP because we were able to use Wolfram." Local `wolframscript` is the established tool going forward.

## Deep Research Gaps — FILED as future research 2026-04-24

The structural open questions surfaced during verification (derive α from GCM dynamics, GCM-specific $\mu(z)$ fit, ISW shape prediction, GCM early-universe physics, halo profile derivation, etc.) are not coherence-paper blockers. Filed to `research/open-questions.md` as OQ-R1-α, OQ-R2-μ(z), OQ-R2-ISW, OQ-R6-photon-model, OQ-D1-halo-profile, OQ-D1-PBH-mass-function, OQ-cosmology-early, OQ-R3-anisotropy, OQ-R5-mechanism, OQ-tooling-1. Wisdom (2026-04-24): "those deep gaps — let's just store those as future research."

---

**Reconciliation status: ✅ CLOSED 2026-04-24.** All pass-1 items done. Convention chosen. Infrastructure TODOs closed. Deep gaps filed as future research. Verification stacks, ledger rows, source markdown, and chronicles are now internally consistent.
