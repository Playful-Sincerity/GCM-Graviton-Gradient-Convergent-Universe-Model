#!/usr/bin/env python3
"""
Check 03 — Premise-dependency scan.

Claim: S1-AX-1-F.
Goal:  For each of P1-P5, remove it from the premise set and confirm that
       the reductio conjunction becomes SAT (i.e., the theorem fails without
       that premise). This confirms every premise is load-bearing and none
       is redundant.

Expected result: removing any of P1-P5 individually makes the conjunction SAT.
Tool:            Python 3 + SymPy 1.14.0.
"""

import sys
from datetime import datetime

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("# Check: 03 — Premise-dependency scan")
    print("# Claim: S1-AX-1-F — Indivisibility Axiom — Formal Derivation")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} + sympy 1.14.0")
    print("# Script: verification/indivisibility-formal/check_03_premise_dependency_scan.py")
    print("# ----")
    print()

    I, Np, Pr, Re, Br, Ph = symbols("I Np Pr Re Br Ph")
    reductio = And(Pr, Ph)

    premises = {
        "P1 (Ind(g))":                 I,
        "P2 (Ind -> not Np)":          Implies(I, Not(Np)),
        "P3 (Pr -> Re or Br)":         Implies(Pr, Or(Re, Br)),
        "P4 (Re -> Np)":               Implies(Re, Np),
        "P5 (Br -> not Ph)":           Implies(Br, Not(Ph)),
    }

    names = list(premises.keys())

    # Full conjunction — baseline UNSAT.
    full = And(*premises.values(), reductio)
    print(f"Baseline (all premises + reductio): {satisfiable(full)}")
    print("  Expected: False (UNSAT).")
    print()

    all_dependent = True
    for skip in names:
        remaining = [v for k, v in premises.items() if k != skip]
        weakened = And(*remaining, reductio)
        result = satisfiable(weakened)
        expected_sat = True
        got_sat = bool(result)
        ok = got_sat == expected_sat
        marker = "OK" if ok else "NOT OK"
        print(f"Remove {skip}:")
        print(f"  satisfiable? {result}")
        print(f"  ({marker} — expected SAT; premise is load-bearing)")
        if not ok:
            all_dependent = False
        print()

    # Summary
    if all_dependent:
        status = "PASS"
        print("All five premises are load-bearing — removing any one breaks the theorem.")
        print("No redundancy in the premise set.")
    else:
        status = "FAIL"
        print("At least one premise is redundant — investigate.")
    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
