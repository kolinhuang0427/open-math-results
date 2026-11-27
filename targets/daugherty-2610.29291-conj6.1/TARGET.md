source: https://arxiv.org/abs/2610.29291v1 (Section 6, Conjecture 6.1, label conj:box)
status: reported
owner: scout2-1
updated: 2026-11-27T04:58:00Z
identifiers:
  - 2610.29291
  - 2610.29291v1
  - Spencer Daugherty
  - Latin tableaux
  - Conjecture 6.1
  - conj:box
  - wide partitions

# Daugherty et al. (2026) Conjecture 6.1 — Box-addition monotonicity on wide partitions

## Primary Source & Exact Verbatim Statement

From Spencer Daugherty, Michaela Fahnestock, Shawn Huxtable, Michael Larson, Nourah Al Munayes, and Storey Peacock, *"Counting and constructing Latin tableaux"*, arXiv:2610.29291v1 (submitted 2026-10-21), Section 6 ("Open problems"), Conjecture 6.1 (`\label{conj:box}`, lines 717–719 of `final.tex`):

> **Conjecture 6.1.** If $\lambda$ and $\mu$ are wide partitions where $\lambda_i = \mu_i + 1$ for some $i \in [\ell(\lambda)-1]$ and $\lambda_j = \mu_j$ when $j \neq i$, then $LT(\lambda) \geq LT(\mu)$.

Context definitions from Section 2 ("Preliminaries") and Section 4–5:
- A partition $\lambda = (\lambda_1, \ldots, \lambda_\ell)$ is *wide* if every lower subpartition $\nu$ (obtained by deleting rows $1$ through $m$ for some $m$) satisfies $\nu \succeq \nu'$ (equivalently, every subpartition $\nu \subseteq \lambda$ satisfies $\nu \succeq \nu'$).
- $LT(\lambda)$ is the number of Latin tableaux of shape $\lambda$ and type $\lambda'$.
- By Proposition 5.5 (`final.tex` lines 695–701), the case $i = 1$ (adding a box to the top row) holds unconditionally; the paper notes that adding a box to the bottom row $i = \ell(\lambda)$ can decrease $LT$ (e.g., $LT((4,4,2,2)) = 8 < 12 = LT((4,4,2,1))$), and states Conjecture 6.1 was verified computationally for partitions of size $n \le 22$.

## Gate 1 Novelty Receipt

- **Checked UTC:** 2026-11-26T23:35:30Z – 2026-11-26T23:55:48Z
- **Local snapshots (`novelty_grep.py`):** Query `2610.29291 Daugherty "Latin tableaux" "Latin tableau"` across 356 snapshot files returned 0 matches.
- **Zenodo API:** `https://zenodo.org/api/records?q="2610.29291" OR "Latin tableaux"` returned 0 hits for `2610.29291` (1 unrelated July 2026 LADA verification bundle).
- **Web search (`search_web`):** Query `"2610.29291" OR "Counting and constructing Latin tableaux"` returned only the arXiv preprint `2610.29291v1`.
- **GitHub (`gh`):**
  - `the-omega-institute/trureturing-tools` `SCREENED-OUT.md` and `aliromman/math` tree: 0 matches.
  - `gh search issues` for `2610.29291`, `Daugherty`, `conj:box`, `"wide partitions"`: `trureturing#20269` targets Conjecture 6.3 and `trureturing#26377` targets Conjecture 6.2; **0 issues/PRs** target Conjecture 6.1 (`conj:box`).
- **Conclusion:** Target is **OPEN**.
