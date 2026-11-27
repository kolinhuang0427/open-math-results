# Independent Blind Audit — `targets/ackelsberg-2604.12864-ques16.4/`

- **Auditor:** `audit-2`
- **Verdict:** **PASS**
- **Audited UTC:** 2026-11-27T11:13Z
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary source: `tools/.arxiv_cache/eprint/2604.12864.src` (`InverseProblemDensity_arXiv_v1.tex`, `arXiv:2604.12864v1`, Ethan Ackelsberg & Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/TARGET.md)
  - [COUNTEREXAMPLE.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/COUNTEREXAMPLE.md)
  - [check-check-1.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.md) and [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.py)
  - Gate 2 novelty receipts: [novelty-gate2-watch-1.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/notes/novelty-gate2-watch-1.md), [novelty-gate2-watch-5.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/notes/novelty-gate2-watch-5.md), [novelty-gate2-watch-6.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.4/notes/novelty-gate2-watch-6.md)

## 1. Statement & Primary Source Fidelity

- **Numbering verified directly from `InverseProblemDensity_arXiv_v1.tex`:**
  - `\newtheorem{Theorem}{Theorem}` (L123), `\newtheorem{Question}[Theorem]{Question}` (L129), `\newtheorem{Example}[Theorem]{Example}` (L134), `\counterwithin{Theorem}{section}` (L162).
  - `\section{Further explorations}` (L5712) is Section 16; `\subsection{More on direct theorems for sumsets in the integers}` (L5716) is Section 16.1; preceded by Question 16.1 (`q_logarithmic_density_Kneser`, L5724), Example 16.2 (L5732), and Question 16.3 (L5747), so `\begin{Question}[Kneser's theorem in $\N^2$]` (L5771–5777) is verbatim **Question 16.4**.
- **Definitions verified verbatim:** $\mathbb{N} = \{1,2,3,\ldots\}$ (L398), $[N] = \{1,\ldots,N\}$ (L405), rectangular $\liminf_{n,m\to\infty}$, $\underline{d}(A) = \liminf_{n,m\to\infty} \frac{|A \cap ([n]\times[m])|}{nm}$, and $H_{a,b,c} = \{(an+bm, cm) : m, n \in \mathbb{Z}\}$ ($a, c \in \mathbb{N}$, $b \in \{0,\ldots,a-1\}$) (L5760–5768).
- **Source typo transparency:** The source text L5776 prints `d(A+H)+d(A+H)-d(H)` instead of `d(A+H)+d(B+H)-d(H)`. Since the counterexample sets $A = B$ and directly refutes the preceding clause ("$A+B$ equals, up to finitely many elements, a finite union of translates of $H$"), both readings are refuted identically.

## 2. Adversarial Mathematical Audit

Checked every step of `COUNTEREXAMPLE.md` for hidden hypotheses, quantifier slips, edge cases, and boundary behavior:

1. **Construction & Exact Slices (§1):** $A = B = (2\mathbb{N} \times \mathbb{N}_{\ge 3}) \sqcup \{(2^j, 1) : j \in \mathbb{N}\} \subseteq \mathbb{N}^2$ is nonempty. Pairwise sumsets $A_0 + A_0 = 2\mathbb{N}_{\ge 2} \times \mathbb{N}_{\ge 6}$, $A_0 + A_1 = A_1 + A_0 = 2\mathbb{N}_{\ge 2} \times \mathbb{N}_{\ge 4}$ (since $2^1 = 2$ already covers all $2k + 2 \in 2\mathbb{N}_{\ge 2}$), and $A_1 + A_1 = \{(2^j + 2^{j'}, 2) : j, j' \in \mathbb{N}\}$ are exact, yielding the stated horizontal slices on $y \in \{1,3\}$, $y = 2$, and $y \ge 4$.
2. **Lower Densities (§2):** For all $n, m \ge 4$, $|A \cap ([n]\times[m])| = \lfloor n/2 \rfloor (m - 2) + \lfloor \log_2 n \rfloor$ and $|(A+B) \cap ([n]\times[m])| = (\lfloor n/2 \rfloor - 1)(m - 3) + S(n)$ with $0 \le S(n) \le (\lfloor \log_2 n \rfloor)^2$. Since $\frac{(\lfloor \log_2 n \rfloor)^2}{nm} \le \frac{(\log_2 n)^2}{n} \cdot \frac{1}{m} \to 0$ uniformly over $n, m \ge N \to \infty$, we get $\underline{d}(A) = \underline{d}(B) = d(A) = \frac{1}{2}$ and $\underline{d}(A+B) = d(A+B) = \frac{1}{2} < 1 = \underline{d}(A) + \underline{d}(B)$.
3. **Obstruction to Finite Union of Translates (§3):**
   - Suppose $(A+B) \triangle \bigcup_{i=1}^r (v_i + H)$ is finite for some $H = H_{a,b,c} \cap (\mathbb{N}\times\mathbb{N})$ ($a, c \in \mathbb{N}$, $b \in \{0,\ldots,a-1\}$). Note that even if arbitrary real/rational translation vectors $v_i \in \mathbb{R}^2$ were allowed, any translate with $v_i \notin \mathbb{Z}^2$ is disjoint from $\mathbb{N}^2$ (and cannot be within a finite symmetric difference of a subset of $\mathbb{N}^2$ since $H$ is infinite), so taking $v_i \in \mathbb{Z}^2$ is without loss of generality.
   - Intersecting $v_i + H$ with $L_2 = \mathbb{N} \times \{2\}$ forces $cm = 2 - v_{i,2} \in \mathbb{N}$, uniquely determining $m_i = (2 - v_{i,2})/c$; if $m_i \notin \mathbb{N}$ the intersection is empty, and if $m_i \in \mathbb{N}$ the intersection is exactly $\{(x, 2) : x \equiv v_{i,1} + b m_i \pmod a,\; x \ge \max(1, v_{i,1}+1)\}$ (both directions checked: $x \ge 1$ puts $(x,2) \in L_2$ and $x \ge v_{i,1}+1$ puts $an + bm_i = x - v_{i,1} \in \mathbb{N}$).
   - **Case 1 ($I = \varnothing$):** $U \cap L_2 = \varnothing$, whereas $(A+B) \cap L_2 \supseteq \{(2^j + 2, 2) : j \in \mathbb{N}\}$ is infinite.
   - **Case 2 ($I \neq \varnothing$):** On $[X_0, 2^K]$ ($2^K > X_0$), there are $2^K - X_0 + 1 > \lfloor (2^K - X_0)/a \rfloor \cdot a$ consecutive integers, so any residue class mod $a$ has at least $\lfloor (2^K - X_0)/a \rfloor$ elements in $[X_0, 2^K]$, whereas $|(A+B) \cap ([2^K]\times\{2\})| \le K^2$. Letting $K \to \infty$ gives $|(U \setminus (A+B)) \cap L_2| = \infty$, contradiction.

## 3. Independent Mechanical Verification & Gate 2 Novelty

- AST check of `targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.py`: **`FLOAT_CONSTANTS: 0 []`**.
- Executed `.venv/bin/python -u targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.py`: exit code `0`, `PASS` (brute-force sumset on $[1..150]\times[1..40]$ = 2763 pts; exact `Fraction` counts on $4 \le n, m \le 64$ & separation at $N = 2^{20}$; 21,675 `(a,b,c,v)` AP slice checks + Case 2 asymptotic gaps).
- Gate 2 novelty receipts (`watch-1`, `watch-5`, `watch-6`): all **PASS** (`arXiv:2604.12864v1` sole version, 0 Question 16.4 hits across 651 snapshots/Zenodo/GitHub/web).

## 4. Verdict

**PASS.** Ready for Gate 3 freshness novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting.

---

## 5. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T13:45Z`) — **PASS**

- **Module audited:** `lean/OpenMath/Ackelsberg260412864Ques164.lean` (imported in `lean/OpenMath.lean` L26).
- **Primary-source & `COUNTEREXAMPLE.md` fidelity:** Verified verbatim against `tools/.arxiv_cache/eprint/2604.12864.src` (`InverseProblemDensity_arXiv_v1.tex`, §1 L398/405 & §16.1 Question 16.4 L5759–5777) and `COUNTEREXAMPLE.md`:
  - Definitions match primary source verbatim: `PosGrid` (L43, $\mathbb{N}^2$ with $\mathbb{N} = \{1,2,\dots\}$), `sumset2` (L46–47), `box n m` (L50–51, $[n]\times[m]$), `boxDensity`, `tailInf`, and `lowerDensity A := ⨆ N : ℕ, tailInf A (N + 1)` (L55–65, with literal `Filter.Tendsto` convergence proven in `tendsto_tailInf_cexA` & `tendsto_tailInf_sumset_cexA` L501–511), `H_abc a b c` (L69–70), `Hpos a b c` (L73–74, $H_{a,b,c} \cap (\mathbb{N}\times\mathbb{N})$), `translateH v H` and `finiteUnionTranslates V H` (L77–82, arbitrary finite sets $V \subset \mathbb{Z}^2$).
  - Main theorems verified faithful:
    - `lowerDensity_cexA` (L409) and `lowerDensity_sumset_cexA` (L454): prove $\underline{d}(A) = 1/2$ and $\underline{d}(A + A) = 1/2 < 1 = \underline{d}(A) + \underline{d}(A)$.
    - `symmDiff_sumset_cexA_infinite` (L518–520): proves $(A + A) \triangle \bigcup_{v \in V} (v + H)$ is infinite for every $a \ge 1, c \ge 1, b \in \mathbb{N}$ and every `V : Finset (ℤ × ℤ)`.
    - `refutes_ackelsberg_question_16_4` (L621–626) and `not_ackelsberg_question_16_4` (L633–638): directly refute Question 16.4 (dropping the extra density equation from the negated second disjunct makes the negation strictly stronger and avoids the source's `d(A+H)+d(A+H)-d(H)` typo).
- **Hygiene & kernel verification:**
  - Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or `set_option`.
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Ackelsberg260412864Ques164.lean` -> exit code `0`, zero warnings.
  - `#print axioms` on `lowerDensity_cexA`, `lowerDensity_sumset_cexA`, `symmDiff_sumset_cexA_infinite`, `refutes_ackelsberg_question_16_4`, and `not_ackelsberg_question_16_4`: strictly `[propext, Classical.choice, Quot.sound]`.
- **Verdict:** **PASS** (upgrades status label to `machine-checked counterexample in Lean 4`).
