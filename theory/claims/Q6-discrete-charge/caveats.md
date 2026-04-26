# Q6 — Caveats

---

## 1. No numerical verification possible at this stage

Because Q6 is a plausibility argument — not a derivation — there is no numerical prediction to check, no formula to dimensionally analyze, and no result to cross-reference against published bounds. The CC-7 verification stack does not apply. This is the correct call: a plausibility argument that *seems* to verify numerically would be an overclaim dressed in rigor.

**What to say in the coherence paper:** "This section is a plausibility argument. It identifies a direction; it does not supply a result. Numerical verification is deferred to the derivation, which does not yet exist."

---

## 2. Magic-number analogy is suggestive, not load-bearing

The atomic and nuclear shell-closure magic numbers are real phenomena supported by quantum-mechanical calculation (Schrödinger equation in an atomic potential; shell model with spin-orbit coupling for nuclei). GCM does not yet have the analogous calculation for graviton shells. The analogy is useful for **framing** the argument to a physicist reader — "this is structurally the kind of thing that happens when shell closure produces stability" — but it is not a derivation by analogy.

**Risk:** A careless reading would treat the analogy as support. The section must be written so no reader concludes "Q6 is supported by the nuclear shell model." It isn't. The nuclear shell model is *precedent* for the idea that shell-closure produces stability, but precedent is not proof for GCM's specific case.

---

## 3. Fractional quark charges are not addressed

Observed elementary charges include $\pm e/3$ and $\pm 2e/3$ (quarks). Q6 as written gestures at integer multiples of $e$; it does not accommodate the fractional case. UNSPEC-2 in gcm_v2.md flags this as an open issue. Any serious treatment of charge in GCM eventually has to explain:

- Why the smallest observed free charge is $\pm e$ (quark confinement)
- Why bound quarks carry $\pm e/3$ and $\pm 2e/3$
- How color confinement emerges in a configurational charge picture

Q6 is silent on all three. This is correct for a plausibility argument but is a substantial gap.

---

## 4. Relationship to H2 (charge sign from flow direction)

H2 proposes that charge *sign* arises from the direction of graviton current ($\nabla \cdot J_g$). Q6 is silent on sign — it concerns only quantization. The two claims must eventually be made consistent:

- If Q6 selects shell counts that are stable, and H2 selects sign via flow, then a single graviton configuration carries both a discrete charge magnitude (from Q6) and a sign (from H2). The full "discrete charge" story is the combination.
- Neither claim currently has the formalism to be checked for consistency with the other. This is future work.

---

## 5. What Q6 contributes to the coherence case

Even as a plausibility argument, Q6 contributes:

- A statement that charge quantization is **compatible** with GCM's one-particle ontology (it does not require intrinsic charge on the graviton, which the Axiom of Indivisibility forbids).
- A structural hypothesis — shell stability produces discrete charge — that a future derivation could target.
- Honest acknowledgment that the derivation isn't done.

This is sufficient for a coherence case (which claims non-trivial internal consistency), but insufficient for a theory claim. The coherence paper should position Q6 accordingly.

---

## 6. What would upgrade Q6 to green-tier

Per `claim.md` §"What Would Make This Green": a stability criterion applied to graviton cluster configurations, producing a discrete spectrum of stable packings, mapped to observed charge values. Without steps 1–2 of that list, Q6 is permanently yellow.

In the coherence paper's ranking, Q6 should be listed under "aspirational" directions, alongside the parity-violation configurational argument and the Lorentz force reproduction (UNSPEC-4). These are the structural gaps the program openly names.
