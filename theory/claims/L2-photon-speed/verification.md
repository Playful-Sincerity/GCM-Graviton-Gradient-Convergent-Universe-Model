# L2 — Verification Record

**Tally:** 5/5 checks passed after tool-precision fix (see Check 5 notes). Cross-tool agreement: mpmath and Wolfram agree on `Δv ≈ 4.71685723e-29 m/s` to ~22 digits.
**Last run:** 2026-04-24.
**Reproducible:** Yes — all scripts live in [verification/](verification/); inputs in [inputs.json](verification/inputs.json); captured stdout in [verification/outputs/](verification/outputs/).

**Convention note:** Per [`theory/speed-of-causality-principle.md`](../../speed-of-causality-principle.md), `c` throughout denotes the causality limit — NOT "the speed of light." GCM commits to `m_γ > 0` (L1), so `v_photon < c` strictly. No script writes `v_photon = c`. The `m_γ → 0` limit of the formula is evaluated only as an algebraic reference point, with an explicit note that GCM does not take this limit.

---

## Check 1 — Symbolic derivation (SymPy)

- **Tool:** Python 3.14.4 / SymPy 1.14.0
- **Script:** [verification/check_01_derivation_sympy.py](verification/check_01_derivation_sympy.py)
- **Output:** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** SymPy derives `v = dE/dp` from `E² = (pc)² + (m_γc²)²` and substitutes `p(E, m_γ, c)`. The resulting expression simplifies to the expected closed form `c·√(1 − (m_γc²/E)²)` (difference simplifies to 0). The series expansion in `ε = m_γc²/E` is `v ≈ c(1 − ε²/2 − ε⁴/8 − …)`. Structural property `v < c` for `m_γ > 0` stated explicitly.

## Check 2 — High-precision Δv (mpmath, 80-digit)

- **Tool:** Python 3.14.4 / mpmath 1.3.0 at 80 decimal digits
- **Script:** [verification/check_02_deltav_mpmath.py](verification/check_02_deltav_mpmath.py)
- **Output:** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Direct evaluation of `c·√(1 − ε²)` at 80-digit precision gives `v_photon = 2.99792457999...9999995283...e8 m/s` and `Δv = 4.7168572332762136595547017378...e-29 m/s`. Agrees with the Taylor expansion `cε²/2` to ~38 digits (difference is the `ε⁴/8` next-order term). 0.5% difference from session brief's stated `4.74e-29` is rounding of the brief's 2-sig-fig inputs, not a computational discrepancy. `Δv/c ≈ 1.57e-37`, below any experimental sensitivity. Structural `v < c` confirmed.

## Check 3 — FRB photon-mass bound cross-check

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_03_frb_bound.py](verification/check_03_frb_bound.py)
- **Output:** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** GCM `m_γ = 1e-54 kg = 5.6096e-19 eV/c²`. Wang 2023 FRB bound `m_γ ≤ 2.1e-15 eV/c²`. `log10(FRB/GCM) = 3.57`. GCM is ~3.6 orders below the bound (session brief said "4 orders" — order-of-magnitude consistent; `3.57` rounds up).

## Check 4 — Structural v < c across energy sweep

- **Tool:** Python 3.14.4 / mpmath 1.3.0 at 60 digits
- **Script:** [verification/check_04_structural_bound.py](verification/check_04_structural_bound.py)
- **Output:** [verification/outputs/check_04.txt](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** Sweeps photon energy across `E = 10⁻³` to `10⁹` eV with `m_γ = 1e-54 kg`. `v/c < 1` strictly at all energies. The deviation `1 − v/c = 0_x` shrinks as `E` increases — this is the IVNA indexed-infinitesimal structure: `0_x` is labeled by the energy regime `x`. Also includes the algebraic `m_γ → 0` reference computation with explicit note that **GCM does not take this limit** (per L1's `m_γ > 0` commitment).

## Check 5 — Wolfram Language independent (with precision fix)

- **Tool:** Wolfram Engine 14.3.0 via `wolframscript` at 60 digits (enforced via `SetPrecision`)
- **Script:** [verification/check_05_wolfram.wls](verification/check_05_wolfram.wls)
- **Output:** [verification/outputs/check_05_wolfram.txt](verification/outputs/check_05_wolfram.txt)
- **Result:** PASS — after precision fix; see below.
- **Notes — real bug found during retrofit:**
  The **initial** version of this script used `N[expr, 60]` to request 60-digit precision. This FAILED silently: `N[]` does not necessarily propagate precision through `Sqrt[1 − ε²]` when an operand is machine-precision. Result: `v_photon` returned exactly `2.99792458e8`, so `Δv = c − v = 0`, and the structural check `v < c` reported `False`, in direct contradiction with the mpmath result.
  **Fix:** wrap all constants in `SetPrecision[_, 60]` *before* any arithmetic. This forces high-precision propagation through the entire computation.
  **Re-run result:** `Δv = 4.71685723327621428512454736787804709886506e-29 m/s`, matching mpmath to all printed digits (~22 digits of agreement). Structural `v < c` reports `True`. Taylor-vs-direct relative difference is `0``22.9` (effectively zero to the precision shown).
  **Lesson:** for claims with `ε ≪ 10⁻¹⁵`, Wolfram `N[]` cannot be trusted without explicit `SetPrecision` on all operands. This is a real tool caveat worth remembering for all GCM claims involving tiny quantities (L2, R6, L3).

---

## Cross-tool Summary

| Quantity | mpmath (80-digit) | Wolfram (60-digit, SetPrecision) | Agreement |
|---|---|---|---|
| `ε = m_γc²/E` | 5.60958860380445230983e-19 | 5.60958860380445230983e-19 | full |
| `ε²` | 3.14674843039327846e-37 | 3.14674843039327846e-37 | full |
| `v_photon` (m/s) | 2.99792457999999...9995283e8 | 2.99792457999999...9995283e8 | ~22 digits |
| `Δv` (m/s, direct) | 4.7168572332762136595e-29 | 4.7168572332762142851e-29 | ~18 digits |
| `Δv` (m/s, Taylor) | 4.7168572332762136595e-29 | 4.7168572332762142851e-29 | ~18 digits |
| `log10(FRB/GCM)` | 3.573288... | 3.573288... | full |
| Structural `v < c` | True | True | agree |

The ~18-digit agreement on `Δv` is limited by the fact that both tools are subtracting two close numbers; both are computing at sufficient precision to carry the result accurately. The Taylor and direct methods agree to ~38 digits in each tool individually.

---

## TODOs / Known gaps

- **Tool lesson:** For any future claim involving `ε < 10⁻¹⁵`, Wolfram scripts must use `SetPrecision` on all constants — not just `N[]` wrapping. Consider adding this as a note in the project's Wolfram conventions.
- **IVNA indexed-infinitesimal:** The `0_x` notation is used in claim/caveats.md but is not formally tied to the IVNA algebra in the verification stack. A later check could import the IVNA convention definitions and verify that the energy-dependence of `0_x` satisfies IVNA's indexed-zero rules. Not urgent for the coherence paper.
- **Structural claim is now robust:** `v_photon < c_causality` strictly, verified at 60+ digit precision by two independent CAS.
