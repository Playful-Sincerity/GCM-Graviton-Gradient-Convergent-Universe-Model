#!/usr/bin/env python3
"""
H2 — Check 01: Newton's cooling ODE solution via SymPy

Claim: The local-release equation
    dρ_g/dt = -λ (ρ_g - ρ_0)
has solution
    ρ_g(t) - ρ_0 = (ρ_g(0) - ρ_0) · exp(-λ t)

Verify by having SymPy solve the ODE symbolically and compare to the
claimed closed form. Also check that the functional form reproduces
Newton's law of cooling structure dT/dt = -k(T - T_env) under the
mapping T - T_env ∝ ρ_g - ρ_0.
"""
import json
import pathlib
import sys
from datetime import datetime

from sympy import symbols, Function, dsolve, Eq, Derivative, exp, simplify

INPUTS = json.loads(
    (pathlib.Path(__file__).parent / "inputs.json").read_text()
)

print(f"# Check: 01 — Newton's cooling ODE solution via SymPy")
print(f"# Claim: H2-release-heat")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy 1.14.0 (dsolve)")
print(f"# Script: verification/check_01_cooling_ode_sympy.py")
print(f"# ----")

t, lam, rho0, rho_init = symbols("t lambda rho_0 rho_init", positive=True, real=True)
rho = Function("rho_g")

# Define the ODE: dρ/dt = -λ (ρ - ρ_0)
ode = Eq(Derivative(rho(t), t), -lam * (rho(t) - rho0))
print(f"ODE: {ode}")

# Initial condition: ρ_g(0) = ρ_init
solution = dsolve(ode, rho(t), ics={rho(0): rho_init})
print(f"\nSymPy dsolve solution:\n  {solution}")

# Claimed solution: ρ_g(t) = ρ_0 + (ρ_init - ρ_0) * exp(-λ t)
claimed = rho0 + (rho_init - rho0) * exp(-lam * t)
print(f"\nClaimed form:\n  rho_g(t) = {claimed}")

# Check equivalence
difference = simplify(solution.rhs - claimed)
passed_ode = difference == 0
print(f"\nDifference (solution - claimed) simplified: {difference}")
print(f"ODE solution matches claimed exponential form: {'PASS' if passed_ode else 'FAIL'}")

# Derived consequence: rho_g - rho_0 = (rho_init - rho_0) * exp(-lambda t)
# This is the Newton's-cooling functional form: "excess decays exponentially"
excess_form = simplify(solution.rhs - rho0)
expected_excess = (rho_init - rho0) * exp(-lam * t)
passed_excess = simplify(excess_form - expected_excess) == 0
print(f"\nExcess form ρ_g(t) - ρ_0 = {excess_form}")
print(f"Expected              = {expected_excess}")
print(f"Exponential decay of excess: {'PASS' if passed_excess else 'FAIL'}")

# Limit check: as t -> infinity, excess -> 0 (equilibrium reached)
from sympy import oo, limit
lim_excess = limit(excess_form, t, oo)
passed_limit = lim_excess == 0
print(f"\nlim t->∞ (ρ_g(t) - ρ_0) = {lim_excess}")
print(f"Asymptotic equilibrium: {'PASS' if passed_limit else 'FAIL'}")

all_pass = passed_ode and passed_excess and passed_limit
print(f"\n# Status: {'PASS' if all_pass else 'FAIL'}")
