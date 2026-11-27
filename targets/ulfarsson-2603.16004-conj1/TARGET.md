---
source: arXiv:2603.16004v1 (Section 2, Conjecture 2.9 / \label{conj:general-reverse}, lines 371–375)
status: reported
owner: attack-5
updated: 2026-11-27T09:52:05Z
identifiers: ["2603.16004", "2603.16004v1", "Ulfarsson", "PAP", "Permutations Avoiding Patterns", "conj:general-reverse"]
---

# Ulfarsson (arXiv:2603.16004v1): Reverse-Reply Conjecture for PAP

## Exact Statement (verbatim, Henning Ulfarsson, *A Permutation Avoidance Game with Reverse Replies and Monotone Traps*, `arXiv:2603.16004v1`, Section 2, Conjecture 2.9; `tools/.arxiv_cache/eprint/2603.16004v1/ItsAllFunAndGamesUntilMonotonicity.tex`, lines 371–375; game defined lines 59–64 & 120–135)

In the normal-play impartial game **PAP** (*Permutations Avoiding Patterns*) with pattern length $k \ge 1$ starting from $\Sym_n$: a position is a subset $X \subseteq \Sym_n$, and a move chooses a pattern $p \in \Sym_k$ contained in at least one permutation of $X$ and replaces $X$ by $\{\pi \in X : \pi \text{ avoids } p\}$. Here $\sg(\Sym_n, k)$ denotes the Sprague–Grundy value of the starting position $\Sym_n$, and the *reverse strategy* is the move-by-move strategy where Player II replies to any move $p$ by choosing its reverse $p^r$ (the reversal of the one-line word of $p$).

> \begin{conjecture}\label{conj:general-reverse}
>   For every $k \geq 3$, there exists $n_0(k)$ such that the reverse strategy is a winning strategy
>   for Player~II on $\Sym_n$ for all $n \geq n_0(k)$.  In particular, $\sg(\Sym_n,k)=0$ for all such
>   $n$.
> \end{conjecture}

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T09:12:00Z` (start time recorded)
- `tools/novelty_grep.py 2603.16004`: 0 hits across 606 files in `watch/snapshots/**`.
- `gh search issues "2603.16004"` and `gh search prs "2603.16004"`: 0 results. (`gh search code "2603.16004"` hit shared HTTP 429 rate limit at `09:10Z`.)
- `search_web` (`"2603.16004" OR ("Permutations Avoiding Patterns" "reverse strategy")`): returns only `arXiv:2603.16004` itself; no later solution or refutation found.

## Attack-Phase Novelty Receipt & Candidate Deliverables

- Attack-phase live novelty check (`2026-11-27T09:34Z–09:36Z`): **PASS** across 608 watch snapshots, live Zenodo API (0), live arXiv API (`2603.16004v1` only), live GitHub repos/issues/PRs (0), and `search_web` (0); full receipt in `notes/novelty-attack.md`.
- Proof: `PROOF.md` (proves Conjecture 2.9 for all $k \ge 3$ with explicit $n_0(k) = k + ((2k+1)(k-1))^2 + 1$).
- Exact verification: `.venv/bin/python targets/ulfarsson-2603.16004-conj1/verify.py` (`PASS`, zero floats, zero `/` divisions).
