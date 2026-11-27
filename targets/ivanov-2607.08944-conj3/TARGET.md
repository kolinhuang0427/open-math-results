source: https://arxiv.org/abs/2607.08944v1 (Illya Ivanov, "Illuminating Primitive Polytopes", Section 1.4 "Two Kinds of Primitive Polytopes", Conjecture 6 / `conj:fleanverts`, lines 308–312)
status: reported
owner: scout2-5
updated: 2026-11-27T09:44:30Z
identifiers: ["2607.08944", "2607.08944v1", "Illya Ivanov", "Illuminating Primitive Polytopes", "conj:fleanverts", "primitive polytope"]

# Ivanov (2026) — Maximum Number of Vertices of a Primitive Polytope (`conj:fleanverts`)

- **Started:** 2026-11-27T09:18:47Z

## Exact Statement
From `tools/.arxiv_cache/eprint/2607.08944/main.tex`, Section 1.4 (*Two Kinds of Primitive Polytopes*, lines 308–312):

> **Conjecture 6 (`\label{conj:fleanverts}`).**
> A primitive polytope in $\mathbb{E}^d, d \ge 4$ has at most $2^d$ vertices, even fewer if it isn't an affine $d$-cube.

Preliminaries from Section 1.3–1.4 (`main.tex`, lines 237–239, 260–269):
- A convex polytope $P \subset \mathbb{E}^d$ (with nonempty interior) is *primitive* if omitting any halfspace from its minimal halfspace representation $P = H_1^- \cap \dots \cap H_n^-$ renders the intersection unbounded.
- Equivalently (`Theorem 3` `thm:facleanposbas` / `Corollary 4` `cor:flean_crit`), with $\mathbf{o} \in \mathrm{int} P$, $P$ is primitive iff the set of vertices of its polar polytope $P^\circ$ (i.e., the outer facet normals of $P$) forms a *positive basis* of $\mathbb{E}^d$, and $|\mathrm{vert}(P)| = f_{d-1}(\mathrm{conv}(\mathrm{vert}(P^\circ)))$.

## Gate 1 Novelty Receipt
- **Checked UTC:** 2026-11-27T09:18:48Z
- **`tools/novelty_grep.py`:** `.venv/bin/python tools/novelty_grep.py "2607.08944" "fleanverts" "primitive polytope" "Illya Ivanov"` returned 0 hits across 608 files in `watch/snapshots/**`.
- **arXiv API (`arxiv_fetch.py`):** `query --id-list 2607.08944` confirms `2607.08944v1` (2026-07-09) is the sole version; `query 'abs:"2607.08944"'` returned 0 citing preprints.
- **GitHub (`gh search code` + `gh api`):** `gh search code "2607.08944"` returned 14 hits (`LeeMarshall1113/ai-math-results` `results/hadwiger-h3/NOVELTY.md` and `MColbrook/AIM` `problems/486-hadwiger-boltyanski-illumination.md`, both inspected via `gh api` — they cite `2607.08944` solely for Hadwiger–Boltyanski illumination Theorem 2, not Conjecture 3 / vertex count). `gh search code "fleanverts" --limit 10` (re-run at 2026-11-27T09:25:27Z after cooldown) returned `no code results matched your search`.
- **`search_web`:** Returned `arXiv:2607.08944v1` itself; no settlement of `conj:fleanverts` found.
- **What was not covered:** Unindexed preprints/repos not indexed by arXiv or GitHub code search.
- **Verdict:** Open (passes Gate 1).
