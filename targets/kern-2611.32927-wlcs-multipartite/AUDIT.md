# Blind Audit: `kern-2611.32927-wlcs-multipartite`

- **Auditor:** `@audit-2` (`auto`)
- **Target:** `targets/kern-2611.32927-wlcs-multipartite/`
- **Primary Source Verified Verbatim:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (`cs.DS, cs.CC, cs.DM`, Nov 24, 2026; full version of LATIN 2026), Section 5 (`sections/conclusion.tex`, line 5), together with `main-arxiv.tex`, `sections/introduction.tex`, `sections/preliminaries.tex`, `sections/stcon.tex`, and `sections/gcon.tex` extracted from `tools/.arxiv_cache/eprint/2611.32927.src` and metadata from `tools/.arxiv_cache/abs/2611.32927.html`.
- **Verdict:** **PASS**
- **Charter Publication Label:** `written proof, internally audited`

## File Fingerprints Verified
- `TARGET.md`: `665d5396cadac15b18f6c60ced416928`
- `PROOF.md`: `c59301070c7ca00e678995e910141c50`
- `notes/check-check-1.md`: `631f4532466cc2f7a13f163dec42ecef`
- `notes/check-check-1.py`: `7ec86643543c1942820f738e22d0fe90`

## Audit Summary

### 1. Statement Fidelity
- Compiled section order verified from `main-arxiv.tex` and `\section` headers across `sections/*.tex`: §1 Introduction, §2 Preliminaries, §3 Local Connectivity (`stcon.tex`), §4 Global Connectivity (`gcon.tex`), §5 Conclusion (`conclusion.tex`). `TARGET.md` L3 accurately cites Section 5 and the LATIN 2026 full-version arXiv metadata (`v1`, Nov 24, 2026).
- `TARGET.md` L14 reproduces `sections/conclusion.tex` L5 character-for-character, and `TARGET.md` L18 matches the `WLCS` definition in `sections/stcon.tex` L215–221 verbatim (where $w : \mathcal{S}(\widehat{G}) \times \mathbb{N}_{\ge 0} \to \mathbb{R}$ and $\lambda \in \mathbb{R}$).

### 2. Mathematical Verification (`PROOF.md`)
- **NP membership (L13):** For binary weights $w(\tilde{s}, i) \in \{0, 1\}$ and $\lambda = 0$, checking $a$--$b$ reachability in $\widehat{G}' \circ c'$ and $\sum_{\tilde{s}} w(\tilde{s}, c'(\tilde{s})) \le 0$ takes linear time (`preliminaries.tex` L21).
- **Source hardness problem (L15):** Since $K_2 + K_2$ has no isolated vertices and is not complete multipartite, Theorem `thm:dichotomy-lcs` (`sections/stcon.tex` L149, L168–186) directly establishes $\mathsf{NP}$-completeness of unweighted `LCS` restricted to $\{1^\star\}$-bounded $(K_2 + K_2)$-shaped switches.
- **Preprocessing (L17):** Every $\{1^\star\}$-bounded $(K_2 + K_2)$-shaped switch $s$ has positions of size $\le 1$ whose union is two vertex-disjoint edges $u_s v_s, x_s y_s$ ($|\{u_s, v_s, x_s, y_s\}| = 4$). Because $a$--$b$ connectivity is monotone under adding edges, deleting empty positions and deduplicating repeated positions in $O(|\widehat{G}|)$ time preserves exact `LCS` equivalence and standardizes every switch to $s[0] = \{u_s v_s\}, s[1] = \{x_s y_s\}$.
- **Reduction & switch properties (L19–28):** Replacing each $s$ by $\tilde{s}[0] = \{u_s v_s\}$ ($w=0$), $\tilde{s}[1] = \{x_s y_s\}$ ($w=0$), $\tilde{s}[2] = \{u_s y_s\}$ ($w=1$), $\tilde{s}[3] = \{x_s v_s\}$ ($w=1$) with $\lambda = 0$ runs in $O(|\widehat{G}|)$ time. Every $\tilde{s}$ is $\{1,1,1,1\}$-bounded (hence $\{1^\star\}$-bounded) and $G[\tilde{s}] \cong K_{2,2}$ with bipartition $\{u_s, x_s\} \sqcup \{v_s, y_s\}$, which is complete multipartite (note `preliminaries.tex` L19 allows distinct switches to share underlying vertex pairs in the switch multigraph, while $\widehat{G}' \circ c'$ takes the simple edge union). Since $w \ge 0$ and $\lambda = 0$, $w(c') \le 0 \iff c'(\tilde{s}) \in \{0, 1\}$ for all $\tilde{s}$, giving a bijection $c(s) = c'(\tilde{s})$ with $\widehat{G}' \circ c' = \widehat{G} \circ c$ (including the degenerate $\mathcal{S}(\widehat{G}) = \emptyset$ case).
- **Remark (L30):** Verified accurate — `thm:dichotomy-lcs`'s reduction from `TCP` on $\{K_2 + K_2, K_3\}$ uses only nonempty switch positions, preserved by $\tilde{s}$, and every non-empty edge-subgraph of a star $\mathcal{K}_{1,\star}$ or $K_3$ remains complete multipartite ($\mathcal{K}_{1,\star}$, $K_3$, or $K_2$).

### 3. Independent Exact-Arithmetic Verification
- Executed `.venv/bin/python -u targets/kern-2611.32927-wlcs-multipartite/notes/check-check-1.py`: exit code `0`, AST-verified `0` float constants and `0` `float()` calls:
  ```
  REDUCTION_EXACT: checked=120, yes=48, no=72, lam1_false_positives=24
  PASS
  ```
- Tested 120 brute-force exact instances (including empty and duplicate positions) verifying `LCS == WLCS(lambda=0)` on all 120 cases (`yes=48`, `no=72`) and confirming 24 false positives when $\lambda$ is relaxed to $1$, plus automated section-number and regression checks against `2611.32927.src`.

## Handoff
- Passed blind audit; handed off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including arXiv, GitHub, ECCC, and complexity venues).
