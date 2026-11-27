---
source: arXiv:2611.30155v1 (E. Ingrosso, M. Trombetti, and A. Zitouni, "Groups with dual classes of subgroups", dated 2026-11-23, Section 4, Question 4.6 at lines 784–786 of pronormali_arxiv.tex)
status: reported
owner: scout-9
updated: 2026-11-27T16:39:00Z
attack_started_utc: 2026-11-27T16:26:25Z
identifiers: ["2611.30155", "2611.30155v1", "Question 4.6", "Theorem 4.5"]
---

# Question 4.6 (`2611.30155v1`, Section 4, `pronormali_arxiv.tex` lines 784–786)

> **Theorem 4.5 (`\label{sip}`):** Let $G$ be a locally graded group whose subgroups are pronormal or contained in the pro-norm. If $H$ is a subnormal subgroup of $G$, then $H$ has defect at most $7$.
>
> **Question 4.6:** What is the smallest possible defect of subnormality in the statement of Theorem 4.5?

## Primary Definitions (`2611.30155v1`, Sections 1–2)

- **Pronormal subgroup (`pronormali_arxiv.tex` L178):** A subgroup $H \le G$ is *pronormal* if for every $g \in G$, $H$ and $H^g$ are conjugate in $\langle H, H^g \rangle$ (equivalently, $g$ *pronormalizes* $H$).
- **Pro-norm (`pronormali_arxiv.tex` L190, L225):** The *pro-norm* $N_{\mathrm{pro}}(G)$ is the set of all elements of $G$ that pronormalize every subgroup of $G$.
- **Locally graded group (`pronormali_arxiv.tex` L219):** Every non-trivial finitely generated subgroup has a non-trivial finite homomorphic image.
- **Subnormal defect:** Minimum $d \ge 0$ such that there exists a chain $H = H_0 \trianglelefteq H_1 \trianglelefteq \dots \trianglelefteq H_d = G$.

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T16:25:17Z`
- `tools/novelty_grep.py "2611.30155"`: 0 settlement hits across `watch/snapshots/**` (`arxiv_submissions.*` and `state.json` only).
- `watch/snapshots/hwzw-algebra-number-theory-drafts.md` and `watch/snapshots/hexagonmath-index.md`: 0 hits.
- `gh search prs/issues/repos/code "2611.30155"`, `trureturing/open-math` `dev` tree (`gh api`): 0 settlement hits.
- Zenodo API (`https://zenodo.org/api/records?q=2611.30155`): `0` hits.
- `tools/arxiv_fetch.py abs 2611.30155 --no-cache` and `search_web`: sole version `2611.30155v1` (2026-11-23), J. Aust. Math. Soc. paper, Question 4.6 open.
