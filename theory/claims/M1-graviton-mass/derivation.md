# M1 — Derivation

## Starting Points

Two physical postulates supply everything needed:

1. **Planck length as natural graviton extent.** The Planck length is the only length scale that can be built from $\hbar$, $G$, and $c$ alone:

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}} \approx 1.616 \times 10^{-35} \text{ m}$$

GCM identifies the Planck volume $V_P = \ell_P^3$ with the natural volume occupied by a single graviton at maximum packing.

2. **Maximum graviton packing density at nuclear scale.** Tenet T3 (softened per S1 Foundations) states that the maximum packing density of gravitons is *approximately* nuclear. The session brief uses $\rho_\text{bound} \approx 10^{18}$ kg/m³ as the round-number representative. This is a provisional choice (open question OQ-2).

## Derivation

Given (1) and (2), the mass of one graviton equals the mass contained in one Planck volume at maximum packing:

$$m_g = \rho_\text{bound} \cdot V_P = \rho_\text{bound} \cdot \ell_P^3$$

## Dimensional Check

$$[\rho_\text{bound}] = \frac{\text{kg}}{\text{m}^3}, \quad [\ell_P^3] = \text{m}^3$$

$$[\rho_\text{bound} \cdot \ell_P^3] = \frac{\text{kg}}{\text{m}^3} \cdot \text{m}^3 = \text{kg} \ \checkmark$$

## Numerical Substitution

$$V_P = \ell_P^3 = (1.616 \times 10^{-35})^3 = 4.222 \times 10^{-105} \text{ m}^3$$

$$m_g = (10^{18} \text{ kg/m}^3) \cdot (4.222 \times 10^{-105} \text{ m}^3) = 4.222 \times 10^{-87} \text{ kg}$$

## Gravitons per Neutron

$$N_g = \frac{m_\text{neutron}}{m_g} = \frac{1.675 \times 10^{-27} \text{ kg}}{4.222 \times 10^{-87} \text{ kg}} \approx 3.97 \times 10^{59}$$

Equivalently: a neutron is approximately $4 \times 10^{59}$ gravitons, consistent with Tenet T1 and §H6 of `gcm_v2.md` ($m_\text{particle} = m_g \cdot \xi$).

## Conversion to Electron-Volts (for comparison with LIGO)

$$m_g = 4.222 \times 10^{-87} \text{ kg} \cdot \frac{1 \text{ eV}/c^2}{1.783 \times 10^{-36} \text{ kg}} \approx 2.37 \times 10^{-51} \text{ eV}/c^2$$

The LIGO bound from gravitational-wave dispersion (Abbott et al., 2021) is $m_g < 10^{-23}$ eV/$c^2$. GCM's value sits 28 orders of magnitude below the bound.

## Structural Form of the Claim

The *structural* relation is $m_g \sim \rho_\text{bound} \cdot \ell_P^3$. The specific numerical value scales linearly with the assumed $\rho_\text{bound}$. Choosing $\rho_\text{neutron} = 4 \times 10^{17}$ kg/m³ (as in §H1 of v2) yields $m_g \approx 1.69 \times 10^{-87}$ kg; the order of magnitude and the LIGO margin are unchanged.
