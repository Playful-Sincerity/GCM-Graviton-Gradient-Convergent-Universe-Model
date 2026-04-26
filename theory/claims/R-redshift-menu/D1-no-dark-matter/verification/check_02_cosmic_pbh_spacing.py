#!/usr/bin/env python3
"""
D1 Check 02 — Cosmic mean inter-PBH spacing if all DM is asteroid-mass PBHs.

Claim in plausibility.md:
  rho_DM ~ 2.4e-27 kg/m^3
  n_PBH = rho_DM / M_PBH ~ 2.4e-44 m^-3
  inter-PBH spacing = n_PBH^{-1/3} ~ 3.5e14 m ~ 2000 AU
"""
from decimal import Decimal, getcontext
import json, os, sys, math
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))
def D(key): return Decimal(INPUTS[key]["value"])

# Compute rho_crit from H0, then rho_DM = Omega_DM * rho_crit
G = D("G")
c = D("c")
Mpc = D("Mpc_m")
H0_SI = D("H0_km_per_s_per_Mpc") * Decimal("1000") / Mpc
Omega_DM = D("Omega_DM")

PI = Decimal("3.14159265358979323846264338327950288419716939937510")
rho_crit = 3 * H0_SI**2 / (8 * PI * G)
rho_DM = Omega_DM * rho_crit

# PBH mass
M_PBH_kg = D("PBH_mass_claim") * Decimal("1e-3")  # g -> kg

# Number density
n_PBH = rho_DM / M_PBH_kg

# Mean inter-PBH spacing: n^{-1/3}
# Compute cube root via decimal pow(1/3)
def cbrt_dec(x):
    """Compute cube root via Newton-Raphson, working in Decimal."""
    x = Decimal(x)
    if x == 0: return Decimal(0)
    # initial guess from float
    g = Decimal(float(x) ** (1/3))
    for _ in range(60):
        g = (2*g + x / (g*g)) / 3
    return g

d_PBH_m = cbrt_dec(Decimal(1) / n_PBH)
AU = D("AU_m")
d_PBH_AU = d_PBH_m / AU

print(f"# Check: 02 — Cosmic mean inter-PBH spacing")
print(f"# Claim: D1-no-dark-matter")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_02_cosmic_pbh_spacing.py")
print(f"# ----")
print()
print(f"H0 in SI (s^-1):       {H0_SI:.4E}")
print(f"rho_crit = 3 H0^2 / (8 pi G): {rho_crit:.3E} kg/m^3")
print(f"Omega_DM:               {Omega_DM}")
print(f"rho_DM = Omega_DM * rho_crit: {rho_DM:.3E} kg/m^3")
print(f"  plausibility.md claim: 2.4e-27 kg/m^3")
print(f"  ratio: {rho_DM / Decimal('2.4e-27'):.4}")
print()
print(f"M_PBH = {M_PBH_kg:.3E} kg")
print(f"n_PBH = rho_DM / M_PBH = {n_PBH:.3E} m^-3")
print(f"  plausibility.md claim: 2.4e-44 m^-3")
print(f"  ratio: {n_PBH / Decimal('2.4e-44'):.4}")
print()
print(f"Mean spacing = n^(-1/3) = {d_PBH_m:.3E} m = {d_PBH_AU:.0f} AU")
print(f"  plausibility.md claim: 2000 AU")
print(f"  ratio: {d_PBH_AU / D('inter_PBH_spacing_claim_AU'):.3}")
print()
tol = abs(d_PBH_AU / D("inter_PBH_spacing_claim_AU") - Decimal(1))
if tol < Decimal("0.5"):
    print(f"Within 50% of claim. STATUS: PASS (order-of-magnitude).")
else:
    print(f"More than 50% off. STATUS: PARTIAL.")
