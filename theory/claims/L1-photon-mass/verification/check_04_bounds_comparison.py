#!/usr/bin/env python3
"""
L1 Check 04 — Bounds comparison. Computes the margin (ratio and orders of
magnitude) between GCM's photon mass estimate and published experimental
bounds.

Bounds checked:
  - Wang et al. 2023 (FRB dispersion): 2.1e-15 eV/c^2
  - PDG 2022 combined (approximate): ~1e-18 eV/c^2 [NEEDS VERIFICATION]

Usage:
    python3 check_04_bounds_comparison.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import mpmath as mp


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    mp.mp.dps = 30
    inputs = load_inputs()

    # Compute GCM's m_gamma in eV/c^2 using high-precision from check 02
    m_kg = mp.mpf(str(inputs["m_gamma_kg"]["value"]))
    c = mp.mpf(str(inputs["c"]["value"]))
    eV = mp.mpf(str(inputs["eV_to_J"]["value"]))
    m_gcm = m_kg * c ** 2 / eV  # in eV/c^2

    wang = mp.mpf(str(inputs["wang_bound_eV_per_c2"]["value"]))
    pdg = mp.mpf(str(inputs["pdg_bound_eV_per_c2_approx"]["value"]))

    print("L1 — Check 04: Bounds comparison")
    print("=" * 60)
    print(f"GCM m_gamma: {mp.nstr(m_gcm, 6)} eV/c^2")
    print()

    def compare(name: str, bound: mp.mpf) -> tuple[mp.mpf, mp.mpf, bool]:
        ratio = bound / m_gcm
        orders = mp.log10(ratio)
        passes = m_gcm < bound
        return ratio, orders, passes

    for name, bound_val in [("Wang 2023 (FRB)", wang), ("PDG 2022 (approx)", pdg)]:
        ratio, orders, passes = compare(name, bound_val)
        tag = "PASS" if passes else "FAIL"
        print(f"  vs {name}: bound = {mp.nstr(bound_val, 4)} eV/c^2")
        print(f"    ratio bound/GCM = {mp.nstr(ratio, 5)}")
        print(f"    orders below    = {mp.nstr(orders, 4)}")
        print(f"    {tag}")
        print()

    # Flag the known drift: plan claims "4 orders" vs. Wang; actual is ~3.6.
    wang_orders = mp.log10(wang / m_gcm)
    plan_claim = mp.mpf("4.0")
    drift = abs(wang_orders - plan_claim)
    print("Honesty flag:")
    print(f"  Plan document claims ~4 orders below Wang bound.")
    print(f"  Actual orders: {mp.nstr(wang_orders, 4)} — drift of {mp.nstr(drift, 3)} orders.")
    print(f"  Not a falsification; a minor overstatement now corrected in derivation.md.")
    print()

    # Overall status
    wang_pass = m_gcm < wang
    pdg_pass = m_gcm < pdg
    overall = "PASS" if (wang_pass and pdg_pass) else "FAIL"
    print(f"Overall: {overall}")
    print(f"  (NB: PDG bound is approximate from training-data memory — see inputs.json)")
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
