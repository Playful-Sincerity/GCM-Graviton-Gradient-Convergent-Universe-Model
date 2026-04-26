"""
Check 03 — Symbolic computation of div(J_g) for generic rho_g and v_g (SymPy)
Claim: E1-flow-asymmetry

Verify the general identity used in derivation.md:
    div(J_g) = div(-D grad(rho_g) + v_g rho_g)
             = -D laplacian(rho_g) + rho_g * div(v_g) + v_g . grad(rho_g)

This is straightforward vector calculus but worth recording for the audit
trail — the identity underlies the "steady-state particles have divergence-
free internal currents but nonzero far-field graviton fluxes" reading.
"""
import sys
import sympy as sp

print("# Check 03 — Symbolic divergence of J_g")
print(f"# SymPy: {sp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

# Use sympy.vector for clean coordinate-free expressions
from sympy.vector import CoordSys3D, divergence, gradient, Laplacian

N = CoordSys3D('N')

# Let rho_g and the components of v_g be generic functions of position
rho_g = sp.Function('rho')(N.x, N.y, N.z)
vx = sp.Function('vx')(N.x, N.y, N.z)
vy = sp.Function('vy')(N.x, N.y, N.z)
vz = sp.Function('vz')(N.x, N.y, N.z)
D = sp.Symbol('D', positive=True)

# v_g as a vector field
v_g = vx * N.i + vy * N.j + vz * N.k

# grad(rho_g)
grad_rho = gradient(rho_g)
print(f"grad(rho_g) = {grad_rho}")

# J_g = -D grad(rho_g) + v_g rho_g
J_g = -D * grad_rho + v_g * rho_g

# div(J_g) — computed symbolically
div_J_raw = divergence(J_g)
div_J = sp.expand(sp.simplify(div_J_raw))

# Expected form: -D * Laplacian(rho_g) + rho_g * div(v_g) + v_g . grad(rho_g)
lap_rho = Laplacian(rho_g).doit()
div_v = divergence(v_g)
dot_v_grad_rho = vx * sp.diff(rho_g, N.x) + vy * sp.diff(rho_g, N.y) + vz * sp.diff(rho_g, N.z)
expected = -D * lap_rho + rho_g * div_v + dot_v_grad_rho
expected_expanded = sp.expand(sp.simplify(expected))

diff = sp.simplify(div_J - expected_expanded)
print(f"\ndiv(J_g) == -D lap(rho) + rho div(v) + v.grad(rho) ?")
print(f"  Difference: {diff}")
assert diff == 0, f"FAIL: identity does not hold: {diff}"
print("  PASS — the identity holds symbolically.")

# Continuity equation: d rho/dt + div(J_g) = 0
# Steady state: d rho/dt = 0 -> div(J_g) = 0 LOCALLY (everywhere in the bulk).
# For a localized particle, the bulk is outside the particle's support (or the
# delta-function source is at the particle's center).
print("\nContinuity equation (steady state): div(J_g) = 0 everywhere in the bulk.")
print("Enclosing-surface flux Phi_g = integral(J_g . dA) can still be nonzero")
print("if the particle is represented as a delta-function source at r = 0.")

print("\n# Status: PASS — vector-calculus identity verified symbolically.")
