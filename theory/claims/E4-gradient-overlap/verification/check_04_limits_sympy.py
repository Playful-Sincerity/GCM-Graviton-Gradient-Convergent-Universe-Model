"""
Check 04 — Limit cases (SymPy symbolic)
Claim: E4-gradient-overlap

Verifies symbolically:
  - lim_{R->0}  U(R) = -G m^2 / (sigma sqrt(pi))  (finite binding, regularized)
  - lim_{R->0}  F(R) = 0                          (linear-in-R approach to zero)
  - lim_{R->inf} R*U(R) = -G m^2                  (point-mass potential recovery)
  - lim_{R->inf} R^2 * F(R) = G m^2               (Newton's law recovery)
"""
import sys
import sympy as sp

print("# Check 04 — Symbolic limits")
print(f"# SymPy: {sp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

R, sigma, m, G = sp.symbols('R sigma m G', positive=True, real=True)

U = -(G * m**2 / R) * sp.erf(R / (2 * sigma))
# Sign convention in derivation.md: F = magnitude of attractive force = +dU/dR
# (U<0 increasing toward 0 as R grows, so dU/dR > 0 is the attractive magnitude).
F = sp.diff(U, R)

# Limit 1: U(R -> 0)
U0 = sp.simplify(sp.limit(U, R, 0))
U0_expected = -G * m**2 / (sigma * sp.sqrt(sp.pi))
print(f"lim U(R->0) = {U0}")
print(f"  expected  = {U0_expected}")
assert sp.simplify(U0 - U0_expected) == 0, f"FAIL: U(0) doesn't match. got {U0}"
print("  PASS")

# Limit 2: F(R -> 0)
F0 = sp.simplify(sp.limit(F, R, 0))
print(f"\nlim F(R->0) = {F0}")
print(f"  expected  = 0")
assert F0 == 0, f"FAIL: F(0) != 0. got {F0}"
print("  PASS (regularized, no 1/R^2 divergence)")

# Limit 3: R * U(R) at R -> inf
RU_inf = sp.simplify(sp.limit(R * U, R, sp.oo))
print(f"\nlim R*U(R -> inf) = {RU_inf}")
print(f"  expected        = -G m^2")
assert sp.simplify(RU_inf - (-G * m**2)) == 0, f"FAIL: large-R point-mass recovery. got {RU_inf}"
print("  PASS (point-mass potential recovered)")

# Limit 4: R^2 * F(R) at R -> inf
R2F_inf = sp.simplify(sp.limit(R**2 * F, R, sp.oo))
print(f"\nlim R^2 * F(R -> inf) = {R2F_inf}")
print(f"  expected            = G m^2")
assert sp.simplify(R2F_inf - G * m**2) == 0, f"FAIL: Newton recovery. got {R2F_inf}"
print("  PASS (Newton's law recovered in the far field)")

# Series expansion of F at small R — confirm LINEAR
F_series = sp.series(F, R, 0, 5).removeO()
print(f"\nSmall-R series F(R) = {sp.simplify(F_series)}")
# Coefficient of R^1 should be nonzero; R^0 should vanish
coeffs = sp.Poly(F_series, R).all_coeffs()[::-1]  # ascending: R^0, R^1, ...
print(f"  Coefficient of R^0 = {coeffs[0] if len(coeffs) > 0 else 0}")
print(f"  Coefficient of R^1 = {coeffs[1] if len(coeffs) > 1 else 0}")
assert coeffs[0] == 0, "F(R->0) should vanish"
assert coeffs[1] != 0, "F(R) should be LINEAR in R near origin"
print("  PASS — F(R) is linear in R near origin (spring-like)")

print("\n# Status: PASS — all four limits match the derivation.md claims.")
