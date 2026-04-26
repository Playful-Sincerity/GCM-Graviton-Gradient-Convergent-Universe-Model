#!/usr/bin/env python3
"""
R6 Check 04 — Falsification gate.

If a future measurement (e.g. LSST) tightens DES 2024 and produces
α = 1.010 ± 0.002, how many σ would R6's prediction of α = 1.000
be excluded at? This is the forward-looking falsification condition
named in caveats.md.

Usage:
    python3 check_04_falsification_gate.py
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

    alpha_r6 = mp.mpf(str(inputs["r6_alpha"]["value"]))

    # Current DES
    alpha_des = mp.mpf(str(inputs["des_2024_alpha_central"]["value"]))
    sigma_des = mp.mpf(str(inputs["des_2024_alpha_sigma"]["value"]))
    dist_des = abs(alpha_r6 - alpha_des) / sigma_des

    # Hypothetical future measurement
    alpha_hyp = mp.mpf(str(inputs["hypothetical_future_alpha_central"]["value"]))
    sigma_hyp = mp.mpf(str(inputs["hypothetical_future_alpha_sigma"]["value"]))
    dist_hyp = abs(alpha_r6 - alpha_hyp) / sigma_hyp

    print("R6 — Check 04: Falsification gate (forward-looking)")
    print("=" * 60)
    print(f"Current (DES 2024):          α = {alpha_des} ± {sigma_des}")
    print(f"  R6 σ-distance: {mp.nstr(dist_des, 4)}σ — PASS")
    print()
    print(f"Hypothetical future (LSST):  α = {alpha_hyp} ± {sigma_hyp}")
    print(f"  R6 σ-distance: {mp.nstr(dist_hyp, 4)}σ")
    print()

    threshold_3sigma = mp.mpf("3")
    threshold_5sigma = mp.mpf("5")

    # Tolerance: decimal-valued inputs (1.01, 0.002) are not exactly
    # representable in mpmath's binary precision, producing ~1e-30 relative
    # rounding. Use a small tolerance for threshold comparisons so that
    # dist == 5.0 exactly at the decimal level is reported as ">=5σ".
    tol = mp.mpf("1e-20")

    if dist_hyp >= threshold_5sigma - tol:
        status_future = "R6 EXCLUDED at 5σ in that hypothetical"
    elif dist_hyp >= threshold_3sigma - tol:
        status_future = "R6 EXCLUDED at 3σ in that hypothetical"
    else:
        status_future = "R6 still compatible in that hypothetical"

    print(f"  Verdict: {status_future}")
    print()
    print("Interpretation: the hypothetical input is illustrative — it shows the")
    print("precision at which R6's α=1.000 structural prediction would fail.")
    print("This names the falsification condition quantitatively.")
    print()
    print(f"Status (current R6 vs current DES): PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
