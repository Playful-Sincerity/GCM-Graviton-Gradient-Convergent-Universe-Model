(* H1 — Check 03: Wolfram Engine independent cross-check                *)
(* Verifies:                                                             *)
(*   (a) Dimensional algebra: coupling m²/A takes (∇·J_g)·v → Tesla      *)
(*   (b) Curl of F_radial + F_uniform is identically 0                   *)
(*   (c) Stagnation point on -z axis at z = -√(q/v₀)                     *)

(* --- Part (a): dimensional algebra --- *)
(* SI exponents encoded as {m, kg, s, A} vectors *)
Print["--- Dimensional algebra ---"];
productExp = {-2, 1, -2, 0};       (* (∇·J_g)·v: kg m⁻² s⁻²           *)
teslaExp   = { 0, 1, -2, -1};      (* Tesla = kg A⁻¹ s⁻²              *)
couplingExp = teslaExp - productExp;
Print["(∇·J_g)·v exponents   = ", productExp];
Print["Tesla exponents         = ", teslaExp];
Print["Coupling needed         = ", couplingExp, "  (expected {2, 0, 0, -1} = m²/A)"];
dimPassA = couplingExp === {2, 0, 0, -1};
Print["Dimensional match (a): ", If[dimPassA, "PASS", "FAIL"]];

(* --- Part (b): curl of combined field --- *)
Print[""];
Print["--- Curl of F_radial + F_uniform ---"];
(* In Wolfram, Curl[] works on vector fields in given coordinate systems. *)
Clear[x, y, z, q, v0];
rVec = {x, y, z};
rMag = Sqrt[x^2 + y^2 + z^2];
Fradial = q * rVec / rMag^3;
Funiform = {0, 0, v0};
Ftotal = Fradial + Funiform;

curlTotal = Simplify[Curl[Ftotal, {x, y, z}]];
Print["Curl of F_total = ", curlTotal];
curlPassB = (curlTotal === {0, 0, 0});
Print["Curl is zero (b): ", If[curlPassB, "PASS", "FAIL"]];

(* --- Part (c): stagnation point on -z axis --- *)
Print[""];
Print["--- Stagnation point on -z axis ---"];
FzOnAxis = q*z/Abs[z]^3 + v0;  (* F_z on the z-axis *)
(* For z<0: Abs[z] = -z, so Abs[z]^3 = -z^3, giving F_z = -q/z² + v₀ *)
FzNeg = -q/z^2 + v0;
solZ = Solve[FzNeg == 0, z];
Print["Solutions for F_z = 0 on the -z axis:  ", solZ];
(* Expected negative root: z = -Sqrt[q/v0] *)
expected = -Sqrt[q/v0];
rootValues = z /. solZ;  (* list of root expressions *)
(* Test each root: does its SQUARE equal q/v0? And is it negative? *)
matchSquare = AssumptionsSimplify /@ rootValues;
squareOK = Map[Simplify[#^2 - q/v0, Assumptions -> {q > 0, v0 > 0}] === 0 &, rootValues];
Print["Roots squared satisfy z² = q/v₀? ", squareOK];
(* Check for a negative root (q, v0 > 0 implies -Sqrt[q/v0] is the negative one) *)
hasNegativeRoot = AnyTrue[rootValues,
  (Simplify[# + Sqrt[q/v0], Assumptions -> {q > 0, v0 > 0}] === 0) &];
Print["Negative root matches -√(q/v₀): ", hasNegativeRoot];

stagPassC = AllTrue[squareOK, TrueQ] && hasNegativeRoot;

(* --- Overall --- *)
allPass = dimPassA && curlPassB && stagPassC;
Print[""];
Print["Status: ", If[allPass, "PASS", "FAIL"]];
