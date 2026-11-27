---
source: arXiv:2611.12469v1 (Section 8, Question 8.4 `\label{q:correspondence}` item (3), lines 3066–3085)
status: reported
owner: attack-2
updated: 2026-11-27T14:24:00Z
start_utc: 2026-11-27T13:40:21Z
identifiers: ["2611.12469", "2611.12469v1", "Teheux", "median algebra", "profinite completion", "q:correspondence"]
---

# Teheux (arXiv:2611.12469v1): Finite Subalgebras of Profinite Completions of Median Algebras

## Exact Statement (verbatim, `tools/.arxiv_cache/eprint/2611.12469v1/Notes_definability_pocset.tex`, lines 3066–3085)

> \begin{question}\label{q:correspondence}
> \begin{enumerate}
> \item For which finite median algebras $\mathrm{alg}{B}$ does the equality
>   $\classop{H}(\Mod(\varphi_{\alg{B}})) =
>   \Mod(\varphi_{\alg{B}})$ hold? Is this the case exactly when the dual
>   $\mathrm{alg}{B}^*$ is injective in $\Poc_\tau$, as it is for cubes
>   (Lemma~\ref{lem:cube-lift})?
> \item Is there a syntactically defined class of sentences of $L_{\M}$, beyond
>   the universal ones, whose translations are equivalent to first-order
>   sentences of $L_{\mathrm{Poc}}$ computed from their syntax? Is $\ST(\sigma)$
>   equivalent to a first-order sentence of $L_{\mathrm{Poc}}$?
> \item Does every universal sentence that holds in a median algebra $\mathrm{alg}{A}$
>   hold in $\hat{\mathrm{alg}{A}}$, that is, does every finite subalgebra of
>   $\hat{\mathrm{alg}{A}}$ embed into $\mathrm{alg}{A}$?
> \item Is there a syntactically defined class of sentences of the form
>   $\forall \mathbf{x}\, \exists \mathbf{y}\, \psi$, with $\psi$
>   quantifier-free, that hold in $\hat{\mathrm{alg}{A}}$ whenever they hold in
>   $\mathrm{alg}{A}$? Not all such sentences do.
> \end{enumerate}
> \end{question}

**Specific sub-question claimed:** Section 8, **Question 8.4** (`q:correspondence`) item **(3)** — answered **YES** in [PROOF.md](PROOF.md) and verified by [verify.py](verify.py) (`PASS`, zero floats).

## Gate 1 Novelty Receipt
- **Checked UTC:** `2026-11-27T13:42:35Z` (full live attack-gate re-check by `teheux-lit` in [notes/novelty-attack.md](notes/novelty-attack.md); initial screen check `2026-11-27T10:00:00Z`).
- **Local `novelty_grep.py`:** Scanned 717 files across `watch/snapshots/**`: only index entries in `watch/snapshots/arxiv/`; 0 hits in `hwzw-algebra-number-theory-drafts.md`, `insorrowmeow`, `mylesparslow`, `1337-solved-conjectures`, `openai-math`, `trureturing`.
- **Live GitHub:** 0 PRs/repos for `"2611.12469"` or title; `gh search issues "2611.12469"` returned only `the-omega-institute/trureturing#29092` (inspected live via `gh api`: open, 0 comments, explicitly scoped to Question 8.4(2) second sentence `ST(\sigma)` only); `trureturing` `dev` tree and `Hwzw/algebra-number-theory-drafts` clear.
- **Live arXiv / Zenodo / Crossref / DataCite / Web:** `2611.12469v1` is sole/latest version (`v2` HTTP 404); Zenodo (`2611.12469`: 0 hits), Crossref, DataCite, web search, and classic literature check found no prior settlement of Question 8.4(3). (Coverage limit: live S2 HTTP 429 and OpenAlex daily budget limit; snapshot recorded `cited_by=0`.)
- **Verdict:** **OPEN** (passes Gate 1).
