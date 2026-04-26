#!/usr/bin/env python3
"""
S5.5(a) — Check 02: Earth-Moon Newtonian force, independent numerical computation

Uses mpmath at 50-digit precision to compute F = G M_E M_M / r^2
and compare to the standard textbook reference value (~1.98e20 N).

Independence from the hand calculation in a-newtonian-limit.md:
  - Constants read from inputs.json (no hardcoding)
  - mpmath arbitrary precision (guards against double-precision clip)
  - Error shown as absolute and relative to reference
"""
import json
import pathlib
import sys
from datetime import datetime

from mpmath import mp, mpf

INPUTS = json.loads(
    (pathlib.Path(__file__).parent / "inputs.json").read_text()
)

mp.dps = 50  # 50 significant digits

print(f"# Check: 02 — Earth-Moon Newtonian force numerical")
print(f"# Claim: S5_5-classical-limits (sub-claim a — Newtonian limit)")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / mpmath (dps={mp.dps})")
print(f"# Script: verification/check_02_earth_moon_numerical.py")
print(f"# ----")

G   = mpf(INPUTS["G_newton"]["value"])
M_E = mpf(INPUTS["M_earth"]["value"])
M_M = mpf(INPUTS["M_moon"]["value"])
r   = mpf(INPUTS["r_earth_moon"]["value"])
F_ref = mpf(INPUTS["earth_moon_force_reference"]["value"])

F = G * M_E * M_M / r**2

print(f"Inputs (from inputs.json):")
print(f"  G   = {G} m^3/(kg*s^2)")
print(f"  M_E = {M_E} kg")
print(f"  M_M = {M_M} kg")
print(f"  r   = {r} m")
print(f"  reference F = {F_ref} N")
print()
print(f"Computed F = G M_E M_M / r^2 = {F} N")
print(f"Computed F (scientific) = {mp.nstr(F, 6)} N")
print()
abs_err = abs(F - F_ref)
rel_err = abs_err / F_ref
print(f"Absolute error vs reference: {mp.nstr(abs_err, 4)} N")
print(f"Relative error vs reference: {mp.nstr(rel_err * 100, 4)} %")

# Pass if within 1% of textbook reference
# (reference value 1.98e20 is itself rounded to 3 sig figs, so 1% tolerance is
# appropriate — any disagreement beyond that would indicate a real issue)
tolerance = mpf("0.01")
passed = rel_err < tolerance
print(f"\nTolerance: {tolerance*100}%")
print(f"\n# Status: {'PASS' if passed else 'FAIL'}")
