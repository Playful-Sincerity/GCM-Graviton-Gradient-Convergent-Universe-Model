#!/usr/bin/env python3
"""M3 Check 3 — Comparison to holographic (Bekenstein-Hawking) entropy.

The holographic entropy S ~ (R_H/ell_P)^2 scales as area, N_Planck as
volume. The ratio should be ~10^62 (since N scales as R^3, S as R^2,
and R_H/ell_P ~ 10^61).
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

    ell_P = sqrt(hbar * G / c**3)
    V_universe = mpf(4)/3 * pi * R_H**3
    V_P = ell_P**3
    N = V_universe / V_P

    # Bekenstein-Hawking area-entropy scale
    S_BH = (R_H / ell_P)**2

    ratio = N / S_BH

    print("# M3 Check 3 — Holographic entropy comparison")
    print()
    print(f"R_H / ell_P        = {R_H/ell_P}")
    print(f"  log10(ratio)     = {log10(R_H/ell_P)}")
    print()
    print(f"N_Planck (volume)  = {N}")
    print(f"S_BH (area-scale)  = {S_BH}")
    print()
    print(f"N / S_BH           = {ratio}")
    print(f"log10(N / S_BH)    = {log10(ratio)}")
    print()
    print("Interpretation: N is a bulk COUNT, S_BH is a surface-ENTROPY bound.")
    print("Dimensionally different quantities; the ratio ~10^62 is expected.")
    print("NOT a holographic violation — would become one only if GCM were")
    print("interpreted as a quantum-information theory with N independent bits.")
    print()

    passes = log10(ratio) > 55 and log10(ratio) < 70  # wide band for order-of-magnitude
    print("STATUS:", "PASS" if passes else "FAIL")


if __name__ == "__main__":
    main()
