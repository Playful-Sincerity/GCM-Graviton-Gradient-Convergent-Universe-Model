# Open Questions — GCM

Living list of what the project doesn't know yet. Append-only, date-stamped.

---

## 2026-04-24 — Session G retrofit (cosmological redshift menu)

Surfaced during the verification retrofit for R1–R6 + D1–D2. Each is future research, not a coherence-paper blocker. Links to where the question was posed.

### OQ-R1-α — Derive space-friction coefficient α from GCM dynamics
- **Where posed:** `theory/claims/R-redshift-menu/R1-space-friction/status.md` "What Would Promote R1 to Green"
- **Question:** What is the first-principles GCM origin of the friction coefficient $\alpha$? At present, $\alpha \sim 1/R_{\text{obs}} \approx 2.3 \times 10^{-27}$ m⁻¹ is dimensionally fixable but structurally free. A real derivation would specify the per-graviton-encounter coupling (cross-section $\sigma_g$ and encounter rate $n_g v$) and recover $\alpha$ from the minimal-model equation of motion applied to a photon-cluster traversing a graviton substrate.
- **What would close it:** A GCM-derived $\alpha = f(\rho_g, m_g, \text{coupling mechanism})$ yielding the observed magnitude without fine-tuning, with frequency-independence at FIRAS precision (50 ppm) shown explicitly.

### OQ-R2-μ(z) — GCM-specific Pantheon+ fit for R2+R6
- **Where posed:** `theory/claims/R-redshift-menu/R2-void-decompression/status.md` "What Would Promote R2 to Green"
- **Question:** Can GCM's R2 (void decompression) + R6 (photon-structure time dilation) reproduce the Pantheon+ Hubble diagram quantitatively? Benchmark: Wiltshire timescape (Seifert et al. 2025 MNRAS Lett. 537, L55) achieves ln B > 5 over ΛCDM on 1,535 SNe Ia. Target: ln B > 1 over ΛCDM at minimum.
- **What would close it:** A specific GCM cosmology model producing $\mu(z)$, fitted to Pantheon+ with Bayesian evidence compared against ΛCDM and timescape.

### OQ-R2-ISW — Quantitative ISW shape in R2
- **Where posed:** `theory/claims/R-redshift-menu/R2-void-decompression/status.md` + plan S6
- **Question:** R2's position on the observed ISW signal is reinterpretation (graviton-density-gradient evolution, not $\Lambda$-driven decay). The signal exists; R2 owes a quantitative shape prediction that matches Planck ISW-Lensing + eBOSS cross-correlation data. Until this lands, R2's ISW story is a promise, not a derivation.
- **What would close it:** GCM-specific ISW signal computation for realistic void statistics; comparison to observed CMB-LSS cross-correlation.

### OQ-R6-photon-model — Concrete photon internal-structure model
- **Where posed:** `theory/claims/R-redshift-menu/R6-photon-structure/status.md` + S5 plan
- **Question:** R6's $(1+z)$ time-dilation cascade depends on two yellow-tier premises: (a) L3 linear wavelength-spacing correspondence, (b) substrate-independent internal-information-propagation speed. Both need a concrete photon internal-structure model to be rigorous — how many graviton clusters form a photon, their connectivity, their dynamics.
- **What would close it:** A specific GCM photon model from first principles, yielding L3 as a derivation (not assumption) and bounding $v_{\text{int}}$'s substrate-dependence.

### OQ-D1-halo-profile — GCM-derived galactic halo density profile
- **Where posed:** `theory/claims/R-redshift-menu/D1-no-dark-matter/status.md`
- **Question:** Observed rotation curves fit NFW or Einasto profiles. D1 claims halos are invisible ordinary matter (with asteroid-mass PBHs as a specific candidate). What does a GCM-derived halo density profile look like? Does it reproduce NFW at least to the accuracy of $\Lambda$CDM simulations?
- **What would close it:** A GCM structure-formation derivation producing halo profiles comparable to observed rotation curves.

### OQ-D1-PBH-mass-function — Why asteroid-mass specifically?
- **Where posed:** `theory/claims/R-redshift-menu/D1-no-dark-matter/status.md`
- **Question:** The asteroid-mass window (10¹⁷–10²³ g) is the least-constrained PBH region. D1 positions GCM against this window. Why would invisible ordinary matter in GCM concentrate at this mass scale rather than others? Is there a GCM-specific primordial-power-spectrum argument?
- **What would close it:** A derivation of the PBH mass-function peak from GCM's early-universe dynamics (or explicit acknowledgment that D1 is mass-agnostic and just needs the window to stay open empirically).

### OQ-cosmology-early — GCM early-universe physics
- **Where posed:** Multiple (R1, R2, D1, D2 all defer to it)
- **Question:** GCM's treatment of the early universe is unspecified. BAO requires a sound-horizon calculation; BBN requires a nucleosynthesis freeze-out calculation; CMB power spectrum requires acoustic-peak positions. All of these are currently "deferred to the broader GCM cosmology" — which doesn't exist yet.
- **What would close it:** A GCM early-universe model (convergence dynamics at $z \sim 10^8$–$10^{10}$) producing BAO sound horizon, BBN element abundances, CMB acoustic peaks consistent with observation.

### OQ-R3-anisotropy — Locate the convergence center
- **Where posed:** `theory/claims/R-redshift-menu/R3-non-central/status.md`
- **Question:** R3's mechanism requires a specific cosmological gravitational anisotropy in a specific direction with magnitude ~$6.8 \times 10^{-10}$ m/s² (within ~5× of MOND's $a_0$). Where is the convergence center? Does any observation (CMB dipole decomposition, Secrest et al. 2021 radio-galaxy-vs-CMB dipole 4.9σ misalignment) constrain or suggest a direction?
- **What would close it:** A GCM convergence-dynamics prediction for the current center position + comparison to observed anisotropy data.

### OQ-R5-mechanism — Microscopic mechanism for selection effect
- **Where posed:** `theory/claims/R-redshift-menu/R5-selection-effect/status.md`
- **Question:** R5 (Wisdom's "we're small" intuition) is structurally distinct from in-transit mechanisms but lacks a microscopic specification. Three candidates named in plausibility.md (gravitational-lensing bias, absorption-scattering bias, geometric-aperture bias) — none developed. Which is it, and what does it predict?
- **What would close it:** A specific $f(d, E)$ filter function derived from GCM dynamics with predictions distinguishable from R2 at current observational precision.

### OQ-tooling-1 — GCM venv with sympy/mpmath/numpy
- **Where posed:** `theory/claims/R-redshift-menu/R1/verification.md` TODO; this chronicle's 04:10 entry
- **Question:** Python 3.14.4 system has no `sympy` / `mpmath` / `numpy`. Verification scripts currently route symbolic work through Wolfram. A GCM-specific venv would enable Python-native verification. Needs update-config skill to set up.
- **What would close it:** `GCM/.venv/` with pinned sympy + mpmath + numpy versions, and a convention that verification scripts use it.

