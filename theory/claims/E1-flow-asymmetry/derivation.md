# E1 — Scaffold: The Minimal Flow Equation

This file states the flow equation as cleanly as we can, and names what derivation would be required to upgrade E1 beyond hypothesis status. No derivation is performed.

## The flow equation

Let $\rho_g(\mathbf{r},t)$ be the local graviton density (units: kg/m³ or graviton number per m³ — convention fixed per gcm_v2 Appendix). Let $\mathbf{J}_g(\mathbf{r},t)$ be the graviton current density (mass flux or number flux per unit area per unit time). Posit the relation
$$\mathbf{J}_g(\mathbf{r},t) = -D\,\nabla\rho_g(\mathbf{r},t) + \mathbf{v}_g(\mathbf{r},t)\,\rho_g(\mathbf{r},t)$$
where
- $D$ [m²/s] is a diffusion coefficient describing local graviton-density spreading by random fluctuations about the mean configuration.
- $\mathbf{v}_g(\mathbf{r},t)$ [m/s] is a local drift velocity field, representing the mean flow direction of the graviton substrate at $(\mathbf{r}, t)$.

This is the **Fokker-Planck form** familiar from Brownian-motion theory, applied to the graviton substrate. The two terms are:

- $-D\,\nabla\rho_g$: **diffusive** current flowing from high-density to low-density regions.
- $\mathbf{v}_g\,\rho_g$: **drift** current carrying density along the flow lines of $\mathbf{v}_g$.

Continuity (graviton-number conservation):
$$\frac{\partial\rho_g}{\partial t} + \nabla\cdot\mathbf{J}_g = 0.$$

## Divergence identities

$$\nabla\cdot\mathbf{J}_g = -D\,\nabla^2\rho_g + \nabla\cdot(\mathbf{v}_g\rho_g) = -D\,\nabla^2\rho_g + \rho_g\,\nabla\cdot\mathbf{v}_g + \mathbf{v}_g\cdot\nabla\rho_g.$$

For a **steady-state particle** ($\partial_t\rho_g = 0$), continuity forces $\nabla\cdot\mathbf{J}_g = 0$ *everywhere*. This is crucial: in a strict steady state, the current is divergence-free.

## The apparent paradox and its resolution

The hypothesis says "electrons have $\nabla\cdot\mathbf{J}_g > 0$" while steady-state continuity says "$\nabla\cdot\mathbf{J}_g = 0$ everywhere." These appear contradictory.

Resolution: the hypothesis refers to the divergence **as felt by the external substrate**, not to the divergence within the particle's core. A steady-state electron maintains internal continuity ($\nabla\cdot\mathbf{J}_g = 0$ internally) by cycling gravitons, but the time-averaged *flux* of gravitons crossing a surface surrounding the electron is non-zero — the electron acts as a **source** of outgoing graviton current in the far-field substrate. This is closely analogous to a steady-state plasma "source" in hydrodynamics (fluid element produces no net fluid internally, but emits fluid into the surrounding medium by some mechanism).

Formally: for a spherical surface $S$ enclosing the electron, the surface integral
$$\Phi_g \equiv \oint_S \mathbf{J}_g \cdot d\mathbf{A} > 0 \quad \text{for electron-type configurations.}$$
Similarly, $\Phi_g < 0$ for protons and $\Phi_g = 0$ for neutrons.

The quantized values $\Phi_g = \pm e'$ (for some constant $e'$ with units of current or graviton-flux) would then map to $\pm e$ electric charge by the relation "electric charge = $c$ × graviton-flux" for some conversion constant $c$ with units $[e]/[e']$.

This reformulation is cleaner and avoids the apparent paradox. It also makes the quantization question sharper: **what selects $\pm e'$ as the only allowed flux magnitudes for stable particles?** That is UNSPEC-1 in its precise form.

## What E1 is actually providing

1. **A functional form for the flow.** The Fokker-Planck-type equation is the minimal structure that allows both diffusion (spreading) and directed flow.
2. **A sign triple.** The three charge states map to $\Phi_g > 0, < 0, = 0$.
3. **A continuity constraint.** Steady-state particles have divergence-free internal currents but non-zero far-field graviton fluxes.
4. **A precise open problem statement.** The quantization of $\Phi_g$ to $\pm e'$ is UNSPEC-1, and requires further machinery.

## What would be needed for a derivation

To move E1 from yellow to green, one would need at minimum:

**Step 1 — An action principle for the graviton substrate.** Write down a Lagrangian $\mathcal{L}[\rho_g, \mathbf{J}_g]$ or $\mathcal{L}[\phi]$ (for a field $\phi$ whose density and current are the observables) whose Euler-Lagrange equations yield the flow equation above *as a consequence*, not as an assumption. Candidate forms include:
- Scalar-field theory for $\rho_g$ with coupled velocity field.
- Hydrodynamic action integrating density and velocity fields.
- Field-theoretic Lagrangian treating $\rho_g$ as a scalar condensate.

**Step 2 — A stability analysis.** Given the action, solve for steady-state solutions corresponding to bound particles. A stable electron would be a localized density profile with non-zero outward flux $\Phi_g > 0$. The stability requires balance between (a) attraction of the local cluster gravitons toward each other, (b) maintenance of the outflow, (c) interaction with the ambient substrate.

**Step 3 — A quantization mechanism.** The analysis must show that only discrete flux amplitudes correspond to stable configurations. Candidate mechanisms:
- Topological charge (analogous to skyrmion winding number in condensed matter).
- Shell-packing stability (Q6 ansatz — only specific closed tetrahedral/icosahedral packings are stable, producing discrete charge).
- Resonance with the substrate (only certain oscillation modes match the substrate's natural frequencies).

Until all three steps are done, E1 is a scaffold, not a derivation.

## Scope honesty

E1 does not derive:
- The numerical value of $e' = e/c$.
- Why the fractional charges of quarks ($\pm 1/3, \pm 2/3$) exist, or why they are confined.
- The connection to Maxwell's equations (how the flow field $\mathbf{J}_g$ couples to observed electromagnetic fields).
- Parity violation in weak interactions (scalar graviton current has no handedness).

The last point is particularly worth flagging: a scalar flow field cannot intrinsically distinguish left- from right-handedness, so the chirality observed in weak decays must emerge from geometric configurations of stable particles, not from the flow itself. This is the parity-violation wall named in S8, and E1 does not help cross it.

## Dimensional self-check

$[D] = \mathrm{m^2 s^{-1}}$ (diffusion coefficient).
$[\nabla\rho_g] = \mathrm{kg\,m^{-4}}$ if $\rho_g$ is mass density.
$[-D\nabla\rho_g] = \mathrm{m^2 s^{-1}}\cdot\mathrm{kg\,m^{-4}} = \mathrm{kg\,m^{-2}\,s^{-1}}$. ✅ matches mass flux.

$[\mathbf{v}_g] = \mathrm{m\,s^{-1}}$.
$[\mathbf{v}_g\rho_g] = \mathrm{m\,s^{-1}}\cdot\mathrm{kg\,m^{-3}} = \mathrm{kg\,m^{-2}\,s^{-1}}$. ✅ matches mass flux.

$[\mathbf{J}_g] = \mathrm{kg\,m^{-2}\,s^{-1}}$. ✅

Both terms have the same units; the equation is dimensionally consistent. The units check in `verification.md`.
