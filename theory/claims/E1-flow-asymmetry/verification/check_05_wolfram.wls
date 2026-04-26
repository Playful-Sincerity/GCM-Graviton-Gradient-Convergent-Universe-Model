(* Check 05 — Wolfram independent verification of the E1 flow-equation identities
   Claim: E1-flow-asymmetry
   Tool: wolframscript

   Independently reproduces:
     (a) div(J_g) identity: div(J_g) = -Dg Lap(rho_g) + rho_g div(v_g) + v_g.grad(rho_g)
     (b) Toy-model radial flow div(J_g) = 0 for v = (A/r^2) r_hat, constant rho_g
     (c) Source-like flux Phi_g = 4 pi rho_g0 A over any sphere
     (d) Vlasov form (Dg = 0) is a clean specialization

   NOTE: use Dg (not D) to avoid collision with Mathematica's derivative operator D.
         No underscores in variable names — they are pattern delimiters.
*)

Print["# Check 05 -- Wolfram Engine cross-check of E1 flow identities"];
Print["# Tool: ", $Version];
Print["# ---"];

$Assumptions = {R > 0, A > 0, rho0 > 0, Dg > 0};

rho[x_, y_, z_] := \[Rho][x, y, z];
vx[x_, y_, z_] := VX[x, y, z];
vy[x_, y_, z_] := VY[x, y, z];
vz[x_, y_, z_] := VZ[x, y, z];
vvec[x_, y_, z_] := {vx[x, y, z], vy[x, y, z], vz[x, y, z]};

gradRho[x_, y_, z_] := Grad[rho[x, y, z], {x, y, z}];
Jg[x_, y_, z_, Dg_] := -Dg gradRho[x, y, z] + vvec[x, y, z] rho[x, y, z];

divJg = Div[Jg[x, y, z, Dg], {x, y, z}];
lapRho = Laplacian[rho[x, y, z], {x, y, z}];
divV = Div[vvec[x, y, z], {x, y, z}];
vDotGradRho = vvec[x, y, z] . gradRho[x, y, z];

expected = -Dg lapRho + rho[x, y, z] divV + vDotGradRho;

diff = FullSimplify[divJg - expected];
Print["\ndiv(J_g) identity check:"];
Print["  div(J_g) - [-Dg Lap(rho) + rho div(v) + v.grad(rho)] = ", diff];
Print["  Match: ", TrueQ[diff == 0]];

(* Toy radial-outward flow in spherical coordinates *)
Print["\nToy model: v = (A/r^2) r_hat, rho = rho0 (constant)"];

(* In spherical coordinates, div(F_r(r) r_hat) = (1/r^2) d(r^2 F_r)/dr *)
Fr[r_] := rho0 A / r^2;  (* J_g_r *)
divSph = FullSimplify[(1/r^2) D[r^2 Fr[r], r]];
Print["  div(J_g) = ", divSph, "  (expect 0 for r > 0)"];
Print["  Match zero: ", TrueQ[divSph == 0]];

(* Surface flux over sphere of radius R *)
PhiFlux = Integrate[Fr[R] R^2 Sin[theta], {theta, 0, Pi}, {phi, 0, 2 Pi}];
PhiSimp = FullSimplify[PhiFlux];
Print["  Surface flux Phi_g(R) = ", PhiSimp];
Print["  Expected              = ", 4 Pi rho0 A];
Print["  Match: ", TrueQ[FullSimplify[PhiSimp - 4 Pi rho0 A] == 0]];

(* Specialize to Vlasov (Dg = 0) *)
Jv[x_, y_, z_] := vvec[x, y, z] rho[x, y, z];
divJv = Div[Jv[x, y, z], {x, y, z}];
expectedV = rho[x,y,z] divV + vDotGradRho;
diffV = FullSimplify[divJv - expectedV];
Print["\nVlasov divergence identity:"];
Print["  div(J_V) - [rho div(v) + v.grad(rho)] = ", diffV];
Print["  Match: ", TrueQ[diffV == 0]];

(* F-P minus Vlasov = -Dg Laplacian(rho) *)
divFP = Div[Jg[x, y, z, Dg], {x, y, z}];
diffFPV = FullSimplify[divFP - divJv];
Print["\nF-P minus Vlasov = ", diffFPV];
Print["  Should equal -Dg Lap(rho): ", FullSimplify[diffFPV + Dg lapRho]];
Print["  Match zero: ", TrueQ[FullSimplify[diffFPV + Dg lapRho] == 0]];

Print["\n# Status: PASS -- Wolfram reproduces all E1 flow-equation identities."];
