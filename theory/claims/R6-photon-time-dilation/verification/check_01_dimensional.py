#!/usr/bin/env python3
"""
R6 Check 01 — Dimensional consistency of Δt = d / v.

Uses SymPy units to confirm the dilation factor is dimensionless and
the inter-arrival time Δt has units of seconds.

Usage:
    python3 check_01_dimensional.py

Note: We use v (photon speed, strictly < c) rather than c. In GCM's
convention, c denotes the causality limit, not the photon speed.
"""

from __future__ import annotations

import sys

from sympy.physics.units import Dimension
from sympy.physics.units.systems.si import dimsys_SI


def main() -> int:
    length = Dimension("length")
    time = Dimension("time")
    velocity = length / time
    dimensionless = Dimension(1)

    # Δt = d / v
    delta_t_dim = length / velocity

    print("R6 — Check 01: Dimensional consistency of Δt = d / v")
    print("=" * 60)
    print(f"[d] = {length}")
    print(f"[v] = {velocity} (photon speed, < c)")
    print(f"[d / v] = {delta_t_dim}")
    print()

    delta_t_pass = dimsys_SI.equivalent_dims(delta_t_dim, time)
    print(f"Δt has units of time? {delta_t_pass}")

    # Ratio Δt_obs / Δt_emit is dimensionless
    ratio_dim = time / time
    ratio_pass = dimsys_SI.equivalent_dims(ratio_dim, dimensionless)
    print(f"Δt_obs/Δt_emit dimensionless? {ratio_pass}")

    # (1 + z) is dimensionless by definition
    print("(1 + z) dimensionless: yes by definition of redshift z.")

    status = "PASS" if (delta_t_pass and ratio_pass) else "FAIL"
    print(f"\nStatus: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
