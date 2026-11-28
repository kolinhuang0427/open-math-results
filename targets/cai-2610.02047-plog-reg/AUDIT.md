# Blind Audit: `cai-2610.02047-plog-reg`

- **Auditor:** `@audit-2` (`auto`)
- **Target:** `targets/cai-2610.02047-plog-reg/`
- **Primary Source Verified Verbatim:** Shaowei Cai and Ziqun Li, *"Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth"*, `arXiv:2610.02047v1` (`cs.CC`, Oct 1, 2026), Section 8 (`\section{Conclusion and future directions}`, `main.tex` L4025–4031), together with Section 3 (`\section{Preliminaries}`, L1000–1153), Section 4 (`\section{Preparations for the constructions}`, L1154–1755), Section 6 (`\section{Regular resolution upper bounds}`, L3234–3360), and Appendix B (`lem:mres-to-res` proof, L4265–4392) extracted from `tools/.arxiv_cache/eprint/2610.02047.src` and metadata from `tools/.arxiv_cache/abs/2610.02047.html`.
- **Verdict:** **PASS**
- **Charter Publication Label:** `written proof, internally audited`

## File Fingerprints Verified
- `TARGET.md`: `8a580f9f1cc5f3619f570ff87156e550`
- `PROOF.md`: `4660560db379744718a91a1d52bc745e`
- `notes/check-check-1.md`: `a92b99d0033a542c83b397a46922bf9b`
- `notes/check-check-1.py`: `e80d172f042766c6db111b6411fb1733`

## Audit Summary

### 1. Statement Fidelity
- Compiled section numbering verified across `main.tex`: Section 3 is `\section{Preliminaries}` (L1000; L1024–1025 states the no-empty/no-tautological-clause convention cited at `PROOF.md` L7), Section 4 introduces $\mathrm{tw}_{\mathrm{plog}}^*(F)$ and `lem:plog-decomposition-size` / `thm:plog-one-sided` / `lem:mres-to-res`, and Section 8 is `\section{Conclusion and future directions}` (L3990; open problem verbatim at L4025–4031).
- `TARGET.md` L14 reproduces `main.tex` L4025–4031 verbatim, and Theorem 1 (`PROOF.md` L7–9) answers it affirmatively with an FPT-sized regular resolution refutation bound $|\pi'| \le k^2(n+m)\, 2^{O(w \log(w+2))} \le (n+m)^3\, 2^{O(w \log(w+2))}$ where $w = \mathrm{tw}_{\mathrm{plog}}^*(F)$.

### 2. Mathematical Verification (`PROOF.md`)
- **Section 1 & Lemma 1 (L15–41):** Uses `lem:plog-decomposition-size` (`|V(T)| = O(k(n+m)w)`) and proves for every $c \in \chi_c(t) \setminus P_t$ that $P_c \cap V(T_t) = \emptyset$, $|c_t^{\mathrm{int}} \setminus \chi_v(t)| \le \rho_{\mathcal P}(c) \le 2^{\omega_{\mathcal P}(t,c)} - 1$, and $\prod_{c \in \chi_c(t) \setminus P_t} |c_t^{\mathrm{int}}| \le (w+2)^{w+1} 2^{w+1} = 2^{O(w \log(w+2))}$. Verified exact.
- **Section 2 (L44–64):** Post-order variable ordering by unique forget-variable node $\mathrm{forg}(x)$ satisfies Observation 1 ($y < x$ for $y \in \mathrm{Var}_t \setminus \chi_v(t), x \in \chi_v(t)$, and $y_1 < y_2 < x$ at join nodes). Hybrid target family $\mathcal E_{\mathrm{plog}}(t,\alpha,A)$ keeps $c_t^{\mathrm{ext}}$ for on-path clauses $c \in B_t(A) \cap U_\alpha(A)$, $\mathcal C_1(c_t^{\mathrm{int}})$ for off-path $c \in A \setminus P_t$, and $\mathcal C_0(c_t^{\mathrm{int}})$ for off-path $c \in (\chi_c(t) \setminus P_t \setminus A) \cap U_\alpha$, specializing to $\{\bot\}$ at the empty root $r$.
- **Section 3 & Lemma 2 (L67–98):** Safe sequential elimination now carries exact hypotheses ($\mathrm{var}(E) \cap \mathrm{var}(H) = \emptyset$, $G \uplus E$ non-tautological, no spurious disjointness between $G$ and $E$), handles both $J \neq \emptyset$ ($j_0 = \max J$) and $J = \emptyset$ ($L_0 = G \uplus E \uplus H$), handles tautological $R_j$ when $\ell_j \in G$ (replaced by repetition/weakening in $\pi'$), and preserves (P2)–(P3) in at most $q + 1$ steps.
- **Section 4 Cases 1–6 (L102–196):** All audit defects from `#2052` and `#2061` verified fixed:
  - **Cases 1–2 (`leaf`, `intro_c`):** Verified exact; weakening introduces only $\chi_v(t)$-variables disjoint from $\mathrm{ResVars}(M') \subseteq \mathrm{Var}_{t'} \setminus \chi_v(t')$.
  - **Case 3 (`intro_v`, L117–140):** Handles $c \in A_x \setminus P_t$ (incl. $\neg\ell \in c$), unifies $W_p \cap U_{\alpha'}$ and $S_{\mathrm{sat}}$ into $W = \{c \in (W_p \cap U_{\alpha'}) \cup S_{\mathrm{sat}} : c_{t'}^{\mathrm{int}} \setminus \chi_v(t') \neq \bot\}$, strips $H_c = c_{t'}^{\mathrm{int}} \setminus \chi_v(t')$ via Lemma 2, weakens $M_{t'} \subseteq M$ adding only $\chi_v(t)$-variables, and bounds total steps per tuple cleanly by $\sum_{d=1}^s \prod_{j=1}^d(1+|H_{c_j}|) + 1 \le 2^{w+2} + 1$.
  - **Case 4 (`forget_v`, L142–150):** Subcases 4a–4c checked term-by-term; Subcase 4c cleanly proves (P3) via $y \in \mathrm{var}(M_0) \cap \mathrm{var}(M_1)$ for $y \in \mathrm{Var}_t$ and (P1) for $y \notin \mathrm{Var}_t$.
  - **Case 5 (`forget_c`, L152–158):** Accurately states tautological $R_j$ iff $\ell_j \in G$ or $\neg\ell_u \in G$ for some $u > j$, weakens initial clause $c$ to $L_0 = G \uplus c$ when $J = \emptyset$, and invokes Lemma 2 in $\le r + 1 \le k + 1$ steps.
  - **Case 6 (`join`, L160–196):** Partitions $B_0^{\mathrm{unsat}}$ into $B_{1,\mathrm{pure}} \sqcup B_{2,\mathrm{pure}} \sqcup B_0^{\mathrm{split}}$, routes $A \setminus P_{t_0}$ into $A_1^{\mathrm{off}}$ ($\mathrm{var}(\ell_i) \in \mathrm{Var}_{t_1} \setminus \chi_v(t_0)$) and $A_2^{\mathrm{off}}$ ($\mathrm{var}(\ell_i) \in \mathrm{Var}_{t_2}$), eliminates $E_1 = D_1 \cup (A_2^{\mathrm{off}} \cap U_\alpha)$ on the $t_1$-branch and $D_2$ on the $t_2$-branch (exploiting $c_{t_2}^{\mathrm{int}} \subseteq C_c$ for $c \in A_1^{\mathrm{off}}$ by Observation 1(2)), performs reverse induction on $h = p, \dots, 0$ via Lemma 2 with $E = d_{t_0}^{\mathrm{ext}}$, and bounds steps per tuple by $(w+2)\cdot 2^{2w+2}\cdot(2^{w+2}+1) \le (w+2)\cdot 2^{3w+5} = 2^{O(w)}$.
- **Section 5 (L199–205):** Total length bound $|\pi| \le k^2(n+m)\, 2^{O(w \log(w+2))}$ verified; since all tautological targets and unused $R_j$ premises are derived in $1$ step from axioms with zero incoming resolution edges, every directed path in $G_\pi$ satisfies `lem:mres-to-res` (`main.tex` L1641, L4376–4384), producing a regular resolution refutation $\pi'$ of length $|\pi'| \le |\pi| \le (n+m)^3\, 2^{O(w \log(w+2))}$.

### 3. Independent Exact-Arithmetic Verification
- Executed `.venv/bin/python -u targets/cai-2610.02047-plog-reg/notes/check-check-1.py`: exit code `0`, AST-verified `0` float constants and `0` `float()` calls:
  ```
  JOIN_COUNTEREXAMPLE: L165_fails=True, corrected_regular_ok=True, len=6
  COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS
  AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS
  PASS
  ```
- Verified all 3 fixed recursion slices (`L486`, `L640`, `L689`), full regular-refutation DAG verification across all 5 adversarial TDs (covering $S_{\mathrm{sat}}$ in `intro_v`, $\alpha'$-satisfied $W_p$, off-path `forget_c` with $G \neq \bot, J = \emptyset$, $|W| = 2$ in `intro_v`, and multi-clause join) plus all 27/27 clause-path assignments on a 3-clause join TD with $|\text{elim\_list}| \ge 2$ and shared external literals in $d_{t_0}^{\mathrm{ext}}$.

## Handoff
- Passed blind audit; handed off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including arXiv, GitHub, ECCC, and complexity venues).
