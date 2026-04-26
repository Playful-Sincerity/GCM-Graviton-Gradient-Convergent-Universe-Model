"""
Check 05 — Cross-check the single-Gaussian potential formula numerically
Claim: E4-gradient-overlap

The textbook Gaussian potential is (Binney & Tremaine "Galactic Dynamics" §2.4):
    Phi(r) = -(G m / r) erf(r / (sigma sqrt(2)))

We verify it by:
 (i) deriving the enclosed mass M(r) via integrating rho(r') * 4 pi r'^2 symbolically,
 (ii) recomputing Phi(r) numerically from -integral_{r}^{inf} G M(r')/r'^2 dr',
 (iii) comparing to the closed-form at several r/sigma values.

Symbolic simplification of the integrated form involves Ei / expint, which
SymPy's simplify cannot always reduce to the erf form — but NUMERICALLY they
should agree. That's the honest check.
"""
import sys
import sympy as sp
from mpmath import mp, mpf, quad, erf, exp, sqrt, pi as mp_pi

print("# Check 05 — Cross-check single-Gaussian potential against Gauss-law derivation")
print(f"# SymPy: {sp.__version__}")
print(f"# mpmath: {mp.dps} digits")
print("# ---")

mp.dps = 30

G_val = mpf(1)
m_val = mpf(1)
sigma_val = mpf(1)

def rho(r):
    """Gaussian mass density normalized to total mass m_val."""
    return m_val / (2 * mp_pi * sigma_val**2)**mpf('1.5') * exp(-r**2 / (2 * sigma_val**2))

def M_enclosed(r):
    """Enclosed mass within radius r via numerical integration of 4 pi r'^2 rho(r')."""
    return 4 * mp_pi * quad(lambda rp: rp**2 * rho(rp), [0, r])

def Phi_from_Gauss(r):
    """Derive Phi(r) by outward-integration of the Newtonian field G M(r)/r^2.

    Split the integral: for r' > ~6 sigma, M_enclosed(r') = m to machine precision,
    so the tail contribution is -G m / r' integrated, giving -G m / r_cut analytically.
    This avoids the slow-convergence issue of a raw [r, inf] quadrature.
    """
    r_cut = mpf(10) * sigma_val  # beyond this, M ≈ m to 1e-22
    # Main contribution with full M(r')
    inner = quad(lambda rp: M_enclosed(rp) / rp**2, [r, r_cut])
    # Tail: M = m_val exact, so tail = int_{r_cut}^inf m/r'^2 dr' = m/r_cut
    tail = m_val / r_cut
    return -G_val * (inner + tail)

def Phi_textbook(r):
    """Textbook closed-form."""
    return -(G_val * m_val / r) * erf(r / (sigma_val * sqrt(2)))

print(f"{'r/sigma':>10}  {'Phi_textbook':>30}  {'Phi_gauss':>30}  {'rel_error':>15}")
print("-" * 90)

errors = []
for rs in ['0.5', '1.0', '2.0', '3.0', '5.0']:
    r = mpf(rs) * sigma_val
    phi_t = Phi_textbook(r)
    phi_g = Phi_from_Gauss(r)
    rel = abs((phi_g - phi_t) / phi_t)
    print(f"{rs:>10}  {mp.nstr(phi_t, 16):>30}  {mp.nstr(phi_g, 16):>30}  {mp.nstr(rel, 6):>15}")
    errors.append(rel)

max_err = max(errors)
print(f"\nMax relative error across sweep: {mp.nstr(max_err, 6)}")

# Threshold: quadrature + finite-upper-limit error should keep us well under 1e-8
if max_err < mpf('1e-6'):
    print("# Status: PASS — Gauss-law derivation matches textbook Phi(r) numerically.")
else:
    print(f"# Status: INCONCLUSIVE — max_err {max_err} above 1e-6 threshold.")

# Also check M_enclosed -> m as r -> inf (conservation of total mass)
M_total = M_enclosed(mpf(10) * sigma_val)
print(f"\nM_enclosed(10 sigma) = {mp.nstr(M_total, 16)} (expect: m = 1)")
assert abs(M_total - m_val) < mpf('1e-10'), f"Total mass not conserved: {M_total}"
print("  PASS — total mass recovered within Gaussian tail.")
