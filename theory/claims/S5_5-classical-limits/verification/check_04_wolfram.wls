(* S5.5(a) — Check 04: Wolfram Engine cross-verification                *)
(* Claim: S5_5-classical-limits (sub-claim a — Newtonian limit)          *)
(* Independent numerical + symbolic computation via Wolfram Language.    *)
(* Constants intentionally hardcoded to match inputs.json — if inputs.json *)
(* is updated, this file must be updated in tandem.                      *)

(* Inputs — from ../inputs.json *)
Gn  = 6.6743*^-11;          (* G, m^3 / (kg s^2), CODATA 2018          *)
ME  = 5.9722*^24;           (* Earth mass, kg                          *)
MM  = 7.342*^22;            (* Moon mass, kg                           *)
rEM = 3.844*^8;             (* Earth-Moon mean distance, m             *)
Fref = 1.98*^20;            (* Textbook reference value, N             *)

(* --- Numerical force --- *)
F = Gn * ME * MM / rEM^2;
Print["F (numerical) = ", ScientificForm[F, 6], " N"];
Print["F reference   = ", ScientificForm[Fref, 6], " N"];
Print["Relative error: ", 100 * Abs[F - Fref] / Fref, " %"];

(* --- Symbolic limit checks --- *)
Clear[m1, m2, r, mg, xA, xB, Gs];
Fsym = Gs*m1*m2/r^2;

Print[""];
Print["Symbolic limits:"];
Print["  Limit[F, r -> Infinity] = ", Limit[Fsym, r -> Infinity]];
Print["  Limit[F, m1 -> 0]       = ", Limit[Fsym, m1 -> 0]];
Print["  Limit[F, m2 -> 0]       = ", Limit[Fsym, m2 -> 0]];

(* Factorization: substitute m1 = mg*xA, m2 = mg*xB *)
Fcomp = Fsym /. {m1 -> mg*xA, m2 -> mg*xB};
Print["  With m1=mg*xA, m2=mg*xB: ", Simplify[Fcomp]];
Print["  Single-graviton (xA=xB=1): ", Simplify[Fcomp /. {xA -> 1, xB -> 1}]];

(* --- Tolerance check --- *)
passed = (100 * Abs[F - Fref] / Fref) < 1.0;
Print[""];
Print["Status: ", If[passed, "PASS", "FAIL"]];
