# Independent Blind Audit — `targets/mbirika-2204.12626-ques6.1/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:45Z`
- **Verdict:** **PASS** *(label: `"counterexample, verified by exact computation"` — see §3 Scientific Transparency Note on apparent branch-swap typo in $\mathcal{F}^3(k)$ vs substantive failure of $\mathcal{L}^3(k)$ even after repairing both typos)*

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against `tools/.arxiv_cache/eprint/2204.12626/main.tex` (`arXiv:2204.12626v2`, updated `2023-01-13`, arXiv comment *"15 pages, this version is the one that is published"*, *Fibonacci Quarterly* Vol. 60 (2022), No. 5, 255–269):
- **Numbering:** Line 85 declares `\newtheorem{thm}{Theorem}[section]` and line 94 declares `\newtheorem{question}[thm]{Question}`. The paper has 6 numbered sections (`1` L140, `2` L208, `3` L248, `4` L503, `5` L731, `6` L811 *Open questions*). Line 815 is the first theorem-like environment in Section 6, hence **Question 6.1**.
- **Definitions verified verbatim:** $F_0 = 0, F_1 = 1$, $L_0 = 2, L_1 = 1$, $G_n = G_{n-1} + G_{n-2}$ (L143, L211–216); $\mathcal{G}_{G_0, G_1}^m(k) = \gcd\left\{\left(\sum_{i=1}^k G_{n+i}^m\right)_{n \ge 0}\right\}$ (L145, L176, L822). *(Minor non-blocking typo in `TARGET.md` L18 quoting `F_{n+i}^n` instead of `F_{n+i}^2` from L176; immediately clarified on L19 as $m = 3$, and the verbatim Question 6.1 block L22–42 matches `main.tex` L815–835 character-for-character.)*
- **Verbatim Conjectures in Question 6.1 (`main.tex` L823–833, for even $k$):**
  - $\mathcal{F}^3(k) = \gcd(F_{k+1}^3 - 1, F_{k+2}^3 - 1)$ if $6 \mid k$, and $\frac{1}{2}\gcd(F_{k+1}^3 - 1, F_{k+2}^3 - 1)$ if $6 \nmid k$.
  - $\mathcal{L}^3(k) = \gcd(L_{k+1}^3 - 1, L_{k+2}^3 - 9)$ if $6 \mid k$, and $\frac{1}{2}\gcd(L_{k+1}^3 - 1, L_{k+2}^3 - 9)$ if $6 \nmid k$.

---

## 2. Line-by-Line Mathematical Audit (`COUNTEREXAMPLE.md`)

Checked every arithmetic computation and modular periodicity argument independently:
1. **Counterexample 1a ($\mathcal{F}^3(2)$, $6 \nmid 2$, lines 9–18):**
   - $F_1^3 + F_2^3 = 1 + 1 = 2$, $F_2^3 + F_3^3 = 1 + 8 = 9$, $\gcd(2, 9) = 1 \implies \mathcal{F}^3(2) = 1$.
   - Formula gives $\frac{1}{2}\gcd(F_3^3 - 1, F_4^3 - 1) = \frac{1}{2}\gcd(7, 26) = \frac{1}{2} \notin \mathbb{Z} \neq 1$. Exact.
2. **Counterexample 1b ($\mathcal{F}^3(6)$, $6 \mid 6$, lines 20–29):**
   - $n = 0$: $\sum_{i=1}^6 F_i^3 = 1+1+8+27+125+512 = 674 = 2 \cdot 337$. $n = 1$: $\sum_{i=2}^7 F_i^3 = 2870$. $\gcd(674, 2870) = 2$.
   - Since $(F_n \bmod 2)_{n \ge 0} = (0, 1, 1, \dots)$ has period $3 \mid 6$ with two odd terms per period, every block of $6$ consecutive cubes has $4$ odd summands, hence is even; thus $\mathcal{F}^3(6) = 2$.
   - Formula gives $\gcd(F_7^3 - 1, F_8^3 - 1) = \gcd(2196, 9260) = 4 \neq 2$. Exact.
3. **Counterexample 2a ($\mathcal{L}^3(2)$, $6 \nmid 2$, lines 35–45):**
   - $L_1^3 + L_2^3 = 1 + 27 = 28$, $L_2^3 + L_3^3 = 27 + 64 = 91$, $L_3^3 + L_4^3 = 64 + 343 = 407$; $\gcd(28, 91, 407) = \gcd(7, 407) = 1 \implies \mathcal{L}^3(2) = 1$.
   - Formula gives $\frac{1}{2}\gcd(L_3^3 - 1, L_4^3 - 9) = \frac{1}{2}\gcd(63, 334) = \frac{1}{2} \notin \mathbb{Z} \neq 1$. Exact.
4. **Counterexample 2b ($\mathcal{L}^3(12)$, $6 \mid 12$, lines 47–55):**
   - $(L_n \bmod 4)_{n \ge 0} = (2, 1, 3, 0, 3, 3, \dots)$ has period $6$; cubes mod $4$ are $(0, 1, 3, 0, 3, 3)$ summing to $10 \equiv 2 \pmod 4$, so every block of $12$ consecutive cubes is $\equiv 0 \pmod 4$.
   - $(L_n \bmod 5)_{n \ge 0} = (2, 1, 3, 4, \dots)$ has period $4$; cubes mod $5$ are $(3, 1, 2, 4)$ summing to $10 \equiv 0 \pmod 5$, so every block of $12$ consecutive cubes is $\equiv 0 \pmod 5$.
   - Hence $20 \mid \mathcal{L}^3(12)$; the $n = 0, 1, 2$ sums are $43702500, 185123260, 784200340$ with $\gcd = 20$, giving $\mathcal{L}^3(12) = 20$.
   - Meanwhile $L_{13} = 521, L_{14} = 843$, giving $L_{13}^3 - 1 = 141420760$, $L_{14}^3 - 9 = 599077098$, $\gcd = 2 \neq 20$. Exact.
   - Line 55 remark ($9 \mapsto 27 = L_2^3$ at $k = 6$): $\gcd(L_7^3 - 1, L_8^3 - 27) = \gcd(24388, 103796) = 28 \neq 2 = \mathcal{L}^3(6)$. Exact.

---

## 3. Scientific Transparency Note (Must Be Disclosed in `RESULTS.md`)

While the **verbatim** published Question 6.1 (`arXiv:2204.12626v2` / *Fibonacci Quarterly* 60(5)) is unequivocally **FALSE** for both $\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$, independent testing of the natural "repaired" formulas reveals an important distinction that should be transparently disclosed:
1. **$\mathcal{F}^3(k)$ (apparent branch-swap typo):** If the $6 \mid k$ and $6 \nmid k$ case labels are swapped (placing $\frac{1}{2}$ on $6 \mid k$ and $1$ on $6 \nmid k$), the swapped formula agrees with $\mathcal{F}^3(k)$ on all 60 even integers $2 \le k \le 120$ tested (`0` mismatches). Thus the failure of the published $\mathcal{F}^3(k)$ formula is consistent with a branch-label transposition error in the paper.
2. **$\mathcal{L}^3(k)$ (substantive refutation even after repairing BOTH typos):** Even if **both** apparent typos are repaired simultaneously — swapping the $6 \mid k$ / $6 \nmid k$ branches **and** replacing $9 = L_2^2$ with $27 = L_2^3$ — the repaired formula **still fails** immediately at $k = 6$ ($\mathcal{L}^3(6) = 2$ vs $\frac{1}{2}\gcd(L_7^3 - 1, L_8^3 - 27) = 14$), $k = 22$ ($199$ vs $1393 = 7 \cdot 199$), $k = 24$ ($1080$ vs $14040 = 13 \cdot 1080$), $k = 34$, $k = 38$, etc.

---

## 4. Independent Verification & Gate 2 Check

- **Independent Checker Re-run (`notes/check-check-1.py`):**
  - Command: `.venv/bin/python targets/mbirika-2204.12626-ques6.1/notes/check-check-1.py`
  - Exit code: `0`
  - Raw output: `PASS` (verified Counterexamples 1a, 1b, 2a, 2b, all modular periods, $k \in \{2, 4, \dots, 30\}$ mismatches, and the $L_2^3 = 27$ remark at $k = 6$ in pure `int` / `Fraction` arithmetic).
- **Gate 2 Novelty Receipts:** Verified all three (`notes/novelty-gate2-watch-{1,5,6}.md`) — all **PASS** (`the-omega-institute/trureturing#22988` targets Question 6.2 scaling only, explicitly excluding Question 6.1).

---

## 5. Verdict & Handoff

**PASS** (label: `"counterexample, verified by exact computation"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification (please flag §3 Transparency Note for `RESULTS.md`).
