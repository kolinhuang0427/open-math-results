# Blind Independent Audit Report — `targets/jensen-2605.27941-ques4/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`), `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-1.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"*, `arXiv:2605.27941v1` (submitted `2026-05-27T04:27:10Z`, sole version), **Section 5** (*Open questions and future work*, `\label{sec:future-work}`, `main.tex` L1059), **Question 4** (`main.tex` L1158–1163; 4th `\begin{question}`).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all blocking and minor fixes from initial FAIL `#1760` were cleanly applied in `PROOF.md`; publication label: **"written proof, internally audited"**).

---

## 1. Primary Source & Statement Fidelity Check

Verified verbatim against `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`):
- **Definitions (Section 2, L191–223):** Definition 1 (`Mixed Lonely Runner Conjecture`) and Definition 2 (`Mixed Loneliness Parameter Space`) match `TARGET.md` L22–28 verbatim.
- **Theorem A (Section 4, `\label{sec:MLPS2}`, L877–1056):** `\newtheorem*{thmA}{Theorem A}` (L18) proves $\mathsf{MLPS}_2 = \{(d_1, d_2) \in (0, 1/2]^2 : 2d_1 + d_2 \le 1 \text{ and } d_1 + 2d_2 \le 1\}$, matching `PROOF.md` L18 verbatim.
- **Section 5 Context & Question 4 (`main.tex` L1158–1163):**
  - Context (L1158–1159): *"Another question concerns the obstructions that define these spaces. In dimension two, the whole space is constrained by the two ordered speed pairs $(1,2)$ and $(2,1)$. It would be useful to know whether higher-dimensional spaces are similarly governed by a finite number of speed sets. If true, this would also imply that the parameter spaces are finite unions of convex sets."*
  - Question 4 (L1161–1163, 4th `\begin{question}` after L1094, L1138, L1150): *"For fixed $k$, is $\mathsf{MLPS}_k$ determined by finitely many speed sets?"*
  - Both match `TARGET.md` L30–33 verbatim. Both ordered $k$-tuple and unordered $k$-element set interpretations are handled rigorously (`PROOF.md` L8, L15, L163).
- **`TARGET.md` fidelity:** **PASS** (zero defects).

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Section 1 (L12–21) — Affirmative Cases ($k = 1, 2$):** **SOUND.**
  - $k = 1$: $t = \frac{1}{2s_1}$ witnesses $\|s_1 t\| = \frac{1}{2} \ge d_1$, so $\mathsf{MLPS}_1 = (0, 1/2] = U(\{(1)\})$.
  - $k = 2$: Theorem A (`main.tex` L877–1056) gives $\mathsf{MLPS}_2 = \{(d_1, d_2) \in (0, 1/2]^2 : 2d_1 + d_2 \le 1,\; d_1 + 2d_2 \le 1\}$. For $(d_1, d_2) \in (0, 1/2]^2$, both safe-interval families for $(1, 2)$ are symmetric under $t \mapsto 1 - t$ with $d_2/2 \le 1/4 < 1/2 \le 1 - d_1$, so intersection holds iff $d_1 \le (1 - d_2)/2 \iff 2d_1 + d_2 \le 1$; symmetry gives $d_1 + 2d_2 \le 1$ for $(2, 1)$. Thus $\mathsf{MLPS}_2 = U(\{(1, 2), (2, 1)\})$.
- **Section 2 (L25–45) — Lemma 0 (Piecewise-Affine Convexity):** **SOUND.**
  - Half-integer breakpoint set $B_{\mathbf{s}} = \{\frac{j}{2s_i} : 1 \le i \le k,\; 0 \le j \le 2s_i\} \subset [0, 1]$ partitions $[0, 1]$ into closed subintervals $I_{\mathbf{s}, r}$ on which each $t \mapsto \|s_i t\|$ is affine ($s_i t - m$ or $(m+1) - s_i t$).
  - Direct convex-combination witness $t_\lambda = (1-\lambda)t + \lambda t' \in I_{\mathbf{s}, r}$ proves $C_{\mathbf{s}, r}$ convex (including empty case); distributing finite intersection over finite unions proves $U(\mathcal{S})$ is a finite union of convex sets (including $\mathcal{S} = \emptyset$, where $U(\emptyset) = (0, 1/2]^k$ is convex).
- **Section 3.1 (L52–65) — Explicit Construction $\{Q_n^{(k)}\}_{n \ge 5}$:** **SOUND.** All range, identity, and monotonicity claims verified.
- **Section 3.2 (L67–98) — Lemmas 1 and 2:** **SOUND.**
  - Lemma 1 speed tuple $(2, 2n+1, 1, s_4, \dots, s_k)$ obstruction verified completely (including $y > \frac{n-x}{2n+1} > \frac{5 - 1/9}{11} = \frac{4}{9} > \frac{1}{3}$ for all $n \ge 5$).
  - Lemma 2 segment exit verified completely, including the exact decomposition $\frac{2m+2n+5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{9}{14} < \frac{2}{3}$ (L92), giving $\frac{y_n - y_m}{x_m - x_n} < \frac{3}{4}\cdot\frac{130}{129} < 1$ and $y^* - \frac{n-x^*}{2n+1} > \frac{16n^2 + 74n + 73}{20(n+1)(2n+1)(2n+3)^2} > 0$.
- **Section 3.3 (L100–158) — Lemmas 3a, 3b, 3c, 4:**
  - **Lemma 3a (L104–108):** **SOUND** as stated ($\lfloor sL \rfloor$ subintervals of length $1/s$ plus one remainder of length $< 1/s$). *(See Minor Defect 2 below regarding its invocation on shifted $\|su + \frac{1}{2}\|$ at L145–147.)*
  - **Lemma 3b (L110–122) — BLOCKING DEFECT at L120:**
    - In L115, $s_3 = 2^\alpha u_0$ and $g_0 = 2^\beta v_0$ ($u_0, v_0$ odd) with $2s_3 = q g_0$, so $v_2(q) = (\alpha + 1) - \beta$.
    - Therefore, $q$ is even ($v_2(q) \ge 1$) if and only if **$0 \le \beta \le \alpha$**, NOT $0 \le \beta \le \alpha - 1$ (which holds only when $4 \mid q$).
    - **L120 writes:** `Case $q \ge 4$ even ($0 \le \beta \le \alpha - 1$, $a$ odd, $(q/2) \mid s_3$):`
    - This parenthetical inequality is **literally false** for every $q \ge 6$ with $q \equiv 2 \pmod 4$: for instance, $s_3 = 3, s = 1$ gives $\alpha = 0, \beta = 0, q = 6 \ge 4$ even, where $0 \le \beta \le \alpha - 1$ asserts $0 \le 0 \le -1$. (Meanwhile, $(q/2) \mid s_3$ still follows immediately from $2s_3 = q g_0 \implies s_3 = (q/2)g_0$, and all counting steps in L120–122 remain valid for all even $q \ge 4$.)
    - Note also L116 (`Case $q = 2$ ($\beta = \alpha$, $a$ odd)`): true as an implication, though writing `($\beta = \alpha$, $u_0 = v_0$, $a$ odd)` avoids suggesting $\beta = \alpha$ characterizes $q = 2$.
  - **Lemma 3c (L124–153):** Core math and case coverage across Regimes A, B, C1, C2, C3a, C3b are **SOUND** (including $s_2 t^* = \frac{s_2(n+2)}{2n+3}$, $q(2n+4)+d_n$, $r(n+2)+d_n$ in C3a and all 7 parity/size pairings in C3b).
    - **Minor Defect 2 (L145–147):** Lemma 3a (L105–106) is stated only for unshifted $\|st\| < x$ on $J \subseteq [0, 1)$, but L145 writes *"By Lemma 3a on $[0, \eta_n]$:"* and then applies it to odd $s \ge 3$ where $\|s(\frac{1}{2} + u)\| = \|su + \frac{1}{2}\|$. In the $t$-variable this is unshifted Lemma 3a applied on $J = [\frac{1}{2}, \frac{1}{2} + \eta_n] \subseteq [0, 1)$ (length $\eta_n$), or else Lemma 3a can be stated with an arbitrary shift $\theta \in \mathbb{R}$ (`\|st + \theta\| < x`).
  - **Lemma 4 (L155–158) & Section 4 (L162–165):** **SOUND.**

---

## 3. Independent Verifier Audit (`notes/check-check-1.py`)

- Re-executed `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py`: exited `0`, `PASS`.
  - `Section 1 (k=1 and k=2 exact grid + small speed pairs): PASS`
  - `Lemma 0 (piecewise-affine breakpoints, affinity, U(S) distribution, convexity): PASS`
  - `Section 3.1 & Lemmas 1-2 (including midpoint m=5,n=7): PASS`
  - `Lemmas 3b, 3c, 4 (exhaustive 1..14 + targeted + k=4 union bound): PASS`
  - `PASS`
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Verified file MD5s at initial audit:
  - `TARGET.md`: `cf0cc0cacb9c59387875802f7eb593e7`
  - `PROOF.md`: `aa2afbe591f840db7875d7cb825f961b`
  - `notes/check-check-1.md`: `f9090150db1b0058791a117b4747879f`
  - `notes/check-check-1.py`: `e91c3aece982f8168ca1f6f54e65e92a`
- Verifier logic inspected line-by-line (L1–348): **PASS** (no changes needed to `check-check-1.{md,py}`).

---

## 4. Gate 2 Novelty Status

- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`2026-11-27T17:11Z`, `0/745` snapshot hits, `2605.27941v1` sole arXiv version, sole OpenAlex citer `2609.06259v3` verified passing cite only, GH/Zenodo/HexagonMath/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

Following `@scout-10` (`#1762`), `@audit-2` re-verified the patched `PROOF.md` verbatim on disk and re-executed the independent verifier:

1. **Blocking Defect 1 resolved (`PROOF.md` L116, L120):** L120 updated to `Case $q \ge 4$ even ($0 \le \beta \le \alpha$, $a$ odd, $(q/2) \mid s_3$)` (covering all $q \equiv 2 \pmod 4$ as well as $4 \mid q$), and L116 clarified to `Case $q = 2$ ($\beta = \alpha$, $u_0 = v_0$, $a$ odd)` (`s_3 = g_0`).
2. **Minor Defect 2 resolved (`PROOF.md` L105–108):** Lemma 3a generalized cleanly to arbitrary shift $\theta \in \mathbb{R}$ (`\|st + \theta\| < x`, period $[\frac{m-\theta}{s}, \frac{m+1-\theta}{s})$), matching both even and odd applications in Subcase C3b (L145–147).
3. **Final independent re-run by `@audit-2`:**
   - Command: `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py` -> exit `0`, raw stdout:
     - `Section 1 (k=1 and k=2 exact grid + small speed pairs): PASS`
     - `Lemma 0 (piecewise-affine breakpoints, affinity, U(S) distribution, convexity): PASS`
     - `Section 3.1 & Lemmas 1-2 (including midpoint m=5,n=7): PASS`
     - `Lemmas 3b, 3c, 4 (exhaustive 1..14 + targeted + k=4 union bound): PASS`
     - `PASS`
   - AST zero-float check: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
   - Verified file MD5s: `TARGET.md` `cf0cc0cacb9c59387875802f7eb593e7`, `PROOF.md` `963e60665bca7620f1b6af3074a4d06e`, `notes/check-check-1.md` `f9090150db1b0058791a117b4747879f`, `notes/check-check-1.py` `e91c3aece982f8168ca1f6f54e65e92a`.

**Final Verdict: PASS** (publication label: **"written proof, internally audited"**). Handing off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`) prior to coordinator reporting.
