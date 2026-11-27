# Blind Audit Report: `ciobanu-2604.22375-conj1`

- **Auditor:** `audit-3` (blind Pro audit; author `notes/` and `verify.py` not read)
- **Audited at (UTC):** `2026-11-27T10:05Z` (initial FAIL) / `2026-11-27T10:11Z` (re-audit **PASS**)
- **Verdict:** **PASS** (after `#588` / `#594` section-numbering & terminology patches; Charter label: `"written proof, internally audited"`)

---

## 1. Strict Isolation Record

Inspected ONLY:
- Primary source: `arXiv:2604.22375v1` live metadata (`2026-04-24`, comment: *"Full version of the conference paper accepted to DLT 2026"*), extracted LaTeX source `tools/.arxiv_cache/eprint/2604.22375v1/Arxiv_version.tex` (lines 1–562), and compiled PDF `https://arxiv.org/pdf/2604.22375v1` (pp. 1–17). Also checked Crossref for published version: *Developments in Language Theory (DLT 2026)*, LNCS, Springer 2026 (`DOI: 10.1007/978-3-032-28404-4_8`, paywalled; `arXiv:2604.22375v1` is the full version).
- `targets/ciobanu-2604.22375-conj1/TARGET.md`
- `targets/ciobanu-2604.22375-conj1/PROOF.md`
- `targets/ciobanu-2604.22375-conj1/notes/check-check-3.md` and `targets/ciobanu-2604.22375-conj1/notes/check-check-3.py`

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Fidelity Audit (**FAIL — Section Numbering Off-by-One**)

1. **Verbatim conjecture & definitions — PASS:**
   - The conjecture statement in `TARGET.md` L15–17 matches `Arxiv_version.tex` L370–372 (`\begin{conj}\label{conjecture1}`) verbatim, and the conjecture number is indeed **Conjecture 1** (p. 10 of compiled PDF).
   - The proposition numbers cited in `PROOF.md` match the compiled `llncs` PDF verbatim: **Proposition 3** (`\label{prop:CongsVPLs}`, p. 5) and **Proposition 4** (`\label{prop:recsetsareficosets}`, p. 6).
   - In `Arxiv_version.tex` L50, L70–71, and L204–209, all groups/generating sets in the paper are explicitly assumed finitely generated with finite $\Sigma = X \cup X^{-1}$ and canonical epimorphism $\pi : \Sigma^\star \to G$.

2. **BLOCKING CITATION ERRORS (Section numbers off by +1):**
   Because the Introduction in `Arxiv_version.tex` (L50–62) has **no** `\section` command, the compiled PDF numbers sections as:
   - `1 Preliminaries` (L68, p. 2; `1.1 VPLs and their closure properties`, `1.2 Congruences on VPLs`, `1.3 Languages in Groups`)
   - `2 The Word Problem` (L242, p. 7)
   - `3 Types of VPL sets in groups` (L305, p. 9)
   - **`3.1 VPL^\forall sets in groups`** (L366, p. 10 — where **Conjecture 1** appears; also explicitly cited as *"Section 3.1"* on p. 2 and p. 13 of the PDF!)
   - `4 Word Equations with Language Constraints` (L474, p. 12)
   - `5 Conclusions` (L529, p. 14)

   Accordingly, the following citations are wrong and must be corrected:
   - `TARGET.md` L2: `Section 4.1` $\to$ **`Section 3.1`**
   - `PROOF.md` L1: `Section 4.1` $\to$ **`Section 3.1`**
   - `PROOF.md` L15: `Section 2` (for VPA conventions) $\to$ **`Section 1.1`** (p. 2–3; Section 2 is *The Word Problem*)
   - `notes/check-check-3.md` L5, L11, L15 and `notes/check-check-3.py` L2: `Section 4.1` $\to$ **`Section 3.1`**, `Section 2` $\to$ **`Section 1.1` / `Section 1`** (and L11 `\section{Types of \vpl ~sets in groups}` is Section 3, not Section 4).

3. **Minor terminology / convention polish (recommended to fix in the same pass):**
   - `PROOF.md` L37 calls $\mathit{MC}(\Sigma)$ *"the matched-return (non-positive-suffix) sublanguage"*, whereas `Arxiv_version.tex` Definition 4(ii) (p. 5) calls $\mathit{MC}(\Sigma)$ the set of **matched-call** words (and $\mathit{MR}(\Sigma)$ matched-response words). Change *"matched-return"* $\to$ *"matched-call"*.
   - `PROOF.md` L15 writes *"$\bot \notin \Gamma$"*, whereas `Arxiv_version.tex` Section 1.1 (p. 3) uses the convention *"$\bot \in \Gamma$"* cannot be pushed (so pushable stack symbols lie in $\Gamma \setminus \{\bot\}$). Aligning L15 and L59 avoids an apparent convention mismatch.

---

## 3. Line-by-Line Mathematical Audit (**PASS — Complete and Airtight**)

Every mathematical step in `PROOF.md` L11–89 was audited adversarially (including edge cases $G = \{1\}$, $\Sigma = \emptyset$, $Q_0 = \emptyset$, $S = \emptyset$, $S = G$, nondeterministic VPAs, non-normal stabilizers $H$, and symmetric partitions such as $F_2$ and $\mathbb{Z}$):

1. **Inclusion $\mathbf{REG}^\forall(G) \subseteq \mathbf{VPL}^\forall(G)$ (L11) — PASS:** Immediate via $\Sigma_i = \Sigma$, $\Sigma_c = \Sigma_r = \emptyset$ (Remark 1 of `arXiv:2604.22375v1`).
2. **Case 1: $\Sigma_r = \emptyset$ (L25–31) — PASS:** With no returns, call transitions neither depend on nor affect future transitions, and acceptance depends only on final state (Footnote 3 of `arXiv:2604.22375v1`). Projecting pushed stack symbols yields an NFA $M'$ accepting the exact same language $L = \pi^{-1}(S)$. For $R(u_1) = R(u_2)$, surjectivity of $\pi$ yields $\pi(u_1)\pi(u_2)^{-1} g \in S \iff g \in S$ for all $g \in G$, so $\pi(u_1)\pi(u_2)^{-1} \in H = \mathrm{Stab}_L(S)$, i.e., $H\pi(u_1) = H\pi(u_2)$, bounding $[G : H] = |H \backslash G| \le 2^{|Q|} < \infty$.
3. **Case 2, Lemma 1 (L41–51) — PASS:** $\varepsilon \in \mathit{MC}(\Sigma)$ and suffix decomposition $s = s_u v$ or $s$ suffix of $v$ shows $\mathit{MC}(\Sigma)$ is a submonoid of $\Sigma^\star$, so $M_{\mathrm{mc}} = \pi(\mathit{MC}(\Sigma))$ is a submonoid of $G$. Checking suffixes of lengths $\le 2$ verifies $\Sigma_r \cup \Sigma_i \cup (\Sigma_c \Sigma_r) \subseteq \mathit{MC}(\Sigma)$; fixing $y_0 \in \Sigma_r \neq \emptyset$ gives $\pi(x) = \pi(x y_0)\pi(y_0)^{-1} \in \langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}}$ for every $x \in \Sigma_c$, hence $\langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}} = G$.
4. **Case 2, Lemma 2 (L53–65) — PASS:**
   - Part 1: Taking $j = \max\{0 \le k < m : h_k = 0\}$ when $h_m > 0$ forces $a_{j+1} \in \Sigma_c$ ($h_{j+1} - h_j = 1$) and $h_{k-1} \ge 1$ for $j+2 \le k \le m$ (so pops always remove a non-$\bot$ symbol and decrement height by $1$), yielding $0 < h_m = \#_c(s) - \#_r(s)$ on the suffix $s = a_{j+1}\cdots a_m$, contradicting $u \in \mathit{MC}(\Sigma)$.
   - Part 2: Since VPAs have no $\varepsilon$-transitions and every run on $u \in \mathit{MC}(\Sigma)$ ends with empty stack $\bot$, $u v \in L \iff \exists q \in R(u)$ with an accepting run on $v$ from $(q, \bot)$ (including $R(u) = \emptyset$), so $R(u_1) = R(u_2) \implies u_1 \sim_0 u_2$ and $|\mathit{MC}(\Sigma)/{\sim_0}| \le 2^{|Q|} < \infty$.
   - Part 3: Identical surjectivity argument yields $u_1 \sim_0 u_2 \implies \pi(u_1)\pi(u_2)^{-1} \in H \implies H\pi(u_1) = H\pi(u_2)$.
5. **Case 2, Lemma 3 (L67–77) — PASS:** $\Omega := \{Hm : m \in M_{\mathrm{mc}}\} \subseteq H \backslash G$ contains $H = H \cdot 1_G$ and satisfies $1 \le |\Omega| \le |\mathit{MC}(\Sigma)/{\sim_0}| \le 2^{|Q|} < \infty$. For each $m \in M_{\mathrm{mc}}$, the bijection $\rho_m(Hx) = H(xm)$ satisfies $\rho_m(\Omega) \subseteq \Omega$ by Lemma 1(1); finiteness of $\Omega$ and injectivity of $\rho_m$ force $\rho_m(\Omega) = \Omega$ and $\rho_{m^{-1}}(\Omega) = \Omega$. Thus the subgroup $K := \{g \in G : \rho_g(\Omega) = \Omega\} \le G$ contains $M_{\mathrm{mc}}$, so $K = G$ by Lemma 1(2). Hence $Hg = \rho_g(H) \in \Omega$ for all $g \in G$, giving $\Omega = H \backslash G$ and $[G : H] = |\Omega| \le 2^{|Q|} < \infty$.
6. **Conclusion (L81–89) — PASS:** The normal core $N = \bigcap_{g \in G} g H g^{-1}$ is the kernel of the left-multiplication action on $G/H$, so $N \trianglelefteq G$ with $[G : N] \le [G : H]! < \infty$ and $N \le H$. Hence $N s \subseteq S$ for all $s \in S$, so $S = \bigcup_{s \in S} N s$ is a finite union of $N$-cosets (including the empty union when $S = \emptyset$), and $\pi^{-1}(S) = (\varphi \circ \pi)^{-1}(\varphi(S))$ is accepted by the explicit finite DFA on $G/N$ (for $\Sigma$, and in fact for every finite generating set of $G$).

---

## 4. Independent Mechanical Verification (**PASS**)

Re-executed `.venv/bin/python targets/ciobanu-2604.22375-conj1/notes/check-check-3.py`:
- Exit code `0`, raw output:
  ```text
  [1/3] Checking Lemma 1 (MC submonoid & generation) & Lemma 2(1) (empty stack) on random VPAs...
  [2/3] Checking Case 1, Case 2 (Lemma 2, Lemma 3, normal core N) on finite & infinite groups...
  [3/3] Checking negative sanity on G = Z, S = {0} (infinite ~_0 index for symmetric partition)...
  PASS
  ```

---

## 5. Action Required for Re-Audit

1. `@scout-12`: Fix section numbers in `TARGET.md` L2 (`Section 4.1` $\to$ `Section 3.1`) and `PROOF.md` L1 (`Section 4.1` $\to$ `Section 3.1`), L15 (`Section 2` $\to$ `Section 1.1`), plus minor terminology polish in `PROOF.md` L37 (`matched-return` $\to$ `matched-call`) and L15/L59 ($\bot \in \Gamma$ convention matching Section 1.1).
2. `@check-3`: Fix `Section 4.1` $\to$ `Section 3.1` and `Section 2` $\to$ `Section 1.1` in `notes/check-check-3.md` (L5, L11, L15) and `notes/check-check-3.py` (L2).
3. Re-ping `@audit-3` once patched for immediate re-audit PASS.

---

## 6. Re-Audit After Author & Checker Patch (`2026-11-27T10:11Z`) — **PASS**

Re-inspected patched `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, and `notes/check-check-3.py` after `#588` and `#594`:
1. All section references now match the compiled `arXiv:2604.22375v1` PDF verbatim (`Section 3.1` for Conjecture 1 in `TARGET.md` L2, `PROOF.md` L1, `check-check-3.md` L5/L11, `check-check-3.py` L2; `Section 1.1` for VPA conventions in `PROOF.md` L15 and `check-check-3.md` L15).
2. `PROOF.md` L37 now uses *"matched-call"* (matching Definition 4(ii)) and L15/L59 align with the paper's $\bot \in \Gamma$ / $\Gamma \setminus \{\bot\}$ stack convention.
3. Re-executed `.venv/bin/python targets/ciobanu-2604.22375-conj1/notes/check-check-3.py`: exit code `0`, raw output `PASS`.

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Handed off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`).

---

## 7. Independent Lean 4 Statement-Fidelity Audit (Batch C, `@audit-1`, `2026-11-27T12:04Z`) — **PASS**

- **Module:** `lean/OpenMath/Ciobanu260422375Conj1.lean` (imported in `lean/OpenMath.lean` L21; `.olean` present).
- **Statement fidelity vs primary source (`tools/.arxiv_cache/eprint/2604.22375v1/Arxiv_version.tex`, Sections 1.1, 1.3, & 3.1 Conjecture 1) & `TARGET.md`:**
  - `DetFA` & `IsRegular` (L66–88): standard finite-state DFA acceptance (`Fintype Q`, universe-polymorphic in `Alph`).
  - `VPA` & `IsVPL` (L91–164): exact nondeterministic VPA matching Section 1.1 (`Arxiv_version.tex` L78–101, Footnote 3) — finite `Q` and `Γ` (modeling `Γ \ {⊥}` with `[]` representing bottom-of-stack `⊥`), no `ε`-transitions, call pushes `γ : Γ`, internal leaves stack unchanged, return pops top symbol or preserves `[]` (`⊥`), acceptance by final state `qf ∈ M.accept` with arbitrary final stack `σ`, quantified over all partitions `kind : Alph → LetterKind`.
  - `IsREGForall`, `IsVPLForall`, & `IsRecognisable` (L167–177): exact match to Section 1.3 (Def. L207–209, Prop. 4 L215 — left-$N$-invariance under a finite-index normal subgroup `N ⊴ G`, hence a finite union of `N`-cosets).
  - Main theorems (L694–760): `ciobanu_turaev_conjecture_1` (`IsVPLForall gen S ↔ IsREGForall gen S`) and `vplForall_iff_recognisable` (`IsVPLForall gen S ↔ IsRecognisable S`) hold for every group `G` and every surjective monoid presentation `evalWord gen : List Alph → G` (strictly more general than finite `Alph`, with zero hidden hypotheses), and `ciobanu_turaev_conjecture_1_symGen` (L757–760) explicitly specializes to `Σ = X ⊔ X` (`symGen f : X ⊕ X → G`, `inl x ↦ f x`, `inr x ↦ (f x)⁻¹`) matching `Arxiv_version.tex` L70 & L204 (`X ∪ X⁻¹`).
- **Hygiene & kernel check:** Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `partial`, `opaque`, or `set_option`.
- **Verification command:** `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Ciobanu260422375Conj1.lean` -> exit code `0`, 0 warnings.
- **Axioms (`#print axioms`):** `vpa_empty_stack_on_mc`, `vplForall_finiteIndex_stabL`, `ciobanu_turaev_conjecture_1`, `vplForall_iff_recognisable`, `ciobanu_turaev_conjecture_1_symGen` all depend strictly on `[propext, Classical.choice, Quot.sound]`.
- **Charter label upgrade:** **PASS** — eligible for `"machine-checked proof in Lean 4"`.
