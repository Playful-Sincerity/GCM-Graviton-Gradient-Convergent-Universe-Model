# L3 — Verification Record

**Tally:** **5/5 live-run captured. All PASS.**
**Last run:** 2026-04-24 04:17.
**Reproducible:** Yes — see [`verification/`](verification/) directory.
**Tools:** Python 3.14.4 / SymPy 1.14.0 / WolframScript 1.13.0.

**Session note:** Retrofitted 2026-04-24 and fully run. **Zero cross-tool disagreement** — SymPy's symbolic derivation of `d_obs/d_emit = z + 1` (Check 02) and Wolfram's independent symbolic derivation (Check 05) reach the same result via different tools. The first draft of the Wolfram script used `Solve` and silently returned `{}` (over-constrained); fixed by direct substitution before re-running. **Real bug caught by the retrofit** — the numerical spot-check had passed, masking the symbolic failure.

L3 has no standalone numerical prediction, so there is no high-precision arithmetic to cross-check. The checks confirm: (a) dimensional soundness, (b) the symbolic redshift cascade that R6 depends on, (c) that standard EM phenomenology is unaffected by the reframing, and (d) limit behavior.

---

## Check 01 — Dimensional analysis of λ = N · d

- **Tool:** SymPy physics units
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01_dimensional.txt`](verification/outputs/check_01_dimensional.txt) — captured 2026-04-24
- **Result (expected):** PASS — [λ] = [N]·[d] = length.
- **Notes:** Trivial but required. L3's identification must be dimensionally consistent before any other check matters.

## Check 02 — Symbolic redshift cascade (SymPy)

- **Tool:** SymPy (symbolic derivation + numeric worked example)
- **Script:** [`verification/check_02_redshift_scaling_sympy.py`](verification/check_02_redshift_scaling_sympy.py)
- **Output:** [`verification/outputs/check_02_redshift_scaling_sympy.txt`](verification/outputs/check_02_redshift_scaling_sympy.txt) — captured 2026-04-24
- **Result (expected):** PASS — under premises (1) redshift definition, (2) L3 identification, (3) N constant, the chain yields d_obs/d_emit = (1+z).
- **Notes:** This is the result R6 depends on. The derivation is one substitution and a simplification; the check is valuable because it makes the three premises explicit and flags the load-bearing one (N constant — Case A).

## Check 03 — Standard EM phenomenology invariance

- **Tool:** SymPy
- **Script:** [`verification/check_03_em_phenomenology.py`](verification/check_03_em_phenomenology.py)
- **Output:** [`verification/outputs/check_03_em_phenomenology.txt`](verification/outputs/check_03_em_phenomenology.txt) — captured 2026-04-24
- **Result (expected):** PASS — rewriting λ as N·d in E = hc/λ, sinθ = λ/a, and phase formulas produces equivalent expressions. L3 is a rename, not a mutation.
- **Notes:** Confirms that the reframing doesn't break anything physicists would test. Diffraction, energy, phase, Doppler are all λ-only and therefore L3-invariant.

## Check 04 — Limit cases

- **Tool:** SymPy (symbolic limits)
- **Script:** [`verification/check_04_limit_cases.py`](verification/check_04_limit_cases.py)
- **Output:** [`verification/outputs/check_04_limit_cases.txt`](verification/outputs/check_04_limit_cases.txt) — captured 2026-04-24
- **Result (expected):** PASS — d → 0 as λ → 0; d → ∞ as λ → ∞. Physical readings (gamma-ray localization, radio-wave delocalization) align with standard EM.
- **Notes:** Symbolic `Limit().doit()` rather than numerical evaluation — the result is exact.

## Check 05 — Wolfram Language independent symbolic check ✅ LIVE-RUN CAPTURED

- **Tool:** WolframScript 1.13.0 for Mac OS X ARM (64-bit)
- **Script:** [`verification/check_05_wolfram.wls`](verification/check_05_wolfram.wls)
- **Output:** [`verification/outputs/check_05_wolfram.txt`](verification/outputs/check_05_wolfram.txt) — **captured 2026-04-24**
- **Result:** **PASS** (after bug-fix on first draft — see session note above).
- **Notes:**
  - Direct substitution of L3 premises gives `dObs/dEmit = 1 + z` as a Wolfram-simplified exact expression.
  - Numerical spot-check at z=1, λ_emit=500 nm, N=1 confirms `dObs/dEmit = 2 = (1+z)`.
  - Confirms the SymPy symbolic derivation (Check 02) independently.

---

## TODOs / Known gaps

- **No open verification gaps.** All 5 checks captured live with zero cross-tool disagreement.
- **Conceptual caveats persist** (not verification gaps — see [`caveats.md`](caveats.md)): N is undetermined; polarization is unaddressed; full Maxwell recovery is not done. These are Yellow-tier features of the claim, not verification failures.
