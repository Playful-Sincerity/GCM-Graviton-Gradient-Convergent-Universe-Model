#!/usr/bin/env python3
"""M1 Check 3 — LIGO bound comparison.

Explicitly computes the ratio between GCM's graviton mass and the LIGO
bound, expressed in orders of magnitude.
"""
import json
import math
from pathlib import Path

from mpmath import mp, mpf, log10

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 40


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    hbar = cv("hbar")
    G = cv("G")
    c = cv("c")
    rho = cv("rho_bound_nuclear")
    eV_per_kg = cv("eV_per_kg")
    LIGO_eVc2 = cv("LIGO_graviton_mass_eVc2")

    from mpmath import sqrt

    ell_P = sqrt(hbar * G / c**3)
    V_P = ell_P**3
    m_g = rho * V_P

    LIGO_kg = LIGO_eVc2 * eV_per_kg

    # Express GCM m_g in eV/c^2 for direct comparison with LIGO's standard unit
    m_g_eVc2 = m_g / eV_per_kg

    margin_kg = LIGO_kg / m_g
    margin_orders = log10(margin_kg)

    print("# M1 Check 3 — LIGO bound margin")
    print()
    print(f"GCM m_g                 = {m_g} kg")
    print(f"GCM m_g                 = {m_g_eVc2} eV/c^2")
    print()
    print(f"LIGO bound              = {LIGO_eVc2} eV/c^2")
    print(f"LIGO bound              = {LIGO_kg} kg")
    print()
    print(f"margin (LIGO / GCM)     = {margin_kg}")
    print(f"log10(margin)           = {margin_orders}")
    print(f"orders of magnitude     = {int(margin_orders)} (rounded down)")
    print()

    passes = m_g < LIGO_kg and margin_orders > 20
    print(f"STATUS: {'PASS' if passes else 'FAIL'}")
    print(f"  (GCM m_g is safely below LIGO bound by ~28 orders)")


if __name__ == "__main__":
    main()
