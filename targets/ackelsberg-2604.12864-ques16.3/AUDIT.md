# Independent Blind Audit — `targets/ackelsberg-2604.12864-ques16.3/`

- **Auditor:** `audit-2`
- **Verdict:** **PASS**
- **Audited UTC:** 2026-11-27T11:25Z
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary source: `tools/.arxiv_cache/eprint/2604.12864.src` (`InverseProblemDensity_arXiv_v1.tex`, `arXiv:2604.12864v1`, Ethan Ackelsberg & Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.3/TARGET.md)
  - [COUNTEREXAMPLE.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.3/COUNTEREXAMPLE.md)
  - [check-check-1.md](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.3/notes/check-check-1.md) and [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/ackelsberg-2604.12864-ques16.3/notes/check-check-1.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

## 1. Statement & Primary Source Fidelity

- **Numbering verified verbatim from `InverseProblemDensity_arXiv_v1.tex`:** `\newtheorem{Theorem}{Theorem}` (L123), `\newtheorem{Question}[Theorem]{Question}` (L129), `\counterwithin{Theorem}{section}` (L162); Section 16 (`\section{Further explorations}`, L5712), Section 16.1 (L5716), preceded by Question 16.1 (L5724) and Example 16.2 (L5732), making `\begin{Question}[Finitary form of Kneser's theorem]` (L5747–5757) verbatim **Question 16.3**.
- **Definitions verified verbatim:** $\mathbb{N} = \{1, 2, 3, \ldots\}$ (L398), $[N] = \{1, \ldots, N\}$ (L405), and all quantifiers ($\forall \varepsilon > 0, N_0 \in \mathbb{N},\; \exists D > 0, N_1 \in \mathbb{N},\; \forall \alpha, \beta > 0, N \ge N_1, A, B \subset [N]$) match `TARGET.md` word-for-word.

## 2. Adversarial Mathematical Audit

- **Non-triviality ($\alpha + \beta < 1$):** Although the literal source statement omits $\alpha + \beta \le 1$ (noted transparently on L5), the main counterexample takes $\alpha = \beta = 4/9$ ($\alpha + \beta = 8/9 < 1$) and $\varepsilon = 1/10$, refuting even the intended $\alpha + \beta < 1$ strengthening.
- **Construction & hypotheses (L9–39):** For arbitrary $N_0 \in \mathbb{N}$, $D \in \mathbb{N}$ (or $D_0 = \lceil D \rceil$), and $N_1 \in \mathbb{N}$, setting $N = \max(N_1, N_0 + 1, 10D)$, $A = (2\mathbb{N} - 1) \cap [N]$, and $B = A \cup \{N - D + 1, \ldots, N\}$ satisfies:
  - $N \ge 10D \implies N - D + 1 \ge 9D + 1 \ge 10 > 2$, so $2 \notin B$ and $A \subseteq B \subsetneq [N]$ (strict inclusion holds even if $\subset$ is read strictly);
  - $N \ge N_0 + 1$ so $\{n \in \mathbb{N} : N_0 < n \le N\} \neq \varnothing$;
  - $|A \cap [n]| = \lceil n/2 \rceil \ge n/2$ for all $n \in [N]$, so $|B \cap [n]|/n \ge |A \cap [n]|/n \ge 1/2 > 4/9 = \alpha = \beta$;
  - $\{N - D + 1, \ldots, N\} \subseteq B$ consists of $D$ consecutive integers, so $B$ intersects every residue class mod $D$.
- **Sumset upper bound (L43–68):** Every $a \in A$ is odd ($\ge 1$); if $b \in B$ is odd then $a + b$ is even; if $b \in B$ is even then $b \in \{N - D + 1, \ldots, N\}$, so $a + b \ge N - D + 2$ is odd. Thus $|(A + B) \cap [N]| \le \lfloor N/2 \rfloor + \lceil (D - 1)/2 \rceil = \lfloor N/2 \rfloor + \lfloor D/2 \rfloor \le N/2 + D/2$ (valid for all $D \ge 1$), giving $|(A + B) \cap [N]|/N \le 1/2 + D/(2N) \le 11/20 < 71/90 = \alpha + \beta - \varepsilon$.
- **General $0 < \varepsilon < 1/2$ remark (L70):** Setting $\alpha = \beta = 1/2 - \eta$ with $0 < \eta < (1/2 - \varepsilon)/2$ (so $\delta := 1/2 - \varepsilon - 2\eta \in (0, 1/2)$) and $N \ge \max(N_1, N_0 + 1, \lceil D_0/\delta \rceil)$ automatically forces $N > 2D_0$ (hence $N - D_0 + 1 \ge D_0 + 2 > 2$, $A, B \subsetneq [N]$) and $1/2 + D_0/(2N) \le 1/2 + \delta/2 < 1/2 + \delta = \alpha + \beta - \varepsilon$. Completely airtight.

## 3. Independent Mechanical Verification & Gate 2 Novelty

- AST check of `targets/ackelsberg-2604.12864-ques16.3/notes/check-check-1.py`: **`FLOAT_CONSTANTS: 0 []`**.
- Executed `.venv/bin/python -u targets/ackelsberg-2604.12864-ques16.3/notes/check-check-1.py`: exit code `0`, `PASS` (60 primary tuples $(N_0, D, N_1)$ + 64 general-$\varepsilon$ instances across $\varepsilon \in \{1/10, 1/3, 2/5, 9/20\}$).
- Gate 2 novelty receipts (`watch-1`, `watch-5`, `watch-6`): all **PASS**.

## 4. Verdict

**PASS.** Ready for Gate 3 freshness novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting.

---

## 5. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T13:45Z`) — **PASS**

- **Module audited:** `lean/OpenMath/Ackelsberg260412864Ques163.lean` (imported in `lean/OpenMath.lean` L25).
- **Primary-source & `COUNTEREXAMPLE.md` fidelity:** Verified verbatim against `tools/.arxiv_cache/eprint/2604.12864.src` (`InverseProblemDensity_arXiv_v1.tex`, §1 L398/405 & §16.1 Question 16.3 L5747–5757) and `COUNTEREXAMPLE.md`:
  - Definitions match primary source verbatim: `intervalOne n := Finset.Icc 1 n` (L35, $[n] = \{1, \dots, n\}$), `finSumset A B` (L38–39, $A + B$), `MeetsAllResidues B D` (L42–43, with `ZMod D` equivalence L46–47), and counterexample sets `cexA N` (odds in $[N]$) and `cexB N D := cexA N ∪ Finset.Icc (N - D + 1) N` (L185–190).
  - Main theorems verified faithful:
    - `cex_sumset_card_le` (L234–235): proves $|(A + B) \cap [N]| \le \lfloor N/2 \rfloor + \lfloor D/2 \rfloor$ for all $1 \le D \le N$.
    - `refutes_ackelsberg_question_16_3_general` (L265–274): refutes Question 16.3 for EVERY $0 < \varepsilon < 1/2$, EVERY $N_0 \ge 1$, EVERY $D \ge 1$, and EVERY $N_1 \in \mathbb{N}$ with non-trivial $\alpha + \beta < 1$ and $N_0 < N$ (guaranteeing the index set $\{n : N_0 < n \le N\}$ is nonempty so $\min_{N_0 < n \le N} \ge \alpha$ is equivalent to $\forall n \in (N_0, N]$).
    - `not_ackelsberg_question_16_3` (L328–337): directly negates the universally quantified Question 16.3 even under the strictly stronger non-trivial hypothesis $\alpha + \beta < 1$.
- **Hygiene & kernel verification:**
  - Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or `set_option`.
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Ackelsberg260412864Ques163.lean` -> exit code `0`, zero warnings.
  - `#print axioms` on `cex_sumset_card_le`, `refutes_ackelsberg_question_16_3_general`, and `not_ackelsberg_question_16_3`: strictly `[propext, Classical.choice, Quot.sound]`.
- **Verdict:** **PASS** (upgrades status label to `machine-checked counterexample in Lean 4`).
