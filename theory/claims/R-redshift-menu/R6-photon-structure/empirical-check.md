# R6 — Empirical Check

R6 is a time-dilation companion mechanism, not a standalone redshift mechanism. Most of the seven empirical constraints don't apply directly to R6. Where they do, the evaluation is below.

## 1. SNe Ia Light-Curve Time Dilation — $(1+z)^{1.003 \pm 0.005}$

**Severity:** ⭐⭐⭐⭐⭐ Highest — this is R6's central test.

**R6 prediction:** Exact $(1+z)$ scaling, i.e., exponent = 1.

**Measurement:** DES 2024, exponent = 1.003 ± 0.005 (stat) ± 0.010 (sys).

**Consistency:** exponent = 1.000 falls within 1σ of the measurement. R6's prediction is empirically indistinguishable from the data at current precision.

**Comparison to alternatives:**
- Classical tired light: predicts exponent = 0. Ruled out at ~200σ.
- Timescape: predicts exponent = 1 via metric structure. Consistent.
- $\Lambda$CDM: predicts exponent = 1 via cosmological expansion. Consistent.

R6 gives the same prediction as timescape and $\Lambda$CDM — which is the point. This is the prediction the data demands; R6 is the GCM way of producing it.

**Status:** 🟢 Consistent with data.

## 2. ISW Effect

**Severity:** ⭐⭐⭐⭐ High.

R6 is not a cosmological-scale mechanism; it operates at the photon-internal scale. It does not produce an ISW signal. It is silent on the observed ISW signal — which is the responsibility of the primary redshift mechanism (R1–R5) paired with R6.

**Status:** 🟢 Not applicable.

## 3. BAO

**Severity:** ⭐⭐⭐⭐ High.

R6 does not affect BAO. The 150 Mpc acoustic scale is set by early-universe physics, and R6 is about photon-internal structure during transit. BAO is the responsibility of the primary redshift mechanism.

**Status:** 🟢 Not applicable.

## 4. BBN

**Severity:** ⭐⭐⭐ Medium-high.

Not applicable. R6 is not a statement about early-universe conditions.

**Status:** 🟢 Not applicable.

## 5. CMB Blackbody Spectrum

**Severity:** ⭐⭐⭐ Medium-high.

R6 scales temporal structure uniformly by $(1+z)$. If applied to a blackbody photon population, this is the same as a temperature shift $T \to T/(1+z)$ — the same shape transformation as adiabatic cooling. Blackbody shape is preserved.

**Status:** 🟢 Preserves blackbody.

## 6. Tolman Surface Brightness

**Severity:** ⭐⭐ Medium.

R6's time-dilation contributes $(1+z)^{-1}$ to the surface-brightness scaling (fewer photon "ticks" per observer-frame second). The full $(1+z)^{-4}$ decomposition requires additional factors from the primary redshift mechanism.

**Status:** 🟢 Contributes the time-dilation piece of the Tolman law correctly.

## 7. DESI DR2 — Weakening Dark Energy

**Severity:** ⭐ Low-medium.

Not applicable. R6 is not a statement about dark energy.

**Status:** 🟢 Not applicable.

## Summary Table

| Constraint | R6 |
|---|---|
| SNe Ia time dilation | 🟢 Exact $(1+z)$ prediction; consistent with DES 2024 |
| ISW | 🟢 Not applicable (photon-internal, not cosmological) |
| BAO | 🟢 Not applicable |
| BBN | 🟢 Not applicable |
| CMB blackbody | 🟢 Preserved (uniform time scaling) |
| Tolman | 🟢 Contributes the $(1+z)^{-1}$ time-dilation factor correctly |
| DESI DR2 | 🟢 Not applicable |

## The Honest Picture

R6 is clean on every empirical check that applies to it. The reason R6 is yellow rather than green overall is *not* empirical — it is formal. The cascade argument is a plausibility argument, not a derivation. A rigorous derivation would require:

- Specific model of photon internal graviton-cluster structure.
- Derivation of internal-information-propagation time from first principles.
- Check that $v_{\text{int}}$ is indeed substrate-independent at the precision relevant for cosmological measurements.

None of this has been done. The structural argument is consistent with the data, but the theoretical framework supporting the argument is not yet rigorous.

## Session E Dependency (Honest Flag)

The plan-coherence-case.md Session E is intended to produce a rigorous R6 treatment. This brief was written from the S5 specification in the plan, not from a Session E output. When Session E runs, the R6 brief should be updated or replaced with the rigorous version.

Current status (this brief): structural argument reproduced from plan; empirical checks pass; formal derivation pending.
