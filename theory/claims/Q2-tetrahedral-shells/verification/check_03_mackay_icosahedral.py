#!/usr/bin/env python3
"""Q2 Check 3 — Cross-geometry robustness: Mackay icosahedral decomposition.

Load-bearing for the 2026-04-23 reframe. Confirms that the SAME formula
P_n = 10n^2 + 2 arises from the Mackay icosahedral decomposition —
  12 vertices + 30(n-1) edges + 20 * (n-1)(n-2)/2 triangular faces
— which is geometrically DIFFERENT from the cuboctahedral decomposition
(cuboctahedron has 24 edges, 8 tri faces, 6 sq faces; icosahedron has
30 edges, 20 tri faces, no square faces).

If both decompositions sum to the same closed form, the formula is a
property of 12-coordinate close-packing broadly, not of FCC specifically.

Reference: Mackay, A. L. (1962). Acta Crystallographica 15, 916-918.
"""

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

V = INPUTS["mackay_icosahedron_geometry"]["vertices"]["value"]              # 12
E = INPUTS["mackay_icosahedron_geometry"]["edges"]["value"]                 # 30
F_tri = INPUTS["mackay_icosahedron_geometry"]["triangular_faces"]["value"]  # 20

a = INPUTS["formula_coefficients"]["a"]["value"]
b = INPUTS["formula_coefficients"]["b"]["value"]

# Symbolic
n = sp.symbols("n", integer=True, positive=True)
mackay_sum = V + E * (n - 1) + sp.Rational(F_tri, 2) * (n - 1) * (n - 2)
mackay_simplified = sp.expand(mackay_sum)
target = sp.expand(a * n ** 2 + b)

print(f"Mackay decomposition: {V} + {E}(n-1) + {F_tri}(n-1)(n-2)/2")
print(f"Expanded:             {mackay_simplified}")
print(f"Target (10n^2 + 2):   {target}")
print(f"Symbolic match:       {'PASS' if sp.simplify(mackay_simplified - target) == 0 else 'FAIL'}")
print()

# Numerical
published = {
    int(k.split("_")[1]): v["value"]
    for k, v in INPUTS["expected_shells_published"].items()
    if not k.startswith("_")
}
fail = False
header = f"{'n':>3}  {'V':>3}  {'E*(n-1)':>8}  {'F*(n-1)(n-2)/2':>16}  {'total':>6}  {'published':>10}  status"
print(header)
print("-" * len(header))
for k in range(1, 6):
    v_term = V
    e_term = E * (k - 1)
    f_term = (F_tri * (k - 1) * (k - 2)) // 2
    total = v_term + e_term + f_term
    pub = published[k]
    ok = total == pub
    print(f"{k:>3}  {v_term:>3}  {e_term:>8}  {f_term:>16}  {total:>6}  {pub:>10}  {'PASS' if ok else 'FAIL'}")
    if not ok:
        fail = True

print()
print("OVERALL:", "PASS (5/5)" if not fail else "FAIL")
print("Interpretation: Mackay icosahedral and FCC cuboctahedral clusters")
print("give the same shell populations via different geometric decompositions.")
print("Therefore P_n = 10n^2 + 2 is a property of 12-coordinate close-packing,")
print("not of any specific crystal geometry.")
