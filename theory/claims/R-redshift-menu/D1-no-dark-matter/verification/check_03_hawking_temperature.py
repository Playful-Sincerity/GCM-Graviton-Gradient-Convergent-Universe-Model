#!/usr/bin/env python3
"""
D1 Check 03 — Hawking temperature of an asteroid-mass primordial black hole.

Claim in plausibility.md:
  'Hawking temperature at these masses is T_H ~ 6e-7 K'
Claim in claim.md:
  'Hawking temperature at these masses is far below the CMB'
  (CMB is 2.725 K)

Formula:
  T_H = hbar c^3 / (8 pi G M k_B)

For M = 10^20 g = 10^17 kg (asteroid-mass PBH).
"""
from decimal import Decimal, getcontext
import json, os, sys, math
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))
def D(key): return Decimal(INPUTS[key]["value"])

hbar = D("hbar")
c = D("c")
G = D("G")
kB = D("kB")
M = D("PBH_mass_claim") * Decimal("1e-3")  # g -> kg

PI = Decimal("3.14159265358979323846264338327950288419716939937510")

T_H = hbar * c**3 / (8 * PI * G * M * kB)

# Cross-check with solar-mass BH Hawking temperature as a calibration
M_sun = D("M_sun")
T_H_sun = hbar * c**3 / (8 * PI * G * M_sun * kB)

# Schwarzschild radius
r_s = 2 * G * M / c**2

# Emitted luminosity (Stefan-Boltzmann black-body approximation)
# sigma_SB = 2 pi^5 k^4 / (15 h^3 c^2), but simpler to use formula L = pi^2 k^4 T^4 / (60 hbar^3 c^2) * A
# Actually just compute L using standard sigma_SB ~ 5.67e-8 W/m^2/K^4.
sigma_SB = Decimal("5.670374419e-8")
A = 4 * PI * r_s**2
L = sigma_SB * T_H**4 * A

print(f"# Check: 03 — Hawking temperature of asteroid-mass PBH")
print(f"# Claim: D1-no-dark-matter")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_03_hawking_temperature.py")
print(f"# ----")
print()
print(f"Inputs:")
print(f"  M = {M} kg (= 10^20 g, asteroid-mass PBH)")
print(f"  hbar, c, G, k_B from CODATA")
print()
print(f"Hawking T = hbar c^3 / (8 pi G M k_B)")
print(f"        = {T_H:.3E} K")
print(f"        = {T_H:.3f} K")
print()
print(f"Solar-mass calibration: T_H(M_sun) = {T_H_sun:.3E} K")
print(f"  (textbook value ~6.17e-8 K -- should agree at this precision)")
print(f"  ratio computed/textbook: {T_H_sun / Decimal('6.17e-8'):.3}")
print()
print(f"Schwarzschild radius: r_s = 2GM/c^2 = {r_s:.3E} m")
print(f"Surface area:          A = 4 pi r_s^2 = {A:.3E} m^2")
print(f"Luminosity (SB): L = sigma_SB T^4 A = {L:.3E} W  (~{L*1000:.1f} mW)")
print()
print(f"Claimed in plausibility.md: T_H ~ 6e-7 K")
print(f"Computed: T_H ~ {T_H:.3E} K")
print(f"Ratio computed/claim: {T_H / Decimal('6e-7'):.3E}")
print()
T_CMB = Decimal("2.725")
print(f"CMB temperature: {T_CMB} K")
print(f"T_H / T_CMB = {T_H / T_CMB:.3E}")
print()
print("FINDING:")
print(f"  The claim 'T_H ~ 6e-7 K far below CMB' IS WRONG BY ~12 ORDERS OF MAGNITUDE.")
print(f"  The actual Hawking temperature at 10^17 kg is ~1.2e6 K, which is HUGE (million K).")
print(f"  The reason asteroid-mass PBHs are observationally hidden is NOT low temperature,")
print(f"  it is tiny emitting surface area (r_s ~ 1.5e-10 m) and therefore tiny luminosity")
print(f"  (~{L*1000:.0f} milliwatts per PBH). The individual radiation is high-energy but")
print(f"  the total power is small and the encounter rate is negligible.")
print()
print("  The OBSERVATIONAL ARGUMENT that asteroid-mass PBHs are hard to detect stands.")
print("  The SPECIFIC TEMPERATURE CLAIM in plausibility.md and claim.md is false.")
print()
print("STATUS: FAIL — plausibility.md and claim.md both have a 12-order-of-magnitude")
print("        error on the Hawking temperature. Need revision to 'T_H ~ 10^6 K,")
print("        but emitted luminosity ~ mW per PBH, undetectable at cosmic distances'.")
