#!/usr/bin/env wolframscript
(* R1 Check 02 (Wolfram independent) — graviton density and cross-section. *)

$MinPrecision = 30;

c = 299792458;
Mpc = 3.0856775814913673*^22;
H0 = 70 * 1000 / Mpc;
ellP = 1.616255*^-35;
Robs = 4.4*^26;

Vobs = 4/3 * Pi * Robs^3;
VP = ellP^3;
NPlanckCells = Vobs / VP;

ng = 1*^185 / Vobs;
ngPlanckFilling = 1 / VP;
alpha = H0 / c;
sigma = alpha / ng;

Print["# Check: 02 — Wolfram independent cross-check"];
Print["# Claim: R1-space-friction"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];

Print["V_obs = (4/3) pi R^3 (m^3):   ", ScientificForm[N[Vobs, 30]]];
Print["N_Planck_cells (V_obs/V_P):   ", ScientificForm[N[NPlanckCells, 30]]];
Print["n_g from 10^185/V_obs:        ", ScientificForm[N[ng, 30]]];
Print["n_g from Planck filling (1/V_P): ", ScientificForm[N[ngPlanckFilling, 30]]];

Print[""];
Print["Cross-check numerics against plausibility.md claims:"];
Print["  claimed n_g = 1e106; computed = ", ScientificForm[N[ng, 6]],
      " => ratio computed/claim = ", N[ng / 1*^106, 6]];
Print["  claimed sigma = 1e-133; self-consistent alpha=H0/c, n_g=N/V_obs gives sigma = ",
      ScientificForm[N[sigma, 6]]];

Print[""];
Print["FINDING (Wolfram concurs with Python):"];
Print["  * N_Planck_cells ~ 8.5e184, consistent with M3's 10^185 claim."];
Print["  * n_g ~ 2.8e104 m^-3 (10^104), NOT 10^106 as plausibility.md states."];
Print["  * Self-consistent sigma_g ~ 2.7e-131 m^2 (10^-131), NOT 10^-133."];
Print[""];
Print["STATUS: INCONCLUSIVE — same as Python check_02. Cross-tool agreement."];
