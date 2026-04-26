# E2 — Derivation: Competing-Attraction Toy Model

## Setup (asymmetric geometry — Configuration A)

One heavy positive mass at the origin, representing a proton or a local concentration of positive matter:
$$P:\; x_P = 0, \quad m_P = m_p = 1.673\times 10^{-27}\,\mathrm{kg}.$$

Two electrons at positions on the $+x$ axis:
$$E_1:\; x_1 = d = a_0, \qquad E_2:\; x_2 = d + r,\quad r = a_0.$$

Here $a_0 = 5.29\times 10^{-11}\,\mathrm{m}$ is the Bohr radius, used as a natural length scale. Both electrons have mass $m_e = 9.109\times 10^{-31}\,\mathrm{kg}$.

This geometry puts both electrons on the *same side* of the heavy attractor. This is the minimal non-trivial case that can produce apparent inter-electron repulsion through competing attraction.

## Force on $E_1$

All forces are along the $x$-axis (1D).

**From the proton at origin.** Distance $|x_1 - x_P| = d$. Force on $E_1$ is attractive, directed toward $P$, i.e., in the $-x$ direction:
$$F^{(E_1)}_{P} = -\frac{G\,m_e\,m_p}{d^2}.$$

**From $E_2$ at $x_2 = d + r$.** Distance $r$. Force on $E_1$ is attractive, directed toward $E_2$, i.e., in the $+x$ direction:
$$F^{(E_1)}_{E_2} = +\frac{G\,m_e\,m_e}{r^2}.$$

**Total force on $E_1$:**
$$F^{(E_1)}_{\rm tot} = -\frac{G\,m_e\,m_p}{d^2} + \frac{G\,m_e^2}{r^2}.$$

## Force on $E_2$

**From the proton at origin.** Distance $d + r$. Force is attractive toward $P$, in $-x$ direction:
$$F^{(E_2)}_{P} = -\frac{G\,m_e\,m_p}{(d+r)^2}.$$

**From $E_1$ at $x_1 = d$.** Distance $r$. Force is attractive toward $E_1$, in $-x$ direction (since $x_1 < x_2$):
$$F^{(E_2)}_{E_1} = -\frac{G\,m_e^2}{r^2}.$$

**Total force on $E_2$:**
$$F^{(E_2)}_{\rm tot} = -\frac{G\,m_e\,m_p}{(d+r)^2} - \frac{G\,m_e^2}{r^2}.$$

## Relative acceleration

The accelerations are $\ddot{x}_i = F^{(E_i)}_{\rm tot}/m_e$, so
$$\ddot{x}_{E_1} = -\frac{G\,m_p}{d^2} + \frac{G\,m_e}{r^2},$$
$$\ddot{x}_{E_2} = -\frac{G\,m_p}{(d+r)^2} - \frac{G\,m_e}{r^2}.$$

The rate of change of the inter-electron separation is
$$\ddot{r} \equiv \ddot{x}_{E_2} - \ddot{x}_{E_1} = G\,m_p\left(\frac{1}{d^2} - \frac{1}{(d+r)^2}\right) - \frac{2\,G\,m_e}{r^2}.$$

The first term is **positive** (since $d < d+r$, so $1/d^2 > 1/(d+r)^2$) — this is the "gradient" of the proton's attractive field: $E_1$ is pulled harder toward the proton than $E_2$ is, so $E_1$ accelerates in $-x$ faster than $E_2$, meaning the separation $r$ grows. This is the competing-attraction effect.

The second term is **negative** and represents the direct gravitational attraction between the two electrons, which would shrink the separation if it were alone.

Whether the net $\ddot{r}$ is positive (apparent repulsion) depends on the ratio
$$\frac{m_p\left[\frac{1}{d^2} - \frac{1}{(d+r)^2}\right]}{2\,m_e/r^2} = \frac{m_p}{2\,m_e}\cdot \frac{r^2 \left(\frac{1}{d^2} - \frac{1}{(d+r)^2}\right)}{1}.$$

With $m_p/m_e \approx 1836$ and a geometry where $d \sim r \sim a_0$, the proton-gradient term overwhelmingly dominates:

At $d = r = a_0$:
$$\frac{1}{d^2} - \frac{1}{(d+r)^2} = \frac{1}{a_0^2} - \frac{1}{(2 a_0)^2} = \frac{3}{4 a_0^2}.$$

Ratio = $\dfrac{1836}{2}\cdot\dfrac{3}{4} \approx 688$ — the proton-gradient term is ~700× larger than the direct electron-electron attraction. Net $\ddot{r}$ is positive.

## Numerical result

Substituting SI values:

```
F_E1_from_proton  = -3.634e-47 N
F_E1_from_E2      = +1.979e-50 N
Net F on E1       = -3.632e-47 N     (toward origin)

F_E2_from_proton  = -9.086e-48 N
F_E2_from_E1      = -1.979e-50 N
Net F on E2       = -9.106e-48 N     (toward origin)

a_E1 = -3.988e-17 m/s^2
a_E2 = -9.997e-18 m/s^2
ddot(r) = a_E2 - a_E1 = +2.988e-17 m/s^2   (POSITIVE: apparent repulsion)
```

## Equivalent repulsive force

For a two-body problem with reduced mass $\mu = m_e/2$, an effective *repulsive* inter-particle force that would produce the observed $\ddot{r}$ is
$$F_{\rm eff} = \mu\,\ddot{r} = \frac{m_e}{2}\cdot 2.988\times 10^{-17}\,\mathrm{m/s^2} \approx +1.361\times 10^{-47}\,\mathrm{N}.$$

## Comparison with Coulomb

Coulomb repulsion at $r = a_0$:
$$F_C = \frac{k_C\,e^2}{r^2} = \frac{(8.988\times 10^{9})(1.602\times 10^{-19})^2}{(5.29\times 10^{-11})^2} \approx 8.24\times 10^{-8}\,\mathrm{N}.$$

Ratio:
$$\frac{F_{\rm eff}}{F_C} = \frac{1.361\times 10^{-47}}{8.24\times 10^{-8}} \approx 1.65\times 10^{-40}.$$

Equivalently, competing-attraction repulsion is **six orders of ten thousand times** weaker than Coulomb repulsion — about a factor of $6\times 10^{39}$ too small.

## Control calculation — Configuration B (symmetric)

For completeness, we repeat the calculation with the proton *between* the two electrons:
$$P:\; x_P = 0, \quad E_1:\; x_1 = -a_0, \quad E_2:\; x_2 = +a_0.$$

By symmetry, each electron feels equal and opposite force toward the origin:
```
a_E1 = +3.991e-17 m/s^2   (in +x, toward origin)
a_E2 = -3.991e-17 m/s^2   (in -x, toward origin)
ddot(r) = a_E2 - a_E1 = -7.981e-17 m/s^2   (NEGATIVE: apparent attraction)
```

In the symmetric configuration, both electrons are pulled toward the central proton, which puts them on a collision course with each other. Competing attraction here produces apparent *attraction*, not repulsion.

**This confirms that the sign of E2's "repulsion" is geometry-dependent, not intrinsic.**

## Dimensional check

$[G\,m_p/d^2] = \dfrac{(\mathrm{m}^3\mathrm{kg}^{-1}\mathrm{s}^{-2})(\mathrm{kg})}{\mathrm{m}^2} = \mathrm{m\,s^{-2}}$ — matches acceleration units. ✅

$[F_{\rm eff}] = [\mu][\ddot{r}] = \mathrm{kg}\cdot\mathrm{m\,s^{-2}} = \mathrm{N}$. ✅

## Summary of the derivation

The calculation shows:

1. In asymmetric geometry with a heavy attractor off to one side, competing attraction *does* produce relative acceleration consistent with apparent repulsion.
2. The sign is correct; the magnitude is off by $\sim 10^{40}$.
3. In symmetric geometry, competing attraction produces apparent attraction instead.
4. The mechanism is real but is only part of the picture. Real electron-electron repulsion is observed to be isotropic and Coulomb-strong; competing attraction alone reproduces neither of those properties.

The derivation is exact within its assumptions (1D, pointlike masses, Newtonian gravity). The question for GCM is not whether the math is right but whether the interpretation survives scrutiny. See `caveats.md` for known issues.
