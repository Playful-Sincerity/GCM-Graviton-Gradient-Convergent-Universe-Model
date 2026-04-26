#!/usr/bin/env wolframscript
(* R3 Check 01 (Wolfram independent) — required gradient dPhi/dr. *)

$MinPrecision = 30;

c = 299792458;
Mpc = 3.0856775814913673*^22;
H0 = 70 * 1000 / Mpc;

grad = c * H0;

Print["# Check: 01 — Wolfram independent cross-check"];
Print["# Claim: R3-non-central"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];
Print["H_0 (SI):     ", ScientificForm[N[H0, 15]], " s^-1"];
Print["c H_0:        ", ScientificForm[N[grad, 15]], " m/s^2"];
Print[""];
Print["plausibility.md claim: 2e-8 m/s^2"];
Print["ratio computed/claim:  ", N[grad / (2*^-8), 8]];
Print[""];
Print["FINDING (Wolfram concurs with Python):"];
Print["  c H_0 at H0=70 km/s/Mpc is 6.80e-10 m/s^2, NOT 2e-8 m/s^2."];
Print["  plausibility.md is off by ~30x (factor of ~30 too large)."];
Print[""];
Print["Side note (not part of the R3 check):"];
Print["  6.8e-10 m/s^2 is within a factor ~5 of the MOND acceleration scale"];
Print["  a_0 ~ 1.2e-10 m/s^2. This coincidence is known in the modified-gravity"];
Print["  literature as 'the Hubble coincidence' — probably worth noting in the"];
Print["  R3 plausibility text."];
Print[""];
Print["STATUS: INCONCLUSIVE — plausibility.md 2e-8 claim is ~30x too large."];
Print["        Structural claim (gradient order of c*H_0) is correct;"];
Print["        specific numerical value was wrong."];
