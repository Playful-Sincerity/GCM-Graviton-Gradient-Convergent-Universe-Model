#!/usr/bin/env python3
"""Q3 Check 2 — Convergence to the 10*Ry asymptote at large n.

Verifies the correction term 2*Ry/n^2 by checking |E_n|*P_n at large n.
"""
import json
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 40


def main():
    Ry = mpf(str(INPUTS["constants"]["Rydberg_eV_rounded"]["value"]))

    print("# Q3 Check 2 — Large-n convergence")
    print()
    print(f"Ry = {Ry} eV (session-brief convention)")
    print(f"Expected asymptote: {10 * Ry} eV")
    print(f"Expected correction: 2*Ry/n^2 = {2*Ry}/n^2 eV")
    print()
    print(f"{'n':>6}  {'|E_n|*P_n (eV)':>20}  {'deviation from 10Ry':>22}")
    for n in (1, 2, 5, 10, 100, 1000, 10000):
        P = 10 * n**2 + 2
        En_abs = Ry / mpf(n)**2
        prod = En_abs * P
        dev = prod - 10 * Ry
        expected_dev = 2 * Ry / mpf(n)**2
        print(f"{n:>6}  {str(prod)[:20]:>20}  {str(dev)[:22]:>22}  (expected {str(expected_dev)[:20]})")
    print()

    # Check the n=1000 case against expected correction
    n = 1000
    prod = (Ry / mpf(n)**2) * (10 * n**2 + 2)
    expected = 10 * Ry + 2 * Ry / mpf(n)**2
    rel_err = abs(prod - expected) / expected
    print(f"At n=1000, relative error between computed and (10Ry + 2Ry/n^2) = {rel_err}")
    print()

    passes = rel_err < mpf("1e-30")
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
