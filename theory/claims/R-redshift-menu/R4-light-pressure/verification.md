# R4 — Verification Record

**Tally:** N/A — no tool-verifiable numerical claims.
**Last run:** 2026-04-24 (inspection only; no scripts needed)
**Tools:** N/A.
**Honesty note:** R4 is tier-🔴 Red in status.md precisely *because* it has no quantitative pressure-frequency relation. There is nothing to compute.

---

## Why No Scripts

R4's plausibility.md says:

> "$\nu_{\text{observed}} \propto \rho_g(\vec{r}_{\text{observer}})^k$ for some exponent $k$. This is a *placeholder* form — it is not derived from any underlying GCM dynamics."

And one dimensional sketch:

> "If $k \approx 1/3$ and $\Delta\rho_g/\rho_g \sim 1$ over the Hubble scale, then $\Delta\nu/\nu \sim 1/3$."

The sketch is trivially arithmetic ($1/3 \times 1 = 1/3$), not worth wrapping in a verification script. And the claim is explicitly flagged as placeholder, not derivation.

The one check that could be done — whether the placeholder form gives the observed Hubble relation — is meaningless without a specific $k$ and a specific $\rho_g(r)$ profile. Neither exists.

## Inherited Checks (via neighbors)

If R4 is a cousin of R2 (path-integrated pressure effect), it inherits R2's numerical scaffolding — the same $H_0/c$ with the same labelling issue. See [R1/verification.md Check 1](../R1-space-friction/verification.md#check-1--hubble-radius-and-alpha--h_0c) for the details.

## What Would Change This

To get a verification stack for R4, one would need:

1. A derived form of $\nu = f(\rho_g)$ from GCM minimal-model dynamics.
2. A specific distinction from R2 (not just "same effect, relabelled").
3. A quantitative $z(d)$ prediction.

Until these exist, R4 stays **🔴 Red** and its verification folder stays empty of scripts.

## TODOs

1. **If R4 gets fleshed out later:** add scripts for (a) derivation of pressure-frequency relation, (b) dimensional analysis, (c) comparison to R2 prediction.
2. **Otherwise:** consider dropping R4 from the coherence-paper menu — honest to flag it as "conceptually distinct mechanism we cannot currently formalize" rather than give it equal billing with R1/R2/R5.

## Honesty Summary

R4 has no verification because R4 has no arithmetic — it's a label for a family of possibilities, not a specific mechanism. Retaining it in the menu is defensible but should be brief in the paper.
