#!/usr/bin/env python3
"""Q3 Check 1 — Exact-arithmetic tabulation.

Uses SymPy's Rational type to compute the E_n * P_n table at exact
arithmetic (not floating-point), with the conventional Ry = 13.6 eV
and the CODATA-precise Ry = 13.605693... eV both shown.
"""
import json
from pathlib import Path
from sympy import Rational, Symbol, limit, oo, simplify, nsimplify

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())


def main():
    Ry_rounded = Rational(136, 10)  # 13.6 eV
    Ry_codata = Rational(INPUTS["constants"]["Rydberg_eV"]["value"]).limit_denominator(10**12)

    print("# Q3 Check 1 — Exact-arithmetic tabulation via SymPy Rational")
    print()
    print("Using Ry = 13.6 eV (session-brief convention):")
    print(f"{'n':>3}  {'P_n':>6}  {'|E_n| (eV)':>14}  {'|E_n|*P_n (eV)':>16}")
    for n in range(1, 6):
        P = 10 * n**2 + 2
        En_abs = Ry_rounded / (n**2)
        prod = En_abs * P
        print(f"{n:>3}  {P:>6d}  {str(En_abs):>14}  {str(prod):>16}  (= {float(prod):.4f})")
    print()

    # Asymptote (symbolic)
    n_sym = Symbol('n', positive=True, integer=True)
    prod_sym = (Ry_rounded / n_sym**2) * (10 * n_sym**2 + 2)
    asymptote = limit(prod_sym, n_sym, oo)
    print(f"Symbolic asymptote lim_{{n→∞}} |E_n|*P_n = {asymptote} eV")
    print(f"Session brief's expected asymptote: 136.0 eV (= 10 * Ry)")
    print(f"Match: {asymptote == Rational(1360, 10)}")
    print()

    # Same with CODATA Ry
    print(f"With CODATA Ry = {float(Ry_codata)} eV, asymptote = {float(10 * Ry_codata)} eV")
    print()

    # Variation across n=1..5
    products = [(Ry_rounded / n**2) * (10 * n**2 + 2) for n in range(1, 6)]
    max_p = max(products)
    min_p = min(products)
    variation = float((max_p - min_p) / max_p) * 100
    print(f"Variation (max-min)/max across n=1..5: {variation:.2f}%")
    print()
    passes = (asymptote == Rational(1360, 10)) and (variation < 20)
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
