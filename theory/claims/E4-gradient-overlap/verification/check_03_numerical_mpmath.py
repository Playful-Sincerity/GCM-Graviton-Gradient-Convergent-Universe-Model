"""
Check 03 — Numerical sweep of F(R)/F_point ratio at high precision (mpmath)
Claim: E4-gradient-overlap

Re-runs the numerical comparison from derivation.md §Step 5 (the table
showing overlap force weaker than 1/R^2 by many orders of magnitude at R<<sigma),
now at 50-digit mpmath precision to eliminate any double-precision artifact.

Expected behavior:
  R/sigma = 0.01   ratio ~ 1e-7
  R/sigma = 1.0    ratio ~ 8.1e-2
  R/sigma = 10.0   ratio -> 1.0  (point-mass recovery)
"""
import json
import sys
from pathlib import Path
import mpmath as mp

print("# Check 03 — High-precision numerical F(R)/F_point sweep (mpmath)")
print(f"# mpmath: {mp.__version__}")
print(f"# Python: {sys.version.split()[0]}")
print("# ---")

mp.mp.dps = 50  # 50-digit precision

HERE = Path(__file__).parent
with open(HERE / "inputs.json") as f:
    inputs = json.load(f)

# Natural units: G=m=sigma=1
G     = mp.mpf(inputs["natural_units"]["G"]["value"])
m     = mp.mpf(inputs["natural_units"]["m"]["value"])
sigma = mp.mpf(inputs["natural_units"]["sigma"]["value"])

sweep = inputs["r_over_sigma_sweep"]["value"]

def F_overlap(R):
    """Force magnitude between two identical Gaussian mass distributions."""
    # F(R) = G m^2 / R^2 * erf(R/(2 sigma)) - G m^2 / (R sigma sqrt(pi)) * exp(-R^2/(4 sigma^2))
    term1 = G * m**2 / R**2 * mp.erf(R / (2 * sigma))
    term2 = G * m**2 / (R * sigma * mp.sqrt(mp.pi)) * mp.exp(-R**2 / (4 * sigma**2))
    return term1 - term2  # this is |F|; in the attractive direction

def F_point(R):
    return G * m**2 / R**2

print(f"{'R/sigma':>10}  {'F_overlap':>30}  {'F_point':>25}  {'ratio':>20}")
print("-" * 95)

for x in sweep:
    R = mp.mpf(x)
    F_ov = F_overlap(R)
    F_pt = F_point(R)
    ratio = F_ov / F_pt
    print(f"{str(x):>10}  {mp.nstr(F_ov, 15):>30}  {mp.nstr(F_pt, 15):>25}  {mp.nstr(ratio, 12):>20}")

# Assertions — compare with values in derivation.md
print()
# At R/sigma = 0.01 the ratio should be around 9.4e-8
R = mp.mpf('0.01')
ratio_small = F_overlap(R) / F_point(R)
print(f"ratio(R/sigma=0.01) = {mp.nstr(ratio_small, 6)}  (derivation.md reports ~9.40e-8)")
assert abs(ratio_small - mp.mpf('9.40e-8')) < mp.mpf('1e-9'), \
    f"Mismatch with derivation.md at small R: {ratio_small}"

# At R/sigma = 10 the ratio should approach 1, limited by the exp(-25) term
# Floor is exp(-25)/sqrt(pi) ~ 7.8e-12 after leading cancellation
R = mp.mpf('10')
ratio_large = F_overlap(R) / F_point(R)
print(f"ratio(R/sigma=10)   = {mp.nstr(ratio_large, 12)} (expect -> 1 to ~1e-10)")
assert abs(ratio_large - 1) < mp.mpf('1e-9'), \
    f"Point-mass recovery failed: {ratio_large}"

# At R/sigma = 20 the approach should be much closer
R = mp.mpf('20')
ratio_far = F_overlap(R) / F_point(R)
print(f"ratio(R/sigma=20)   = {mp.nstr(ratio_far, 20)} (expect: exponentially close to 1)")
assert abs(ratio_far - 1) < mp.mpf('1e-40'), \
    f"Far-field recovery should be exponential: {ratio_far}"

print("\n# Status: PASS — R<<sigma regularization (ratio ~1e-7) and R>>sigma recovery (ratio -> 1) confirmed at 50-digit precision.")
