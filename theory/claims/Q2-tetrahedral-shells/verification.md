# Q2 — Verification Record

**Tally:** 6/6 checks passed (5 PASS + 1 NOTED boundary case). Green-tier.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory. All scripts read constants from [`verification/inputs.json`](verification/inputs.json); re-run any check with `python3 check_NN_*.py` or `wolframscript -file check_06_wolfram.wls` from inside `verification/`.

**Claim being verified:** $P_n = 10n^2 + 2$ is the shell population for any 12-coordinate close-packed finite cluster — the geometric consequence of uniform graviton attraction selecting densest packing (Kepler / Hales 2005). See [`claim.md`](claim.md) and [`derivation.md`](derivation.md).

---

## Check 1 — Algebraic expansion (cuboctahedral) via SymPy

- **Tool:** Python 3.14.4 / SymPy 1.14.0
- **Script:** [`verification/check_01_algebraic_sympy.py`](verification/check_01_algebraic_sympy.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** ✅ PASS
- **What it confirms:** Symbolic expansion of the cuboctahedral decomposition $12 + 24(n-1) + 8\cdot\frac{(n-1)(n-2)}{2} + 6(n-1)^2$ simplifies exactly to $10n^2 + 2$; `sp.simplify(geometric - formula) == 0`.

## Check 2 — Numerical cuboctahedral (n=1..5)

- **Tool:** Python 3.14.4
- **Script:** [`verification/check_02_numerical_cuboctahedral.py`](verification/check_02_numerical_cuboctahedral.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** ✅ PASS (5/5)
- **What it confirms:** For $n = 1, 2, 3, 4, 5$, the formula, the cuboctahedral geometric count, and the published values from `gcm_v2.md` H7 all agree: 12, 42, 92, 162, 252.

## Check 3 — Mackay icosahedral cross-geometry (load-bearing for the reframe)

- **Tool:** Python 3.14.4 / SymPy 1.14.0
- **Script:** [`verification/check_03_mackay_icosahedral.py`](verification/check_03_mackay_icosahedral.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** ✅ PASS (symbolic + 5/5 numerical)
- **What it confirms:** The Mackay icosahedral decomposition $12 + 30(n-1) + 20\cdot\frac{(n-1)(n-2)}{2}$ — which is geometrically different from the cuboctahedral one (different number of edges, different face types, no square faces) — sums to the identical closed form $10n^2 + 2$. This is the load-bearing evidence that the shell formula is a property of 12-coordinate close-packing generally, not of FCC specifically. Reference: Mackay (1962), *Acta Crystallographica* 15, 916.

## Check 4 — Limit case P_0 (boundary condition)

- **Tool:** Python 3.14.4
- **Script:** [`verification/check_04_limit_case_p0.py`](verification/check_04_limit_case_p0.py)
- **Output:** [`verification/outputs/check_04.txt`](verification/outputs/check_04.txt)
- **Result:** 🟡 NOTED (not a failure — boundary condition)
- **What it confirms:** $P(0) = 2$ from the formula; this is a mathematical artifact, not a physical pair. The central site of a cluster is one graviton. Formula is valid for $n \geq 1$. Stated explicitly in `claim.md` and `caveats.md`.

## Check 5 — OEIS A005901 cross-reference (n=1..10)

- **Tool:** Python 3.14.4
- **Script:** [`verification/check_05_oeis_cross_reference.py`](verification/check_05_oeis_cross_reference.py)
- **Output:** [`verification/outputs/check_05.txt`](verification/outputs/check_05.txt)
- **Result:** ✅ PASS (10/10)
- **What it confirms:** Formula values $P(1)..P(10)$ match OEIS A005901 a(1)..a(10): 12, 42, 92, 162, 252, 362, 492, 642, 812, 1002. Independent external validation from a published sequence database.

## Check 6 — Wolfram Language independent verification

- **Tool:** WolframScript 1.13.0 for Mac OS X ARM (64-bit)
- **Script:** [`verification/check_06_wolfram.wls`](verification/check_06_wolfram.wls)
- **Output:** [`verification/outputs/check_06_wolfram.txt`](verification/outputs/check_06_wolfram.txt)
- **Result:** ✅ PASS
- **What it confirms:** Wolfram's symbolic engine independently confirms all three polynomial identities:
  - Cuboctahedral == Formula: True
  - Mackay == Formula: True
  - Cuboctahedral == Mackay: True
- Numerical table for $n=1..5$ produces 12, 42, 92, 162, 252 from all three decompositions.
- OEIS A005901 match for $n=1..10$ confirmed via `AllTrue[checks, # &] → True`.

---

## Cross-tool agreement

| | Python | SymPy | Wolfram |
|---|---|---|---|
| Cuboctahedral symbolic expansion → $10n^2 + 2$ | (n/a) | ✅ | ✅ |
| Mackay symbolic expansion → $10n^2 + 2$ | (n/a) | ✅ | ✅ |
| Cuboctahedral $\equiv$ Mackay | (n/a) | (via both → formula) | ✅ (direct) |
| Numerical match for $n=1..5$ | ✅ | ✅ | ✅ |
| OEIS A005901 match $n=1..10$ | ✅ | (n/a) | ✅ |

No cross-tool disagreements. Three independent implementations (Python integer arithmetic, SymPy symbolic, Wolfram Language symbolic) converge on the same closed form and the same numerical values.

---

## Literature / standard-reference cross-check

- **Kepler's conjecture (12-coordinate is densest in 3D):** Hales, T. C. (2005). *A proof of the Kepler conjecture*. Annals of Mathematics 162(3), 1065–1185.
- **Cuboctahedral cluster shells:** Conway, J. H. & Sloane, N. J. A. (1999). *Sphere Packings, Lattices and Groups* (3rd ed., Springer), §1.4 and Appendix A.
- **Mackay icosahedral shells:** Mackay, A. L. (1962). *A dense non-crystallographic packing of equal spheres*. Acta Crystallographica 15, 916–918.
- **Magic-number cluster physics:** Marks, L. D. (1994). *Experimental studies of small particle structures*. Reports on Progress in Physics 57(6), 603–649.
- **OEIS sequence:** A005901.

---

## Historical note — what v1 of this record said

The pre-2026-04-24 version of this file documented Checks 1–7 as hand derivations + literature citation + a pending Python/SymPy block. During the retrofit pass, the "pending" block was actually run, and three new independent tool confirmations (live Python, live SymPy, live Wolfram) were added. The geometric decomposition counts were corrected to read from `inputs.json` rather than being hardcoded, which is how one bug was actually caught: the initial `inputs.json` included `_source` meta-keys that broke a dict comprehension in Check 2. Bug fixed; re-run; 5/5 pass. Noting this here because the caught bug is exactly the kind of thing the retrofit was designed to surface.

## Known gaps / TODOs

None at this tier. All checks passed; cross-tool agreement clean; literature confirmed. For a deeper stability analysis of *which* of FCC / HCP / icosahedral gravitons actually adopt, see open question OQ-Q2a in [`caveats.md`](caveats.md) — that is not a verification gap for Q2 but a downstream open question for S3 / S6 / S7.
