# Adversarial Audit Report (`audit-1`): `targets/kallat-2610.40342-ques14.10/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Audited UTC:** `2026-11-27T14:50Z`
- **Target:** Ahaan Kallat, *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, `arXiv:2610.40342v1` (October 2026), Section 14 (*Column 2 and open questions*, `\label{sec:open}`), **Question 14.10** (`\label{prob:gcdr}`, `paper1_valuation_calculus.tex` lines 1220–1222).
- **Files Inspected (Strict Isolation):** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and primary source `tools/.arxiv_cache/eprint/2610.40342/paper1_valuation_calculus.tex` (live `arxiv.org/abs/2610.40342` confirmed `[v1]` is the sole version). Author `verify.py` and scratch `notes/` were **not** read.
- **Verdict:** **PASS** (`"written proof, internally audited"`)

---

## 1. Primary-Source, Version, Citation, & Scope Fidelity — PASS

- **Verbatim statement & numbering:** Verified verbatim against `paper1_valuation_calculus.tex` (`\newtheorem{problem}[theorem]{Question}`):
  - **Question 14.10** (`\label{prob:gcdr}`, L1220–1222) matches `TARGET.md` word-for-word.
  - All internal references match the compiled numbering verbatim: **Theorem 5.1** (`\label{thm:gcdfamily}`, L350), eq. `(5.2)` (`\label{eq:sameg}`, L378), **Theorem 11.1** (`\label{thm:counter}`, L914), **Proposition 11.2** (`\label{prop:lead}`, L924), **Proposition 11.3** (`\label{prop:globalgcd}`, L937), and **Example 11.4** (`\label{ex:51}`, L953).
- **Honest scope:** Question 14.10 asks four subquestions:
  - **Q1** ($r = 3$: $g_3(n) \ne G_3(n)$ iff $n \equiv 30 \pmod{81}$ with $n \ge 111$): **Completely proved (YES)** for all $n \ge 5$, with $G_3(n)/g_3(n) = 3$.
  - **Q2** ($g_r(n) = G_r(n)$ for all $r \ge 4$ and $n \ge r + 2$): **Completely disproved (NO)** at $n = 1248$ for all $64 \le r \le 79$.
  - **Q3 & Q4** ($v_p(g_r(n)/(n-1)_r)$ and when $\Lambda_r(n) \ne g_r(n)$): **Completely proved for $r = 3$** (all $n \ge 5$, exact closed forms for $p = 2, 3$ and exact ratio $g_3(n)/\Lambda_3(n) = 3^{\delta_3(n)}$), with both `TARGET.md` and `PROOF.md` transparently stating that general closed forms/classifications for arbitrary $r \ge 4$ remain open.
- **Gate 2 novelty clear:** Passed by `@watch-6` (`#1523`), `@watch-1` (`#1524`), and `@watch-5` (`#1525`) with receipts in `notes/novelty-gate2-watch-{1,5,6}.md`.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

Every lemma, inequality, case split, modular congruence, and boundary case was audited line by line:

1. **§1 Preliminaries & Lemma 1 (L43–62) — PASS:** Boolean-lattice Möbius inversion for $g_r(n) = \gcd_P f_P(n)$ (Proposition 11.3(i),(iv)), $a_{S_{n-1}}(n) = a_{S_\infty}(n)$ for $n \ge r + 2$ yielding $G_r(n) \mid (a_{S_\infty}(n) - a_{S_k}(n))$, and Unique Maximum Principle are airtight.
2. **§2 Disproof of Q2 — Theorem 2 & Lemmas 2.1–2.2 (L65–142) — PASS:**
   - Deficit $\Delta(m) = \frac{m}{16} - (v_2(m) + 1)$ and identity (2.1) ($1248 = 78 \cdot 16$) are exact.
   - Lemma 2.1 exhaustively checks $e = v_2(m) \in \{0,1,2\}, 3, 4, 5, 6, 7, \ge 8$ for $m \ge 65$: $\Delta(m) \ge 0$, vanishing iff $m \in \{80, 96, 128\}$, with $m = 72$ ($\Delta(72) = 1/2$) the unique other integer with $\Delta(m) \le 1$.
   - Lemma 2.2 Step 1 cleanly rules out any part outside $\{80, 96, 128\}$ for $\mathrm{cost}_2(\lambda) \ge 75$ ($D + S \le 3$), including $t \ge 2$, $t = 1$ alone ($1248/2^u \in \{1248, 624, 312, 156, 78\}$ all have $\Delta \ge 23/8 > 2$), and $t = 1$ with $\{80, 96, 128\}$ ($m_1 = 72, \lambda_{72} = 2 \implies 1248 - 144 = 1104 = 16 \cdot 69$ divisible by none of $80, 96, 128$).
   - Lemma 2.2 Step 2 checks all even $a \in \{0, 2, \dots, 14\}$ in $5a + 6b + 8c = 78$: no solution has $s_2(a)+s_2(b)+s_2(c) \le 2$, and **exactly four** achieve $3$: $96^{13}$, $96^1 128^9$, $80^6 96^8$, $80^8 96^1 128^4$ (all parts $\ge 80 > r$ for $64 \le r \le 79$).
   - Theorem 2: $v_2(1248!) = 1244$, $v_2(\Lambda_r(1248)) = 1169$; for every $k \in (r, 1248]$, the count of surviving top-4 partitions in $a_{S_k}(1248)$ is even ($4, 2, 2,$ or $0$), so $v_2(G_r(1248)) \ge 1170$; meanwhile $S = \mathbb{N} \setminus \{96\}$ gives $a_S(1248) = N(96^{13})$ with $v_2 = 1169$. Completely airtight!
3. **§3 Exact $2$-adic Formula for $r = 3$ — Theorem 3 (L145–185) — PASS:**
   - Bound (3.1) $\ell_m(c) \le \frac{mc}{2} - 1$ ($m \ge 5, c \ge 1$; equality on $v_2(m)+1 = m/2$ only at $m=8$) verified across $e = 0,1,2,3,\ge 4$.
   - Uniqueness of $\lambda^*$ ($4^q$ or $4^{q-1}(4+\nu)^1$) verified across $\nu = 0$, $\nu \in \{1,2,3\}$ with $\Delta = 0$, $\Delta \ge 4$, and $\Delta \in \{1,2,3\}$ ($w \in \{9..11, 13..15, 17..19\}$). Choice of $k \notin \mathrm{supp}(\lambda^*)$ ($5, 6,$ or $4$ at $n=5$) and final Legendre subtraction for all $\nu \in \{0,1,2,3\}$ are exact.
4. **§4 Exact $3$-adic Classification for $r = 3$ — Lemmas 4.1–4.3 & Theorem 4 (L188–391) — PASS:**
   - Lemma 4.1 (`6^3 <-> 9^2` trade identity & Kummer base-$3$ classification of $\Delta_{\mathrm{trade}}(Y', t) \le 1$) is exact.
   - Lemma 4.2: bound $\ell_m(c) \le \frac{5}{36} mc - \frac{1}{2}$ ($m \ge 4, m \notin \{6,9\}$), $\delta \ge 3 \implies \mathrm{drop} \ge 3$ ($83/36 > 2$ and $11/4 > 2$), exact $\mu_{\max}(w)$ for $0 \le w \le 30$, full classification table across $\rho = 0,\dots,8$, and valuation identity $v_3(\Lambda_3(n)) = v_3((n-1)_3) + \lfloor(n-4)/9\rfloor + \lfloor(n+2)/9\rfloor$ all verified exact.
   - Lemma 4.3: exact mod-$9$ evaluations of $\tau_0, \dots, \tau_4$ and $S(x_0, y) \bmod 9$ for $x_0 \in \{1,2\}, y \ge 5, y \equiv 2 \pmod 3$ are exact.
   - Theorem 4: Cases 1 ($n \in \{5..9\}$), 2 ($n \ge 10, n \not\equiv 1,2,3,24 \pmod{27}$), 3 ($n \in \{24,28,29,30\}$), and 4 (all $12$ residue classes mod $81$ for $n \ge 51$, partitioned exhaustively by Subcases 4a–4f with exact minimum thresholds $55, 56, 78, 57, 51, 111$) are completely airtight, including the rational identities $\frac{5}{32}, \frac{11}{128}, \frac{33}{32}, \frac{653}{4480}$ and the exact $P = \{4, 9\}$ witness for $n \equiv 30 \pmod{81}, n \ge 111$.
5. **§5 Synthesis & Primes $q \ge 5$ — Theorem 1 (L394–425) — PASS:**
   - Proof of $v_q(\Lambda_3(n)) = v_q((n-1)_3)$ for every prime $q \ge 5$ and $n \ge 5$ (via $\ell_m(c) \le \frac{mc}{2(q-1)} - \frac{1}{q-1}$ for $m \ge 4, m \ne q$, and clean $\Delta = 0 / \Delta \ge 1$ split for both $s \in \{0, 4..q-1\}$ and $s \in \{1,2,3\}$) combines with Theorem 5.1, Theorem 3, and Theorem 4 to close parts (a)–(d) of Theorem 1 in full.

---

## 3. Independent Exact Verification — PASS

- **Checker AST check:** `FLOATS: [] FLOAT_CALLS: []` on `targets/kallat-2610.40342-ques14.10/notes/check-check-1.py`.
- **Executed checker:** `.venv/bin/python -u targets/kallat-2610.40342-ques14.10/notes/check-check-1.py` -> exit code `0`, raw output:
  - `Theorem 2 & Lemmas 2.1-2.2 (all r in [64..79] at n=1248, exact DP + mod 2^1173 recurrence): PASS`
  - `Lemmas 4.1-4.3 (trade identity, mu_max table 0..30, S(x0,y) mod 9): PASS`
  - `Theorems 1, 3, 4 (all n in 5..134 + {138,165,192,213,273,354}): PASS`
  - `PASS`

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Ready for Gate 3 freshness verification (`@watch-1`, `@watch-5`, `@watch-6`).
