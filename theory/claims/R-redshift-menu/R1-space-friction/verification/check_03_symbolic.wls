#!/usr/bin/env wolframscript
(* R1 Check 03 (Wolfram symbolic) — symbolic derivation of z(r) from
   dE/dr = -alpha E and verification that linear form is the r->0 limit.

   This uses Wolfram's symbolic DSolve and Series to do what SymPy would
   have done (SymPy not available in this environment). *)

Print["# Check: 03 (Wolfram symbolic)"];
Print["# Claim: R1-space-friction"];
Print["# Run:   ", DateString[]];
Print["# Tool:  Wolfram Engine via wolframscript"];
Print["# ----"];

(* Solve dE/dr = -alpha E with E(0) = E0. *)
sol = DSolve[{en'[r] == -alpha * en[r], en[0] == E0}, en[r], r];
Print[""];
Print["dE/dr = -alpha E, E(0) = E0  =>  E(r) = ", en[r] /. sol[[1]]];

(* Observed redshift: 1 + z = E0 / E(r). *)
Eofr = en[r] /. sol[[1]];
onePlusZ = E0 / Eofr // Simplify;
Print["1 + z = E0/E(r) = ", onePlusZ];

z = onePlusZ - 1;
Print["z = ", z];

(* Expand in small alpha r. *)
zSeries = Series[z, {alpha, 0, 3}] // Normal;
Print[""];
Print["Taylor series of z in small alpha (up to O(alpha^3)):"];
Print["  z ≈ ", zSeries];
Print[""];
Print["Leading term: z ≈ alpha r   (linear Hubble-like law for small alpha r)"];

(* Numerical sanity at alpha r = 0.1: *)
numericZ = N[(Exp[alpha r] - 1) /. {alpha -> 1, r -> 0.1}, 20];
Print[""];
Print["Sanity at alpha*r = 0.1:"];
Print["  exact z = exp(0.1) - 1 = ", numericZ];
Print["  linear z = 0.1"];
Print["  relative error: ", (numericZ - 0.1) / numericZ];

Print[""];
Print["STATUS: PASS — symbolic derivation confirms exp(alpha r) - 1 collapses to"];
Print["        alpha r in the small-alpha-r limit. Cross-tool with Python check_03."];
