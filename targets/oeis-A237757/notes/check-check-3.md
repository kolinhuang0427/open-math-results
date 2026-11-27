# Check Report — `oeis-A237757` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A237757&fmt=text` (`%I A237757 #17 Jan 22 2022 07:31:08`).
- **`TARGET.md` check:** Revision (`rev. 17`), `%N` definition, `%O` (`1,8`), `%S..%U` initial 58 terms ($a(1)=0$ through $a(58)=3013$), and Peter Bala's Feb 02, 2021 `%F` conjectured generating function match the live OEIS record verbatim. *(Cosmetic note: `TARGET.md` L17 writes `n = 1,...,57:` before listing all 58 OEIS `%S..%U` terms.)*

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–35:
  - Partitioning $\mathcal{P}(N) = \bigsqcup_{m \ge 1} \mathcal{P}_m(N)$ by least part $m$ (with $2m$ parts) is exact.
  - Subtracting $m$ from all $2m$ parts gives a well-defined bijection $\Phi_m : \mathcal{P}_m(N) \to \mathcal{Q}_{\le 2m-1}(N - 2m^2)$ with explicit two-sided inverse $\Psi_m$.
  - Ferrers conjugation identifies $\mathcal{Q}_{\le 2m-1}(M)$ with partitions of $M$ into parts $\le 2m - 1$, whose generating function is $\prod_{k=1}^{2m-1}(1 - q^k)^{-1}$. Shifting by $q^{2m^2}$ and summing over $m = n+1 \ge 1$ proves Bala's identity in $\mathbb{Z}[[q]]$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A237757/notes/check-check-3.py) (pure `int` arithmetic, `FLOAT_COUNT: 0`).
- Checked:
  1. Exact $q$-series expansion of $\sum_{n \ge 0} q^{2(n+1)^2}/\prod_{k=1}^{2n+1}(1-q^k)$ up to $q^{58}$ matches all 58 OEIS `%S..%U` terms.
  2. Brute-force enumeration of all partitions of $N$ for $N = 1..28$ confirms the direct `%N` definition count and verifies the explicit bijection $\Phi_m \leftrightarrow \Psi_m$ and Ferrers conjugation count for every $(N, m)$ with $2m^2 \le N$.
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```
