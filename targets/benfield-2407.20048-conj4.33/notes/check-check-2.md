# Independent Check Report: `targets/benfield-2407.20048-conj4.33`

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/benfield-2407.20048-conj4.33/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against `arXiv:2407.20048v2` (`fiborder.tex`, lines 84, 273, 306–310, 675–682):
- Definitions of $K$-Fibonacci sequence ($F_{K,0}=0, F_{K,1}=1, F_{K,n}=K F_{K,n-1}+F_{K,n-2}$), $\pi_K(m)$, $\alpha_K(m)$, and $\omega_K(m)$ match `TARGET.md` verbatim.
- Conjecture 4.33 (`\label{even-K-exceptions}`, lines 675–682) matches `TARGET.md` verbatim (even $K$, all $m > 3$, all three assertions).

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python targets/benfield-2407.20048-conj4.33/notes/check-check-2.py
```
Output:
```
PASS (Lemmas 1-3 + all 7 proof subcases verified across 6422 even-(K,m) pairs)
```
All checks use pure exact integer modular simulation (zero floating point):
- **Setup & identities:** Verified Cassini-type identity $F_{K,n+1}F_{K,n-1} - F_{K,n}^2 = (-1)^n$, duplication $F_{K,2r} = F_{K,r}L_{K,r}$, and $L_{K,2r} = L_{K,r}^2 - 2(-1)^r \equiv 2 \pmod 4$ ($\nu_2(L_{K,2r}) = 1$) for even $K \in [-10, 20]$ and $1 \le r < 20$.
- **Lemmas 1–3:** Verified Lemma 1(3) ($\omega_K(m) = \mathrm{ord}_m(\beta) \in \{1,2,4\}$, $\pi = \alpha\omega$, $\beta^2 \equiv (-1)^\alpha$) and Lemma 2 for odd $n \in [3, 99]$; Lemma 1(4) $\mathrm{lcm}$ identities for $a, b \in [2, 25]$; Lemma 3 ($\omega_K(2^x) = 1$, $\pi_K(2^x) = \alpha_K(2^x) = 2^a \ge 2$) for $1 \le x \le 7$ across even $K \in [-10, 20]$ (including $K = 0$).
- **Full sweep of Conjecture 4.33:** Verified all three assertions directly from the recurrence period for all $6{,}422$ pairs $(K, m)$ with $K \in \{-10, -8, \dots, 40\}$ and $4 \le m \le 250$, confirming all 7 proof subcases (`case1_odd`, `case2_pow2`, `case3_om1`, `case3_om2_alev`, `case3_om2_agtv`, `case3_om4_a1`, `case3_om4_age2`) are populated and consistent.
