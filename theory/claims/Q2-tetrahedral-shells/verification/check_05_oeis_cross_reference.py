#!/usr/bin/env python3
"""Q2 Check 5 — OEIS cross-reference.

Prints the formula's first 10 terms and compares against OEIS A005901
(published cuboctahedral / Mackay icosahedral shell population sequence):
  1, 12, 42, 92, 162, 252, 362, 492, 642, 812, ...

Note: OEIS A005901 begins with a(0)=1 (the central atom, by convention,
not the formula value P_0=2), then a(n) = 10n^2 + 2 for n >= 1. So we
check the formula values against OEIS a(1) through a(10).
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

a = INPUTS["formula_coefficients"]["a"]["value"]
b = INPUTS["formula_coefficients"]["b"]["value"]


def P(n):
    return a * n ** 2 + b


# OEIS A005901, terms a(1) through a(10), sourced from oeis.org/A005901
# Saved here so scripts are offline-reproducible; update if the OEIS
# sequence is ever re-curated.
OEIS_A005901 = {
    1: 12,
    2: 42,
    3: 92,
    4: 162,
    5: 252,
    6: 362,
    7: 492,
    8: 642,
    9: 812,
    10: 1002,
}

fail = False
print(f"{'n':>3}  {'P(n)':>6}  {'OEIS A005901':>12}  status")
print("-" * 34)
for n in range(1, 11):
    val = P(n)
    oeis = OEIS_A005901[n]
    ok = val == oeis
    print(f"{n:>3}  {val:>6}  {oeis:>12}  {'PASS' if ok else 'FAIL'}")
    if not ok:
        fail = True

print()
print("OVERALL:", "PASS (10/10 match OEIS A005901)" if not fail else "FAIL")
