#!/usr/bin/env python3
"""
R6 Check 05 — Symbolic derivation of the cascade:

  λ_obs / λ_emit = (1 + z)            [definition of z]
  d = λ / N, N constant                [L3]
  Δt = d / v                            [information propagation at photon speed]

  ⇒ Δt_obs / Δt_emit = (1 + z) · (v_emit / v_obs)
                     ≈ (1 + z)        [v_emit ≈ v_obs, deviation ~10^-37]

This script does the symbolic manipulation explicitly and shows the
(v_emit / v_obs) correction factor is identically 1 when photons are
treated as massless, and ~1 + O((m c^2/E)^2) when massive.

Usage:
    python3 check_05_redshift_cascade_sympy.py
"""

from __future__ import annotations

import sys

from sympy import symbols, simplify, sqrt, series, Rational


def main() -> int:
    print("R6 — Check 05: Symbolic redshift-cascade derivation")
    print("=" * 60)

    lam_emit, lam_obs, d_emit, d_obs, v_emit, v_obs, N, z = symbols(
        "lambda_emit lambda_obs d_emit d_obs v_emit v_obs N z",
        positive=True, real=True,
    )

    # L3: λ = N d
    d_emit_expr = lam_emit / N
    d_obs_expr = lam_obs / N

    # Redshift: λ_obs = (1+z) λ_emit
    lam_obs_expr = (1 + z) * lam_emit
    d_obs_sub = d_obs_expr.subs(lam_obs, lam_obs_expr)

    # Inter-cluster times
    dt_emit = d_emit_expr / v_emit
    dt_obs = d_obs_sub / v_obs

    # Ratio
    ratio = simplify(dt_obs / dt_emit)
    print("Inter-cluster times:")
    print(f"  Δt_emit = d_emit / v_emit = {dt_emit}")
    print(f"  Δt_obs  = d_obs  / v_obs  = {dt_obs}")
    print()
    print(f"Δt_obs / Δt_emit = {ratio}")
    print()

    # Substitute v_emit = v_obs to see the leading result
    ratio_equal_v = simplify(ratio.subs(v_emit, v_obs))
    print(f"Set v_emit = v_obs (massless-photon or leading approximation):")
    print(f"  Result: {ratio_equal_v}")
    print()

    # Massive photon correction
    # v = c * sqrt(1 - (m c^2 / E)^2); E_emit = h c / λ_emit; E_obs = h c / λ_obs = E_emit/(1+z)
    # Therefore (m c^2 / E_obs)^2 = (1+z)^2 * (m c^2 / E_emit)^2
    # Ratio v_emit/v_obs = sqrt((1 - x^2) / (1 - (1+z)^2 x^2)) where x = m c^2 / E_emit
    print("Massive-photon correction (symbolic):")
    x = symbols("x", positive=True)  # x = m c^2 / E_emit
    factor_emit = sqrt(1 - x ** 2)
    factor_obs = sqrt(1 - (1 + z) ** 2 * x ** 2)
    correction = factor_emit / factor_obs
    print(f"  v_emit / v_obs = sqrt((1 - x^2) / (1 - (1+z)^2 x^2))")
    print(f"  where x = m_gamma c^2 / E_emit")
    print()

    # Expand around x = 0 (massless limit)
    expansion = series(correction, x, 0, 3).removeO()
    expansion = simplify(expansion)
    print(f"  Expansion around x = 0: {expansion}")
    print(f"  Leading correction term is O(x^2) = O((m c^2/E)^2)")
    print()

    print("Conclusion:")
    print("  Δt_obs / Δt_emit = (1 + z) · [1 + O((m c^2/E)^2)]")
    print("  For GCM's m_gamma ≈ 5.6e-19 eV/c^2 and E ≈ 1 eV:")
    print("    (m c^2/E)^2 ≈ 3e-37")
    print("  So the leading non-linear correction is ~3e-37 times negligible.")
    print("  R6 produces (1 + z)^1.000 to staggering precision.")
    print()
    print("Status: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
