#!/usr/bin/env python3
"""
R6 Check 01 — Convert GCM claim m_gamma = 1e-54 kg to eV/c^2, compare to
Wang et al. 2023 FRB bound m_gamma <= 2.1e-15 eV/c^2.

Claim (plausibility.md, R6-photon-structure/plausibility.md inherits from
R5-adjacent comparison): GCM value is ~4 orders below the Wang bound.
This script verifies the conversion and the order-of-magnitude claim.
"""
from decimal import Decimal, getcontext
import json, os, sys, math
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))
def D(key): return Decimal(INPUTS[key]["value"])

c = D("c")
eV = D("eV_in_J")
m_kg = D("m_photon_GCM_kg_claim")

# Rest energy in Joules, then convert to eV.
# m c^2 (Joules) / eV_in_J = energy in eV; dividing by c^2 gives mass in eV/c^2 (numerically same magnitude since c^2 cancels in "mass expressed as rest energy").
rest_energy_J = m_kg * c * c
rest_energy_eV = rest_energy_J / eV  # mass in eV/c^2 numerical value

# Wang bound
wang_eV = D("FRB_bound_Wang2023_eV")

# Ratio bound / GCM
ratio = wang_eV / rest_energy_eV
log10_ratio = Decimal(math.log10(float(ratio)))

print(f"# Check: 01 — photon mass conversion and comparison to FRB bound")
print(f"# Claim: R6-photon-structure")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_01_photon_mass_kg_to_eV.py")
print(f"# ----")
print()
print(f"GCM claim:  m_gamma = {m_kg} kg")
print(f"  c^2 = {c*c} m^2/s^2")
print(f"  rest energy m c^2 = {rest_energy_J:.6E} J")
print(f"  in eV: {rest_energy_eV:.6E} eV")
print(f"  (i.e., m = {rest_energy_eV:.4E} eV/c^2)")
print()
print(f"Claimed in plausibility.md: 5.6e-19 eV/c^2")
claim_eV = D("m_photon_GCM_eV_claim")
print(f"  ratio computed/claim:      {rest_energy_eV / claim_eV:.4}")
print()
print(f"Wang et al. 2023 bound:     {wang_eV:.3E} eV/c^2")
print(f"  ratio Wang/GCM:            {ratio:.4E}")
print(f"  log10(Wang/GCM):           {log10_ratio:.4f}")
print()
print(f"Claim in R6 brief: GCM is ~4 orders below Wang bound.")
print(f"Computed: {log10_ratio:.2f} orders below.")
print()
if abs(log10_ratio - Decimal("4")) < Decimal("0.5"):
    print("Within ~0.5 order of the '4 orders' claim. PASS (order-of-magnitude).")
    status = "PASS"
else:
    print(f"{float(log10_ratio):.2f} orders is more than 0.5 away from 4. Claim is approximate.")
    status = "PARTIAL"

print()
print(f"STATUS: {status}")
print()
print("Note on adjacent-programs file precision:")
print("  2026-04-23-adjacent-programs.md states '28 orders below' for graviton mass")
print("  vs LIGO bound, NOT for the photon mass. R6's '4 orders' is the correct claim")
print("  for the photon mass vs FRB bound. The Plan's M1 section (graviton mass)")
print("  cites 28 orders correctly. These two orders-below claims are for different")
print("  particles and should not be conflated.")
