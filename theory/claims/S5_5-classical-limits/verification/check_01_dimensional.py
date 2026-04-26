#!/usr/bin/env python3
"""
S5.5(a) — Check 01: Dimensional analysis of F = G * m1 * m2 / r^2

Two independent checks:
  (i)  SymPy dimension system: build [G], [m], [r] and verify product has dimensions of force.
  (ii) Manual exponent-tracking of SI base-unit exponents (m, kg, s).

Both must agree, and must equal the exponent vector for Newton = kg*m/s^2.
"""
import json
import pathlib
import sys
from datetime import datetime

from sympy.physics.units.dimensions import Dimension
from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units import length, mass, time as dim_time, force

INPUTS = json.loads(
    (pathlib.Path(__file__).parent / "inputs.json").read_text()
)

print(f"# Check: 01 — Dimensional analysis of F = G*m1*m2/r^2")
print(f"# Claim: S5_5-classical-limits (sub-claim a — Newtonian limit)")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy.physics.units")
print(f"# Script: verification/check_01_dimensional.py")
print(f"# ----")

# --- Check (i): SymPy dimension arithmetic ---
# G has dimensions [length^3 / (mass * time^2)]
dim_G = length**3 / (mass * dim_time**2)
dim_product = dim_G * mass * mass / length**2
# Reduce to base dimensions
base_product = dimsys_SI.get_dimensional_dependencies(dim_product)
base_force   = dimsys_SI.get_dimensional_dependencies(force)

print("SymPy dimension arithmetic:")
print(f"  dim(G) * dim(m)^2 / dim(r)^2 = {dict(base_product)}")
print(f"  dim(force)                   = {dict(base_force)}")
sympy_pass = base_product == base_force
print(f"  Match: {'PASS' if sympy_pass else 'FAIL'}")

# --- Check (ii): manual SI base-unit exponents ---
# Track exponents of (m, kg, s) through the product
# G:    (m^3, kg^-1, s^-2)
# m^2:  (kg^2)
# r^-2: (m^-2)
G_exp     = {"m":  3, "kg": -1, "s": -2}
m1m2_exp  = {"m":  0, "kg":  2, "s":  0}
r_inv2_exp= {"m": -2, "kg":  0, "s":  0}

product_exp = {k: G_exp[k] + m1m2_exp[k] + r_inv2_exp[k] for k in ("m","kg","s")}
newton_exp  = {"m": 1, "kg": 1, "s": -2}  # kg*m/s^2

print("\nManual exponent tracking (m, kg, s):")
print(f"  G        : {G_exp}")
print(f"  m1 * m2  : {m1m2_exp}")
print(f"  1 / r^2  : {r_inv2_exp}")
print(f"  product  : {product_exp}")
print(f"  Newton   : {newton_exp}")
manual_pass = product_exp == newton_exp
print(f"  Match: {'PASS' if manual_pass else 'FAIL'}")

# --- Agreement ---
overall = sympy_pass and manual_pass
print(f"\nBoth methods agree: {'YES' if sympy_pass == manual_pass else 'NO'}")
print(f"\n# Status: {'PASS' if overall else 'FAIL'}")
