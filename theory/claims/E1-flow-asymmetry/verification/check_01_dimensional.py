"""
Check 01 — Dimensional analysis of the flow equation
Claim: E1-flow-asymmetry

Verify all terms in
    J_g = -D * grad(rho_g) + v_g * rho_g
have consistent dimensions of mass flux (kg/m^2/s), and that the continuity
equation
    d rho_g / dt + div(J_g) = 0
is dimensionally closed.
"""
import sys

print("# Check 01 — Dimensional analysis of J_g and continuity")
print(f"# Python: {sys.version.split()[0]}")

try:
    import pint
    print(f"# Tool: Pint {pint.__version__}")
    print("# ---")
    u = pint.UnitRegistry()

    # Define physical dimensions
    rho_g = 1 * u.kilogram / u.meter**3       # graviton mass density
    D     = 1 * u.meter**2 / u.second         # diffusion coefficient
    v_g   = 1 * u.meter / u.second            # drift velocity
    grad_length = 1 / u.meter                 # gradient operator adds 1/m
    time_inv = 1 / u.second                   # d/dt adds 1/s
    J_g_target = 1 * u.kilogram / u.meter**2 / u.second

    # Term 1: D * grad(rho_g)
    term1 = D * grad_length * rho_g
    # Term 2: v_g * rho_g
    term2 = v_g * rho_g

    print(f"-D grad(rho_g) dim = {term1.dimensionality}")
    print(f"v_g * rho_g   dim = {term2.dimensionality}")
    print(f"J_g target    dim = {J_g_target.dimensionality}")
    assert term1.dimensionality == J_g_target.dimensionality, "Diffusion term mismatch"
    assert term2.dimensionality == J_g_target.dimensionality, "Drift term mismatch"
    print("  PASS — both terms have units of mass flux (kg/m^2/s).")

    # Continuity: d rho_g / dt + div(J_g) = 0
    # div adds 1/m, so div(J_g) has dim [J_g]/m
    drho_dt = rho_g * time_inv
    div_J = J_g_target * grad_length
    print(f"\nd rho_g / dt dim = {drho_dt.dimensionality}")
    print(f"div(J_g)     dim = {div_J.dimensionality}")
    assert drho_dt.dimensionality == div_J.dimensionality
    print("  PASS — continuity equation dimensionally closed.")

    # Surface-integrated flux Phi_g = integral(J_g . dA) has units of J_g * m^2
    Phi_g = J_g_target * u.meter**2
    print(f"\nSurface flux Phi_g dim = {Phi_g.dimensionality}  (expect kg/s)")
    expected = (1 * u.kilogram / u.second).dimensionality
    assert Phi_g.dimensionality == expected
    print("  PASS — Phi_g has units of mass flow rate (kg/s).")

    print("\n# Status: PASS — flow equation, continuity, and flux are dimensionally consistent.")

except ImportError:
    import sympy as sp
    print("# Tool: SymPy (Pint unavailable)")
    print("# ---")
    L, M, T = sp.symbols('L M T', positive=True)
    rho_g_d = M / L**3
    D_d = L**2 / T
    v_g_d = L / T
    grad = 1 / L
    time_inv = 1 / T
    J_target = M / L**2 / T

    term1 = D_d * grad * rho_g_d
    term2 = v_g_d * rho_g_d
    div_J = J_target * grad
    drho_dt = rho_g_d * time_inv

    print(f"-D grad(rho_g) = {sp.simplify(term1)}  target: {J_target}")
    assert sp.simplify(term1 - J_target) == 0
    print("  PASS")

    print(f"v_g rho_g = {sp.simplify(term2)}  target: {J_target}")
    assert sp.simplify(term2 - J_target) == 0
    print("  PASS")

    print(f"div(J_g)   = {sp.simplify(div_J)}")
    print(f"d rho/dt   = {sp.simplify(drho_dt)}")
    assert sp.simplify(div_J - drho_dt) == 0
    print("  PASS — continuity closed.")

    print("\n# Status: PASS (SymPy fallback).")
