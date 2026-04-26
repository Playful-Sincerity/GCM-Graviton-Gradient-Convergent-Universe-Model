#!/usr/bin/env python3
"""M3 Check 2 — Full-precision numerical computation (mpmath, 40-digit).

Uses the CODATA-derived Planck length (not the 4-sig-fig session-brief
value) for precision, and compares to the expected ~8.5e184 count.
"""
import json
from pathlib import Path
from mpmath import mp, mpf, pi, sqrt, log10

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 40


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    hbar = cv("hbar")
    G = cv("G")
    c = cv("c")
    R_H = cv("R_H")
    N_baryon = cv("N_baryon_observable")

    # Precise Planck length
    ell_P_precise = sqrt(hbar * G / c**3)
    # Session brief's 4-sig-fig value
    ell_P_short = cv("ell_P_shortform")

    V_universe = mpf(4)/3 * pi * R_H**3
    V_P_precise = ell_P_precise**3
    V_P_short = ell_P_short**3

    N_precise = V_universe / V_P_precise
    N_short = V_universe / V_P_short

    print("# M3 Check 2 — Numerical, mpmath 40-digit precision")
    print()
    print(f"R_H                   = {R_H} m")
    print()
    print(f"ell_P (CODATA precise) = {ell_P_precise} m")
    print(f"ell_P (brief 4-sig-fig)= {ell_P_short} m")
    print()
    print(f"V_universe            = {V_universe} m^3")
    print(f"V_P (precise)         = {V_P_precise} m^3")
    print()
    print(f"N (precise)           = {N_precise}")
    print(f"N (brief ell_P)       = {N_short}")
    print()
    print(f"log10(N_precise)      = {log10(N_precise)}")
    print(f"Expected: N ≈ 8.5e184 ≈ 10^185")
    print()

    # Comparison to baryon count
    ratio_precise = N_precise / N_baryon
    print(f"N_baryon              = {N_baryon}")
    print(f"N / N_baryon (precise)= {ratio_precise}")
    print(f"log10 ratio           = {log10(ratio_precise)}")
    print(f"Expected: ~10^105")
    print()

    # Check it matches expected ~8.5e184
    expected_N_magnitude = mpf("8.5e184")
    rel_err = abs(N_precise - expected_N_magnitude) / expected_N_magnitude
    print(f"relative difference to 8.5e184: {rel_err}")

    passes = rel_err < mpf("0.01") and log10(ratio_precise) > 100 and log10(ratio_precise) < 110
    print()
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
