# L1 Verification Outputs — TODO

**Status (2026-04-24):** Python execution was denied in the retrofit session
that generated this verification stack. The scripts at
`../check_0[1-5]_*.py` are runnable as-is, but their stdout has not yet been
captured to this directory.

**To populate:** Re-run each script in a session with `python3` permission
and redirect stdout to the corresponding `check_0N_*.txt` file:

```bash
cd "$(dirname "$0")/.."
python3 check_01_dimensional.py        > outputs/check_01_dimensional.txt
python3 check_02_numerical_mpmath.py   > outputs/check_02_numerical_mpmath.txt
python3 check_03_sympy_symbolic.py     > outputs/check_03_sympy_symbolic.txt
python3 check_04_bounds_comparison.py  > outputs/check_04_bounds_comparison.txt
python3 check_05_limit_cases.py        > outputs/check_05_limit_cases.txt
```

After running, prepend each output with the standard header format (see
verification.md) and update the ledger at `theory/claims/ledger.md`.

**Wolfram MCP:** unavailable in this session. When a session with Wolfram
access is available, add a `check_NN_wolfram.wls` script checking the
kg -> eV/c^2 conversion and the bounds comparison independently.
