# Q3 — Verification Record

**Tally:** 4/4 checks passed. Cross-tool agreement: SymPy and Wolfram both return the asymptote `10 · Ry = 136 eV` as an exact symbolic limit. Variation across n=1..5 confirmed at 16% (both tools).
**Last run:** 2026-04-24.
**Reproducible:** Yes — all scripts live in [verification/](verification/); inputs in [inputs.json](verification/inputs.json); captured stdout in [verification/outputs/](verification/outputs/).

---

## Check 1 — Exact-arithmetic tabulation (SymPy Rational)

- **Tool:** Python 3.14.4 / SymPy 1.14.0
- **Script:** [verification/check_01_table_exact.py](verification/check_01_table_exact.py)
- **Output:** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** Table computed with exact rational arithmetic: `|E_1|·P_1 = 816/5 = 163.2`, `|E_2|·P_2 = 714/5 = 142.8`, `|E_3|·P_3 = 6256/45 ≈ 139.022`, `|E_4|·P_4 = 1377/10 = 137.7`, `|E_5|·P_5 = 17136/125 = 137.088`. Symbolic `limit(Prod, n, oo) = 136` exactly. Variation (max-min)/max = 16.0%.

## Check 2 — Large-n convergence (mpmath, 40-digit)

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_02_large_n_convergence.py](verification/check_02_large_n_convergence.py)
- **Output:** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** The correction term `2·Ry/n² = 27.2/n²` eV matches computation at `n=1000` to better than 1e-30 relative error. Converges monotonically from above:

  | n | `\|E_n\|·P_n` (eV) | deviation from 136 |
  |---|---|---|
  | 10 | 136.272 | 0.272 = 27.2/100 ✓ |
  | 100 | 136.00272 | 2.72e-3 = 27.2/10⁴ ✓ |
  | 1000 | 136.0000272 | 2.72e-5 = 27.2/10⁶ ✓ |
  | 10000 | 136.000000272 | 2.72e-7 = 27.2/10⁸ ✓ |

## Check 3 — FCC coordination-shell formula cross-check

- **Tool:** Python 3.14.4
- **Script:** [verification/check_03_fcc_crosscheck.py](verification/check_03_fcc_crosscheck.py)
- **Output:** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** `P_n = 10n²+2` matches OEIS A005901 (canonical FCC/tetrahedral coordination-shell sequence) for `n=1..9`: 12, 42, 92, 162, 252, 362, 492, 642, 812. Standard FCC nearest-neighbor count (P_1 = 12) confirmed. The formula is a known crystallographic result, not a GCM-internal invention.

## Check 4 — Wolfram Language independent

- **Tool:** Wolfram Engine 14.3.0 via `wolframscript`
- **Script:** [verification/check_04_wolfram.wls](verification/check_04_wolfram.wls)
- **Output:** [verification/outputs/check_04_wolfram.txt](verification/outputs/check_04_wolfram.txt)
- **Result:** PASS — full agreement with SymPy/mpmath.
- **Notes:**
  - `Limit[Prod[n], n → Infinity] = 136` (exact symbolic).
  - `Simplify[Prod[n]] = (136·(5 + 1/n²))/5` — giving the correction in closed form: `136 + 136/(5n²) = 136 + 27.2/n²`. Agrees with Python.
  - Variation `16.0%`, identical to SymPy.
  - n=10, 100, 1000, 10000 deviations match mpmath to printed precision.

---

## Cross-tool Summary

| Quantity | SymPy (exact) | Wolfram (exact) | mpmath (numeric) | Agreement |
|---|---|---|---|---|
| `lim_{n→∞} \|E_n\|·P_n` | 136 eV | 136 eV | n/a | exact |
| `Simplify(Prod)` | `136·(5 + n⁻²)/5` | `136·(5 + n⁻²)/5` | matches | exact |
| `\|E_1\|·P_1` | 816/5 = 163.2 eV | 816/5 | 163.2 | exact |
| Variation n=1..5 | 16.0% | 16.0% | n/a | exact |
| Deviation at n=1000 | `2·Ry/n² = 27.2e-6` | 27.2e-6 | 2.72e-5 | full |
| OEIS A005901 match | n=1..9 all match | n/a | n/a | full |

**No cross-tool disagreements.**

---

## TODOs / Known gaps

- **None in the numerical claim.** The near-invariance is exactly what the two input formulas (Bohr + FCC) imply; the `16%` variation and `10·Ry` asymptote are verified by three independent tools.
- **Mechanism-level Q6 (aspirational, not Q3):** Q3 does not derive `E_n ∝ 1/n²` from FCC packing. That is Q6 and remains open. Q3 is a compatibility observation, as stated in `claim.md` and `caveats.md`.
