(* H2 — Check 04: Wolfram Engine independent cross-check                *)
(* Confirms the ODE and PDE derivations via Wolfram's DSolve.            *)

(* --- Newton's cooling ODE --- *)
Print["--- ODE: dρ/dt = -λ(ρ - ρ_0) ---"];
sol = DSolve[{rho'[t] == -lambda*(rho[t] - rho0), rho[0] == rhoInit}, rho[t], t];
Print["Solution: ", sol];

(* Claimed form *)
claimed[t_] := rho0 + (rhoInit - rho0)*Exp[-lambda*t];
diff = Simplify[(rho[t] /. First[sol]) - claimed[t]];
Print["Difference (Wolfram sol - claimed exponential) simplified: ", diff];
odePass = (diff === 0);

(* Asymptotic behaviour — limit returns ConditionalExpression under real/positive
   assumptions; wrap with Simplify[..., Assumptions] to strip the condition. *)
tLimit = Simplify[
  Limit[(rho[t] /. First[sol]) - rho0, t -> Infinity],
  Assumptions -> {lambda > 0, rho0 \[Element] Reals, rhoInit \[Element] Reals}
];
Print["lim t->∞ (ρ - ρ_0) under λ>0, ρ_0 & ρ_init real = ", tLimit];
limitPass = (tLimit === 0);

(* --- Fourier PDE derivation from continuity + diffusive flux --- *)
(* Note: D is a Wolfram built-in for partial derivatives; use Dcoef for the *)
(* diffusion coefficient symbol to avoid collision. *)
Print[""];
Print["--- Fourier PDE from continuity + J = -D_coef ∇ρ ---"];
Clear[rhoF, x, y, z, tt, Dcoef];
fluxX = -Dcoef * D[rhoF[x, y, z, tt], x];
fluxY = -Dcoef * D[rhoF[x, y, z, tt], y];
fluxZ = -Dcoef * D[rhoF[x, y, z, tt], z];
divJ = D[fluxX, x] + D[fluxY, y] + D[fluxZ, z];
continuityRhs = -divJ;
laplacian = D[rhoF[x, y, z, tt], {x, 2}] + D[rhoF[x, y, z, tt], {y, 2}] + D[rhoF[x, y, z, tt], {z, 2}];
expectedRhs = Dcoef * laplacian;
pdeDiff = Simplify[continuityRhs - expectedRhs];
Print["Continuity RHS -∇·J = ", continuityRhs];
Print["Expected D∇²ρ      = ", expectedRhs];
Print["Difference: ", pdeDiff];
pdePass = (pdeDiff === 0);

(* --- Overall --- *)
allPass = odePass && limitPass && pdePass;
Print[""];
Print["ODE form matches claimed exponential: ", If[odePass, "PASS", "FAIL"]];
Print["Asymptotic equilibrium (ρ -> ρ_0):     ", If[limitPass, "PASS", "FAIL"]];
Print["Fourier PDE derivation:                ", If[pdePass, "PASS", "FAIL"]];
Print[""];
Print["Status: ", If[allPass, "PASS", "FAIL"]];
