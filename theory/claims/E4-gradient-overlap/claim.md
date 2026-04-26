# E4 — Density-Gradient Overlap for Local Interaction Strength

**Claim code:** E4 (Section S3, GCM Coherence Case)
**Epistemic tier:** 🔴 Red (the load-bearing *amplification* reading of E4 fails in standard gravity; a *regularization* reading is 🟢 Green but does not rescue E2)
**Date:** 2026-04-23
**Session:** C (Unification Mechanics)

---

## Statement (as originally proposed)

Particles are not point masses; they are extended density distributions in the graviton substrate. When two particles are close enough for their density distributions to overlap, the *effective* gravitational interaction is no longer captured by $F = Gm_1m_2/r^2$ with $r$ as the center-to-center distance. Instead, the interaction is an integral over the overlap region. The proposal (from Wisdom's 2026-04-23 speech) is that this overlap integral yields an effective interaction strength at short distances that is **orders of magnitude larger** than the naive point-mass estimate — enough (in combination with competing attraction, E2) to account for the apparent $10^{36}$ ratio between electromagnetic and gravitational force magnitudes.

## What the calculation actually shows

Modeling each particle as a Gaussian mass distribution
$$\rho(\mathbf{r}) = \frac{m}{(2\pi\sigma^2)^{3/2}}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma^2}\right)$$
of characteristic width $\sigma$, and computing the Newtonian interaction energy between two such distributions at center-to-center separation $R$, we obtain (closed form, see `derivation.md`):

$$U(R) = -\frac{Gm^2}{R}\,\mathrm{erf}\!\left(\frac{R}{2\sigma}\right)\,.$$

The corresponding force magnitude
$$F(R) = -\frac{dU}{dR} = \frac{Gm^2}{R^2}\,\mathrm{erf}\!\left(\frac{R}{2\sigma}\right) - \frac{Gm^2}{R\sigma\sqrt{\pi}}\exp\!\left(-\frac{R^2}{4\sigma^2}\right)$$
behaves as follows:

| Regime | Behaviour of $F(R)$ vs.\ point-particle $F_{\rm pt} = Gm^2/R^2$ |
|---|---|
| $R \gg \sigma$ (well-separated) | $F(R) \to Gm^2/R^2$ — recovers point-mass limit |
| $R \sim \sigma$ | $F(R) \approx 0.08\,Gm^2/\sigma^2$ — of the same order as $F_{\rm pt}(\sigma)$ |
| $R \ll \sigma$ (fully overlapping) | $F(R) \to 0$ **linearly in $R$** — the $1/R^2$ singularity is regularized |

Numerically, at $R = 0.01\sigma$, $F(R)/F_{\rm pt}(R) \approx 10^{-7}$. At $R \ll \sigma$, the overlap integral is *seven orders of magnitude weaker*, not larger, than the naive $1/R^2$ estimate.

**The overlap integral regularizes; it does not amplify.**

This is a definitive, symbolic and numerical result for the Newtonian-gravity reading of the overlap integral. The "overlap makes local gravity strong enough to produce EM-scale interactions" intuition does not survive contact with the calculation.

## Two honest readings of the result

**Reading A — the *amplification* hypothesis (fails).** The originally proposed version of E4 — that overlap produces an effective interaction $\gg Gm^2/R^2$ at short range — does not hold in standard gravity applied to extended density distributions. At short range the exact integral is bounded and tends to zero, not to infinity. There is no mechanism within Newtonian gravity + extended-mass distributions by which $\sim 10^{36}$ amplification can arise.

**Reading B — the *regularization* observation (holds, but narrower).** The overlap integral does show that extended density distributions do not suffer the $1/R^2$ singularity of point particles. The gravitational interaction between two fully overlapped Gaussians is finite, bounded by $U(0) = -Gm^2/(\sigma\sqrt{\pi})$. This is a clean and physically meaningful feature: it is how nature avoids Newtonian self-energy divergences. But it is a mildness at short range, not the amplification the GCM unification case was hoping for.

## Consequence for GCM's unification case

This is a **structural gap for S3**. The E4-amplification-via-overlap story was meant to close the $10^{36}$ hierarchy problem (EM vs.\ gravity). That story fails as stated. Any rescue requires new physics — **none of which is in the current GCM formalism**:

1. **Non-linear gravity.** A force law that depends non-linearly on density (e.g., $\propto \rho^n$ with $n > 1$) could in principle amplify at high density. GCM has no such law; adopting one would alter the minimal-model equation of motion beyond T1–T4.
2. **Substrate-dependent $G$.** If Newton's constant were itself a function of local graviton density, short-range physics could look very different from long-range physics. No GCM derivation yet.
3. **Contact-only interaction.** If gravitons interacted only via direct contact (zero-range), the overlap volume *would* matter and effective $F \propto \int \rho_1 \rho_2\, dV$ at short range. But this contradicts the long-range $1/r^2$ behavior GCM needs for Newtonian gravity to emerge.

None of these is presently available. This is an honest red-tier gap.

## Relationship to E2, E3

- **E2 (competing attraction)** is the consumer of E4: the toy model assumes that at short range the effective gravitational force is enhanced. With E4 as computed here, E2's quantitative magnitude is off by $\sim 10^{39}$ (see `E2-competing-attraction/`). E2 is therefore qualitatively correct (sign of repulsion) but quantitatively catastrophic.
- **E3 (VdW as universal attraction)** independently fails its original form: the gradient-gradient correlation of two Gaussians is exponentially suppressed at large $R$, not power-law $1/R^6$ (see `E3-vdw-universal/`). The two short-range effects (E4 regularization, E3 exponential suppression) do not combine into a long-range attractive tail.

## What this means for the coherence paper

S3 in the coherence paper must acknowledge:

1. The overlap integral is exactly computable and yields a finite, regularized short-range force — a positive result on its own.
2. The amplification reading required by the unification case fails.
3. The unification case is structurally incomplete until a non-Newtonian mechanism (substrate-$G$ or contact-interaction) is specified.
4. This gap *does not* falsify GCM's broader ontology; it localizes where the hard theoretical work remains.

## Verification stack (CC-7)

- ✅ Dimensional analysis (hand + symbolic)
- ✅ Symbolic derivation (SymPy)
- ✅ Numerical comparison with $Gm^2/R^2$ across $R/\sigma \in [0.01, 10]$
- ✅ Limit checks: $R \to 0$ (finite), $R \to \infty$ (point-mass recovery)
- ✅ Cross-check against standard potential-of-Gaussian textbook formula

See `verification.md` for full detail and `caveats.md` for known limitations.
