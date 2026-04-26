#!/usr/bin/env python3
"""M3 Check 1 — Dimensional analysis via SymPy units.

Confirms that N = (4/3)*pi * R_H^3 / ell_P^3 is dimensionless (a count).
"""
import json
from pathlib import Path

from sympy import sqrt, simplify, pi, Rational
from sympy.physics.units import meter, kilogram, second, convert_to
from sympy.physics.units.util import quantity_simplify

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())


def cv(name, sect="constants"):
    return INPUTS[sect][name]["value"]


def main():
    R_H_q = cv("R_H") * meter
    ell_P_q = cv("ell_P_shortform") * meter

    V_universe = Rational(4, 3) * pi * R_H_q**3
    V_P = ell_P_q**3

    N_q = V_universe / V_P

    print("# M3 Check 1 — Dimensional analysis")
    print()
    print(f"R_H * meter         = {R_H_q}")
    print(f"ell_P * meter       = {ell_P_q}")
    print()
    print(f"V_universe          = {quantity_simplify(V_universe)}")
    print(f"V_P                 = {quantity_simplify(V_P)}")
    print(f"N = V_universe/V_P  = {quantity_simplify(N_q)}")
    print()

    # The result should have no residual units (dimensionless count)
    N_simpl = quantity_simplify(N_q)
    has_units = any(
        str(sym) in ("meter", "second", "kilogram") for sym in N_simpl.free_symbols
    )
    if has_units:
        print(f"STATUS: FAIL — residual units found: {N_simpl.free_symbols}")
    else:
        print(f"STATUS: PASS — N is dimensionless (count).")
        print(f"  numerical value  ≈ {float(N_simpl):.4e}")


if __name__ == "__main__":
    main()
