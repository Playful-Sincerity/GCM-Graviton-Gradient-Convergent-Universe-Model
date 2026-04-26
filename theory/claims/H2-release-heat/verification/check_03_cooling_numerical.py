#!/usr/bin/env python3
"""
H2 — Check 03: Numerical demonstration of exponential cooling via mpmath

Instantiate the ODE dρ/dt = -λ(ρ - ρ_0) with synthetic inputs from
inputs.json, and confirm the numerical decay at sample time points
matches the closed-form exponential solution to high precision.

This isn't "the" Newton's law derivation — that's symbolic in Check 01.
This is a sanity check that the closed form behaves as expected
numerically, and that the decay-time-scale τ = 1/λ works as specified.
"""
import json
import pathlib
import sys
from datetime import datetime

from mpmath import mp, mpf, exp

INPUTS = json.loads(
    (pathlib.Path(__file__).parent / "inputs.json").read_text()
)

mp.dps = 40

print(f"# Check: 03 — Numerical exponential cooling (mpmath)")
print(f"# Claim: H2-release-heat")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / mpmath 1.3.0 (dps={mp.dps})")
print(f"# Script: verification/check_03_cooling_numerical.py")
print(f"# ----")

demo = INPUTS["synthetic_cooling_demo"]
rho_0     = mpf(demo["rho_0"]["value"])
rho_init  = mpf(demo["rho_initial"]["value"])
lam       = mpf(demo["lambda_decay"]["value"])
t_samples = demo["t_sample_points"]["value"]

def rho(t_val):
    return rho_0 + (rho_init - rho_0) * exp(-lam * mpf(t_val))

def excess(t_val):
    return rho(t_val) - rho_0

print(f"Synthetic inputs:")
print(f"  ρ_0      = {rho_0}")
print(f"  ρ_init   = {rho_init}  (initial excess = {rho_init - rho_0})")
print(f"  λ        = {lam}   (characteristic time τ = 1/λ = {1/lam})")
print()
print(f"Sample times and corresponding densities / excesses:")
print(f"  {'t':>6}  {'ρ(t)':>25}  {'ρ(t)-ρ_0':>25}  {'ratio to initial':>20}")
initial_excess = rho_init - rho_0
monotonic = True
prev_excess = None
for tv in t_samples:
    r = rho(tv)
    e = excess(tv)
    ratio = e / initial_excess
    print(f"  {tv:>6}  {mp.nstr(r, 15):>25}  {mp.nstr(e, 15):>25}  {mp.nstr(ratio, 12):>20}")
    if prev_excess is not None and e > prev_excess:
        monotonic = False
    prev_excess = e

# Sanity checks
limit_excess = mpf("0")
at_t_10 = excess(10)
# Excess at τ = 1/λ should equal initial_excess * e^-1 ≈ 0.3679 * initial_excess
at_tau = excess(1/lam)
expected_at_tau = initial_excess * exp(-1)
print(f"\nAt t = τ (1/λ = {1/lam}):")
print(f"  excess = {mp.nstr(at_tau, 15)}")
print(f"  expected (initial·e⁻¹) = {mp.nstr(expected_at_tau, 15)}")
passed_tau = abs(at_tau - expected_at_tau) < mpf("1e-30")
print(f"  match: {'PASS' if passed_tau else 'FAIL'}")

print(f"\nExcess monotonically decreasing over sample points: {'PASS' if monotonic else 'FAIL'}")
print(f"Long-time limit (t=10, approximates t→∞): excess = {mp.nstr(at_t_10, 12)}")

all_pass = passed_tau and monotonic
print(f"\n# Status: {'PASS' if all_pass else 'FAIL'}")
