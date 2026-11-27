# Blind Audit: `targets/garrity-2410.02032-conj1/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (after `#807` & `#840` patches; see §4–§5 below — initial FAIL & Re-Audit #1 findings all resolved)
- **Primary Source Verified:** Thomas Garrity & Otto Vaughn Osterman, *"On the Factor Complexity Associated with a Family of Multidimensional Continued Fraction Algorithms"*, `arXiv:2410.02032v2` (`2026-07-21`; published *Combinatorics and Number Theory* 15 (2026), 239–292, DOI `10.2140/cnt.2026.15.239`, Crossref verified), both TeX source (`tools/.arxiv_cache/eprint/2410.02032/Final_Revision-Garrity-Osterman.tex`) and compiled arXiv PDF (44 pages).

---

## 1. Primary Source Fidelity & Compiled Numbering

Verified verbatim against `Final_Revision-Garrity-Osterman.tex` and the compiled `arXiv:2410.02032v2` PDF:
- **Conjecture 1** (`\label{conj:e-23-e}`, Section 8, p. 31, L2149–2151): matches `TARGET.md` L21 verbatim.
- **Definitions & Preliminaries:** Section 3 Definition 4 (p. 7, L460–462, $p_{\mathcal{L}}(n)$ defined for positive integers $n \ge 1$), Section 4 Definition 12 (p. 10, L664–669, `\label{def:lang-coding-seq}`), Section 5 Corollary 1 (p. 11, L753–763, `\label{cor:bi-complex}`), Section 7 Propositions 18–19 (pp. 28–29, L1945/L1974), Section 10 Farey substitutions $S_0(e,23,e), S_1(e,23,e)$ (p. 39, L2663–2667, Propositions 26–28 at L2684–2737).
- **Citation defects to fix:**
  1. `PROOF.md` L9 cites `Section 13 Appendix item 4 (L2889–2895)`. Because `\section{Hidden \R^2 maps}` (L2754) is inside `\iffalse...\fi` (L2749–2824), `\section{Appendix: Conjugates and Twins}` (L2837, p. 41) is **Section 12**, not Section 13 (also flagged in `notes/check-check-1.md` L10).
  2. `TARGET.md` L27 (Gate 1 receipt) writes `Section 6 sets up a partial proof strategy`, whereas `\label{sec:e-23-e}` is **Section 10** (p. 39).

---

## 2. Mathematical Findings (Required Fixes)

Independent exact symbolic verification of Sections 1–4 of `PROOF.md` confirms that the overall strategy (truncation to $(1,1)$-tailed double-Gauss coding sequences, Proposition 1, finite-state alternating non-neutral bispecial sequence with componentwise abelianization monotonicity, and Corollary 1) **works**, and `.venv/bin/python -u targets/garrity-2410.02032-conj1/notes/check-check-1.py` ran cleanly (exit code 0, `PASS`). However, `PROOF.md` has four substantive/critical mathematical errors and two minor rigor gaps:

### 2.1 Critical: False $(0,0)$-step words, matrix $M_{0,0}$, and gap formulas (`PROOF.md` L102, L126–128)
- `PROOF.md` L126 and L127 assert **$M_{0,0} = I_3$**. This is **false**: by L17–19, $\tau_{0,0}(1)=13$, $\tau_{0,0}(2)=23$, $\tau_{0,0}(3)=3$, so
  $$M_{0,0} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} \neq I_3.$$
- Consequently, `PROOF.md` L102 (`$w_1^- = 3^{t_m} 1^{j_{m+t_m}}$`), L126 (`$w_1^- := 3 \cdot 1^{j_{m+1}}$`), and L127 (`$w_1^- = 3^{t_m} 1^{j_{m+t_m}}$`) are **false** (for $j_{m+t_m} \ge 2$, the word $3^{t_m} 1^{j_{m+t_m}}$ is not even a factor of $\mathcal{L}^{(m)}$, because $\tau_{0,0}$ forces every $1$ to be followed by $3$). Under $t_m$ applications of $v \mapsto 3\tau_{0,0}(v)$, $v_0^- = 1^{j_{m+t_m}}$ maps to
  $$w_1^- = 3(13^{t_m})^{j_{m+t_m}}$$
  (at $t_m = 1$, $w_1^- = 3\tau_{0,0}(1^{j_{m+1}}) = 3(13)^{j_{m+1}}$).
- In L126, the abelianization gap formulas are correspondingly wrong:
  - $\ell(w_1^-) - \ell(w_1^+) = \ell(3(13)^{j_{m+1}}) - \ell(3) = (j_{m+1}, 0, j_{m+1})^T = M_{0,0}(j_{m+1},0,0)^T \ge 0$ (not $(j_{m+1},0,0)^T$).
  - $\ell(w_2^+) - \ell(w_1^-) = \bigl((0,0,1)^T + M_{0,0}\ell(v_1^+)\bigr) - \bigl((0,0,1)^T + M_{0,0}\ell(v_0^-)\bigr) = M_{0,0}(\ell(v_1^+) - \ell(v_0^-))$ (there is no extra `$+ (0,0,1)^T$`).
  - For all $(0,0)$-step tail gaps (L126–128), replace "$M_{0,0}=I_3$ preserves gaps identically" with the true fact: for any $\delta \ge 0$, $M_{0,0}\delta = (\delta_1, \delta_2, \delta_1+\delta_2+\delta_3)^T \ge 0$, which preserves $\delta \ge 0$, preserves $\delta \ge (0,0,1)^T$, and preserves $\delta_2 + \delta_3 \ge 1$ (since $(M_{0,0}\delta)_2 + (M_{0,0}\delta)_3 = \delta_1 + 2\delta_2 + \delta_3 \ge \delta_2 + \delta_3 \ge 1$).

### 2.2 Critical: Non-inductive transition invariant in Theorem 4(3)/(4) (`PROOF.md` L108, L111, L147) and omitted $r=0$ case (`PROOF.md` L108, L136)
- Theorem 4(3) (L108) allows $(E(w_r^-), E(w_{r+1}^+)) = (E_{32}^-, B^+)$ for $r \ge 1$ (and $E(w_1^+) \in \{A^+, B^+\}$ for $E_{33}^B$, $E(w_1^+) \in \{E_{32}^+, B^+\}$ for $E_{33}^C$). **This invariant is not closed under the inductive step:** under mode $k \ge 1$, $E_{32}^-$ lifts to $B^-$ and $B^+$ lifts to $B^+$, so $(E_{32}^-, B^+)$ would lift to $(B^-, B^+)$, which is **not** in Theorem 4(3)'s allowed list `{(E_{32}^-, A^+), (E_{32}^-, B^+), (A_1^-, B^+), (A_2^-, B^+), (B^-, A^+)}`! (L147 also cites `$v_{r+1}^+ \in E_{32}^+$`, although $(E_{32}^-, E_{32}^+)$ is absent from Theorem 4(3)–(4).)
- Exact symbolic reachability from the $(1,1)$ base case shows the true closed inductive invariant is strictly tighter and cleaner:
  - **$r \ge 1$ transitions:** ONLY $\{(E_{32}^-, A^+),\; (A_1^-, B^+),\; (A_2^-, B^+),\; (B^-, A^+)\}$ (remove $(E_{32}^-, B^+)$ entirely from Theorem 4(3)–(4) and remove L147).
  - **$r = 0$ transitions $(E(w_0^-), E(w_1^+))$:** ONLY $(E_{33}^A, E_{33}^+)$, $(E_{33}^B, A^+)$, $(E_{33}^C, E_{32}^+)$, and $(E_{32}^-, A^+)$ (when $j_m, k_m \ge 1$). Note that L108 currently omits specifying $E(w_1^+)$ when $j_m, k_m \ge 1$, even though L138 relies on it for $r=0$.
- In L136 (or L149–150), explicitly write the 1-line $r=0$ gap check when $t_{m+1}=0$ ($v_0^+ = \varepsilon$, $E_{33}^+$) and $j, k \ge 1$: $w_0^- = 1^j$ ($E_{32}^-$), $w_1^+ = 1^j 3$ ($A^+$), so $\ell(w_1^+) - \ell(w_0^-) = (0,0,1)^T$ ($\Delta_2+\Delta_3 = 1$).

### 2.3 Critical: Wrong image of $A_2^-$ under $(j \ge 1, k = 0)$ (`PROOF.md` L131)
- L131 states: `For $A_2^-$ ($E^+=\{2,3\}$), if $k = 0$ then $b = \varepsilon$ gives $A_2^-$`. Since L130 assumes $(j, k) \neq (0, 0)$, $k = 0$ means $j \ge 1, k = 0$, where $\alpha^R_{\varepsilon, j, 0}(3) = 1$. Hence $A_2^- = \{(1,3),(2,2)\}$ maps to $\{(1,1),(2,2)\} = A_1^-$ (not $A_2^-$), while $b = 1^j$ maps $2 \mapsto \varnothing$ (non-bispecial).

### 2.4 Substantive: Explicit extension-set errors in Lemma 2 proof & Lemma 3 $\mathcal{N}_0$ (`PROOF.md` L77, L80, L81, L92, L96)
- **L77:** claims intra-block `$21$ (iff $j \ge 1, k \ge 1$)` and `$23$ (iff $j = 0, k \ge 1$)`. False: $21$ occurs iff $j \ge 1$ ($\tau_{j,0}(2) = 21^j 3$ contains $21$, contradicting L79) and $23$ occurs iff $j = 0$ ($\tau_{0,0}(2) = 23$ contains $23$).
- **L80:** for $1 \le r < k$, claims $E(2^r) = \{(3,2),(2,2),(3,y)\}$. False: every run of $2$'s has length $k$ or $k+1 > r$, so $2^r$ cannot be simultaneously preceded by $3$ and followed by $y$; the actual set is $E(2^r) = \{(3,2),(2,2),(2,y)\}$ (still $2\times 2, m=0$).
- **L81:** for $1 \le r < j$ and $k = 0$, claims $E(1^r) = \{(1,1),(1,3),(3,1)\}$. False: $\tau_{j,0}(2) = 21^j 3$ contributes $(2,1)$, so $E(1^r) = \{(1,1),(1,3),(2,1),(3,1)\}$ for all $k \ge 0$ (still $3\times 2, m=0$).
- **L92 & L96:** L92 lists $\{(1,1),(1,3),(3,1)\}$ as one of "`4` sets in $3\times 2$", whereas it is $2\times 2$ and never occurs; the exact minimal closed neutral family $\mathcal{N}_0$ has **13** sets ($E_{33}^A$, the 9 listed $2\times 2$ sets, and the first 3 listed $3\times 2$ sets). In L96, make Lemma 3's proof self-contained (e.g., compact image table or direct check over the 13 sets in the 4 modes) rather than outsourcing it via `(verified exhaustively in verify.py)`.

### 2.5 Minor Rigor Polish (Fix Together)
- **Pairwise distinctness (`PROOF.md` L100, L161–163):** Explicitly note in Theorem 4 and the final Corollary 1 deduction that all non-neutral terms in $(w_r^+, w_r^-)_{r \ge 0}$ are pairwise distinct (age-$0$ words are $3$-free while lifted words contain $3$, and distinct $(a, v, b)$ produce distinct $a\tau(v)b$ by Proposition 1.1; neutral $w_0^+ = w_0^-$ contributes $m = 0$), so summing $m(w)$ over the set $\{w \in \mathcal{L}' : |w| \le N\}$ matches summing over the sequence with no double-counting.
- **Monotonicity of finite-prefix factor sets (`PROOF.md` L12, L16):** Note in one sentence that every letter of $\{1,2,3\}$ appears in the images of both $S_0$ and $S_1$, so $\bigcup_{c \in \mathcal{A}} \mathrm{Fac}((\sigma_0\circ\dots\circ\sigma_{N-1})(c))$ is non-decreasing in $N$ (justifying a single $N$ covering $\mathcal{L}(\mathbf{\sigma})_n$ and $\mathcal{L}(\mathbf{\sigma}') = \mathcal{L}(\tau_0,\tau_1,\dots)$).

---

## 3. Handoff
Returned to `@scout-11`, `@check-1`, and `@triage` for revision. Once `PROOF.md` and `TARGET.md` are patched and `@check-1` updates/re-runs `check-check-1.{md,py}` (including verifying the corrected $(0,0)$-step formula $w_1^- = 3(13^{t_m})^{j_{m+t_m}}$ and the tightened 4-transition invariant), ping `@audit-3` for re-audit.

---

## 4. Re-Audit #1 (`audit-3`, 2026-11-27, after `#807` patches)

- **Verdict:** **FAIL** (almost completely clean — all 52 cells of the new Lemma 3 table in L105–115 verified `0` mismatches, `TARGET.md` L27 & `PROOF.md` L9 citations fixed, Lemma 2 L77/L80/L81 fixed, Theorem 4 closed 4-transition invariant $\mathcal{T}_{\ge 1}$ + distinctness/monotonicity verified — only **4** remaining localized formula/label typos in `PROOF.md`, plus awaiting `@check-1`'s updated `check-check-1.{md,py}`):
  1. **`PROOF.md` L122, L148, L150 ($(0,0)$-step exponent on leading $3$):** Iterating $f(v) := 3\tau_{0,0}(v)$ $t_m$ times sends $v \mapsto 3^{t_m}\tau_{0,0}^{t_m}(v)$ (since $\tau_{0,0}(3)=3$ and $\tau_{0,0}(1)=13$), so $1^j \mapsto \mathbf{3^{t_m}(13^{t_m})^j}$, **not** $3(13^{t_m})^j$ (note `#777` had the same missing exponent on the leading $3$; e.g., $f^2(1) = 3\tau_{0,0}(313) = 33133 = 3^2(13^2)^1$). Fix L122 (`$w_1^- = 3^{t_m}(13^{t_m})^{j_{m+t_m}}$`, and change the parenthetical to `where $\tau_{0,0}^{t_m}(1)=13^{t_m}$, $\tau_{0,0}(3)=3$, so $t_m$ iterations of $v \mapsto 3\tau_{0,0}(v)$ send $v \mapsto 3^{t_m}\tau_{0,0}^{t_m}(v)$`), L148 (`$3\tau_{0,0}(3^t(13^t)^j) = 3^{t+1}(13^{t+1})^j$`), and L150 (`$w_1^- = 3^{t_m}(13^{t_m})^{j_{m+t_m}}$`).
  2. **`PROOF.md` L158 (wrong neutral label):** Under $j \ge 1, k = 0$, the neutral image $1^j 3\tau(v_r^+) 1^j$ of $E_{33}^+$ is **$N_{10} = \{(1,1),(1,3),(2,1),(3,1)\}$**, not $N_{12}$.
  3. **`PROOF.md` L176 (missing $\tau_{0,k}(3^{t_{m+1}})$ factor):** When $E(v_0^\pm) = E_{33}^A$ ($v_1^+ = 3^{t_{m+1}}$) and $j = 0, k \ge 1$, the lifted word is **$w_1^+ = 3\tau_{0,k}(3^{t_{m+1}})$**, not $w_1^+ = 3$.
  4. **`PROOF.md` L182 (wrong neutral labels):** Under $k \ge 1$, the neutral image $2^k 1^j 3\tau_{j,k}(3^{t_{m+1}})$ of $E_{33}^C$ is **$N_6 = \{(2,1),(3,1),(3,2)\}$** for both $j \ge 1$ and $j = 0$ (not `$N_2$` / `$N_4$`).

Once these 4 lines in `PROOF.md` are patched and `@check-1` updates/re-runs `notes/check-check-1.{md,py}`, ping `@audit-3` for final PASS.

---

## 5. Re-Audit #2 (`audit-3`, 2026-11-27, after `#840` patches) — **PASS**

Verified every single item from §1–§4 against the updated `TARGET.md` (29 lines) and `PROOF.md` (191 lines):
- **Primary Source & Citations:** `TARGET.md` L27 (`Section 10`) and `PROOF.md` L9 (`Section 12 Appendix item 4`, L2889–2895) match both `Final_Revision-Garrity-Osterman.tex` and the compiled 44-page `arXiv:2410.02032v2` PDF (*Combinatorics and Number Theory* 15 (2026), 239–292, DOI `10.2140/cnt.2026.15.239`).
- **Mathematical Verification (Line-by-Line + Exhaustive Independent Symbolic Check):**
  - §1 (L9–20): Monotonicity of finite factor sets $\bigcup_{c\in\mathcal{A}} \mathrm{Fac}((\sigma_0\circ\dots\circ\sigma_{N-1})(c))$ justified via surjectivity of $S_0, S_1$ onto $\{1,2,3\}$; reduction to $(1,1)$-tailed double-Gauss coding sequences $(\tau_m)$ with $M_{1,1}^2 > 0$ and extendability is exact.
  - §2 (L26–59, Proposition 1): Unique desubstitution, left/right special $a, b$ forms, and every entry of $\alpha^L_{a,k}, \alpha^R_{b,j,k}$ verified exhaustively for $0 \le j, k \le 3$.
  - §3 (L65–81, Lemma 2): L77 ($21$ iff $j \ge 1$, $23$ iff $j = 0$), L80 ($E(2^r) = \{(3,2),(2,2),(2,y)\}$ for $1 \le r < k$), and L81 ($E(1^r) = \{(1,1),(1,3),(2,1),(3,1)\}$ for $1 \le r < j$, all $k \ge 0$) all verified exact.
  - §4 (L87–116, Lemma 3): Exact 13-element neutral collection $\mathcal{N}_0 = \{N_0,\dots,N_{12}\}$ contains all age-$0$ neutral sets; all $13 \times 4 = 52$ cells of the self-contained closure table (L105–115) verified independently with `0` mismatches.
  - §4 (L118–184, Theorem 4):
    - $(0,0)$-step (L122, L146–151): Correct matrix $M_{0,0} = \left(\begin{smallmatrix}1&0&0\\0&1&0\\1&1&1\end{smallmatrix}\right)$, correct iterated word $w_1^- = 3^{t_m}(13^{t_m})^{j_{m+t_m}}$ (verified for $1 \le j, t \le 4$), and exact gap calculations preserved by $M_{0,0}$.
    - Closed inductive invariant (L128–132, L153–182): Tightened 4-transition set $\mathcal{T}_{\ge 1} = \{(E_{32}^-,A^+),(A_1^-,B^+),(A_2^-,B^+),(B^-,A^+)\}$ and exact $r=0$ heads $\{(E_{33}^A,E_{33}^+),(E_{33}^B,A^+),(E_{33}^C,E_{32}^+),(E_{32}^-,A^+)\}$ verified closed under all 4 modes $(j>0,k>0) \in \{0,1\}^2$, with $A_2^- \mapsto A_1^-$ under $(j\ge 1, k=0)$ (L154), $N_{10}$ (L158), $w_1^+ = 3\tau_{0,k}(3^{t_{m+1}})$ (L176), and $N_6$ (L182) all exact.
    - Pairwise distinctness of non-neutral terms (L118–120, L134, L187) established via age-$0$ vs $3$-containing separation and Proposition 1.1 unique desubstitution.
  - §4 (L186–191, Proof of Conjecture 1): Cancellation of $(w_r^+, w_r^-)$ yields $\sum_{|w| \le N} m(w) \le 1$, and Corollary 1 (`cor:bi-complex`, Section 5, p. 11) with $|\mathcal{L}'_1| = 3$ gives $p_{\mathcal{L}(\mathbf{\sigma})}(n) \le p_{\mathcal{L}'}(n) \le 3n$ for all $n \ge 1$ (and for all 5 conjugates and 6 twins).
- **Independent Verifier Re-Run:**
  - Command: `.venv/bin/python -u targets/garrity-2410.02032-conj1/notes/check-check-1.py`
  - Result: exit code `0`, raw `PASS` (pure integer/tuple/set/dict arithmetic, zero floats).
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).
