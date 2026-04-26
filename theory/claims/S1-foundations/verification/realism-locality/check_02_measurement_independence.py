#!/usr/bin/env python3
"""
Check 02 — Measurement-independence denial is coherent.

Claim: S1-RL-1.
Goal:  Show that denying Measurement Independence (ρ(λ | a, b) = ρ(λ)) is a
       well-defined logical move that does not entail denying Locality or
       Realism. The superdeterministic move is consistent, not smuggled.

Method: Encode two auxiliary propositions capturing the common-history
        explanation of correlations, and check that GCM's {Lo, Re, ¬MI}
        together with the common-history explanation (CH) is SAT.

Expected result:
  - {Lo, Re, ¬MI, CH, (¬MI → CH)} is SAT.
  - {Lo, Re, ¬MI, CH, (CH → ¬FTL)} is SAT — denying MI does not force FTL.
Tool: Python 3 + SymPy 1.14.0.
"""

import sys
from datetime import datetime

from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies
from sympy.logic.inference import satisfiable


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("# Check: 02 — Measurement-independence denial is coherent")
    print("# Claim: S1-RL-1")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} + sympy 1.14.0")
    print("# Script: verification/realism-locality/check_02_measurement_independence.py")
    print("# ----")
    print()

    # Base Bell variables
    Lo, Re, MI = symbols("Lo Re MI")
    # Auxiliary:
    # CH = Common-History correlation (shared causal past of λ, a, b).
    # FTL = faster-than-light signaling required to explain correlations.
    CH, FTL = symbols("CH FTL")

    # Premises:
    # (AX1) Superdeterministic reading: denying MI is explained by CH.
    AX1 = Implies(Not(MI), CH)
    # (AX2) Common history does not require FTL.
    AX2 = Implies(CH, Not(FTL))
    # (AX3) Locality forbids FTL.
    AX3 = Implies(Lo, Not(FTL))

    # GCM commitments:
    gcm = And(Lo, Re, Not(MI))

    conjecture = And(AX1, AX2, AX3, gcm, CH)
    print(f"Premises: AX1 (¬MI → CH), AX2 (CH → ¬FTL), AX3 (Lo → ¬FTL)")
    print(f"GCM commitment: Lo ∧ Re ∧ ¬MI ∧ CH")
    print()
    r1 = satisfiable(conjecture)
    print(f"Is this SAT? {r1}")
    if r1:
        print("OK — the superdeterministic commitment is consistent with locality,")
        print("realism, and common-history causation; no FTL is entailed.")
        ok_a = True
    else:
        print("FAIL — encoding is wrong or axioms are inconsistent.")
        ok_a = False
    print()

    # Negative control: if we ASSERT FTL while holding Lo, should be UNSAT.
    ctrl = And(Lo, FTL, AX3)
    r2 = satisfiable(ctrl)
    print(f"Negative control (Lo ∧ FTL): {r2}")
    if r2 is False:
        print("OK — Lo is incompatible with FTL (expected).")
        ok_b = True
    else:
        print("FAIL — Lo should rule out FTL.")
        ok_b = False
    print()

    # Secondary: the superdeterministic choice blocks the FTL "conspiracy" objection.
    # If denying MI forced FTL, GCM would have no coherent move. Show it does NOT.
    blocked = And(AX1, AX2, Not(MI), Lo, AX3)
    # Can we derive ¬FTL here? Equivalently, is (blocked ∧ FTL) UNSAT?
    r3 = satisfiable(And(blocked, FTL))
    print(f"Can GCM have ¬MI and FTL simultaneously given AX1–AX3? {r3}")
    if r3 is False:
        print("OK — from ¬MI and the axioms, FTL follows false. Conspiracy objection")
        print("does not force GCM into faster-than-light signaling.")
        ok_c = True
    else:
        print(f"Counterexample: {r3}")
        ok_c = False

    print()
    if ok_a and ok_b and ok_c:
        status = "PASS"
        print("Denying measurement independence is a consistent and locality-preserving")
        print("move under the common-history causal reading. GCM's superdeterminism")
        print("does not smuggle nonlocality through the back door.")
    else:
        status = "FAIL"

    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
