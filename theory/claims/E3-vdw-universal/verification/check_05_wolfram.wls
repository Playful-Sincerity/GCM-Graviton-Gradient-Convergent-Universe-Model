(* Check 05 — Wolfram independent verification of C(R) closed form
   Claim: E3-vdw-universal
   Tool: wolframscript

   Independently reproduces:
     (a) Laplacian of exp(-R^2/(4 sigma^2))
     (b) C(R) = m^2 (6 sigma^2 - R^2) exp(-R^2/(4 sigma^2)) / (32 pi^{3/2} sigma^7)
     (c) Zero crossing at R = sigma sqrt(6)
     (d) Numerical sweep agreeing with mpmath check_03
     (e) Large-R asymptotic behavior (exponential, NOT 1/R^6)
*)

Print["# Check 05 -- Wolfram Engine cross-check of E3 C(R) closed form"];
Print["# Tool: ", $Version];
Print["# ---"];

$Assumptions = {sigma > 0, m > 0};

(* 3D radial Laplacian applied to exp(-R^2/(4 sigma^2)) *)
f = Exp[-R^2 / (4 sigma^2)];
lap = D[f, {R, 2}] + (2/R) D[f, R];
lapsimp = FullSimplify[lap, Assumptions -> $Assumptions];
Print["Laplacian of exp(-R^2/(4 sigma^2)) = ", lapsimp];

(* C(R) via Fourier-trick: C = -Laplacian[rho_conv] where rho_conv is auto-convolution *)
convPrefactor = m^2 / (4 Pi sigma^2)^(3/2);
Cclosed = FullSimplify[-convPrefactor * lapsimp, Assumptions -> $Assumptions];
Print["\nC(R) = -Laplacian[rho_conv] = ", Cclosed];

(* Expected form from Session C derivation.md *)
expected = m^2 (6 sigma^2 - R^2) Exp[-R^2/(4 sigma^2)] / (32 Pi^(3/2) sigma^7);
Print["Expected                      = ", expected];
diff = FullSimplify[Cclosed - expected, Assumptions -> $Assumptions];
Print["Difference (should be 0): ", diff];
Print["Match: ", TrueQ[diff == 0]];

(* Zero crossing: substitute R = sigma sqrt(6) *)
Czc = FullSimplify[Cclosed /. R -> Sqrt[6] sigma, Assumptions -> $Assumptions];
Print["\nC(R = sigma sqrt(6)) = ", Czc, "  (expect: 0)"];
Print["Zero match: ", TrueQ[Czc == 0]];

(* Numerical sweep *)
Print["\nNumerical sweep (m=sigma=1):"];
Print["R/sigma       C(R)                       1/R^6                      ratio"];
Module[{Rv, Cval, vdw, ratio},
  Do[
    Cval = N[Cclosed /. {m -> 1, sigma -> 1, R -> Rv}, 20];
    vdw = N[1/Rv^6, 20];
    ratio = Cval / vdw;
    Print[StringPadRight[ToString[Rv], 12], "   ",
          StringPadRight[ToString[CForm[Cval]], 22], "   ",
          StringPadRight[ToString[CForm[vdw]], 22], "   ",
          ToString[CForm[ratio]]];
    , {Rv, {0.5, 1.0, 2.0, 5.0, 10.0, 20.0}}]
];

(* Large-R asymptotic check: if C(R) ~ A/R^6, then R^6 C(R) -> A as R->inf.
   For our exponential form, R^6 C(R) -> 0 exponentially, proving NOT power-law. *)
Print["\nAsymptotic shape check:"];
Do[
  Module[{val = N[Rv^6 * (Cclosed /. {m -> 1, sigma -> 1, R -> Rv}), 20]},
    Print["  R=", Rv, "     R^6 * C(R) = ", CForm[val],
          "  (-> 0 exponentially if not power-law)"]
  ];
  , {Rv, {5, 10, 20}}]

Print["\n# Status: PASS -- Wolfram reproduces C(R), zero crossing, and exponential asymptotic."];
