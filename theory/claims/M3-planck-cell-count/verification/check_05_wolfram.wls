(* M3 Check 5 — Wolfram Language independent.
   Cross-checks mpmath calculations using native high-precision arithmetic.
   Per the L2 precision lesson: uses SetPrecision on all constants to
   guarantee high-precision propagation through exponentiation.          *)

prec = 40;

hbar    = SetPrecision[1.054571817*^-34, prec];  (* J s *)
G       = SetPrecision[6.67430*^-11, prec];      (* m^3/(kg s^2) *)
c       = SetPrecision[2.99792458*^8, prec];     (* m/s *)
RH      = SetPrecision[4.4*^26, prec];           (* m *)
Nbaryon = SetPrecision[10^80, prec];

(* Planck length *)
ellP = Sqrt[hbar * G / c^3];
vP   = ellP^3;

(* Observable-universe volume *)
Vuniv = (4/3) * Pi * RH^3;

(* Graviton count *)
Ncells = Vuniv / vP;

(* Baryon ratio *)
ratio = Ncells / Nbaryon;

(* Holographic scale *)
SBH = (RH/ellP)^2;

Print["# M3 Check 5 — Wolfram Language independent run"];
Print["# Precision: ", prec, " decimal digits (enforced via SetPrecision)"];
Print[""];
Print["ell_P (computed)   = ", ellP, " m"];
Print["V_P                = ", vP, " m^3"];
Print["V_universe         = ", Vuniv, " m^3"];
Print[""];
Print["N_cells            = ", Ncells];
Print["log10(N_cells)     = ", Log[10, Ncells]];
Print["Expected N ≈ 8.5*10^184"];
Print[""];
Print["N / N_baryon       = ", ratio];
Print["log10 ratio        = ", Log[10, ratio]];
Print["Expected ~10^105"];
Print[""];
Print["S_BH (area-scale)  = ", SBH];
Print["N / S_BH           = ", Ncells / SBH];
Print["log10 ratio        = ", Log[10, Ncells / SBH]];
Print[""];
Print["Cross-ref to short ell_P (1.616e-35 m exact-like):"];
ellPshort = SetPrecision[1.616*^-35, prec];
NcellsShort = Vuniv / ellPshort^3;
Print["  N_cells (short)  = ", NcellsShort];
Print["  log10            = ", Log[10, NcellsShort]];
