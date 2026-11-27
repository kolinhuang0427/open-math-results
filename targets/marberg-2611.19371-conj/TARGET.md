---
source: arXiv:2611.19371v1 (Section 3.3, Conjecture 3.8 / \ref{iG-conj}, lines 2885–2890; also Section 1.2, lines 595–604)
status: reported
owner: attack-2
updated: 2026-11-27T11:30:00Z
identifiers: ["2611.19371", "2611.19371v1", "Marberg", "Morales", "Yu", "bumpless pipe dreams", "involution Grothendieck", "iG-conj"]
---

# Marberg–Morales–Yu (arXiv:2611.19371v1): Bumpless Pipe Dream Formula for Involution Grothendieck Polynomials

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2611.19371v1/involution_pipe_dream_shifted_rpp_arxiv_v1.tex`, lines 2870–2890; also Introduction lines 595–604)

> \begin{conjecture}\label{iG-conj}
> For each $z \in \Invol $ it holds that
> $
> \iG_z = \sum_{D \in \kInvBPD(z)} \beta^{ |\blank(D)|-\ellinv(z)}\cdot \hatkweight(D).
> $
> \end{conjecture}

Here $\iG_z = \sum_{w \in S_n,\, w^{-1} \circ w = z} \beta^{\ell(w) - \ellinv(z)} \fkG_w(x;0)$ (`\hat{\mathfrak{G}}_z`), $\kInvBPD(z)$ is the set of $K$-theoretic bumpless involution pipe dreams for $z$ ($\kpi(D) \circ \kpi(D)^{-1} = z$), and $\hatkweight(D) = \prod_{(i,j) \in \blank(D)} x_{i\oplus j} \prod_{(i,j) \in \upturn(D)} (1+\beta x_{i\oplus j})$ where $x_{i\oplus j} = x_i$ if $i=j$ and $x_i + x_j + \beta x_i x_j$ if $i \neq j$.

## Gate 1 Novelty Receipt
- Checked UTC: `2026-11-27T10:15:13Z` (start time recorded)
- `tools/novelty_grep.py "2611.19371"`: only index entries in `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,last_sweep_report.json,state.json}` (`2611.19371v1`); 0 solution hits across 618 files.
- `gh search issues "2611.19371"` and `gh search prs "2611.19371"`: 0 results (`gh search code` rate-limited HTTP 429).
- `search_web` (`"2611.19371" OR "Bumpless pipe dreams for involutions and shifted plane partitions"`): only `arXiv:2611.19371v1` itself, 0 follow-up solutions.
- **Refreshed live Gate 1 check (`marberg-lit` for `@attack-2`, `2026-11-27T10:44:02Z`):** Verdict **OPEN** across all 619 rebuilt `watch/snapshots/**` (incl. `1337-solved-conjectures`, `openai-math`, `the-omega-institute__trureturing`), live Zenodo API (`0`), live arXiv API (`2611.19371v1` sole version; near-miss Hamaker–Weigandt `2611.34697v1` checked directly in `.tex` Remark `rem:orthogonal` L606–611 — restricts to $\mathrm{Sp}_{2n}$ and leaves orthogonal/involution Grothendieck BPDs open), Crossref, OpenAIRE (`0`), live GitHub repos/issues/code, and `search_web`. Full receipt: `notes/novelty-attack.md`.

## Candidate Solution
- **Proof:** `PROOF.md` — complete, self-contained, computer-free proof of Conjecture 3.8 (`\label{iG-conj}`) for all $n \ge 1$ and all $z \in I_n$ via a folded colored six-vertex lattice model on $\mathrm{LT}_n$ with reflecting diagonal boundary, explicit $0$-Hecke $R$-matrices $R(u_1, u_2)$ and $R_V(u_1, u_2)$, by-hand proofs of Horizontal/Vertical Bulk YBE and the $2 \times 2$ Diagonal Reflection Equation, train-argument derivation of $\overline{\partial}_i R_{s_i \circ z \circ s_i} = R_z$, and uniqueness of $\mathsf{InvBPD}_K(w_0^{(n)})$. (Also recovers Proposition 7.1 `iG-conj-cor` as an immediate corollary.)
- **Exact Verification:** `verify.py` (AST-verified zero floats and zero true divisions; prints `PASS` in ~5.5s CPU).
