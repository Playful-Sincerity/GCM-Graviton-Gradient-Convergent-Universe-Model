#!/usr/bin/env python3
"""L2 Check 4 — Structural property: v_photon < c strictly for all m_gamma > 0.

Per the speed-of-causality principle, GCM commits to m_gamma > 0 (L1).
The L2 formula must therefore yield v < c strictly — NOT v -> c in a
limit GCM takes. This check confirms the structural inequality at a
range of photon energies and masses.

The m_gamma -> 0 limit is computed as an algebraic reference point
(the formula reduces to c in that limit) but is NOT a GCM regime:
GCM does not take m_gamma to zero.
"""
import json
from pathlib import Path
from mpmath import mp, mpf, sqrt, log10

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 60


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def v_over_c(m_g, E_J, c):
    """Returns v_photon / c_causality — strictly < 1 for m_g > 0."""
    eps = m_g * c**2 / E_J
    return sqrt(1 - eps**2)


def main():
    c = cv("c_causality")
    J_per_eV = cv("J_per_eV")

    print("# L2 Check 4 — Structural v < c property")
    print("# Per speed-of-causality-principle: GCM commits to m_gamma > 0 (L1),")
    print("# therefore v_photon < c strictly. This is NOT an approximation.")
    print()

    # Sweep over energies at fixed m_gamma = 1e-54 kg (GCM value)
    m_g = cv("m_gamma_GCM")
    print(f"Fixed m_gamma = {m_g} kg (GCM value):")
    print(f"{'E (eV)':>10}  {'v/c (deviation from 1)':>30}  {'0_x = 1 - v/c':>22}")
    for log_E in (-3, 0, 3, 6, 9):
        E_eV = mpf(10)**log_E
        E_J = E_eV * J_per_eV
        ratio = v_over_c(m_g, E_J, c)
        dev = 1 - ratio
        print(f"{str(E_eV)[:10]:>10}  v/c = 1 - {str(dev)[:20]:>20}  {str(dev)[:22]:>22}")
    print()
    print("Observation: higher E -> smaller 0_x (v closer to c, but never equal).")
    print("This is the IVNA indexed infinitesimal: 0_x varies with energy index x.")
    print()

    # The m_g -> 0 case is the formula's algebraic limit, NOT a GCM regime.
    print("Algebraic reference — the m_gamma -> 0 mathematical limit of the formula:")
    print("  (NOTE: GCM does NOT take this limit; L1 commits to m_gamma > 0.)")
    for log_m in (-54, -60, -70, -80, -90):
        m = mpf(10)**log_m
        E_J = mpf(1) * J_per_eV
        ratio = v_over_c(m, E_J, c)
        dev = 1 - ratio
        print(f"  m_gamma = 10^{log_m} kg  ->  v/c = 1 - {str(dev)[:22]:>22}")
    print()
    print("The formula reduces to v = c as m_gamma -> 0, confirming the SR limit")
    print("as an algebraic property. GCM rejects the m_gamma = 0 case as unphysical")
    print("(massless photon would have indistinguishable-from-causality speed, but")
    print("the composite-graviton structure requires nonzero rest mass).")
    print()

    # All values with m_g > 0 must give ratio strictly < 1
    passes = all(v_over_c(m_g, E_eV * J_per_eV, c) < 1 for E_eV in [mpf(10)**k for k in (-3, 0, 3, 6, 9)])
    print("STATUS:", "PASS" if passes else "FAIL")
    print("  v < c verified for m_gamma = 1e-54 kg across 12 orders of magnitude in energy.")


if __name__ == "__main__":
    main()
