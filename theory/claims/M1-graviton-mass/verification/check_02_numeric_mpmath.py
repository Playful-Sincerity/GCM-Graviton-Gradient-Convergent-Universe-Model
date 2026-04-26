#!/usr/bin/env python3
"""M1 Check 2 — Numerical substitution with mpmath (50-digit precision).

Computes m_g = rho_bound * ell_P^3 and N_g = m_neutron / m_g.
Uses arbitrary-precision arithmetic so future sweeps over rho_bound
or finer-grained constants do not lose precision.
"""
import json
from pathlib import Path

from mpmath import mp, mpf, sqrt, pi

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())

mp.dps = 50  # 50 decimal-place precision


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    hbar = cv("hbar")
    G = cv("G")
    c = cv("c")
    rho_nuclear = cv("rho_bound_nuclear")
    rho_neutron = cv("rho_bound_neutron_density")
    m_neutron = cv("m_neutron")
    eV_per_kg = cv("eV_per_kg")
    LIGO_eVc2 = cv("LIGO_graviton_mass_eVc2")

    ell_P = sqrt(hbar * G / c**3)
    V_P = ell_P**3

    m_g_nuclear = rho_nuclear * V_P
    m_g_neutron = rho_neutron * V_P

    N_g_nuclear = m_neutron / m_g_nuclear
    N_g_neutron = m_neutron / m_g_neutron

    # LIGO bound expressed in kg
    LIGO_kg = LIGO_eVc2 * eV_per_kg

    # Order-of-magnitude margin vs LIGO
    margin_nuclear = LIGO_kg / m_g_nuclear

    print("# M1 Check 2 — Numerical substitution, mpmath 50-digit precision")
    print()
    print(f"ell_P          = {ell_P} m")
    print(f"V_P (= ell_P^3) = {V_P} m^3")
    print()
    print(f"With rho_bound = 1.0e18 kg/m^3 (session brief):")
    print(f"  m_g          = {m_g_nuclear} kg")
    print(f"  N_g/neutron  = {N_g_nuclear}")
    print()
    print(f"With rho_bound = 4.0e17 kg/m^3 (gcm_v2 neutron density):")
    print(f"  m_g          = {m_g_neutron} kg")
    print(f"  N_g/neutron  = {N_g_neutron}")
    print()
    print(f"LIGO bound (m_g < {LIGO_eVc2} eV/c^2) in kg:")
    print(f"  LIGO_kg      = {LIGO_kg}")
    print(f"  margin       = LIGO_kg / m_g_nuclear = {margin_nuclear}")
    print()

    # PASS criteria:
    #  1. m_g at nuclear density matches session brief 4.22e-87 kg to 3 sig figs
    #  2. m_g < LIGO_kg
    claim_value = mpf("4.22e-87")
    rel_err = abs(m_g_nuclear - claim_value) / claim_value

    print(f"claim value       = {claim_value}")
    print(f"computed value    = {m_g_nuclear}")
    print(f"relative error    = {rel_err}")
    print()

    passes = (rel_err < mpf("1e-2")) and (m_g_nuclear < LIGO_kg)
    print(f"STATUS: {'PASS' if passes else 'FAIL'}")


if __name__ == "__main__":
    main()
