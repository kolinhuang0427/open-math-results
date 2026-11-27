# Blind Audit Report: `ballantine-2408.13346-e2p4-periods`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:29Z`
**Verdict:** **PASS** — Counterexample verified by exact computation and rational generating function (`"counterexample, verified by exact computation"`), with transparent publication-version note below.

## 1. Primary-Source Fidelity & Version Note
Verified verbatim against `arXiv:2408.13346v1` (confirmed latest arXiv version via live arXiv API query on `2026-11-27`, published/updated `2024-08-23T19:41:53Z`), Cristina Ballantine, George Beck, and Mircea Merca, *"Partitions and elementary symmetric polynomials -- an experimental approach"*, `tools/.arxiv_cache/eprint/2408.13346/main.tex`:
- **Definitions (Section 1, lines 66–67 & 84–85):** $e_2(\lambda) = \sum_{1 \le i_1 < i_2 \le \ell(\lambda)} \lambda_{i_1}\lambda_{i_2}$, $\mathcal{P}(4, n)$ is the set of partitions of $n$ into $4$ positive parts, and $e_2p_4(n) = \sum_{\lambda \in \mathcal{P}(4,n)} e_2(\lambda)$ ($e_2p_4(0) = 0$ since $\mathcal{P}(4, 0) = \emptyset$).
- **Conjectural Table of Minimal Periods (Section 1, lines 93–97):** Explicitly states for $e_2p_4(n) \bmod m$ (for sufficiently large $n$) minimal period `1150` at $m = 10$ and minimal period `1246` at $m = 18$, alongside 24 other moduli $m \in \{2,\dots,37\}$.
- **Theorem 2 (`\label{Th0}`, Section 1, lines 103–108):** Proves periods $48$ mod $2$, $54$ mod $3$, and $96$ mod $4$ for $n \ge 0$ (verified `\label{Th0}` is indeed the second `\begin{theorem}` environment in `main.tex`).
- **Publication-version transparency note:** `arXiv:2408.13346v1` was later published in *The Ramanujan Journal* **66** (2025), Art. 34 (`DOI: 10.1007/s11139-024-01001-6`, Jan 2025). The arXiv preprint was never revised beyond `v1`, and the Springer journal PDF is paywalled, so it could not be verified whether the published journal table silently corrected the two entries (`1150 = 1200 - 50` and `1246 = 1296 - 50`). This caveat should be stated in `RESULTS.md`.

## 2. Mathematical Verification of `COUNTEREXAMPLE.md`
1. **Direct counterexamples at $n = 0, 4$ (and all sufficiently large $n$):**
   - $e_2p_4(0) = 0$, $e_2p_4(4) = 6$.
   - $m = 10$: $e_2p_4(1150) = 4204006824112 \equiv 2 \not\equiv 0 = e_2p_4(0) \pmod{10}$ and $e_2p_4(1154) = 4277582023120 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{10}$.
   - $m = 18$: $e_2p_4(1246) = 6275602376628 \equiv 6 \not\equiv 0 = e_2p_4(0) \pmod{18}$ and $e_2p_4(1250) = 6376921776108 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{18}$.
2. **Pure periodicity & eventual-period validity:**
   - Audited the self-contained symbolic derivation in `check-check-3.py` via the bijection $(a,b,c,d) = (t_4+t_3+t_2+t_1, t_4+t_3+t_2, t_4+t_3, t_4)$ ($t_4 \ge 1$, $t_1,t_2,t_3 \ge 0$) and commuting differential operators $x_i \partial_{x_i}$ on $x_4 q^4 / \prod_{k=1}^4 (1 - x_k q^k)$: yields $\sum_{n \ge 0} e_2p_4(n) q^n = N(q)/D(q)$ with $D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3$ ($\deg D = 22$, leading and constant coefficients both $+1$) and $\deg N < 22$.
   - Hence $(e_2p_4(n))_{n \ge 0}$ satisfies the exact order-22 recurrence for all $n \ge 22$ with companion matrix in $\mathrm{SL}_{22}(\mathbb{Z})$, so $(e_2p_4(n) \bmod m)_{n \ge 0}$ is purely periodic from $n = 0$ for every $m \ge 2$. In particular, eventual period ("for sufficiently large $n$") coincides with pure period from $n = 0$, and minimal scalar period equals minimal 22-state period.
   - Therefore $e_2p_4(n+1150) \equiv e_2p_4(n) \pmod{10}$ and $e_2p_4(n+1246) \equiv e_2p_4(n) \pmod{18}$ fail for infinitely many $n$, and the true minimal periods are $\mathrm{per}(10) = \mathrm{lcm}(48, 300) = 1200 \neq 1150$ and $\mathrm{per}(18) = \mathrm{lcm}(48, 324) = 1296 \neq 1246$.
3. **Conceptual contradiction with Theorem 2 & full 26-entry audit:**
   - Verified $1150 \equiv 46 \not\equiv 0 \pmod{48}$ ($e_2p_4(5) = 9 \equiv 1 \not\equiv 0 \equiv 770034 = e_2p_4(51) \pmod 2$) and $1246 \equiv 4 \not\equiv 0 \pmod{54}$ ($e_2p_4(2) = 0 \not\equiv 1 \equiv 25 = e_2p_4(6) \pmod 3$).
   - Independently computed the exact minimal period modulo every one of the 26 moduli in the table: confirmed the claim in `COUNTEREXAMPLE.md` line 5 that the other 24 entries hold exactly, while $m = 10$ ($1200 \ne 1150$) and $m = 18$ ($1296 \ne 1246$) fail.

## 3. Independent Mechanical Verification
Audited and executed `targets/ballantine-2408.13346-e2p4-periods/notes/check-check-3.py` (exact Python `int` + SymPy rational GF, zero floats):
- Command: `.venv/bin/python -u targets/ballantine-2408.13346-e2p4-periods/notes/check-check-3.py`
- Result: exit `0`, raw `PASS` (DP vs brute force $0 \le n \le 40$; exact counterexample values; symbolic GF $N(q)/D(q)$ and order-22 recurrence; minimal periods `per(10) = 1200 != 1150`, `per(18) = 1296 != 1246`).

## 4. Verdict & Handoff
**PASS.** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final coordinator verification (include the *Ramanujan Journal* 66 (2025) paywalled-version note in `RESULTS.md`).
