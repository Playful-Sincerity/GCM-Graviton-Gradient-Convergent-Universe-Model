# H2 — Release Theory of Heat: Derivation Sketch

**Tier:** 🟡 Yellow — structural argument, not formal derivation.
**Verification level:** Qualitative consistency with standard thermodynamics. No numerical reproduction of equipartition or Planck's law.

---

## Starting Point

GCM's thermal hypothesis (from v2 H5, source notes):

> "Heat is release of light that by Newton's 3rd causes the source to recoil."
> "A completely cold/content particle does not toroidally cycle. Disequilibrium (heat) causes cycling."
> "Seebeck effect, thermoelectric emission, thermoluminescence are more naturally predicted here."

The theoretical primitive: a system is "hot" when its local graviton density $\rho_g$ exceeds the local equilibrium background $\rho_0$. This excess is thermodynamically unstable. The system sheds the excess as photon clusters (graviton-cluster structures traveling at $c$) — that shedding is heat release.

---

## Step 1 — The Directional Divergence Principle

Define the **graviton density flux**:
$$J_g = -D\nabla\rho_g + v_g\rho_g$$

where $D$ is a diffusivity constant (not yet derived from graviton properties — open), and the second term is the convective flow. In a purely diffusive limit:
$$J_g \approx -D\nabla\rho_g$$

The flux points from high to low density — downhill in the density landscape. Heat-carrying photon-cluster releases accompany this flux. This is the **directional divergence principle**: heat flows in the direction of steepest density decrease, not randomly.

**Qualitative check:** In standard thermodynamics, heat flows from high to low temperature. If temperature is monotonically related to local density excess ($T \propto \rho_g - \rho_0$), then the GCM flux direction and the thermodynamic heat-flow direction coincide. ✓

---

## Step 2 — Newton's Law of Cooling

Consider a small system with local density $\rho_g(t)$ embedded in an environment at background density $\rho_0$. The release rate is proportional to the excess:

$$\frac{d\rho_g}{dt} = -\lambda(\rho_g - \rho_0), \quad \lambda > 0$$

This first-order linear ODE has the solution:
$$\rho_g(t) - \rho_0 = (\rho_g^{(0)} - \rho_0)\,e^{-\lambda t}$$

Mapping $T - T_\text{env} \propto \rho_g - \rho_0$ gives:
$$T(t) - T_\text{env} = (T_0 - T_\text{env})\,e^{-\lambda t}$$

which is Newton's law of cooling. The exponential decay is a consequence of the proportional-release assumption ($\frac{d\rho_g}{dt} \propto -\Delta\rho_g$), not a separately postulated law.

**What GCM derives:** the functional form $e^{-\lambda t}$, given the proportional-release assumption.
**What GCM does not derive:** the rate constant $\lambda$ from graviton properties. This would require a model of how photon-cluster release rate scales with local density packing.

---

## Step 3 — Fourier Heat Conduction

In a spatially extended system, the continuity equation for graviton density is:
$$\frac{\partial\rho_g}{\partial t} = -\nabla\cdot J_g = D\nabla^2\rho_g$$

(in the purely diffusive limit, ignoring the release-as-photon-clusters term for the spatial propagation equation). Mapping $\rho_g \propto T$:
$$\frac{\partial T}{\partial t} = \alpha\nabla^2 T$$

This is the Fourier heat equation with $\alpha = D$ (treating diffusivity as the thermal diffusivity). The heat flux $\mathbf{q} = -\kappa\nabla T$ follows from $J_g = -D\nabla\rho_g$ under the density-temperature mapping.

**What GCM derives:** the same PDE structure as Fourier heat conduction, from the graviton-density diffusion equation.
**What GCM does not derive:** $\kappa$ or $\alpha$ from first principles.

---

## Step 4 — Blackbody Spectrum (Structural Framing Only)

The Planck distribution:
$$B(\nu, T) = \frac{2h\nu^3/c^2}{e^{h\nu/kT}-1}$$

arises in standard physics from the quantization of electromagnetic modes in a cavity at thermal equilibrium.

GCM framing: The photon-cluster release events from a graviton-dense system are not monoenergetic. They span a distribution of energies depending on the local density configuration at the time of release. In GCM terms:
- Low-energy releases: large, loosely packed photon clusters (long wavelength, low $\nu$)
- High-energy releases: small, densely packed photon clusters (short wavelength, high $\nu$)

The Planck distribution is, in GCM's reading, the equilibrium distribution of graviton-release-state energies for a system at density excess corresponding to temperature $T$. The $(e^{h\nu/kT}-1)^{-1}$ factor reflects that higher-energy release states are exponentially less likely at a given density — consistent with the general principle that dense, compact configurations are rarer than spread-out ones.

**This is an analogy, not a derivation.** GCM has not derived the Planck distribution from graviton dynamics. Doing so would require:
1. A model of the density-of-states for photon-cluster releases
2. A derivation of why the relevant statistics are Bose-Einstein (bosonic modes) rather than Maxwell-Boltzmann
3. A connection between $h$ (Planck's constant) and graviton properties

All three are open. See UNSPEC-5.

---

## Verification Table

| Check | Method | Result |
|---|---|---|
| Direction of heat flow matches thermodynamics | Qualitative: density gradient vs. temperature gradient | ✓ Consistent (directional divergence → downhill density flow matches low→high temperature direction of heat) |
| Newton's cooling functional form | Algebraic: solve ODE $\dot{\rho}_g = -\lambda\Delta\rho_g$ | ✓ Produces $e^{-\lambda t}$ decay, matches Newton's law |
| Fourier heat equation structural form | Algebraic: apply $\nabla\cdot J_g$ to continuity equation | ✓ Produces $\partial T/\partial t = \alpha\nabla^2 T$ under density-temperature mapping |
| Blackbody spectrum | Qualitative framing only | ⚠️ Analogy only — not derived |
| Equipartition ($C_V = \frac{3}{2}kT$) | Not attempted | ✗ Open (UNSPEC-5) |
| Planck distribution ($h\nu/kT$ factor) | Not attempted | ✗ Open (UNSPEC-5) |

**Verification tally: 3/6 full passes; 1/6 qualitative analogy; 2/6 open gaps. Consistent with 🟡 Yellow tier.**
