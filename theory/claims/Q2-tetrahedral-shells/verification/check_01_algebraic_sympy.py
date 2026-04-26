#!/usr/bin/env python3
"""Q2 Check 1 — SymPy algebraic expansion.

Confirms that the cuboctahedral geometric decomposition —
  12 (vertices) + 24(n-1) (edges) + 8 * (n-1)(n-2)/2 (tri faces) + 6(n-1)^2 (sq faces)
— simplifies symbolically to 10*n**2 + 2.

Reads geometric counts from inputs.json; does not hardcode.
"""

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

n = sp.symbols("n", integer=True, positive=True)

V = INPUTS["cuboctahedron_geometry"]["vertices"]["value"]              # 12
E = INPUTS["cuboctahedron_geometry"]["edges"]["value"]                 # 24
F_tri = INPUTS["cuboctahedron_geometry"]["triangular_faces"]["value"]  # 8
F_sq = INPUTS["cuboctahedron_geometry"]["square_faces"]["value"]       # 6

vertices_term = V
edges_term = E * (n - 1)
tri_term = sp.Rational(F_tri, 2) * (n - 1) * (n - 2)  # 8 * (n-1)(n-2)/2
sq_term = F_sq * (n - 1) ** 2

geometric_sum = vertices_term + edges_term + tri_term + sq_term
simplified = sp.expand(geometric_sum)

expected = INPUTS["formula_coefficients"]["a"]["value"] * n ** 2 + INPUTS["formula_coefficients"]["b"]["value"]
expected_sym = sp.expand(expected)

agreement = sp.simplify(simplified - expected_sym) == 0

print(f"Geometric sum: {geometric_sum}")
print(f"Simplified:    {simplified}")
print(f"Expected:      {expected_sym}")
print(f"Difference:    {sp.simplify(simplified - expected_sym)}")
print(f"PASS" if agreement else "FAIL")
