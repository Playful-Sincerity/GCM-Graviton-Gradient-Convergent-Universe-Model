(* L2 Check 5 — Wolfram Language independent high-precision check.

   Convention reminder: c here is the causality limit, not the speed
   of light. Per theory/speed-of-causality-principle.md, GCM photons
   travel at v < c strictly. DO NOT write v = c.

   IMPORTANT precision note (found during initial run):
   Naive use of `N[...]` does NOT propagate precision correctly when an
   operand is a machine-precision number; Sqrt[1 - 10^-37] computed
   with standard N[] returns 1 exactly, causing c - v to report zero.
   Solution: use SetPrecision on all quantities BEFORE arithmetic so
   the chain of operations carries >= 60 decimal digits of precision.  *)

prec = 60;

cCausality = SetPrecision[299792458, prec];                (* m/s *)
mGamma     = SetPrecision[10^-54, prec];                   (* kg *)
EJ         = SetPrecision[1.602176634*^-19, prec];         (* J  = 1 eV *)
FRBbound   = SetPrecision[2.1*^-15, prec];                 (* eV/c^2 *)
eVperKg    = SetPrecision[1.782661921*^-36, prec];         (* kg per eV/c^2 *)

(* High-precision computation of Delta_v *)
mGc2 = mGamma * cCausality^2;
eps  = mGc2 / EJ;
eps2 = eps^2;

vPhoton     = cCausality * Sqrt[1 - eps2];
DeltaV      = cCausality - vPhoton;
DeltaVTaylor = cCausality * eps2 / 2;

Print["# L2 Check 5 — Wolfram Language independent run"];
Print["# Convention: c = causality limit, v_photon < c strictly."];
Print["# Precision: ", prec, " decimal digits (enforced via SetPrecision)."];
Print[""];
Print["c (causality)     = ", cCausality, " m/s"];
Print["m_gamma (GCM)     = ", mGamma, " kg"];
Print["E (photon example)= 1 eV = ", EJ, " J"];
Print[""];
Print["epsilon           = ", eps];
Print["epsilon^2         = ", eps2];
Print[""];
Print["v_photon (exact, high precision) = ", vPhoton, " m/s"];
Print["Delta_v (direct)                 = ", DeltaV, " m/s"];
Print["Delta_v (Taylor approx c*eps^2/2)= ", DeltaVTaylor, " m/s"];
Print["  rel diff direct vs Taylor      = ", Abs[DeltaV - DeltaVTaylor]/DeltaV];
Print[""];
Print["Session brief Δv                 = 4.74*10^-29 m/s"];
Print["  rel error direct vs brief      = ", Abs[DeltaV - 4.74*^-29]/(4.74*^-29)];
Print[""];

(* v < c structural check — the load-bearing property *)
Print["Structural: v_photon < c_causality? ", vPhoton < cCausality];
Print["  (GCM REQUIRES v < c strictly; per L1 commitment m_gamma > 0)"];
Print[""];

(* FRB bound comparison *)
mGammaEVc2 = mGamma / eVperKg;
Print["GCM m_gamma in eV/c^2  = ", mGammaEVc2];
Print["Wang 2023 FRB bound    = ", FRBbound, " eV/c^2"];
Print["log10(FRB/GCM)         = ", Log[10, FRBbound / mGammaEVc2]];
Print[""];

(* Symbolic Taylor expansion *)
Clear[eps];
taylorSeries = Series[Sqrt[1 - eps^2], {eps, 0, 6}];
Print["Symbolic Taylor expansion of sqrt(1-eps^2) around eps=0:"];
Print["  ", Normal[taylorSeries]];
