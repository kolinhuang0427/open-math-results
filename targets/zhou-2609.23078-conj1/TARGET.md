---
source: arXiv:2609.23078v1 (You Zhou, "Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module", submitted 2026-09-19, Section 1 Conjecture 1 / Section 4 Conjecture 4.1 `conj:main1-all-types`, lines 136–138 and 516–523)
status: reported
owner: attack-2
updated: 2026-11-27T15:09:00Z
start_utc: 2026-11-27T14:13:11Z
identifiers: ["2609.23078", "2609.23078v1", "conj:main1-all-types", "Conjecture 1", "Conjecture 4.1"]
---

# You Zhou (`arXiv:2609.23078v1`): Conjecture 1 / Conjecture 4.1 (`conj:main1-all-types`)

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2609.23078/MAXIMAL_PROPER_EXTREMAL_SUBSET_IN_THE_CRYSTAL_BASIS_OF_A_FINITE-DIMENSIONAL_IRREDUCIBLE_MODULE.tex`, lines 136–138, 516–523)

> **Conjecture 1** (`\label{conj:main1-all-types}`, Conjecture 4.1 in Section 4):
> For $\lambda \in P^+$, we have
> $$\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}.$$
> Therefore, by Proposition 3.7 (`prop:max-proper-extremal`), $\mathcal{B}(\lambda) \setminus \mathcal{F}(b_\star)$ is the maximal proper extremal subset of $\mathcal{B}(\lambda)$.

*(Numbering verified from `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}` at lines 17–21; Theorem 1 / Theorem 4.4 proves the conjecture for type $A_{n-1}$.)*

## Primary Definitions (Sections 1–4, lines 101–138, 169–357, 452–528)

- $\mathfrak{g}$ is a finite-dimensional simple Lie algebra over $\mathbb{C}$ with simple root index set $I$, Weyl group $W$ with longest element $w_\circ$, dominant integral weights $P^+$, and $\mathcal{B}(\lambda)$ the crystal basis of the finite-dimensional irreducible $U_q(\mathfrak{g})$-module $V(\lambda)$ with lowest element $b_{w_\circ \lambda}$ and Kashiwara operators $\tilde{e}_i, \tilde{f}_i$ ($i \in I$).
- The $i$-string of $b \in \mathcal{B}(\lambda)$ is $S^i(b) := \{\tilde{e}_i^{\max}(b), \dots, \tilde{e}_i(b), b, \tilde{f}_i(b), \dots, \tilde{f}_i^{\max}(b)\} \setminus \{0\}$.
- A subset $X \subseteq \mathcal{B}(\lambda)$ is *extremal* if $S^i(b) \cap X \in \{\varnothing, S^i(b), \{\tilde{e}_i^{\max}(b)\}\}$ for all $b \in \mathcal{B}(\lambda), i \in I$; $\langle c \rangle_{\mathrm{Ext}}$ is the smallest extremal subset containing $c$, and $\Gamma_\lambda := \{c \in \mathcal{B}(\lambda) \mid \langle c \rangle_{\mathrm{Ext}} = \mathcal{B}(\lambda)\}$.
- Checked operators: $\check{e}_i(b) := \tilde{f}_i \tilde{e}_i^{\max}(b)$ if $\tilde{e}_i(b) \ne 0$, else $b$; for a reduced expression $w_\circ = s_{i_1}\cdots s_{i_\ell}$, $\check{e}_{w_\circ} := \check{e}_{i_1}\cdots \check{e}_{i_\ell}$.
- $b_\star := \check{e}_{w_\circ}(b_{w_\circ\lambda})$, $\mathcal{C}_{b_\star} := \{c \in \mathcal{B}(\lambda) \mid \check{e}_{w_\circ}(c) = b_\star\}$, and $\mathcal{F}(b_\star) := \{\tilde{f}_{j_1}\cdots \tilde{f}_{j_s}(b_\star) \mid s \ge 0,\ j_1,\dots,j_s \in I\} \setminus \{0\}$.

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T14:15:06Z` (full attack-time receipt in `notes/novelty-attack.md`; initial scout receipt `2026-11-27T13:44:30Z`).
- `tools/novelty_grep.py` across `watch/snapshots/**`: `0/721` files (`hwzw-algebra-number-theory-drafts.md`, `insorrowmeow-oeis-ids.md`, `mylesparslow-conjecture-ledger.md`, `1337-solved-conjectures`, `openai-math` all clear).
- Live GitHub (`gh search prs/issues/repos/code` for `2609.23078` and `"maximal proper extremal subset"`, plus `the-omega-institute/trureturing` `dev` tree & PRs and `Hwzw/algebra-number-theory-drafts` `main` tree): `0` settlements (`13` code hits are arXiv RSS/daily mirrors or numeric collisions).
- Live Zenodo API, Crossref, DataCite, arXiv API (`--no-cache`, `2609.23078v2` returns HTTP `404`), and `search_web` (incl. Assaf–Dranowski–González, Armon `2310.14584`, Kashiwara/Joseph/Littelmann/Biane–Bougerol–O'Connell/Berenstein–Zelevinsky): no settlement or v2 found. Verdict: **OPEN** outside type $A$.

## Candidate Resolution

- **Result:** **PROVED** in full generality for all finite-dimensional complex simple Lie algebras $\mathfrak{g}$ ($A, B, C, D, E, F, G$) and all $\lambda \in P^+$.
- **Artifacts:** `PROOF.md` (proves general tensor dominance monotonicity $H(a \otimes b) \ge H(a \otimes \tilde{f}_i(b))$ via Lusztig canonical basis positivity + folding in $\mathfrak{g}^\vee$, an exact path-ordered exponential gauge identity $g(\psi_u) = y_j(a) g(\psi) y_j(-b)$, and Littelmann–Pitman tropical limits, then deduces $\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$ and $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$) and exact zero-float/zero-`/` `verify.py` (`PASS`, exit `0` in `1.93s`, AST check `[]`, covering 34 crystals across $A_2, C_2, G_2, B_3, C_3, D_4$ plus explicit $D_4 \to G_2^\vee$ folding & tropical identity checks).
