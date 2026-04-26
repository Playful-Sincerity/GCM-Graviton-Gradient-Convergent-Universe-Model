"""
Check 01 — Dimensional analysis of the toy-model expressions
Claim: E2-competing-attraction

Verify that:
  F_gravity = G m_1 m_2 / r^2        has units of N
  F_Coulomb = k_C e^2 / r^2           has units of N
  F_eff     = mu * d^2 r / dt^2       has units of N  (reduced-mass definition)
"""
import json
import sys
from pathlib import Path

print("# Check 01 — Dimensional analysis of E2 force expressions")
print(f"# Python: {sys.version.split()[0]}")

try:
    import pint
    print(f"# Tool: Pint {pint.__version__}")
    print("# ---")
    u = pint.UnitRegistry()

    G   = 1 * u.meter**3 / u.kilogram / u.second**2
    m_e = 1 * u.kilogram
    m_p = 1 * u.kilogram
    r   = 1 * u.meter
    k_C = 1 * u.newton * u.meter**2 / u.coulomb**2
    e   = 1 * u.coulomb
    mu  = 1 * u.kilogram
    a   = 1 * u.meter / u.second**2

    F_grav_dim = (G * m_e * m_p / r**2).dimensionality
    F_coul_dim = (k_C * e**2 / r**2).dimensionality
    F_eff_dim  = (mu * a).dimensionality
    newton_dim = (1 * u.newton).dimensionality

    print(f"F_gravity  dim = {F_grav_dim}")
    print(f"F_Coulomb  dim = {F_coul_dim}")
    print(f"F_effect.  dim = {F_eff_dim}")
    print(f"Newton     dim = {newton_dim}")

    for name, d in [("F_gravity", F_grav_dim), ("F_Coulomb", F_coul_dim), ("F_effective", F_eff_dim)]:
        assert d == newton_dim, f"{name} not in N: {d}"
        print(f"  PASS — {name} is in newtons.")

    print("\n# Status: PASS — all three force expressions have units of N.")

except ImportError:
    import sympy as sp
    print("# Tool: SymPy (Pint unavailable)")
    print("# ---")
    L, M, T, Q = sp.symbols('L M T Q', positive=True)
    G_d   = L**3 / (M * T**2)
    mass  = M
    r_d   = L
    kC_d  = M * L**3 / (T**2 * Q**2)   # N m^2 / C^2 = kg m^3 / (s^2 C^2)
    e_d   = Q
    accel = L / T**2

    F_grav = G_d * mass**2 / r_d**2
    F_coul = kC_d * e_d**2 / r_d**2
    F_eff  = mass * accel
    newton = M * L / T**2

    for name, expr in [("F_grav", F_grav), ("F_coul", F_coul), ("F_eff", F_eff)]:
        print(f"{name} dim = {sp.simplify(expr)}")
        assert sp.simplify(expr - newton) == 0, f"{name} not in N: {expr}"
        print(f"  PASS")
    print("\n# Status: PASS — all via SymPy fallback.")
