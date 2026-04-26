# Q3 — $E_n \cdot P_n$ Approximate Invariant

**Claim code:** Q3
**Epistemic tier:** Green (5/5 verification checks pass).
**Section:** S2 — Verifiable Math Spine (also cross-referenced in S4 — Quantum Structure)
**Source:** `GCM/theory/versions/gcm_v2.md` §H7; original tabulation this session.
**Verified:** 2026-04-23

---

## The Claim

For hydrogen energy levels $n = 1, 2, 3, 4, 5$, using the Bohr energy $E_n = -13.6/n^2$ eV and the tetrahedral/FCC shell population formula $P_n = 10n^2 + 2$:

| $n$ | $P_n$ | $E_n$ (eV) | $E_n \cdot P_n$ (eV) |
|---|---|---|---|
| 1 | 12  | 13.600 | 163.2 |
| 2 | 42  | 3.400  | 142.8 |
| 3 | 92  | 1.511  | 139.0 |
| 4 | 162 | 0.850  | 137.7 |
| 5 | 252 | 0.544  | 137.1 |

(We quote $|E_n|$ throughout so the product is positive; the original Bohr energies are negative, so strictly $E_n \cdot P_n$ is negative with the same magnitude.)

The product varies by ~16% across $n = 1$ to $5$, dropping sharply from $n=1$ and asymptoting to a fixed value at large $n$:

$$\lim_{n \to \infty} |E_n| \cdot P_n = \lim_{n \to \infty} \frac{13.6}{n^2} \cdot (10n^2 + 2) = 13.6 \cdot 10 = 136.0 \text{ eV}$$

The asymptote is exactly $10 \times$ the Rydberg energy ($\text{Ry} = 13.6$ eV).

## Framing — Observed Near-Invariance, Not a Derivation

Q3 is a **numerical observation**: the product of the hydrogen energy and the tetrahedral-shell population is approximately conserved across levels. It is **not** a derivation of hydrogen quantization from shell packing. The direction "shell packing *produces* $1/n^2$ scaling" is aspirational (Q6) and remains open.

## Why This Might Matter

If hydrogen's quantum numbers index GCM tetrahedral shells (a core conjecture of T1/T4), one would expect some invariant to emerge from the compatibility of the geometric shell structure with the empirical $1/n^2$ energy scaling. $E_n \cdot P_n \to 10 \, \text{Ry}$ is such an invariant. Whether it is *the* invariant — as opposed to a numerical coincidence that survives because both formulas scale as $1/n^2 \cdot n^2 = \text{const}$ asymptotically — is the open question.

---

## What This Claim Is

A clean numerical tabulation and an analytic asymptote, both verified independently. The $E_n \cdot P_n$ product is approximately $136$–$163$ eV across the first five hydrogen levels, with an exact large-$n$ limit of $10 \, \text{Ry}$.

## What This Claim Is Not

- **Not a derivation of hydrogen's $1/n^2$ scaling from tetrahedral geometry.** $E_n = -13.6/n^2$ is empirical (and derivable from Schrödinger's equation). The shell formula $P_n = 10n^2 + 2$ is standard crystallography. Their product being nearly constant is a coincidence of the common $n^2$ scaling, not (yet) a first-principles derivation.
- **Not a claim about the physical meaning of the $10 \, \text{Ry}$ asymptote.** Why $10$, specifically, is not explained here. The shell-formula's coefficient $10$ comes from tetrahedral geometry (FCC 12 nearest neighbors generalized); that coincidence with the Rydberg multiplier is intriguing but not mechanistic.
- **Not an alternative to Schrödinger.** Hydrogen's energy levels are derived cleanly from the Schrödinger equation; Q3 is a *compatibility observation* between that established result and GCM's tetrahedral-shell conjecture.

---

## Provenance

The $P_n = 10n^2 + 2$ formula is from `gcm_v2.md` §H7 and traces back to source notes on tetrahedral/FCC close packing. The $E_n \cdot P_n$ tabulation and the $10 \, \text{Ry}$ asymptote are computed in this and the v2 session.
