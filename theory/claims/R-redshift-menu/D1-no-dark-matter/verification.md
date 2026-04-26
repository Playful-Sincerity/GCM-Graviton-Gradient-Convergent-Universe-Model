# D1 — Verification Record

**Tally:** 2/3 PASS, 1/3 FAIL (real 12-order-of-magnitude error caught).
**Last run:** 2026-04-24
**Reproducible:** Yes — see `verification/` directory.
**Tools:** Python 3.14 (stdlib `decimal`, prec=50) + Wolfram Engine via `wolframscript`. Wolfram MCP unavailable.
**Honesty note:** Scripts added 2026-04-24 as new forward-verification; not retrofit of prior runs.

---

## Check 1 — Number of asteroid-mass PBHs in Milky Way halo

- **Tool:** Python `decimal` prec=50
- **Script:** [verification/check_01_pbh_count_milky_way.py](verification/check_01_pbh_count_milky_way.py)
- **Output:** [verification/outputs/check_01.txt](verification/outputs/check_01.txt)
- **Result:** **PASS** — claim.md's $N_{\text{PBH}} \sim 10^{25}$ is correct (computed $1.87 \times 10^{25}$ at $M_{\text{halo,dark}} = 9.4 \times 10^{11} M_\odot$, $M_{\text{PBH}} = 10^{20}$ g).
- **Finding (chronicle correction needed):** In Session G's chronicle summary and the D1 ledger draft, I wrote "~10^18 asteroid-mass PBHs in Milky Way halo" — off by **7 orders of magnitude**. claim.md was correct; the chronicle summary I wrote derived from it was not. Chronicle entry needs a correction note.

## Check 2 — Cosmic mean inter-PBH spacing

- **Tool:** Python `decimal` prec=50 with arbitrary-precision cube root
- **Script:** [verification/check_02_cosmic_pbh_spacing.py](verification/check_02_cosmic_pbh_spacing.py)
- **Output:** [verification/outputs/check_02.txt](verification/outputs/check_02.txt)
- **Result:** **PASS (order-of-magnitude).**
- **Computed:** $\rho_{\text{crit}} = 9.20 \times 10^{-27}$ kg/m³ at $H_0 = 70$ km/s/Mpc. $\rho_{\text{DM}} = \Omega_{\text{DM}} \rho_{\text{crit}} = 2.39 \times 10^{-27}$ kg/m³ (plausibility.md says 2.4e-27, ratio 0.997). $n_{\text{PBH}} = \rho_{\text{DM}}/M_{\text{PBH}} = 2.39 \times 10^{-44}$ m⁻³ (plausibility.md says 2.4e-44, ratio 0.997). Mean spacing $n^{-1/3} = 3.47 \times 10^{14}$ m = **2320 AU** (plausibility.md says 2000 AU, ratio 1.16).
- **Verdict:** all three of $\rho_{\text{DM}}$, $n_{\text{PBH}}$, and inter-PBH spacing are correct to within ~16% (well within the order-of-magnitude tolerance appropriate for a yellow-tier claim).

## Check 3 — Hawking temperature at $M = 10^{17}$ kg

- **Tool:** Python `decimal` prec=50 + Wolfram independent cross-check
- **Script (Python):** [verification/check_03_hawking_temperature.py](verification/check_03_hawking_temperature.py)
- **Script (Wolfram):** [verification/check_03_hawking_temperature.wls](verification/check_03_hawking_temperature.wls)
- **Output (Python):** [verification/outputs/check_03.txt](verification/outputs/check_03.txt)
- **Output (Wolfram):** [verification/outputs/check_03_wolfram.txt](verification/outputs/check_03_wolfram.txt)
- **Result:** **FAIL — 12-order-of-magnitude error caught.**
- **Formula:** $T_H = \hbar c^3 / (8 \pi G M k_B)$. Textbook value for $M = M_\odot$ is 6.17e-8 K; both tools reproduce to 3+ significant figures (calibration confirmed correct).
- **Computed at $M = 10^{17}$ kg:** $T_H = 1.23 \times 10^6$ K (both Python and Wolfram).
- **Claim in plausibility.md:** $T_H \approx 6 \times 10^{-7}$ K.
- **Claim in claim.md:** "Hawking temperature at these masses is far below the CMB (2.725 K)."
- **Both claims are wrong by ~12 orders of magnitude.** Actual $T_H / T_{\text{CMB}} = 4.5 \times 10^5$ — 5 orders ABOVE CMB, not below.
- **The observational conclusion is still correct, but via a different mechanism:** Schwarzschild radius is $1.49 \times 10^{-10}$ m, emitting area is $2.77 \times 10^{-19}$ m². At $T_H = 10^6$ K, Stefan-Boltzmann luminosity is only $\sim 36$ mW per PBH. At typical cosmic inter-PBH distances ($\sim 2000$ AU), individual PBHs are too dim and sparse to be detected.
- **Required fix to plausibility.md and claim.md:** replace the "low-temperature" argument with a "high-temperature but negligible-luminosity" argument. The observational conclusion survives; the specific physical reasoning was wrong.

## Cross-Tool Disagreements

**None.** Python and Wolfram agree on every numerical quantity across all three checks. The one FAIL is a disagreement between the tools (agreed) and plausibility.md / claim.md (wrong). This is the verification catching a real error.

## TODOs

1. **Revise D1/plausibility.md Hawking-temperature paragraph.** Replace "$T_H \approx 6 \times 10^{-7}$ K (far below CMB)" with: "At $M = 10^{17}$ kg, $T_H \approx 1.2 \times 10^6$ K — actually hot. But the Schwarzschild radius is only $\sim 10^{-10}$ m (atomic scale), so the emitting area is $\sim 10^{-19}$ m² and the total Hawking luminosity per PBH is only $\sim 36$ mW. At cosmic inter-PBH distances and given the rarity of close encounters, this is entirely undetectable."
2. **Revise D1/claim.md similarly.** The sentence "they emit no light of their own" is also misleading — they emit Hawking radiation, just negligibly. Correct framing: "they emit negligible electromagnetic radiation at any plausible observer distance given the tiny emitting surface and typical cosmic inter-PBH spacing."
3. **Correct Session G chronicle summary.** "~10^18 PBHs in Milky Way halo" should read "~10^25" (claim.md had it right).
4. **Wolfram MCP.** Still unavailable; local wolframscript substituted.

## Honesty Summary

D1 emerges from retrofit verification with:
- One clean PASS (PBH count; claim.md value was correct; my chronicle summary was off by 7 orders).
- One PASS within 16% tolerance (cosmic density / spacing).
- One FAIL (Hawking temperature — 12 orders off; the observational conclusion survives but via a different physical mechanism than the one claimed).

The **structural position** of D1 (dark matter is ordinary matter we can't see; asteroid-mass PBHs are one candidate; observationally plausible) survives unchanged. The **specific physical justification** for why asteroid-mass PBHs are observationally hidden needs a rewrite: it is luminosity, not temperature, that makes them invisible.

D1 stays at **🟡 Yellow** structurally. The failing Hawking check is a *mechanism error*, not a claim error — the claim (PBHs as viable DM candidate) is supported by the Profumo literature and this verification; my specific stated mechanism was wrong.
