---
source: arXiv:2310.15207v1 (Victor J. W. Guo, "Dwork-type q-congruences through the q-Lucas theorem", 2023-10-23; Section 6, Conjecture 6.4 [conj:4], and Conjecture 6.3 [conj:3] / Section 2 Lemma 2.3 [lem:3])
status: reported
owner: scout-11
created: 2026-11-27T10:45:10Z
updated: 2026-11-27T10:48:20Z
identifiers:
  - arXiv:2310.15207v1
  - conj:4
  - conj:3
  - lem:3
---

# Target: Guo (`arXiv:2310.15207v1`), Section 6, Conjecture 6.4 (and Conjecture 6.3)

## Verbatim Statement (arXiv:2310.15207v1, `main.tex`, Section 6 "Open problems", lines 746–760)

Note on numbering: `main.tex` defines `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}` (shared counter with Section 6 `Conjecture 6.1`, `6.2`, `6.3`, `6.4`, ...).

**Conjecture 6.4 (`\label{conj:4}`):**

> Let $n\equiv 1\pmod{4}$ be an integer greater than $1$ and let $r,s$ be positive integers with $r>s$. Then, modulo $\Phi_{n^s}(q)^2$,
> $$\frac{(q;q^2)_{(n^r-1)/4} (q^{2n};q^{2n})_{(n^{r-1}-1)/4} }{(q^2;q^2)_{(n^r-1)/4} (q^{n};q^{2n})_{(n^{r-1}-1)/4}} \equiv \frac{(q;q^2)_{(n^s-1)/4} (q^{2n};q^{2n})_{(n^{s-1}-1)/4} }{(q^2;q^2)_{(n^s-1)/4} (q^{n};q^{2n})_{(n^{s-1}-1)/4}}.$$

**Companion Conjecture 6.3 (`\label{conj:3}`, also proved in `PROOF.md`):**

> We believe that Lemma \ref{lem:3} can be strengthened as follows.
>
> **Conjecture 6.3.** The $q$-congruence \eqref{eq:lem3} holds modulo $\Phi_{n^s}(q)^2$.

where Lemma 2.3 (`\label{lem:3}`, `main.tex` lines 273–284) states for integers $n \equiv 1 \pmod{4}$ ($n > 1$ for $r>s\ge 1$) and $r > s \ge 1$ that equation `\eqref{eq:lem3}` is:
$$[n]\frac{(q^3;q^4)_{(n^r-1)/2} (q^{5n};q^{4n})_{(n^{r-1}-1)/2} }{(q^5;q^4)_{(n^r-1)/2} (q^{3n};q^{4n})_{(n^{r-1}-1)/2}} \equiv [n]\frac{(q^3;q^4)_{(n^s-1)/2} (q^{5n};q^{4n})_{(n^{s-1}-1)/2} }{(q^5;q^4)_{(n^s-1)/2} (q^{3n};q^{4n})_{(n^{s-1}-1)/2}}.$$

(Here $(a;q)_m := \prod_{k=0}^{m-1}(1-aq^k)$, $[n] := (1-q^n)/(1-q)$, and $\Phi_m(q)$ denotes the $m$-th cyclotomic polynomial.)

## Gate 1 Novelty Receipt (`2026-11-27T10:45:10Z` – `10:48:00Z`)

1. `tools/novelty_grep.py` across `watch/snapshots/**` (619–635 files): `0` matches for `2310.15207`, `(q;q^2)_{(n^r-1)/4}`, `(q^3;q^4)_{(n^r-1)/2}`, `q^{5n};q^{4n}`, or Guo's Conjecture 6.3 / 6.4.
2. `tools/arxiv_fetch.py abs 2310.15207`: `2310.15207v1` (2023-10-23) is the sole and latest version on arXiv.
3. `tools/arxiv_fetch.py query` on Victor J. W. Guo 2023–2026: returned `2501.09626v1` (Guo 2025, checked `.tex` source via `arxiv_fetch.py`: `0` occurrences of `2310.15207`, `\Phi_{n^s}(q)^2`, `conj:3`, or `conj:4`).
4. `search_web` for `"2310.15207"`, `"Conjecture 6.3"`, `"Conjecture 6.4"`, `"Victor J. W. Guo" "Phi_{n^s}(q)^2"`: only points back to `arXiv:2310.15207v1` itself; no subsequent resolution found.
