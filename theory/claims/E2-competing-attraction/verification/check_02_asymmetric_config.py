"""
Check 02 — Asymmetric-config numerical simulation (Config A, the load-bearer)
Claim: E2-competing-attraction

Geometry: proton at origin, E1 at +a_0, E2 at +2 a_0. Both electrons on the +x
side of the proton. Compute Newtonian gravitational forces on each electron
from (i) the proton and (ii) the other electron. Verify:

  - Net force on E1: in -x direction, dominated by proton pull.
  - Net force on E2: in -x direction, weaker than E1's (farther from proton).
  - Relative acceleration ddot_r = a_E2 - a_E1 > 0 → apparent repulsion.
  - Effective inter-electron "repulsive" force ~ 1.361e-47 N.
  - Ratio to Coulomb at r = a_0: ~ 1.65e-40 (off by ~6e39).

Re-produces the Session C numerical table (E2/derivation.md §Numerical result).
"""
import json
import sys
from pathlib import Path
from mpmath import mp, mpf

print("# Check 02 — Asymmetric-config toy model (Python + mpmath)")
print(f"# mpmath precision: 30 digits")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

mp.dps = 30

HERE = Path(__file__).parent
with open(HERE / "inputs.json") as f:
    inp = json.load(f)

G = mpf(inp["constants"]["G"]["value"])
m_e = mpf(inp["constants"]["m_e"]["value"])
m_p = mpf(inp["constants"]["m_p"]["value"])
a_0 = mpf(inp["constants"]["a_0"]["value"])
k_C = mpf(inp["constants"]["k_C"]["value"])
e_elem = mpf(inp["constants"]["e"]["value"])

# Asymmetric geometry
x_P = mpf(0)
x_E1 = a_0            # d = Bohr radius
x_E2 = 2 * a_0        # E1 + r where r = Bohr radius

def force_1D(x_source, m_source, x_target, m_target):
    """Gravitational force on target at x_target due to source at x_source.
    Sign: in +x direction if source is at +x relative to target (attractive)."""
    dx = x_source - x_target
    r = abs(dx)
    if r == 0:
        return mpf(0)
    # Magnitude times direction (toward source)
    return G * m_source * m_target / r**2 * (dx / r)   # = sign(dx) * |F|

# Forces on E1
F_E1_from_P  = force_1D(x_P,  m_p, x_E1, m_e)
F_E1_from_E2 = force_1D(x_E2, m_e, x_E1, m_e)
F_E1_total   = F_E1_from_P + F_E1_from_E2

# Forces on E2
F_E2_from_P  = force_1D(x_P,  m_p, x_E2, m_e)
F_E2_from_E1 = force_1D(x_E1, m_e, x_E2, m_e)
F_E2_total   = F_E2_from_P + F_E2_from_E1

print("Forces on E1 (+x positive):")
print(f"  From proton: {mp.nstr(F_E1_from_P, 8)} N  (expect toward P, -x)")
print(f"  From E2:     {mp.nstr(F_E1_from_E2, 8)} N  (expect toward E2, +x)")
print(f"  Net E1:      {mp.nstr(F_E1_total, 8)} N\n")
print("Forces on E2:")
print(f"  From proton: {mp.nstr(F_E2_from_P, 8)} N")
print(f"  From E1:     {mp.nstr(F_E2_from_E1, 8)} N")
print(f"  Net E2:      {mp.nstr(F_E2_total, 8)} N\n")

a_E1 = F_E1_total / m_e
a_E2 = F_E2_total / m_e
ddot_r = a_E2 - a_E1

print(f"a_E1 = {mp.nstr(a_E1, 8)} m/s^2")
print(f"a_E2 = {mp.nstr(a_E2, 8)} m/s^2")
print(f"ddot(r) = a_E2 - a_E1 = {mp.nstr(ddot_r, 8)} m/s^2")
print(f"  sign: {'POSITIVE (apparent repulsion)' if ddot_r > 0 else 'NEGATIVE (apparent attraction)'}")

mu = m_e / 2
F_eff = mu * ddot_r
print(f"\nEffective repulsive force: F_eff = mu * ddot(r) = {mp.nstr(F_eff, 8)} N")

# Compare to Coulomb at r = a_0
F_Coulomb = k_C * e_elem**2 / a_0**2
print(f"Coulomb reference (two e at r=a_0): {mp.nstr(F_Coulomb, 8)} N")
ratio = F_eff / F_Coulomb
print(f"Ratio F_eff / F_Coulomb = {mp.nstr(ratio, 8)}  (expect ~1.65e-40)")
print(f"So competing attraction is {mp.nstr(F_Coulomb / abs(F_eff), 6)} times WEAKER than Coulomb.")

# Cross-check against inputs.json reference values
print("\n--- Comparison to reference values (from Session C derivation.md) ---")
ref = inp["reference_values"]
def compare(label, got, expected_key, tol_rel=1e-4):
    exp = mpf(inp["reference_values"][expected_key]["value"])
    rel = abs((got - exp) / exp) if exp != 0 else abs(got)
    ok = rel < tol_rel
    print(f"  {label}: computed={mp.nstr(got, 8)}, expected={exp}, rel_err={mp.nstr(rel, 4)} {'PASS' if ok else 'FAIL'}")
    return ok

passes = []
passes.append(compare("F_E1 from proton", F_E1_from_P, "F_E1_from_proton_expected"))
passes.append(compare("F_E1 from E2",      F_E1_from_E2, "F_E1_from_E2_expected"))
passes.append(compare("a_E1",              a_E1, "a_E1_expected"))
passes.append(compare("a_E2",              a_E2, "a_E2_expected"))
passes.append(compare("ddot(r)",           ddot_r, "ddot_r_expected"))
passes.append(compare("F_effective",       F_eff, "F_effective_expected"))
passes.append(compare("F_Coulomb",         F_Coulomb, "F_Coulomb_at_a0"))
passes.append(compare("ratio",             ratio, "ratio_F_competing_Coulomb"))

# Most important: the sign must be positive
assert ddot_r > 0, f"FAIL: ddot_r is not positive (got {ddot_r})"
print(f"\nSign check: ddot(r) > 0 ✓ (apparent repulsion confirmed)")

if all(passes):
    print("\n# Status: PASS — all numerical values match Session C reference to <1e-4 rel. err.")
else:
    print(f"\n# Status: PARTIAL — {sum(passes)}/{len(passes)} values match; investigate mismatches.")
