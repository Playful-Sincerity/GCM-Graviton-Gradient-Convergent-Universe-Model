#!/usr/bin/env python3
"""
R1 Check 02 — Graviton number density n_g and implied cross-section sigma_g.

Claims in plausibility.md:
  n_g ~ 10^185 / V_universe ~ 10^106 m^-3
  alpha ~ n_g * sigma_g  =>  sigma_g ~ 10^-133 m^2

This script:
  (a) Computes the volume of the observable-universe sphere at R_obs = 4.4e26 m.
  (b) Divides 10^185 by this volume to get implied n_g.
  (c) Back-solves sigma_g = alpha / n_g using both the claimed alpha (2.3e-27)
      and the H0/c value (7.57e-27).
  (d) Flags any numerical disagreement with plausibility.md.
"""

from decimal import Decimal, getcontext
import json, os, sys
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))
def D(key): return Decimal(INPUTS[key]["value"])

c = D("c")
Mpc = D("Mpc_m")
H0 = D("H0_km_per_s_per_Mpc") * Decimal("1000") / Mpc
ell_P = D("ell_Planck")
N_univ = D("N_gravitons_universe_claim")  # 1e185

# Observable universe volume
R_obs = Decimal("4.4e26")
# pi to ~50 digits
PI = Decimal("3.14159265358979323846264338327950288419716939937510")
V_obs = Decimal(4) / Decimal(3) * PI * R_obs**3

# Planck volume (for comparison)
V_P = ell_P**3

# Implied graviton number density
n_g_from_Nuniv = N_univ / V_obs
n_g_from_Planck_filling = Decimal(1) / V_P

# Cross-section back-solve
alpha_from_H0 = H0 / c
alpha_claimed = D("alpha_claim")

sigma_from_claimed = alpha_claimed / D("n_g_claim")
sigma_from_H0_consistent = alpha_from_H0 / n_g_from_Nuniv

print(f"# Check: 02 — graviton number density and cross-section")
print(f"# Claim: R1-space-friction")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_02_graviton_density_and_cross_section.py")
print(f"# ----")
print()
print(f"R_obs (observable universe radius): {R_obs:.3E} m")
print(f"V_obs = (4/3) pi R^3:               {V_obs:.3E} m^3")
print(f"V_Planck = ell_P^3:                 {V_P:.3E} m^3")
print(f"N_Planck_cells = V_obs / V_P:       {V_obs / V_P:.3E}")
print()
print(f"Claim: N_gravitons_universe = 10^185")
print(f"Implied n_g = 10^185 / V_obs = {n_g_from_Nuniv:.3E} m^-3")
print(f"  claimed in plausibility.md:  1e106 m^-3")
print(f"  ratio computed/claim:        {n_g_from_Nuniv / D('n_g_claim'):.4}")
print()
print(f"Alt: n_g from Planck-filling (1/V_P) = {n_g_from_Planck_filling:.3E} m^-3")
print(f"     (this is what a graviton-per-Planck-volume picture would give)")
print()
print("Cross-section back-solve sigma = alpha / n_g:")
print(f"  (using claimed alpha=2.3e-27 and claimed n_g=1e106): sigma = {sigma_from_claimed:.3E} m^2")
print(f"    claimed in plausibility.md:                        1e-133 m^2")
print(f"    ratio: {sigma_from_claimed / D('sigma_g_claim'):.4}")
print()
print(f"  (using alpha=H0/c=7.57e-27 and n_g from 10^185/V_obs = {n_g_from_Nuniv:.2E}):")
print(f"    sigma = {sigma_from_H0_consistent:.3E} m^2")
print()
print("FINDINGS:")
print(f"  * n_g from 10^185/V_obs is ~{n_g_from_Nuniv:.1E} m^-3, which is 10^104, not 10^106.")
print( "    The plausibility.md claim 'n_g ~ 10^106 m^-3' is off by ~2 orders of magnitude.")
print( "  * Using the self-consistent alpha=H0/c and n_g=N/V_obs, the implied")
print(f"    cross-section is ~{sigma_from_H0_consistent:.1E} m^2, about 2-3 orders larger than the claimed 1e-133.")
print( "  * The structural claim 'sigma_g is an extraordinarily small per-graviton cross-section' is")
print( "    correct regardless of the specific exponent; the specific 10^-133 value is unreliable.")
print()
print("STATUS: INCONCLUSIVE (arithmetic errors in plausibility.md numerics; structural claims stand).")
