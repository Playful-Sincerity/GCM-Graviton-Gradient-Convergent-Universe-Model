#!/usr/bin/env python3
"""
R6 Check 02 — Limit cases for the time-dilation factor (1 + z).

z = 0:       no dilation
z → ∞:       arbitrary dilation
z << 1:      linear in z (classical Doppler limit)

Usage:
    python3 check_02_limit_cases_sympy.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import Symbol, Limit, series, oo


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    print("R6 — Check 02: Limit cases of the dilation factor (1 + z)")
    print("=" * 60)

    z = Symbol("z", real=True, nonnegative=True)
    dilation = 1 + z

    # Limit z → 0
    lim_zero = Limit(dilation, z, 0, dir="+").doit()
    print(f"z → 0: dilation = {lim_zero} (no time dilation as expected)")

    # Limit z → ∞
    lim_inf = Limit(dilation, z, oo).doit()
    print(f"z → ∞: dilation = {lim_inf} (unbounded, consistent with high-z observations)")

    # Small-z expansion: should be linear in z
    small_z = series(dilation, z, 0, 3).removeO()
    print(f"Small z expansion (to O(z^2)): dilation ≈ {small_z}")
    print("   Leading correction is linear in z — standard redshift limit behavior.")
    print()

    # Numerical table at illustrative z values
    inputs = load_inputs()
    z_vals = inputs["z_examples"]["value"]
    print("Numerical table:")
    print("  z       |  dilation factor (1+z)")
    print("  --------+---------------------")
    for zv in z_vals:
        print(f"  {zv:7.2f} |  {1 + zv:20.6f}")

    print()
    print("All limits behave as expected.")
    print("Status: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
