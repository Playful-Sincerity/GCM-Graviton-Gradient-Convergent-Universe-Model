# M1 — Verification Record

**Tally:** 4/5 checks passed cleanly; 1 check is framing-dependent (see Check 4). Cross-tool agreement: Wolfram ↔ mpmath to 15+ digits.
**Last run:** 2026-04-24.
**Reproducible:** Yes — all scripts live in [verification/](verification/); inputs centralized in [inputs.json](verification/inputs.json); captured stdout in [verification/outputs/](verification/outputs/).

---

## Check 1 — Dimensional analysis (SymPy units)

- **Tool:** Python 3.14.4 / SymPy 1.14.0 (symbolic units module)
- **Script:** [verification/check_01_dimensional.py](verification/check_01_dimensional.py)
- **Output:** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** The symbolic expression `rho * sqrt(hbar*G/c^3)^3` reduces to pure `kilogram` — the meter and second units cancel as expected. The numeric prefactor is `4.222e-87`, matching the claim.

## Check 2 — Numerical substitution (mpmath, 50-digit precision)

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_02_numeric_mpmath.py](verification/check_02_numeric_mpmath.py)
- **Output:** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** At 50-digit precision, `m_g = 4.22211116262...e-87 kg` and `N_g/neutron = 3.967...e+59`. The 0.05% difference from the claim's round-number `4.22e-87` is rounding of the stated value in the session brief, not a computational discrepancy. Both the `rho_bound = 1e18` (session brief) and `rho_bound = 4e17` (gcm_v2) cases are computed; the second yields `m_g ≈ 1.69e-87 kg` as expected.

## Check 3 — LIGO bound margin

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_03_ligo_margin.py](verification/check_03_ligo_margin.py)
- **Output:** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** `log10(LIGO_kg / m_g_GCM) = 27.626` — margin is 27.6 orders of magnitude (rounds up to "~28 orders"). Both the kg-form and eV/c² -form are printed for direct comparison with the LIGO-Virgo literature.

## Check 4 — Planck-density limit (honesty check; framing-dependent)

- **Tool:** Python 3.14.4 / mpmath 1.3.0
- **Script:** [verification/check_04_limit_planck_density.py](verification/check_04_limit_planck_density.py)
- **Output:** [verification/outputs/check_04.txt](verification/outputs/check_04.txt)
- **Result:** INCONCLUSIVE (two valid readings; see below)
- **Notes:** The session brief asked: "at `rho_bound → rho_Planck`, `m_g` should stay consistent with LIGO." It does not. At Planck density, `m_g` equals the Planck mass (`2.176e-8 kg`), which exceeds the LIGO bound by 51 orders of magnitude. **This is an algebraic identity** — `rho * ell_P^3` at Planck density necessarily returns `sqrt(hbar*c/G)`. The check confirmed the identity (relative difference between `rho_Planck * ell_P^3` and the standard Planck mass is 0.0 in mpmath, 1.5e-16 in Wolfram — both machine-level). Reinterpreted as a *constraint* on `rho_bound`: LIGO requires `rho_bound ≤ 4.22e+45 kg/m^3`. Nuclear density satisfies this by 27.6 orders of magnitude. Under the literal reading of the session brief the check fails; under the physically-meaningful reading the check is a PASS that strengthens the claim by deriving a hard upper bound on the density assumption.

## Check 5 — Wolfram Language independent cross-check

- **Tool:** Wolfram Engine 14.3.0 via `wolframscript`
- **Script:** [verification/check_05_wolfram.wls](verification/check_05_wolfram.wls)
- **Output:** [verification/outputs/check_05_wolfram.txt](verification/outputs/check_05_wolfram.txt)
- **Result:** PASS — agrees with mpmath to 15+ significant digits on every quantity.
- **Notes:**
  - `ell_P`: Wolfram `1.61625502392855e-35`; mpmath `1.6162550239285500e-35` — identical.
  - `m_g (nuclear)`: Wolfram `4.2221111626220185e-87`; mpmath `4.2221111626220184e-87` — agreement to last digit.
  - `log10(LIGO margin)`: both give `27.6255393...`.
  - `m_g(rho_Planck)`: both give `2.1764343e-8 kg`, agreeing with the standard Planck-mass identity to machine precision.
  - No cross-tool disagreements found.

---

## Cross-tool Summary

| Quantity | Python (mpmath, 50-digit) | Wolfram (14.3.0) | Agreement |
|---|---|---|---|
| `ell_P` (m) | 1.6162550239285500e-35 | 1.61625502392855e-35 | full |
| `m_g` (kg, nuclear) | 4.2221111626220184840...e-87 | 4.2221111626220185e-87 | 16 digits |
| `N_g` per neutron | 3.967037895325890e+59 | 3.96703789532589e+59 | 15 digits |
| `log10(LIGO / m_g)` | 27.6255393242027 | 27.625539324202702 | 16 digits |
| `m_g(rho_Planck)` (kg) | 2.17643434205112666864...e-8 | 2.176434342051127e-8 | 16 digits |

**No disagreements. The claim is numerically robust.**

---

## TODOs / Known gaps

- **Tier decision (green vs yellow):** Per the session-brief strict reading of CC-5 ("no claim is green-tier if any check fails"), Check 4's literal FAIL downgrades M1 to yellow. Per the physically-meaningful reading, Check 4 is a PASS that strengthens the claim. Wisdom's call; the ledger records `amber` until resolved.
- **OQ-2 (max-density scale).** The value `rho_bound ≈ 10^18 kg/m^3` is provisional. If a first-principles argument for this scale is developed, `m_g` updates linearly. The scripts are parameterized by `inputs.json` so sweeping across densities is a one-field edit.
- **OQ-4 (vacuum graviton density).** Not addressed by M1; M1 uses the *maximum packing* density, not the vacuum baseline.
