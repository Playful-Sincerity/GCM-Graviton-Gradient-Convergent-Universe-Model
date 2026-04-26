# E3 — Van der Waals as Universal Attraction

**Claim code:** E3 (Section S3, GCM Coherence Case)
**Epistemic tier:** 🟡 Yellow as framing co-optation; 🔴 Red for the specific claim that graviton-gradient overlap *reproduces* the VdW $1/r^6$ scaling
**Date:** 2026-04-23
**Session:** C (Unification Mechanics)

---

## Statement (framing co-optation, not new derivation)

Van der Waals forces — specifically the London dispersion component — are a universally-recognized **attractive** force between all electrically neutral particles, with long-range energy scaling as $-C_6/r^6$. Standard physics explains this as arising from correlated fluctuations of induced dipoles between the two bodies.

GCM does not attempt to derive VdW from scratch. Instead, E3's claim is a *reading-in*:

> The charge-fluctuation correlations that standard physics identifies as the origin of VdW are, in GCM's ontology, manifestations of **graviton-density-gradient fluctuations** between the two bodies. VdW is already a universal weak attraction; GCM claims it for its unification program by identifying its substrate with graviton-substrate fluctuations.

This is a framing move, not a new physical prediction. GCM agrees with all standard VdW calculations and predictions; it simply reinterprets what "fluctuating dipole" means at the substrate level.

## What the direct calculation shows (honest caveat)

The naïve version of this framing would say: two Gaussian density distributions have gradient fluctuations; the overlap of those gradient fluctuations should directly reproduce the $1/r^6$ VdW scaling at long range.

We can test that directly. The gradient-gradient correlation between two identical Gaussians of width $\sigma$ at separation $R$ is (see `derivation.md`):

$$C(R) = \int \nabla\rho_1(\mathbf{r}) \cdot \nabla\rho_2(\mathbf{r}-\mathbf{R})\,d^3r = \frac{m^2(6\sigma^2 - R^2)}{32\pi^{3/2}\sigma^7}\exp\!\left(-\frac{R^2}{4\sigma^2}\right).$$

At large $R$, this is **exponentially suppressed**, not power-law $1/R^6$. At $R = 10\sigma$, the correlation is ~$10^{-5}$ of the $1/R^6$ VdW value at the same $R$ (numerical comparison in `verification.md`).

**So the naive "overlap gradient-gradient correlation → 1/R^6" reading fails.** Gaussian density distributions do not produce the VdW long-range tail through direct gradient overlap; the long-range dispersion force requires something else.

## What actually produces $1/r^6$ in standard physics

Standard VdW-London dispersion comes from *induced-dipole* interactions, not from static gradient overlap:

1. A transient fluctuation in the charge distribution of body 1 creates an instantaneous dipole moment $\mathbf{p}_1(t)$.
2. This dipole generates an electric field $\mathbf{E}_2 \sim \mathbf{p}_1/r^3$ at body 2.
3. Body 2 is polarizable (characterized by polarizability $\alpha$), so it develops an induced dipole $\mathbf{p}_2 = \alpha \mathbf{E}_2 \sim \alpha \mathbf{p}_1/r^3$.
4. The interaction energy between the induced dipole and the fluctuating source scales as $\mathbf{p}_1 \cdot \mathbf{E}_1 \sim p_1^2 / r^6$.
5. Time-averaging over the thermal/quantum fluctuations of $\mathbf{p}_1$ yields the net attractive $-C_6/r^6$ dispersion force.

The key ingredients are: (a) the Coulomb dipole field falling off as $1/r^3$, not as a Gaussian tail; (b) polarizability of the distant body; (c) time-averaged correlations.

## What GCM would need, to properly claim VdW

For GCM's gradient-substrate framing to actually reproduce $1/r^6$ dispersion, each of these three ingredients must have a GCM analogue:

1. **Long-range dipole potential.** A fluctuation in graviton density at body 1 must produce a gradient field at body 2 that falls as $1/r^3$, not as a Gaussian. Newtonian gravity of a dipolar mass distribution does fall as $1/r^3$ in the potential's dipole moment — so this is plausible *if* graviton-density fluctuations carry a non-zero dipole moment and interact gravitationally.
2. **Polarizability.** The distant body must have a susceptibility to distortion by an applied gravitational gradient. This is well-defined in principle (Gaussian mass distributions distort under tidal forces), but quantitative calculation is not done within GCM.
3. **Fluctuation spectrum.** The statistics of graviton-density fluctuations must be specified — their amplitude, frequency content, and correlation time. These would be analogous to the zero-point quantum fluctuations that drive London dispersion in standard physics.

If all three are in place, the *structure* of the VdW calculation ports over to the graviton substrate, and the $1/r^6$ scaling is expected to be recovered. This is a plausible direction. But it is not yet a completed derivation, and the *naive* direct-overlap reading (which we tested) does not produce it.

## Relationship to Verlinde entropic gravity

Verlinde's entropic-gravity program (SciPost 2017) treats gravity as an emergent entropic force arising from entanglement entropy on holographic screens. At short scales, Verlinde does not produce a VdW-like residual — his framework lives at cosmological and galactic scales, not at molecular scales. So we cannot use Verlinde's framework to rescue this portion of E3.

Entropic-gravity approaches more generally (Padmanabhan, Jacobson) do not explicitly address intermolecular dispersion forces. The VdW-as-graviton-fluctuation reading, if it can be made rigorous, would be a distinctive GCM contribution — VdW as the lowest-$r$ window into graviton substrate physics.

## Epistemic status

**At the level of "co-option of existing physics":** 🟡 Yellow.
The claim "VdW is universal and is a manifestation of substrate-level graviton fluctuations" is a reading-in that is logically compatible with all existing VdW observations. Nothing in standard physics rules it out; nothing in GCM forces it in. It's a compatibility claim, not a prediction.

**At the level of "GCM derives $1/r^6$ from first principles":** 🔴 Red.
The direct-overlap calculation does not produce $1/r^6$. A proper derivation would require specifying graviton polarizability, the fluctuation spectrum of the graviton density, and performing the analog of a Casimir-Polder calculation in the graviton substrate. This work is not done.

## Claim for the coherence paper

The coherence paper should state this honestly:

> GCM takes the universality of Van der Waals attraction — already accepted in standard physics — as structural evidence that a universal weak attractive force exists between all neutral bodies. GCM reinterprets the fluctuating-dipole correlations that standard physics identifies as the origin of VdW as manifestations of graviton-density-gradient fluctuations. This is a re-framing, not a new calculation. A rigorous derivation of the $1/r^6$ scaling from graviton-substrate physics — analogous to the standard Casimir-Polder approach — is future work. The direct-overlap calculation performed in Session C shows that gradient-gradient correlation of Gaussian density distributions does not produce $1/r^6$ without additional ingredients (polarizability, dipole fluctuations, time averaging); these must be specified to complete the derivation.

## Verification stack (CC-7)

- ✅ Dimensional analysis of the gradient-gradient correlation integral
- ✅ Symbolic computation of $C(R)$ for Gaussian distributions (SymPy)
- ✅ Numerical comparison of $C(R)$ to $1/R^6$ at multiple $R/\sigma$
- ✅ Cross-check against standard VdW treatment (Griffiths *Introduction to Electrodynamics* §4.2.3; Landau-Lifshitz *Statistical Physics* §82)
- ⚠️ No verification of the full GCM-analog Casimir-Polder derivation (not attempted; flagged as future work)

See `verification.md` for full numerical tables and `caveats.md` for what the claim does and does not commit to.
