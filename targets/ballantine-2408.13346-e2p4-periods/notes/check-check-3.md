# Independent Check Report (`check-3`): `targets/ballantine-2408.13346-e2p4-periods/`

## 1. Primary-Source Fidelity Check
Checked directly against `arXiv:2408.13346v1` (`tools/.arxiv_cache/eprint/2408.13346/main.tex`, Section 1, lines 66, 84–97, 103–108):
- **Definitions (lines 66, 84–85):** $e_2(\lambda) = \sum_{1 \le i_1 < i_2 \le \ell(\lambda)} \lambda_{i_1}\lambda_{i_2}$, $\mathcal{P}(m,n)$ is the set of partitions of $n$ of length $m$, and $e_2p_4(n) = \sum_{\lambda \in \mathcal{P}(4,n)} e_2(\lambda)$ (with $e_2p_4(0) = 0$ since $\mathcal{P}(4,0) = \emptyset$).
- **Conjectural Table (lines 93–97):** Claims minimal period `1150` for $m = 10$ and minimal period `1246` for $m = 18$ (in the sense of lines 91–93, modulo $m$ for sufficiently large $n$).
- **Theorem 2 (`\label{Th0}`, lines 103–108):** Establishes $e_2p_4(n+48) \equiv e_2p_4(n) \pmod 2$ and $e_2p_4(n+54) \equiv e_2p_4(n) \pmod 3$ for $n \ge 0$.
- **Result:** `TARGET.md` and `COUNTEREXAMPLE.md` match the primary source verbatim.

## 2. Independent Mechanical Verification
Written solely from the partition definition and `main.tex` without consulting `verify.py`, using pure Python `int` arithmetic and SymPy exact rational GF derivation (zero floats):
- Script: `targets/ballantine-2408.13346-e2p4-periods/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/ballantine-2408.13346-e2p4-periods/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/4] Direct partition DP matches brute-force enumeration for n = 0..40.
[2/4] Exact values at n=0,2,4,5,6,51,1150,1154,1246,1250 verified.
[3/4] Symbolically proved exact rational GF N(q)/D(q) and order-22 recurrence for all n >= 22.
[4/4] Exact minimal periods verified: per(10) = 1200 != 1150, per(18) = 1296 != 1246.
PASS
```
Summary:
- Verified direct partition DP against brute-force enumeration of $\mathcal{P}(4,n)$ for $0 \le n \le 40$.
- Verified all counterexample values in `COUNTEREXAMPLE.md`:
  - $m = 10$: $e_2p_4(1150) = 4204006824112 \equiv 2 \not\equiv 0 = e_2p_4(0) \pmod{10}$ and $e_2p_4(1154) = 4277582023120 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{10}$.
  - $m = 18$: $e_2p_4(1246) = 6275602376628 \equiv 6 \not\equiv 0 = e_2p_4(0) \pmod{18}$ and $e_2p_4(1250) = 6376921776108 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{18}$.
  - Also verified $e_2p_4(5) = 9 \ne 770034 = e_2p_4(51) \pmod 2$ and $e_2p_4(2) = 0 \not\equiv 25 = e_2p_4(6) \pmod 3$.
- Independently derived the exact rational generating function $N(q)/D(q)$ ($\deg N = 16 < 22$, $D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3$) directly from the 4-part partition parameterization, proving the order-22 monic-and-unit-constant-term recurrence for all $n \ge 22$ (hence pure periodicity from $n = 0$ modulo every $m \ge 2$) and exact minimal periods $\mathrm{per}(10) = 1200 \ne 1150$ and $\mathrm{per}(18) = 1296 \ne 1246$.

## 3. Verdict
- **PASS** (`Gate 2` `watch-1` PASS in `notes/novelty-gate2-watch-1.md`; `@watch-5`/`@watch-6` Gate 2 pending per `#300`).
