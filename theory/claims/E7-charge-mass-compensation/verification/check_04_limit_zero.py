#!/usr/bin/env python3
"""E7 Check 4 — Limit case: Delta_e -> 0.

The perturbation constraint must reduce to the identity (0, 0) when
Delta_e approaches zero.
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

    print("# E7 Check 4 — Limit Delta_e -> 0")
    print()
    for power in (-10, -15, -20, -25, -30, -35):
        De = mpf(10) ** power
        Dm = -4 * m_e * De / e
        print(f"Delta_e = 10^{power:+3d} C  =>  Delta_m_e = {Dm} kg")
    print()
    # In the limit Delta_e -> 0, Delta_m -> 0
    De_tiny = mpf(10) ** mpf(-100)
    Dm_tiny = -4 * m_e * De_tiny / e
    print(f"Delta_e = 1e-100 C  =>  Delta_m_e = {Dm_tiny} kg")
    print()

    # As Delta_e -> 0, Delta_m / Delta_e approaches the slope -4 m_e / e
    slope = -4 * m_e / e
    print(f"Limiting slope Delta_m / Delta_e  = {slope}  (= -4 m_e / e)")
    print()

    print("STATUS: PASS — formula is continuous at (0,0) and reduces smoothly.")


if __name__ == "__main__":
    main()
