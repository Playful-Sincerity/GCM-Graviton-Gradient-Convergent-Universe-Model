# Indivisibility Axiom — Formal Derivation

**Claim code:** S1-AX-1-F
**Parent:** `indivisibility-axiom.md`
**Epistemic tier:** Green (logical derivation; argument is deductive within stated premises)
**Intended audience:** Physicist or analytic philosopher. This is a 1–2 page formal derivation, not a machine-verified proof. Lean 4 formalization is named as a future direction.

---

## Purpose

This document presents two complementary formalizations of the Axiom of Indivisibility:

(a) **First-order logic layer** — explicit premises and a derived theorem.
(b) **Mereological layer** — the same argument in the vocabulary of classical atomic mereology (Leonard–Goodman 1940; Simons 1987).

Together they make precise the informal claim: *"if you can call something truly indivisible, it cannot have intrinsic properties — only relational ones."*

---

## Layer (a): First-Order Logic

### Primitive predicates

| Symbol | Reading |
|---|---|
| $\text{Ind}(x)$ | $x$ is indivisible: has no proper parts |
| $\text{Prop}(P, x)$ | $P$ is an intrinsic (non-relational) property of $x$ |
| $\text{Part}(y, x)$ | $y$ is a proper part of $x$ |
| $\text{Rel}(P, x)$ | $P$ is a relational property of $x$ (reduces to $x$'s relations to external entities $y \neq x$) |
| $\text{Reduce}(P, x)$ | $P$ reduces to the proper parts of $x$ |
| $\text{Brute}(P, x)$ | $P$ is a brute primitive of $x$: no further structure, no reduction |

### Premises

**(P1)** $\text{Ind}(g)$ — the graviton is indivisible. (From T1: "one fundamental particle.")

**(P2)** $\forall x:\ \text{Ind}(x) \to \neg \exists y:\ \text{Part}(y, x)$
— An indivisible entity has no proper parts. (Definition of indivisibility.)

**(P3)** $\forall x\, \forall P:\ \text{Prop}(P, x) \to \text{Reduce}(P, x) \lor \text{Brute}(P, x)$
— Any intrinsic property either reduces to the entity's parts or is a bare primitive. (Principle of property grounding; denies floating non-relational properties.)

**(P4)** $\forall x\, \forall P:\ \text{Reduce}(P, x) \to \exists y:\ \text{Part}(y, x)$
— Reduction requires parts to reduce to. (Property-reduction schema.)

**(P5)** $\forall x\, \forall P:\ \text{Brute}(P, x) \to \neg \text{Physical}(P)$
— A brute primitive has no geometric or algebraic structure; therefore it is not a physical property in the sense physicists intend. (Physical properties — spin, chirality, charge — require mathematical structure: angular momentum is an algebraic invariant of the rotation group; chirality is a parity eigenvalue; charge is a $U(1)$ phase. A property with none of this structure is not yet a physical property.)

### Theorem: No intrinsic properties for an indivisible entity

**Theorem (T).** $\text{Ind}(g) \to \forall P:\ \neg \text{Prop}(P, g) \lor \text{Rel}(P, g)$

*Equivalently:* every property of an indivisible particle is either not truly intrinsic or is relational.

**Proof.** Assume $\text{Ind}(g)$ and $\text{Prop}(P, g)$ for arbitrary $P$. We derive a contradiction unless $\text{Rel}(P, g)$.

By P3: $\text{Reduce}(P, g) \lor \text{Brute}(P, g)$.

*Case 1: $\text{Reduce}(P, g)$.*
By P4: $\exists y:\ \text{Part}(y, g)$.
By P2 and P1: $\neg \exists y:\ \text{Part}(y, g)$.
Contradiction. $\square$

*Case 2: $\text{Brute}(P, g)$.*
By P5: $\neg \text{Physical}(P)$.
But we assumed $\text{Prop}(P, g)$ intends $P$ to be a physical property (spin, chirality, charge).
Contradiction with the stipulated domain of physical properties. $\square$

Both cases yield contradiction. Therefore $\text{Prop}(P, g)$ cannot hold for any physically meaningful non-relational $P$. Any property that $g$ possesses is relational — it consists of $g$'s position relative to other gravitons, or its identity as the entity that participates in the one fundamental interaction. $\blacksquare$

### Corollary

**Corollary (C).** The complete description of a graviton is:
$$g \equiv (m_g,\ \mathbf{x})$$
where $m_g$ is a uniform scalar parameter (the same for all gravitons — a constant of the theory, not a variable property) and $\mathbf{x} \in \mathbb{R}^3$ is a relational position. No other term appears.

Spin, chirality, charge, and flavor are not in $g$'s description. They appear in the description of *configurations* of $g$'s.

---

## Layer (b): Mereological Framing

Standard atomic mereology (Leonard and Goodman, "The Calculus of Individuals," 1940; Simons, *Parts: A Study in Ontology*, 1987) provides the rigorous vocabulary for "has no proper parts."

### Axioms of classical mereology (Simons 1987, §1.1)

**(AM1)** $x \leq x$ — Reflexivity: everything is a part of itself.

**(AM2)** $x \leq y \land y \leq x \to x = y$ — Antisymmetry.

**(AM3)** $x \leq y \land y \leq z \to x \leq z$ — Transitivity.

**(AM4)** $x < y \to \exists z\ (z \leq y \land \neg \text{Ov}(z, x))$ — Weak Supplementation: every proper part has a disjoint complement within the whole.

Here $x < y$ abbreviates $x \leq y \land x \neq y$ (proper part), and $\text{Ov}(x, y)$ abbreviates $\exists z\ (z \leq x \land z \leq y)$ (overlap).

**(AM5)** $\text{Atom}(g)$, where $\text{Atom}(x) \equiv \neg \exists y\ (y < x)$ — the graviton is a mereological atom.

### Theorem in atomic mereology

**Theorem (AM-T).** Let $\text{Atom}(g)$. Then there is no $y$ such that $y < g$. Consequently, no property of $g$ can be grounded in $g$'s parts, because $g$ has none. Under the property-grounding principle (P3 above), every physically meaningful intrinsic property of $g$ requires structural grounding — and that grounding must therefore be external (relational).

**Proof.**
$\text{Atom}(g)$ by AM5 means $\neg \exists y\ (y < g)$.
Suppose for contradiction that some property $P$ of $g$ reduces to $g$'s parts. By P4, $\exists y\ (y < g)$. Contradiction. $\square$

**AM4 consequence.** If $g$ had any proper part $p$, AM4 guarantees a complementary part $q$ disjoint from $p$ within $g$. But $\text{Atom}(g)$ precludes any proper part — so the condition of AM4 never triggers for $g$. $g$ is the ground case below which the supplementation principle does not apply, which is exactly what "atom" means.

### Structural consequence for GCM

In atomic mereology, the complete structural description of an atom is its participation in mereological relations with other atoms and composites (what overlaps with what, what is a part of what larger thing). This is the mereological analog of saying that the graviton's only non-trivial property is position — which is a relational property, specifying $g$'s relationship to the coordinate structure established by all other gravitons.

The GCM claim is therefore: the graviton is a mereological atom in the ontological sense, not merely the physical sense. Its entry in the ontology is $g \equiv (m_g, \mathbf{x})$ and nothing more.

---

## Lean 4 Formalization (Future Direction)

The argument above is informally rigorous — legible to a logician or philosopher of physics, but not machine-verified. The next level of formalization would encode:

- The mereological axioms AM1–AM5 as Lean 4 type-class instances
- The property-grounding premises P3–P5 as axioms
- The derivations above as Lean 4 theorems with `sorry`-free proofs

This is the trajectory followed by the IVNA formalization project and is named here as a parallel future direction for GCM. As of 2026-04-23, no `.lean` files exist in this repository. Lean 4 formalization is a goal, not a claim.

---

## Verification

**Tally:** 4/5 checks passed live, 1/5 pending (Wolfram). Epistemic tier: **Green** on the strength of live checks; cross-tool redundancy open as TODO.
**Last run:** 2026-04-24.
**Reproducible:** Yes — see [`verification/indivisibility-formal/`](verification/indivisibility-formal/). All inputs, scripts, and captured outputs are archived; scripts are runnable as `python3 <file>` (using the venv at `/tmp/gcm-verify-venv` with sympy 1.14.0) or `lean <file>`.

### Check 1 — FOL propositional encoding (UNSAT of reductio)
- **Tool:** Python 3.14.4 + SymPy 1.14.0 (satisfiable())
- **Script:** [verification/indivisibility-formal/check_01_fol_propositional.py](verification/indivisibility-formal/check_01_fol_propositional.py)
- **Output:** [verification/indivisibility-formal/outputs/check_01.txt](verification/indivisibility-formal/outputs/check_01.txt)
- **Result:** PASS — UNSAT confirmed; P1–P5 ∧ Prop(P,g) ∧ Physical(P) has no satisfying assignment.
- **Notes:** Propositional instantiation of the first-order theorem at a fixed (g, P). The universal-quantifier flattening is sound here because the reductio is over a single (g, P) pair.

### Check 2 — Atomic mereology Atom theorem
- **Tool:** Python 3.14.4 + SymPy 1.14.0
- **Script:** [verification/indivisibility-formal/check_02_mereology_atom.py](verification/indivisibility-formal/check_02_mereology_atom.py)
- **Output:** [verification/indivisibility-formal/outputs/check_02.txt](verification/indivisibility-formal/outputs/check_02.txt)
- **Result:** PASS — Atom(g) ∧ Part(y, g) is UNSAT. Negative control (with AM5 removed) is SAT, confirming the Atom axiom is doing the logical work.

### Check 3 — Premise-dependency scan (negative controls per premise)
- **Tool:** Python 3.14.4 + SymPy 1.14.0
- **Script:** [verification/indivisibility-formal/check_03_premise_dependency_scan.py](verification/indivisibility-formal/check_03_premise_dependency_scan.py)
- **Output:** [verification/indivisibility-formal/outputs/check_03.txt](verification/indivisibility-formal/outputs/check_03.txt)
- **Result:** PASS — removing any one of P1–P5 turns the reductio SAT. No premise is redundant; every premise is load-bearing.

### Check 4 — Lean 4 stub type-check
- **Tool:** Lean 4.16.0 (elan)
- **Script:** [verification/indivisibility-formal/check_04_lean_stub.lean](verification/indivisibility-formal/check_04_lean_stub.lean)
- **Output:** [verification/indivisibility-formal/outputs/check_04.txt](verification/indivisibility-formal/outputs/check_04.txt)
- **Result:** PASS (stub) — theorem declared with correct type signature; premises P2–P5 encoded as axioms; proof body is `sorry` (expected future-direction placeholder). Lean's only diagnostic is the expected "declaration uses sorry" warning.

### Check 5 — Wolfram Language independent verification
- **Tool:** Wolfram Engine / Wolfram MCP — **UNAVAILABLE in this session.**
- **Script:** [verification/indivisibility-formal/check_05_wolfram_todo.wls](verification/indivisibility-formal/check_05_wolfram_todo.wls)
- **Output:** [verification/indivisibility-formal/outputs/check_05_wolfram.txt](verification/indivisibility-formal/outputs/check_05_wolfram.txt)
- **Result:** PENDING — expected invocation and expected result (`SatisfiableQ[formula] == False`) are documented in the `.wls` header so a Wolfram-capable session can run and archive the output. No Wolfram output fabricated.

### Known gaps / TODOs

- **Wolfram MCP re-run.** Check 5 needs to run in a session with Wolfram Engine or MCP attached. This is the one cross-tool redundancy gap.
- **Lean proof body.** The `sorry` placeholder should be discharged by a future session; the proof follows the same case analysis as check_01 and is not technically difficult, just not yet done.

### Philosophical caveat preserved

P5 (brute primitive implies non-physical) is the single most contestable premise. The "bare particular" position in analytic metaphysics holds that a property with no structure can still be a real property. The argument here treats such a property as physically inadmissible — standard in philosophy of physics, but named here explicitly so the argument's load-bearing commitment is visible. If a reader accepts bare particulars, Check 1's UNSAT still holds (logic doesn't depend on P5's philosophical defensibility), but the philosophical weight of the conclusion shifts. This is the right place to flag it for S8's philosophical-challenges treatment.
