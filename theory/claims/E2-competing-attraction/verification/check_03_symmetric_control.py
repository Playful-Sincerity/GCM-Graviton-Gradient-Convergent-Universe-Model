"""
Check 03 — Symmetric-config control (Config B)
Claim: E2-competing-attraction

Geometry: proton at origin, E1 at -a_0, E2 at +a_0 (proton BETWEEN electrons).
Expected: by symmetry, each electron accelerates toward origin (toward the
other electron), so apparent ATTRACTION not repulsion. This confirms that
competing attraction's sign is geometry-dependent, not a universal property.
"""
import json
import sys
from pathlib import Path
from mpmath import mp, mpf

print("# Check 03 — Symmetric-config control (apparent attraction expected)")
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

# Symmetric geometry
x_P  = mpf(0)
x_E1 = -a_0
x_E2 = +a_0

def force_1D(x_source, m_source, x_target, m_target):
    dx = x_source - x_target
    r = abs(dx)
    if r == 0:
        return mpf(0)
    return G * m_source * m_target / r**2 * (dx / r)

F_E1 = force_1D(x_P, m_p, x_E1, m_e) + force_1D(x_E2, m_e, x_E1, m_e)
F_E2 = force_1D(x_P, m_p, x_E2, m_e) + force_1D(x_E1, m_e, x_E2, m_e)

a_E1 = F_E1 / m_e
a_E2 = F_E2 / m_e
ddot_r = a_E2 - a_E1

print(f"E1 at x = {mp.nstr(x_E1, 6)} m, E2 at x = {mp.nstr(x_E2, 6)} m")
print(f"a_E1 = {mp.nstr(a_E1, 8)} m/s^2  (expect POSITIVE, toward origin in +x)")
print(f"a_E2 = {mp.nstr(a_E2, 8)} m/s^2  (expect NEGATIVE, toward origin in -x)")
print(f"ddot(r) = {mp.nstr(ddot_r, 8)} m/s^2")
print(f"  sign: {'POSITIVE (repulsion)' if ddot_r > 0 else 'NEGATIVE (apparent ATTRACTION)'}")

# Sanity: with perfect symmetry, |a_E1| == |a_E2|
# With floating-point: a_E1 > 0, a_E2 < 0, ddot_r = a_E2 - a_E1 < 0 (attraction)
assert ddot_r < 0, f"FAIL: symmetric config should give attraction, got ddot_r = {ddot_r}"
assert abs(a_E1 + a_E2) < mpf('1e-25'), "Symmetric config should give equal/opposite accelerations"

print("\nGeometry dependence confirmed: symmetric proton-between-electrons gives apparent ATTRACTION.")
print("Together with Check 02 (asymmetric → apparent repulsion), E2's sign is shown to be geometry-dependent.")

# Also check isotropy/Gauss theorem intuition:
# For a HYPOTHETICAL spherically symmetric background around both electrons, the net force
# from the background on each electron is zero by Gauss's theorem. Here we aren't simulating
# that — we're showing the non-isotropy with a single offset heavy mass.

print("\n# Status: PASS — symmetric control yields opposite sign, confirming geometry-dependence.")
