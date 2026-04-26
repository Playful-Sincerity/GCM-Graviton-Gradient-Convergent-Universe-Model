# E3 — Future Work / Paper-1 Status

**Paper-1 decision:** EXCLUDE from unification claim. In paper-1 §8 (Structural Challenges) only, as honest falsification result.
**Source:** `theory/claims/audit-2026-04-24.md` (E3 row + §8 framing).

## Why excluded from unification

The naïve "direct overlap → $1/R^6$" reading of Van der Waals was FALSIFIED by the verification retrofit. Closed-form shape is exponential, not power-law:

$$C(R) = \frac{m^2(6\sigma^2 - R^2)}{32\pi^{3/2}\sigma^7}\exp\left(-\frac{R^2}{4\sigma^2}\right)$$

At $R = 20\sigma$: $R^6 C(R) \sim 5 \times 10^{-36}$. SymPy and Wolfram produced bit-identical closed forms.

Framing co-optation (universal attraction is *compatible* with observed Van der Waals) survives at the level of "GCM's substrate doesn't contradict VdW"; a direct derivation does not.

## What would promote E3 to INCLUDE

A GCM-specific Casimir-Polder-like calculation that reproduces the observed $C_6$ coefficient from graviton-substrate fluctuation correlations — not from direct gradient overlap but from the proper many-body integration analogous to QED Casimir-Polder. This would require:
- A specific model of graviton zero-point fluctuations
- A dispersion-relation-like calculation over fluctuation spectrum
- Reproduction of empirical $C_6$ for at least one atom-atom pair (hydrogen-hydrogen is the test case)

Directionally: this is a many-body substrate-fluctuation problem, not a two-particle gradient-overlap problem.

## Where this lives going forward

- **Paper-1 §8:** one paragraph as "exponential-vs-power-law falsification caught by verification; framing compatibility preserved, direct derivation deferred."
- **Verification folder preserved:** archive.
- **Future work:** GCM-Casimir-Polder derivation is paper-2+ work.

## See
- `theory/claims/audit-2026-04-24.md` — E3 row
- `theory/claims/E3-vdw-universal/verification.md` — falsification record
- Cross-reference `E4-gradient-overlap/` — the amplification-falsification side-result
