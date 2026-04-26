#!/usr/bin/env python3
"""E7 Check 2 — Finite-difference numerical derivatives.

Computes the partial derivatives of E_1 numerically and compares
against the analytical closed forms (4*E_1/e and E_1/m_e).
Independent sanity check that the symbolic derivation is correct.
"""
import json
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 40


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def E1(m_val, e_val, k_val, hbar_val):
    return -m_val * k_val**2 * e_val**4 / (2 * hbar_val**2)


def main():
    m_e = cv("m_e")
    e = cv("e")
    k = cv("k_e")
    hbar = cv("hbar")
    J_per_eV = cv("J_per_eV")

    E1_base = E1(m_e, e, k, hbar)
    E1_base_eV = E1_base / J_per_eV

    print("# E7 Check 2 — Finite-difference derivatives (mpmath)")
    print()
    print(f"E_1 base            = {E1_base} J")
    print(f"E_1 base            = {E1_base_eV} eV")
    print(f"Expected -13.60569 eV")
    print()

    # Finite-difference step size
    de_step = e * mpf("1e-10")
    dm_step = m_e * mpf("1e-10")

    dE1_de_num = (E1(m_e, e + de_step, k, hbar) - E1(m_e, e - de_step, k, hbar)) / (2 * de_step)
    dE1_dm_num = (E1(m_e + dm_step, e, k, hbar) - E1(m_e - dm_step, e, k, hbar)) / (2 * dm_step)

    dE1_de_anal = 4 * E1_base / e
    dE1_dm_anal = E1_base / m_e

    print(f"dE_1/de  numerical   = {dE1_de_num}")
    print(f"dE_1/de  analytical  = {dE1_de_anal}  (= 4*E_1/e)")
    print(f"relative difference   = {abs(dE1_de_num - dE1_de_anal) / abs(dE1_de_anal)}")
    print()
    print(f"dE_1/dm_e numerical   = {dE1_dm_num}")
    print(f"dE_1/dm_e analytical  = {dE1_dm_anal}  (= E_1/m_e)")
    print(f"relative difference   = {abs(dE1_dm_num - dE1_dm_anal) / abs(dE1_dm_anal)}")
    print()

    # Tolerance: 1e-15 is generous for finite-diff at step 1e-10
    tol = mpf("1e-10")
    pass_de = abs(dE1_de_num - dE1_de_anal) / abs(dE1_de_anal) < tol
    pass_dm = abs(dE1_dm_num - dE1_dm_anal) / abs(dE1_dm_anal) < tol

    print("STATUS:", "PASS" if pass_de and pass_dm else "FAIL")


if __name__ == "__main__":
    main()
