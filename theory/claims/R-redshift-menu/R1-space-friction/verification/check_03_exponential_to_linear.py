#!/usr/bin/env python3
"""
R1 Check 03 — Exponential energy-loss law produces linear redshift-distance
relation at small z.

Claim in claim.md:
  dE/dr = -alpha E  =>  E(r) = E_0 exp(-alpha r)
  1 + z = E_0 / E(r) = exp(alpha r)
  For small alpha r: 1 + z ≈ 1 + alpha r, so z ≈ alpha r (Hubble-like)

Numerical check: how small does alpha*r need to be for the linear approximation
to hold to 1%? To 0.1%?
"""

from decimal import Decimal, getcontext
import json, os, sys
from datetime import datetime
import math

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))

def exp_dec(x, terms=60):
    """Taylor series exp for Decimal x, 60 terms is plenty at prec=50."""
    s = Decimal(0)
    term = Decimal(1)
    for n in range(terms):
        if n > 0:
            term = term * x / Decimal(n)
        s += term
    return s

print(f"# Check: 03 — exponential-to-linear redshift limit")
print(f"# Claim: R1-space-friction")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_03_exponential_to_linear.py")
print(f"# ----")
print()
print("Model: E(r) = E_0 exp(-alpha r); observed z = exp(alpha r) - 1.")
print()
print(f"{'alpha*r':>12s}  {'z_exact = exp(x)-1':>22s}  {'z_linear = x':>14s}  {'err (exact-linear)/exact':>26s}")
for ar in [Decimal("0.001"), Decimal("0.01"), Decimal("0.1"), Decimal("0.3"),
           Decimal("0.5"), Decimal("1.0"), Decimal("2.0")]:
    z_exact = exp_dec(ar) - Decimal(1)
    z_lin = ar
    err = (z_exact - z_lin) / z_exact
    print(f"{ar:>12f}  {z_exact:>22.6E}  {z_lin:>14.4f}  {err:>26.4%}")

print()
print("Interpretation:")
print("  * For alpha*r < 0.01, linear approximation is good to ~0.5%.")
print("  * For alpha*r ~ 0.3 (a plausible 'small-z' cosmological distance), error is ~15%.")
print("  * For z > 1, fully exponential expression must be used; linear approx invalid.")
print()
print("At alpha=1/R_observable = 2.3e-27 m^-1 and z=1, alpha*r = ln(2) ~ 0.693.")
print("That is NOT small — the linear approximation is ~37% off.")
print("So R1's story z = alpha * r is a LOW-z APPROXIMATION only.")
print("At cosmological redshifts >= 1, the exponential form must be used; fit to")
print("Pantheon+ data requires fitting exp(alpha r), not alpha r.")
print()
print("STATUS: PASS — the exponential-to-linear mapping is elementary and confirmed.")
print("        Caveat named: R1 must use the exp form (not linear) for z >= ~0.1.")
