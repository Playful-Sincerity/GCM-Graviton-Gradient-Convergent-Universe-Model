# E1 — Charge as Graviton-Flow Asymmetry

**Claim code:** E1 (Section S3, GCM Coherence Case)
**Epistemic tier:** 🟡 Yellow hypothesis — scaffold only, no derivation attempted
**Date:** 2026-04-23
**Session:** C (Unification Mechanics)

---

## Statement

Electric charge, under GCM, is a macroscopic label for the **net divergence of graviton-number current** in a particle's density gradient. The three charge-type categories map to three divergence states:

| Particle type | Divergence of graviton current | Intuition |
|---|---|---|
| Electron (negative charge) | $\nabla\cdot\mathbf{J}_g > 0$ (**net outflow**) | density decreases toward the center — the particle "sheds" gravitons outward |
| Proton (positive charge) | $\nabla\cdot\mathbf{J}_g < 0$ (**net inflow**) | density increases toward the center — the particle "absorbs" gravitons inward |
| Neutron (zero net charge) | $\nabla\cdot\mathbf{J}_g = 0$ (**balanced**) | circulatory flow with no net flux |

This is the hypothesis stated as a hypothesis. No derivation is attempted in this claim folder — for structural reasons explained below.

## The minimal flow equation

The graviton-current field $\mathbf{J}_g$ is modeled by a Fokker-Planck-type flow equation balancing **diffusion** against **drift**:

$$\mathbf{J}_g = -D\,\nabla\rho_g + \mathbf{v}_g\,\rho_g$$

where:

- $\rho_g(\mathbf{r},t)$ is the local graviton number (or mass) density,
- $D$ is a diffusion coefficient characterizing the spread of local graviton-density fluctuations,
- $\mathbf{v}_g(\mathbf{r},t)$ is a local drift velocity field — the *direction* in which gravitons, on average, are moving.

The continuity condition for graviton conservation reads
$$\frac{\partial \rho_g}{\partial t} + \nabla\cdot\mathbf{J}_g = 0.$$

For a steady-state particle (the usual case for a stable electron, proton, or neutron), $\partial_t \rho_g = 0$ and the claim reduces to: **the charge of the particle is the steady-state divergence of its graviton current, integrated over the particle's volume.**

## What this does NOT derive

E1 as written is not a derivation. It is a *statement of shape* — what charge would have to be, if it is anything, in GCM's ontology. The unsolved structural question is **why some density configurations produce net $\nabla\cdot\mathbf{J}_g > 0$ while others produce $\nabla\cdot\mathbf{J}_g < 0$**. This is flagged in gcm_v2.md as:

> **UNSPEC-1.** No derivation yet for why electron-type configurations produce net outflow and proton-type produce net inflow. Requires solving $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ for stable configurations.

UNSPEC-1 is the central open problem for E1. Its resolution would require:

1. **A Lagrangian or Hamiltonian for the graviton substrate.** Currently GCM has a minimal-model equation of motion (Newtonian $\ddot{\mathbf{x}}_i = \sum_j Gm_g/r_{ij}^2\,\hat{r}_{ij}$) but no action principle or field-theoretic formulation.
2. **A stability analysis of density configurations.** Given the Lagrangian, which spatial distributions of $\rho_g$ and $\mathbf{v}_g$ are stable steady states? Among stable configurations, which have $\nabla\cdot\mathbf{J}_g > 0$, $< 0$, or $= 0$?
3. **A quantization condition.** The observed fundamental charge $\pm e$ must be a quantized property. This requires either (a) the stability analysis naturally quantizes the net outflow amplitude, or (b) a separate mechanism (shell packing — see Q6) selects specific flow magnitudes as stable. The Q6 hypothesis is that stable tetrahedral/FCC/icosahedral packings quantize the number of "escape channels" for graviton flow; this is plausibility-level and not derived.

None of the three are presently available. Hence E1 is flagged as a scaffolded hypothesis, with `derivation.md` stating only the minimal flow equation, not a derivation of charge.

## Why it still belongs in the coherence paper

The coherence case does not require that every claim be derived; it requires that the pieces fit together. E1's fit is structural:

- **Compatibility with T2 (gravity as the only fundamental force).** If charge is not an independent property but a consequence of graviton-flow asymmetry, then "electromagnetism" is not a separate force — it is a pattern in the gravitational substrate. This is required for GCM's unification program.
- **Compatibility with T4 (all existence is dimensions of change).** Charge-as-flow-divergence is exactly "a dimension of change" in the graviton density. It is not a static property painted on top of the density; it is *what the density is doing over time*.
- **Compatibility with H2 (charge flow direction) in gcm_v2.md.** Already stated there; E1 sharpens the formulation by making the flow equation explicit.

## Scope of the claim (intentionally modest)

E1 commits only to the following:

1. The divergence triple $\{>\!0, <\!0, =\!0\}$ of $\nabla\cdot\mathbf{J}_g$ maps to the charge triple $\{\text{negative}, \text{positive}, \text{neutral}\}$.
2. A minimal Fokker-Planck-type flow equation $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ is the simplest structure consistent with this.
3. Steady-state particles have time-independent $\rho_g$ distributions, which by the continuity equation means spatially-varying $\nabla\cdot\mathbf{J}_g$.
4. The hypothesis is sign-correct with the electron/proton/neutron phenomenology: electrons "want to shed" (outflow), protons "want to absorb" (inflow), neutrons are balanced.

It does **not** commit to:

- Any specific mechanism by which an electron-like configuration produces net outflow.
- A derivation of $\pm e$ as the quantized magnitude.
- A derivation of fractional charges (quarks). UNSPEC-2 in gcm_v2.md.
- The relationship between $\mathbf{J}_g$ and observed electric field $\mathbf{E}$.

## Relationship to other claims

- **E2 (competing attraction).** E2's toy model treats electrons as point masses with no flow structure. Including E1's flow asymmetry would add sub-particle detail that the 1D two-body toy model ignores. The macroscopic result (repulsion) is unchanged; the microscopic mechanism (flow divergence) is what E1 posits.
- **Q6 (discrete charge from stable shells).** Q6 claims shell-packing geometry produces discrete charge magnitudes. E1 provides the field-level description of what "charge" even *is* in terms of graviton flow. Q6 and E1 are complementary: Q6 says "packings are stable"; E1 says "stable packings with net outward flow are what we call electrons."
- **H4 (magnetism from toroidal alignment).** Magnetism requires moving charge. In E1's language, a moving electron is a spatially-translated flow-divergence configuration. H4 states the aligned-toroidal-oscillation picture; E1 underlies it by specifying what the oscillation is *of* (the graviton current field $\mathbf{J}_g$).

## Verification stack (CC-7)

- ✅ Dimensional analysis of $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ (see `verification.md`)
- ✅ Sign-consistency check with phenomenology (electron outflow, proton inflow, neutron balanced)
- ⚠️ No derivation of the flow equation from a first-principles action — flagged as future work (UNSPEC-1)
- ⚠️ No quantization: why $\pm e$ specifically? (UNSPEC-2, quark fractional charges)

See `derivation.md` for the flow-equation statement, `verification.md` for the dimensional check, and `caveats.md` for the structural gap.
