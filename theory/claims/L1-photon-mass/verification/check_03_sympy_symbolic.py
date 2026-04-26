#!/usr/bin/env python3
"""
L1 Check 03 — SymPy symbolic derivation of the kg -> eV/c^2 conversion.

Keeps everything symbolic, substitutes inputs only at the end. This
guards against the numerical check hiding a conceptual error in the
algebra.

Usage:
    python3 check_03_sympy_symbolic.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import symbols, simplify, N, Rational


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    inputs = load_inputs()

    # Symbolic variables
    m, c, eV_to_J = symbols("m c eV_to_J", positive=True, real=True)

    # Claim: mass in eV/c^2 equals (m * c^2) / eV_to_J, in units of eV
    # (then reinterpreted as eV/c^2 for mass).
    expr_symbolic = (m * c ** 2) / eV_to_J

    # Substitute inputs
    subs = {
        m: Rational(str(inputs["m_gamma_kg"]["value"])),
        c: Rational(str(inputs["c"]["value"])),
        eV_to_J: Rational(str(inputs["eV_to_J"]["value"])),
    }
    expr_val = simplify(expr_symbolic.subs(subs))
    numeric = N(expr_val, 20)  # 20 significant digits

    print("L1 — Check 03: SymPy symbolic derivation")
    print("=" * 60)
    print(f"Symbolic expression: m * c^2 / eV_to_J")
    print(f"  = {expr_symbolic}")
    print()
    print(f"After substitution of inputs:")
    print(f"  Exact rational: {expr_val}")
    print(f"  Numeric (20 sig figs): {numeric}")
    print()

    # Compare to hand value
    expected = Rational("561", "1000") * Rational(10) ** -18  # 5.61e-19
    rel_err = abs(expr_val - expected) / expected
    print(f"Hand value (3 sig figs): 5.61e-19")
    print(f"Relative error: {N(rel_err, 5)}")

    status = "PASS" if abs(rel_err) < 0.01 else "FAIL"
    print(f"\nStatus: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
