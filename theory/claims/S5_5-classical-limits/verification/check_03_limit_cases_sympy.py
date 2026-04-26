#!/usr/bin/env python3
"""
S5.5(a) — Check 03: Symbolic limit cases of F = G*m1*m2/r^2

Uses SymPy to verify three limit cases claimed in the derivation:
  1. F -> 0 as r -> infinity
  2. F -> 0 as either m1 or m2 -> 0
  3. For xi_A = xi_B = 1 (single-graviton "composites"), F -> G m_g^2 / r^2
     — recovering the minimal-model single-pair term
"""
import sys
from datetime import datetime

from sympy import symbols, oo, limit, Symbol, simplify, Eq

print(f"# Check: 03 — Symbolic limit cases")
print(f"# Claim: S5_5-classical-limits (sub-claim a — Newtonian limit)")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy symbolic limits")
print(f"# Script: verification/check_03_limit_cases_sympy.py")
print(f"# ----")

G, m1, m2, r, m_g, xi_A, xi_B = symbols("G m1 m2 r m_g xi_A xi_B", positive=True)

F = G * m1 * m2 / r**2

# --- Limit 1: r -> oo ---
L1 = limit(F, r, oo)
print(f"lim r->oo  G*m1*m2/r^2       = {L1}")
pass1 = L1 == 0

# --- Limit 2a: m1 -> 0 ---
L2a = limit(F, m1, 0)
print(f"lim m1->0  G*m1*m2/r^2       = {L2a}")
pass2a = L2a == 0

# --- Limit 2b: m2 -> 0 ---
L2b = limit(F, m2, 0)
print(f"lim m2->0  G*m1*m2/r^2       = {L2b}")
pass2b = L2b == 0

# --- Limit 3: single-graviton composites ---
# Substitute m1 = m_g * xi_A, m2 = m_g * xi_B, then set xi_A = xi_B = 1
F_composite = F.subs({m1: m_g * xi_A, m2: m_g * xi_B})
F_single = F_composite.subs({xi_A: 1, xi_B: 1})
F_expected = G * m_g**2 / r**2
print(f"\nSubstitute m1=m_g*xi_A, m2=m_g*xi_B, then xi_A=xi_B=1:")
print(f"  Result   = {F_single}")
print(f"  Expected = {F_expected}")
pass3 = simplify(F_single - F_expected) == 0
print(f"  Match: {'PASS' if pass3 else 'FAIL'}")

# --- Bonus: factorization check ---
# F = G * (m_g * xi_A) * (m_g * xi_B) / r^2 should equal G * xi_A * xi_B * m_g^2 / r^2
lhs = F_composite
rhs = G * xi_A * xi_B * m_g**2 / r**2
pass_factorization = simplify(lhs - rhs) == 0
print(f"\nFactorization: G*(m_g*xi_A)*(m_g*xi_B)/r^2 == G*xi_A*xi_B*m_g^2/r^2")
print(f"  Match: {'PASS' if pass_factorization else 'FAIL'}")
print(f"  This is the step 'm_g^2 * xi_A * xi_B = m_A * m_B' used in the derivation.")

all_pass = pass1 and pass2a and pass2b and pass3 and pass_factorization
print(f"\n# Status: {'PASS' if all_pass else 'FAIL'}")
