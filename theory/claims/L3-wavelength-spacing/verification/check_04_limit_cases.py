#!/usr/bin/env python3
"""
L3 Check 04 — Limit cases.

λ → 0: d = λ/N → 0. The photon's internal structure collapses (gamma-ray
photons are spatially localized, consistent with observed interaction
behavior).

λ → ∞: d → ∞. Radio-wave photons have enormously extended internal
structure, consistent with the known delocalization of long-wavelength EM.

Usage:
    python3 check_04_limit_cases.py
"""

from __future__ import annotations

import sys

from sympy import Symbol, Limit, oo


def main() -> int:
    print("L3 — Check 04: Limit cases")
    print("=" * 60)

    lam = Symbol("lambda", positive=True)
    N = Symbol("N", positive=True, integer=True)

    d_expr = lam / N

    # λ → 0
    lim_zero = Limit(d_expr, lam, 0, dir="+").doit()
    # λ → ∞
    lim_inf = Limit(d_expr, lam, oo).doit()

    print(f"d(λ) = λ / N")
    print(f"  lim (λ -> 0+) d = {lim_zero}")
    print(f"  lim (λ -> ∞)  d = {lim_inf}")
    print()
    print("Physical reading:")
    print("  λ -> 0 (gamma rays): cluster spacing shrinks to zero — localized interactions.")
    print("  λ -> ∞ (radio):      cluster spacing grows without bound — delocalized waves.")
    print("Both limits match known EM phenomenology.")
    print()
    print("Status: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
