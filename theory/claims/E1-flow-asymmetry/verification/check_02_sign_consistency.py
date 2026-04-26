"""
Check 02 — Sign consistency with electron/proton/neutron phenomenology
Claim: E1-flow-asymmetry

E1 posits the sign mapping:
  Electron  (q = -e):  div J_g > 0    (net outflow, graviton flux OUT of particle)
  Proton    (q = +e):  div J_g < 0    (net inflow, graviton flux INTO particle)
  Neutron   (q = 0):   div J_g = 0    (balanced)

Verify this mapping against the known particle charge signs (including
antiparticles), and compute a simple toy-model flux for a radially-outward
velocity field v_g = A/r^2 to confirm the mathematical shape of "source-like"
flow.
"""
import sys
import json
from pathlib import Path

print("# Check 02 — Sign consistency of E1 flow mapping with phenomenology")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

HERE = Path(__file__).parent
with open(HERE / "inputs.json") as f:
    inp = json.load(f)

table = inp["phenomenology_sign_table"]

def sign_from_flux_label(label):
    return {">0": "positive", "<0": "negative", "=0": "zero"}[label]

def expected_charge_from_flux(flux_label):
    # Mapping per E1: outflow = negative charge, inflow = positive, balanced = neutral
    return {">0": "-", "<0": "+", "=0": "0"}[flux_label]

all_consistent = True
print(f"{'Particle':<12} {'Observed charge':<18} {'Posited div J_g':<18} {'Derived charge':<18} {'Consistent?'}")
print("-" * 80)
for particle, props in table.items():
    observed_sign = props["charge_sign"]
    posited_div = props["expected_div_J_g"]
    derived_sign = expected_charge_from_flux(posited_div)
    consistent = observed_sign == derived_sign
    all_consistent &= consistent
    print(f"{particle:<12} {observed_sign:<18} {posited_div:<18} {derived_sign:<18} {'YES' if consistent else 'NO'}")

assert all_consistent, "Sign mapping inconsistent with phenomenology"
print("\n  PASS — E1's sign mapping is self-consistent across 5 particle species.")

# Now the toy-model calculation: outward radial flow v_g = A/r^2, constant rho_g = rho_0.
# Verify that:
#   (i) div(J_g) = 0 in bulk (r > 0), because J_g = rho_0 * A / r^2 * r_hat,
#       and div(r_hat / r^2) = 0 for r > 0 (classic).
#   (ii) Surface integral Phi_g = 4 pi R^2 * (rho_0 A / R^2) = 4 pi rho_0 A.
# These demonstrate the source-like shape consistent with E1's "steady-state
# electron has divergence-free internal flow but nonzero external flux."

import sympy as sp
r, theta, phi, rho_0, A = sp.symbols('r theta phi rho_0 A', positive=True, real=True)

# Radial velocity: v = A / r^2 * r_hat
v_r = A / r**2
# J_g = rho_0 * v_r * r_hat
# div in spherical coords for radial vector field: (1/r^2) d(r^2 * F_r)/dr
J_r = rho_0 * v_r
div_J = (1 / r**2) * sp.diff(r**2 * J_r, r)
div_J_simp = sp.simplify(div_J)
print(f"\nToy model: J_g = (rho_0 * A / r^2) r_hat")
print(f"  div(J_g) = {div_J_simp}  (expect 0 for r>0)")
assert div_J_simp == 0
print("  PASS — divergence vanishes in the bulk (r > 0).")

# Surface integral over sphere of radius R
R_s = sp.Symbol('R_s', positive=True)
# J_g . dA = J_r * R^2 * sin(theta) dtheta dphi; integrate over (0, pi) x (0, 2pi)
flux = sp.integrate(J_r.subs(r, R_s) * R_s**2 * sp.sin(theta),
                    (theta, 0, sp.pi), (phi, 0, 2 * sp.pi))
flux_simp = sp.simplify(flux)
print(f"\n  Surface flux Phi_g over sphere r=R = {flux_simp}")
print(f"  Expected: 4 pi rho_0 A  (independent of R — source-like)")
expected = 4 * sp.pi * rho_0 * A
assert sp.simplify(flux_simp - expected) == 0
print("  PASS — flux is R-independent (source-like).")

# The coexistence of div = 0 and Phi_g != 0 is what E1 needs:
# continuity is preserved in the bulk, but the particle acts as a point source
# (delta-function at origin, or a nonzero density pattern at the particle's
# center that sources the outward flow).
print(f"\nKey observation: div(J_g) = 0 everywhere except r = 0 (the particle center).")
print(f"The point-source is mathematically a delta function; physically, in GCM,")
print(f"the steady-state density pattern at the electron's core sources the outflow")
print(f"by internal graviton recycling (not by net creation).")

print("\n# Status: PASS — E1 sign mapping consistent with phenomenology; toy radial flow demonstrates the formal shape.")
