# Blind Adversarial Audit Report: `targets/yasutomi-2609.32450-conj6.1/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T09:59Z`
- **Verdict:** **PASS** (after re-audit of `#583`/`#599` fixes; initial audit at `09:59Z` was FAIL due to 2 blocking errors in `PROOF.md`, now fully resolved — see §5)
- **Files Audited (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2609.32450/lagrangev2.tex` (`arXiv:2609.32450v2`), `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (`arXiv:2609.32450v2`)

- **Latest Version Check:** Live arXiv query (`tools/arxiv_fetch.py query --id-list 2609.32450`) confirms `2609.32450v2` (published `2026-09-26`, updated `2026-10-14`, Shin-ichi Yasutomi, *"On the Ordering and Injectivity of Lagrange Constants Associated with Certain Substitutions"*) is the latest version, with no journal ref or DOI.
- **Numbering Check (`lagrangev2.tex`):** `\newtheorem{thm}{Theorem}[section]` (L15) and `\newtheorem{con}[thm]{Conjecture}` (L19); Section 5 (`\section{Conjecture}`, L1833) contains `\begin{con}` at L1840–1876, which is **Section 5, Conjecture 5.1**. Both `TARGET.md` and `PROOF.md` now cite **Section 5, Conjecture 5.1** accurately (retaining historical folder slug `yasutomi-2609.32450-conj6.1`), and the verbatim LaTeX of `\label{l1}` (L135–144) and `\begin{con}` (L1840–1876) matches `TARGET.md` verbatim.
- **Minor citation note:** `TARGET.md` L12 labels `Lemma l1` as `(Section 2)`, whereas `\begin{lem}\label{l1}` is stated in **Section 1** (`lagrangev2.tex` L135, Lemma 1.4) and proved in Section 2 (L221).
- **Soundness of cited Theorem `\ref{t3}` (Theorem 3.5, L798–805):** Verified directly from `lagrangev2.tex` L567–805 that Lemmas 3.2–3.4 (`\ref{l4}`–`\ref{l6}`) and Theorem 3.5 (`\ref{t3}`) hold for all integers $1 \le a < b$ and all $x \in \mathbb{Q} \cap [0, 1]$.

---

## 2. Blocking Mathematical Defects Found

### Blocking Defect 1 — False inequality in Section 1.2 boundary case $0 < x < y = 1$ (`PROOF.md` L28)

`PROOF.md` L28 argues:
> *"there is a minimal $k \ge 1$ with $G(x, -k) = 0$. Hence $a_{-1} \dots a_{-2k} = \underbrace{b \dots b}_{2k-2} a a$ (an even number $2k-2$ of $b$'s followed by $a < b$), which yields $[0; a_{-1}, a_{-2}, \dots] > [0; \overline{b}]$. Thus $L(x, 1) > b + 2[0; \overline{b}] = \mathcal{L}(1)$."*

This is **false** due to an off-by-one parity error:
- By definition (`lagrangev2.tex` L572, `PROOF.md` L13), $a_{2m-1} a_{2m} = \phi_{a,b}(G(x, m))$.
- Thus $G(x, 0) = 1$ gives $a_{-1} = b$ (**$1$** copy of $b$), $G(x, -1) = \dots = G(x, -(k-1)) = 1$ give $a_{-2} \dots a_{-2k+1} = b^{2k-2}$ (**$2k-2$** copies of $b$), and $G(x, -k) = 0$ gives $a_{-2k} a_{-2k-1} = aa$.
- Therefore $a_{-1} a_{-2} \dots a_{-2k-1} = \underbrace{b \dots b}_{2k-1} a a$ has an **odd** number ($2k-1$) of $b$'s before the first discrepancy $a_{-2k} = a < b$, which sits at the **even** index $2k$.
- Consequently, the continued fraction satisfies the **opposite** strict inequality $[0; a_{-1}, a_{-2}, \dots] < [0; \overline{b}]$ for **every** $x \in \mathbb{Q} \cap (0, 1)$ and $1 \le a < b$.
- **Explicit counterexample to the claimed step:** For $a = 2, b = 3, x = 1/2$, we have $G(1/2, 0) = 1, G(1/2, -1) = 0$, so $[0; a_{-1}, a_{-2}, \dots] = [0; \overline{3, 2, 2, 3}] \approx 0.2931837 < 0.3027756 \approx [0; \overline{3}]$ (exact algebraic difference $\approx -0.009592$).
- **Required fix:** Replace the false claim $[0; a_{-1}, a_{-2}, \dots] > [0; \overline{b}]$ with a valid proof that $[0; a_1, a_2, \dots] + [0; a_{-1}, a_{-2}, \dots] > 2[0; \overline{b}]$ for all $0 < x < 1$ (under the Type (3) hypotheses $a \ge 2$ or $b \ge a^2+2$, or for all $1 \le a < b$).

### Blocking Defect 2 — False lower bound in Section 4, Type (1) Part (I)(1), Case $n \ge 3$, $b = a^2 + 1$ (`PROOF.md` L135; echoed in `notes/check-check-3.py` L176)

`PROOF.md` L134–135 states:
> *"Meanwhile $m_2 \ge \frac{a m_4}{ab+1}$. If $b = a^2 + 1$: keeping the $m_2 m_4$ term gives $(b-a)(ab-1)(q_{AA} q_{AB} - q_{SA} q_{SB}) > (a^2-a+1)(a^3+a-1)\frac{2(a-1)(a^2+1)^2((a^2+1)^2+1)}{a+1/a} m_4^2 > (a^2+2)^4 m_4^2$ for all $a = 2+u \ge 2$."*

This denominator **$a + 1/a$ is wrong**:
- At $b = a^2 + 1$, $\frac{a}{ab + 1} = \frac{1}{b + 1/a} = \frac{1}{a^2 + 1 + 1/a}$, **not** $\frac{1}{a + 1/a}$.
- **Explicit counterexample to the claimed bound $m_2 / m_4 \ge \frac{1}{a + 1/a}$:** Take $a = 2, b = a^2 + 1 = 5, n = 3$ with $c_2 = b = 5$, so $M = B = \begin{pmatrix}1 & 5 \\ 5 & 26\end{pmatrix}$. Then $m_2 / m_4 = \frac{5}{26} \approx 0.1923 < \frac{2}{5} = \frac{1}{a + 1/a}$.
- Furthermore, `notes/check-check-3.py` L176 copied `rhs_b1 = (a + sp.Rational(1) / a) * (a**2 + 2) ** 4` verbatim, so it checked the false bound rather than the true bound.
- **Independent confirmation that the fix works:** With the true denominator $a^2 + 1 + 1/a$, the auditor verified in exact SymPy arithmetic that $a\bigl((a^2-a+1)(a^3+a-1)\cdot 2(a-1)(a^2+1)^2((a^2+1)^2+1) - (a^2+1+1/a)(a^2+2)^4\bigr)$ expanded at $a = 2 + u$ has all $16$ coefficients strictly positive (`[2, 56, 742, ..., 55944]`). Both `PROOF.md` L135 and `notes/check-check-3.py` L176 (and author `verify.py`) must be updated to use $a^2 + 1 + 1/a$.

---

## 3. Non-Blocking Precision Issues (Should Be Fixed in the Same Patch)

1. **`PROOF.md` L67:** $\frac{1}{b+1} < \frac{a}{ab+1}$ is an equality ($\frac{1}{b+1} = \frac{1}{b+1}$) when $a = 1$; write $\frac{1}{b+1} \le \frac{a}{ab+1} < \frac{b}{b^2+1} \le \alpha, \beta < \frac{1}{a}$.
2. **`PROOF.md` L94:** *"if $y_2 \le x_2$ then $L(y,1) - L(x,1) < 0$ holds immediately"* omits checking the positive term $+\frac{1}{q_{AB} Q_{AB}(y_1)}$ against $-\frac{(b-a)(ab-1)}{q_{AA} q_{AB}}$; in fact the bound L96 already holds uniformly without assuming $y_2 > x_2$ (since $y_2 - x_2 < b - a$ holds even when $y_2 \le x_2$, or note directly $(b-a)(ab-1) Q_{AB}(y_1) > q_{AB} > q_{AA}$).
3. **`PROOF.md` L164:** $q_{AA} < m_4(X + \frac{1}{4C_U}) C_U$ should be $\le$ (equality holds for $a = 1, n = 3, M = A$ where $m_4 = 2$; the downstream strict inequalities remain unaffected since $q_{SA} q_{SB} - q_{AA} q_{AB} > m_4^2 (Y^2 - X^2) C_U C_V$ is strict).
4. **`notes/check-check-3.py` L2–3:** Update docstring from `"referred to as Conjecture 6.1 in TARGET.md/PROOF.md"` to reflect Section 5, Conjecture 5.1.

---

## 4. Sections Verified Sound

- **Section 1.1 (Tail bounds):** Sound (verified $(a+\frac{1}{a+1})^2 - a(a+\frac{1}{a+1}) - 1 = \frac{1-(a+1)}{(a+1)^2} < 0$, $[\overline{1}] > 8/5$, $[\overline{a}]^2 > a^2+1$, $[\overline{b}] - [\overline{a}] < b-a$, and $T_a(z) < a + 1/a \le b < [\overline{b}]$).
- **Section 1.2 (Boundary cases $(0,1)$ and $0 < y < 1$):** Sound.
- **Section 1.3 (Matrix setup & convergent identities):** All signs, parity of determinants, and Type (1)–(3) decompositions match `lagrangev2.tex` Lemmas `ml1`–`ml3`.
- **Section 1.4 (Structural matrix bounds, aside from L67 strict `<` at $a=1$):** Sound, including the $a=1$ induction $\alpha, \beta \le \frac{13}{21} < \frac{5}{8}$.
- **Section 2 (Type (2)):** Completely sound (all 10 $(m_1,m_2,m_3,m_4)$ coefficients strictly positive on $u,v \ge 0$).
- **Section 3 (Type (3), modulo L94 wording):** All polynomial inequalities verified strictly positive with strictly positive denominators in independent SymPy audit.
- **Section 4 (Type (1) Part (I)(1), aside from L135 `a + 1/a` bug):** $n = 2$ and $n \ge 3$ ($a+1 \le b \le a^2$) verified strictly positive.
- **Section 5 (Type (1) Part (II)(1), modulo L164 `<` vs `<=`):** $n = 2$, $n \ge 3$ ($a=1, b=3$; $a=1, b \ge 4$; $a \ge 2, b \ge a^2+2$) all verified strictly positive with strictly positive denominators in independent SymPy audit.
- **Checker script run:** `.venv/bin/python targets/yasutomi-2609.32450-conj6.1/notes/check-check-3.py` exited `0` (`PASS`, `FLOAT_CONSTANTS: 0`), but requires updating L176 once `PROOF.md` L135 is patched.
- **Gate 2 receipts:** `notes/novelty-gate2-watch-{1,5,6}.md` all PASS.

---

## 5. Re-Audit Following `#583` / `#599` Patches (`2026-11-27T10:15Z`) — **PASS**

Re-read `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, and `notes/check-check-3.py` (L1–200) and re-ran `.venv/bin/python targets/yasutomi-2609.32450-conj6.1/notes/check-check-3.py`:

1. **Blocking Defect 1 (`PROOF.md` L28, boundary case $0 < x < y = 1$) — RESOLVED:**
   - Replaced the false backward-tail parity argument with an explicit exact lower bound using $\mathcal{L}(1) = \sqrt{b^2+4} = b + \frac{4}{\sqrt{b^2+4}+b} < b + \frac{2}{b}$, $[0; a_1, a_2, \dots] > \frac{1}{a + 1/a} = \frac{a}{a^2+1}$, and $[0; a_{-1}, a_{-2}, \dots] > \frac{1}{b + 1/a} = \frac{a}{ab+1}$.
   - Verified every algebraic step by hand:
     - $a \ge 2$: $\frac{a}{a^2+1} + \frac{a}{ab+1} - \frac{2}{b} = \frac{a^2 b(b-a) - 2a^2 - 2}{b(a^2+1)(ab+1)} \ge \frac{a^3 - a^2 - 2}{b(a^2+1)(ab+1)} > 0$.
     - $a = 1, b \ge 3$: $[0; 1, 1, a_3, \dots] > [0; 1, 1, b+1] = \frac{b+2}{2b+3} > \frac{1}{2}$ and $[0; a_{-1}, \dots] > \frac{1}{b+1}$, with $\frac{1}{2} + \frac{1}{b+1} - \frac{2}{b} = \frac{b^2 - b - 4}{2b(b+1)} > 0$.
     - $a = 1, b = 2$: $L(x, 1) > 2 + \frac{4}{7} + \frac{1}{3} = 2 + \frac{19}{21} > \frac{20}{7} > \sqrt{8}$ (since $\frac{400}{49} > 8$).
2. **Blocking Defect 2 (`PROOF.md` L135 & `notes/check-check-3.py` L176, $b = a^2+1$) — RESOLVED:**
   - Both `PROOF.md` L135 and `notes/check-check-3.py` L176 now use the true denominator $a^2 + 1 + 1/a$ from $\frac{a}{ab+1} = \frac{1}{a^2+1+1/a}$.
3. **Non-blocking precision items — ALL RESOLVED:** `TARGET.md` L12 (`Section 1, Lemma 1.4; proved in Section 2`), `PROOF.md` L67 ($\frac{1}{b+1} \le \frac{a}{ab+1} < \frac{b}{b^2+1} \le \alpha,\beta < \frac{1}{a}$), L94 (uniform bound regardless of sign of $y_2 - x_2$), L164 ($\le$ for $m_4 \ge 2$), and `notes/check-check-3.py` L2–3 docstring (`Section 5, Conjecture 5.1`).
4. **Fresh Independent Verifier Run:** `.venv/bin/python targets/yasutomi-2609.32450-conj6.1/notes/check-check-3.py` exited `0`, raw output:
   ```text
   [1/5] Checking Sections 1.3 & 1.4 matrix & convergent identities...
   [2/5] Checking Section 2 (Type 2) polynomial inequalities...
   [3/5] Checking Section 3 (Type 3) polynomial inequalities...
   [4/5] Checking Section 4 (Type 1, Part I(1)) identities & inequalities...
   [5/5] Checking Section 5 (Type 1, Part II(1)) + exact direct tests...
   PASS
   ```

**Final Verdict:** **PASS.** Ready for Gate 3 freshness check (`<1h`) before reporting.
