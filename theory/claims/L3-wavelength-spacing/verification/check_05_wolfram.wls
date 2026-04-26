(* L3 Check 05 — Wolfram Language independent symbolic check.
   Derives d_obs / d_emit = (1 + z) from the three L3 premises
   using Wolfram's symbolic engine as independent arbiter of the
   SymPy result in check_02.

   Run with: wolframscript -file check_05_wolfram.wls *)

Print["L3 — Check 05: Wolfram independent symbolic check"];
Print["=============================================================="];
Print[""];

(* Premises:
   (1) lambdaObs = (1 + z) * lambdaEmit   [redshift definition]
   (2) lambda = N * d                      [L3 identification]
   (3) NEmit = NObs = N                    [L3 Case A: N constant]

   We compute by direct substitution, not Solve — Solve over-constrained
   on an under-determined system returns {}. Direct substitution is the
   correct derivation.
*)

Print["Premises:"];
Print["  (1) lambdaObs = (1 + z) * lambdaEmit   [redshift definition]"];
Print["  (2) lambda = N * d                      [L3 identification]"];
Print["  (3) NEmit = NObs = N                    [N constant, L3 Case A]"];
Print[""];

(* Direct substitution derivation *)
(* By (2): dEmit = lambdaEmit / N, dObs = lambdaObs / N. *)
dEmitSymb = lambdaEmit / N;
dObsSymb = lambdaObs / N;

(* By (1): lambdaObs = (1+z)*lambdaEmit. Substitute into dObs. *)
dObsFromPremises = dObsSymb /. lambdaObs -> (1 + z) * lambdaEmit;
Print["dEmit = ", dEmitSymb];
Print["dObs  = ", dObsFromPremises];
Print[""];

ratio = Simplify[dObsFromPremises / dEmitSymb];
Print["dObs / dEmit = ", ratio];
Print[""];

(* Target *)
target = 1 + z;
matches = Simplify[ratio - target] == 0;
Print["Target: (1 + z) = ", target];
Print["ratio == target ? ", matches];
Print[""];

(* Worked example at z = 1, lambdaEmit = 500 nm, N = 1 *)
zVal = 1;
lambdaEmitVal = 500 * 10^-9;  (* 500 nm in meters *)
NVal = 1;
dEmitVal = lambdaEmitVal / NVal;
dObsVal = ((1 + zVal) * lambdaEmitVal) / NVal;

Print["Worked example (numerical spot check):"];
Print["  z = ", zVal];
Print["  lambdaEmit = ", N[lambdaEmitVal], " m (500 nm)"];
Print["  N = ", NVal];
Print["  dEmit = ", N[dEmitVal], " m"];
Print["  dObs  = ", N[dObsVal], " m"];
Print["  dObs / dEmit = ", N[dObsVal / dEmitVal]];
Print["  (1 + z) = ", 1 + zVal];
Print["  Match? ", dObsVal / dEmitVal == 1 + zVal];
Print[""];

If[matches,
  Print["Status: PASS — Wolfram symbolic: d_obs/d_emit = (1+z). Confirms SymPy Check 02."],
  Print["Status: FAIL — symbolic derivation does not match target."]
];
