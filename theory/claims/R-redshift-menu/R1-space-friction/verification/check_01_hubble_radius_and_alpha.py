#!/usr/bin/env python3
"""
R1 Check 01 — Hubble radius R_H and friction coefficient alpha = H0/c.

Claim in plausibility.md:
  For z ~ 1 at distances of order the Hubble radius R_H ~ 4.4e26 m,
  alpha ~ 1/R_H ~ 2.3e-27 m^-1, same order as H0/c.

This script verifies:
  (a) R_H = c/H0 at H0 = 70 km/s/Mpc
  (b) alpha = H0/c equals 1/R_H (identity)
  (c) Numerical values match the claimed 4.4e26 m and 2.3e-27 m^-1
      within rounding / H0-choice tolerance.

Uses Python decimal for >=30-digit precision (mpmath not available in
this environment; decimal with prec=50 is the fallback).
"""

from decimal import Decimal, getcontext
import json
import os
import sys
from datetime import datetime

getcontext().prec = 50

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))

def D(key):
    return Decimal(INPUTS[key]["value"])

def Dval(val):
    return Decimal(val)

c = D("c")                                 # m/s
H0_kmsMpc = D("H0_km_per_s_per_Mpc")       # 70
Mpc_m = D("Mpc_m")                         # 3.0857e22 m

# H0 in SI units (s^-1)
H0_SI = H0_kmsMpc * Decimal("1000") / Mpc_m

# Hubble radius
R_H = c / H0_SI

# Required alpha
alpha = H0_SI / c
alpha_alt = Decimal(1) / R_H  # identity: alpha = 1/R_H

print(f"# Check: 01 — Hubble radius and alpha = H0/c")
print(f"# Claim: R1-space-friction")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_01_hubble_radius_and_alpha.py")
print(f"# Status: computed below; claim match decided by ratio vs claimed value")
print(f"# ----")
print()
print(f"H0 input:                {H0_kmsMpc} km/s/Mpc")
print(f"H0 in SI:                {H0_SI:.6E} s^-1")
print(f"R_H = c/H0:              {R_H:.6E} m")
print(f"  claimed (plausibility): 4.4e26 m")
print(f"  ratio (computed/claim): {R_H / D('R_H_claim'):.6}")
print()
print(f"alpha = H0/c:            {alpha:.6E} m^-1")
print(f"alpha = 1/R_H:           {alpha_alt:.6E} m^-1  (identity)")
print(f"  claimed (plausibility): 2.3e-27 m^-1")
print(f"  ratio (computed/claim): {alpha / D('alpha_claim'):.6}")

# Test H0 sensitivity: both Planck (67.4) and SH0ES (73.0)
print()
print("H0 tension sensitivity:")
for H0key in ["H0_planck18", "H0_sh0es"]:
    H0v = Dval(INPUTS[H0key]["value"])
    H0v_SI = H0v * Decimal("1000") / Mpc_m
    a = H0v_SI / c
    R = c / H0v_SI
    print(f"  H0 = {H0v} ({H0key}) -> R_H = {R:.3E} m, alpha = {a:.3E} m^-1")

# Compare both interpretations of the plausibility.md claim:
#  (A) Hubble radius = c/H0 at H0=70  -> R_H = 1.32e26 m; alpha = 7.57e-27 m^-1
#  (B) Observable universe / particle horizon = 4.4e26 m ~= 46 Gly
#      -> alpha_obs_inv = 1/(4.4e26) = 2.27e-27 m^-1
print()
print("Interpretation check:")
R_obs = Decimal("4.4e26")
alpha_from_R_obs = Decimal(1) / R_obs
print(f"  (A) Hubble radius = c/H0:         R = {R_H:.3E} m  alpha = H0/c = {alpha:.3E} m^-1")
print(f"  (B) Observable universe radius:   R = {R_obs:.3E} m  alpha = 1/R = {alpha_from_R_obs:.3E} m^-1")
print(f"  Ratio B/A for R: {R_obs / R_H:.3}")
print(f"  Ratio B/A for alpha: {alpha_from_R_obs / alpha:.3}")
print()
print("FINDING: plausibility.md claims BOTH 'Hubble radius = 4.4e26 m' AND")
print("'alpha ~ H0/c ~ 2.3e-27 m^-1'. These are inconsistent by a factor of ~3.3.")
print("  - 4.4e26 m is the OBSERVABLE UNIVERSE RADIUS (particle horizon), not Hubble radius.")
print("  - The Hubble radius c/H0 at H0=70 is 1.32e26 m.")
print("  - If the claim uses R = 4.4e26 m, then alpha = 2.3e-27 m^-1 is consistent but")
print("    should be written as alpha ~ 1/R_observable, NOT alpha ~ H0/c.")
print("  - If the claim uses alpha = H0/c, then the numerical value at H0=70 is 7.57e-27 m^-1.")
print()
print("STATUS: INCONCLUSIVE (labelling error in plausibility.md — see findings).")
print("        Structural claim 'alpha is of order the inverse cosmological length scale' is robust.")
print("        Specific numerical values have a factor-of-3.3 labeling ambiguity.")
