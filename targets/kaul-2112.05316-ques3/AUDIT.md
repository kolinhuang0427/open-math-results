# Blind Audit Report: `targets/kaul-2112.05316-ques3/` (`@audit-2`)

**Verdict: PASS (re-audit after `#745`/`#760` patches)**

*(Initial audit failed solely on subsection citation numbering and one omitted zero-contribution subcase in Lemma 2 Case 3; both items have been patched and verified below — see §5.)*

The refutation proof for all $p \ge 4$ (and $d_G(v) = p \ge 4$) at $m = p+1$ via $G_0^{(p)} = K_{p-2} \vee K_{2,p}$ tessellated along its $2p$ $p$-cliques is mathematically sound and completely self-contained. Two localized defects must be patched before Gate 3 / reporting.

---

## 1. Primary Source & Version Verification

- **Live arXiv query:** `arXiv:2112.05316v2` (`2023-08-14`, Hemanshu Kaul, Michael Maxfield, Jeffrey A. Mudrock, Seth Thomason, *"The DP Color Function of Clique-Gluings of Graphs"*, published in *Enumerative Combinatorics and Applications* 4:2 (2024), Article S2R11) is the sole latest version on arXiv; web check confirms the ECA 2024 publication has the same scope ($p=2$ yes, $p=3$ no, $p \ge 4$ open).
- **Verbatim TeX verification (`tools/.arxiv_cache/eprint/2112.05316/paper.tex`, original gzipped name `Gluings_Paper.tex`):**
  - Preamble (L52–60): `\newtheorem{thm}{Theorem}`, `\newtheorem{ques}[thm]{Question}` (global shared `[thm]` counter): Theorem 1 (`thm: evengirth`, L167), **Question 2** (`ques: classify`, L173–177), **Question 3** (`ques: easier`, L181–183).
  - Exact subsection structure of Section 1 (`\section{Introduction}`, L124):
    - **Section 1.1** (L128): *List Coloring and DP-Coloring*
    - **Section 1.2** (L151): *Counting Proper Colorings and List Colorings*
    - **Section 1.3** (L161): *The DP Color Function and Motivating Question* — contains **Question 2** (`\label{ques: classify}`, L173–177) and **Question 3** (`\label{ques: easier}`, L181–183).
    - **Section 1.4** (L187): *Outline of the Paper and a Conjecture* — contains the open-cases statement at **L199** (*"While the answers to Questions~\ref{ques: classify} and~\ref{ques: easier} are unknown for each $p \geq 4$ and $d_G(v) \geq 4$ respectively, our result in Section~\ref{triangle} makes us suspect both questions have a negative answer for each of these values."*).
  - Exact wording of Question 2, Question 3, L199, and all definitions in `TARGET.md` L13–31 matches `paper.tex` verbatim.

---

## 2. Blocking Defects (Must Fix)

1. **Wrong subsection numbering across `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-2.md`:**
   - Question 2 (`ques: classify`) and Question 3 (`ques: easier`) are in **Section 1.3** (not 1.2), and line 199 is in **Section 1.4** (not 1.3).
   - Fixes required:
     - `TARGET.md` L1: `Section 1.2–1.3` $\to$ `Section 1.3–1.4` (and add the missing opening `---` YAML frontmatter delimiter on L1 so `tools/gen_index.py` parses frontmatter cleanly).
     - `TARGET.md` L24: `Section 1.1–1.2, lines 132–179` $\to$ `Section 1.1–1.3, lines 132–179`.
     - `COUNTEREXAMPLE.md` L3: `Section 1.3 (paper.tex, line 199)` $\to$ `Section 1.4 (paper.tex, line 199)`.
     - `notes/check-check-2.md` L3: `Section 1.1–1.3, L52–60, L126–205` $\to$ `Section 1.1–1.4, L52–60, L126–205`.
2. **Omitted subcase in Lemma 2 Case 3 (`COUNTEREXAMPLE.md` L48–52):**
   - For $\{1, 2\} \subseteq S$ (say $S = \{1, 2, r\}$), the three bullet points cover only $3 + 2 + 2 = 7$ of the $9$ ordered pairs $(c(v_1), c(v_2)) \in S^2$:
     - $c(v_1) \notin \{1, 2\}$ ($3$ pairs),
     - $c(v_1) = c(v_2) \in \{1, 2\}$ ($2$ pairs),
     - $\{c(v_1), c(v_2)\} = \{1, 2\}$ ($2$ pairs).
   - The remaining $2$ pairs — **$c(v_1) \in \{1, 2\}$ and $c(v_2) \notin \{1, 2\}$** (i.e., $c(v_2) = r$) — are omitted. Although they contribute zero net change (since $|S \setminus \{\tau(c(v_1)), r\}| = 1 = |S \setminus \{c(v_1), r\}|$), they must be explicitly included so the 9-pair case split is exhaustive.

---

## 3. Mathematical Audit of `COUNTEREXAMPLE.md`

- **Reduction from Questions 2 & 3 (L5–14):** $G_0^{(p)} = K_{p-2} \vee K_{2,p}$ is a finite, simple, connected graph on $2p$ vertices. Attaching simplicial degree-$p$ vertices $d_1, \dots, d_{2p}$ to the $2p$ $p$-cliques $K_1, \dots, K_{2p}$ gives $G_k \in G_{k-1} \oplus_p K_{p+1}$ with $G_k - \{d_k\} = G_{k-1}$. At $m = p+1 \ge p$, $(p+1-d_{G_k}(d_k)) = 1$ and $P_{DP}(K_{p+1}, p+1)/\prod_{i=0}^{p-1}(p+1-i) = (p+1)!/(p+1)! = 1$, so $P_{DP}(G_k, p+1) > P_{DP}(G_{k-1}, p+1)$ simultaneously refutes both Question 3 (`d_G(v) = p`) and Question 2 (`p`, `n = 2`, `m = p+1`). Also independently verified the parenthetical remark on L15: $P(K_2 \vee K_{2,3}, 5) = 600$ and twisting the single edge $v_1 u_3$ by the derangement $(1\,2)(3\,4\,5)$ gives exactly $570$ colorings ($P_{DP}(K_2 \vee K_{2,3}, 5) \le 570 < 600$). **PASS.**
- **Lemma 1 (L21–25):** Direct greedy matching lower bound $P_{DP}(K_{p+1}, p+1) = (p+1)!$ and triangle-freeness of $K_{2,p}$ classifying all $2p$ copies of $K_p$ in $G_0^{(p)}$ as $W \cup \{v_i, u_j\}$ are airtight. **PASS.**
- **Lemma 2 (L27–56):** Conditioning on the $(p-2)$-clique $W$ leaves a 3-subset $S \subseteq [p+1]$ with $(p-2)!$ ordered $W$-colorings each; $N_{\mathrm{canon}}(S) = 3 \cdot 2^p + 6$ and $P(G_0^{(p)}, p+1) = \frac{(p+1)!}{6}(3 \cdot 2^p + 6)$. Case 1 ($S \cap \{1, 2\} = \emptyset$: $\Delta = 0$) and Case 2 ($|S \cap \{1, 2\}| = 1$: $(p-1)(p-2)$ subsets, $\Delta = +2$) are exact (including $c(v_1) = c(v_2) = a$ where $S \setminus \{\tau(a), a\} = S \setminus \{a\}$). Case 3 ($\{1, 2\} \subseteq S$: $p-1$ subsets, $\Delta = 2 - 2^p$) gives the exact sum $-(p-1)!(2^p - 2p + 2) < 0$ for all $p \ge 3$, pending addition of the omitted 2-pair zero-change subcase noted in §2 above. **FAIL only for omitted subcase.**
- **Lemma 3 (L58–63):** Precoloring extension from any $K_k = W \cup \{v_i, u_j\}$ to $G_0^{(p)}$ under any $(p+1)$-fold cover $\mathcal{H}$: $v_{3-i}$ has $p-1$ neighbors in $K_k$ ($\ge 2$ choices), then each $u_{j'}$ ($j' \neq j$) has $p$ neighbors in $K_k \cup \{v_{3-i}\}$ ($\ge 1$ choice) and $\{u_{j'}\}$ is independent. Airtight for all $p \ge 3$. **PASS.**
- **Main Theorem (L65–90):**
  - Completing partial matchings to full cover cannot increase $|\mathcal{C}^*|$: airtight.
  - Disjointness of $f(I)$ and $|f(I)| \ge 1$ (since $\{d_1, \dots, d_{2p}\}$ is independent and each $d_k$ has $p$ neighbors in $G_0^{(p)}$): airtight.
  - Case 1 ($\mathcal{H}_0$ canonical): $|\mathcal{C}^*| \ge |\mathcal{C}_0| = P(G_0^{(p)}, p+1) > P_{DP}(G_0^{(p)}, p+1)$, contradiction. Airtight.
  - Case 2 ($\mathcal{H}_0$ non-canonical): Fixing universal vertex $w_1 \in W$ gives a non-identity edge $yz$ ($y, z \neq w_1$); every edge of $G_0^{(p)}$ lies in some $K_k$ containing $w_1$; $\mathcal{H}_{K_k}$ has no canonical labeling (direct self-contained proof); relabeling via full edges to $d_k$ gives an edge $ab \in E(K_k)$ with $(a, c_0)'(b, c_0)' \notin E(H^*)$; greedy completion over the $p-2$ remaining vertices of $K_k$ leaves $\ge 2$ choices at each step and produces an $\mathcal{H}_{K_k}$-coloring $A$ using $\le p-1$ distinct primed indices, leaving $\ge 2$ choices for $d_k$; Lemma 3 extends $A$ to $D \in \mathcal{C}_0$ with $|f(D)| \ge 2$, yielding $P_{DP}(G^*, p+1) \ge |\mathcal{C}_0| + 1 \ge P_{DP}(G_0^{(p)}, p+1) + 1$, contradiction! Completely self-contained and airtight. **PASS.**

---

## 4. Independent Checker & Gate 2 Verification

- Re-ran `.venv/bin/python -u targets/kaul-2112.05316-ques3/notes/check-check-2.py`: `exit 0`, AST `FLOAT_CONSTANTS: 0`, output `PASS`.
- Independently enumerated full $G^* = G_{2p}$ coloring extensions for the $(1\,2)$-twisted cover on $v_1 u_p$ (all other edges canonical):
  - $p = 3$: $|\mathcal{C}_0| = 112 < 120$, $|\mathcal{C}^*| = 124$, $\min |f(I)| = 1$, $\max |f(I)| = 2$.
  - $p = 4$: $|\mathcal{C}_0| = 1020 < 1080$, $|\mathcal{C}^*| = 1068$, $\min |f(I)| = 1$, $\max |f(I)| = 2$.
- Gate 2 novelty receipts verified (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`): all 3 PASS.

---

## 5. Re-Audit Verification (`2026-11-27T10:30Z`) — **PASS**

Verified all patches from `#760` (`@scout-9`) and `@check-2`:
1. **`TARGET.md` L1, L2, L25:** Added opening `---` YAML frontmatter delimiter; corrected subsection citations to `Section 1.3–1.4` (L2) and `Section 1.1–1.3` (L25). Matches `paper.tex` (`Gluings_Paper.tex`) in `arXiv:2112.05316v2` verbatim.
2. **`COUNTEREXAMPLE.md` L3, L48–53:**
   - L3 corrected to `Section 1.4 (paper.tex, line 199)`.
   - L48–53 (Lemma 2 Case 3) now explicitly enumerates all $9$ ordered pairs $(c(v_1), c(v_2)) \in S^2$ with $S = \{1, 2, s_0\}$: $c(v_1) = s_0$ ($3$ pairs, $0$), $c(v_1) \in \{1, 2\}, c(v_2) = s_0$ ($2$ pairs, $|S \setminus \{c(v_1), s_0\}| = 1 = |S \setminus \{\tau(c(v_1)), s_0\}|$, $0$), $c(v_1) = c(v_2) \in \{1, 2\}$ ($2$ pairs, $-2^p$), and $\{c(v_1), c(v_2)\} = \{1, 2\}$ ($2$ pairs, $+2$), yielding $\Delta(S) = 2 - 2^p$. Completely exhaustive.
3. **`notes/check-check-2.md` L3:** Updated to `Section 1.1–1.4` with exact §1.3 / §1.4 attribution and 9-pair check.
4. **Independent checker (`notes/check-check-2.py`):** Exact integer arithmetic (`FLOAT_CONSTANTS: 0`), verified `exit 0` / `PASS`.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

---

## 6. Independent Lean 4 Statement-Fidelity Audit (`2026-11-27T16:26Z`) — **PASS**

- **Auditor:** `audit-3` (`auto`)
- **Lean Module:** `lean/OpenMath/Kaul211205316Ques3.lean` (imported on L30 of `lean/OpenMath.lean`)
- **Charter Label:** `machine-checked counterexample in Lean 4`
- **Primary-Source Fidelity (`arXiv:2112.05316v2`, `paper.tex` L126–199):**
  - `FoldCover G m` (`clique_part`, `adj_subset`, `matching_right` + derived `matching_left`), `IsIndepColoring` (independent set in $H$ of size $|V(G)|$, bijected to functional $\mathcal{H}$-colorings via `indepColoringEquiv`), `dpColorCount`, and `dpColorFun G m` (`sInf` over ALL $m$-fold covers, with `exists_min_full_foldCover` proving a full cover achieves the minimum) match Section 1.1–1.3 (`paper.tex` L132–143, L163) verbatim.
  - `IsSimplicial G v`, `vertexDeg G v`, and `IsCliqueGluing2 p G₁ G₂ G` ($V(G) = S_1 \cup S_2$, $|S_1 \cap S_2| = p$, $G[S_1 \cap S_2]$ complete, no cross-edges between $S_1 \setminus S_2$ and $S_2 \setminus S_1$, $G[S_1] \simeq_g G_1$, $G[S_2] \simeq_g G_2$) match `paper.tex` L155 & L179 verbatim.
  - Witness graphs `Gk p k` ($0 \le k \le 2p$, $p \ge 3$) are nonempty, finite, simple, and connected (universal vertex `Sum.inl ⟨0, _⟩`), with `m = p + 1 ≥ p ≥ 3 > 0`.
  - `kaul_question_3_false` directly refutes Question 3 (`ques: easier`) for every $d_G(v) = p \ge 3$ (hence every $p \ge 4$): $(m - d_G(v)) P_{DP}(G - \{v\}, m) < P_{DP}(G, m)$.
  - `kaul_question_2_false` directly refutes Question 2 (`ques: classify`) at $n = 2$ for every $p \ge 3$ (hence every $p \ge 4$): $(P_{DP}(G_1, m) P_{DP}(G_2, m)) / \prod_{i=0}^{p-1}(m - i) < P_{DP}(G, m)$ in $\mathbb{Q}$.
- **Type-Check & Axiom Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Kaul211205316Ques3.lean`
  - Exit code: `0`, zero warnings, zero `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern`/`set_option`.
  - `#print axioms` strictly `[propext, Classical.choice, Quot.sound]` for both `kaul_question_3_false` and `kaul_question_2_false`.
