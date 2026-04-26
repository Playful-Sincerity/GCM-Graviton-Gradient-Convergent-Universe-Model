# R1 — Empirical Check

Evaluation of R1 (space friction) against the seven empirical constraints from `research/sources/2026-04-23-redshift-empirics.md`. R6 companion assumed where time dilation is required.

## 1. SNe Ia Light-Curve Time Dilation — $(1+z)^{1.003 \pm 0.005}$

**Severity:** ⭐⭐⭐⭐⭐ Highest.

**R1 alone:** FAILS. Classical tired light predicts zero time dilation; ruled out at ~200σ by DES 2024 (arXiv:2406.05050).

**R1 + R6:** Survives if the R6 cascade (wavelength $\propto (1+z)$ → internal spacing $\propto \lambda$ → time dilation $\propto$ spacing) holds structurally. R6 is the load-bearer for this test, not R1.

**Status:** Contingent on R6.

## 2. ISW Effect and Void Growth

**Severity:** ⭐⭐⭐⭐ High.

R1 does not require void growth. Friction happens in any graviton substrate regardless of whether structure is evolving. R1 is consistent with static potentials and therefore does not *produce* a dark-energy-like ISW signal.

However, R1 does not *explain* the observed ISW signal either. In ΛCDM, the observed ISW cross-correlation is positive and significant; in R1 alone, it should be zero. This is a tension in a different direction from R2: not "my mechanism produces an unwanted signal" but "my mechanism is silent on an observed signal that needs an explanation."

**Status:** 🟡 No direct tension, but leaves an observed signal unexplained.

## 3. BAO — 150 Mpc Acoustic Standard Ruler

**Severity:** ⭐⭐⭐⭐ High.

BAO relies on early-universe sound-crossing physics plus later-universe distance measurements. R1 changes the distance-redshift relation (via $\alpha$) but does not change early-universe physics. The sound horizon at recombination is fixed.

Whether R1 reproduces the same 150 Mpc peak at different observed redshifts depends on how $\alpha$ behaves over cosmic time. A constant $\alpha$ gives a specific distance law that must be tested against DESI DR2 BAO.

**Status:** 🔴 Not addressed — requires a quantitative R1 model fitted to BAO data. Open.

## 4. BBN — Primordial Nucleosynthesis

**Severity:** ⭐⭐⭐ Medium-high.

BBN depends on the expansion rate during the first ~20 minutes after the Big Bang (via neutron-proton freeze-out). R1 is a statement about photon propagation in the present substrate, not about early-universe dynamics. BBN requires a separate early-universe treatment in GCM.

**Status:** 🔴 Not addressed by R1 specifically. Open in the larger GCM cosmology.

## 5. CMB Blackbody Spectrum

**Severity:** ⭐⭐⭐ Medium-high.

**This is R1's most specific vulnerability.** Friction that couples photons to the graviton substrate is likely to be frequency-dependent in a way that would distort a blackbody spectrum over cosmological distances. A pure $dE/dr = -\alpha E$ friction (frequency-independent) preserves the blackbody shape — but it is unusual for a coupling to be exactly frequency-independent across 20+ decades of frequency.

COBE/FIRAS measured the CMB blackbody to a precision of ~50 parts per million. Any frequency-dependent friction would show up as a μ- or y-distortion at this level.

**Constraint on R1:** The coupling mechanism must be frequency-independent (or frequency-dependent in a way that exactly mimics adiabatic cooling) to this precision.

**Status:** 🔴 Serious tension unless the friction coefficient is demonstrably frequency-independent at FIRAS precision.

## 6. Tolman Surface Brightness

**Severity:** ⭐⭐ Medium.

Standard expansion predicts surface brightness $\propto (1+z)^{-4}$. A pure non-expansion R1 with no geometric distance dilution would give $(1+z)^{-1}$ (from redshift energy loss only). R1 + R6 adds time-dilation dimming, giving $(1+z)^{-2}$. Still short of $(1+z)^{-4}$.

This is a real discrepancy that R1 + R6 cannot hide. The available escape hatches are: (a) galaxy evolution corrections that make up the difference (debated in the literature), or (b) additional geometric effects from the GCM substrate.

**Status:** 🟡 Tension. Observationally debated because galaxy evolution corrections are large. Not a clean falsifier, but not supportive either.

## 7. DESI DR2 — Weakening Dark Energy

**Severity:** ⭐ Low-medium.

DESI DR2 (2025) shows mild evidence (2.8–4.2σ) for evolving $w(z)$, inconsistent with simple $\Lambda$CDM. Any non-expansion mechanism that eliminates dark energy is supportive here, including R1 + R6.

**Status:** 🟢 Supportive (not proof).

## Summary Table

| Constraint | R1 Alone | R1 + R6 |
|---|---|---|
| SNe Ia time dilation | Fails (tired light) | Contingent on R6 |
| ISW | No tension, unexplained signal | Same |
| BAO | Open | Open |
| BBN | Not addressed | Not addressed |
| CMB blackbody | Serious tension if frequency-dependent | Same |
| Tolman | Tension; $(1+z)^{-2}$ vs. $(1+z)^{-4}$ | Same |
| DESI DR2 | Supportive | Supportive |
