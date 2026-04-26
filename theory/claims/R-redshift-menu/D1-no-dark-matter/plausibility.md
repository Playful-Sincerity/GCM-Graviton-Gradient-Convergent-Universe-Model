# D1 — Plausibility

## Why D1 Deserves Engagement

The "dark matter particle" hypothesis is not confirmed. Decades of direct detection experiments (XENON, LUX, PICO, CDMS, PandaX) have produced null results for WIMPs across the theoretically motivated mass-cross-section space. Profumo (2024) wrote about the "waning of the WIMP": the paradigm has not been ruled out but has been unable to produce a positive signal, and the community is increasingly diversifying into alternative candidates (axions, sterile neutrinos, fuzzy DM, PBHs, and modified-gravity alternatives).

The empirical door to "dark matter is not a new particle" is more open now than it has been in decades. D1 is GCM's entry into this space.

## The Profumo PBH Program

Stefano Profumo (UCSC) leads one of the most rigorous programs attempting to account for dark-matter phenomenology without new-particle dark matter. Key results (from the `2026-04-23-adjacent-programs.md` research):

- **Lehmann, Profumo & Yant (2018, JCAP 2018:007).** Maximal-density mass function for PBH dark matter. Establishes the framework for PBH-as-DM constraints.
- **Smyth, Profumo et al. (2019, arXiv:1910.01285).** Updated microlensing constraints showing the asteroid-mass window is weaker than previously thought.
- **Koulen, Profumo & Smyth (2025, PRD).** PBHs above ~100 $M_{\odot}$ accelerate Population III star formation — potentially explaining JWST early massive black hole anomalies.

The program is active, peer-reviewed, and producing results. D1's positioning toward Profumo is strategic: GCM's "matter whose light doesn't reach us" claim structurally contains PBHs as a specific case, and Profumo has already done the quantitative constraint work.

## Why the Asteroid-Mass Window Matters

At $10^{17}$–$10^{23}$ g ($\sim 10^{-16}$–$10^{-10} M_{\odot}$), PBHs are:

- **Small enough to escape all current microlensing:** optical surveys with observation cadences of minutes to hours cannot detect PBHs in this range (Einstein-ring crossing is too fast).
- **Small enough to evade femtolensing bounds:** the Barnacka gamma-ray-burst bounds constrain $10^{16}$–$10^{17}$ g but weaken at $10^{18}$+.
- **Large enough that Hawking evaporation timescales exceed the age of the universe:** $\tau_{\text{evap}} \gg t_{\text{universe}}$ for $M \gtrsim 10^{15}$ g.
- **Dim enough that Hawking radiation is undetectable despite being hot:** At $M = 10^{17}$ kg ($= 10^{20}$ g), the Hawking temperature is actually $T_H \approx 1.23 \times 10^6$ K — about 5 orders of magnitude *above* the CMB, not below. But the Schwarzschild radius is only $r_s = 2GM/c^2 \approx 1.5 \times 10^{-10}$ m (atomic scale), so the emitting area $4\pi r_s^2 \approx 2.8 \times 10^{-19}$ m² is tiny. Stefan-Boltzmann gives total Hawking luminosity $L \sim \sigma T_H^4 \cdot 4\pi r_s^2 \approx 36$ mW per PBH — cosmically negligible. At typical cosmic inter-PBH spacing (~2000 AU) and detector areas, no individual asteroid-mass PBH produces a detectable flux. *Asteroid-mass PBHs are observationally hidden by their vanishing luminosity, not by low temperature.* Verified in `verification/check_03_hawking_temperature.py` + `.wls` (solar-mass calibration reproduces textbook $T_H(M_\odot) = 6.17 \times 10^{-8}$ K to 3+ figures, confirming the formula).
- **Numerous enough to account for all DM:** $N_{\text{PBH}} \sim 10^{25}$ in a Milky Way halo at $10^{20}$ g each.

This is the one PBH mass range where $f_{\text{PBH}} = 1$ (all DM is PBH) is currently allowed by observational bounds. D1's quantitative case runs through this window.

## Order-of-Magnitude Check

**Total dark matter in the observable universe:** $\Omega_{\text{DM}} h^2 \sim 0.12$; with $\Omega_{\text{DM}} \sim 0.26$, mean DM density $\rho_{\text{DM}} \sim 2.4 \times 10^{-27}$ kg/m$^3$.

**PBH number density if all DM is asteroid-mass PBHs at $10^{20}$ g $= 10^{17}$ kg:**

$$n_{\text{PBH}} = \rho_{\text{DM}} / M_{\text{PBH}} \sim 2.4 \times 10^{-44} \text{ m}^{-3}$$

Mean inter-PBH spacing:

$$d_{\text{PBH}} = n_{\text{PBH}}^{-1/3} \sim 3.5 \times 10^{14} \text{ m} \sim 2000 \text{ AU}$$

Spacing of a few thousand AU between asteroid-mass PBHs is consistent with none of them being found in the solar system, since at typical Oort-cloud distances the probability of one being within detection range is low. Plausible.

## Structural Consistency with GCM

In GCM, there is no privileged matter category. Everything is graviton density structures. PBHs are high-density graviton structures; ordinary stars are lower-density structures; cold gas is even lower. The distinction "dark" vs. "visible" is about EM coupling to these structures, not about their fundamental nature.

This makes D1 ontologically natural in GCM. In $\Lambda$CDM, "dark matter particle" requires an entire new sector of physics. In GCM, "matter we can't see" is just a configuration we didn't happen to anticipate.

## What Plausibility Doesn't Establish

1. **Halo shape.** Rotation curves fit NFW or Einasto profiles. D1 needs to show why invisible ordinary matter would distribute this way. PBHs from primordial-era production could plausibly follow these profiles (if their formation mechanism correlates with primordial density peaks), but this is not derived.

2. **CMB consistency.** At recombination, the universe had a specific dark-to-baryon matter ratio that shapes the acoustic peaks. PBHs formed well before recombination act like "cold dark matter" in the CMB perspective — they are gravitationally relevant but don't couple to photons as baryons do. This is actually a favorable feature for D1: PBH-as-DM can reproduce the CMB acoustic structure in a way that "all baryons" cannot. Full quantitative check requires CMB power spectrum fits with PBH DM.

3. **Structure formation.** Large-scale structure in $\Lambda$CDM simulations forms correctly with particle DM. PBH DM would form structure similarly in principle (gravitationally cold, non-interacting with photons) but N-body simulations with PBH DM across all mass ranges have not been exhaustively performed.

## Where This Is Honest

D1 does not claim to solve dark matter. It claims: (a) the "it's a new particle" hypothesis is not confirmed; (b) there is enough room in invisible ordinary matter — specifically PBHs — to potentially account for observed DM phenomenology; (c) this is a live, peer-reviewed area of research (Profumo), not fringe.

The coherence paper should present D1 at exactly this level. Saying "GCM solves dark matter" would be overclaim. Saying "GCM is consistent with the PBH-as-DM program currently being pursued by serious physicists, and PBHs are a specific instance of what GCM predicts (ordinary matter we can't see)" is honest and strategically strong.
