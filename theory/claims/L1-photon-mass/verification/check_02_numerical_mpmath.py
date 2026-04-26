#!/usr/bin/env python3
"""
L1 Check 02 — High-precision numerical conversion: m_gamma (kg) -> eV/c^2.

Uses mpmath at 50-digit precision. This is the canonical numeric check.

Usage:
    python3 check_02_numerical_mpmath.py

Reads: inputs.json
Emits: stdout with both the hand value (5.61e-19 eV/c^2) and the
       high-precision value for cross-check.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    mp.mp.dps = 50  # 50 decimal digits

    inputs = load_inputs()
    m_gamma_kg = mp.mpf(str(inputs["m_gamma_kg"]["value"]))
    c = mp.mpf(str(inputs["c"]["value"]))
    eV_to_J = mp.mpf(str(inputs["eV_to_J"]["value"]))

    # Step-by-step at high precision
    c_sq = c ** 2
    energy_J = m_gamma_kg * c_sq
    energy_eV = energy_J / eV_to_J
    m_gamma_eV_per_c2 = energy_eV  # numerically the same number; the unit is eV/c^2

    print("L1 — Check 02: Numerical conversion (mpmath, 50 dps)")
    print("=" * 60)
    print(f"Inputs:")
    print(f"  m_gamma = {mp.nstr(m_gamma_kg, 10)} kg")
    print(f"  c       = {mp.nstr(c, 15)} m/s")
    print(f"  eV->J   = {mp.nstr(eV_to_J, 15)} J/eV")
    print()
    print("Computation:")
    print(f"  c^2           = {mp.nstr(c_sq, 15)} m^2/s^2")
    print(f"  m_gamma * c^2 = {mp.nstr(energy_J, 15)} J")
    print(f"  / eV_to_J     = {mp.nstr(energy_eV, 15)} eV")
    print()
    print(f"Result: m_gamma = {mp.nstr(m_gamma_eV_per_c2, 15)} eV/c^2")
    print()

    # Compare to the hand-calc value cited in verification.md
    hand_value = mp.mpf("5.61e-19")
    rel_err = abs(m_gamma_eV_per_c2 - hand_value) / hand_value
    print(f"Hand-calc value (from derivation.md): 5.61e-19 eV/c^2")
    print(f"Relative error vs. high-precision: {mp.nstr(rel_err, 5)}")

    # The hand value is rounded to 3 sig figs; agreement to <1% is expected.
    if rel_err < mp.mpf("0.01"):
        status = "PASS"
    else:
        status = "FAIL"
    print()
    print(f"Status: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
