# E7 — Verification Record

**Tally:** 5/5 checks passed. Cross-tool agreement: SymPy and Wolfram both return `-4` exactly for the `(Δm_e/m_e)/(Δe/e)` ratio.
**Last run:** 2026-04-24.
**Reproducible:** Yes — all scripts live in [verification/](verification/); inputs centralized in [inputs.json](verification/inputs.json); captured stdout in [verification/outputs/](verification/outputs/).

---

## Check 1 — SymPy symbolic derivation

- **Tool:** Python 3.14.4 / SymPy 1.14.0
- **Script:** [verification/check_01_sympy_symbolic.py](verification/check_01_sympy_symbolic.py)
- **Output:** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** SymPy differentiates `E_1 = -m_e k² e⁴ / (2ℏ²)` and confirms `∂E_1/∂e = 4 E_1/e` and `∂E_1/∂m_e = E_1/m_e` are algebraic identities (difference simplifies to 0). Solving `(∂E_1/∂e)Δe + (∂E_1/∂m_e)Δm = 0` for `Δm` gives `-4 m_e Δe / e`, and the ratio `(Δm/m_e)/(Δe/e)` simplifies to exactly `-4`.

## Check 2 — Finite-difference derivatives (mpmath, 40-digit)

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_02_finite_diff.py](verification/check_02_finite_diff.py)
- **Output:** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Central-difference derivatives at step `1e-10 × parameter` match the analytical closed forms `4 E_1/e` and `E_1/m_e` to well below `1e-10` relative error. Independent numerical confirmation that the symbolic partial derivatives are correct. The Bohr ground-state value reproduces to 6 sig figs: `-13.605693124 eV` (expected `-13.6057 eV`).

## Check 3 — Spot check against the session brief's example

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_03_numeric_spot.py](verification/check_03_numeric_spot.py)
- **Output:** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** `Δe = 10⁻³⁵ C` yields `Δm_e = -2.274252e-46 kg`. Session brief's rounded value is `-2.27e-46 kg`; 0.2% difference is rounding of the brief's stated figure, not a computational discrepancy.

## Check 4 — Limit case `Δe → 0`

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_04_limit_zero.py](verification/check_04_limit_zero.py)
- **Output:** [verification/outputs/check_04.txt](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** `Δm_e → 0` as `Δe → 0`, smoothly. The limiting slope `Δm/Δe = -4 m_e/e = -2.2742e-11 kg/C`. Formula is continuous at `(0, 0)`.

## Check 5 — Wolfram Language independent

- **Tool:** Wolfram Engine 14.3.0 via `wolframscript`
- **Script:** [verification/check_05_wolfram.wls](verification/check_05_wolfram.wls)
- **Output:** [verification/outputs/check_05_wolfram.txt](verification/outputs/check_05_wolfram.txt)
- **Result:** PASS — Wolfram confirms the symbolic identity `(Δm/m_e)/(Δe/e) = -4` exactly.
- **Notes:**
  - Wolfram's `dE_1/de - 4 E_1/e` simplifies to `True` (identical expressions).
  - Wolfram's `dE_1/dm_e - E_1/m_e` simplifies to `True`.
  - Solved `Dm = -4 De me / e` directly; ratio printed as `-4` (not a floating-point approximation).
  - Numerical spot check: Wolfram gives `-2.274252e-46 kg`, identical to mpmath to 15 digits.
  - Bohr ground state: `-13.605693 eV` (agrees with mpmath).

---

## Cross-tool Summary

| Quantity | SymPy | mpmath | Wolfram | Agreement |
|---|---|---|---|---|
| `∂E_1/∂e` analytical form | `4 E_1/e` | matches | `4 E_1/e` | symbolic exact |
| `∂E_1/∂m_e` analytical form | `E_1/m_e` | matches | `E_1/m_e` | symbolic exact |
| `(Δm/m_e)/(Δe/e)` ratio | `-4` | n/a (numeric) | `-4` | symbolic exact |
| `Δm_e` for `Δe = 1e-35 C` | n/a | `-2.274252e-46 kg` | `-2.274252e-46 kg` | 15 digits |
| `E_1` (Bohr) | n/a | `-13.60569 eV` | `-13.60569 eV` | 6 digits (inputs precision) |

**No cross-tool disagreements.**

---

## TODOs / Known gaps

- None for the Bohr-level claim itself. The claim is robustly verified.
- **Open for future work (not a gap in E7):** Extending to Dirac / QED / hyperfine levels would modify the `-4` ratio. E7 is honest at Bohr; the QED extension is a research agenda, not a gap in the present claim.
