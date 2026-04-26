(* Q3 Check 4 — Wolfram Language cross-check.
   Computes the E_n * P_n table, the analytic limit, and the correction
   series to independently verify the SymPy and mpmath calculations.  *)

Ry = 136/10;  (* 13.6 eV, exact as rational *)
En[n_] := Ry / n^2;
Pn[n_] := 10 n^2 + 2;
Prod[n_] := En[n] * Pn[n];

Print["# Q3 Check 4 — Wolfram Language independent run"];
Print[""];
Print["Using Ry = 136/10 (rational, exact):"];
Print[""];
Print[StringJoin["n    P_n    |E_n| (eV)    |E_n|*P_n (eV)"]];

Table[
 Print[n, "    ", Pn[n], "    ", N[En[n], 10], "    ", Simplify[Prod[n]], " = ", N[Prod[n], 10]],
 {n, 1, 5}
];

Print[""];
Print["Symbolic asymptote Limit_{n->Infinity} |E_n|*P_n:"];
asymptote = Limit[Prod[n], n -> Infinity];
Print["  = ", asymptote, " eV  (expected 136)"];
Print[""];

Print["Correction series (Ry*(10 + 2/n^2) form):"];
alt = Simplify[Prod[n]];
Print["  Prod[n] simplified = ", alt];
Print[""];

Print["Variation across n=1..5:"];
prods = Table[N[Prod[n], 10], {n, 1, 5}];
Print["  values   = ", prods];
Print["  max      = ", Max[prods]];
Print["  min      = ", Min[prods]];
Print["  fraction = ", N[(Max[prods] - Min[prods])/Max[prods] * 100, 4], " %"];
Print[""];

Print["Large-n convergence:"];
Table[
 Print["  n = ", n, "  Prod = ", N[Prod[n], 15], "  deviation from 136 = ", N[Prod[n] - 136, 6]],
 {n, {10, 100, 1000, 10000}}
];
