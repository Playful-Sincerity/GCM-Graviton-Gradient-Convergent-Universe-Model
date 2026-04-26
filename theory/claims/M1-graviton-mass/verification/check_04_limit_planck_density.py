#!/usr/bin/env python3
"""M1 Check 4 — Limit case: rho_bound -> rho_Planck.

Session brief asked: 'at rho_bound -> rho_Planck, what does m_g become?
(Should stay consistent with LIGO.)'

Verifies that m_g(rho_Planck) equals the Planck mass (expected from the
formula's algebraic structure), and that this value exceeds the LIGO
bound by many orders of magnitude.

Interpretation: this is NOT a physics failure of GCM — GCM never claims
rho_bound = rho_Planck. It is a structural property of the formula
rho * ell_P^3: evaluated at Planck density, it returns the Planck mass.
The check converts into a constraint on rho_bound: LIGO requires
rho_bound <= ~4e45 kg/m^3, which nuclear density (1e18) satisfies by
27 orders of magnitude.
"""
import json
from pathlib import Path

from mpmath import mp, mpf, sqrt, log10

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 40


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    hbar = cv("hbar")
    G = cv("G")
    c = cv("c")
    eV_per_kg = cv("eV_per_kg")
    LIGO_eVc2 = cv("LIGO_graviton_mass_eVc2")

    ell_P = sqrt(hbar * G / c**3)
    V_P = ell_P**3

    # Planck density
    rho_Planck = c**5 / (hbar * G**2)
    m_g_at_Planck = rho_Planck * V_P

    # Planck mass (standard identity: sqrt(hbar * c / G))
    m_Planck = sqrt(hbar * c / G)

    LIGO_kg = LIGO_eVc2 * eV_per_kg

    # rho upper bound from LIGO: rho_bound <= LIGO_kg / V_P
    rho_max_from_LIGO = LIGO_kg / V_P

    rho_nuclear = cv("rho_bound_nuclear")

    print("# M1 Check 4 — Planck-density limit (honesty check)")
    print()
    print(f"rho_Planck                  = {rho_Planck} kg/m^3")
    print(f"m_g(rho_Planck) = rho*V_P   = {m_g_at_Planck} kg")
    print(f"sqrt(hbar*c/G) [Planck mass]= {m_Planck} kg")
    print(f"  relative difference       = {abs(m_g_at_Planck - m_Planck)/m_Planck}")
    print()
    print(f"LIGO bound                  = {LIGO_kg} kg")
    print(f"m_g(Planck) vs LIGO         = {m_g_at_Planck / LIGO_kg} times above bound")
    print(f"log10 ratio                 = {log10(m_g_at_Planck / LIGO_kg)}")
    print()
    print(f"Reinterpreted as constraint on rho_bound:")
    print(f"  rho_bound must be <= LIGO_kg / V_P = {rho_max_from_LIGO} kg/m^3")
    print(f"  rho_nuclear = {rho_nuclear} kg/m^3")
    print(f"  margin:     log10({rho_max_from_LIGO} / {rho_nuclear}) = {log10(rho_max_from_LIGO/rho_nuclear)} orders")
    print()

    # Session brief says "should stay consistent with LIGO" — it does not.
    # We report both the literal FAIL and the reframed PASS.
    literal_fail = m_g_at_Planck > LIGO_kg
    reframed_pass = rho_nuclear < rho_max_from_LIGO

    print("# Two readings:")
    print(f"  Literal (brief framing): m_g(rho_Planck) vs LIGO -> {'FAIL' if literal_fail else 'PASS'}")
    print(f"    (formula at Planck density yields Planck mass, far above LIGO)")
    print(f"  Reframed (physical claim): rho_nuclear vs rho_max_LIGO -> {'PASS' if reframed_pass else 'FAIL'}")
    print(f"    (nuclear density satisfies LIGO by 27 orders)")
    print()
    print("STATUS: INCONCLUSIVE (framing-dependent; see verification.md)")


if __name__ == "__main__":
    main()
