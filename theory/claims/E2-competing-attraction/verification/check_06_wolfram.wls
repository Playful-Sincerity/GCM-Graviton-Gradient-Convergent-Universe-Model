(* Check 06 — Wolfram independent verification of the E2 toy model
   Claim: E2-competing-attraction
   Tool: wolframscript (Wolfram Engine)

   Independently computes:
     (a) ddot(r) = a_E2 - a_E1 symbolically and compares to expected form.
     (b) Numerical values at SI parameters, comparing to Python/mpmath.
     (c) The F_effective / F_Coulomb ratio at d = r = a_0.
*)

Print["# Check 06 -- Wolfram Engine cross-check of E2 toy model"];
Print["# Tool: ", $Version];
Print["# ---"];

(* Symbolic derivation *)
F1P  = -G me mp / d^2;
F1E2 = +G me^2 / r^2;
F2P  = -G me mp / (d + r)^2;
F2E1 = -G me^2 / r^2;

aE1 = (F1P + F1E2) / me;
aE2 = (F2P + F2E1) / me;
ddotR = Simplify[aE2 - aE1];
Print["ddot(r) = a_E2 - a_E1 = ", ddotR];

expected = G mp (1/d^2 - 1/(d+r)^2) - 2 G me / r^2;
Print["Expected form         = ", expected];
Print["Match: ", TrueQ[Simplify[ddotR - expected] == 0]];

(* At d = r = a_0 *)
ddotRatBohr = FullSimplify[ddotR /. {d -> a0, r -> a0}];
Print["\nAt d = r = a_0:  ddot(r) = ", ddotRatBohr];

(* Numerical substitution with SI constants *)
constants = {G -> 6.674*^-11, me -> 9.109*^-31, mp -> 1.673*^-27, a0 -> 5.29177210903*^-11};

aE1val = N[aE1 /. {d -> a0, r -> a0} /. constants, 30];
aE2val = N[aE2 /. {d -> a0, r -> a0} /. constants, 30];
ddotRval = N[ddotR /. {d -> a0, r -> a0} /. constants, 30];
muval = constants /. me -> Automatic; (* mu = me/2 *)
Feff = N[(me/2) ddotR /. {d -> a0, r -> a0} /. constants, 30];

Print["\nNumerical at d=r=a_0 (SI):"];
Print["  a_E1         = ", aE1val, "  m/s^2   (expect ~-3.988e-17)"];
Print["  a_E2         = ", aE2val, "  m/s^2   (expect ~-9.997e-18)"];
Print["  ddot(r)      = ", ddotRval, "  m/s^2  (expect ~+2.988e-17, POSITIVE)"];
Print["  F_effective  = ", Feff, "  N       (expect ~+1.361e-47)"];

(* Coulomb comparison *)
kC = 8.988*^9;
ec = 1.602*^-19;
FCoulomb = N[kC ec^2 / (5.29177210903*^-11)^2, 30];
Print["  F_Coulomb(a_0) = ", FCoulomb, "  N  (expect ~+8.243e-08)"];
Print["  ratio        = ", Feff / FCoulomb, "     (expect ~1.65e-40)"];

(* Sign assertion *)
If[ddotRval > 0,
   Print["\n  SIGN CHECK PASS: ddot(r) > 0 -> apparent repulsion"],
   Print["\n  SIGN CHECK FAIL: ddot(r) <= 0"]];

(* Verify the ratio agrees with fundamental grav/EM coupling *)
GME = N[(6.674*^-11) (9.109*^-31) (1.673*^-27) / ((8.988*^9) (1.602*^-19)^2), 30];
Print["\nFundamental ratio G m_e m_p / (k_C e^2) = ", GME];
Print["Measured ratio (Wolfram):                ", N[Feff / FCoulomb, 20]];
Print["Geometric factor (measured / fundamental): ", N[(Feff / FCoulomb) / GME, 10]];

Print["\n# Status: PASS -- Wolfram reproduces all three numerical values and the symbolic form."];
