# Q6 — Discrete Charge from Stable Shell Packings

**Claim code:** Q6
**Epistemic tier:** 🟡 Yellow (plausibility argument only, not a derivation)
**Status:** Aspirational. Presented as a *direction a future derivation would take*, not as a result.
**Session:** D (Quantum Structure), 2026-04-23

---

## The Plausibility Argument

Charge, in GCM, is a property of *shell structure* — not of individual gravitons. (This follows from CC-5, the Axiom of Indivisibility: a truly indivisible particle cannot possess intrinsic charge. All charge-like properties must emerge configurationally from arrangements of gravitons.)

Given this, the question *"why is charge quantized in units of $e$?"* becomes the question *"why are only certain graviton configurations gravitationally stable?"*

The plausibility argument proceeds as follows:

1. **Gravitons pack into shells governed by FCC/cuboctahedral geometry** (Q2). The $n$th shell contains exactly $P_n = 10n^2 + 2$ sites.
2. **Not all graviton counts produce stable configurations.** Just as chemical "magic numbers" (2, 8, 18, 36, 54, 86) correspond to closed-shell electron configurations, and nuclear "magic numbers" (2, 8, 20, 28, 50, 82, 126) correspond to closed-shell nucleon configurations, GCM posits that a discrete set of graviton counts corresponds to *closed graviton shells* — the stable packings.
3. **If the set of stable packings is** $\{N_1, N_2, N_3, \ldots\}$ with $N_k = k \cdot N_1$ (or some similarly regular sequence), **then the observable charges are quantized** by that set.
4. **The fundamental charge $e$ emerges** because only the smallest stable non-neutral packing corresponds to a single unit of charge; larger stable packings correspond to multiples.

This gives, in principle, a mechanism for why charge is observed in integer units of $e$: the stability condition selects the quanta.

---

## What This Argument Does and Does Not Achieve

**The argument gestures at:** a mechanism whereby charge quantization emerges from packing stability, consistent with GCM's one-particle ontology and the Axiom of Indivisibility.

**The argument does not establish:**

- **Which graviton counts are stable.** The magic-number analogy is suggestive, not derived. GCM has no explicit stability calculation — no potential-well analysis, no eigenvalue problem, no minimization over configurations.
- **That stable packings produce exactly one charge unit per packing.** Even if certain counts are stable, there is no argument that each stable packing carries charge $\pm e$ rather than some other amount.
- **Why $e$ has the value it does.** The magnitude of $e \approx 1.602 \times 10^{-19}$ C is not predicted. A derivation would need to connect shell count to coupling strength, which requires dynamics GCM does not yet have.
- **Fractional quark charges.** Observed charges of $\pm e/3$ and $\pm 2e/3$ are not addressed here. UNSPEC-2 (v2) flags this as an open issue.
- **Sign asymmetry.** Why positive and negative charges are both quantized at the same magnitude is not addressed; this connects to H2 (charge from graviton flow direction) and UNSPEC-1.

---

## Honest Flag (per CC-4)

> **We have not shown that only certain packings are stable, or that those packings produce exactly one charge unit. This is the direction a future derivation would take, not a result achieved.**

The argument as given is a *plausibility sketch*: it names a mechanism consistent with GCM's foundations, points at a standard precedent (atomic/nuclear shell closure), and leaves the actual derivation as future work. A physicist reading this should hear: "GCM offers a configurational story for charge quantization, but the load-bearing stability calculation is not done."

---

## Connection to Other Claims

- **Q2** (cuboctahedral shells): Supplies the geometric substrate. Q6 asks which shell sizes are stable; Q2 just tells us how many sites each shell has.
- **Q3** ($E_n \cdot P_n$ near-invariant): Suggests a relationship between shell population and energetic "budget" per shell — hints at stability structure but does not establish the discrete set.
- **CC-5 (Axiom of Indivisibility):** Forces charge to be configurational. Q6 is the direct consequence: if charge is configurational, what configurations does nature pick?
- **H2 (charge from flow direction):** The sign of charge (positive vs. negative) is posited to arise from graviton current direction ($\nabla \cdot J_g$ sign). Q6 addresses quantization; H2 addresses sign. They are complementary pieces of the charge picture, both incomplete.

---

## What Would Make This Green

A genuine derivation of Q6 would need, at minimum:

1. **A stability criterion** — an energy functional or variational principle whose minima correspond to stable graviton packings. This requires graviton dynamics (the minimal-model equation of motion) to be applied to *internal* cluster configurations, not just the free-space $N$-body problem.
2. **A discrete spectrum of stable configurations** — the stable set $\{N_1, N_2, N_3, \ldots\}$ identified by the stability criterion.
3. **A mapping from stable configurations to charge values** — ideally showing that the smallest non-neutral stable configuration carries $\pm e$ (in whatever units the theory chooses), with larger configurations being integer multiples.
4. **Agreement with observation** — the proton-electron charge equality to $10^{-21}$ (Dylla & King, 1973), and charge conservation in every known reaction.

Steps 1 and 2 are the hard part. Without them, Q6 remains a plausibility argument.

---

## Why This Level of Honesty Matters

A common failure mode in unification programs is to claim that "charge quantization follows from structure" without actually deriving which structures are stable. GCM is explicit that this step is not done. The coherence paper should present Q6 as motivating future work, not as a completed piece of the unification case. The credibility-cost of an honest flag is much smaller than the credibility-cost of an overclaim caught in peer review.
