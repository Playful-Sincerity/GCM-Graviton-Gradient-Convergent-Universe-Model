# Q3 — Caveats

## What This Proves

- **A numerical near-invariance.** $|E_n| \cdot P_n$ varies by only $\sim 16\%$ across $n = 1, \ldots, 5$, and asymptotes to $136.0$ eV as $n \to \infty$.
- **An exact analytic identity.** $\lim_{n \to \infty} |E_n| \cdot P_n = 10 \cdot \text{Ry}$, where Ry = 13.6 eV is the Rydberg energy.
- **Compatibility between two well-established formulas** — Bohr hydrogen and FCC shell populations — in the sense that their product has a clean asymptote.

## What This Does Not Prove

- **Not a derivation of hydrogen quantization from tetrahedral geometry.** Both input formulas — $E_n = -13.6/n^2$ and $P_n = 10n^2 + 2$ — are derived outside GCM: Bohr from the Schrödinger equation, FCC from crystallography. Their product being near-constant is a consequence of their common $n^2$ scaling, not of a deeper mechanism.
- **Not a prediction.** Q3 is retrospective — given both formulas, compute the product. GCM predicts neither formula from first principles at this stage.
- **Not an explanation of the $10 \, \text{Ry}$ coincidence.** The coefficient $10$ in $P_n$ comes from FCC geometry; the Rydberg $13.6$ eV comes from QED/Bohr. Why their product specifically equals $10 \cdot \text{Ry}$ (as opposed to, say, $12 \cdot \text{Ry}$ if you used a different shell-count convention) is not addressed here.

## Three Layers of the Near-Invariance

It helps to state explicitly what is exact, what is asymptotic, and what is empirical:

1. **Exact (analytic):** $|E_n| \cdot P_n = \text{Ry} \cdot (10 + 2/n^2)$. Given both input formulas, this is algebraic identity.
2. **Asymptotic:** $\lim_{n \to \infty} = 10 \, \text{Ry}$ exactly.
3. **Near-constant at finite $n$:** the correction $2 \, \text{Ry}/n^2$ is small for $n \geq 2$ and large only for $n = 1$. The $n = 1$ value ($163.2$ eV) is $20\%$ above the asymptote; $n = 5$ is $0.8\%$ above.

## The $n = 1$ Anomaly

The ground state accounts for most of the variation. This is interesting in its own right: the "infinite-sum" asymptote converges quickly for $n \geq 2$, but the ground state is an outlier at 163 vs 136 eV. If one were to read this as a shell-closing story, the $n = 1$ outlier would correspond to the tightest, most-curved shell — the regime where finite-size geometric effects bite hardest. This is speculative and not asserted as proof.

## On the "Aspirational" Direction (Q6)

The sister claim Q6 — that stable tetrahedral shell packings *produce* the $1/n^2$ energy scaling from first principles — is yellow to red tier. Q3 is not a step toward that derivation; Q3 is a *compatibility check*. If Q6 is ever established, Q3 falls out as a consequence. If Q6 is not established, Q3 remains a numerical observation whose significance depends on future work.

## Honesty Flag for the Coherence Paper

When Q3 appears in S2 or S4 of the coherence paper, the framing must be:

> "The Bohr energies and FCC shell populations satisfy $|E_n| \cdot P_n \to 10 \cdot \text{Ry}$. This is a numerical compatibility between two independently-derived formulas — suggestive of a tetrahedral-shell story for hydrogen, but not yet a derivation of one. The direction is Q6 (aspirational)."

Avoid phrasings like: "$|E_n| \cdot P_n$ is conserved in GCM" or "GCM derives hydrogen from shell packing." Both overclaim.

## Open Questions Surfaced

- **Q6 (aspirational):** Does stable tetrahedral-shell packing produce $E_n \propto 1/n^2$?
- **Why coefficient 10?** The FCC coefficient $10$ matches the Rydberg multiplier cleanly. Is there a deeper connection, or is it a coincidence of dimensionality?
- **Does the pattern survive extensions?** With relativistic corrections and Lamb shift, $E_n$ develops $n$-dependence beyond the simple $1/n^2$. Does $E_n \cdot P_n$ still converge to a clean limit?

## Relationship to Other Claims

- **Independent of M1, E7, L2, M3** at the formula level.
- **Q2 (derive $P_n = 10n^2 + 2$ from first principles)** — this is the crystallographic input, standard result.
- **Q6 (discrete charge from stable shell packings)** — the direction Q3 gestures toward but does not establish.
- **T1 (one fundamental particle)** — Q3 is a mild consistency check on the "quantum states are geometric configurations" reading of T1/T4.
