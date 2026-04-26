# S5.5 — Verification Record

**Tally:** 4/4 runnable checks passed for sub-claim (a); (b) and (c) are framing claims with no runnable numerics.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory.

---

## Sub-claim (a) — Newtonian Gravity as a Limit — 🟢 Green

Four independent checks confirm $F = G m_1 m_2 / r^2$ emerges cleanly from the minimal-model sum. mpmath (50 digits) and Wolfram Engine (symbolic + numerical) agree to ~15 significant figures; SymPy confirms the symbolic factorization and limit behaviour.

### Check 01 — Dimensional analysis
- **Tool:** SymPy `physics.units` + manual SI base-unit exponent tracking
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS — both methods agree; product $[G \cdot m^2 / r^2]$ reduces to $(m^1, kg^1, s^{-2}) = $ Newton.

### Check 02 — Earth-Moon numerical (mpmath, 50-digit precision)
- **Tool:** Python 3.14.4 / mpmath 1.3.0, dps=50
- **Script:** [`verification/check_02_earth_moon_numerical.py`](verification/check_02_earth_moon_numerical.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS — $F = 1.98056 \times 10^{20}$ N; 0.028% relative deviation from textbook reference ($1.98 \times 10^{20}$ N). Within 1% tolerance; the deviation traces to reference-value rounding.

### Check 03 — Symbolic limit cases (SymPy)
- **Tool:** SymPy 1.14.0 `limit()`, `Symbol`, `simplify`
- **Script:** [`verification/check_03_limit_cases_sympy.py`](verification/check_03_limit_cases_sympy.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS — all five sub-checks pass:
  - $\lim_{r\to\infty} F = 0$ ✓
  - $\lim_{m_1\to 0} F = 0$ and $\lim_{m_2\to 0} F = 0$ ✓
  - Single-graviton substitution ($\xi_A = \xi_B = 1$) recovers $F = G m_g^2 / r^2$ ✓
  - Factorization $G \cdot (m_g \xi_A)(m_g \xi_B) / r^2 \equiv G \xi_A \xi_B m_g^2 / r^2$ verified symbolically (this is the load-bearing algebraic step of the derivation)

### Check 04 — Wolfram Engine independent verification
- **Tool:** Wolfram Language Engine 14.3.0 (local `wolframscript`)
- **Script:** [`verification/check_04_wolfram.wls`](verification/check_04_wolfram.wls)
- **Output:** [`verification/outputs/check_04_wolfram.txt`](verification/outputs/check_04_wolfram.txt)
- **Result:** PASS — $F = 1.9805585650280287 \times 10^{20}$ N (agrees with mpmath to the 15th significant digit; discrepancy at that level is double-precision rounding in the Wolfram literal). Symbolic limits match SymPy; factorization matches.

**Cross-tool agreement (a):** mpmath 50-dp and Wolfram 14.3 agree numerically to 15+ digits. SymPy and Wolfram agree symbolically on all five limit/factorization checks. No cross-tool disagreement.

---

## Sub-claim (b) — Special Relativity as Graviton-Density-Wave Propagation — 🟡 Yellow (framing)

No runnable numerical checks exist for this sub-claim — it is a consistency argument invoking Robertson (1949), not a derivation. See [`b-special-relativity.md`](b-special-relativity.md) for the structural argument.

**What the verification narrative in [`b-special-relativity.md`](b-special-relativity.md) asserts:**
- Robertson (1949) derivation is standard — ✓ citation verified bibliographically.
- Minimal-model equation is Galilean-covariant — can be inspected directly in the equation; no computation needed.
- Michelson-Morley compatibility — conceptual argument about substrate structure.
- Deriving $c$ from GCM parameters, substrate light-cone, $E = mc^2$ from dynamics — all ⏳ OPEN (OQ-3).

**TODO / open gaps:**
- Add a short Robertson-sketch derivation (half-page) as a conceptual appendix. Conceptual-only, but would firm up the citation dependence.
- When GCM eventually derives $c$ from graviton dynamics (OQ-3), a numerical verification script comparing the derived value against the defined SI $c$ becomes possible.

---

## Sub-claim (c) — Local Realism via Superdeterminism — 🟡 Yellow (framing)

No runnable numerical checks — framing only. See [`c-local-realism.md`](c-local-realism.md).

**What the verification narrative asserts:**
- Superdeterminism is a recognized Bell-escape — bibliographically verified ('t Hooft 2016 Springer; Hossenfelder 2020 *Frontiers in Physics*).
- GCM's minimal-model equation is deterministic — inspection of the equation suffices.
- GCM does not derive quantum correlations — ⏳ OPEN, and acknowledged as red-tier.

**TODO / open gaps:**
- No runnable check is meaningful until GCM has a theory of what quantum "states" are in graviton terms. That belongs to a different research phase.

---

## Running the Full Suite

From this directory:

```bash
cd verification
../../_verification-env/venv/bin/python check_01_dimensional.py          | tee outputs/check_01.txt
../../_verification-env/venv/bin/python check_02_earth_moon_numerical.py | tee outputs/check_02.txt
../../_verification-env/venv/bin/python check_03_limit_cases_sympy.py    | tee outputs/check_03.txt
wolframscript -file check_04_wolfram.wls                                 | tee outputs/check_04_wolfram.txt
```

Each script reads constants from [`verification/inputs.json`](verification/inputs.json); no values are hardcoded in the scripts.

---

## Overall Status for S5.5

| Sub-claim | Tier | Runnable checks | Cross-tool verified | Open gaps |
|---|---|---|---|---|
| (a) Newtonian limit | 🟢 Green | 4/4 pass | Yes (mpmath + SymPy + Wolfram agree) | None |
| (b) SR consistency | 🟡 Yellow (framing) | N/A | Citation-level only | OQ-3: derive $c$ from graviton dynamics |
| (c) Local realism + superdeterminism | 🟡 Yellow (framing) | N/A | Citation-level only | Quantitative Bell correlations from GCM dynamics |

No overclaim. No cross-tool disagreement. The fourth-IVNA-layer gap previously flagged in `a-newtonian-limit.md` is now closed by Wolfram Engine independent verification.
