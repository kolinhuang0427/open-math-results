---
source: arXiv:2310.15207v1 (Victor J. W. Guo, "Dwork-type q-congruences through the q-Lucas theorem", 2023-10-23; Section 6, Conjecture 6.8 [conj:8])
status: reported
owner: scout-11
created: 2026-11-27T10:57:46Z
updated: 2026-11-27T11:28:00Z
identifiers:
  - arXiv:2310.15207v1
  - conj:8
---

# Target: Guo (`arXiv:2310.15207v1`), Section 6, Conjecture 6.8

## Verbatim Statement (arXiv:2310.15207v1, `main.tex`, Section 6 "Open problems and concluding remarks", lines 812–818)

Note on numbering: `main.tex` defines `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}` (shared counter with Section 6 `Conjecture 6.1`–`6.8`).

**Conjecture 6.8 (`\label{conj:8}`):**

> Let $m$ and $n$ be positive integers with $n$ odd. Then, modulo $\Phi_n(q)^2$,
> $$\sum_{k=0}^{mn-1}(-1)^k[4k+1]\frac{(q;q^2)_k^3}{(q^2;q^2)_k^3}\,q^{k^2} \equiv (-1)^{(n-1)/2}q^{(n-1)^2/4}[n] \sum_{k=0}^{m-1}(-1)^k(4k+1)\frac{(\frac{1}{2})_k^3}{k!^3}.$$

(Here $(a;q)_k := \prod_{j=0}^{k-1}(1-aq^j)$, $[m] := (1-q^m)/(1-q)$, $(x)_k := x(x+1)\cdots(x+k-1)$, and $\Phi_n(q)$ is the $n$-th cyclotomic polynomial.)

Scope note: As in Conjectures 6.1, 6.2, and 6.4 of the paper, $n>1$ is implicitly intended ($n=1$ has $\Phi_1(q)=q-1$, for which $m=1$ holds trivially while $m=2$ gives $\frac{3}{8} - \frac{15}{16}(q-1) \not\equiv \frac{3}{8} \pmod{(q-1)^2}$). `PROOF.md` proves Conjecture 6.8 unconditionally for all positive integers $m \ge 1$ and all odd integers $n \ge 3$ (and documents the $n=1$ boundary case).

## Gate 1 Novelty Receipt (`2026-11-27T10:58:33Z`)

1. `tools/novelty_grep.py` across `watch/snapshots/**` (635 files): `0` hits for `conj:8`, `Conjecture 6.8`, `q^{k^2}`, `[4k+1]`, `(q;q^2)_k^3/(q^2;q^2)_k^3`, or `2310.15207`.
2. `tools/arxiv_fetch.py abs 2310.15207`: `2310.15207v1` (2023-10-23) is the sole and latest arXiv version; Guo `arXiv:2501.09626v1` checked (`0` mentions).
3. `search_web` for `"2310.15207" "Conjecture 6.8"` and `q^{k^2}`/`(q;q^2)_k^3/(q^2;q^2)_k^3`: only cites `arXiv:2310.15207v1` itself; `watch-5` (`#899`) also confirmed all 3 S2 citing works of `2310.15207v1` / `10.1007/s13398-025-01762-9` are distinct.
