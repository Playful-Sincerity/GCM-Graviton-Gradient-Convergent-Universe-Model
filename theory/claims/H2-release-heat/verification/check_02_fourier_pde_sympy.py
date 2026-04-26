#!/usr/bin/env python3
"""
H2 — Check 02: Fourier heat equation structure via SymPy

Claim: Starting from
    continuity:  ∂ρ_g/∂t + ∇·J_g = 0
    flux law:    J_g = -D ∇ρ_g

derive the Fourier diffusion PDE:
    ∂ρ_g/∂t = D ∇²ρ_g

Mapping T ∝ ρ_g yields the standard Fourier heat equation
    ∂T/∂t = α ∇²T,  α = D.

Verify symbolically that the substitution produces the Laplacian form.
"""
import sys
from datetime import datetime

from sympy import symbols, Function, Derivative, diff, simplify
from sympy.vector import CoordSys3D, divergence, gradient

print(f"# Check: 02 — Fourier heat equation structure via SymPy vector calculus")
print(f"# Claim: H2-release-heat")
print(f"# Run: {datetime.now():%Y-%m-%d %H:%M}")
print(f"# Tool: python3 {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} / SymPy 1.14.0 (vector calculus)")
print(f"# Script: verification/check_02_fourier_pde_sympy.py")
print(f"# ----")

# Set up 3D coordinates
N = CoordSys3D("N")
x, y, z, t, D = symbols("x y z t D", positive=True, real=True)

# Scalar density field ρ_g(x, y, z, t)
rho = Function("rho_g")(N.x, N.y, N.z, t)

# Compute gradient of ρ_g
grad_rho = gradient(rho)
print(f"∇ρ_g (SymPy): {grad_rho}")

# Flux J_g = -D ∇ρ_g
J_g = -D * grad_rho
print(f"\nJ_g = -D ∇ρ_g: {J_g}")

# Divergence of flux: ∇·J_g
div_J = divergence(J_g)
print(f"\n∇·J_g = {div_J}")

# Continuity equation:  ∂ρ_g/∂t = -∇·J_g
# So:  ∂ρ_g/∂t = -∇·(-D∇ρ_g) = D ∇²ρ_g
lhs = diff(rho, t)
rhs = -div_J
print(f"\nContinuity: ∂ρ_g/∂t = {lhs}")
print(f"           -∇·J_g = {rhs}")

# Claim: the right-hand side equals D · (Laplacian of ρ_g)
laplacian_rho = diff(rho, N.x, 2) + diff(rho, N.y, 2) + diff(rho, N.z, 2)
expected_rhs = D * laplacian_rho
print(f"\nExpected RHS = D ∇²ρ_g = D·({laplacian_rho})")

difference = simplify(rhs - expected_rhs)
passed = difference == 0
print(f"\nDifference (actual RHS - expected): {difference}")
print(f"\nFourier PDE ∂ρ/∂t = D ∇²ρ derived correctly: {'PASS' if passed else 'FAIL'}")

print(f"\n# Status: {'PASS' if passed else 'FAIL'}")
