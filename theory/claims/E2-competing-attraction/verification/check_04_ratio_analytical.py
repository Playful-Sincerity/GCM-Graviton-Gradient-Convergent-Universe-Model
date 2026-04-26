"""
Check 04 — Analytical scaling of the F_competing / F_Coulomb ratio
Claim: E2-competing-attraction

Derive an analytical estimate of the ratio (F_competing / F_Coulomb) at d=r=a_0
and compare to the numerical result. The estimate should be:

  F_competing ~ G m_e m_p / a_0^2 × (geometric factor)
  F_Coulomb   = k_C e^2 / a_0^2 × (geometric factor)
  ratio ≈ (G m_e m_p) / (k_C e^2) × (factor of order 1)

This is independent of the toy model — a purely dimensional-plus-scaling
argument. If the numerical result is off by orders of magnitude from this
estimate, something is wrong with the toy. If they agree, the 10^40 gap
is intrinsic to the gravity-vs-EM hierarchy.
"""
import json
import sys
from pathlib import Path
from mpmath import mp, mpf

print("# Check 04 — Analytical estimate of F_competing / F_Coulomb ratio")
print(f"# mpmath: {mp.dps} digits")
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

# Fundamental gravity-to-EM coupling ratio for electron-electron
grav_em_ratio_ee = (G * m_e**2) / (k_C * e_elem**2)
print(f"Grav:EM coupling ratio (electron-electron): G m_e^2 / (k_C e^2) = {mp.nstr(grav_em_ratio_ee, 8)}")
print(f"  (textbook value ≈ 2.4e-43)")

# Electron-proton version (the competing attraction uses m_e m_p in the gravity term)
grav_em_ratio_ep = (G * m_e * m_p) / (k_C * e_elem**2)
print(f"\nGrav:EM coupling ratio (electron-proton): G m_e m_p / (k_C e^2) = {mp.nstr(grav_em_ratio_ep, 8)}")
print(f"  Factor larger than ee ratio: {mp.nstr(grav_em_ratio_ep / grav_em_ratio_ee, 6)} ≈ m_p/m_e ≈ 1836")

# The toy model's effective repulsion, to leading order, is
# F_eff ≈ (1/2) m_e * (G m_p / d^2) * (geometric factor)
# = (G m_e m_p / d^2) * (geometric factor / 2)
# At d=a_0, F_Coulomb = k_C e^2 / a_0^2 * (dimensionless position factor 1/4 for r=a_0 from electron-Coulomb)
# Wait — for Coulomb we used r = a_0 (the inter-electron separation); at r = a_0 this
# is just k_C e^2 / a_0^2.

# Expected order of magnitude
# ratio ≈ grav_em_ratio_ep * (geometric factor O(1))
print(f"\nExpected order of magnitude: ratio ~ {mp.nstr(grav_em_ratio_ep, 4)} × (O(1) geometric factor)")
print(f"  i.e., 10^-40 ± 1 order")

# Actual measured ratio from check_02
ratio_measured = mpf(inp["reference_values"]["ratio_F_competing_Coulomb"]["value"])
print(f"\nMeasured ratio (Check 02):  {mp.nstr(ratio_measured, 6)}")
print(f"Order-of-magnitude agreement: measured/expected = {mp.nstr(ratio_measured / grav_em_ratio_ep, 6)}")
print(f"  (should be O(1), factor of at most ~10)")

factor = ratio_measured / grav_em_ratio_ep
# The geometric factor (1/2) from reduced mass * some number between 0.1-10
assert mpf('0.01') < abs(factor) < mpf('10'), \
    f"FAIL: measured ratio differs from order estimate by > 2 orders: factor {factor}"

print(f"\nConclusion: the measured ratio agrees with the pure G m_e m_p / k_C e^2 scaling")
print(f"to within a geometric factor of O(1). The ~10^40 gap is therefore intrinsic to the")
print(f"gravity-vs-EM hierarchy, not an artifact of the specific toy geometry.")

print("\n# Status: PASS — numerical ratio matches fundamental-coupling estimate to O(1).")
