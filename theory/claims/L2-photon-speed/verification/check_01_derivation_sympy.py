#!/usr/bin/env python3
"""L2 Check 1 — Symbolic derivation from energy-momentum relation.

Starting from E^2 = (pc)^2 + (m_gamma c^2)^2 and group velocity
v = dE/dp, confirm the closed form
  v_photon = c_causality * sqrt(1 - (m_gamma * c_causality^2 / E)^2)

Per the speed-of-causality-principle convention, `c` here denotes the
causality limit, not the speed of light; `v_photon` is strictly less
than `c` whenever m_gamma > 0 (which GCM commits to, L1).
"""
from sympy import symbols, sqrt, simplify, diff, solve, series, Rational

E, p, c, m_g = symbols('E p c_causality m_gamma', positive=True, real=True)

print("# L2 Check 1 — Symbolic derivation from E^2 = (pc)^2 + (m_gamma c^2)^2")
print()

# Solve for p in terms of E and m_gamma
p_sol = solve(E**2 - (p*c)**2 - (m_g * c**2)**2, p)
# Take the positive root
p_expr = [s for s in p_sol if s != 0 and s.is_real is not False][0]
print(f"p(E, m_g, c)  = {simplify(p_expr)}")
print()

# v = dE/dp from E = sqrt((pc)^2 + (m_g c^2)^2)
E_of_p = sqrt((p*c)**2 + (m_g * c**2)**2)
v_expr = simplify(diff(E_of_p, p))
print(f"v = dE/dp       = {v_expr}")
print()

# Express v in terms of E and m_g (eliminate p)
v_in_E = simplify(v_expr.subs(p, p_expr))
v_in_E_simpler = simplify(v_in_E)
print(f"v(E, m_g, c)    = {v_in_E_simpler}")
print()

# Compare with the expected closed form
expected = c * sqrt(1 - (m_g * c**2 / E)**2)
print(f"Expected form   = {expected}")

diff_expr = simplify(v_in_E_simpler - expected)
print(f"Difference      = {diff_expr}")
print()

# Taylor expansion for small epsilon = m_g c^2 / E
eps = m_g * c**2 / E
taylor = series(c * sqrt(1 - eps**2), eps, 0, 5).removeO()
print(f"Taylor expansion in epsilon = m_g c^2 / E:")
print(f"  v ≈ {taylor}")
Dv_taylor = simplify(c - taylor)
print(f"  Δv = c - v ≈ {Dv_taylor}")
print()

# The key property: v < c for any finite E, m_g > 0
# symbolically, sqrt(1 - x^2) < 1 for x > 0
print("Key structural property (per speed-of-causality principle):")
print(f"  For m_g > 0 and finite E: sqrt(1 - (m_g c^2/E)^2) < 1")
print(f"  Therefore v_photon < c_causality, strictly.")
print()

all_ok = (diff_expr == 0)
print("STATUS:", "PASS" if all_ok else "FAIL")
