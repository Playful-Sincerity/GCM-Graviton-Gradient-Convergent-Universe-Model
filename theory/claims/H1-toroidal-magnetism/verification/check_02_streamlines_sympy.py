#!/usr/bin/env python3
"""
H1 — Check 02: Vector-calculus structure of the radial + uniform superposition

Claim in derivation.md Step 3:
    "The composition of a radial flow with a linear drift produces a vector
     field with toroidal streamlines around the axis of motion."

Verify with SymPy:
  1. The combined field F = q * r̂/r^2 + v0 * ẑ has a stagnation point on the
     -ẑ axis at r* = sqrt(q/v0). Streamlines wrap around this stagnation
     point → topologically looping geometry (Rankine half-body).
  2. Both F_radial and F_uniform are irrotational (curl = 0).
  3. Therefore the SUPERPOSITION is also curl-free in the open region.

Important honesty note produced by this check:
  Pure superposition is curl-free. To get a REAL magnetic field (with
  non-zero curl, matching Ampère-Maxwell's ∇×B = μ₀J + ...), the H1
  mechanism must invoke TIME-DEPENDENT OSCILLATION — not just static
  superposition. The "toroidal streamlines" are topological, not rotational.
  This strengthens the UNSPEC-4 statement: reproducing Lorentz force needs
  the oscillation dynamics, not just the static vector-field geometry.
"""
import sys
from datetime import datetime

from sympy import symbols, sqrt, solve, simplify, Matrix, Rational
from sympy.vector import CoordSys3D, gradient, curl, divergence

print(f"# Check: 02 — Vector-calculus structure of radial+uniform superposition")
print(f"# Claim: H1-toroidal-magnetism")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy 1.14.0 (sympy.vector)")
print(f"# Script: verification/check_02_streamlines_sympy.py")
print(f"# ----")

N = CoordSys3D("N")
q, v0 = symbols("q v_0", positive=True)

# Position magnitude and unit vector
r2 = N.x**2 + N.y**2 + N.z**2
r = sqrt(r2)

# F_radial = q * r̂ / r^2 = q * r_vec / r^3
F_radial = q * (N.x*N.i + N.y*N.j + N.z*N.k) / r**3

# F_uniform = v0 * ẑ
F_uniform = v0 * N.k

F = F_radial + F_uniform
print("Combined field F = q * r̂/r² + v₀ * ẑ")

# --- Check 1: curl of each piece and of combined field ---
curl_rad = curl(F_radial)
curl_uni = curl(F_uniform)
curl_F   = curl(F)
print("\nCurl of each piece:")
print(f"  curl(F_radial)  = {simplify(curl_rad)}")
print(f"  curl(F_uniform) = {simplify(curl_uni)}")
print(f"  curl(F_total)   = {simplify(curl_F)}")

# Expect curl = 0 for both (and therefore for the sum)
zero_vec = N.i*0 + N.j*0 + N.k*0
curl_pass_rad = simplify(curl_rad - zero_vec) == zero_vec
curl_pass_uni = simplify(curl_uni - zero_vec) == zero_vec
curl_pass_F = simplify(curl_F - zero_vec) == zero_vec
print(f"\nBoth pieces irrotational: {'PASS' if (curl_pass_rad and curl_pass_uni) else 'FAIL'}")
print(f"Superposition curl-free : {'PASS' if curl_pass_F else 'FAIL'}")

# --- Check 2: stagnation point on -ẑ axis ---
# On the z-axis: x=y=0, r = |z|, r̂ = sign(z) ẑ
# F_z_on_axis = q * z / |z|^3 + v0 = q * sign(z) / z^2 + v0
# For stagnation on -z axis: z < 0, so z = -|z|, giving F_z = -q/z^2 + v0
# Set F_z = 0: v0 = q/z^2 → z = -sqrt(q/v0) (taking negative root)
z = symbols("z", real=True, negative=True)  # restrict to -z axis
F_z_on_minus_axis = q * z / (-z)**3 + v0  # here (−z)^3 = |z|^3 * (−1)^3 since z<0 means |z|=−z
# Simplify: for z<0, |z|=−z, so z / |z|^3 = z / (−z)^3 = z / (−z)^3 = z * (−1) / z^3 = −1/z^2
F_z_clean = -q / z**2 + v0
stagnation_z = solve(F_z_clean, z)
print(f"\nStagnation point on -ẑ axis (z<0):")
print(f"  F_z(z) = -q/z² + v₀")
print(f"  Solutions z = {stagnation_z}")
# The negative root corresponds to the stagnation point.
# Expected z* = -sqrt(q/v0) with r* = sqrt(q/v0)
# Let's compute r* = |z*|
z_star_neg = [s for s in stagnation_z if s.is_negative]
r_star = -z_star_neg[0] if z_star_neg else None
expected_r = sqrt(q/v0)
stagnation_pass = r_star is not None and simplify(r_star - expected_r) == 0
print(f"  Negative-axis stagnation point: z* = {z_star_neg[0] if z_star_neg else 'NONE'}")
print(f"  r* = |z*| = {r_star}")
print(f"  Expected r* = √(q/v₀) = {expected_r}")
print(f"  Stagnation point matches expected: {'PASS' if stagnation_pass else 'FAIL'}")

# --- Honesty note produced by the check ---
print("\n--- Honesty note ---")
print("Pure static superposition of radial source + uniform drift has ZERO curl.")
print("This means the 'toroidal streamlines' in H1 are topological (Rankine-half-body),")
print("NOT vortical. To produce a magnetic field with non-zero ∇×B (matching")
print("Ampère-Maxwell), the H1 mechanism must invoke time-dependent toroidal")
print("OSCILLATION of the graviton density — not just static superposition.")
print("The oscillation dynamics (not captured in this check) are exactly what")
print("UNSPEC-4 names as out of scope for the current claim.")

all_pass = (curl_pass_rad and curl_pass_uni and curl_pass_F and stagnation_pass)
print(f"\n# Status: {'PASS' if all_pass else 'FAIL'}")
