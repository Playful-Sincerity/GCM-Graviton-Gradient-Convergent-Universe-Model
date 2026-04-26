# L1 — Derivation: Unit Conversion and Bound Comparison

**Claim code:** L1
**Date:** 2026-04-23

---

## Step 1 — Unit Conversion by Hand

**Goal:** Convert the GCM photon mass estimate from kg to eV/c².

**Given:**
- $m_\gamma = 10^{-54}$ kg (GCM estimate)
- $c = 2.998 \times 10^8$ m/s
- $1 \text{ eV} = 1.602 \times 10^{-19}$ J

**Conversion:**

$$m_\gamma c^2 = 10^{-54} \text{ kg} \times (2.998 \times 10^8 \text{ m/s})^2$$

$$= 10^{-54} \times 8.988 \times 10^{16} \text{ J}$$

$$= 8.988 \times 10^{-38} \text{ J}$$

Converting to eV:

$$m_\gamma c^2 = \frac{8.988 \times 10^{-38} \text{ J}}{1.602 \times 10^{-19} \text{ J/eV}} = 5.61 \times 10^{-19} \text{ eV}$$

Therefore:

$$\boxed{m_\gamma \approx 5.61 \times 10^{-19} \text{ eV}/c^2}$$

**Note:** The brief cites "5.6 × 10⁻¹⁹ eV/c²" — consistent with this calculation (rounding at the last digit).

---

## Step 2 — Compare to Wang 2023 Bound

**Wang et al. (2023, JCAP)** used fast radio burst (FRB) dispersion measures to constrain photon mass:

$$m_\gamma^{\text{Wang}} \leq 2.1 \times 10^{-15} \text{ eV}/c^2$$

**Margin calculation:**

$$\frac{m_\gamma^{\text{Wang}}}{m_\gamma^{\text{GCM}}} = \frac{2.1 \times 10^{-15}}{5.61 \times 10^{-19}} = 3{,}740$$

**Orders of magnitude:** $\log_{10}(3{,}740) \approx 3.57$ orders.

**Honesty flag:** The plan document and session brief describe this as "4 orders of margin." The actual calculation gives **~3.6 orders**. The difference is not material to the coherence argument (GCM is safely below the bound by any account), but "4 orders" is slightly overstated. This derivation uses the more precise value of 3.6 orders.

**Verdict:** GCM's $m_\gamma \approx 5.61 \times 10^{-19}$ eV/c² is $\approx 3{,}740 \times$ smaller than the Wang 2023 bound. The claim passes this constraint.

---

## Step 3 — Additional Bounds (Contextual)

The Wang 2023 FRB bound is not the tightest photon-mass bound. Magnetostatic and solar-wind analyses have placed constraints in the range $m_\gamma \lesssim 10^{-18}$ eV/c² (Particle Data Group 2022, various). 

Against $m_\gamma^{\text{PDG}} \sim 10^{-18}$ eV/c²:

$$\frac{10^{-18}}{5.61 \times 10^{-19}} \approx 1.8$$

GCM's claimed mass is approximately **1.8× below** the tightest published bounds (as of this writing). This is within the bound but with very thin margin. See `caveats.md` for the full treatment.

---

## Step 4 — Future Bound Scenario

If photon-mass bounds tighten by 4+ additional orders of magnitude (reaching $m_\gamma \lesssim 10^{-19}$ eV/c²), GCM's claimed $5.61 \times 10^{-19}$ eV/c² would be excluded. This is a falsification condition that should be tracked as new FRB and quantum-optics experiments improve sensitivity.

**Falsification trigger:** Any photon-mass bound at $m_\gamma < 5 \times 10^{-19}$ eV/c² would require GCM to revise the photon mass estimate downward or confront the constraint as a structural gap.
