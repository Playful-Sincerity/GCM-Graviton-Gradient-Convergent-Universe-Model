#!/usr/bin/env python3
"""
R6 Check 02 (Python companion) — R6 structural prediction consistency with DES 2024
SNe Ia time-dilation measurement.

The symbolic derivation of the cascade exponent is in check_02_cascade_exponent.wls
(Wolfram). This Python script does the numerical sigma comparison independently.
"""

from decimal import Decimal, getcontext
import json, os, sys, math
from datetime import datetime

getcontext().prec = 50
HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS = json.load(open(os.path.join(HERE, "inputs.json")))

b_obs = Decimal(INPUTS["DES_time_dilation_exponent_claim"]["value"])
sigma_stat = Decimal(INPUTS["DES_time_dilation_stat_err"]["value"])
sigma_sys = Decimal("0.010")  # DES 2024 systematic, not in inputs.json but from the paper
b_R6 = Decimal(INPUTS["R6_prediction_exponent"]["value"])

def sqrt_dec(x):
    """Newton's method square root in Decimal."""
    x = Decimal(x)
    if x < 0:
        raise ValueError
    if x == 0:
        return Decimal(0)
    guess = x / 2
    for _ in range(50):
        guess = (guess + x / guess) / 2
    return guess

sigma_tot = sqrt_dec(sigma_stat**2 + sigma_sys**2)
diff = abs(b_obs - b_R6)
n_sigma_stat = diff / sigma_stat
n_sigma_sys = diff / sigma_sys
n_sigma_tot = diff / sigma_tot

print(f"# Check: 02 (Python companion) — DES consistency")
print(f"# Claim: R6-photon-structure")
print(f"# Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"# Tool: Python {sys.version.split()[0]} / stdlib decimal prec=50")
print(f"# Script: verification/check_02_DES_consistency.py")
print(f"# ----")
print()
print(f"DES 2024 measurement:     b = {b_obs} ± {sigma_stat} (stat) ± {sigma_sys} (sys)")
print(f"R6 structural prediction: b = {b_R6} (exact, from cascade)")
print()
print(f"|b_obs - b_R6|:           {diff}")
print(f"... / sigma_stat:         {n_sigma_stat:.4f}  sigma")
print(f"... / sigma_sys:          {n_sigma_sys:.4f}  sigma")
print(f"sigma_tot (quadrature):   {sigma_tot:.6f}")
print(f"... / sigma_tot:          {n_sigma_tot:.4f}  sigma")
print()
if n_sigma_tot < Decimal("2"):
    print("Prediction within 2 sigma of measurement. PASS.")
    print("STATUS: PASS")
else:
    print("Prediction > 2 sigma from measurement.")
    print("STATUS: FAIL")
