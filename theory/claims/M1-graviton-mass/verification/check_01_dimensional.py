#!/usr/bin/env python3
"""M1 Check 1 — Dimensional analysis.

Computes m_g = rho_bound * ell_P^3 in SI units and confirms the result
has units of mass (kg). SymPy's `units` module provides symbolic unit
tracking so the dimensionality is checked mechanically.
"""
import json
import sys
from pathlib import Path

from sympy import sqrt, simplify, Rational
from sympy.physics.units import kilogram, meter, second, convert_to
from sympy.physics.units.util import quantity_simplify

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())


def value(name, sect="constants"):
    return INPUTS[sect][name]["value"]


def units_of(name, sect="constants"):
    return INPUTS[sect][name]["units"]


def main():
    hbar_v = value("hbar")
    G_v = value("G")
    c_v = value("c")
    rho_v = value("rho_bound_nuclear")

    # Build symbolic quantities with units. Use CODATA magnitudes.
    hbar_q = hbar_v * kilogram * meter**2 / second  # [J*s] = kg m^2 / s
    G_q = G_v * meter**3 / (kilogram * second**2)    # [m^3/(kg s^2)]
    c_q = c_v * meter / second                       # [m/s]
    rho_q = rho_v * kilogram / meter**3              # [kg/m^3]

    ell_P_q = sqrt(hbar_q * G_q / c_q**3)
    V_P_q = ell_P_q**3
    m_g_q = rho_q * V_P_q

    # Simplify the symbolic expression to compare dimensions.
    ell_P_simplified = quantity_simplify(ell_P_q)
    V_P_simplified = quantity_simplify(V_P_q)
    m_g_simplified = quantity_simplify(m_g_q)

    print(f"# M1 Check 1 — Dimensional analysis via SymPy units")
    print(f"# hbar  units (input JSON): {units_of('hbar')}")
    print(f"# G     units (input JSON): {units_of('G')}")
    print(f"# c     units (input JSON): {units_of('c')}")
    print(f"# rho   units (input JSON): {units_of('rho_bound_nuclear')}")
    print()
    print(f"ell_P   symbolic: {ell_P_simplified}")
    print(f"V_P     symbolic: {V_P_simplified}")
    print(f"m_g     symbolic: {m_g_simplified}")
    print()

    # Dimension check: final result should reduce to kilograms.
    # Convert to kilograms and check no residual dimensional factors remain.
    m_g_in_kg = convert_to(m_g_simplified, kilogram)
    print(f"m_g converted to kg: {m_g_in_kg}")

    # Test: the ratio m_g_in_kg / kilogram must be a pure (dimensionless) number.
    ratio = simplify(m_g_in_kg / kilogram)
    # If the simplified ratio is a pure number, free_symbols excluding numbers is empty
    # and dimension analysis passes.
    has_residual_units = any(
        str(sym) in ("meter", "second") for sym in ratio.free_symbols
    )
    print()
    if has_residual_units:
        print(f"STATUS: FAIL — residual units in result: {ratio.free_symbols}")
        sys.exit(1)
    print(f"STATUS: PASS — result reduces to pure kilograms.")
    print(f"ratio (m_g / kg) ≈ {float(ratio):.6e}")


if __name__ == "__main__":
    main()
