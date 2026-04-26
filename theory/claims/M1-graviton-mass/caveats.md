# M1 — Caveats

## What This Proves

- **Dimensional consistency.** $m_g = \rho_\text{bound} \cdot \ell_P^3$ has units of mass.
- **Consistency with LIGO.** At nuclear-scale $\rho_\text{bound}$, GCM's graviton mass is ~28 orders of magnitude below the LIGO bound from gravitational-wave dispersion.
- **Internal consistency with T1.** A neutron composed of ~$4 \times 10^{59}$ gravitons is consistent with §H6's $m = m_g \cdot \xi$ relation, where $\xi$ is the graviton count.

## What This Does Not Prove

- **Not a first-principles derivation of $m_g$.** The value is a product of two provisional inputs: the Planck length (universally adopted, motivated but not derived from GCM) and the assumed maximum density (nuclear scale, flagged as open question OQ-2 in `gcm_v2.md`).
- **Not a prediction.** A measured graviton mass would test the formula. No such measurement exists, and the claimed $m_g$ is many orders of magnitude below any conceivable near-term experimental sensitivity.
- **Not a resolution of OQ-4.** The vacuum graviton density $\rho_0$ — distinct from the maximum packing density $\rho_\text{bound}$ — remains undefined. All density *gradients* are defined relative to $\rho_0$; no particle property can be finalized until $\rho_0$ is specified.

## Open Questions Inherited

- **OQ-2.** Why is $\rho_\text{bound} = \rho_\text{nuclear}$? Planck density is ~78 orders higher. A first-principles argument (e.g., stability of graviton close-packing at a specific density scale) is needed.
- **OQ-4.** What is $\rho_0$? All of GCM's gradient machinery depends on a defined vacuum graviton density.
- **"Planck's constant = graviton mass" claim** (§H1 v2). Dimensionally broken ($h$ is action, not mass). Pending formulation.

## The Planck-Density Limit (check 5)

The session brief's check 5 ("at $\rho_\text{bound} \to \rho_\text{Planck}$, $m_g$ should stay consistent with LIGO") is physically incoherent: the formula $\rho \cdot \ell_P^3$ evaluated at Planck density necessarily returns the Planck mass ($2.18 \times 10^{-8}$ kg), which exceeds the LIGO bound by ~51 orders of magnitude. This does not undermine the claim — GCM never asserts $\rho_\text{bound} = \rho_\text{Planck}$. It does, however, convert the LIGO bound into a constraint on $\rho_\text{bound}$: LIGO requires $\rho_\text{bound} \lesssim 4 \times 10^{45}$ kg/m³. Nuclear density satisfies this by 27 orders.

If a future physicist audits M1, they will likely frame this identically. Acknowledging it upfront preserves honesty.

## Framing for the Coherence Paper

M1 should be presented in the main body as: *"Given Tenet T1 and the provisional nuclear-density packing bound, the graviton mass scale is ~$10^{-87}$ kg, which satisfies the LIGO bound by 28 orders of magnitude."* The *structural* claim — $m_g \sim \rho_\text{bound} \cdot \ell_P^3$ — is load-bearing; the *numerical* value depends on OQ-2 and shifts linearly with $\rho_\text{bound}$.

## Relationship to Other Claims

- **M3 (Planck-cell count):** shares the Planck-volume assumption. If $\ell_P$ is revised or the graviton volume is not exactly $\ell_P^3$, both M1 and M3 update in tandem.
- **E7 (charge-mass compensation):** independent.
- **Q3 (E·P invariant):** independent, but the idea that hydrogen's electron is a configuration of ~$10^{59}$ gravitons × (number of electrons) is implicit in GCM's composite-particle reading.
- **L2 (photon speed):** independent at the formula level, but the GCM photon-mass ($\sim 10^{-54}$ kg) and graviton mass ($\sim 10^{-87}$ kg) differ by $\sim 10^{33}$, implying a photon is ~$10^{33}$ gravitons — a number to reconcile with GCM's photon-as-traveling-structure reading.
