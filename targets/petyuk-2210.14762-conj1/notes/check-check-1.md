# Check Report — `petyuk-2210.14762-conj1`

- Checker: `check-1`
- Checked UTC: `2026-11-27T01:45:59Z`
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source: `arXiv:2210.14762v2` (published `2022-10-20T07:50:43Z`, updated `2023-07-12T01:46:41Z`, sole latest version), `tools/.arxiv_cache/eprint/2210.14762/simplified_de_Bruijn_graphs__4_.tex`:
  - Section 1.1 (lines 50–51, 61): definition of letter alternation, word-representable graph, and `Theorem 2` (`\label{3-col}`: every $3$-colorable graph is word-representable).
  - Section 1.2 (lines 65–67): definition of $B(n,k)$ and simplified de Bruijn graph $S(n,k)$ (simple graph obtained from $B(n,k)$ by removing orientations and loops and replacing multiple edges by a single edge).
  - Section 4 (line 123, Conjecture 1): `$S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$.`
- Comparison against `TARGET.md` and `COUNTEREXAMPLE.md`: exact verbatim match with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Verification

- Verifier script: `targets/petyuk-2210.14762-conj1/notes/check-check-1.py` (written strictly from Petyuk's Section 1 definitions and `COUNTEREXAMPLE.md`, without reading `verify.py` or `notes/`).
- Verified directly:
  1. $S(4, 3)$ constructed from $B(4, 3)$ has $81$ vertices, $237$ undirected edges, contains triangle `0010–0100–1001`, and the $9$-row lookup function $f: \mathbb{Z}_3^3 \to \{0,1,2\}$ satisfies $f(d_1,d_2,d_3) \not\equiv d_1 + f(d_2,d_3,d_4) \pmod 3$ on all $80$ nonzero tuples in $\mathbb{Z}_3^4 \setminus \{0\}$, giving a proper $3$-coloring $c$ with $|A_0|=|A_1|=|A_2|=27$ on all $237$ edges.
  2. Explicit representing word $w$ of length $4536$ ($M=28$ rounds $\times 3 \times 54$, verified both for lexicographic and for an arbitrary shuffled ordering of each $A_i$) satisfies the exact alternation property on ALL $\binom{81}{2} = 3240$ vertex pairs $\{u, v\}$: $u$ and $v$ alternate in $w$ if and only if $uv \in E(S(4,3))$.

### Command & Raw Output

```bash
.venv/bin/python -u targets/petyuk-2210.14762-conj1/notes/check-check-1.py
```

Raw output (exit code `0`):
```text
S(4,3) (81 vertices, 237 edges), triangle, 80 nonzero tuples, & 3-coloring (27/27/27): OK
Explicit representing word (len=4536, M=28, lex order) across all 3240 pairs: OK
Explicit representing word (arbitrary shuffled class order) across all 3240 pairs: OK
PASS
```
