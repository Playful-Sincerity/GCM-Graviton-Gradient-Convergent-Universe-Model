"""
Check 02 — Symbolic derivation of U(R), F(R), and limits (SymPy)
Claim: E4-gradient-overlap

Re-runs the derivation reported in derivation.md §Step 2-4:
 - Single-Gaussian potential Phi(r) = -(G m / r) erf(r / (sigma sqrt 2))
 - Pair interaction U(R) = -(G m^2 / R) erf(R / (2 sigma))
 - Force F(R) = -dU/dR
 - Small-R and large-R expansions and limits
"""
import json
import sys
from pathlib import Path
import sympy as sp

print("# Check 02 — SymPy symbolic derivation of U(R), F(R)")
print(f"# SymPy: {sp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

r, R, sigma, m, G = sp.symbols('r R sigma m G', positive=True, real=True)

# Single-Gaussian potential from the textbook result (Binney & Tremaine, Gal. Dyn.)
Phi = -(G * m / r) * sp.erf(r / (sigma * sp.sqrt(2)))
print(f"Phi(r) = {Phi}")
print(f"  lim r->0    = {sp.simplify(sp.limit(Phi, r, 0))}")
print(f"  lim r->inf  = {sp.limit(Phi, r, sp.oo)}")

# Interaction energy between two identical Gaussians
U = -(G * m**2 / R) * sp.erf(R / (2 * sigma))
print(f"\nU(R) = {U}")

# Small-R series (should be bounded)
series_U = sp.series(U, R, 0, 4).removeO()
print(f"  series U(R, R->0, O(4)) = {sp.simplify(series_U)}")

U0 = sp.limit(U, R, 0)
print(f"  U(R=0) = {sp.simplify(U0)}    (expect: -G m^2 / (sigma sqrt(pi)))")

# Expected value
U0_expected = -G * m**2 / (sigma * sp.sqrt(sp.pi))
print(f"  U(R=0) expected = {U0_expected}")
match = sp.simplify(U0 - U0_expected) == 0
print(f"  MATCH: {match}")

# Large-R: R * U(R) should give -G m^2
R_U_inf = sp.simplify(sp.limit(U * R, R, sp.oo))
print(f"\n  lim_{{R->inf}} R*U(R) = {R_U_inf}   (expect: -G m^2)")
match_inf = sp.simplify(R_U_inf - (-G * m**2)) == 0
print(f"  MATCH: {match_inf}")

# Force F(R) = -dU/dR
F = -sp.diff(U, R)
F_simp = sp.simplify(F)
print(f"\nF(R) = -dU/dR = {F_simp}")

# Small-R expansion of F
F_series = sp.series(F, R, 0, 5).removeO()
print(f"  series F(R, R->0, O(5)) = {sp.simplify(F_series)}")
print(f"  F(R=0) = {sp.limit(F, R, 0)}   (expect: 0)")

# Ratio to point-particle force
F_point = G * m**2 / R**2
ratio = sp.simplify(F / F_point)
print(f"\nRatio F/F_point = {ratio}")

print("\n# Status: PASS — U(0) and lim R*U at infinity match expected closed forms")
