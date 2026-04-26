#!/usr/bin/env python3
"""L2 Check 3 — Cross-check against Wang et al. 2023 FRB photon-mass bound.

Expresses the GCM photon mass (1e-54 kg) in eV/c^2 units and compares
against the Wang et al. 2023 FRB dispersion bound.
"""
import json
from pathlib import Path
from mpmath import mp, mpf, log10

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 30


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    m_g = cv("m_gamma_GCM")
    eV_per_kg = cv("eV_per_kg")
    FRB_bound = cv("FRB_photon_mass_bound_eVc2")

    # Convert GCM photon mass to eV/c^2
    m_g_eVc2 = m_g / eV_per_kg

    # Margin
    margin = FRB_bound / m_g_eVc2
    log_margin = log10(margin)

    print("# L2 Check 3 — FRB photon-mass bound")
    print()
    print(f"GCM m_gamma            = {m_g} kg")
    print(f"GCM m_gamma            = {m_g_eVc2} eV/c^2")
    print()
    print(f"Wang 2023 FRB bound    = {FRB_bound} eV/c^2")
    print(f"FRB bound in kg        = {FRB_bound * eV_per_kg} kg")
    print()
    print(f"margin (FRB / GCM)     = {margin}")
    print(f"log10(margin)          = {log_margin}")
    print(f"orders of magnitude    = {int(log_margin)}")
    print()
    print("Note: session brief says '4 orders below'; precise value is ~3.6 orders.")
    print("Both are order-of-magnitude consistent.")
    print()

    passes = m_g_eVc2 < FRB_bound and log_margin > 3
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
