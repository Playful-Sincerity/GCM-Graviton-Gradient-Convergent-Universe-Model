# R6 — Derivation: Geometric Time Dilation from Cluster Spacing

**Claim code:** R6
**Date:** 2026-04-23

---

## Premises

1. **(L3)** A photon is a traveling graviton-density structure with internal periodicity. Its wavelength $\lambda$ equals $N \cdot d$ where $d$ is the spacing between internal graviton clusters and $N$ is a fixed structural parameter.
2. **(Redshift)** A photon emitted at redshift $z$ is observed with wavelength $\lambda_{\text{obs}} = (1+z) \cdot \lambda_{\text{emit}}$. This is GCM-agnostic — whatever the redshift mechanism, this definition of $z$ is how observed wavelength relates to emitted wavelength.
3. **(Information propagation)** Information encoded in the photon's structure — phase, modulation, wave-train identity, the "start" and "end" of a pulse — is communicated by the arrival of successive graviton clusters at the observer. The clusters travel at the **photon speed $v$**, which is strictly less than $c$. Per the GCM speed-of-causality principle ([`theory/speed-of-causality-principle.md`](../../speed-of-causality-principle.md)): $v = c - 0_x$ where $0_x$ is an IVNA indexed infinitesimal (energy-dependent). The photon's composite massive structure forbids it from reaching $c$ exactly; $c$ is the causality limit, not the light speed. Numerically $v \approx c$ to within $\sim 10^{-37}$ parts for any observable photon, so the substitution of $v$ for $c$ in the derivation is not a numerical correction — it is a conceptual one GCM is committed to.

---

## Step 1 — Cluster Spacing Scales with $(1+z)$

From L3 (with $N$ constant between emission and observation):

$$d_{\text{obs}} = \frac{\lambda_{\text{obs}}}{N} = \frac{(1+z) \cdot \lambda_{\text{emit}}}{N} = (1+z) \cdot d_{\text{emit}}$$

So the observed cluster spacing is $(1+z)$ times the emitted cluster spacing.

---

## Step 2 — Time Between Cluster Arrivals

Two successive clusters in the photon's structure, separated by distance $d$, both travel at the photon speed $v$ (where $v = c - 0_x < c$) toward the observer. The first cluster arrives at time $t_1$; the second arrives at time $t_2$. The time between arrivals is:

$$\Delta t = t_2 - t_1 = \frac{d}{v}$$

This follows because in the frame of propagation, the two clusters are a fixed distance $d$ apart and travel at the same speed, so the second arrives after the first by exactly $d/v$.

**At emission:**
$$\Delta t_{\text{emit}} = \frac{d_{\text{emit}}}{v_{\text{emit}}}$$

**At observation:**
$$\Delta t_{\text{obs}} = \frac{d_{\text{obs}}}{v_{\text{obs}}} = \frac{(1+z) \cdot d_{\text{emit}}}{v_{\text{obs}}}$$

**Remark on $v_{\text{emit}}$ vs. $v_{\text{obs}}$:** Because the photon's energy decreases under redshift, its speed $v$ also decreases slightly (per L2's $v = c\sqrt{1 - (m_\gamma c^2/E)^2}$). The ratio $v_{\text{emit}}/v_{\text{obs}} = 1 + \delta$ where $\delta \sim (m_\gamma c^2 / E)^2 \sim 10^{-37}$ for any observable photon. This correction is utterly undetectable. Treating $v_{\text{emit}} \approx v_{\text{obs}}$ introduces an error of order $10^{-37}$, far below the 0.005 precision of the DES 2024 measurement. So:

$$\Delta t_{\text{obs}} \approx \frac{(1+z) \cdot d_{\text{emit}}}{v_{\text{emit}}} = (1+z) \cdot \Delta t_{\text{emit}}$$

with the understanding that the "$\approx$" hides a term of order $10^{-37}$, not a term of order $c = 0$.

---

## Step 3 — Time Dilation Factor

The ratio of observed to emitted inter-cluster timing is:

$$\boxed{\frac{\Delta t_{\text{obs}}}{\Delta t_{\text{emit}}} = (1+z)}$$

This is the time dilation of the photon's information stream. Any periodic signal encoded in the photon's structure — including the light curve of a supernova viewed through the photon's pulse — will be observed to pass at a rate $1/(1+z)$ times the emitted rate.

**Explicit form:** If a supernova emits a light curve with characteristic timescale $T_{\text{emit}}$, the observer sees a light curve with characteristic timescale:

$$T_{\text{obs}} = (1+z) \cdot T_{\text{emit}}$$

---

## Step 4 — Comparison to DES 2024

DES 2024 (arXiv:2406.05050) measured the SNe Ia light-curve time-dilation scaling to be:

$$T_{\text{obs}} / T_{\text{emit}} = (1+z)^{\alpha}, \quad \alpha = 1.003 \pm 0.005$$

with ~200σ significance against $\alpha = 0$ (tired-light hypothesis).

**R6 prediction:** $\alpha = 1.000$ (exact).

**Comparison:** $1.000 \in [0.998, 1.008]$, the 1σ error band on DES's $\alpha$. R6 is consistent with the measurement at better than 1σ.

**What R6 does not explain:** The specific value $0.003$ in DES's measured exponent. This could reflect:
- A genuine small deviation from linear scaling (possibly requiring a more detailed GCM treatment).
- Systematic errors in DES's analysis (K-corrections, evolution effects, stretch-color relations).
- Just statistical noise — $1.000$ and $1.003$ differ by $0.6\sigma$, which is not a meaningful difference.

R6 does not currently distinguish between these possibilities, and the DES data alone cannot exclude $\alpha = 1.000$.

---

## Step 5 — Independence From Redshift Mechanism

Crucially, Step 1 did not specify *why* $\lambda_{\text{obs}} = (1+z) \cdot \lambda_{\text{emit}}$. It only used the definition of $z$. Therefore R6 operates as a time-dilation companion for **any** redshift mechanism, as long as that mechanism stretches the wavelength:

- If R1 (space friction) stretches $\lambda$ by $(1+z)$, R6 gives $(1+z)$ time dilation.
- If R2 (void decompression) stretches $\lambda$ by $(1+z)$, R6 gives $(1+z)$ time dilation.
- If a hybrid mechanism stretches $\lambda$ by $(1+z)$, R6 gives $(1+z)$ time dilation.

This is the load-bearing insight: in GCM's framework, redshift and time dilation are the same phenomenon viewed at different scales — the photon's wavelength is its cluster spacing, and stretching the cluster spacing stretches the temporal rhythm of information carried by the cluster sequence.

---

## Dimensional Consistency

- $d$: [m]
- $v$: [m/s] (photon speed, $v < c$)
- $\Delta t = d/v$: [m]/[m/s] = [s] ✓

The ratio $\Delta t_{\text{obs}} / \Delta t_{\text{emit}}$ is dimensionless, as required for a time-dilation factor. ✓

$(1+z)$ is dimensionless. ✓

**Note on $c$ vs. $v$:** In this derivation $c$ never appears as the speed of the photon. $c$ is reserved for the causality limit — the fundamental speed at which nothing in GCM can travel. The photon's speed $v$ is strictly less than $c$ by $0_x$ (IVNA indexed infinitesimal, energy-dependent). See `theory/speed-of-causality-principle.md` for the full convention.
