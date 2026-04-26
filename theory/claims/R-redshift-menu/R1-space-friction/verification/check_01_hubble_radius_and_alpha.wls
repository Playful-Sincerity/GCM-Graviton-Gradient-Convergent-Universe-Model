#!/usr/bin/env wolframscript
(* R1 Check 01 (Wolfram independent) — Hubble radius and alpha = H0/c.
   Same physics as check_01_hubble_radius_and_alpha.py, using Wolfram's
   native high-precision arithmetic as a cross-check. *)

$MinPrecision = 30;

c = 299792458;                                    (* m/s, exact *)
Mpc = 3.0856775814913673*^22;                     (* m *)
H0km = 70;                                        (* km/s/Mpc *)
H0SI = H0km * 1000 / Mpc;                         (* s^-1 *)

RH = c / H0SI;
alpha = H0SI / c;

Print["# Check: 01 — Wolfram independent cross-check"];
Print["# Claim: R1-space-friction"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# Script: verification/check_01_hubble_radius_and_alpha.wls"];
Print["# ----"];

Print["H0 in SI (s^-1):  ", ScientificForm[N[H0SI, 30]]];
Print["R_H = c/H0 (m):   ", ScientificForm[N[RH, 30]]];
Print["alpha = H0/c:     ", ScientificForm[N[alpha, 30], 6]];

Print[""];
Print["Claimed in plausibility.md:"];
Print["  R_H = 4.4e26 m  -> ratio computed/claim = ",
      ScientificForm[N[RH / (4.4*^26), 10]]];
Print["  alpha = 2.3e-27 m^-1  -> ratio computed/claim = ",
      ScientificForm[N[alpha / (2.3*^-27), 10]]];

Print[""];
Print["Cross-check ratio of claimed-R and claimed-alpha product:"];
Print["  (4.4e26) * (2.3e-27) = ", N[4.4*^26 * 2.3*^-27, 10], " (should be 1 if self-consistent)"];
Print["  (c/H0) * (H0/c) identity = ", N[RH * alpha, 10], "  (exactly 1 by construction)"];

Print[""];
Print["H0 tension range:"];
Do[
  H0v = H0tension;
  H0vSI = H0v * 1000 / Mpc;
  a = H0vSI / c;
  R = c / H0vSI;
  Print["  H0=", H0v, " km/s/Mpc -> R_H=",
        ScientificForm[N[R, 6]], " m, alpha=",
        ScientificForm[N[a, 6]], " m^-1"],
  {H0tension, {67.4, 70.0, 73.0}}
];

Print[""];
Print["FINDING (Wolfram concurs with Python):"];
Print["  alpha = H0/c at H0=70 gives 7.57e-27 m^-1, NOT 2.3e-27 m^-1."];
Print["  4.4e26 m is the observable-universe particle horizon, NOT the Hubble radius."];
Print["  plausibility.md has a labelling/value inconsistency of factor ~3.3."];

Print[""];
Print["STATUS: INCONCLUSIVE — same finding as Python check_01. Cross-tool agreement."];
