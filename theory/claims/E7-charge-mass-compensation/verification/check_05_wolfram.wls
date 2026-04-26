(* E7 Check 5 — Wolfram Language independent.
   Cross-checks the SymPy symbolic derivation with a different CAS,
   plus reproduces the spot-check numeric.                          *)

(* Symbolic check *)
E1[me_, e_, k_, hbar_] := -me * k^2 * e^4 / (2 * hbar^2);

Print["# E7 Check 5 — Wolfram independent run"];
Print[""];

dE1de = D[E1[me, e, k, hbar], e];
dE1dme = D[E1[me, e, k, hbar], me];

Print["E_1               = ", E1[me, e, k, hbar]];
Print["dE_1/de           = ", Simplify[dE1de]];
Print["dE_1/dm_e         = ", Simplify[dE1dme]];
Print[""];

(* Verify the analytical identities *)
expectedDe = Simplify[4 * E1[me, e, k, hbar] / e];
expectedDm = Simplify[E1[me, e, k, hbar] / me];

Print["4*E_1/e           = ", expectedDe];
Print["E_1/m_e           = ", expectedDm];
Print["dE/de == 4E_1/e?  ", Simplify[dE1de - expectedDe] === 0];
Print["dE/dm == E_1/m_e? ", Simplify[dE1dme - expectedDm] === 0];
Print[""];

(* Solve for Delta_m given the perturbation condition *)
sol = Solve[dE1de * De + dE1dme * Dm == 0, Dm];
ratio = Simplify[(Dm /. sol[[1]]) / me / (De / e)];
Print["Solve perturb=0 for Dm: ", Dm /. sol[[1]]];
Print["(Dm/m_e) / (De/e) = ", ratio];
Print[""];

(* Numerical spot check *)
meVal = 9.1093837015*^-31;
eVal = 1.602176634*^-19;
DeVal = 1.0*^-35;
DmComputed = -4 * meVal * DeVal / eVal;
Print["Numerical spot check (De = 1e-35 C):"];
Print["  Dm_computed  = ", DmComputed, " kg"];
Print["  brief stated = -2.27*10^-46 kg"];
Print["  relative diff = ", N[Abs[DmComputed - (-2.27*^-46)]/(2.27*^-46), 6]];
Print[""];

(* Also verify the Bohr ground state is ~-13.6 eV *)
kVal = 8.9875517873681764*^9;
hbarVal = 1.054571817*^-34;
E1Val = E1[meVal, eVal, kVal, hbarVal];
E1eV = E1Val / 1.602176634*^-19;
Print["E_1 (Bohr)  = ", E1Val, " J = ", E1eV, " eV (expected -13.6057 eV)"];
