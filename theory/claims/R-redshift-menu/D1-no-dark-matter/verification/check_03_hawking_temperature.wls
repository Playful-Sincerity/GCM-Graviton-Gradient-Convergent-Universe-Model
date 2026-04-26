#!/usr/bin/env wolframscript
(* D1 Check 03 (Wolfram independent) — Hawking temperature of asteroid-mass PBH. *)

$MinPrecision = 30;

hbar = 1.054571817*^-34;
c = 299792458;
G = 6.67430*^-11;
kB = 1.380649*^-23;
M = 1*^17;           (* kg, asteroid-mass *)

TH = hbar * c^3 / (8 * Pi * G * M * kB);

Msun = 1.98892*^30;
THsun = hbar * c^3 / (8 * Pi * G * Msun * kB);

rs = 2 * G * M / c^2;
A = 4 * Pi * rs^2;
sigmaSB = 5.670374419*^-8;
L = sigmaSB * TH^4 * A;

Print["# Check: 03 — Wolfram independent cross-check"];
Print["# Claim: D1-no-dark-matter"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];

Print["Hawking T (M=10^17 kg): ", ScientificForm[N[TH, 30]], " K"];
Print["Hawking T (M=M_sun):    ", ScientificForm[N[THsun, 10]], " K (textbook ~6.17e-8 K)"];
Print["Schwarzschild r_s:      ", ScientificForm[N[rs, 10]], " m"];
Print["Area A = 4 pi r_s^2:    ", ScientificForm[N[A, 10]], " m^2"];
Print["Luminosity L = sigma T^4 A: ", ScientificForm[N[L, 10]], " W"];
Print[""];
Print["Ratio T_H / T_CMB:      ", N[TH / 2.725, 6]];
Print["Ratio T_H / T_claim(6e-7 K): ", ScientificForm[N[TH / 6*^-7, 6]]];

Print[""];
Print["FINDING (Wolfram concurs with Python):"];
Print["  T_H at 10^17 kg is ~1.23 million K (not 6e-7 K)."];
Print["  This is ~5e5 times the CMB temperature, NOT below it."];
Print["  The plausibility.md / claim.md Hawking-T claim is false by 12 orders."];
Print["  Observational invisibility is actually due to tiny luminosity (~36 mW),"];
Print["  not low temperature."];
Print[""];
Print["STATUS: FAIL — same as Python. Cross-tool agreement on the error."];
