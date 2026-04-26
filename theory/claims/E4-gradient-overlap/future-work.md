# E4 — Future Work / Paper-1 Status

**Paper-1 decision:** EXCLUDE the amplification reading. INCLUDE the regularization observation in §8 as side-result.
**Source:** `theory/claims/audit-2026-04-24.md` (E4 row + §8 framing).

## What was falsified

The "density-gradient overlap amplifies local force" reading was intended to close the E2 $10^{40}$ magnitude gap. Seven cross-tool checks (Pint + SymPy + mpmath + scipy + Wolfram) produced bit-identical closed form:

$$U(R) = -\frac{Gm^2}{R}\,\mathrm{erf}\left(\frac{R}{2\sigma}\right)$$

The overlap **regularizes** (force → 0 linearly at $R \to 0$); it does **not amplify**. The amplification reading is falsified at the level of functional form. SymPy and Wolfram agreed to $7.6 \times 10^{-24}$ against Gauss-law derivation; mpmath and Wolfram sweeps agreed to 14+ sig figs.

## What survives as positive side-result

The Newtonian $1/r$ singularity is naturally resolved when point-masses are replaced by finite-width density gradients. This is a structural observation about how GCM's substrate picture softens the short-range divergence — not a unification result, but a legitimate mathematical consequence of the framework.

## What would promote E4 to INCLUDE (beyond §8 mention)

A mechanism that *uses* the regularization observation — e.g., connecting the erf-shaped short-range behavior to a specific emergent coupling constant or to a charge-quantization condition. None specified currently.

Alternatively: a derivation that starts from E4's closed form and produces a non-trivial phenomenological consequence (inner-structure scattering cross-sections, for instance).

## Where this lives going forward

- **Paper-1 §8:** one short paragraph noting the amplification falsification and the regularization side-result.
- **Verification folder preserved:** excellent verification work; archive intact.
- **Future work:** connecting regularization observation to downstream phenomenology.

## See
- `theory/claims/audit-2026-04-24.md` — E4 row
- `theory/claims/E4-gradient-overlap/verification.md` — 7-check record
- `theory/claims/E2-competing-attraction/future-work.md` — linked magnitude gap
