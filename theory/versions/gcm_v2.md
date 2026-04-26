# Graviton Gradient Convergent Universe Model (GCM)
**Version**: 2.0 — Quick-Win Revision
**Date**: 2026-03-21
**Status**: Pre-formal theoretical document. Math is exploratory; all underspecified mechanisms flagged explicitly.

**Changes from v1**:
- CRITICAL-1 fixed: Mass formula m = ξ²/V → m = mg·ξ (dimensionally sound)
- CRITICAL-3 fixed: LIGO bound corrected 1.8 × 10⁻⁵⁶ kg → 1.78 × 10⁻⁵⁹ kg
- CRITICAL-2 fixed: H7 energy mapping revised ΔEn ∝ ΔPn → En ∝ 1/Pn
- Source notes integrated throughout (PDFs: Physics Proposal, 物理 Outline, 物理 Compilation, 物理 Raw Notes)

---

## Part I — Axioms

These are non-negotiable. All hypotheses must be consistent with them.

**Tenet 1 (T1)**: There is exactly one fundamental particle: the **graviton** (dimensionless point). All matter, energy, space, and time are configurations of gravitons.

**Tenet 2 (T2)**: There is exactly one fundamental force: **gravity** — the tendency of gravitons to attract one another. All other forces are emergent. Repulsion is not fundamental — it is **competing attraction** (a configuration where each body is more attracted elsewhere than toward the other).

**Tenet 3 (T3)**: The long-term trajectory of the universe is **convergence**. Current cosmological evidence for accelerating expansion reflects a misinterpretation of redshift and luminosity data.

**Tenet 4 (T4)**: All existence is dimensions of change in the graviton substrate. Wave-particle duality reflects real gradient distributions, not probability amplitudes.

---

## Part II — Foundational Definitions

### The Graviton

- Dimensionless point particle with mass mg (kg)
- No intrinsic spin (spin requires an extended body; dimensionless points cannot rotate)
- Interaction is local: gravity acts between contiguous gravitons only

**Spacetime as graviton distances**: Space is the set of distances between gravitons. Time is the process of those distances shortening. There is no gravitational field — just gravitons that want to come together. This is what gives rise to the effects of general relativity.

> ⚠️ **Open (Graviton Mobility)**: Does the graviton itself move, or do only the distances between gravitons change? The distinction matters for how forces propagate and whether the substrate is better modeled as a dynamic lattice or a relational distance field. Pending formalization.

### Particles

A particle is a **nucleated density gradient** in the graviton substrate: a region where local density ρ_g = mg·ξ/V significantly exceeds the background vacuum density ρ₀.

- **Nucleation**: How sharply concentrated the density gradient is
- **Boundaries**: Real and gradual, not probabilistic
- **Wave-particle duality**: Natural consequence of extended density structures. Double-slit interference occurs because the outer levels of a photon's density distribution interact with both slits simultaneously. Measurement collapses this by absorbing the outer levels.

### Vacuum State

> ⚠️ **OQ-4 (Most Foundational Open Question)**: The baseline graviton density ρ₀ in empty space is undefined. All density gradients are meaningful only relative to this background. No quantitative particle property can be finalized until ρ₀ is defined or derived.

---

## Part III — Hypotheses

### H1: Graviton Mass

**Claim**: The graviton has mass mg. Its upper bound is constrained by LIGO.

**LIGO graviton mass constraint** (v1 conversion error corrected):

```
LIGO bound:         mg < 10⁻²³ eV/c²
Conversion factor:  1 eV/c² = 1.783 × 10⁻³⁶ kg

mg < 10⁻²³ × 1.783 × 10⁻³⁶ = 1.78 × 10⁻⁵⁹ kg   ✓ CORRECTED
v1 had:  1.8 × 10⁻⁵⁶ kg  (off by factor 1000 — now fixed)
```

**Proposed estimate** (using neutron density as graviton packing proxy):

```
ρ_neutron ≈ 4 × 10¹⁷ kg/m³
ℓ_Planck  = 1.616 × 10⁻³⁵ m
V_Planck  = ℓP³ ≈ 4.22 × 10⁻¹⁰⁵ m³

mg ≈ ρ_neutron × V_Planck ≈ 1.69 × 10⁻⁸⁷ kg
```

This is ~28 orders of magnitude below the LIGO bound. H1 passes the constraint.

> ⚠️ **OQ-2**: The choice of ρ_neutron as packing upper bound is provisional. Planck density is ~78 orders higher. This assumption must be derived from first principles or explicitly stated as a boundary condition.

> ⚠️ **Open (Planck's constant)**: Source notes claim "Planck's constant is the mass of the graviton." Dimensional check: h = 6.626 × 10⁻³⁴ J·s ≠ kg. Closest reinterpretation: h/c² ≈ 7.37 × 10⁻⁵¹ kg — still 36 orders above proposed mg. A different formulation is needed. Pending investigation.

---

### H2: Charge from Graviton Flow Direction

**Claim**: Electric charge arises from the net direction of graviton current in a particle's density gradient.

Formal statement using graviton current density J_g:

```
q > 0  (positive / proton-like):   ∇·J_g < 0   net inflow, density increasing toward center
q < 0  (negative / electron-like): ∇·J_g > 0   net outflow, density decreasing toward center
q = 0  (neutral / neutron-like):   ∇·J_g = 0   balanced flow
```

"Proton wants to give, electron wants to take, neutron is content."

Charge is quantized because any sub-threshold excess is shed as light before accumulating to a full unit.

**Why EM appears stronger than gravity**: The electromagnetic interaction between electron and proton outer density levels occurs at effectively zero separation (r ≈ 0). The gravitational force law F ∝ 1/r² produces enormous force when r→0, which is what we label the electromagnetic force. "The protons and electrons are so close the force is strong enough because they are practically touching — r² is almost 0."

**Van der Waals**: Temporary polarization of electron density gradients creates asymmetric competing attraction — the weaker "partial charge" case of the same mechanism.

> ⚠️ **UNSPEC-1**: No derivation yet for why electron-type configurations produce net outflow and proton-type produce net inflow. Requires solving J_g = −D∇ρ_g + v_g·ρ_g for stable configurations.

> ⚠️ **UNSPEC-2**: Fractional quark charges (+2/3, −1/3) not addressed. Mechanism must generalize to sub-integer flow states.

---

### H3: Pauli Exclusion from Toroidal Oscillation

**Claim**: Particles not at equilibrium undergo **toroidal cycling** — oscillation of their graviton density in a toroidal geometry. Pauli exclusion arises because two toroidal oscillation modes cannot simultaneously occupy the same state.

Key properties from source notes:
- "Angular momentum is translation of 1D motion into 2D; toroidal momentum is translation of 2D motion into 3D."
- "A completely cold/content particle does not toroidally cycle. Disequilibrium (heat) causes cycling."
- "Pauli exclusion happens because of the 1-dimensional nature of field oscillation in toruses."
- Toroidal oscillation follows the right-hand rule (why? — open)
- Light polarization is the orientation of its gravitons' toroidal cycling

> ⚠️ **UNSPEC-3**: No wave equation for toroidal oscillations yet. Need ρ_g(r,θ,φ,t) in toroidal coordinates with self-interaction term to formally define "same quantum state."

> ⚠️ **OQ-3**: Does GCM derive Pauli exclusion from graviton dynamics alone? Must state position on Lorentz invariance (does it emerge from the graviton substrate?) before claiming compatibility with spin-statistics theorem.

---

### H4: Magnetism from Toroidal Alignment

**Claim**: Magnetism arises when the toroidal oscillations of multiple particles align — which is forced by charge movement.

- "Electricity travels straight down a wire, makes a circular magnetic field, because electron motion moves forward toroidally."
- A static magnetic field is composed of "static light that moves slightly along field lines."
- "A magnetic monopole is an electric field. E and M are the same force — E is either in or out; M is out and in."
- Permanent magnets sustain the force with ambient light; electromagnets generate it directly from current.

> ⚠️ **UNSPEC-4 (Urgent)**: The Lorentz force law F = q(E + v×B) is verified to extraordinary precision. GCM must reproduce the **identical numerical result** from toroidal alignment dynamics — not just describe the analogy.

---

### H5: Heat as Graviton Release

**Claim**: Heat is not primarily kinetic energy of particles. It is the release of photon clusters from a particle experiencing density disequilibrium — the graviton-substrate origin of thermal radiation.

- "Heat is release of light that by Newton's 3rd causes the source to recoil."
- "Heat: light moves most. Electricity: electrons move most. Sound: nucleons move most."
- Disequilibrium is what causes toroidal cycling.
- Seebeck effect, thermoelectric emission, thermoluminescence are more naturally predicted here.

> ⚠️ **UNSPEC-5**: Must reproduce equipartition (CV = 3/2 kT for monatomic gas) and Fourier heat conduction (∂T/∂t = α∇²T) in tested regimes.

---

### H6: Mass, Energy, and Density (CRITICAL-1 FIXED)

**v1 had m = ξ²/V — dimensionally broken (produces kg·m⁻³, not kg). Fixed:**

```
ξ    = graviton count (dimensionless integer)
mg   = graviton mass (kg)
V    = volume of particle (m³)

m    = mg · ξ                   [kg ✓]
E    = mg · ξ · c²              [J ✓]
ρ_g  = mg · ξ / V  =  m / V    [kg/m³ ✓]
```

This is E = mc² per graviton, summed over all gravitons in the particle. Fully consistent with T1.

**Physical interpretation of inertia**: A denser particle (higher ξ/V) is harder to accelerate because more gravitons must be collectively displaced. Inertia is resistance to changing a density distribution's configuration.

**Rest energy extension** (from source notes): "e=mc² should change to include density." A denser packing may increase binding energy. Proposed reformulation:

```
E_rest = f(ρ_g) · mg · ξ · c²
```

where f → 1 at normal particle densities (recovering standard result). The function f(ρ_g) is pending derivation.

---

### H7: Tetrahedral Shell Quantization (CRITICAL-2 FIXED)

**Claim**: Gravitons in spacetime occupy a tetrahedral close-packed lattice. Particle quantum levels correspond to successive tetrahedral shells with populations:

```
P_n = 10n² + 2
```

| n | P_n | ΔP_n |
|---|-----|------|
| 1 | 12  | —    |
| 2 | 42  | 30   |
| 3 | 92  | 50   |
| 4 | 162 | 70   |
| 5 | 252 | 90   |

Shell growth is linear in n (ΔP_n = 20n − 10). Shell populations grow as n².

**v1 energy mapping failed**: Claimed ΔE_n ∝ ΔP_n. Test: E_n/ΔP_n varies 100× from n=2 to n=5. No single constant can bridge linear-in-n shell growth with cubic-inverse-in-n hydrogen energy spacing.

**Corrected mapping: E_n ∝ 1/P_n**

Verification — compute E_n · P_n across hydrogen levels:

| n | P_n | E_n (eV) | E_n · P_n (eV) |
|---|-----|----------|----------------|
| 1 | 12  | 13.600   | 163.2          |
| 2 | 42  | 3.400    | 142.8          |
| 3 | 92  | 1.511    | 139.0          |
| 4 | 162 | 0.850    | 137.7          |
| 5 | 252 | 0.544    | 137.1          |

**E_n · P_n ≈ 136–163 eV across all levels** (~20% variation, dominated by n=1 ground state). This is a strong approximate invariant — dramatically better than v1's 100× variation.

The asymptotic value as n → ∞: E_n → 0, P_n → ∞, but E_n · P_n → ~136 eV ≈ 13.6 eV × 10. The significance of this asymptote warrants investigation.

**Revised H7 claim**:
> *Shell stability scales inversely with shell population. The product E_n · P_n is approximately conserved — representing a nearly-constant total energetic "budget" per shell, distributed across its gravitons. More gravitons per shell → more stable → lower energy per graviton.*

---

### H8: Cosmological Convergence (OQ-1 — Largest Gap)

**T3 is currently axiomatic, not derived.** No quantitative mechanism for cosmological redshift has been specified. This is the largest empirical gap in the framework.

**Proposed mechanisms** (source notes — candidate list, not yet ranked or formalized):

1. **Space friction** — light loses energy to friction with gravitons during propagation. "Light loses energy to friction with small pieces of space."

2. **Void decompression** — as matter collapses toward dense regions, the voids between clusters expand. Light traveling through an expanding void has its wavelength stretched. "Light is expanded by the voids being expanded through the collapse of matter in their boundaries."

3. **Non-central position** — we are not at the gravitational center of the universe. Distant light is preferentially attracted elsewhere, arriving at lower energy. ("Unattractive Earth hypothesis.")

4. **Light pressure sensitivity** — "light lowers frequency when in less pressure." Low graviton-density regions (voids) reduce photon energy.

**Structural advantage over tired light — time dilation**:

The classical objection to tired light is that SNe Ia light curves show time dilation (events appear stretched in time at high redshift). This killed tired light. But GCM's source notes anticipate this:

> "All redshifting forces must also result in time dilation. As light redshifts, the distance between the nuclei of the photons increases, thus increasing the delay of information, making it seem like time dilation."

In GCM, as a photon loses energy (wavelength increases), the distance between successive graviton clusters comprising that photon increases — which directly produces time dilation as a geometric consequence. This is not a coincidence; it is built into the mechanism. GCM is not classical tired light.

**Supporting cosmological context**:
- **Timescape cosmology** (Wiltshire 2024): Peer-reviewed claim that apparent acceleration is a misidentification of average expansion rate vs. local clocks in underdense regions. Direct GCM ally.
- **DESI DR2** (March 2025): 4.2σ evidence for evolving/weakening dark energy — supports future convergence.
- **Hubble tension**: H₀ = 67.4 km/s/Mpc (CMB) vs. 73 km/s/Mpc (local) — systematic in distance ladder; may be reinterpretable under GCM void decompression model.

> ⚠️ **OQ-1 (Largest Gap)**: One mechanism must be formalized into a quantitative redshift law that simultaneously matches:
> 1. The observed z vs. comoving distance relationship
> 2. SNe Ia light curve time dilation (GCM's photon-nuclei separation mechanism is the candidate)
> 3. CMB blackbody spectrum at 2.725 K
> 4. Distance modulus dimming of SNe Ia
>
> Until this is done, T3 remains a philosophical stance, not a scientific hypothesis.

---

## Part IV — Open Questions Summary

| ID | Description | Priority |
|----|-------------|----------|
| OQ-4 | Vacuum ground state ρ₀ undefined — most foundational | Immediate |
| OQ-1 | Cosmological redshift/CMB/SNe mechanism — largest empirical gap | Wave 2 |
| OQ-2 | Neutron density as graviton upper bound unjustified | Wave 2 |
| OQ-3 | Lorentz invariance / spin-statistics — deep structural | Wave 3 |
| UNSPEC-1 | H2: flow direction derivation missing | Wave 2 |
| UNSPEC-2 | H2: fractional quark charges unaddressed | Wave 2 |
| UNSPEC-3 | H3: no toroidal wave equation | Wave 2 |
| UNSPEC-4 | H4: Lorentz force not reproduced numerically | Wave 2, urgent |
| UNSPEC-5 | H5: equipartition not derived | Wave 3 |
| PENDING  | "Planck's constant = graviton mass" dimensional resolution | Near-term |

---

## Part V — Proposed Experiments

1. **Vacuum friction redshift** — bounce light in optical cavity; measure frequency decay over extended time. Rate should extrapolate to cosmological redshift.

2. **Like-charge attraction** — isolate two like-charge particles from all other attractors. At sufficiently small separation, competing attraction mechanism predicts net attraction.

3. **Current has more mass** — compare gravitational mass of wire heated by friction vs. current vs. moving magnetic field. Current-heated wire should show higher mass (greater electron density alignment).

4. **Aligned magnets conduct heat better** — toroidal alignment should reduce resistance to graviton-release heat flow; measure thermal conductivity across aligned vs. unaligned magnet chain.

5. **Seebeck/thermoelectric precision** — compare graviton-release predictions vs. kinetic theory for Seebeck coefficient in novel materials.

6. **Decompression redshift** — measure light wavelength after passing through artificially expanded gas void; compare to control path.

7. **SNe Ia light curve reanalysis** — apply photon-nuclei separation model to existing datasets; test whether void decompression + nuclei separation reproduces observed time dilation stretching factors without invoking expansion.

---

## Appendix — Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| mg | Graviton mass | kg |
| ξ | Graviton count in a particle | dimensionless |
| V | Particle volume | m³ |
| ρ_g | Graviton mass density | kg/m³ |
| ρ₀ | Vacuum baseline graviton density | kg/m³ — undefined (OQ-4) |
| J_g | Graviton current density | kg/(m²·s) |
| P_n | Gravitons in nth tetrahedral shell | dimensionless |
| ℓP | Planck length | 1.616 × 10⁻³⁵ m |

---

*v3 target: define vacuum state (OQ-4) and formalize one cosmological redshift mechanism (OQ-1), after Wave 2 agents complete.*
