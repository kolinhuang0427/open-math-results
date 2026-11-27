# Independent Check Report: `garrison-2401.09497-conj5.2`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2401.09497/WCS.tex` (`arXiv:2401.09497v1`):
  - Definition 1.1 (`\label{def:weak_consec}`, Section 1, `lines 83–85`) and Conjecture 5.2 (`\label{conj:1 at end}`, Section 5, `lines 718–720`) match `TARGET.md` and `PROOF.md` verbatim.
  - Lemma 2.1 (`\label{lem:characterization}`, Section 2, `lines 221–223`) matches the cited residue-class characterization in `PROOF.md` Lemma 2.

## 2. Proof & Independent Mechanical Verification
- Checked every step of `PROOF.md` (`k=1, 2`, Lemmas 1–3, Case 1 for even $k \ge 4$, Case 2 Steps 1–4 for odd $k \ge 3$):
  - **Lemmas 1–3:** Reversal invariance, $S_m^\sigma = T_m^\sigma$ with $c_m > k \bmod m$, and CRT construction of $a \in \{0, \dots, L_k - 1\}$ with $\sigma(i) = \gcd(a + i, L_k)$ and $m \mid \sigma(i) \iff m \mid (a+i)$ for all $m \in [k]$ are all exact.
  - **Case 1 (even $k \ge 4$):** Reversing if needed so $c_2 = 2$, $m = k/2 + 1$ forces $\sigma(k/2+1) = k/2+1$; any $A = \sigma(1) > 1$ is odd with $A \mid k$, hence $A \mid k/2$ and $A \mid k/2+1$, contradiction.
  - **Case 2 (odd $k \ge 3$):** $A = \sigma(1) < \sigma(k) = B$ odd coprime divisors of $k = ABR$ ($BR \ge 5, k \ge 15$), $m = (k+A)/2$ pins $j = (k-A)/2 + 1$ and $\frac{BR+1}{2} \mid (a+1-A)$, $i_1 = (A-1)BR$ forces $s \ge 2$ and $a \equiv A - 1 + 2^{s-1} \pmod{2^s}$ (otherwise $B(BR+1) \mid \sigma(i_1) \le k$, contradicting $A < B$), and $i_t = (2^{s-1}-1)A + 1 + t \cdot 2^s A$ ($0 \le t < u$) yields $u$ distinct multiples of $2^s A$ in $[k]$ whereas $k = A(2^s u - 1) < u \cdot 2^s A$, contradiction.
- Wrote independent exact-integer verifier `targets/garrison-2401.09497-conj5.2/notes/check-check-1.py` (pure `int` arithmetic, zero floats, without reading `verify.py` or author notes).
- Command: `.venv/bin/python targets/garrison-2401.09497-conj5.2/notes/check-check-1.py`
- Results (`PASS`):
  - Exhaustive permutation verification of Definition 1.1 and Lemmas 1–3 for $k=1 \dots 8$.
  - Exhaustive GCD search across all $0 \le a < L_k$ for $k=3 \dots 12$ (confirming all WCS and Lemmas 1–3 + Case 1/Conjecture 5.2, e.g., $N(9)=8, N(10)=16, N(11)=16, N(12)=4$).
  - Verified Case 2 Steps 2–4 modular congruences, index bounds $1 \le i_t < k$, and pigeonhole contradiction $k < u \cdot 2^s A$ across all $46$ admissible odd composite triples $(A, B, R)$ with $k = ABR \le 150$.

## 3. Gate 2 Novelty Status
- Gate 2 passed (`notes/novelty-gate2-watch-1.md` and `notes/novelty-gate2-watch-5.md`). Ready for blind audit.
