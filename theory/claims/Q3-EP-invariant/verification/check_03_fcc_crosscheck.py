#!/usr/bin/env python3
"""Q3 Check 3 — FCC coordination-shell formula cross-check.

Verifies P_n = 10n^2 + 2 against OEIS A005901 canonical terms.

OEIS A005901 starts: 1, 12, 42, 92, 162, 252, 362, 492, 642, 812, ...
The initial 1 is the central atom. Subsequent terms are 10n^2 + 2 for n=1, 2, ...
"""

# OEIS A005901 canonical reference sequence
# Source: https://oeis.org/A005901 (Number of lattice points on surface of n-th shell)
OEIS_A005901 = [1, 12, 42, 92, 162, 252, 362, 492, 642, 812]


def main():
    print("# Q3 Check 3 — P_n = 10n^2 + 2 vs OEIS A005901")
    print()
    print(f"OEIS A005901 (first 10 terms):  {OEIS_A005901}")
    print()

    # Our formula, starting at n=1 (skipping the OEIS n=0 term which is 1, the central atom)
    computed = [10 * n**2 + 2 for n in range(1, 10)]
    reference = OEIS_A005901[1:10]

    print(f"{'n':>3}  {'OEIS A005901':>14}  {'10n^2 + 2':>12}  {'match':>6}")
    all_ok = True
    for n, (ref_val, comp_val) in enumerate(zip(reference, computed), start=1):
        ok = (ref_val == comp_val)
        all_ok &= ok
        print(f"{n:>3}  {ref_val:>14d}  {comp_val:>12d}  {'YES' if ok else 'NO':>6}")
    print()

    # Standard-physics crosscheck: FCC nearest-neighbor count is 12
    # (i.e. P_1 = 12). This is Ashcroft & Mermin Ch. 4 / any crystallography textbook.
    print(f"Standard FCC nearest-neighbor count: 12")
    print(f"Our P_1 = 10*1^2 + 2 = {10*1**2 + 2}")
    print(f"Match: {10*1**2 + 2 == 12}")
    print()

    print("STATUS:", "PASS" if all_ok else "FAIL")


if __name__ == "__main__":
    main()
