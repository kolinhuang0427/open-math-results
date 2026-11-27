# Target: kallat-2610.40342-ques14.8

- source: arXiv:2610.40342v1 (Ahaan Kallat, "A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths", October 2026), Section 14 (`\label{sec:open}`), Question 14.8 (`\label{prob:composite}`, lines 1212–1214; with Section 13 Definition 13.1 `\label{def:types}` and Lemma 13.2 `\label{lem:typeB}`, lines 1011–1025)
- status: reported
- owner: scout-10
- updated: 2026-11-27T10:15:00Z
- started: 2026-11-27T10:14:00Z
- identifiers: 2610.40342, 2610.40342v1, Ahaan Kallat, Question 14.8, prob:composite, valuation calculus, restricted cycle lengths, type II prime, least period

## Exact statement
From Section 14 (`\label{sec:open}`), lines 1212–1214 of `paper1_valuation_calculus.tex` in `arXiv:2610.40342v1`:

> **Question 14.8** (Least periods at primes of type II).
> Section~\ref{sec:composite} gives the set of $n$ with $m\mid a_A(n)$ and its density. Is the least period of $a(n)\bmod p^e$ at a prime of type~II always $p^e$, or $2p^e$ when the sign of Lemma~\ref{lem:typeB}(a) is $-$? This holds in every case we computed. The natural approach shows $a(p^{e-1})\not\equiv1\pmod{p^e}$, which needs a second-order shift congruence, while the residue formulas behind Theorem~\ref{thm:dichotomy} give $a(p^e)\bmod p^e$ only, and the interpolation of Theorem~\ref{thm:interp} controls valuations and not residues.

Context from Section 13 (`\label{sec:composite}`): for any set $A \subseteq \mathbb{N}$, $a(n) = a_A(n)$ counts permutations of $\{1,\dots,n\}$ all of whose cycle lengths lie in $A$ (exponential generating function $\exp(\sum_{m\in A} x^m/m)$), and a prime $p$ is of **type II** for $A$ if $[1 \in A] \ne [p \in A]$ (`\label{def:types}`). Lemma 13.2(a) (`\label{lem:typeB}`) states:
> For every $e\ge1$ and $n\ge0$ one has $a(n+p^e)\equiv\pm a(n)\pmod{p^e}$. For odd $p$ the sign is $+$ when $1\in A$, $p\notin A$, and $-$ when $1\notin A$, $p\in A$. For $p=2$ the sign is $+$ except for $e=2$, where it is $(-1)^{[2\in A]+[4\in A]}$.

## Gate 1 novelty receipt
- Checked `targets/` on 2026-11-27T10:11Z: no existing `kallat` or `2610.40342` target.
- Ran `.venv/bin/python tools/novelty_grep.py "2610.40342" "valuation calculus" "3x2^{k+2}" "lfloor 7(k+1)/2"`: `# 0 lines across 0/618 files in 3.06s`.
- Ran `.venv/bin/python tools/novelty_grep.py "Ahaan Kallat" "prop:globalgcd" "Lambda_r" "g_r(n)"`: 4 unrelated substring matches (`Lambda_r`, `g_r(n)`), 0 hits for Ahaan Kallat or `2610.40342`.
- Ran `gh search repos "2610.40342"` (`no repositories matched`), `gh search issues "2610.40342"` (only automated `bguanmath/ArXiv_*` digests), Zenodo API `q=2610.40342` (`total: 0`), `search_web` (`"2610.40342"`, confirms `arXiv:2610.40342v1` is latest version, no external solution found).
