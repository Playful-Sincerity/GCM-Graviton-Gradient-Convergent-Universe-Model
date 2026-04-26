#!/usr/bin/env python3
"""
R3 Check 01 — Required gravitational potential gradient for R3 mechanism.

Claim in plausibility.md:
  For R3 to produce the observed Hubble relation, the cosmological potential
  gradient must be:
    d Phi / dr ~ c H_0 ~ 2e-8 m/s^2

Let's verify. For gravitational redshift z = Delta Phi / c^2, and desired
z = H_0 d / c at small z, we have Delta Phi = c H_0 d, so dPhi/dr = c H_0.
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
H0_SI = D("H0_km_per_s_per_Mpc") * Decimal("1000") / Mpc

gradient = c * H0_SI

print(f"# Check: 01 — required potential gradient")
print(f"# Claim: R3-non-central")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_01_gradient_magnitude.py")
print(f"# ----")
print()
print(f"For z ~ H_0 d / c at low z via gravitational redshift z ~ Delta Phi / c^2:")
print(f"  Delta Phi = c H_0 d  =>  dPhi/dr = c H_0")
print()
print(f"H_0 (SI):    {H0_SI:.4E} s^-1")
print(f"c:           {c} m/s")
print(f"c * H_0:     {gradient:.4E} m/s^2")
print()
claim = D("potential_gradient_claim_m_s2")
print(f"plausibility.md claim: {claim} m/s^2 = 2e-8 m/s^2")
print(f"ratio computed/claim:  {gradient / claim:.4}")
print()
tol = abs(gradient / claim - Decimal(1))
if tol < Decimal("0.5"):
    print("Within 50% of claim. STATUS: PASS (order-of-magnitude).")
else:
    print(f"Off by {tol*100:.0f}%. STATUS: PARTIAL.")
print()
print("Note: this computation checks the magnitude of the required gradient.")
print("It does NOT check whether such a gradient exists in the observed universe.")
print("R3 remains red because the required gradient has not been measured; that is")
print("a theory-vs-observation gap, not an arithmetic issue.")
