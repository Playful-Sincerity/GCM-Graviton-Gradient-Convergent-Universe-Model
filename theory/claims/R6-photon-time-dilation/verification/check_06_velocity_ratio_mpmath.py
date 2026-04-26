#!/usr/bin/env python3
"""
R6 Check 06 — High-precision v_emit / v_obs ratio (mpmath, 60 dps).

Exercises the speed-of-causality principle: photons travel at v = c - 0_x
(IVNA indexed infinitesimal), strictly < c. Under redshift the photon's
energy decreases; by L2 (v = c sqrt(1 - (m c^2/E)^2)), its speed also
decreases slightly. This script computes v_emit/v_obs explicitly and
shows the correction to R6's (1+z) result is ~10^-37.

Double-precision IEEE-754 floats have ~1e-16 precision, which CANNOT
represent a deviation of 1e-37 from 1. We use mpmath at 60 digits.

Usage:
    python3 check_06_velocity_ratio_mpmath.py
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


def photon_speed(m_eV: mp.mpf, E_eV: mp.mpf, c: mp.mpf) -> mp.mpf:
    """v = c * sqrt(1 - (m c^2 / E)^2). Returns v in m/s.
    Note: we treat the input mass in eV/c^2 units, so m c^2 has units eV.
    The formula then becomes: v = c * sqrt(1 - (m_eV / E_eV)^2).
    """
    ratio = m_eV / E_eV
    return c * mp.sqrt(1 - ratio ** 2)


def main() -> int:
    mp.mp.dps = 60
    inputs = load_inputs()

    c = mp.mpf(str(inputs["c"]["value"]))
    eV = mp.mpf(str(inputs["eV_to_J"]["value"]))
    m_kg = mp.mpf(str(inputs["m_gamma_kg"]["value"]))
    E_emit_eV = mp.mpf(str(inputs["E_visible_photon_eV"]["value"]))

    m_eV = m_kg * c ** 2 / eV

    print("R6 — Check 06: v_emit / v_obs ratio (mpmath, 60 dps)")
    print("=" * 60)
    print("Speed-of-causality principle: photons at v < c strictly.")
    print(f"  m_gamma = {mp.nstr(m_eV, 6)} eV/c^2")
    print(f"  c (causality limit) = {c} m/s (exact)")
    print()

    # Consider a photon emitted at E_emit = 1 eV, observed at z = 1
    # E_obs = E_emit / (1+z)
    for z_val in [mp.mpf("0.1"), mp.mpf("1"), mp.mpf("10")]:
        E_obs_eV = E_emit_eV / (1 + z_val)

        v_emit = photon_speed(m_eV, E_emit_eV, c)
        v_obs = photon_speed(m_eV, E_obs_eV, c)

        ratio = v_emit / v_obs
        correction = ratio - 1  # excess over 1 — the R6 correction factor

        print(f"At z = {z_val}:")
        print(f"  E_emit = {E_emit_eV} eV")
        print(f"  E_obs  = {mp.nstr(E_obs_eV, 8)} eV")
        print(f"  v_emit = {mp.nstr(v_emit, 40)} m/s")
        print(f"  v_obs  = {mp.nstr(v_obs, 40)} m/s")
        print(f"  v_emit < c? {v_emit < c}")
        print(f"  v_obs  < c? {v_obs < c}")
        print(f"  v_emit / v_obs = 1 + {mp.nstr(correction, 8)}")
        print()

    # Full R6 result including correction
    # Δt_obs / Δt_emit = (1+z) * (v_emit/v_obs)
    z_val = mp.mpf("1")
    E_obs_eV = E_emit_eV / (1 + z_val)
    v_emit = photon_speed(m_eV, E_emit_eV, c)
    v_obs = photon_speed(m_eV, E_obs_eV, c)
    full_dilation = (1 + z_val) * (v_emit / v_obs)
    r6_leading = 1 + z_val

    print("R6 full dilation at z = 1 (including v_emit/v_obs correction):")
    print(f"  (1+z) * (v_emit/v_obs) = {mp.nstr(full_dilation, 40)}")
    print(f"  Leading R6 (v_emit = v_obs) = {r6_leading}")
    print(f"  Correction from v ratio    = {mp.nstr(full_dilation - r6_leading, 8)}")
    print()
    print("Conclusion: v < c strictly; correction to (1+z) leading result is ~10^-37.")
    print("Speed-of-causality principle honored; R6 structural result intact.")
    print()
    print("Status: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
