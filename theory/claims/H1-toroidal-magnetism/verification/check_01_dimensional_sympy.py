#!/usr/bin/env python3
"""
H1 — Check 01: Dimensional analysis of the proposed GCM → Tesla coupling

Confirms:
  (a) [J_g] = kg/(m^2 s)
  (b) [div J_g] = kg/(m^3 s)
  (c) [(div J_g) * v] = kg/(m^2 s^2) = N/m^3  (force per unit volume)
  (d) [Tesla] = kg/(A s^2)
  (e) A coupling constant with units [m^2 / A] takes (div J_g)·v into Tesla.

Verified two ways:
  i.  Manual SI base-unit exponent tracking
  ii. SymPy physics.units symbolic dimension arithmetic
"""
import sys
from datetime import datetime

from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units import length, mass, time as dim_time, current

print(f"# Check: 01 — Dimensional analysis of (div J_g)·v and Tesla coupling")
print(f"# Claim: H1-toroidal-magnetism")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy 1.14.0 (physics.units)")
print(f"# Script: verification/check_01_dimensional_sympy.py")
print(f"# ----")

# --- Manual SI exponent tracking: (m, kg, s, A) ---
# J_g: kg / (m^2 s)
J_g_exp         = {"m": -2, "kg":  1, "s": -1, "A":  0}
# div J_g: kg / (m^3 s)
div_J_g_exp     = {"m": -3, "kg":  1, "s": -1, "A":  0}
# v: m/s
v_exp           = {"m":  1, "kg":  0, "s": -1, "A":  0}
# Product
product_exp     = {k: div_J_g_exp[k] + v_exp[k] for k in div_J_g_exp}
# Tesla: kg / (A s^2)
tesla_exp       = {"m":  0, "kg":  1, "s": -2, "A": -1}
# Required coupling: takes product -> Tesla
coupling_exp    = {k: tesla_exp[k] - product_exp[k] for k in tesla_exp}

print("Manual SI-exponent tracking (m, kg, s, A):")
print(f"  J_g           : {J_g_exp}")
print(f"  ∇·J_g         : {div_J_g_exp}")
print(f"  v             : {v_exp}")
print(f"  (∇·J_g)·v     : {product_exp}   (expected kg m^-2 s^-2 = N/m^3)")
print(f"  Tesla         : {tesla_exp}     (kg A^-1 s^-2)")
print(f"  coupling      : {coupling_exp}   (expected m^2 / A = {{m:2, kg:0, s:0, A:-1}})")

# Checks
product_expected = {"m": -2, "kg": 1, "s": -2, "A": 0}
coupling_expected = {"m": 2, "kg": 0, "s": 0, "A": -1}
manual_product_pass = product_exp == product_expected
manual_coupling_pass = coupling_exp == coupling_expected

print(f"\n  (∇·J_g)·v exponent match: {'PASS' if manual_product_pass else 'FAIL'}")
print(f"  coupling exponent match : {'PASS' if manual_coupling_pass else 'FAIL'}")

# --- SymPy physics.units cross-check ---
# J_g dimension
dim_Jg      = mass / (length**2 * dim_time)
dim_div_Jg  = mass / (length**3 * dim_time)
dim_v       = length / dim_time
dim_product = dim_div_Jg * dim_v
dim_tesla   = mass / (current * dim_time**2)
dim_coupling = dim_tesla / dim_product

def deps(d):
    return {str(k.name): v for k, v in dimsys_SI.get_dimensional_dependencies(d).items()}

print("\nSymPy physics.units cross-check:")
print(f"  dim(J_g)           = {deps(dim_Jg)}")
print(f"  dim(∇·J_g)         = {deps(dim_div_Jg)}")
print(f"  dim(v)             = {deps(dim_v)}")
print(f"  dim((∇·J_g)·v)     = {deps(dim_product)}")
print(f"  dim(Tesla)         = {deps(dim_tesla)}")
print(f"  dim(coupling=T/product) = {deps(dim_coupling)}")

# Tesla: kg / (A s^2)
expected_tesla_deps = {"length": 0, "mass": 1, "time": -2, "current": -1}
# Product: kg m^-2 s^-2 (no current)
expected_product_deps = {"length": -2, "mass": 1, "time": -2}
# Coupling: m^2 / A
expected_coupling_deps = {"length": 2, "time": 0, "current": -1}

def deps_match_expected(actual, expected):
    # Expected may omit zero entries. Compare nonzero parts.
    for k, v in expected.items():
        if actual.get(k, 0) != v:
            return False
    for k, v in actual.items():
        if k not in expected and v != 0:
            return False
    return True

sympy_product_pass = deps_match_expected(deps(dim_product), expected_product_deps)
sympy_coupling_pass = deps_match_expected(deps(dim_coupling), expected_coupling_deps)
sympy_tesla_pass = deps_match_expected(deps(dim_tesla), expected_tesla_deps)

print(f"\n  SymPy product match    : {'PASS' if sympy_product_pass else 'FAIL'}")
print(f"  SymPy Tesla match      : {'PASS' if sympy_tesla_pass else 'FAIL'}")
print(f"  SymPy coupling match   : {'PASS' if sympy_coupling_pass else 'FAIL'}")

# Agreement
agreement = (manual_product_pass == sympy_product_pass and
             manual_coupling_pass == sympy_coupling_pass)
print(f"\nManual and SymPy agree: {'YES' if agreement else 'NO'}")

# Also explicitly confirm the 'm^2 * A' alternative (the pre-audit error) is WRONG
bad_coupling_expected = {"length": 2, "current": 1}
bad_attempt_product = dim_product * (length**2 * current)
bad_attempt_deps = deps(bad_attempt_product)
bad_is_tesla = deps_match_expected(bad_attempt_deps, expected_tesla_deps)
print(f"\nSanity: the pre-audit error (coupling = m^2·A) would give:")
print(f"  (∇·J_g)·v * (m^2·A) = {bad_attempt_deps}")
print(f"  which is Tesla? {'YES' if bad_is_tesla else 'NO (confirms the audit fix was correct)'}")

all_pass = (manual_product_pass and manual_coupling_pass and
            sympy_product_pass and sympy_coupling_pass and sympy_tesla_pass
            and not bad_is_tesla)
print(f"\n# Status: {'PASS' if all_pass else 'FAIL'}")
