#!/usr/bin/env python3
"""
Check 02 — Atomic mereology: Atom(g) theorem.

Claim: S1-AX-1-F.
Goal:  Encode the classical-mereology atom definition and verify that Atom(g)
       is incompatible with the existence of any proper part of g.

Premises (Simons 1987 §1.1, simplified to propositional instantiation):
  (defAtom)  Atom(g) iff (not exists y. Part(y, g))
  (AM5)      Atom(g)

Target theorem: given AM5 and defAtom, assuming Part(y, g) for some y leads to
                contradiction.

Expected result: UNSAT for the conjunction {Atom(g), defAtom, Part(y, g)}.
Tool:            Python 3 + SymPy 1.14.0.
"""

import os
import sys
from datetime import datetime

from sympy import symbols
from sympy.logic.boolalg import And, Not, Equivalent
from sympy.logic.inference import satisfiable


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("# Check: 02 — Atomic mereology Atom theorem")
    print("# Claim: S1-AX-1-F — Indivisibility Axiom — Formal Derivation")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} + sympy 1.14.0")
    print("# Script: verification/indivisibility-formal/check_02_mereology_atom.py")
    print("# ----")
    print()

    # At a fixed candidate y, encode:
    # Part_yg: y is a proper part of g
    # Atom_g:  g is a mereological atom
    Part_yg, Atom_g = symbols("Part_yg Atom_g")

    # Definition of atom (existentially closed): Atom(g) iff no proper part exists
    # Because we are working at a single representative y, we encode
    # Atom_g iff (not Part_yg). This is the propositional projection of the
    # quantified definition for the representative witness; any proper part
    # y would make the right-hand side false.
    defAtom = Equivalent(Atom_g, Not(Part_yg))

    # AM5 (Atom axiom instantiated): Atom(g)
    AM5 = Atom_g

    # Reductio: assume some y is a proper part of g
    reductio = Part_yg

    conjecture = And(defAtom, AM5, reductio)

    print("Premises:")
    print(f"  defAtom (Atom(g) iff not Part(y,g)): {defAtom}")
    print(f"  AM5    (Atom(g)):                    {AM5}")
    print(f"  Reductio (Part(y,g)):                {reductio}")
    print(f"Conjunction tested for SAT:            {conjecture}")
    print()

    result = satisfiable(conjecture)

    if result is False:
        status = "PASS"
        print("Result:  UNSAT")
        print()
        print("Interpretation:")
        print("  Atom(g) is inconsistent with the existence of a proper part.")
        print("  Theorem AM-T holds: Atom(g) -> not Part(y, g) for any y.")
    else:
        status = "FAIL"
        print(f"Result:  SAT — counterexample model: {result}")
        print("Encoding is wrong — check defAtom and AM5 formulation.")

    print()

    # Secondary check: with AM5 removed, the reductio should be satisfiable.
    # This is a negative control ensuring our encoding is not trivially UNSAT.
    weaker = And(defAtom, reductio)
    neg_ctrl = satisfiable(weaker)
    print("Negative control (AM5 removed):")
    print(f"  defAtom ∧ Part(y,g) satisfiable? {neg_ctrl}")
    if neg_ctrl:
        print("  Expected SAT — confirms AM5 is doing the UNSAT work above.")
    else:
        print("  Unexpected UNSAT — something else in the encoding forces the result.")

    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
