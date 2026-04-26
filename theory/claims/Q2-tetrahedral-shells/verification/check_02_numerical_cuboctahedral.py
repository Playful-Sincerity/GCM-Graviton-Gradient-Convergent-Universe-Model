#!/usr/bin/env python3
"""Q2 Check 2 — Numerical agreement between formula and cuboctahedral geometric count (n=1..5).

For each n in 1..5:
- Computes the formula value P_n = a*n^2 + b (a=10, b=2) from inputs.json.
- Computes the geometric decomposition sum for the cuboctahedron.
- Compares both against the published expected values from gcm_v2.md (also in inputs.json).
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

a = INPUTS["formula_coefficients"]["a"]["value"]
b = INPUTS["formula_coefficients"]["b"]["value"]

V = INPUTS["cuboctahedron_geometry"]["vertices"]["value"]
E = INPUTS["cuboctahedron_geometry"]["edges"]["value"]
F_tri = INPUTS["cuboctahedron_geometry"]["triangular_faces"]["value"]
F_sq = INPUTS["cuboctahedron_geometry"]["square_faces"]["value"]

published = {
    int(k.split("_")[1]): v["value"]
    for k, v in INPUTS["expected_shells_published"].items()
    if not k.startswith("_")
}

fail = False
header = f"{'n':>3}  {'formula':>8}  {'geometric':>10}  {'published':>10}  {'status':>6}"
print(header)
print("-" * len(header))

for n in range(1, 6):
    formula = a * n ** 2 + b
    geometric = V + E * (n - 1) + (F_tri * (n - 1) * (n - 2)) // 2 + F_sq * (n - 1) ** 2
    pub = published[n]
    match = formula == geometric == pub
    print(f"{n:>3}  {formula:>8}  {geometric:>10}  {pub:>10}  {'PASS' if match else 'FAIL':>6}")
    if not match:
        fail = True

print()
print("OVERALL:", "PASS (5/5)" if not fail else "FAIL")
