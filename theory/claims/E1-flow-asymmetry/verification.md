# E1 — Verification Record

**Tally:** 5/5 checks passed.
**Last run:** 2026-04-24
**Reproducible:** Yes — see [`verification/`](verification/) directory. Constants in [`verification/inputs.json`](verification/inputs.json).

## Result summary

E1 is a hypothesis scaffold, not a quantitative prediction. The verification stack establishes:

- **Dimensional consistency** of $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ — every term has mass-flux units (kg/m²/s); the continuity equation is dimensionally closed.
- **Sign consistency** of the three-way charge mapping ($\mathrm{div}\mathbf{J}_g > 0 \Leftrightarrow$ negative charge, etc.) across five particle species (electron/proton/neutron/positron/antiproton).
- **Divergence identity** $\mathrm{div}\mathbf{J}_g = -D\nabla^2\rho_g + \rho_g\,\mathrm{div}\mathbf{v}_g + \mathbf{v}_g\cdot\nabla\rho_g$ verified symbolically by SymPy and Wolfram Engine independently.
- **Vlasov specialization** ($D = 0$ case) shown to be a clean limit; this addresses the open question surfaced in Session C about whether GCM's deterministic substrate permits a Fokker-Planck (diffusive) form.
- **Toy-model source-like flow** $\mathbf{v}_g = (A/r^2)\hat{\mathbf{r}}$ with constant $\rho_g$: div vanishes in the bulk, surface flux $\Phi_g = 4\pi\rho_0 A$ is $R$-independent — the formal shape of a "source-like" steady-state particle.

What the stack does NOT verify — intentionally — is the *existence* of stable graviton-density configurations producing the required flow divergences. That is UNSPEC-1, the central open problem for E1, and is future work.

## Per-check detail

### Check 01 — Dimensional analysis of $\mathbf{J}_g$ and continuity
- **Tool:** Python + Pint 0.25
- **Script:** [`verification/check_01_dimensional.py`](verification/check_01_dimensional.py)
- **Output:** [`verification/outputs/check_01.txt`](verification/outputs/check_01.txt)
- **Result:** PASS
- **Notes:** Both $-D\nabla\rho_g$ and $\mathbf{v}_g\rho_g$ have units of kg/m²/s. $\partial\rho/\partial t$ and $\nabla\cdot\mathbf{J}_g$ both have units of kg/m³/s (continuity closed). Surface flux $\Phi_g$ has units of kg/s.

### Check 02 — Sign consistency with electron/proton/neutron phenomenology
- **Tool:** Python + SymPy 1.14
- **Script:** [`verification/check_02_sign_consistency.py`](verification/check_02_sign_consistency.py)
- **Output:** [`verification/outputs/check_02.txt`](verification/outputs/check_02.txt)
- **Result:** PASS
- **Notes:** Three-way mapping (div>0↔negative charge, div<0↔positive, div=0↔neutral) cross-checked against five particle species including antiparticles. Toy radial flow $\mathbf{v}_g = (A/r^2)\hat{\mathbf{r}}$: div vanishes in bulk, surface flux = $4\pi\rho_0 A$ (R-independent, source-like). Both results computed in spherical coordinates by SymPy.

### Check 03 — Symbolic divergence of $\mathbf{J}_g$ (SymPy vector calculus)
- **Tool:** SymPy 1.14 + `sympy.vector`
- **Script:** [`verification/check_03_sympy_divergence.py`](verification/check_03_sympy_divergence.py)
- **Output:** [`verification/outputs/check_03.txt`](verification/outputs/check_03.txt)
- **Result:** PASS
- **Notes:** Verifies the identity $\mathrm{div}\mathbf{J}_g = -D\nabla^2\rho_g + \rho_g\,\mathrm{div}\mathbf{v}_g + \mathbf{v}_g\cdot\nabla\rho_g$ symbolically for generic $\rho_g(x,y,z)$ and $\mathbf{v}_g(x,y,z)$. Difference simplifies to 0.

### Check 04 — Fokker-Planck vs Vlasov consistency
- **Tool:** SymPy 1.14 + `sympy.vector`
- **Script:** [`verification/check_04_fp_vs_vlasov.py`](verification/check_04_fp_vs_vlasov.py)
- **Output:** [`verification/outputs/check_04.txt`](verification/outputs/check_04.txt)
- **Result:** PASS
- **Notes:** Demonstrates $\mathbf{J}_{FP}|_{D=0} = \mathbf{J}_V$ componentwise. Computes the identity $\mathrm{div}\mathbf{J}_V = \rho_g\,\mathrm{div}\mathbf{v}_g + \mathbf{v}_g\cdot\nabla\rho_g$. Shows that $\mathrm{div}\mathbf{J}_{FP} - \mathrm{div}\mathbf{J}_V = -D\nabla^2\rho_g$ — the only formal distinction. Key take-away: **E1's sign-level claim is preserved whether we use FP or Vlasov**; the drift field $\mathbf{v}_g$ alone can set $\mathrm{div}\mathbf{J}_g$'s sign. Recommendation (captured in caveats.md): revise to Vlasov form for GCM's deterministic substrate.

### Check 05 — Wolfram Engine cross-verification
- **Tool:** Wolfram Engine via `wolframscript`
- **Script:** [`verification/check_05_wolfram.wls`](verification/check_05_wolfram.wls)
- **Output:** [`verification/outputs/check_05_wolfram.txt`](verification/outputs/check_05_wolfram.txt)
- **Result:** PASS
- **Notes:** All five `Match` tests return True: (a) the main divergence identity, (b) toy radial flow has zero bulk divergence, (c) surface flux equals $4\pi\rho_0 A$, (d) Vlasov divergence identity, (e) F-P minus Vlasov equals $-D_g\nabla^2\rho_g$. Retrofit caught a real Mathematica bug: underscores in variable names (`divJ_spherical`, `Phi_simp`) are pattern delimiters in Mathematica — the assignments silently failed on the first pass. Fixed by renaming to `divSph`, `PhiSimp`, `Dg`, etc.

## Cross-tool agreement

- SymPy 1.14 and Wolfram Engine agree on the divergence identity symbolically (both give zero difference after `FullSimplify`).
- SymPy and Wolfram agree on the toy-model flow vanishing in the bulk and giving $4\pi\rho_0 A$ over a sphere.
- Both CAS tools agree on the F-P/Vlasov difference being exactly $-D_g\nabla^2\rho_g$.

No tool disagreements.

## Honesty flags — what this verification does NOT confirm

1. **UNSPEC-1 remains open.** The verification does not derive which graviton density configurations correspond to stable electron-like ($\mathrm{div}\mathbf{J}_g > 0$) or proton-like ($\mathrm{div}\mathbf{J}_g < 0$) patterns. That requires an action principle + stability analysis that GCM doesn't yet have.

2. **Quantization unaddressed.** The mapping from graviton-flux magnitude to $\pm e$ (electron charge quantum) is not checked. Q6 (discrete shells) is the candidate quantization mechanism; E1 + Q6 form a yellow pair, not a green derivation.

3. **Fractional quark charges (UNSPEC-2) not addressed.** Would require mechanism for $\pm 1/3, \pm 2/3$ of the electron flux.

4. **No coupling to observed EM fields.** How $\mathbf{J}_g$ sources observed $\mathbf{E}, \mathbf{B}$ is not verified — requires work beyond E1's scope.

5. **The Vlasov recommendation is made but not adopted.** Check 04 recommends revising E1's canonical form from Fokker-Planck to Vlasov for T1-T4 consistency. The coherence paper draft should incorporate this.

## Tier assignment

- **🟡 Yellow** for the hypothesis scaffold: flow equation dimensionally consistent, sign mapping self-consistent with phenomenology, toy source-like example demonstrates mathematical shape.
- **🔴 UNSPEC-1 stays red** at the derivation level: no theoretical path yet from T1-T4 to an electron-shaped stable configuration with outward graviton flux.
- **🔴 UNSPEC-2 stays red:** quark fractional charges.

Overall: E1 is a clean yellow-tier scaffold with structural verification complete. Its upgrade to green would require a full GCM action principle and stability analysis — a research program, not a session.

## TODOs / Known gaps

- Wolfram MCP unavailable in this session; Wolfram check ran via local `wolframscript`.
- No script exists for deriving stable density configurations from an action principle (UNSPEC-1). This is a multi-session research program if/when GCM develops an action.
- The caveats.md recommendation to revise the flow equation from Fokker-Planck to Vlasov needs to be reflected in the claim.md and derivation.md before the coherence paper draft.
