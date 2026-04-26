#!/usr/bin/env python3
"""
R6 Check 03 — DES 2024 comparison.

R6 predicts α = 1.000 for the time-dilation exponent in (1+z)^α.
DES 2024 (arXiv:2406.05050) measures α = 1.003 ± 0.005.

Compute the σ-distance between R6's prediction and DES's central value.

Usage:
    python3 check_03_des_2024_comparison.py
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
    mp.mp.dps = 30
    inputs = load_inputs()

    alpha_des = mp.mpf(str(inputs["des_2024_alpha_central"]["value"]))
    sigma_des = mp.mpf(str(inputs["des_2024_alpha_sigma"]["value"]))
    alpha_r6 = mp.mpf(str(inputs["r6_alpha"]["value"]))

    print("R6 — Check 03: DES 2024 comparison")
    print("=" * 60)
    print(f"DES 2024 measured α: {alpha_des} ± {sigma_des}")
    print(f"R6 predicted α:     {alpha_r6} (exact)")
    print()

    diff = abs(alpha_r6 - alpha_des)
    sigma_distance = diff / sigma_des

    print(f"|α_R6 - α_DES|  = {mp.nstr(diff, 6)}")
    print(f"σ-distance       = {mp.nstr(sigma_distance, 4)}σ")
    print()

    # 1σ interval
    lower = alpha_des - sigma_des
    upper = alpha_des + sigma_des
    in_1sigma = (alpha_r6 >= lower) and (alpha_r6 <= upper)
    print(f"DES 1σ interval for α: [{lower}, {upper}]")
    print(f"R6's α = {alpha_r6} in interval? {in_1sigma}")
    print()

    # Comparison to tired-light null
    alpha_tired = mp.mpf("0")
    tired_distance = abs(alpha_des - alpha_tired) / sigma_des
    print(f"Tired-light null (α = 0): excluded at {mp.nstr(tired_distance, 4)}σ")
    print(f"R6 is structurally distinct from tired light and passes the test.")
    print()

    status = "PASS" if in_1sigma else "FAIL"
    print(f"Status: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
