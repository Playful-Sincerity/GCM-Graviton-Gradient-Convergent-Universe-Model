# E2 — Competing Attraction as "Electron Repulsion"

**Claim code:** E2 (Section S3, GCM Coherence Case) — **the load-bearer for S3.**
**Epistemic tier:** 🟡 Yellow (sign correct, geometry-specific); 🔴 Red for quantitative magnitude
**Date:** 2026-04-23
**Session:** C (Unification Mechanics)

---

## Statement

GCM claims there is no repulsive force at the fundamental level — only attraction (T2). What appears as "electron-electron repulsion" is, under the competing-attraction reading, the result of each electron being pulled more strongly toward some other attracting body (a proton or a concentration of matter) than toward the other electron. In a suitable geometric configuration, this produces a net dynamical separation between the two electrons that looks, from the pair's reference frame, like a repulsive force.

The toy model must show at least that the **sign** of this apparent repulsion can be produced by gravitational competing attraction. Quantitative magnitude reproduction is future work.

## What the calculation shows

Setting up the simplest toy geometry that works — a heavy positive mass (proton, $m_p$) at the origin, and two electrons ($m_e$) both located on the $+x$ axis at positions $d$ and $d+r$ — the exact Newtonian forces give:

- **Net acceleration of $E_1$** (the inner electron, at $+d$): toward the origin (in $-x$). Dominated by the proton's pull, partially offset by the outer electron's pull.
- **Net acceleration of $E_2$** (the outer electron, at $+d+r$): toward the origin (in $-x$), but weaker, because the proton is farther.
- **Relative acceleration** $\ddot{r} = \ddot{x}_{E_2} - \ddot{x}_{E_1}$: **positive** — the inter-electron separation $r$ increases with time.

This matches the expected sign of repulsion. The two electrons drift apart under the gradient of the proton's attractive field.

Working with real physical constants (Bohr radius $a_0 = 5.29 \times 10^{-11}\,\mathrm{m}$ for both $d$ and $r$, and $m_p, m_e$ at their SI values), the numerical result is:

| Quantity | Value |
|---|---|
| Force on $E_1$ from proton | $-3.63 \times 10^{-47}$ N (toward origin) |
| Force on $E_1$ from $E_2$ | $+1.98 \times 10^{-50}$ N (toward $E_2$) |
| Net $\ddot{x}_{E_1}$ | $-3.99 \times 10^{-17}$ m/s$^2$ |
| Net $\ddot{x}_{E_2}$ | $-1.00 \times 10^{-17}$ m/s$^2$ |
| Relative acc. $(\ddot{x}_{E_2} - \ddot{x}_{E_1})$ | $+2.99 \times 10^{-17}$ m/s$^2$ (positive = separation growing) |
| Apparent repulsive force on pair | $+1.36 \times 10^{-47}$ N |

For comparison, the Coulomb repulsion between two electrons at the same separation is $F_C = k_C e^2/r^2 \approx +8.24 \times 10^{-8}$ N.

**Ratio:** $F_{\rm competing} / F_{\rm Coulomb} \approx 1.65 \times 10^{-40}$.

That is, the competing-attraction mechanism produces apparent repulsion of the correct sign, but the magnitude is roughly $6 \times 10^{39}$ times weaker than actual Coulomb repulsion between two electrons at Bohr-radius separation.

## Control: symmetric configuration

If the proton is placed **between** the two electrons (at the midpoint), the calculation gives the opposite sign: the two electrons both accelerate toward the proton, which means they accelerate toward *each other*. The relative acceleration is $-8.0 \times 10^{-17}$ m/s$^2$ (negative = separation shrinking). Symmetric geometry produces apparent *attraction*.

So competing attraction is **geometry-dependent**. Repulsion emerges only when the attracting background is positioned asymmetrically with respect to the electron pair. When the background is symmetric (proton equidistant from both electrons, or a spherically symmetric cloud around the pair), the two electrons feel the same background force and nothing nets out as repulsion. In that case, only the direct (attractive) inter-electron gravity remains.

## Honest verdict

**Sign:** ✅ Correct. Competing attraction *can* produce apparent electron repulsion in the right geometry.

**Magnitude:** ❌ Off by $\sim 10^{40}$. Bare Newtonian gravity is simply too weak to reproduce Coulomb-scale forces.

**Geometry dependence:** ⚠️ Intrinsic. The mechanism does not produce isotropic repulsion — it requires a specific background configuration.

E2 demonstrates that "electron repulsion is really competing attraction" is a **structurally coherent** idea at the sign level, but **quantitatively requires additional physics** to match observed Coulomb strengths. This additional physics was supposed to come from E4 (gradient-overlap amplification), but E4 as originally framed does not produce the needed amplification (see `../E4-gradient-overlap/`). The structural gap is therefore real and acknowledged.

## Interpretation for the coherence paper

The paper should state plainly:

1. The competing-attraction reading of electron repulsion is sign-correct in a simple Newtonian toy model, in a geometry where a heavy attractor sits off to one side of the electron pair.
2. It is **not** quantitatively viable with bare gravity — off by ~40 orders of magnitude.
3. Closing the quantitative gap requires one of: density-dependent $G$, non-linear graviton coupling, or contact-only interactions — none presently specified.
4. This is a **structural gap for the unification case**. Per the coherence-case methodology (CC-4, CC-5), the gap is named openly rather than hidden. S3 is downgraded accordingly: the force-unification claim is *aspirational*, pending the mechanism that closes the magnitude gap.

The gap does not falsify GCM's broader ontology (T1–T4). It localizes the hard theoretical work: either find a physically principled mechanism for short-range gravitational amplification, or restructure E2 as "competing attraction is the sign of a yet-to-be-specified short-range interaction in the graviton substrate."

## Recommendation

Run `/debate` on E2's framing before committing to the coherence paper. Specifically, stress-test:

- Whether any physically principled short-range amplification mechanism can close the $10^{40}$ gap without violating long-range Newtonian gravity.
- Whether the geometry-dependence of the apparent repulsion is compatible with the observed isotropic repulsion of real electrons at the same location.
- Whether competing attraction should be demoted from "the mechanism of electron repulsion" to "a compatible framing of electron-electron dynamics in the presence of heavy background matter."

## Verification stack (CC-7)

- ✅ Hand calculation of Newtonian forces
- ✅ Python numerical simulation with SI constants
- ✅ Sign check (both configurations — asymmetric and symmetric control)
- ✅ Order-of-magnitude comparison with Coulomb's law
- ✅ Dimensional analysis

See `verification.md` for details and `caveats.md` for caveats.
