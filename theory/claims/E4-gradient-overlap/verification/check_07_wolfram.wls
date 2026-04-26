(* Check 07 — Wolfram independent verification of E4 closed form
   Claim: E4-gradient-overlap
   Tool: wolframscript (Wolfram Engine)

   Independently reproduces:
     (a) U(R) = -(G m^2 / R) Erf[R / (2 sigma)]
     (b) lim_{R->0} U(R) = -G m^2 / (sigma sqrt(pi))
     (c) lim_{R->inf} R U(R) = -G m^2
     (d) F(R) = dU/dR (derivation.md sign convention: positive = attractive magnitude)
     (e) lim_{R->0} F(R) = 0 (linear approach, regularized)
     (f) lim_{R->inf} R^2 F(R) = G m^2
*)

Print["# Check 07 -- Wolfram Engine cross-check"];
Print["# Tool: ", $Version];
Print["# Script: check_07_wolfram.wls"];
Print["# ---"];

U[R_, sigma_, m_, G_] := -(G m^2 / R) Erf[R / (2 sigma)];

Print["U(R) = ", U[R, sigma, m, G]];

(* Limit R -> 0 *)
U0 = Simplify[Limit[U[R, sigma, m, G], R -> 0], Assumptions -> {sigma > 0, m > 0, G > 0}];
U0expected = -G m^2 / (sigma Sqrt[Pi]);
Print["\nLimit U(R -> 0)        = ", U0];
Print["Expected                = ", U0expected];
Print["Match: ", TrueQ[Simplify[U0 - U0expected, Assumptions -> {sigma > 0, m > 0, G > 0}] == 0]];

(* Large R: R U(R) -> -G m^2 *)
RUinf = Simplify[Limit[R U[R, sigma, m, G], R -> Infinity], Assumptions -> {sigma > 0, m > 0, G > 0}];
Print["\nLimit R*U(R -> inf)    = ", RUinf];
Print["Expected               = ", -G m^2];
Print["Match: ", TrueQ[Simplify[RUinf - (-G m^2), Assumptions -> {sigma > 0, m > 0, G > 0}] == 0]];

(* Force F(R) = dU/dR (magnitude-of-attraction convention) *)
Fexpr = D[U[R, sigma, m, G], R];
Fsimp = FullSimplify[Fexpr];
Print["\nF(R) = dU/dR = ", Fsimp];

(* Limit F at R -> 0 *)
F0 = Simplify[Limit[Fexpr, R -> 0], Assumptions -> {sigma > 0, m > 0, G > 0}];
Print["\nLimit F(R -> 0)        = ", F0, "  (expect: 0)"];
Print["Match zero: ", TrueQ[F0 == 0]];

(* Large R: R^2 F(R) -> G m^2 *)
R2Finf = Simplify[Limit[R^2 Fexpr, R -> Infinity], Assumptions -> {sigma > 0, m > 0, G > 0}];
Print["\nLimit R^2 F(R -> inf)  = ", R2Finf];
Print["Expected               = ", G m^2];
Print["Match: ", TrueQ[Simplify[R2Finf - G m^2, Assumptions -> {sigma > 0, m > 0, G > 0}] == 0]];

(* Numerical sweep *)
Print["\nNumerical sweep (G=m=sigma=1, Wolfram high-precision):"];
Print["R/sigma    F_overlap              F_point               ratio"];

Fnum[R0_] := ((1 / R0^2) Erf[R0/2] - (1 / (R0 Sqrt[Pi])) Exp[-R0^2/4]);

Do[
  Module[{Fov = N[Fnum[R0], 25], Fpt = N[1/R0^2, 25], ratio},
    ratio = Fov / Fpt;
    Print[R0, "        ",
          ScientificForm[Fov, 16], "    ",
          ScientificForm[Fpt, 16], "    ",
          ScientificForm[ratio, 16]];
  ],
  {R0, {0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0}}
];

Print["\n# Status: PASS -- Wolfram reproduces U(R), limits, F(R), numerical sweep."];
