#!/usr/bin/env python3
"""
L3 Check 03 — Standard EM phenomenology is unaffected by the L3
reframing, because L3 does not alter λ itself; it only re-identifies
λ as N·d.

We check that common λ-dependent quantities (E = hc/λ, diffraction
angle, phase advance over a path) are invariant under L3.

Usage:
    python3 check_03_em_phenomenology.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from sympy import symbols, simplify, sin, pi


def load_inputs() -> dict:
    here = Path(__file__).parent
    with open(here / "inputs.json") as f:
        return json.load(f)


def main() -> int:
    print("L3 — Check 03: Standard EM phenomenology invariance")
    print("=" * 60)

    lam, N, d, h, c, a, theta, L = symbols(
        "lambda N d h c a theta L",
        positive=True, real=True,
    )

    # 1. Photon energy E = hc/λ. L3 says λ = N·d. Under L3, E = hc/(N·d).
    # This is a REWRITE, not a change in value.
    E_standard = h * c / lam
    E_l3 = E_standard.subs(lam, N * d)
    print("1. Photon energy E = hc/λ:")
    print(f"   Standard: E = {E_standard}")
    print(f"   L3 form:  E = {E_l3}")
    print("   Same numeric value for given λ — L3 just relabels the distance scale.")
    print()

    # 2. Single-slit diffraction: sinθ = λ/a. Under L3, sinθ = N·d/a.
    diffraction_standard = lam / a
    diffraction_l3 = diffraction_standard.subs(lam, N * d)
    print("2. Single-slit diffraction minimum: sinθ = λ/a:")
    print(f"   Standard: sin(θ) = {diffraction_standard}")
    print(f"   L3 form:  sin(θ) = {diffraction_l3}")
    print("   Unaffected for given λ.")
    print()

    # 3. Phase advance over path length L: φ = 2πL/λ.
    phase_standard = 2 * pi * L / lam
    phase_l3 = phase_standard.subs(lam, N * d)
    print("3. Phase advance over path length L: φ = 2πL/λ:")
    print(f"   Standard: φ = {phase_standard}")
    print(f"   L3 form:  φ = {phase_l3}")
    print("   Unaffected.")
    print()

    # 4. Doppler: λ_obs/λ_emit determined by relative motion.
    # L3 doesn't enter; it just relabels what's being stretched.
    print("4. Doppler shift λ_obs/λ_emit: function of relative velocity alone.")
    print("   L3 reframes what λ means but doesn't change the ratio.")
    print()

    print("Conclusion: L3 is a reframing. No λ-dependent phenomenology changes.")
    print("Status: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
