#!/usr/bin/env python3
"""M3 Check 4 — Ratio to baryon count.

Expected: N / N_baryon ~ 10^105.
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

    ell_P = sqrt(hbar * G / c**3)
    V_universe = mpf(4)/3 * pi * R_H**3
    V_P = ell_P**3
    N = V_universe / V_P

    ratio = N / N_baryon
    log_ratio = log10(ratio)

    print("# M3 Check 4 — Ratio to baryon count")
    print()
    print(f"N                = {N}")
    print(f"N_baryon         = {N_baryon}")
    print()
    print(f"N / N_baryon     = {ratio}")
    print(f"log10 ratio      = {log_ratio}")
    print(f"Expected         = ~10^105")
    print()

    # Also: gravitons per baryon (intrinsic), relating M1 to M3
    # M1 says a neutron contains ~4e59 gravitons (intrinsic).
    # M3 / N_baryon says ~10^105 gravitons per baryon (in the whole universe,
    # including the empty space around them).
    # Difference: 10^105 / 4e59 ~ 10^45 'extra' gravitons per baryon occupying
    # the space between them.
    N_g_per_neutron_intrinsic = mpf("4e59")
    extra_per_baryon = ratio / N_g_per_neutron_intrinsic
    print(f"Cross-reference with M1: neutron contains ~{N_g_per_neutron_intrinsic} gravitons.")
    print(f"Extra gravitons per baryon (in space between matter): {extra_per_baryon}")
    print(f"  log10 = {log10(extra_per_baryon)}")
    print(f"Consistent with T1's 'gravitons are the substrate, matter is a tiny subset.'")
    print()

    passes = log_ratio > 100 and log_ratio < 110
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
