# Independent Check Report: targets/biswas-2603.04876-conj5.5/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2603.04876v1` (`2026-03-05T07:05:37Z`, sole version), *"Lattice points arising from regularity and $\mathrm{v}$-number of Graphs: Whisker and Cameron-Walker"* by Prativa Biswas, Mousumi Mandal, and Kamalesh Saha, cached TeX source `tools/.arxiv_cache/eprint/2603.04876/Arxiv.tex`.
- **Exact definitions & conjecture match:**
  - Section 1 (`\newcommand{\N}{\mathbb{N}}`, lines 104, 250–262): $\mathbb{N} = \{1,2,3,\dots\}$, $\mathcal{RV}(n) = \{(\mathrm{reg}(R/I(G)), \mathrm{v}(I(G))) : G \text{ connected on } n \text{ vertices}\}$.
  - Section 2 (`Arxiv.tex` lines 293, 303–346):
    - Definition 2.4 (`\label{def:v}`): $\mathrm{v}(G) = \min\{|A| : A \text{ independent and } N_G(A) \text{ is a vertex cover of } G\}$.
    - Definition 2.5 (line 311): chordal iff no induced cycle of length $> 3$.
    - Proposition 2.9 (`\label{prop:reg<n/2}`): $\mathrm{reg}(G) < n/2$ for connected $G$ on $n \ge 3$.
    - Theorem 2.11 (`\label{thm:reg chordal}`, citing Hà–Van Tuyl Cor. 6.9): $\mathrm{reg}(G) = \mathrm{im}(G)$ for every chordal graph $G$.
  - Section 3 (`\label{thm:RV(n)}`, lines 380–381): $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$.
  - Section 5 (*Future Directions*, lines 975–983), Conjecture 5.5:
    > For the class of connected chordal graphs on $n\geq 3$ vertices, we have
    > $$\mathcal{RV}_{\mathrm{chordal}}(n)=\left\{(r,v)\in \mathbb{N}^{2} \mid 1\leq r<\frac{n}{2}, 1\leq v\leq r-\left\lceil\frac{r}{n-2r}\right\rceil+1\right\}.$$
- **Fidelity:** `TARGET.md` and `PROOF.md` match `arXiv:2603.04876v1` verbatim with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical & Mathematical Check

- Independently wrote `targets/biswas-2603.04876-conj5.5/notes/check-check-3.py` (strictly without reading `verify.py` or `notes/*`), verifying using exact integer / set / graph-theoretic algorithms:
  1. **Exhaustive connected chordal graphs (`n = 3..7`):** Enumerated all `352` non-isomorphic connected chordal graphs (`{3: 2, 4: 5, 5: 15, 6: 58, 7: 272}`, with `n <= 6` cross-checked against all $2^{\binom{n}{2}}$ labeled graphs). Verified Lemmas 1–5 (including simplicial roots `R = N_G[s]` for *every* simplicial vertex `s`, clique-tree axioms, Lemma 4 greedy bottom-up cover & induced matching, Lemma 5 clique cover hitting $X$ including Subcase B2) and Theorem 1 (`im(G - N_G[x*]) <= r - ceil(r/(n-2r))`, `v(G) <= r - ceil(r/(n-2r)) + 1`), confirming exact equality $\mathcal{RV}_{\mathrm{chordal}}(n) = A(n)$ for $3 \le n \le 7$.
  2. **Part 2 reverse witnesses (`n = 3..11`):** Constructed the explicit Case I (`m >= r`) and Case II (`m < r`) connected chordal witnesses for all `42` lattice points $(r, v) \in A(n)$, verifying connectedness, chordality, exact `im(G) == r`, and exact `v(G) == v`.
  3. **Larger stress tests (`n = 8..14`):** Generated `84` connected chordal graphs by random simplicial attachment and verified Lemmas 1–5 and Theorem 1 on all of them.

- **Command run:**
```bash
.venv/bin/python -u targets/biswas-2603.04876-conj5.5/notes/check-check-3.py
```

- **Raw output:**
```text
Exhaustive n=3..7 PASS: checked 352 non-isomorphic connected chordal graphs {3: 2, 4: 5, 5: 15, 6: 58, 7: 272}; RV_chordal(n)==A(n) exact.
Part 2 PASS: constructed and verified exact (im, v) for all 42 lattice points in A(3..11).
Large Stress PASS: 84 connected chordal graphs on n=8..14 verified against Lemmas 1-5 & Thm 1.
PASS
```
