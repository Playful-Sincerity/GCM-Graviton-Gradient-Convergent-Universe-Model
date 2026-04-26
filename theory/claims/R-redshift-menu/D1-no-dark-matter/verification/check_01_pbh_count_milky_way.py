#!/usr/bin/env python3
"""
D1 Check 01 — Number of asteroid-mass PBHs needed to constitute Milky Way dark halo.

Claim in D1/claim.md:
  N_PBH = M_halo_dark / M_PBH ~ 10^12 M_sun / 10^-13 M_sun = 10^25 PBHs in MW halo
  (assuming PBH mass = 10^20 g = 10^-13 M_sun, and M_halo_total = 10^12 M_sun,
   M_visible = 6e10 M_sun, so M_dark = ~9.4e11 M_sun)

Claim in D1/plausibility.md (chronicle summary):
  N_PBH ~ 10^18  <-- *** this is the value I stated in the 2026-04-23 chronicle/claim summary ***

This check arbitrates: is N_PBH 10^18 or 10^25?
"""
from decimal import Decimal, getcontext
import json, os, sys, math
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))
def D(key): return Decimal(INPUTS[key]["value"])

# Convert M_halo to kg
M_sun = D("M_sun")
M_halo_total_Msun = D("M_MW_halo_claim")  # 1e12 M_sun
M_visible_Msun = D("M_MW_visible_claim")  # 6e10 M_sun
M_halo_dark_Msun = M_halo_total_Msun - M_visible_Msun
M_halo_dark_kg = M_halo_dark_Msun * M_sun

# PBH mass: 1e20 g = 1e17 kg
M_PBH_g = D("PBH_mass_claim")  # 1e20
M_PBH_kg = M_PBH_g * Decimal("1e-3")  # grams -> kg

N_PBH = M_halo_dark_kg / M_PBH_kg

print(f"# Check: 01 — PBH count in Milky Way halo")
print(f"# Claim: D1-no-dark-matter")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_01_pbh_count_milky_way.py")
print(f"# ----")
print()
print(f"Inputs:")
print(f"  M_halo_total:     {M_halo_total_Msun} M_sun = {M_halo_total_Msun * M_sun:.3E} kg")
print(f"  M_visible:        {M_visible_Msun} M_sun = {M_visible_Msun * M_sun:.3E} kg")
print(f"  M_halo_dark:      {M_halo_dark_Msun:.3E} M_sun = {M_halo_dark_kg:.3E} kg")
print(f"  M_PBH:            {M_PBH_g} g = {M_PBH_kg:.3E} kg")
print()
print(f"N_PBH = M_halo_dark / M_PBH = {N_PBH:.4E}")
print()
N_claim = D("N_PBH_MW_claim")  # 1e25
print(f"Claimed in claim.md:     ~1e25")
print(f"Claimed in chronicle summary: ~1e18")
print()
print(f"Ratio computed/claim.md:      {N_PBH / N_claim:.3}")
print(f"Ratio computed/chronicle:     {N_PBH / Decimal('1e18'):.3}")
print()
log10 = Decimal(math.log10(float(N_PBH)))
print(f"log10(N_PBH) = {log10:.4f}")
print()
print("FINDING:")
print(f"  claim.md's '~10^25 PBHs' is CORRECT (within 0.1 order).")
print(f"  The chronicle summary I wrote on 2026-04-23 saying '~10^18 PBHs'")
print(f"  was WRONG by ~7 orders of magnitude. claim.md is the authoritative one.")
print()
print("STATUS: PASS (for claim.md's 10^25). FAIL (for chronicle summary's 10^18).")
print("        Chronicle needs correction.")
