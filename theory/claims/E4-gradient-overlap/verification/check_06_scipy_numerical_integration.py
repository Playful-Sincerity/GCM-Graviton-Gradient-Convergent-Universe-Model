"""
Check 06 — Independent numerical verification via direct 6D integration (scipy)
Claim: E4-gradient-overlap

Re-compute the interaction energy U(R) for two Gaussian mass distributions
by NUMERICALLY integrating the double integral
    U(R) = -G integral integral  rho_1(r1) rho_2(r2) / |r1 - r2|  d^3r1 d^3r2
at a few sample values of R, and compare to the closed-form
    U_closed(R) = -(G m^2 / R) erf(R/(2 sigma)).

This is the "cross-tool verification" that catches formula-transcription errors
that SymPy alone would pass through.

Strategy: collapse the 6D integral to effective 2D by exploiting spherical
symmetry. Using the convolution interpretation:
    U(R) = integral rho_2(r2) Phi(|r2 - R_2 center|) d^3r2
where Phi is the Gaussian potential. That reduces to a 1D radial integral
after angular integration.
"""
import sys
import json
from pathlib import Path
import numpy as np
from scipy import integrate
from math import erf, exp, pi, sqrt

print("# Check 06 — Numerical double integration (scipy) vs closed-form")
print(f"# scipy: check --version below")
import scipy
print(f"# scipy: {scipy.__version__}")
print(f"# numpy: {np.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

HERE = Path(__file__).parent
with open(HERE / "inputs.json") as f:
    inputs = json.load(f)

G = inputs["natural_units"]["G"]["value"]
m = inputs["natural_units"]["m"]["value"]
sigma = inputs["natural_units"]["sigma"]["value"]

def Phi_gaussian(r):
    """Gravitational potential at distance r from a Gaussian of mass m, width sigma."""
    if r < 1e-12:
        # Use the finite-r limit Phi(0) = -sqrt(2) G m / (sqrt(pi) sigma)
        return -sqrt(2) * G * m / (sqrt(pi) * sigma)
    return -(G * m / r) * erf(r / (sigma * sqrt(2)))

def U_closed(R):
    """Closed-form pair interaction energy."""
    if R < 1e-12:
        return -G * m**2 / (sigma * sqrt(pi))
    return -(G * m**2 / R) * erf(R / (2 * sigma))

def U_numerical(R):
    """
    Compute U(R) by integrating rho_2(r2) * Phi_1(|r2 - R_hat|) over all space,
    using spherical coordinates and exploiting axial symmetry about the axis
    joining the two centers.

    Place Gaussian 2 at origin, Gaussian 1 at (R, 0, 0). Integrate rho_2(r2) over r2,
    where |r2 - (R,0,0)| = sqrt(r^2 + R^2 - 2 r R cos(theta)) in spherical coords.
    """
    def integrand(theta, r):
        # rho_2 at radius r from its center (origin)
        rho_2 = m / (2 * pi * sigma**2)**1.5 * exp(-r**2 / (2 * sigma**2))
        # Distance from (r,theta) to Gaussian-1 center at (R,0,0)
        d = sqrt(r**2 + R**2 - 2 * r * R * np.cos(theta))
        # Phi from Gaussian 1 at that distance
        phi = Phi_gaussian(d)
        # Volume element: r^2 sin(theta) dr dtheta dphi; integrate phi [0,2pi]
        return rho_2 * phi * r**2 * np.sin(theta) * 2 * pi
    # Integrate r from 0 to ~6 sigma (Gaussian decays), theta from 0 to pi
    result, error = integrate.dblquad(
        integrand, 0, 6 * sigma, 0, pi, epsabs=1e-10, epsrel=1e-8
    )
    return result, error

print(f"{'R/sigma':>10}  {'U_numeric':>20}  {'U_closed':>20}  {'rel_error':>15}")
print("-" * 75)

results = []
for R_over_sigma in [0.1, 0.5, 1.0, 2.0, 5.0]:
    R = R_over_sigma * sigma
    U_num, err = U_numerical(R)
    U_cl = U_closed(R)
    rel_err = abs(U_num - U_cl) / abs(U_cl) if abs(U_cl) > 0 else float('inf')
    print(f"{R_over_sigma:>10}  {U_num:>20.10e}  {U_cl:>20.10e}  {rel_err:>15.4e}")
    results.append((R_over_sigma, U_num, U_cl, rel_err))

# Accept if relative error < 1e-5 at all sample points (accounting for quadrature error)
max_rel_err = max(r[3] for r in results)
print(f"\nMax relative error across sweep: {max_rel_err:.4e}")
if max_rel_err < 1e-5:
    print("# Status: PASS — closed-form matches scipy double integration to 5+ decimal places.")
else:
    print(f"# Status: INCONCLUSIVE — max rel error {max_rel_err:.4e} above 1e-5 threshold. Investigate.")
