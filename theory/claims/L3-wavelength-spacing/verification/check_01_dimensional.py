#!/usr/bin/env python3
"""
L3 Check 01 — Dimensional analysis of λ = N · d.

Uses SymPy units to verify [λ] = [N]·[d] is dimensionally consistent.

Usage:
    python3 check_01_dimensional.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import Symbol
from sympy.physics.units import meter, Dimension
from sympy.physics.units.systems.si import dimsys_SI


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    # Dimensions
    length = Dimension("length")
    dimensionless = Dimension(1)

    lam_dim = length
    N_dim = dimensionless  # cluster count per wavelength
    d_dim = length

    product_dim = N_dim * d_dim

    print("L3 — Check 01: Dimensional analysis of λ = N · d")
    print("=" * 60)
    print(f"[λ] = {lam_dim}")
    print(f"[N] = {N_dim}")
    print(f"[d] = {d_dim}")
    print(f"[N · d] = {product_dim}")
    print()

    # They should be equivalent
    equal = dimsys_SI.equivalent_dims(lam_dim, product_dim)
    print(f"[λ] equivalent to [N · d]? {equal}")

    status = "PASS" if equal else "FAIL"
    print(f"\nStatus: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
