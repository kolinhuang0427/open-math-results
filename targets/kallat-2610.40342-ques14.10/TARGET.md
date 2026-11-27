---
source: "Ahaan Kallat, 'A p-adic Valuation Calculus for Permutations with Restricted Cycle Lengths', arXiv:2610.40342v1 (October 2026), Section 14 (sec:open), Question 14.10 (prob:gcdr, lines 1220–1222; Section 5 Theorem 5.1 thm:gcdfamily & Section 11 sec:globalgcd, lines 910–963)"
status: reported
owner: attack-4
started: 2026-11-27T10:16:26Z
updated: 2026-11-27T14:56:00Z
identifiers: ["arXiv:2610.40342v1", "prob:gcdr", "thm:gcdfamily", "prop:globalgcd", "g_r(n)", "G_r(n)", "Lambda_r(n)"]
---

# Target: `kallat-2610.40342-ques14.10`

## Exact Statement
From Section 14 (`\label{sec:open}`), lines 1220–1222 of `paper1_valuation_calculus.tex` in `arXiv:2610.40342v1`:

> **Question 14.10** (The global gcd).
> By Theorem~\ref{thm:gcdfamily}, $(n-1)_r\mid g_r(n)\mid G_r(n)=(n-1)_rm_r(n)$ with $m_r(n)$ involving only primes at most $r$, and $m_1(n)=1$, $m_2(n)=2^{\lfloor(n-1)/4\rfloor}$. By the computations of Section~\ref{sec:globalgcd}, for $r=3$ and $n\le900$ the two gcds differ exactly for $n=111+81j$ with $0\le j\le9$. Do they differ for every $n\equiv30\pmod{81}$ with $n\ge111$ and for no other $n$? Is $g_r(n)=G_r(n)$ for every $r\ge4$ and every $n\ge r+2$? What is the exponent of each prime $p\le r$ in $g_r(n)/(n-1)_r$ for $r\ge3$? The gcd $\Lambda_r(n)$ of the cycle type counts divides $g_r(n)$ (Proposition~\ref{prop:globalgcd}), and for $r=3$ the two differ at $p=3$ for $n=51,55,56,57,78,82,83,84$ in $n\le90$. For which $n$ do $\Lambda_r(n)$ and $g_r(n)$ differ?

## Gate 1 Novelty Receipt
- Checked `targets/` on 2026-11-27T10:11Z: no existing `kallat` target for Question 14.10 (`kallat-2610.40342-ques14.8` is a separate question in the same paper).
- Ran `.venv/bin/python tools/novelty_grep.py "2610.40342" "valuation calculus" "3x2^{k+2}" "lfloor 7(k+1)/2"` (0 hits across 618 files) and `.venv/bin/python tools/novelty_grep.py "Ahaan Kallat" "prop:globalgcd" "Lambda_r" "g_r(n)"` (0 hits for Kallat / `2610.40342`).
- Checked `gh search repos "2610.40342"` (`no repositories matched`), `gh search issues "2610.40342"` (only automated `ArXiv_Mail` digest), Zenodo API `q=2610.40342` (`total: 0`), `search_web` (`"2610.40342"`).

## Attack Log (`attack-4`)
- Started attack: `2026-11-27T13:58:00Z` (stop condition: 60–90 min -> `14:58Z`–`15:28Z`).
- Live Gate 1 novelty check (`notes/novelty-attack.md`, `2026-11-27T14:01:01Z`): **CLEAR** (no v2, 0 settlements across snapshots/GitHub/Zenodo/web; `rainwangphy/aftd-platform` `OP-746` only formalizes definitions and notes Question 14.10 remains open).
- Candidate ready (`2026-11-27T14:40:06Z`, 42 min): `PROOF.md` + zero-float AST-checked `verify.py` (`PASS` in `9.3s`).
  - **Q1 ($r = 3$: $g_3(n) \ne G_3(n)$ iff $n \equiv 30 \pmod{81}, n \ge 111$):** **YES** (complete `iff` proved for all $n \ge 5$, with $G_3(n)/g_3(n) = 3$; Theorem 1(d) & Theorem 4).
  - **Q2 ($g_r(n) = G_r(n)$ for all $r \ge 4, n \ge r+2$):** **NO (DISPROVED)** — explicit elementary proof that for every $64 \le r \le 79$ at $n = 1248$, $v_2(g_r(1248)) = v_2(\Lambda_r(1248)) = 1169 < 1170 = v_2(G_r(1248))$ via $S = \mathbb{N} \setminus \{96\}$ and the 4-partition Boolean square $\{96^{13}, 96^1 128^9, 80^6 96^8, 80^8 96^1 128^4\}$ (Theorem 2; computational scan in `notes/comp-q2.md`).
  - **Q3 ($v_p(g_r(n)/(n-1)_r)$ for $p \le r$):** **Completely solved for $r = 3$** (all $n \ge 5$, exact closed forms for $p = 2, 3$; Theorem 1(a)–(b), Theorems 3–4). *Scope note: general closed forms for arbitrary $r \ge 4$ remain open.*
  - **Q4 (When $\Lambda_r(n) \ne g_r(n)$):** **Completely solved for $r = 3$** (all $n \ge 5$: iff $n \equiv 1, 2, 3, 24 \pmod{27}$ and $n \ge 51$, with $g_3(n)/\Lambda_3(n) = 3^{\delta_3(n)} \in \{3, 9\}$; Theorem 1(c)). *Scope note: full classification for arbitrary $r \ge 4$ remains open.*
