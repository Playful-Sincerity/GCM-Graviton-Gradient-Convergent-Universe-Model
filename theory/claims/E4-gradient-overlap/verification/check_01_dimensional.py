"""
Check 01 — Dimensional analysis of U(R) and F(R) [Pint-based]
Claim: E4-gradient-overlap

U(R) = -(G m^2 / R) erf(R/(2 sigma)) should have units of energy (J)
F(R) = -dU/dR should have units of force (N)

Strategy: use Pint (if available) for first-class unit tracking; otherwise
do manual dimensional bookkeeping with SymPy.Dimension simplification.
This approach is more robust than the SymPy physics.units module for
simple algebraic combinations.
"""
import json
import sys
from pathlib import Path

print("# Check 01 — Dimensional analysis of U(R) and F(R)")
print(f"# Python: {sys.version.split()[0]}")

try:
    import pint
    print(f"# Tool: Pint {pint.__version__}")
    print("# ---")
    ureg = pint.UnitRegistry()

    # Assign units
    G = 1.0 * ureg.meter**3 / ureg.kilogram / ureg.second**2
    m = 1.0 * ureg.kilogram
    R = 1.0 * ureg.meter
    sigma = 1.0 * ureg.meter

    # erf argument must be dimensionless
    arg_erf = (R / (2 * sigma))
    print(f"erf(R/(2 sigma)):  arg dimensionality = {arg_erf.dimensionality}")
    assert arg_erf.dimensionless, f"erf arg not dimensionless: {arg_erf.dimensionality}"
    print("  PASS — erf argument dimensionless.")

    # exp argument must be dimensionless
    arg_exp = R**2 / sigma**2
    print(f"exp(-R^2/(4 sigma^2)): arg dimensionality = {arg_exp.dimensionality}")
    assert arg_exp.dimensionless
    print("  PASS — exp argument dimensionless.")

    # U(R) = (G m^2 / R) * [dimensionless erf]
    U = G * m**2 / R
    U_dim = U.dimensionality
    U_target = (1 * ureg.joule).dimensionality
    print(f"U(R):  [G m^2 / R] has dimensionality {U_dim}")
    print(f"  target (joule):                   {U_target}")
    assert U_dim == U_target, f"U not in energy units: {U_dim}"
    print("  PASS — U(R) has units of energy.")

    # F(R) = G m^2 / R^2 * (dimensionless)
    F = G * m**2 / R**2
    F_dim = F.dimensionality
    F_target = (1 * ureg.newton).dimensionality
    print(f"F(R):  [G m^2 / R^2] has dimensionality {F_dim}")
    print(f"  target (newton):                     {F_target}")
    assert F_dim == F_target, f"F not in force units: {F_dim}"
    print("  PASS — F(R) has units of force.")

    print("\n# Status: PASS — all four dimensional checks passed via Pint.")

except ImportError:
    # Fall back: manual dimensional algebra via SymPy
    import sympy as sp
    print("# Tool: SymPy (Pint unavailable)")
    print("# ---")

    # Represent dimensions as monomials in L, M, T
    L, M, T = sp.symbols('L M T', positive=True)
    G_dim = L**3 / (M * T**2)
    m_dim = M
    R_dim = L
    sigma_dim = L

    arg_erf_dim = R_dim / sigma_dim
    arg_exp_dim = R_dim**2 / sigma_dim**2
    U_dim_expr = G_dim * m_dim**2 / R_dim
    F_dim_expr = G_dim * m_dim**2 / R_dim**2

    energy_dim = M * L**2 / T**2  # J = kg m^2 / s^2
    force_dim = M * L / T**2       # N = kg m / s^2

    print(f"arg_erf dimension = {sp.simplify(arg_erf_dim)} (expect: 1)")
    assert sp.simplify(arg_erf_dim) == 1
    print("  PASS")

    print(f"arg_exp dimension = {sp.simplify(arg_exp_dim)} (expect: 1)")
    assert sp.simplify(arg_exp_dim) == 1
    print("  PASS")

    print(f"U dim = {sp.simplify(U_dim_expr)}  (expect energy: {energy_dim})")
    assert sp.simplify(U_dim_expr - energy_dim) == 0
    print("  PASS")

    print(f"F dim = {sp.simplify(F_dim_expr)}  (expect force: {force_dim})")
    assert sp.simplify(F_dim_expr - force_dim) == 0
    print("  PASS")

    print("\n# Status: PASS — all four dimensional checks passed via SymPy fallback.")
