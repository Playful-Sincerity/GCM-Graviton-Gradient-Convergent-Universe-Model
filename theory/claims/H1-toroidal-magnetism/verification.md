# H1 — Verification Record

**Tally:** 3/3 runnable checks passed. 2 structural/topological arguments stated but intentionally not runnable. UNSPEC-4 (exact Lorentz force / Maxwell) remains open by design.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory.

---

## Claim Summary

H1 is a **plausibility sketch**. The only runnable mathematical content is:
1. Dimensional algebra of the proposed $(\nabla\cdot J_g)\cdot v \to$ Tesla coupling.
2. Vector-calculus structure of the radial + uniform superposition (stagnation point, curl).

Two of the previously-listed "qualitative passes" (right-hand-rule sign and monopole-absence topology) are *geometric / topological arguments*, not computations. They are discussed in [`derivation.md`](derivation.md) and retained there, but no script can meaningfully verify them without recapitulating the argument in code.

The UNSPEC-4 items (exact Lorentz force reproduction, Maxwell's equations) are explicitly out of scope. No check is attempted; they remain open.

---

## Check 01 — Dimensional analysis (SymPy + manual SI-exponent tracking)
- **Tool:** Python 3.14.4 / SymPy 1.14.0 `physics.units` + parallel manual exponent tracking
- **Script:** [`verification/check_01_dimensional_sympy.py`](verification/check_01_dimensional_sympy.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** Confirms $(\nabla\cdot J_g)\cdot v$ has units $\text{kg}/(\text{m}^2\cdot\text{s}^2) = \text{N}/\text{m}^3$ (force per unit volume). Coupling constant needed to reach Tesla $\text{kg}/(\text{A}\cdot\text{s}^2)$ must have units $\text{m}^2/\text{A}$. Script also explicitly verifies that the pre-audit draft's $\text{m}^2\cdot\text{A}$ coupling does NOT produce Tesla (current exponent +1 instead of −1) — confirming yesterday's dimensional fix was correct.

## Check 02 — Radial + uniform superposition structure (SymPy `sympy.vector`)
- **Tool:** SymPy 1.14.0 `sympy.vector` (CoordSys3D, `curl`, `divergence`)
- **Script:** [`verification/check_02_streamlines_sympy.py`](verification/check_02_streamlines_sympy.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS (three sub-checks: curl of radial piece, curl of uniform piece, curl of superposition, stagnation point on $-\hat{z}$ axis)
- **Notes + HONESTY FINDING:** Both sub-fields are irrotational, so the superposition is irrotational. The claimed "toroidal streamlines" are topological (Rankine-half-body geometry with a stagnation point at $z^* = -\sqrt{q/v_0}$), NOT rotational. This sharpens UNSPEC-4: producing a magnetic field with non-zero $\nabla\times\mathbf{B}$ matching Ampère-Maxwell requires the **time-dependent oscillation dynamics**, not just static vector-field superposition. The "toroidal geometry is necessary but not sufficient" statement has become more specific as a result of this check.

## Check 03 — Wolfram Engine independent cross-check
- **Tool:** Wolfram Language Engine 14.3.0 (local `wolframscript`)
- **Script:** [`verification/check_03_wolfram.wls`](verification/check_03_wolfram.wls)
- **Output:** [`verification/outputs/check_03_wolfram.txt`](verification/outputs/check_03_wolfram.txt)
- **Result:** PASS (three sub-checks: dimensional exponent algebra; `Curl[F_total, {x,y,z}] == {0,0,0}`; stagnation-point solve returns $z = \pm\sqrt{q/v_0}$, with the negative root being the expected stagnation point)
- **Notes:** Wolfram's `Curl` confirms SymPy's zero-curl result. Solve finds both roots; assumptions-based simplification confirms the negative root matches $-\sqrt{q/v_0}$.

**Cross-tool agreement:** SymPy and Wolfram agree exactly on all three shared claims (curl = 0, stagnation point, coupling-exponent algebra). No cross-tool disagreement.

---

## Structural / Topological Claims NOT Verified by Script

These are discussed in [`derivation.md`](derivation.md) and [`claim.md`](claim.md). They are stated as geometric arguments — a script would be a restatement of the argument in code, not an independent check.

### Right-hand-rule sign convention
Given a positive charge ($\nabla\cdot J_g < 0$, net inflow) moving in $+\hat{z}$, the circulation around the motion axis matches the right-hand rule. This is a sign-convention argument — the natural composition of inflow + $+\hat{z}$ drift produces counterclockwise rotation (viewed from $+\hat{z}$), which IS the right-hand rule sense for positive charges. No script adds clarity beyond the geometric argument.

### Monopole absence
GCM's mechanism produces *toroidal* fields (closed field lines around a motion axis). A magnetic monopole would require a purely radial field $\mathbf{B} \propto \hat{r}/r^2$ — but in GCM's picture, the radial component is already identified with the electric-field-like flow $\nabla\cdot J_g$. There is no topological room in the mechanism for a separate "radial B" mode. This is a structural argument, not a computation.

---

## Open Gaps (UNSPEC-4, UNSPEC-5, other)

Unchanged by this retrofit:
- **Lorentz force $F = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ exact reproduction — UNSPEC-4, open.**
- **Maxwell's equations derivation from graviton-substrate dynamics — open.**
- **Value of $c$ from graviton parameters — OQ-3, open.**
- **Value of $e$ from flow-asymmetry strength — open.**
- **Preon failure modes (hypercolor, wrong masses) — open.**

Check 02's honesty finding adds a **more specific** statement of UNSPEC-4: the oscillation dynamics (time-dependent curl generation) are what's missing, not just "some unspecified mechanism." This gives future work a clearer target.

---

## Running the Full Suite

```bash
cd verification
../../_verification-env/venv/bin/python check_01_dimensional_sympy.py  | tee outputs/check_01.txt
../../_verification-env/venv/bin/python check_02_streamlines_sympy.py  | tee outputs/check_02.txt
wolframscript -file check_03_wolfram.wls                               | tee outputs/check_03_wolfram.txt
```

Dimensional-algebra inputs (unit dependencies) live in [`verification/inputs.json`](verification/inputs.json).
