"""
Check 02 — Symbolic derivation of the gradient-gradient correlation C(R) via Fourier-trick
Claim: E3-vdw-universal

Derives the closed form
    C(R) = m^2 (6 sigma^2 - R^2) exp(-R^2/(4 sigma^2)) / (32 pi^{3/2} sigma^7)

using the identity
    C(R) = -Laplacian[(rho_1 * rho_2)](R)
where * is convolution. For two identical Gaussians of width sigma, the
auto-convolution is Gaussian with width sigma*sqrt(2), so
    (rho_1 * rho_2)(R) = m^2 / (4 pi sigma^2)^{3/2} * exp(-R^2/(4 sigma^2))
and then we apply the 3D radial Laplacian and the identity C = -Laplacian(conv).
"""
import sys
import sympy as sp

print("# Check 02 — SymPy derivation of C(R)")
print(f"# SymPy: {sp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

R, sigma, m = sp.symbols('R sigma m', positive=True, real=True)

# Auto-convolution of two Gaussians of width sigma — Gaussian of width sigma sqrt(2)
rho_conv = m**2 * (4 * sp.pi * sigma**2)**(-sp.Rational(3, 2)) * sp.exp(-R**2 / (4 * sigma**2))

# Radial 3D Laplacian applied to a function that depends only on R:
#    Laplacian f(R) = f''(R) + 2/R f'(R)
f = sp.exp(-R**2 / (4 * sigma**2))
laplacian_f = sp.diff(f, R, 2) + (2 / R) * sp.diff(f, R)
laplacian_f = sp.simplify(laplacian_f)
print(f"Laplacian of exp(-R^2/(4 sigma^2)) = {laplacian_f}")

# C(R) = -Laplacian[rho_conv] = -rho_conv_prefactor * Laplacian[gaussian]
C = -m**2 * (4 * sp.pi * sigma**2)**(-sp.Rational(3, 2)) * laplacian_f
C_simp = sp.simplify(C)
print(f"\nC(R) = {C_simp}")

# Expected form
expected = m**2 * (6 * sigma**2 - R**2) * sp.exp(-R**2 / (4 * sigma**2)) / (32 * sp.pi**sp.Rational(3, 2) * sigma**7)
diff = sp.simplify(C - expected)
print(f"\nExpected     = {expected}")
print(f"Difference   = {diff}")
assert diff == 0, f"Symbolic mismatch: {diff}"
print("  PASS — closed form matches.")

# Zero crossing
# C(R) = 0 requires (6 sigma^2 - R^2) = 0 → R = sigma sqrt(6)
zero_crossing = sp.sqrt(6) * sigma
C_at_zc = C.subs(R, zero_crossing)
print(f"\nZero crossing predicted at R = sigma*sqrt(6) = {zero_crossing}")
print(f"C(R = sigma sqrt(6)) = {sp.simplify(C_at_zc)}  (expect: 0)")
assert sp.simplify(C_at_zc) == 0
print("  PASS — zero crossing confirmed.")

# Asymptotic behavior — exponential, NOT 1/R^6
# At large R, C(R) ~ -m^2 R^2 exp(-R^2/(4 sigma^2)) / (32 pi^{3/2} sigma^7)
# -> exponentially suppressed
# If it were power-law 1/R^6, we'd have C(R) ~ const / R^6.
# Compare ratios at a few large R values (done numerically in check_03).

print("\n# Status: PASS — closed form and zero crossing symbolically verified.")
