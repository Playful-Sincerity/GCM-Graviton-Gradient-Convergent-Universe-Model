# R6 Verification Outputs — TODO

**Status (2026-04-24):** Python execution was denied in the retrofit session.
Scripts in `../check_0[1-6]_*.py` are runnable but outputs have not yet been
captured.

**To populate:**

```bash
cd "$(dirname "$0")/.."
python3 check_01_dimensional.py              > outputs/check_01_dimensional.txt
python3 check_02_limit_cases_sympy.py        > outputs/check_02_limit_cases_sympy.txt
python3 check_03_des_2024_comparison.py      > outputs/check_03_des_2024_comparison.txt
python3 check_04_falsification_gate.py       > outputs/check_04_falsification_gate.txt
python3 check_05_redshift_cascade_sympy.py   > outputs/check_05_redshift_cascade_sympy.txt
python3 check_06_velocity_ratio_mpmath.py    > outputs/check_06_velocity_ratio_mpmath.txt
```

**Wolfram MCP:** unavailable. When available, add a Wolfram Language check
for the symbolic redshift cascade and the high-precision v_emit/v_obs ratio
(Wolfram handles arbitrary-precision arithmetic natively).

**Cross-tool agreement expected:**
- Checks 02, 05 (SymPy symbolic) should agree with Check 05's expansion.
- Check 06 (mpmath 60 dps) should show v_emit/v_obs − 1 ≈ O(10⁻³⁷) at z=1, E≈1 eV.
- Any disagreement between Check 05's symbolic series and Check 06's
  numeric evaluation would be a real signal worth surfacing.
