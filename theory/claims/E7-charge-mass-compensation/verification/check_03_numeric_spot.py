#!/usr/bin/env python3
"""E7 Check 3 — Numerical spot check against the session-brief example.

Delta_e = 1e-35 C should yield Delta_m_e ≈ -2.27e-46 kg per the
brief's stated example.
"""
import json
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 30


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    m_e = cv("m_e")
    e = cv("e")
    Delta_e = mpf(str(INPUTS["perturbation_example"]["Delta_e"]["value"]))
    expected_Dm = mpf(str(INPUTS["perturbation_example"]["Delta_m_e_expected"]["value"]))

    # E7 relation: Delta_m_e / m_e = -4 Delta_e / e  =>  Delta_m_e = -4 * m_e * Delta_e / e
    Dm_computed = -4 * m_e * Delta_e / e

    print("# E7 Check 3 — Numerical spot check")
    print()
    print(f"Inputs from session brief:")
    print(f"  Delta_e       = {Delta_e} C")
    print(f"  m_e           = {m_e} kg")
    print(f"  e             = {e} C")
    print()
    print(f"Computed Delta_m_e = -4 * m_e * Delta_e / e = {Dm_computed} kg")
    print(f"Brief stated value                          = {expected_Dm} kg")
    print()

    rel_err = abs(Dm_computed - expected_Dm) / abs(expected_Dm)
    print(f"Relative difference = {rel_err}")
    print(f"  (~{rel_err * 100} %)")
    print()

    # The brief's value is rounded to 3 sig figs; 1% tolerance is appropriate
    tol = mpf("0.01")
    passes = rel_err < tol
    print("STATUS:", "PASS" if passes else "FAIL")
    print(f"  Interpretation: 0.2% difference is rounding in the brief's stated value, not a computational error.")


if __name__ == "__main__":
    main()
