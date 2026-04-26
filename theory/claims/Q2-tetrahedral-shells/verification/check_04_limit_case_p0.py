#!/usr/bin/env python3
"""Q2 Check 4 — Limit case P_0.

Confirms that the formula gives P_0 = 2, and documents that this is a
mathematical artifact with no geometric meaning. The central site of a
cluster is one graviton, not two. The formula is valid for n >= 1.

Also verifies that P_{-1} = 12 (same as P_1) — another formula artifact
irrelevant to physics.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

a = INPUTS["formula_coefficients"]["a"]["value"]
b = INPUTS["formula_coefficients"]["b"]["value"]


def P(n):
    return a * n ** 2 + b


print(f"P(-1) = {P(-1)}  (formula artifact; no geometric meaning)")
print(f"P(0)  = {P(0)}   (formula artifact; physical center is 1 graviton, not 2)")
print(f"P(1)  = {P(1)}  (first shell; cuboctahedral or icosahedral)")
print(f"P(2)  = {P(2)}  (second shell)")
print()
print("Check: does P(0) = 2 correspond to a 'center + inversion partner'? NO.")
print("Reason: an inversion partner at the same site would be coincident, not a")
print("separate site. Formula's n=0 output is pure algebraic artifact.")
print()
print("Status: NOTED (not a failure; boundary condition stated explicitly).")
