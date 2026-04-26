# E1 — Caveats

## What E1 claims, tightly

A hypothesis relating electric charge to the **net divergence of graviton-number current** in a particle's density structure. Three sign states map to three charge phenomenologies (electron / proton / neutron). A minimal flow equation is stated as the simplest form consistent with the hypothesis.

## What E1 does NOT claim

- A derivation of why electron-like configurations have net outward flux and proton-like configurations have net inward flux.
- A derivation of the quantization of charge to $\pm e$.
- A derivation of the fractional charges of quarks.
- A coupling of $\mathbf{J}_g$ to Maxwell's electromagnetic field $\mathbf{E}, \mathbf{B}$.
- A mechanism for weak-interaction parity violation (scalar flow has no intrinsic handedness).
- A quantitative value for the conversion constant between graviton-flux and electric charge.

## Key honest flags

### 1. The diffusion term may be wrong
The Fokker-Planck form $\mathbf{J}_g = -D\nabla\rho_g + \mathbf{v}_g\rho_g$ implicitly assumes stochastic spreading. But GCM's T1 and the minimal model specify deterministic dynamics. For a conservative N-body system, the continuum coarse-grained equation is typically the Vlasov (collisionless) equation
$$\mathbf{J}_g = \mathbf{v}_g\rho_g,$$
not Fokker-Planck. The diffusion term has no place unless a stochastic process is introduced, which GCM's axioms do not include.

**Recommended revision before paper draft:** restate the flow equation as $\mathbf{J}_g = \mathbf{v}_g\rho_g$ (pure drift), with the velocity field $\mathbf{v}_g$ to be determined by the still-open action principle.

### 2. The "flux through surface" picture is not mechanistic
We say electrons have $\Phi_g > 0$ on an enclosing surface. But in a conservative system with no particle creation, what actually happens physically is that gravitons cycle through the electron's structure — they flow in on one side and flow out on another, producing zero *net* transport of graviton number, but perhaps a non-zero net *flow pattern* that distant bodies couple to. This is more like a "charge-like topological feature of the velocity field" than a "source/sink."

This reformulation would require careful explanation. The current E1 language leans on source/sink intuition that may be misleading. The coherence paper should be careful here.

### 3. The link to observed electric charge is unspecified
E1 says "$\Phi_g$ correlates with charge sign," but the *quantitative* relation (how many units of graviton-flux equals one coulomb?) is completely open. Until this is specified, E1 cannot be checked against experimental measurements of charge, only against the sign phenomenology.

### 4. Parity violation
A scalar flow field (where $\mathbf{v}_g$ is an ordinary 3-vector with no handedness) cannot produce the chiral asymmetry observed in weak interactions. This is the wall named in S8. E1 does not attempt to cross it. The expectation is that parity violation requires *geometric* chirality in stable particle configurations (left-handed vs. right-handed graviton packings), not anything in the flow field itself.

### 5. Quantization
Discrete charge magnitudes ($\pm e$ for leptons and ordinary baryons, $\pm e/3, \pm 2e/3$ for quarks) must arise from *some* mechanism. E1 does not provide it. Q6 (discrete-charge from stable shells) is the candidate companion claim, but Q6 itself is plausibility-level and not derived. Together, E1 + Q6 are still a yellow pair, not a green derivation.

## Relationship to other GCM claims

- **Q6 (discrete charge from stable packings).** Q6 argues that stable tetrahedral/icosahedral/FCC packings produce discrete charge magnitudes. E1 provides the *field description* of what "charge" *is* (flow divergence). If Q6's stability argument succeeds, it gives E1 a quantization mechanism. Both need development.
- **H2 (gcm_v2.md).** E1 is essentially H2 with the flow equation made explicit. The two should be treated as a pair or unified in the paper.
- **H4 (magnetism from toroidal alignment).** A moving electron = a translating $\mathbf{v}_g$ pattern. H4 needs E1 to even have something to move. Derivation of $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ from the moving-flow picture is UNSPEC-4.

## Where UNSPEC-1 actually lives

UNSPEC-1 (why electron-type configurations produce net outflow) is the largest single open problem for GCM's force-unification project at the sub-particle level. It is orthogonal to the E2/E4 problem (why gravity becomes strong at short range), though the two are related — both require new physics beyond the N-body minimal model.

Solving UNSPEC-1 would require:
1. Writing an action principle for the graviton substrate (currently only an equation of motion exists).
2. Solving the action for stable localized configurations.
3. Showing that among stable configurations, there are two inequivalent types (outflow-dominant and inflow-dominant) with the observed quantized flux magnitudes.

This is a research program, not a session. The coherence paper should name it clearly and leave it for future work.

## Scope honesty for the paper

E1 should appear in the coherence paper as a **structural scaffold**, not as a claim of substance. Suggested text:

> **E1 — Charge from graviton-flow divergence (hypothesis).** GCM posits that electric charge, in its ontology, is a macroscopic label for the net divergence of graviton-current in a particle's density structure. Electrons correspond to configurations with net outward graviton flux through any enclosing surface; protons to net inward flux; neutrons to balanced flow. This is stated at the level of sign phenomenology. A derivation of why specific density configurations produce these flow signs, and why the quantized flux magnitudes map to $\pm e$, requires a GCM action principle and a stability analysis of bound configurations. Both are future work (UNSPEC-1, UNSPEC-2). E1 is listed as yellow-tier.

This sets expectations appropriately. It's a hypothesis with a clear form, explicit open problems, and no dishonest claim of derivation.

## Recommendation

The coherence paper should:

1. Include E1 as a scaffolded hypothesis in S3.
2. Revise the flow equation to Vlasov form (drift only, no diffusion) for T1–T4 consistency.
3. Name UNSPEC-1 and UNSPEC-2 as the open problems.
4. Pair E1 with Q6 in the narrative: the combined (flow description + shell quantization) forms GCM's approach to charge.
5. Not overclaim. E1 is a shape, not a solution.
