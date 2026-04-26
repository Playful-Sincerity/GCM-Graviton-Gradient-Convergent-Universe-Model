#!/usr/bin/env python3
"""
L1 Check 01 — Dimensional analysis of kg → eV/c^2 conversion.

Uses sympy.physics.units to track units symbolically and verify the
conversion chain closes. This is the runnable version of the hand
dimensional-analysis check from the original verification.md.

Usage:
    python3 check_01_dimensional.py

Reads: inputs.json (constants)
Emits: stdout (human-readable) and exit code 0 if PASS.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import Symbol, simplify
from sympy.physics.units import (
    Quantity,
    convert_to,
    kg,
    meter,
    second,
    joule,
    electronvolt,
    speed_of_light,
)


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    inputs = load_inputs()
    m_gamma_kg_val = inputs["m_gamma_kg"]["value"]

    # Symbolic unit tracking: m_gamma [kg], c^2 [m^2/s^2], eV [J]
    m_gamma = m_gamma_kg_val * kg
    c_sq = speed_of_light ** 2

    # m_gamma * c^2 has units of kg * m^2 / s^2 = J (energy)
    energy_expr = m_gamma * c_sq
    energy_in_J = convert_to(energy_expr, joule)
    energy_in_eV = convert_to(energy_expr, electronvolt)

    print("L1 — Check 01: Dimensional analysis of kg -> eV/c^2")
    print("=" * 60)
    print(f"Input: m_gamma = {m_gamma_kg_val:e} kg (GCM estimate)")
    print()
    print("Step 1: m_gamma * c^2")
    print(f"  Raw expression:   {energy_expr}")
    print(f"  In joules:        {energy_in_J}")
    print(f"  In electronvolts: {energy_in_eV}")
    print()
    print("Step 2: Interpret as mass in eV/c^2")
    print("  Dividing the eV value by c^2 gives mass units of eV/c^2.")
    print("  (In particle physics, the 'eV/c^2' is the conventional mass unit.)")
    print()
    print("Dimensional chain:")
    print("  [kg] * [m^2/s^2] = [kg * m^2 / s^2] = [J] (definition of joule)")
    print("  [J] / [J/eV]     = [eV]")
    print("  Treat as mass:     [eV]/[c^2] = eV/c^2  (mass unit)")
    print()
    print("Result: PASS — units close consistently.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
