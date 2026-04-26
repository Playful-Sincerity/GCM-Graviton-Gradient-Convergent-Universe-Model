#!/usr/bin/env python3
"""E7 Check 1 — SymPy symbolic derivation.

Confirms the key identity: setting the total differential of the Bohr
ground state E_1(m_e, e) = -m_e * k^2 * e^4 / (2 * hbar^2) to zero yields
Delta_m_e / m_e = -4 * Delta_e / e.

This is the load-bearing symbolic check for E7.
"""
from sympy import symbols, diff, simplify, solve, Rational, Symbol, sstr

m_e, k, e, hbar = symbols('m_e k e hbar', positive=True, real=True)
De, Dm = symbols('Delta_e Delta_m', real=True)

E1 = -m_e * k**2 * e**4 / (2 * hbar**2)

dE1_de = diff(E1, e)
dE1_dm = diff(E1, m_e)

# Simplify each partial in terms of E1 itself
# Expected: dE1/de = 4*E1/e, dE1/dm_e = E1/m_e
expected_de = 4 * E1 / e
expected_dm = E1 / m_e

print("# E7 Check 1 — SymPy symbolic derivation")
print()
print(f"E_1              = {E1}")
print(f"dE_1/de          = {dE1_de}")
print(f"dE_1/dm_e        = {dE1_dm}")
print()
print(f"Expected: dE_1/de = 4*E_1/e = {expected_de}")
print(f"Expected: dE_1/dm_e = E_1/m_e = {expected_dm}")
print()

# Verify the analytical simplifications
diff_de_form = simplify(dE1_de - expected_de)
diff_dm_form = simplify(dE1_dm - expected_dm)
print(f"diff (dE/de - 4E1/e) simplified     = {diff_de_form}")
print(f"diff (dE/dm_e - E1/m_e) simplified  = {diff_dm_form}")
print()

de_ok = diff_de_form == 0
dm_ok = diff_dm_form == 0

# Now solve the perturbation condition dE1/de * Delta_e + dE1/dm_e * Delta_m = 0
# for Delta_m, then divide by m_e to get the ratio.
perturb_eq = dE1_de * De + dE1_dm * Dm
sol = solve(perturb_eq, Dm)
print(f"Solve dE1/de * Delta_e + dE1/dm_e * Delta_m = 0 for Delta_m:")
print(f"  Delta_m = {sol[0]}")

# Compute the ratio (Delta_m / m_e) / (Delta_e / e) — expected to be -4
ratio = simplify((sol[0] / m_e) / (De / e))
print()
print(f"Ratio (Delta_m/m_e) / (Delta_e/e) = {ratio}")
print()

ratio_ok = (ratio == -4) or (simplify(ratio - (-4)) == 0)

all_pass = de_ok and dm_ok and ratio_ok
print("STATUS:", "PASS" if all_pass else "FAIL")
if not all_pass:
    print(f"  partial derivative check (de): {'OK' if de_ok else 'FAIL'}")
    print(f"  partial derivative check (dm): {'OK' if dm_ok else 'FAIL'}")
    print(f"  ratio check: {'OK' if ratio_ok else 'FAIL'}")
