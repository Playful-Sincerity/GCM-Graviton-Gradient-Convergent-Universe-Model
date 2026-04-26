# R2 — Plausibility

## Structural Argument

R2 is the mechanism with the strongest peer-reviewed analog among the six. Wiltshire timescape already demonstrates, within GR backreaction, that an inhomogeneous universe with voids and walls produces a clock-rate differential that fits SNe Ia data better than $\Lambda$CDM at ln B > 5 (Seifert et al. 2025, MNRAS Letters 537, L55, on 1,535 Pantheon+ SNe). The phenomenology is empirically credible; the question for R2 is whether GCM provides a mechanism consistent with that phenomenology.

In GCM's one-particle ontology, the link is natural:

1. Matter = graviton density structure (T1).
2. As matter converges, graviton density in matter regions rises; density in the voids between falls.
3. Space is the set of distances between gravitons (T4); so void regions have larger inter-graviton distances.
4. A photon is a graviton-cluster structure; its wavelength reflects internal graviton spacing, which tracks the local inter-graviton scale of the substrate it propagates through.
5. Therefore, a photon crossing a decompressing void has its wavelength stretched in proportion to the local inter-graviton-distance increase.

## Order-of-Magnitude Consistency

For the observed Hubble constant $H_0 \approx 70$ km/s/Mpc, the required fractional wavelength growth per unit distance is:

$$\frac{1}{\lambda} \frac{d\lambda}{dr} \sim \frac{1}{R_{\text{obs}}} \approx 2.3 \times 10^{-27} \text{ m}^{-1}$$

at the observable-universe scale $R_{\text{obs}} \approx 4.4 \times 10^{26}$ m (particle horizon). Equivalently this is of order $H_0/c \approx 7.57 \times 10^{-27}$ m⁻¹ at the Hubble-radius scale $c/H_0 \approx 1.32 \times 10^{26}$ m; the two length scales (and corresponding rates) differ by a factor of 3.3. See [`../R1-space-friction/verification/check_01_hubble_radius_and_alpha.py`](../R1-space-friction/verification/check_01_hubble_radius_and_alpha.py) for the convention check.

Void fractional volume in the observed universe is ~60–80% depending on threshold (from DESI BGS and large-scale-structure surveys). If voids are decompressing at rate $\dot{V}/V \sim H_0$, the fractional void-volume change over a Hubble time is of order unity — which is observed in simulations of structure formation within $\Lambda$CDM (void-and-wall segregation strengthens with time).

**This is an order-of-magnitude consistency check, not a derivation.** What is NOT shown: that the void-decompression rate in GCM without Big Bang expansion produces exactly the same Hubble-diagram shape as $\Lambda$CDM or timescape. That requires a quantitative model.

## Wiltshire Reference — What R2 Inherits and What It Adds

**From Wiltshire (inherited):**
- A non-$\Lambda$ cosmology where apparent acceleration arises from inhomogeneity.
- An empirical fit to Pantheon+ that outperforms $\Lambda$CDM.
- A ~35% clock-rate differential between walls and voids.
- The positioning that observed ISW signals need reinterpretation, not elimination.

**What R2 adds:**
- A substrate mechanism for the clock-rate differential (graviton density, not just GR backreaction).
- A force-unification program that timescape does not address.
- A dark-matter explanation (D1) that timescape does not provide.
- A specific claim about photon internal structure (R6) that gives a time-dilation companion.

**What R2 doesn't add yet:**
- A quantitative $\mu(z)$ prediction that can be compared directly to Pantheon+.
- A specific ISW signal shape.
- A specific model of void-boundary dynamics.

## ISW — The Real Tension

R2's central difficulty is not whether void growth is observed (it is) or whether it produces an ISW signal (it does). The tension is interpretive: *what does the observed ISW cross-correlation tell us about the underlying physics?*

**Standard cosmology's reading:** potentials decay in the presence of $\Lambda$. Crossing photons lose/gain energy differentially. The observed positive cross-correlation of CMB with LSS is evidence for dark energy.

**R2's reading:** the same cross-correlation is evidence for graviton-density-gradient evolution in a converging universe. Whether the signal's *shape* matches R2's prediction is an open empirical question requiring a quantitative R2 model to answer.

**The honest statement:** R2 is consistent with observed ISW *in direction* (growing voids produce the right sign of signal). R2 is not yet consistent with observed ISW *in shape* (no R2 derivation has been performed). Quantitative fit is future work. This is an honest "yellow" — not hand-waved, not overclaimed.

## Where Plausibility Falls Off

- **Void-decompression rate.** In a converging universe, is the decompression rate actually $\sim H_0$? That depends on the overall matter convergence rate in GCM, which is not yet quantified from the minimal-model equation of motion.
- **Line-of-sight path averaging.** Different paths through the cosmic web see different void/wall structure. The observed redshift-distance relation is tight (scatter ~5%), so path averaging must work out to not produce much more scatter than $\Lambda$CDM predicts.
- **Effect on the CMB.** The CMB was emitted before most large-scale-structure voids formed. R2's effect on the CMB is therefore largely in transit through later voids, not at emission. This produces anisotropies (ISW), and it must not distort the blackbody (a frequency-independent wavelength stretching by void transit is the question).
