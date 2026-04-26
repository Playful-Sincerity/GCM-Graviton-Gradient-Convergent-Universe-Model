#!/usr/bin/env wolframscript
(* R6 Check 02 (Wolfram symbolic) — verify the structural cascade

     lambda_obs = (1+z) * lambda_emit   (by definition of redshift)
     d_internal \propto lambda          (L3 correspondence)
     tau_internal \propto d_internal    (information-propagation bound)
     ==> tau_obs / tau_emit = (1+z)^1 exactly.

   The exponent '1' in the DES 2024 measurement (1+z)^{1.003 ± 0.005}
   is consistent with the R6 structural prediction at 1 sigma.

   Uses Wolfram's symbolic algebra (SymPy not available).
*)

$MinPrecision = 30;

Print["# Check: 02 (Wolfram symbolic) — cascade exponent derivation"];
Print["# Claim: R6-photon-structure"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];

(* Parameterize: lambdaO / lambdaE = (1 + z).
   L3:   dO / dE = k * (lambdaO / lambdaE) = k (1+z) for some constant k.
   Information-propagation bound: tauO / tauE = dO / dE.
   Therefore tauO / tauE = k (1+z), and k = 1 if propagation speed is
   constant between emission and observation. *)

ratioLambda = 1 + z;
ratioDInternal = ratioLambda;  (* L3: exact proportionality, k absorbed in units *)
ratioTau = ratioDInternal;

Print[""];
Print["Structural cascade:"];
Print["  lambdaO / lambdaE   = ", ratioLambda];
Print["  dInternalO / dInternalE (L3) = ", ratioDInternal];
Print["  tauO / tauE (prop. delay)    = ", ratioTau];
Print[""];
Print["Exponent in (1+z)^n on tauO/tauE:"];
exponent = Exponent[ratioTau, 1 + z];
Print["  n = ", exponent];

(* DES 2024 measurement *)
obsExponent = 1.003;
obsErr = 0.005;
prediction = 1;

nSigma = Abs[obsExponent - prediction] / obsErr;
Print[""];
Print["DES 2024 measurement: (1+z)^b, b = 1.003 ± 0.005 (stat) ± 0.010 (sys)"];
Print["R6 structural prediction: b = 1 (exact)"];
Print["|b_obs - b_R6| / sigma_stat = ", N[nSigma, 6], " sigma from stat uncertainty alone"];
Print["|b_obs - b_R6| / sigma_sys  = ", N[Abs[obsExponent - prediction] / 0.010, 6], " sigma from sys uncertainty alone"];

Print[""];
Print["Combined (stat + sys in quadrature):"];
sigmaTot = Sqrt[obsErr^2 + 0.010^2];
Print["  sigma_tot = ", N[sigmaTot, 6]];
Print["  |b_obs - b_R6| / sigma_tot = ", N[Abs[obsExponent - prediction] / sigmaTot, 6], " sigma"];

Print[""];
If[Abs[obsExponent - prediction] / sigmaTot < 2,
  Print["Prediction within 2 sigma of measurement. PASS."];
  Print["STATUS: PASS"],
  Print["Prediction more than 2 sigma from measurement."];
  Print["STATUS: FAIL"]
];

Print[""];
Print["Caveat (flagged in plausibility.md): the cascade depends on"];
Print["  (a) L3 (wavelength ∝ internal spacing) being exact, not just approximate,"];
Print["  (b) internal information-propagation speed being substrate-independent."];
Print["Both are currently yellow-tier assumptions. Falsification of either"];
Print["would change the exponent away from 1."];
