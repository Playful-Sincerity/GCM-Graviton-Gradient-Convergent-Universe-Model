#!/usr/bin/env python3
"""
Check 01 — Propositional encoding of the indivisibility argument.

Claim: S1-AX-1-F.
Goal:  Show that premises P1-P5 together with the reductio assumption
       {Prop_intrinsic(P, g), Physical(P)} is UNSAT at a fixed instantiation (g, P).
       If UNSAT, the theorem "no intrinsic physical property for indivisible g" holds.

Method: First-order premises are instantiated at a specific (g, P) pair and encoded
        as propositional formulas. SymPy's `satisfiable` is used to check UNSAT.

Expected result: UNSAT.
Tool:            Python 3 + SymPy 1.14.0 (via /tmp/gcm-verify-venv).
"""

import json
import os
import sys
from datetime import datetime

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable


HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS_PATH = os.path.join(HERE, "inputs.json")


def load_inputs():
    with open(INPUTS_PATH, "r") as f:
        return json.load(f)


def main():
    inputs = load_inputs()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"# Check: 01 — FOL propositional encoding (indivisibility)")
    print(f"# Claim: {inputs['claim_id']} — {inputs['claim_name']}")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} + sympy 1.14.0")
    print(f"# Script: verification/indivisibility-formal/check_01_fol_propositional.py")
    print("# ----")
    print()

    # Propositional variables — each is the instantiation of a predicate at (g, P).
    I, Np, Pr, Re, Br, Ph = symbols("I Np Pr Re Br Ph")
    # I  = Ind(g)
    # Np = exists y. Part(y, g)            ("has a proper part")
    # Pr = Prop_intrinsic(P, g)            (P is intrinsic, non-relational)
    # Re = Reduce(P, g)                    (P reduces to parts of g)
    # Br = Brute(P, g)                     (P is a brute primitive)
    # Ph = Physical(P)                     (P requires geometric/algebraic structure)

    # Premises (universally quantified claims instantiated at g, P):
    P1 = I                              # P1: Ind(g)
    P2 = Implies(I, Not(Np))            # P2: Ind(x) -> no proper parts
    P3 = Implies(Pr, Or(Re, Br))        # P3: intrinsic prop reduces or is brute
    P4 = Implies(Re, Np)                # P4: reduction requires parts
    P5 = Implies(Br, Not(Ph))           # P5: brute primitive is not physical

    premises = And(P1, P2, P3, P4, P5)

    # Reductio assumption: the graviton has an intrinsic PHYSICAL property P.
    reductio = And(Pr, Ph)

    conjecture = And(premises, reductio)

    # Labelled echo
    print("Premises:")
    print(f"  P1 (Ind(g)):                        {P1}")
    print(f"  P2 (Ind(x) -> not Np):              {P2}")
    print(f"  P3 (Pr -> Re or Br):                {P3}")
    print(f"  P4 (Re -> Np):                      {P4}")
    print(f"  P5 (Br -> not Ph):                  {P5}")
    print(f"Reductio assumption (Pr and Ph):      {reductio}")
    print(f"Conjunction tested for SAT:           {conjecture}")
    print()

    result = satisfiable(conjecture)

    if result is False:
        status = "PASS"
        print("Result:  UNSAT (no satisfying assignment)")
        print()
        print("Interpretation:")
        print("  Under P1-P5, a graviton CANNOT host a property that is both")
        print("  intrinsic (Pr) and physical (Ph). Therefore any property")
        print("  attributed to g must be non-intrinsic, i.e. relational.")
        print("  Theorem T holds.")
    else:
        status = "FAIL"
        print(f"Result:  SAT  — counterexample model: {result}")
        print("Theorem T does NOT follow from the stated premises.")
        print("Encoding or premise set is wrong — investigate.")

    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
