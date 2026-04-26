"""
Check 05 — Symbolic derivation of the relative acceleration (SymPy)
Claim: E2-competing-attraction

Derive the relative acceleration ddot(r) = a_E2 - a_E1 symbolically,
confirming the decomposition into a "proton-gradient" term and an
"inter-electron" term shown in derivation.md §Relative acceleration:

  ddot(r) = G m_p [1/d^2 - 1/(d+r)^2] - 2 G m_e / r^2

Under physical parameters (d ~ r ~ a_0, m_p/m_e ~ 1836), the first term
dominates and ddot(r) > 0.
"""
import sys
import sympy as sp

print("# Check 05 — Symbolic derivation of ddot(r) via SymPy")
print(f"# SymPy: {sp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

G, m_e, m_p, d, r = sp.symbols('G m_e m_p d r', positive=True, real=True)

# Forces in 1D (positive = +x direction)
# E1 at +d, E2 at +d+r, proton at 0

# Force on E1 from proton (at x=0): toward proton (-x direction)
F_E1_from_P = -G * m_e * m_p / d**2
# Force on E1 from E2 (at +d+r): toward E2 (+x direction)
F_E1_from_E2 = +G * m_e**2 / r**2

# Force on E2 from proton (at x=0): toward proton (-x)
F_E2_from_P = -G * m_e * m_p / (d + r)**2
# Force on E2 from E1 (at +d): toward E1 (-x)
F_E2_from_E1 = -G * m_e**2 / r**2

F_E1 = F_E1_from_P + F_E1_from_E2
F_E2 = F_E2_from_P + F_E2_from_E1

a_E1 = F_E1 / m_e
a_E2 = F_E2 / m_e

ddot_r = sp.simplify(a_E2 - a_E1)
print(f"ddot(r) = a_E2 - a_E1 = {ddot_r}")

# Expected form from derivation.md
ddot_r_expected = G * m_p * (1/d**2 - 1/(d + r)**2) - 2 * G * m_e / r**2
diff = sp.simplify(ddot_r - ddot_r_expected)
print(f"\nExpected form         = G m_p (1/d^2 - 1/(d+r)^2) - 2 G m_e / r^2")
print(f"Difference (should be 0): {diff}")
assert diff == 0, f"FAIL: Symbolic form does not match expected: {diff}"
print("  PASS — ddot(r) matches derivation.md expected form.")

# Substitution: d = r = a_0 (the specific geometry used in the toy model)
a_0 = sp.Symbol('a_0', positive=True)
ddot_r_at_Bohr = sp.simplify(ddot_r.subs({d: a_0, r: a_0}))
print(f"\nAt d = r = a_0:  ddot(r) = {ddot_r_at_Bohr}")

# Simplify to isolate the two terms
# 1/d^2 - 1/(2d)^2 = 1/d^2 - 1/(4 d^2) = 3/(4 d^2)
#   so proton-gradient term = G m_p * 3 / (4 a_0^2)
# inter-electron term = -2 G m_e / a_0^2
proton_grad = G * m_p * sp.Rational(3, 4) / a_0**2
ee_term = -2 * G * m_e / a_0**2
sum_terms = sp.simplify(proton_grad + ee_term)
print(f"Isolated form: {sum_terms}")
match = sp.simplify(ddot_r_at_Bohr - sum_terms) == 0
print(f"  Match: {match}")

# Dominant-term check
ratio_terms = sp.simplify(proton_grad / (-ee_term))
print(f"\nRatio (proton-gradient term) / |inter-electron term| = {ratio_terms}")
print(f"  = 3 m_p / (8 m_e) (symbolic)")
# Numerical
numerical_ratio = ratio_terms.subs({m_p: 1.673e-27, m_e: 9.109e-31})
print(f"  numerical = {float(numerical_ratio):.3e}   (expect ~688)")
assert float(numerical_ratio) > 100, "Proton term should dominate by > 100x"

print("\n# Status: PASS — ddot(r) symbolic form verified, and proton-gradient term dominates by ~688x.")
