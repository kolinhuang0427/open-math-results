# Blind Independent Audit Report — `targets/jensen-2605.27941-ques2/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`), `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-1.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"*, `arXiv:2605.27941v1` (submitted `2026-05-27T04:27:10Z`, verified sole version via live `tools/arxiv_fetch.py query --id-list 2605.27941 --no-cache`), **Section 5** (*Open questions and future work*, `\label{sec:future-work}`), **Question 2** (`main.tex` L1138–1140).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all blocking and minor fixes from initial FAIL `#1723` were cleanly applied in `TARGET.md`, `PROOF.md`, and `notes/check-check-1.{md,py}`; publication label: **"written proof, internally audited"**).

---

## 1. Primary Source & Statement Fidelity Check

Verified verbatim against `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`):
- **Definitions (Section 2, L191–223):** `\newtheorem{definition}{Definition}` gives Definition 1 (`Mixed Lonely Runner Conjecture`, L191–204) and Definition 2 (`Mixed Loneliness Parameter Space`, L212–223). Both match `TARGET.md` L22–28 verbatim.
- **Question wording (L1138–1140):**
  > `\begin{question} For \(k\geq 3\), off of the coordinate planes, is \(\MLPS_k\) convex, or a finite union of convex sets? \end{question}`
  Matches `TARGET.md` L33–34 verbatim; `\newtheorem{question}{Question}` has no section reset, and L1138 is the 2nd `\begin{question}` (after L1094), so **Question 2** is exact.
- **DEFECT 1 (Blocking — Wrong Section Number):**
  The five `\section` commands in `main.tex` are:
  1. `L69`: *Introduction* (Section 1)
  2. `L184`: *Mixed loneliness* (Section 2)
  3. `L314`: *Indicator functions and arithmetic time progressions* (Section 3)
  4. `L714`: *The two-dimensional mixed loneliness parameter space* (Section 4)
  5. `L1059`: *Open questions and future work* (**Section 5**, `\label{sec:future-work}`)

  `TARGET.md` (L3, L20), `PROOF.md` (L4), and `notes/check-check-1.md` (L8) all erroneously cite **Section 4** instead of **Section 5**.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Section 1 (L14–28) — Construction & Monotonicity:** **SOUND.** Verified $0 < x_n < d_n \le \frac{1}{13}$, $0 < \varepsilon_{n,k} < \mu_n < \eta_n \le \frac{5}{104} < \frac{1}{12}$, $y_n \in (\frac{5}{12}, \frac{1}{2})$, exact algebraic identity for $x_n - x_{n+1} > 0$, and strict decrease of $\eta_n$.
- **Lemma 1 (L33–50) — Speed-tuple obstruction:** **SOUND.** Verified reduction to $t \in [0, 1/2]$, $y > \frac{4}{9} > \frac{1}{3}$, $u = \frac{1}{2} - t \in [0, 1/6)$, $\|2t\| = 2u \ge x \implies u \ge x/2$, $\frac{1}{2} - x < (2n+1)\frac{x}{2} < \frac{1}{2} + x$, forcing $(2n+1)u \ge \frac{1}{2} + x \implies t \le \frac{n-x}{2n+1}$, contradiction.
- **Lemma 2 (L52–80) — Every segment $(Q_n^{(k)}, Q_m^{(k)})$ exits $\mathsf{MLPS}_k$:**
  - **DEFECT 2 (Blocking — False intermediate inequality at `PROOF.md` L68):**
    `PROOF.md` L68 writes:
    > *"Since $m+1 \ge 6$, $2m+2n+5 < 2(2n+3)$, and $\frac{1}{n+1} < \frac{2}{2n+3}$, the second term is at most $\frac{3}{4} \cdot \frac{4(n-m)}{6(2m+3)(2n+3)} = \frac{1}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}$."*
    The inequality $\frac{1}{n+1} < \frac{2}{2n+3}$ is **FALSE** for every $n \ge 0$ (since $2n+3 > 2n+2 \iff \frac{1}{n+1} > \frac{2}{2n+3}$), and the algebraic substitution also drops a factor of $(2n+3)$.
    - **Clean exact fix:** For $5 \le m < n$ ($m+1 \ge 6$, $n+1 \ge 7$),
      $$\frac{2m + 2n + 5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{2}{7} + \frac{2}{6} + \frac{1}{42} = \frac{9}{14} < \frac{2}{3},$$
      so the second term of $y_n - y_m$ is at most $\frac{3}{4} \cdot \frac{9}{14} \cdot \frac{n-m}{(2m+3)(2n+3)} = \frac{27}{56} \cdot \frac{n-m}{(2m+3)(2n+3)} < \frac{1}{2} \cdot \frac{n-m}{(2m+3)(2n+3)}$.
  - All other steps of Lemma 2 (L57–67, L69–80: $x_n < x^* < x_m$, $\frac{1}{2n+3} < x^* < \frac{1}{2n-1}$, $x_m - x_n$ lower bound, $y^* > y_n - 2\delta_n$, $5(2n+5)(2n+3) - 2(n+1)(2n+1) = 16n^2 + 74n + 73 > 0$, and the $m=5, n=7$ midpoint check) are **SOUND**.
- **Lemma 3a (L90–93) — Elementary Bad-Measure Bound:** **SOUND.**
- **Lemma 3b (L95–116) — Midpoint Counting Lemma:** **SOUND.** Verified odd $q$ ($\beta \ge \alpha$, $q \mid s_3$, $\gcd(2a, q)=1$, exact count $2\lceil q d_n \rceil - 1$ for $\theta=0$ and $\lceil 2q d_n \rceil$ for arbitrary $\theta$) and even $q$ ($\beta \le \alpha - 1$, $a$ odd, $(q/2) \mid s_3$, exact odd-residue count $2\lceil (q d_n - 1)/2 \rceil$ for $\theta = 0$ and $\lceil q d_n \rceil$ for arbitrary $\theta$).
- **Lemma 3c (L118–158) — Uniform 3-Runner Safe Measure:** **SOUND** across all regimes and subcases:
  - Reduction to $\gcd(s_1, s_2, s_3) = 1$, $s_1 < s_2$, and exhaustiveness of Regimes A, B, C verified.
  - Regime A (L128): $\frac{5}{2}x_n L_3 < \frac{1}{4}L_3$, total $\ge \eta_n > \mu_n$.
  - Regime B (L130–137): both $2s_3 \nmid s_1$ and $2s_3 \mid s_1$ ($m_1 = 1$ and $m_1 \ge 2$) yield disjoint intervals of length $\ge w_n/s_3$ and total measure $\ge W_n$; removing $s_2$ leaves $\ge \frac{3}{4}W_n = \frac{3}{8}\delta_n \eta_n > \mu_n$. *(Minor typo at L133: `since \delta_n < \frac{1}{20(2n+3)^2}` should use `=`, as $\delta_n$ is defined equal to $\frac{1}{20(2n+3)^2}$.)*
  - Regime C1 (L141), C2 (L142), C3a (L144–148, all three branches including odd $s_2 = 2j+1$ where $2(n+j+2) \equiv 2j+1 \pmod{2n+3}$ and odd $r$ where $r(2n+3)+r$ is even), and C3b (L149–156, all 7 parity/size pairings covered by Cases 1–3, including the patched L156 bound $\frac{25}{6} + \frac{74}{11} = \frac{719}{66} < 11$) verified line-by-line.
- **Lemma 4 (L160–165) & Main Theorem (L169–175):** **SOUND.** Union bound $(k-3)\cdot \frac{\mu_n}{k} < \mu_n \le \mu(S_{123})$ gives $Q_n^{(k)} \in \mathsf{MLPS}_k$ for all $n \ge 5, k \ge 3$; Pigeonhole Principle + Lemma 2 rules out both convexity and any finite union of convex sets.

---

## 3. Independent Verifier Audit (`notes/check-check-1.py`)

- Re-executed `.venv/bin/python -u targets/jensen-2605.27941-ques2/notes/check-check-1.py`: exited `0`, `PASS`.
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Minor cleanup requested for `@check-1`: update `notes/check-check-1.md` L7–8 (Section 4 $\to$ Section 5, cite `tools/.arxiv_cache/eprint/2605.27941.src` instead of `/tmp/...`), and in `notes/check-check-1.py` clean up the stale L164 comment and add an assertion for the corrected L68 bound $\frac{2m+2n+5}{(m+1)(n+1)} \le \frac{9}{14}$.

---

## 4. Gate 2 Novelty Status

- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`2026-11-27T16:54Z`–`16:56Z`, `0/743` snapshot hits, `2605.27941v1` sole arXiv version, sole OpenAlex citer `2609.06259v3` verified in TeX `lonelyrelations.tex:257-258` unrelated, GH/Zenodo/HexagonMath/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

Following `@scout-10` (`#1727`) and `@check-1` (`#1728`), `@audit-2` re-verified all updated files verbatim on disk and re-executed the independent verifier:

1. **Defect 1 resolved (`TARGET.md` L3, L20; `PROOF.md` L4; `notes/check-check-1.md` L8):** All citations updated from `Section 4` to **Section 5** (*Open questions and future work*, `main.tex` L1059, Question 2 L1138–1140), and `notes/check-check-1.md` cites `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`).
2. **Defect 2 resolved (`PROOF.md` Lemma 2 L68):** False intermediate inequality $\frac{1}{n+1} < \frac{2}{2n+3}$ replaced by the exact decomposition
   $$\frac{2m+2n+5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{2}{7} + \frac{2}{6} + \frac{1}{42} = \frac{9}{14} < \frac{2}{3},$$
   yielding second term $\le \frac{3}{4}\cdot\frac{9}{14}\cdot\frac{n-m}{(2m+3)(2n+3)} = \frac{27}{56}\cdot\frac{n-m}{(2m+3)(2n+3)} < \frac{1}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}$.
3. **Minor cleanup resolved (`PROOF.md` L133 & `notes/check-check-1.py`):** Fixed `\delta_n < \frac{1}{20(2n+3)^2}` $\to$ `\delta_n = \frac{1}{20(2n+3)^2}`, removed stale comment in `check-check-1.py`, and added exact assertion for the corrected L68 bound.
4. **Final independent re-run by `@audit-2`:**
   - Command: `.venv/bin/python -u targets/jensen-2605.27941-ques2/notes/check-check-1.py` -> exit `0`, raw stdout:
     - `Section 1 & Lemmas 1-2 (including midpoint m=5,n=7): PASS`
     - `Lemmas 3b & 3c (exhaustive 1..14 + targeted A/B/C1/C2/C3a/C3b): PASS`
     - `PASS`
   - AST zero-float check: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
   - Verified file MD5s: `TARGET.md` `72a392e4c81f2ab84250fe717860ac63`, `PROOF.md` `3dd29e6f48c83b5a8fc058e60b1310c0`, `notes/check-check-1.md` `5a4b18f58b8a2a2a59cba37f875a5293`, `notes/check-check-1.py` `fe3991f1b01b282e56e7205595ab399a`.

**Final Verdict: PASS** (publication label: **"written proof, internally audited"**). Handing off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`) prior to coordinator reporting.
