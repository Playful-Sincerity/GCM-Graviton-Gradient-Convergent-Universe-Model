# M3 — Derivation

## Inputs

1. **Hubble radius.** The radius of the observable universe is $R_H \approx 4.4 \times 10^{26}$ m. This is the standard approximation $R_H \approx c / H_0$ with $H_0 \approx 70$ km/s/Mpc, multiplied by the ~3.25 factor that accounts for the proper distance to the particle horizon in a flat $\Lambda$CDM universe. The specific value we adopt here follows the session brief.

2. **Planck length.** $\ell_P = \sqrt{\hbar G / c^3} \approx 1.616 \times 10^{-35}$ m.

3. **Assumption.** One graviton per Planck cell $\ell_P^3$, uniformly packed.

## Derivation

Volume of the observable universe (sphere):

$$V_\text{universe} = \frac{4}{3} \pi R_H^3$$

Volume per graviton:

$$V_P = \ell_P^3$$

Graviton count:

$$N = \frac{V_\text{universe}}{V_P} = \frac{(4/3) \pi R_H^3}{\ell_P^3}$$

## Dimensional Check

$$[R_H^3] = \text{m}^3, \quad [\ell_P^3] = \text{m}^3, \quad [N] = \frac{\text{m}^3}{\text{m}^3} = \text{dimensionless (count)} \ \checkmark$$

## Numerical Substitution

$R_H^3 = (4.4 \times 10^{26})^3 = 8.518 \times 10^{79}$ m³.

$(4/3) \pi R_H^3 = (4/3) \cdot 3.1416 \cdot 8.518 \times 10^{79} = 3.568 \times 10^{80}$ m³.

$\ell_P^3 = (1.616 \times 10^{-35})^3 = 4.222 \times 10^{-105}$ m³.

$$N = \frac{3.568 \times 10^{80}}{4.222 \times 10^{-105}} = 8.45 \times 10^{184}$$

So $N \approx 8.5 \times 10^{184} \approx 10^{185}$, matching the session brief's stated value.

## Comparison to Baryon Count

Observable-universe baryon count: $N_b \approx 10^{80}$.

$$\frac{N}{N_b} = \frac{8.45 \times 10^{184}}{10^{80}} \approx 10^{105}$$

Session brief's expected ratio: $\sim 10^{105}$. ✓

This ratio says that, per GCM, there are $\sim 10^{105}$ gravitons in the observable universe for every baryon (proton or neutron). Given that M1 puts $\sim 4 \times 10^{59}$ gravitons *inside* each neutron, the remaining $\sim 10^{105} / 10^{59} \approx 10^{46}$ "extra" gravitons per baryon occupy the vast intervening space. This is consistent with T1's "gravitons are the substrate, not the exception."

## Comparison to Holographic Bound

The Bekenstein-Hawking entropy of a sphere of radius $R_H$:

$$S_\text{BH} \sim \left( \frac{R_H}{\ell_P} \right)^2 = (2.72 \times 10^{61})^2 \approx 7.4 \times 10^{122}$$

$S_\text{BH}$ scales as $R^2$ (surface area); $N$ scales as $R^3$ (volume). Their ratio:

$$\frac{N}{S_\text{BH}} = \frac{8.5 \times 10^{184}}{7.4 \times 10^{122}} \approx 10^{62}$$

M3's volume-count vastly exceeds the holographic surface-entropy bound. **This is expected.** The holographic bound is the maximum information content (in bits) of a region bounded by a surface of area $A$. GCM's $N$ is a *bulk count* of substrate cells, not an information bound. They are different quantities — apples and oranges — and the fact that $N \gg S_\text{BH}$ does not contradict the holographic principle.

**Honesty note:** if one took GCM seriously as a *quantum information* theory, $N$ would have to be reconciled with the holographic bound (likely by arguing that most gravitons are correlated and do not contribute independent bits). That reconciliation is not attempted here. M3 is a classical dimensional estimate, not a quantum-information claim.

## Sensitivity to Inputs

$N$ scales as $R_H^3 / \ell_P^3$. A 10% error in $R_H$ shifts $N$ by ~30%. The Hubble radius itself is uncertain at the ~5% level (depending on which value of $H_0$ you trust, given the current Hubble tension). Either way, the order of magnitude ($10^{184}$–$10^{185}$) is robust.
