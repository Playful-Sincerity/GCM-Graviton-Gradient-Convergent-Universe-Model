# L2 — Derivation

## Starting Point — Energy-Momentum Relation

For a relativistic particle with rest mass $m_0$, total energy $E$, and momentum $p$:

$$E^2 = (pc)^2 + (m_0 c^2)^2$$

Solve for momentum:

$$p = \frac{1}{c} \sqrt{E^2 - (m_0 c^2)^2}$$

The group velocity (the speed of a localized wave packet) is:

$$v = \frac{\partial E}{\partial p}$$

From $E = \sqrt{(pc)^2 + (m_0 c^2)^2}$:

$$\frac{\partial E}{\partial p} = \frac{pc^2}{E} = \frac{pc^2}{\sqrt{(pc)^2 + (m_0 c^2)^2}}$$

Substituting $pc = \sqrt{E^2 - (m_0 c^2)^2}$:

$$v = \frac{c^2 \sqrt{E^2 - (m_0 c^2)^2}}{c \cdot E} = c \sqrt{1 - \left( \frac{m_0 c^2}{E} \right)^2}$$

## Taylor Expansion for Small $m_0$

When $m_0 c^2 \ll E$:

$$v = c \sqrt{1 - \varepsilon^2} \approx c \left( 1 - \tfrac{1}{2} \varepsilon^2 - \tfrac{1}{8} \varepsilon^4 - \cdots \right), \quad \varepsilon \equiv \frac{m_0 c^2}{E}$$

Keeping the leading term:

$$\Delta v \equiv c - v \approx \tfrac{1}{2} c \, \varepsilon^2 = \tfrac{1}{2} c \cdot \left( \frac{m_0 c^2}{E} \right)^2$$

## Numerical Substitution

For $m_0 = 10^{-54}$ kg and $E = 1$ eV:

- $m_0 c^2 = 10^{-54} \cdot (2.998 \times 10^8)^2 = 8.988 \times 10^{-38}$ J
- $E = 1$ eV $= 1.602 \times 10^{-19}$ J
- $\varepsilon = (m_0 c^2)/E = 5.61 \times 10^{-19}$
- $\varepsilon^2 = 3.15 \times 10^{-37}$
- $\Delta v = \tfrac{1}{2} c \varepsilon^2 = \tfrac{1}{2} (2.998 \times 10^8) \cdot (3.15 \times 10^{-37}) = 4.72 \times 10^{-29}$ m/s

Session brief stated value: $\Delta v \approx 4.74 \times 10^{-29}$ m/s. Our computed value: $4.72 \times 10^{-29}$ m/s. Agreement to within 0.4% (well within the rounding of the stated inputs $m_0 = 10^{-54}$ kg and $E = 1$ eV).

## Note on Floating-Point Precision

Direct computation of $v = c\sqrt{1 - \varepsilon^2}$ in standard double-precision floating point gives $v = c$ identically (no departure visible) because $\varepsilon^2 \sim 10^{-37}$ is far below the double-precision epsilon ($\sim 10^{-16}$). **To see the departure from $c$, one must use the Taylor expansion.** This is a computational artifact, not a physics issue — the formula is exact; the floating-point representation cannot resolve $c - v$ at this scale. Higher-precision arithmetic (e.g., `mpmath` at 100+ decimal digits) would recover the direct computation; the Taylor result is correct and preferred here for clarity.

## Dimensional Check

$$[v] = \text{m/s}, \quad [c] = \text{m/s}, \quad \left[ \frac{m_0 c^2}{E} \right] = \frac{\text{kg} \cdot \text{m}^2/\text{s}^2}{\text{J}} = \frac{\text{J}}{\text{J}} = \text{dimensionless}$$

So $v = c \cdot \sqrt{\text{dimensionless}}$ has units of m/s. ✓

## Limit Case — $m_0 \to 0$

$$\lim_{m_0 \to 0} v = c \cdot \sqrt{1 - 0} = c$$

The speed reduces exactly to $c$ in the massless limit, recovering the standard-model photon. ✓

## Order-of-Magnitude Sanity

$\Delta v / c \approx \varepsilon^2 / 2 = 1.57 \times 10^{-37}$.

For reference:
- Best direct measurements of $c$ have fractional precision $\sim 10^{-9}$.
- Constraints on Lorentz invariance via MMX-type experiments approach $10^{-18}$.
- GIM-type constraints on photon dispersion from $\gamma$-ray bursts are $\sim 10^{-15}$.

GCM's $\Delta v / c \sim 10^{-37}$ is ~19 orders below the best current measurements of dispersion. Not measurable in any foreseeable experiment.
