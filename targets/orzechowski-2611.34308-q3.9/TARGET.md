---
source: arXiv:2611.34308v1 (Kamil Orzechowski, "Measurable equidecomposability and the Banach--Ruziewicz problem over locally compact non-Archimedean valued fields", dated November 24, 2026, Section 3, Open problems, Question 3.9, lines 621–623 of Measurable-equidecompositions-in-Q_p_n.tex)
status: reported
owner: scout-9
updated: 2026-11-27T15:19:00Z
attack_started_utc: 2026-11-27T14:59:07Z
identifiers: ["2611.34308", "2611.34308v1", "q:prime_residue_field", "Question 3.9"]
---

# Question 3.9 (`2611.34308v1`, Section 3, `Measurable-equidecompositions-in-Q_p_n.tex` lines 621–623)

> **Question.** Let $\mathbb{L}$ be a locally compact non-Archimedean valued field with residue field $\mathbb{F}_p$, $p$ prime. Is the action $\mathrm{Iso}(\mathbb{L})\curvearrowright (\mathbb{L},m_{\mathbb{L}})$ expanding?

*(Numbering verified from `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{question}[theorem]{Question}` in `Measurable-equidecompositions-in-Q_p_n.tex` L16–27: Section 3 contains Proposition 3.1, Proposition 3.2, Theorem 3.3, Corollary 3.4, Example 3.5, Corollary 3.6, Corollary 3.7, Question 3.8, and Question 3.9 at L621–623.)*

## Primary Definitions (`2611.34308v1`)

- **Non-Archimedean valued field (`Measurable-equidecompositions-in-Q_p_n.tex` L159–172):** A field $\mathbb{L}$ equipped with a nontrivial non-Archimedean valuation $|\cdot| : \mathbb{L} \to [0, \infty)$ inducing the ultrametric $d_{\mathbb{L}}(x, y) := |x - y|$. Its valuation ring is $\mathcal{O}_{\mathbb{L}} = \{x \in \mathbb{L} : |x| \le 1\}$, maximal ideal $\mathfrak{m}_{\mathbb{L}} = \{x \in \mathbb{L} : |x| < 1\}$, residue field $\mathcal{O}_{\mathbb{L}}/\mathfrak{m}_{\mathbb{L}} \cong \mathbb{F}_p$, and value group $|\mathbb{L}^\times|$. By `[UC, Corollary 12.2]` (cited at L171), $\mathbb{L}$ is locally compact iff it is complete, its residue field is finite, and $|\mathbb{L}^\times|$ is infinite cyclic.
- **Haar measure $m_{\mathbb{L}}$ (L384–387):** A nonzero Radon (left-)translation-invariant Borel measure on the locally compact abelian group $(\mathbb{L}, +)$.
- **Isometry group $\mathrm{Iso}(\mathbb{L})$ (L100, L386, L610, L622):** The group of surjective isometries of $(\mathbb{L}, d_{\mathbb{L}})$.
- **Family $\mathcal{C}(G \curvearrowright X)$ (L270):** All subsets $C \subseteq X$ with compact closure that $G$-cover a nonempty open set (i.e., $U \subseteq \bigcup_{i=1}^r g_i \cdot C$ for some nonempty open $U \subseteq X$ and finitely many $g_1, \dots, g_r \in G$).
- **Domain of expansion (Definition 2.8 / `def:domain_of_exp`, L321–334):** For a measure-preserving action $G \curvearrowright (X, \mathcal{A}, \mu)$, a set $C \in \mathcal{A}_\mu$ with $0 < \mu(C) < \infty$ is a *domain of expansion* if for every $\eta > 0$ there is a finite $R \subseteq G$ such that $\mu((R \cdot Y) \cap C) \ge \min\{(1 - \eta)\mu(C), \mu(Y)/\eta\}$ for all $Y \subseteq C$, $Y \in \mathcal{A}_\mu$ (equivalently, there exist $c > 0$ and finite $S \subseteq G$ such that $\mu((S \cdot Y) \cap C) \ge (1 + c)\mu(Y)$ for all $Y \subseteq C$ with $\mu(Y) \le \mu(C)/2$).
- **Expanding action (Definition 2.10 / `def:expanding_action`, L342–344):** Let $\mu$ be a $\sigma$-finite Borel measure on a Polish topological space $X$ that is nonzero on all nonempty open sets. A measure-preserving action $G \curvearrowright (X, \mu)$ is *expanding* if every $C \in \mathcal{B}_\mu \cap \mathcal{C}(G \curvearrowright X)$ is a domain of expansion.
- **Local spectral gap (Definition 2.13 / `def:local_spectral_gap`, L359–367):** $G \curvearrowright (X, \mathcal{A}, \mu)$ has *local spectral gap* with respect to $C \in \mathcal{A}_\mu$ ($0 < \mu(C) < \infty$) if there exist a finite $S \subseteq G$ and $\kappa > 0$ such that $\|f\|_{2, C} \le \kappa \sum_{g \in S} \|g \cdot f - f\|_{2, C}$ for all $f \in L^2(X, \mu)$ with $\int_C f \, d\mu = 0$. When $\mu(X) < \infty$, local spectral gap wrt $X$ is *spectral gap*.

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T14:57:18Z`
- `tools/novelty_grep.py "2611.34308" "prime_residue_field" "expanding" "Iso("`: 0 settlement hits across `watch/snapshots/**` (only `watch/snapshots/arxiv/arxiv_submissions.*` / `state.json` announcing `2611.34308v1`).
- `watch/snapshots/hwzw-algebra-number-theory-drafts.md`: 0 hits.
- `gh search prs "2611.34308"`, `gh search issues "2611.34308"`, `gh search repos "2611.34308"`, `gh search code "2611.34308"`, `trureturing/open-math` `dev` tree (`gh api`): 0 settlement hits (code search shows only daily arXiv RSS announcement feeds).
- Zenodo API (`https://zenodo.org/api/records?q=2611.34308`): `0` hits.
- `tools/arxiv_fetch.py abs 2611.34308 --no-cache` and `search_web`: sole version `2611.34308v1` (2026-11-25), Question 3.9 open.
