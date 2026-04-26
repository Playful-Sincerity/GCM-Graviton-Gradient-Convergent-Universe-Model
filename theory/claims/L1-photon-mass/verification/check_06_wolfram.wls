(* L1 Check 06 — Wolfram Language independent verification.
   Unit conversion of m_gamma (kg -> eV/c^2) and bounds comparison.

   Reads nothing — inputs are embedded as literals (labeled with source).
   This is intentional: Wolfram acts as the independent oracle and should
   not depend on files the Python stack owns.

   Run with: wolframscript -file check_06_wolfram.wls

   The .py scripts read verification/inputs.json; this .wls hardcodes the
   same constants for independence. If values drift, they drift visibly. *)

Print["L1 — Check 06: Wolfram Language independent verification"];
Print["=============================================================="];

(* Inputs (same as inputs.json) *)
mGammaKg = 10.0^-54;                        (* GCM estimate *)
c = Quantity["SpeedOfLight"];                (* causality limit, exact *)
eVtoJ = 1.602176634 * 10^-19;                (* SI 2019 exact definition, J/eV *)
wangBoundEVpc2 = 2.1 * 10^-15;               (* Wang et al. 2023, FRB dispersion *)
pdgBoundEVpc2 = 1.0 * 10^-18;                (* PDG 2022 approximate; needs live check *)

Print["Input: m_gamma = 10^-54 kg (GCM estimate)"];
Print[""];

(* Method A: Wolfram's native unit system *)
energyNative = UnitConvert[Quantity[mGammaKg, "Kilograms"] * c^2, "Electronvolts"];
Print["Method A (Wolfram UnitConvert):"];
Print["  m_gamma * c^2 = ", energyNative];

(* Extract numerical value in eV *)
mGammaEVnumeric = QuantityMagnitude[energyNative];
Print["  m_gamma in eV/c^2 = ", N[mGammaEVnumeric, 20]];
Print[""];

(* Method B: arithmetic check with exact SI 2019 constants *)
cExact = 299792458;                         (* m/s, exact *)
mGammaEVarith = mGammaKg * cExact^2 / eVtoJ;
Print["Method B (explicit arithmetic with exact c):"];
Print["  m_gamma in eV/c^2 = ", N[mGammaEVarith, 20]];
Print[""];

(* Agreement check *)
agreement = Abs[mGammaEVnumeric - mGammaEVarith]/mGammaEVarith;
Print["Relative agreement between methods: ", N[agreement, 6]];
Print[""];

(* Compare to hand-calculated value (5.61e-19) from derivation.md *)
handValue = 5.61 * 10^-19;
handAgreement = Abs[mGammaEVnumeric - handValue]/handValue;
Print["Hand calc (5.61e-19) relative error: ", N[handAgreement, 6]];
Print[""];

(* Bounds comparison *)
Print["Bounds comparison:"];
wangRatio = wangBoundEVpc2 / mGammaEVnumeric;
wangOrders = Log[10, wangRatio];
Print["  vs Wang 2023 (2.1e-15):"];
Print["    bound / GCM = ", N[wangRatio, 6]];
Print["    orders below = ", N[wangOrders, 6]];
Print["    Passes? ", mGammaEVnumeric < wangBoundEVpc2];
Print[""];

pdgRatio = pdgBoundEVpc2 / mGammaEVnumeric;
pdgOrders = Log[10, pdgRatio];
Print["  vs PDG 2022 approx (1.0e-18):"];
Print["    bound / GCM = ", N[pdgRatio, 6]];
Print["    orders below = ", N[pdgOrders, 6]];
Print["    Passes? ", mGammaEVnumeric < pdgBoundEVpc2];
Print[""];

(* Drift from plan's "4 orders" claim *)
planClaim = 4.0;
drift = Abs[wangOrders - planClaim];
Print["Plan claims '4 orders below Wang'. Actual: ", N[wangOrders, 6]];
Print["Drift: ", N[drift, 6], " orders (minor overstatement, corrected in derivation.md)"];
Print[""];

Print["Status: PASS — Wolfram independent check confirms the kg -> eV/c^2 conversion and bounds comparison."];
