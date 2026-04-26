# S5.5(a) — Newtonian Gravity as a Limit of the Minimal Model

**Claim code:** S5.5(a)
**Epistemic tier:** 🟢 Green
**Date:** 2026-04-23
**Verification:** Hand derivation + dimensional check + limit case. All three pass.

---

## The Claim

For two composite particles (each made of many gravitons) at separations large compared to their internal extents, with densities that are locally smooth, the minimal-model equation
$$\ddot{\mathbf{x}}_i = \sum_{j\neq i} \frac{G\,m_g}{\max(r_{ij},\,\ell_{\min})^2}\,\hat{r}_{ij}$$
reduces to Newton's law of universal gravitation
$$\mathbf{F}_{1\to 2} = -\,G\,\frac{m_1 m_2}{r^2}\,\hat{r}_{12}$$
with the same $G$ appearing in both. Here $m_i = m_g \xi_i$ is the composite mass (H6 from v2), $r$ is the center-of-mass separation, and $\hat{r}_{12}$ points from 1 toward 2.

---

## Derivation

### Step 1 — Force on a Single Graviton

From the minimal-model equation, the acceleration of graviton $i$ due to all others is the vector sum of $G m_g / r_{ij}^2$ terms along $\hat{r}_{ij}$. Multiplying by $m_g$ gives the net force on graviton $i$:

$$\mathbf{F}_i = \sum_{j\neq i} \frac{G m_g^2}{r_{ij}^2}\,\hat{r}_{ij}$$

(Here we take separations $r_{ij}$ well above the $\ell_{\min}$ floor — the regime of interest for macroscopic gravity.)

### Step 2 — Total Force Between Two Composite Particles

Consider two composite particles, $A$ with gravitons $\{a_1, \ldots, a_{\xi_A}\}$ and $B$ with gravitons $\{b_1, \ldots, b_{\xi_B}\}$. The total gravitational force of $B$ on $A$ is:

$$\mathbf{F}_{B\to A} = \sum_{a\in A}\sum_{b\in B} \frac{G m_g^2}{r_{ab}^2}\,\hat{r}_{ab}$$

This is a double sum over all cross-pairs (graviton in $A$, graviton in $B$). Internal forces within $A$ or within $B$ cancel internally and do not contribute to the center-of-mass acceleration of either composite.

### Step 3 — Large-Separation Limit

Let $\mathbf{r}_A$, $\mathbf{r}_B$ be the centers of mass of $A$ and $B$. Write $\mathbf{x}_a = \mathbf{r}_A + \boldsymbol{\delta}_a$ where $\boldsymbol{\delta}_a$ is the graviton's displacement from the composite COM, and similarly for $b$. Then:

$$\mathbf{r}_{ab} = (\mathbf{r}_B - \mathbf{r}_A) + (\boldsymbol{\delta}_b - \boldsymbol{\delta}_a) \equiv \mathbf{r} + \boldsymbol{\epsilon}_{ab}$$

where $\mathbf{r} = \mathbf{r}_B - \mathbf{r}_A$ is the COM separation and $|\boldsymbol{\epsilon}_{ab}| \ll |\mathbf{r}|$ by assumption (large-separation limit).

Expand $1/r_{ab}^2 \hat{r}_{ab}$ around $\mathbf{r}$. To zeroth order in $|\boldsymbol{\epsilon}_{ab}|/|\mathbf{r}|$:

$$\frac{\hat{r}_{ab}}{r_{ab}^2} \approx \frac{\hat{r}}{r^2}$$

The first-order corrections are tidal terms that, when summed over the two composite particles with locally-smooth densities, cancel by the standard multipole expansion argument (the dipole moment about each COM vanishes by definition of the COM; the quadrupole and higher moments fall off faster than $1/r^2$).

### Step 4 — Factorization

To leading order:

$$\mathbf{F}_{B\to A} \approx \frac{G m_g^2}{r^2}\,\hat{r}\;\sum_{a\in A}\sum_{b\in B} 1 = \frac{G m_g^2}{r^2}\,\hat{r}\;(\xi_A \xi_B)$$

Using $m_A = m_g \xi_A$, $m_B = m_g \xi_B$:

$$\mathbf{F}_{B\to A} = \frac{G\,(m_g \xi_A)(m_g \xi_B)}{r^2}\,\hat{r} = \frac{G\,m_A m_B}{r^2}\,\hat{r}$$

This is **Newton's law of universal gravitation**, attractive (directed from $A$ toward $B$), with the same constant $G$ that appeared in the minimal-model equation. □

---

## Verification

### Check 1 — Dimensional Analysis

Unit check on the final equation:
- $[G] = \text{m}^3/(\text{kg}\cdot\text{s}^2)$
- $[m_A m_B / r^2] = \text{kg}^2/\text{m}^2$
- $[F] = [G \cdot m_A m_B/r^2] = \text{m}^3/(\text{kg}\cdot\text{s}^2) \cdot \text{kg}^2/\text{m}^2 = \text{kg}\cdot\text{m}/\text{s}^2 = \text{N}$ ✓

Consistent. Newtons on both sides.

### Check 2 — Numerical Substitution

Earth-Moon system, to sanity-check:
- $m_E = 5.972 \times 10^{24}$ kg, $m_M = 7.342 \times 10^{22}$ kg
- $r_{EM} = 3.844 \times 10^{8}$ m
- $G = 6.674 \times 10^{-11}$ m³/(kg·s²)

$$F = \frac{6.674 \times 10^{-11} \times 5.972 \times 10^{24} \times 7.342 \times 10^{22}}{(3.844 \times 10^{8})^2}$$

Numerator: $6.674 \times 5.972 \times 7.342 \times 10^{-11+24+22} = 292.6 \times 10^{35} = 2.926 \times 10^{37}$
Denominator: $14.78 \times 10^{16} = 1.478 \times 10^{17}$
Result: $F \approx 1.98 \times 10^{20}$ N

Reference value: $\approx 1.98 \times 10^{20}$ N (standard textbook value for Earth-Moon gravitational force). ✓

### Check 3 — Limit Case

As $r \to \infty$, $F \to 0$. ✓ (Forces decrease with distance; force vanishes at infinite separation.)

As either $m_A \to 0$ or $m_B \to 0$, $F \to 0$. ✓ (No matter, no gravitational attraction.)

For $\xi_A = \xi_B = 1$ (two lone gravitons at large separation), we recover $F = G m_g^2/r^2$ — the minimal-model equation for two gravitons, consistent with the starting point. ✓

### Check 4 — Independent-Tool Computation (Wolfram Engine + SymPy + mpmath)

Closed 2026-04-24 via retrofit verification stack. See [`verification.md`](verification.md) for the full summary and links to scripts/outputs.

- **mpmath at 50-digit precision:** $F = 1.98055856502802840452 \times 10^{20}$ N (0.028% deviation from $1.98 \times 10^{20}$ textbook reference). Script: [`verification/check_02_earth_moon_numerical.py`](verification/check_02_earth_moon_numerical.py).
- **Wolfram Engine 14.3.0:** $F = 1.9805585650280287 \times 10^{20}$ N — agrees with mpmath to the 15th significant digit. Symbolic limits match SymPy. Script: [`verification/check_04_wolfram.wls`](verification/check_04_wolfram.wls).
- **SymPy symbolic limits and factorization:** All three limit cases ($r\to\infty$, $m_i\to 0$, $\xi_A=\xi_B=1$) and the load-bearing factorization $(m_g\xi_A)(m_g\xi_B) \to \xi_A\xi_B m_g^2$ pass. Script: [`verification/check_03_limit_cases_sympy.py`](verification/check_03_limit_cases_sympy.py).

No cross-tool disagreement.

---

## Verification Tally

**4/4 checks passed, cross-tool verified.** Claim S5.5(a) is 🟢 green. Full reproducible scripts archived at [`verification/`](verification/).

| Check | Method | Result |
|---|---|---|
| Dimensional analysis | SymPy `physics.units` + manual SI exponent check | ✓ PASS (both methods agree) |
| Numerical (mpmath, 50 dp) | $F = G M_E M_M / r^2$ from `inputs.json` | ✓ PASS (0.028% vs textbook) |
| Symbolic limits (SymPy) | $r\to\infty$, $m\to 0$, single-graviton, factorization | ✓ PASS (all five sub-checks) |
| Independent computation (Wolfram Engine 14.3.0) | Numerical + symbolic cross-check | ✓ PASS (agrees with mpmath to 15 digits) |

---

## Caveats

- **Large-separation, locally-smooth-density assumption.** The derivation assumes $|\boldsymbol{\epsilon}_{ab}| \ll r$. For compact particles at typical gravitational separations (astronomical distances), this is overwhelmingly satisfied. For strongly-interacting systems where particles overlap (nuclear and below), the derivation does not apply; GCM's E4 gradient-overlap mechanism handles those regimes (S3).
- **Tidal corrections.** The standard Newtonian law is the leading-order term. Higher multipoles (tidal interactions, $1/r^3$ and faster) emerge from the expansion and match the standard Newtonian tidal terms exactly.
- **Relativistic corrections not addressed here.** Post-Newtonian corrections (perihelion precession, gravitational wave emission, frame-dragging) are GR phenomena and require a GR-like expansion of GCM's substrate dynamics. This is part of the semiclassical GR limit problem discussed in S8 — it is NOT part of S5.5(a)'s green claim.
- **$\ell_{\min}$ floor.** The minimum-separation floor plays no role in the large-separation limit but matters at Planck-scale distances. Its value is not yet derived from GCM parameters.

---

## Relationship to Earlier Claims

- Uses H6 (v2) for the composite mass $m = m_g \xi$.
- Consistent with M1 (graviton mass from Planck scale and density bound) — $m_g$ is defined there.
- Independent of H2 (charge), H3 (Pauli), H4/H1 (magnetism), H5/H2 (heat). Only the gravity-between-gravitons part of the minimal model is used.
- Completes a long-standing requirement of GCM: that the program not only claim to unify forces, but also reproduce the classical gravity law we already know.
