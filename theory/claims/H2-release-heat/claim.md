# H2 — Release Theory of Heat

**Claim code:** H2
**Session:** F (Thermodynamics, Classical & Relativistic Limits)
**Epistemic tier:** 🟡 Yellow — plausibility sketch upgraded from conceptual-only per CC-6.
**Date:** 2026-04-23
**Status:** Pre-formal. No quantitative reproduction of equipartition or Planck's law. Structural logic is argued; derivation is not.

---

## The Claim

Heat is not primarily kinetic energy of particles in random motion. It is the **release of excess graviton-density matter** from a system that has exceeded its local density capacity — photon-cluster emission driven by disequilibrium in the graviton substrate. Kinetic motion is a downstream side effect of that release, not the primary mechanism.

More precisely:

> A system at thermal disequilibrium has local graviton density exceeding the equilibrium background value $\rho_0$. The excess is shed as photon clusters (light quanta, in GCM's framing: traveling graviton-cluster structures). Each release event produces a recoil force on the emitting particle (Newton's 3rd law), which produces the kinetic motion standard thermodynamics attributes *to* heat. Kinetic motion is the shadow of release, not its cause.

**Direction of heat flow:** Heat flows toward regions of lower graviton density — not because of random diffusion, but because excess density structures seek the steepest gradient path to equilibrium. This is the **directional divergence principle**: the graviton density flux $J_g = -D\nabla\rho_g$ flows down the gradient, carrying energy with it.

---

## What This Predicts Qualitatively

### 1. Direction of Heat Flow

Standard thermodynamics: heat flows from hot to cold (Clausius).

GCM substrate reading: "hot" regions are those with elevated graviton density (higher packing, more disequilibrium). "Cold" regions have lower graviton density. The graviton flux $J_g$ flows from high to low density, carrying photon-cluster releases with it. Heat flow direction is determined by the density gradient, not by random particle velocity.

This matches Clausius qualitatively. The advantage of the GCM framing: it gives a *directionality mechanism* (gradient equalization) rather than a *statistical postulate* (entropy maximization). Whether GCM's mechanism can reproduce the Second Law quantitatively is not established — see Caveats.

### 2. Blackbody Radiation

Standard thermodynamics: a blackbody in thermal equilibrium emits radiation with a specific spectral distribution (Planck's law), with a peak wavelength inversely proportional to temperature (Wien's law).

GCM substrate reading: a blackbody in equilibrium is a system where graviton-release events are occurring at all scales. The spectrum of emitted photon clusters reflects the **distribution of graviton-release states** available at a given density. Hotter systems (higher local density excess) have more high-density release events available — releasing shorter-wavelength photon clusters (higher-energy releases correspond to smaller, denser photon structures). The Planck distribution is, in GCM's reading, the natural distribution of graviton-release energies at equilibrium density.

**Honest flag:** This is a structural analogy, not a derivation. GCM has not reproduced Planck's law $B(\nu, T) = \frac{2h\nu^3/c^2}{e^{h\nu/kT}-1}$ from graviton-release dynamics. That would require a specific model of the density-of-states function for graviton releases, which is not yet formulated. See UNSPEC-5.

### 3. Newton's Law of Cooling (qualitative)

Newton's law of cooling: $\frac{dT}{dt} = -k(T - T_{\text{env}})$ — the rate of cooling is proportional to the temperature difference.

GCM substrate reading: temperature difference maps to graviton density excess $\Delta\rho_g = \rho_g^{\text{hot}} - \rho_g^{\text{env}}$. The rate of photon-cluster release is proportional to this excess — more excess means more release events per unit time. Release rate $\propto \Delta\rho_g$, and since cooling reduces $\Delta\rho_g$, the cooling rate itself diminishes as equilibrium is approached. This produces the same exponential decay structure as Newton's law.

**Explicit emergence argument:**
$$\frac{d\rho_g}{dt} = -\lambda(\rho_g - \rho_0)$$

where $\rho_0$ is the equilibrium background density and $\lambda$ is a release rate constant. This first-order equation has the solution $\rho_g(t) - \rho_0 \propto e^{-\lambda t}$, which maps to $T(t) - T_{\text{env}} \propto e^{-kt}$ — Newton's cooling law — if temperature is proportional to local density excess.

GCM does not derive $\lambda$; it asserts the proportionality and shows the functional form follows.

### 4. Fourier Heat Conduction (qualitative)

Fourier's law: $\mathbf{q} = -\kappa \nabla T$ — heat flux is proportional to the negative temperature gradient.

GCM substrate reading: if temperature maps to graviton density excess, then the heat flux maps to the graviton density flux: $J_g = -D\nabla\rho_g$. For a material in which graviton density tracks temperature linearly, $D\nabla\rho_g \propto \kappa\nabla T$. Fourier's law is emergent from the directional divergence principle applied to the spatial gradient of density.

The diffusion equation $\frac{\partial T}{\partial t} = \alpha\nabla^2 T$ follows by combining the rate-of-release equation with the spatial Fourier flux — the same structural argument as above but in spatial terms.

**Honest flag:** GCM does not derive the thermal conductivity $\kappa$ or the diffusivity $\alpha$ from graviton properties. These would require modeling how graviton releases propagate through different materials — solid, liquid, gas — at the microstructural level. That is out of scope for this sketch.

---

## Comparison to Verlinde Entropic Gravity

Erik Verlinde's entropic gravity program (2017, SciPost) treats thermodynamics as fundamental rather than emergent — gravity *is* an entropic force arising from entanglement entropy on holographic screens, not a fundamental interaction. Temperature (in Verlinde's framework) is related to the Unruh temperature, itself tied to the acceleration of boundaries through the quantum vacuum.

**Structural sympathy with GCM:** Both programs treat thermodynamic quantities as substrate-level phenomena rather than as statistical overlays on classical mechanics. In Verlinde's framing, the substrate is the entanglement structure of the vacuum; in GCM's framing, it is the graviton density distribution. Both agree: thermodynamics is not *about* particles bouncing around, it is *about* the underlying structure of space.

**Key divergence:** Verlinde's program accepts quantum mechanics as foundational (entanglement entropy is a QM quantity); GCM treats QM as an emergent description of real density distributions. Verlinde's framework accepts cosmological expansion (entropic gravity with a dark energy component); GCM rejects expansion (T3). Verlinde does not commit to a specific substrate particle; GCM commits to the graviton.

**GCM's position:** GCM's density-gradient framing and Verlinde's entropic framing are both "substrate thermodynamics" programs. They share the move that makes thermodynamics deep rather than statistical. They diverge in what the substrate is made of and what large-scale cosmology looks like. Neither has reproduced all thermodynamic laws quantitatively.

---

## What This Establishes

- A directional mechanism for heat flow (gradient equalization, not random walk)
- Structural consistency with Newton's law of cooling (same exponential functional form)
- Structural consistency with Fourier's law (same gradient-proportional flux)
- A framing of blackbody radiation as the distribution of release states (analogy, not derivation)
- A structural distinction from classical tired light and from purely kinetic-theoretic thermodynamics
