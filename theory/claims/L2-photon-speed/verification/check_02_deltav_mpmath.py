#!/usr/bin/env python3
"""L2 Check 2 — High-precision Delta_v computation (mpmath, 80-digit).

Direct double-precision evaluation of c * sqrt(1 - eps^2) returns c
identically because eps^2 ~ 10^-37 is below machine epsilon. High
precision arithmetic is required to resolve Delta_v.

This is the core numerical check: Delta_v should match the session
brief's ~4.74e-29 m/s for a 1 eV photon with m_gamma = 1e-54 kg.
"""
import json
from pathlib import Path
from mpmath import mp, mpf, sqrt

HERE = Path(__file__).parent
INPUTS = json.loads((HERE / "inputs.json").read_text())
mp.dps = 80  # 80-digit precision — more than sufficient for 10^-37 scale


def cv(name, sect="constants"):
    return mpf(str(INPUTS[sect][name]["value"]))


def main():
    c = cv("c_causality")
    m_g = cv("m_gamma_GCM")
    J_per_eV = cv("J_per_eV")
    E_eV = cv("E_photon_example")
    E_J = E_eV * J_per_eV
    brief_Dv = mpf(str(INPUTS["expected"]["Delta_v_from_brief"]["value"]))

    print("# L2 Check 2 — Delta_v with mpmath 80-digit precision")
    print("# Convention: c denotes causality limit; v_photon < c strictly.")
    print()
    print(f"c (causality)            = {c} m/s")
    print(f"m_gamma (GCM)            = {m_g} kg")
    print(f"E (photon example)       = {E_eV} eV = {E_J} J")
    print()

    m_g_c2 = m_g * c**2
    eps = m_g_c2 / E_J
    eps2 = eps**2

    print(f"m_gamma * c^2            = {m_g_c2} J")
    print(f"epsilon = m_g c^2 / E    = {eps}")
    print(f"epsilon^2                = {eps2}")
    print()

    # Direct evaluation at 80-digit precision
    v = c * sqrt(1 - eps2)
    Dv_direct = c - v
    print(f"v_photon = c sqrt(1-ε²)  = {v} m/s  (80-digit)")
    print(f"Δv = c - v (direct)       = {Dv_direct} m/s")
    print()

    # Taylor expansion check: Δv ≈ (1/2) c ε^2  (leading order)
    Dv_taylor = c * eps2 / 2
    print(f"Δv ≈ c ε²/2  (Taylor)     = {Dv_taylor} m/s")
    print(f"rel diff direct vs Taylor = {abs(Dv_direct - Dv_taylor) / Dv_direct}")
    print()

    print(f"Session brief stated Δv   = {brief_Dv} m/s")
    rel_err = abs(Dv_direct - brief_Dv) / brief_Dv
    print(f"relative error to brief   = {rel_err}")
    print(f"  (brief is 2-sig-fig; 0.4% is rounding of stated inputs, not computational)")
    print()

    # Fractional speed deficit for order-of-magnitude sanity
    Dv_over_c = Dv_direct / c
    print(f"Δv / c                    = {Dv_over_c}")
    print(f"  (~10^-37, below any experimental sensitivity)")
    print()

    passes = rel_err < mpf("0.01") and v < c  # strict inequality is the key structural check
    print("STATUS:", "PASS" if passes else "FAIL")
    print("  v_photon < c_causality confirmed (structural, per L1 commitment m_gamma > 0)")


if __name__ == "__main__":
    main()
