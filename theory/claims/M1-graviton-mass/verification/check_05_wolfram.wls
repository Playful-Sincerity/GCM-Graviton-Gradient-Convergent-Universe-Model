(* M1 Check 5 — Independent Wolfram Language computation.
   Cross-checks the Python/mpmath results at 40-digit precision.
   Run with: wolframscript -file check_05_wolfram.wls                 *)

(* Constants from CODATA 2018 *)
hbar = 1.054571817*^-34;  (* J*s *)
G    = 6.67430*^-11;      (* m^3/(kg*s^2) *)
c    = 2.99792458*^8;     (* m/s *)
mNeutron = 1.67492749804*^-27;  (* kg *)
eVperKg = 1.782661921*^-36;     (* kg per eV/c^2 *)
LIGOeVc2 = 1.0*^-23;            (* eV/c^2 *)
rhoNuclear = 1.0*^18;           (* kg/m^3 *)

(* Planck length and volume, full precision *)
ellP = N[Sqrt[hbar G/c^3], 40];
vP   = ellP^3;

(* Graviton mass at nuclear density *)
mG = rhoNuclear * vP;

(* Gravitons per neutron *)
Ng = mNeutron/mG;

(* LIGO bound in kg *)
LIGOkg = LIGOeVc2 * eVperKg;

(* Planck density *)
rhoPlanck = c^5/(hbar G^2);

(* m_g at Planck density — should equal Planck mass *)
mGAtPlanck = rhoPlanck * vP;
mPlanckStandard = N[Sqrt[hbar c/G], 40];

(* rho_bound upper-bound from LIGO *)
rhoMaxLIGO = LIGOkg/vP;

Print["# M1 Check 5 — Wolfram Language independent run"];
Print[""];
Print["ell_P              = ", N[ellP, 20], " m"];
Print["V_P                = ", N[vP,   20], " m^3"];
Print["m_g (nuclear rho)  = ", N[mG,   20], " kg"];
Print["N_g per neutron    = ", N[Ng,   20]];
Print[""];
Print["LIGO bound         = ", N[LIGOkg, 20], " kg"];
Print["margin LIGO/m_g    = ", N[LIGOkg/mG, 20]];
Print["log10 margin       = ", N[Log[10, LIGOkg/mG], 10]];
Print[""];
Print["rho_Planck          = ", N[rhoPlanck, 20], " kg/m^3"];
Print["m_g(rho_Planck)     = ", N[mGAtPlanck, 20], " kg"];
Print["sqrt(hbar*c/G)      = ", N[mPlanckStandard, 20], " kg  (Planck mass, standard)"];
Print["relative agreement = ", N[Abs[mGAtPlanck - mPlanckStandard]/mPlanckStandard, 6]];
Print[""];
Print["rho_bound <= LIGO constraint: ", N[rhoMaxLIGO, 10], " kg/m^3"];
Print["nuclear rho = 1.0e18 kg/m^3 -> margin ",
       N[Log[10, rhoMaxLIGO/rhoNuclear], 6], " orders of magnitude"];
Print[""];
Print["Expected claim value m_g = 4.22e-87 kg"];
Print["Relative error           = ", N[Abs[mG - 4.22*^-87]/(4.22*^-87), 6]];
