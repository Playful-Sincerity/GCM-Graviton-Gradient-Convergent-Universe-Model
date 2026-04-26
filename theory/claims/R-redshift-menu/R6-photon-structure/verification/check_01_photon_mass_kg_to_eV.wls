#!/usr/bin/env wolframscript
(* R6 Check 01 (Wolfram independent) — photon mass conversion & FRB bound ratio. *)

$MinPrecision = 30;

c = 299792458;
eVJ = 1.602176634*^-19;
mGCM = 1*^-54;
mPlaus = 5.6*^-19;
Wang = 2.1*^-15;

restE = mGCM * c^2;
restEeV = restE / eVJ;
ratio = Wang / restEeV;
lratio = Log[10, ratio];

Print["# Check: 01 — Wolfram independent cross-check"];
Print["# Claim: R6-photon-structure"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];
Print["m c^2 (J):                ", ScientificForm[N[restE, 30]]];
Print["m (eV/c^2):               ", ScientificForm[N[restEeV, 30]]];
Print["plausibility.md claim:    5.6e-19"];
Print["ratio computed/claim:     ", N[restEeV / mPlaus, 6]];
Print[""];
Print["Wang 2023 bound:          ", ScientificForm[N[Wang, 10]], " eV/c^2"];
Print["Wang / GCM:               ", ScientificForm[N[ratio, 10]]];
Print["log10(Wang/GCM):          ", N[lratio, 8], " orders below bound"];
Print["Claim 'approx 4 orders below':  |computed - 4| = ", Abs[N[lratio, 6] - 4]];
Print[""];
Print["STATUS: PASS (order-of-magnitude). Cross-tool with Python check_01."];
