# E3 — Caveats

## What E3 actually claims, once sharpened

**Not:** "GCM has derived Van der Waals from graviton-density-gradient overlap."

**Yes:** "Van der Waals-London dispersion is a universal weak attraction between neutral bodies, well-accepted in standard physics. GCM's ontology (one fundamental attractive force, universal graviton substrate) is compatible with this universality. GCM reinterprets the fluctuating-dipole correlations that standard physics identifies as the origin of VdW as manifestations of graviton-substrate fluctuations. A rigorous derivation of the $1/r^6$ scaling from graviton physics — analogous to standard Casimir-Polder — is future work and requires: a graviton fluctuation spectrum, a notion of gravitational polarizability, and porting the Casimir-Polder calculation. None of these ingredients is presently specified."

## What the direct calculation ruled out

The naive reading, "Gaussian density distributions have gradient fluctuations whose overlap directly reproduces $1/r^6$," is falsified by the direct SymPy calculation. The gradient-gradient correlation between two Gaussians is exponentially suppressed at long range, not power-law, and changes sign at $R = \sigma\sqrt{6}$. This is a definitive negative result for the naive reading.

## Why this does not falsify GCM

Standard VdW is a *dynamic* effect — it arises from time-averaged correlations of *induced* dipoles, not from static overlap of density gradients. The naive reading conflated these. GCM's ontology (static density distributions interacting via gravitational attraction) at the level we've specified it does not include:

- A fluctuation spectrum for graviton density
- A polarizability response
- Time-averaged induced-dipole physics

If those three were added — and they plausibly could be, within the T1–T4 framework — the analog of the Casimir-Polder derivation would go through and $1/r^6$ would be recovered. The gap is in the machinery, not in the ontology.

## Honest limitations

1. **No fluctuation theory.** GCM has no equivalent of quantum zero-point motion yet. Without it, there is nothing to "fluctuate" and hence no dispersion force.
2. **No polarizability.** We have not computed how a Gaussian density distribution distorts in response to an applied gravitational gradient. This is a variational calculation that has not been attempted.
3. **Sign problem.** Our gradient-gradient correlation changes sign at $R = \sigma\sqrt{6}$. Real VdW is monotonically attractive at all separations (becomes short-range-repulsive only from Pauli / exchange physics that have nothing to do with VdW itself). A proper derivation needs to avoid the zero-crossing artifact of the static calculation.

## Comparison to Verlinde, Padmanabhan

Neither Verlinde's entropic-gravity framework nor Padmanabhan's thermodynamic-gravity framework derives Van der Waals. Both live at cosmological scales. GCM's attempt to extend substrate-gravity to molecular scales (via VdW) is distinctive — and its failure in the naive form tells us something specific about what GCM must develop to become a complete force-unification program at *all* scales.

## Positive framing for the coherence paper

While direct gradient overlap fails to reproduce $1/r^6$, there is a genuinely positive claim E3 can make:

**The ubiquity of Van der Waals attraction is structural evidence that neutral bodies attract universally.** This is a fact. Standard physics explains it via induced-dipole correlations. GCM's ontology (gravitons attract universally) is consistent with this observation in a way that theories with only repulsive or only short-range forces would not be. VdW, the most universal inter-molecular force, is already attractive, already universal, and already weakly coupled — exactly the form GCM predicts as the *default* behavior of neutral bodies.

This is an abductive argument: "our ontology predicts universal weak attraction between neutral bodies, and that's what we observe (Van der Waals), so this is consistency evidence even though we haven't derived the specific $1/r^6$ form." The paper should lead with this framing.

## What would make E3 green

Development of:
1. A GCM theory of graviton-density fluctuations (possibly via superdeterministic fluctuation-dissipation relations).
2. Gravitational polarizability for Gaussian density distributions.
3. A GCM-Casimir-Polder calculation yielding $-C_6/R^6$.
4. Numerical match to at least one measured VdW coefficient (e.g. He-He, Ar-Ar, or H₂-H₂ dispersion).

Until these are in place, E3 stays yellow as a framing claim and red as a derivation. That's the honest epistemic status.

## Recommendation

In the coherence paper, present E3 as:
- A framing alignment: GCM predicts universal weak attraction between neutral bodies; observed VdW is consistent with this prediction.
- A named open problem: a rigorous graviton-substrate derivation of $1/r^6$ requires machinery (fluctuation theory, polarizability, Casimir-Polder analog) that is future work.
- A rule-out of the naive direct-overlap reading, with the honesty that this was tested and didn't hold.

This is better for the program's credibility than claiming a derivation we don't have.
