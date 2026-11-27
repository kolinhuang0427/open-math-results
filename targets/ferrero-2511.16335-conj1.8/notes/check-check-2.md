# Independent Check Report: `targets/ferrero-2511.16335-conj1.8/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2511.16335v1` (confirmed latest version via `tools/arxiv_fetch.py query --id-list 2511.16335`), TeX file `tools/.arxiv_cache/eprint/2511.16335/NewFixedPropTime.tex`.
- **Exact sections/lines verified:**
  - Section 1, Definition 1.2 (line 231): $\overline{\mathrm{PT}}(G)$ is the maximum propagation time of any minimal standard zero forcing set of $G$.
  - Section 1, Definition 1.5 (lines 272–276): A graph $G$ of order $n \ge 2$ is a *standard fast join* iff $G \cong K_n$ or $G = \bigvee_{i=1}^t G_i$ with $t \ge 2$ and each $G_i \cong n_i K_1$ or $G_i \cong K_{n_i} \dot{\cup} K_{m_i}$ ($n_i, m_i \ge 2$).
  - Section 1, Conjecture 1.8 (`\label{c:std}`, lines 293–296): "Let $G$ be a connected graph. If $\overline{\mathrm{PT}}(G)=1$, then $G$ is a standard fast join."
  - Section 1, lines 312, 319–326: Standard zero forcing rule CCR-$\mathbb{Z}$ (simultaneous rounds $B^{(i+1)}$, propagation time $\mathrm{pt}(G, B) = \max \{p : B^{(p)} \ne \emptyset\}$).
- **Comparison with `TARGET.md` and `COUNTEREXAMPLE.md`:** Word-for-word match with `NewFixedPropTime.tex`; zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

Written independently from the primary-source definitions and the explicit witness in `COUNTEREXAMPLE.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py
  ```
- **Raw output:**
  ```text
  Circ(12, {1, 5}): {'n': 12, 'num_forcing': 361, 'num_minimal': 144, 'Z': 8, 'Zbar': 8, 'pt_ul': 1, 'pt_bar': 1, 'proper_forcing_pts': {1}}
  C_6[2, 2, 2, 2, 2, 2] (n=12): Z=8, Zbar=8, pt_ul=1, pt_bar=1, num_min=144
  C_6[3, 2, 2, 2, 2, 2] (n=13): Z=9, Zbar=9, pt_ul=1, pt_bar=1, num_min=192
  C_6[2, 3, 2, 3, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=252
  C_6[3, 2, 3, 2, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=252
  C_6[4, 2, 2, 2, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=240
  C_6[3, 3, 2, 3, 2, 2] (n=15): Z=11, Zbar=11, pt_ul=1, pt_bar=1, num_min=336
  PASS (all checks passed in 0.454s)
  ```

## 3. Summary of Verified Properties

1. `Circ(12, {1, 5})` has the exact same edge set as $C_6[2K_1]$ with parts $A_i = \{i, i+6\}$, is connected, 4-regular, bipartite, with 24 edges ($G \not\cong K_{12}$).
2. $\overline{G}$ is connected (so $G$ is not a nontrivial join of $t \ge 2$ nonempty graphs), hence $G$ fails Definition 1.5 of a standard fast join.
3. Exhaustive evaluation of all $2^{12} = 4096$ subsets confirms 361 forcing sets, 144 minimal forcing sets, $\mathbb{Z}(G) = \overline{\mathbb{Z}}(G) = 8$, $\underline{\mathrm{PT}}(G) = \overline{\mathrm{PT}}(G) = 1$, and every proper forcing set has $\mathrm{pt}(G, B) = 1$.
4. Exhaustive verification on six parameter tuples $(r_0,\dots,r_5)$ with $r_i \ge 2$ up to $n=15$ confirms $\overline{\mathrm{PT}} = \underline{\mathrm{PT}} = 1$, $\mathbb{Z} = \overline{\mathbb{Z}} = n - 4$, connectedness of both $G$ and $\overline{G}$, and failure of Definition 1.5, matching the infinite-family proof in `COUNTEREXAMPLE.md`.
