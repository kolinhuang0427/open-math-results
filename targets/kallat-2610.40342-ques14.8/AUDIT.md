# Blind Audit Report: `targets/kallat-2610.40342-ques14.8/` (`@audit-2`)

**Verdict: PASS (re-audit after `#705`/`#741` patches)**

*(Initial audit failed solely on source-citation numbering; all blocking defects and the §4 polish item have been patched and verified below — see §5.)*

All three non-constant counterexamples (`A = {1, 7}` mod $27$, `A = {5}` mod $25$, `A = {2, 4}` mod $4$) and the constant-residue families in `COUNTEREXAMPLE.md` are mathematically sound and unconditionally refute `Question 14.8` (`\label{prob:composite}`) of `arXiv:2610.40342v1`. However, `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-2.md` contain systematic section/theorem/equation numbering errors against the primary TeX source that must be corrected before Gate 3 / reporting.

---

## 1. Primary Source & Version Verification

- **Live arXiv query:** `arXiv:2610.40342v1` (2026-10-29, Ahaan Kallat, *"A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths"*) is the sole version on arXiv.
- **Verbatim TeX verification (`paper1_valuation_calculus.tex` in `tools/.arxiv_cache/eprint/2610.40342.src`):**
  - Preamble (L11–22): `\numberwithin{equation}{section}`, shared `[theorem]` counter within each section (`theorem`, `proposition`, `lemma`, `corollary`, `definition`, `example`, `problem` displaying as `Question`, `observation`, `remark`).
  - Section numbering verified sequentially across all `\section{...}` commands:
    - Sec. 1 (L47): Introduction — eq. `(1.1)` `\label{eq:egf}` (L58), eq. **`(1.2)`** `\label{eq:last0}` (L62). (There is no equation `(1.3)`.)
    - Sec. 11 (L910): *The global gcd over all excluded sets* (`\label{sec:ties}\label{sec:globalgcd}`), containing Theorem 11.1 (`thm:counter`), Proposition 11.2 (`prop:lead`), etc.
    - Sec. 12 (L964): *Valuations inside a residue class* (`\label{sec:interp}`).
    - **Sec. 13 (L1003):** *Composite moduli* (`\label{sec:composite}`), containing **Definition 13.1** (`\label{def:types}`, L1011–1013) and **Lemma 13.2** (`\label{lem:typeB}`, L1017–1025). Also explicitly confirmed in Kallat's ancillary `anc/interp/composite/README.md` L3 (`"Scripts and outputs behind Section 13: the two kinds of primes (Lemmas 13.2 and 13.3)..."`).
    - **Sec. 14 (L1144):** *Column 2 and open questions* (`\label{sec:open}`), containing Prop. 14.1 (`prop:col2`), Ex. 14.2 (`ex:19`), Thm. 14.3 (`thm:bad`), Thm. 14.4 (`thm:col2`), Cor. 14.5 (`cor:firstcol2`), Question 14.6 (`prob:odd`), Remark 14.7 (`rem:lines`), and **Question 14.8** (`\label{prob:composite}`, L1212–1214).
  - **Standing assumptions on $A$:** Verified throughout (L73, L544, L1012, L1213) that $A \subseteq \mathbb{N}$ is an arbitrary set of positive integers (allowed cycle lengths), with no restriction excluding finite sets, singletons, or sets missing $1$. `TARGET.md` L14 quotes Question 14.8 (`\label{prob:composite}`) verbatim, and L17 quotes the first three sentences of Lemma 13.2(a) (`\label{lem:typeB}`) verbatim.

---

## 2. Blocking Defects (Must Fix)

1. **Wrong section/definition/lemma numbering for `\label{sec:composite}`, `\label{def:types}`, `\label{lem:typeB}`:**
   - `\label{sec:composite}` is **Section 13** (not Section 11), `\label{def:types}` is **Definition 13.1** (not Definition 11.1), and `\label{lem:typeB}` is **Lemma 13.2** (not Lemma 11.2).
   - Occurrences to fix:
     - `TARGET.md` L3, L16 (`Section 11` $\to$ `Section 13`; `Definition 11.1` $\to$ `Definition 13.1`; `Lemma 11.2` $\to$ `Lemma 13.2`),
     - `COUNTEREXAMPLE.md` L5, L14, L31, L45 (`Definition 11.1` $\to$ `Definition 13.1`; `Lemma 11.2(a)` $\to$ `Lemma 13.2(a)`),
     - `notes/check-check-2.md` L3 (`Definition 11.1` $\to$ `Definition 13.1`; `Lemma 11.2` $\to$ `Lemma 13.2`).
2. **Wrong equation number for `\label{eq:last0}`:**
   - `COUNTEREXAMPLE.md` L47 cites `equation (1.3) \label{eq:last0}`. In `paper1_valuation_calculus.tex`, `\label{eq:last0}` (L62) is **equation `(1.2)`** (and the equivalent restatement in Lemma 2.1 `\label{eq:last}` is `(2.1)`). Fix `(1.3)` $\to$ `(1.2)`.

---

## 3. Mathematical Audit of `COUNTEREXAMPLE.md` (All Proofs Valid)

- **§1 ($A = \{1, 7\}$, $p = 3$, $e = 3$):** Type II ($1 \in A, 3 \notin A$), sign $+$ (predicted $\varpi(27) = 27$). EGF coefficient $a_{\{1,7\}}(n) = \sum_{j=0}^{\lfloor n/7\rfloor} \binom{n}{7j} \frac{(7j)!}{7^j j!}$ is exact. For $j \ge 2$, $3 \nmid 7$ and Legendre's formula gives $v_3((7j)!/(7^j j!)) \ge \lfloor 7j/3\rfloor - \lfloor j/3\rfloor = 2j \ge 4 > 3$, killing all $j \ge 2$ terms mod $27$. For $j = 0, 1$, $6! = 720 \equiv -9 \pmod{27}$, giving $a_{\{1,7\}}(n) \equiv 1 - 9\binom{n}{7} \pmod{27}$ for all $n \ge 0$ (including $n < 7$). Lucas's theorem mod $3$ on $7 = (21)_3$ yields the 9-periodic block $(1,1,1,1,1,1,1,19,10)$; since $a(7) \equiv 19 \not\equiv 1 \equiv a(4), a(1) \pmod{27}$, neither $1$ nor $3$ is a period, so exact least period $\varpi(27) = 9 < 27$. **PASS.**
- **§2 ($A = \{5\}$, $p = 5$, $e = 2$):** Type II ($1 \notin A, 5 \in A$), sign $-$ (predicted $\varpi(25) = 50$). $a_{\{5\}}(n) = 0$ for $5 \nmid n$ and $a_{\{5\}}(5k) = \prod_{j=0}^{k-1} (5j+1)(5j+2)(5j+3)(5j+4)$. Pairing gives $(5j+1)(5j+4) \equiv 4$ and $(5j+2)(5j+3) \equiv 6 \pmod{25}$, product $24 \equiv -1 \pmod{25}$, hence $a_{\{5\}}(5k) \equiv (-1)^k \pmod{25}$ and repeating 10-block $(1,0,0,0,0,24,0,0,0,0)$. Since $a(0)=1$ differs from $a(1), a(2), a(5) \pmod{25}$, exact least period $\varpi(25) = 10 < 50$. The parenthetical Wilson-prime generalization ($p \in \{5, 13, 563\}$) was independently checked and holds verbatim. **PASS.**
- **§3 ($A = \{2, 4\}$, $p = 2$, $e = 2$):** Type II ($1 \notin A, 2 \in A$), sign $(-1)^{[2 \in A] + [4 \in A]} = +1$ (predicted $\varpi(4) = 4$). $a_{\{2,4\}}(2m+1) = 0$. The recurrence $a(2m) = (2m-1)a(2m-2) + (2m-1)(2m-2)(2m-3)a(2m-4)$ ($m \ge 2$) with $a(0)=a(2)=1$ and parity-split induction $a(2m) \equiv 1 \pmod 4$ are exact, yielding alternating $(1, 0, 1, 0, \dots)$ with exact least period $\varpi(4) = 2 < 4$. **PASS** (modulo the `(1.3)` $\to$ `(1.2)` and `Lemma 11.2(a)` $\to$ `Lemma 13.2(a)` citation fixes above).
- **§4 (Constant-residue families):** The general claim for $A = \{1\}$ and $A = \{1, M\}$ with $p \nmid M$ and $M \ge p^e + 1$ is true for every prime $p$ and $e \ge 1$ ($v_p((Mj)!/(M^j j!)) \ge \lfloor Mj/p \rfloor - \lfloor j/p \rfloor \ge \lfloor (M-1)j/p \rfloor \ge p^{e-1}j \ge p^{e-1} \ge e$ for all $p \ge 2, e \ge 1, j \ge 1$). *Non-blocking polish:* consider inserting that one-line general inequality in L58 alongside the $A = \{1, 10\}$ example so §4 is self-contained for arbitrary $(p, e, M)$.

---

## 4. Independent Checker & Gate 2 Verification

- Re-ran `.venv/bin/python targets/kallat-2610.40342-ques14.8/notes/check-check-2.py`: `exit 0`, AST `FLOAT_CONSTANTS: 0`, exact integer recurrence DP matching all claims for $0 \le n \le 120$:
  ```
  PASS
  Verified counterexamples A={1,7} mod 27 (period 9<27), A={5} mod 25 (period 10<50), A={2,4} mod 4 (period 2<4), and constant families for 0 <= n <= 120.
  ```
- Gate 2 novelty receipts verified (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`): all 3 PASS.

---

## 5. Re-Audit Verification (`2026-11-27T10:29Z`) — **PASS**

Verified all patches from `#741` (`@scout-10`) and `@check-2`:
1. **`TARGET.md` L3, L16:** Corrected to `Section 13`, `Definition 13.1` (`\label{def:types}`), and `Lemma 13.2` (`\label{lem:typeB}`). Verbatim match against `paper1_valuation_calculus.tex` in `arXiv:2610.40342v1`.
2. **`COUNTEREXAMPLE.md` L5, L14, L31, L45, L47, L58:**
   - All four `Definition 11.1` / `Lemma 11.2(a)` citations updated to `Definition 13.1` / `Lemma 13.2(a)`.
   - L47 equation citation updated from `(1.3)` to `(1.2)` (`\label{eq:last0}`).
   - L58 now includes the complete general Legendre bound for $A = \{1, M\}$ ($p \nmid M, M \ge p^e + 1$): $v_p((Mj)!/(M^j j!)) \ge \sum_{i=1}^e (\lfloor Mj/p^i \rfloor - \lfloor j/p^i \rfloor) \ge \sum_{i=1}^e p^{e-i} j = \frac{p^e - 1}{p - 1} j \ge ej \ge e$ for all $j \ge 1$ — verified step-by-step for all primes $p \ge 2$ and $e \ge 1$.
3. **`notes/check-check-2.md` L3:** Updated to `Section 13 Definition 13.1`, `Lemma 13.2`, `(1.2)`, and L58 general bound.
4. **Independent checker (`notes/check-check-2.py`):** Exact integer DP (`FLOAT_CONSTANTS: 0`), verified `exit 0` / `PASS`.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

---

## 6. Lean 4 Statement-Fidelity Audit (`@audit-1`, Batch E `#1674`) — **PASS**

- **Module:** `lean/OpenMath/Kallat261040342Ques148.lean` (imported at line 31 of `lean/OpenMath.lean`).
- **Statement fidelity vs primary source (`paper1_valuation_calculus.tex`, `arXiv:2610.40342v1`):**
  - `AllCyclesIn A σ` & `aPerm A n` (L48–53): directly defines $a_A(n) = \#\{\sigma \in \mathrm{Perm}(\mathrm{Fin}\,n) \mid \forall x,\ |\mathrm{orbit}_\sigma(x)| \in A\}$ from Mathlib's `Equiv.Perm.SameCycle`, with `aPerm_zero : aPerm A 0 = 1`; moreover `aPerm_succ_rec` (L494–499) proves Kallat's cycle-of-$n$ recurrence eq. `(1.2)` (`\label{eq:last0}`) combinatorially from scratch.
  - `IsTypeII A p` (L57–58): `Nat.Prime p ∧ ((1 ∈ A) ↔ (p ∉ A))` matches Definition 13.1 (`\label{def:types}`, L1011–1012) verbatim.
  - `typeIINegSign A p e` & `predictedPeriod A p e` (L65–71): `(p ≠ 2 ∧ 1 ∉ A ∧ p ∈ A) ∨ (p = 2 ∧ e = 2 ∧ ((2 ∈ A) ↔ (4 ∉ A)))`, predicting `2 * p ^ e` vs `p ^ e`, matches Lemma 13.2(a) (`\label{lem:typeB}`, L1020) and Question 14.8 (`\label{prob:composite}`, L1213) verbatim.
  - `IsPeriodMod`, `IsLeastPeriodMod`, `NonConstantMod` (L74–83): exact positive-period minimality from $n = 0$ and non-constancy mod $M$.
  - **All three non-constant counterexample regimes proved:**
    - `kallat_counterexample_odd_plus` ($A_1 = \{1, 7\} \subset \mathbb{Z}_{\ge 1}$, $p = 3, e = 3$, sign $+$, predicted $27$, exact least period $9 \ne 27$, non-constant mod $27$);
    - `kallat_counterexample_odd_minus` ($A_2 = \{5\} \subset \mathbb{Z}_{\ge 1}$, $p = 5, e = 2$, sign $-$, predicted $50$, exact least period $10 \ne 50$, non-constant mod $25$);
    - `kallat_counterexample_even` ($A_3 = \{2, 4\} \subset \mathbb{Z}_{\ge 1}$, $p = 2, e = 2$, sign $(-1)^{1+1} = +1$, predicted $4$, exact least period $2 \ne 4$, non-constant mod $4$);
    - `not_kallat_question_14_8` (L1102–1105): direct negation of the universal statement of Question 14.8 even restricted to `1 ≤ e` and `NonConstantMod (aPerm A) (p ^ e)`.
- **Hygiene & kernel verification:**
  - Zero `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `partial`, `opaque`, or `set_option`.
  - Executed `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Kallat261040342Ques148.lean`: exit `0`, `0` warnings.
  - `#print axioms` on all 5 main theorems (`aPerm_succ_rec`, `kallat_counterexample_odd_plus`, `kallat_counterexample_odd_minus`, `kallat_counterexample_even`, `not_kallat_question_14_8`): strictly `[propext, Classical.choice, Quot.sound]`.
- **Lean Audit Verdict:** **PASS** — cleared for upgrade to `"Lean 4 formalized (zero sorry, verified by lake build)"` by `@coordinator`.
