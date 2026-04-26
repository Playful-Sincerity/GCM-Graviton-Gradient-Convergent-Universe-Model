"""
Check 03 — Numerical evaluation of C(R) and comparison to 1/R^6 (mpmath)
Claim: E3-vdw-universal

Reproduces Session C derivation.md §Numerical comparison table, at 50-digit
precision. The key finding is that C(R) decays EXPONENTIALLY at large R,
while 1/R^6 decays only polynomially — the naive reading (gradient overlap
reproduces VdW) fails.
"""
import json
import sys
from pathlib import Path
import mpmath as mp

print("# Check 03 — Numerical C(R) vs 1/R^6 (mpmath at 50 dps)")
print(f"# mpmath: {mp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

mp.mp.dps = 50

HERE = Path(__file__).parent
with open(HERE / "inputs.json") as f:
    inp = json.load(f)

m = mp.mpf(inp["natural_units"]["m"]["value"])
sigma = mp.mpf(inp["natural_units"]["sigma"]["value"])

def C(R):
    """Gradient-gradient correlation of two identical Gaussian mass distributions."""
    R = mp.mpf(R)
    factor = (6 * sigma**2 - R**2) * mp.exp(-R**2 / (4 * sigma**2))
    return m**2 * factor / (32 * mp.pi**mp.mpf('1.5') * sigma**7)

print(f"{'R/sigma':>10}  {'C(R)':>25}  {'1/R^6':>25}  {'C/(1/R^6)':>25}")
print("-" * 95)

for R_val in inp["r_over_sigma_sweep"]["value"]:
    R = mp.mpf(R_val)
    c_val = C(R)
    vdw = 1 / R**6
    ratio = c_val / vdw
    print(f"{R_val:>10}  {mp.nstr(c_val, 15):>25}  {mp.nstr(vdw, 15):>25}  {mp.nstr(ratio, 15):>25}")

# Assertions
# At R = 1 sigma: Session C recorded C = 2.185353e-02; we reproduce.
C1 = C(1)
expected_1 = mp.mpf(inp["reference_values"]["C_at_R_1.0"]["value"])
rel1 = abs((C1 - expected_1) / expected_1)
print(f"\nC(R=sigma) = {mp.nstr(C1, 10)}  expected = {expected_1}  rel_err = {mp.nstr(rel1, 6)}")
assert rel1 < mp.mpf('1e-6'), f"Mismatch at R=1: {rel1}"

# Zero crossing: C(sqrt(6) sigma) == 0
C_zc = C(mp.sqrt(6))
print(f"C(R = sigma sqrt(6)) = {mp.nstr(C_zc, 15)}  (expect: 0)")
assert abs(C_zc) < mp.mpf('1e-40'), f"Zero crossing failed: {C_zc}"

# Sign changes across the zero crossing:
# R = 2 (below zc): C > 0
# R = 5 (above zc): C < 0
C2 = C(2)
C5 = C(5)
print(f"\nSign check:  C(R=2)={mp.nstr(C2, 6)} (>0)  C(R=5)={mp.nstr(C5, 6)} (<0)")
assert C2 > 0, f"C(2) should be positive: {C2}"
assert C5 < 0, f"C(5) should be negative: {C5}"

# Crucial claim: at large R, ratio |C(R)|/(1/R^6) -> 0 exponentially
R_far = mp.mpf(20)
C_far = C(R_far)
vdw_far = 1 / R_far**6
ratio_far = C_far / vdw_far
print(f"\nAt R = 20 sigma:  C(R) = {mp.nstr(C_far, 15)}")
print(f"                  1/R^6 = {mp.nstr(vdw_far, 15)}")
print(f"                  ratio = {mp.nstr(ratio_far, 15)}  (should be tiny)")
assert abs(ratio_far) < mp.mpf('1e-30'), f"At R=20 sigma, ratio should be << 1/R^6; got {ratio_far}"

print("\n# Status: PASS — C(R) closed form, zero crossing, and exponential (not power-law) asymptotic all confirmed.")
