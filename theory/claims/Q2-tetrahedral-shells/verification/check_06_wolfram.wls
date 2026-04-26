(* Q2 Check 6 — Wolfram Language algebraic + numerical verification.

   Run with:  wolframscript -file check_06_wolfram.wls
   or load into a Wolfram notebook.

   Confirms the symbolic and numerical equivalence of:
   (a) Cuboctahedral decomposition: 12 + 24(n-1) + 4(n-1)(n-2) + 6(n-1)^2
   (b) Mackay icosahedral decomposition: 12 + 30(n-1) + 10(n-1)(n-2)
   (c) Closed-form formula: 10 n^2 + 2

   All three should be identically equal as polynomials in n.
*)

Print["=== Q2 Verification — Wolfram Language ==="];
Print[];

(* Cuboctahedral decomposition *)
cubocta[n_] := 12 + 24 (n - 1) + 4 (n - 1) (n - 2) + 6 (n - 1)^2;
cuboctaExpanded = Expand[cubocta[n]];
Print["Cuboctahedral decomposition: ", cubocta[n]];
Print["  Expanded: ", cuboctaExpanded];
Print[];

(* Mackay icosahedral decomposition *)
mackay[n_] := 12 + 30 (n - 1) + 10 (n - 1) (n - 2);
mackayExpanded = Expand[mackay[n]];
Print["Mackay icosahedral decomposition: ", mackay[n]];
Print["  Expanded: ", mackayExpanded];
Print[];

(* Closed form *)
formula[n_] := 10 n^2 + 2;
Print["Closed-form formula: ", formula[n]];
Print[];

(* Symbolic equivalence checks *)
Print["=== Symbolic equivalence ==="];
Print["Cuboctahedral == Formula: ", Simplify[cubocta[n] - formula[n]] === 0];
Print["Mackay       == Formula: ", Simplify[mackay[n] - formula[n]] === 0];
Print["Cuboctahedral == Mackay: ", Simplify[cubocta[n] - mackay[n]] === 0];
Print[];

(* Numerical table for n = 1..5 *)
Print["=== Numerical table (n = 1..5) ==="];
Print["  n    cubocta  mackay  formula"];
Do[
  Print["  ", n, "      ", cubocta[n], "      ", mackay[n], "      ", formula[n]],
  {n, 1, 5}
];
Print[];

(* Limit / boundary *)
Print["=== Boundary ==="];
Print["formula[0] = ", formula[0], "  (artifact; central site is 1 graviton, not 2)"];
Print[];

(* OEIS A005901 cross-check *)
Print["=== OEIS A005901 cross-check (n = 1..10) ==="];
oeis = {12, 42, 92, 162, 252, 362, 492, 642, 812, 1002};
checks = Table[formula[n] === oeis[[n]], {n, 1, 10}];
Print["All 10 values match OEIS A005901: ", AllTrue[checks, # &]];
