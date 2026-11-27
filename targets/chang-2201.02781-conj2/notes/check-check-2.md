# Independent Check Report: `targets/chang-2201.02781-conj2/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2201.02781v1` (Yuhong Chang, Chao Yang, Yujun Yin, Bing Yao, *"An extension on neighbor sum distinguishing non-proper total coloring of graphs"* — confirmed sole/latest version via `tools/arxiv_fetch.py query --id-list 2201.02781`), TeX file `tools/.arxiv_cache/eprint/2201.02781/An_extension_on_nsdt-_coloring_of_graphs-arXiv.tex`.
  - `arXiv:2303.02611v4` (Ralph Keusch, *"A Solution to the 1-2-3 Conjecture"*, *J. Combin. Theory Ser. B* 166, 2024 — confirmed latest version via `tools/arxiv_fetch.py query --id-list 2303.02611`), TeX file `tools/.arxiv_cache/eprint/2303.02611/123ConjectureRevisedVersion.tex`.
- **Exact sections/lines verified:**
  - `An_extension_on_nsdt-_coloring_of_graphs-arXiv.tex` lines 125–162:
    - Line 125: finite, undirected, simple, and connected graphs.
    - Lines 146–151 (Definition 1): $f: V(G)\cup E(G) \to [1, k]$ non-proper $k$-total coloring, $\phi(x) = f(x) + \sum_{e \ni x} f(e) + \sum_{y \in N(x)} f(y)$, conflict-free iff $\phi(x) \ne \phi(y)$ for all $xy \in E(G)$; $\mathrm{fgndi}_{\sum}(G)$ is the minimum such $k$.
    - Lines 156–162 (Conjecture 2): $K_2$ admits no NFSD-total coloring; for every connected graph $G \ne K_2$ (equivalently $|V|=1$, trivially $\mathrm{fgndi}_{\sum}(K_1)=1$, or $|V|\ge 3$), $\mathrm{fgndi}_{\sum}(G) \le 3$.
  - `123ConjectureRevisedVersion.tex` lines 111–418: Lemmas 1–6 (`lemma:divide`, `lemma:weighting`, `lemma:flow`, `lemma:edgesbetween`, `lemma:basicsituation`, `lemma:remainingvertex`, `lemma:rearranging`, `lemma:blocks`) and main case split.
- **Comparison with `TARGET.md` and `PROOF.md`:**
  - `TARGET.md` Definition 1 and Conjecture 2 match `arXiv:2201.02781v1` verbatim.
  - `PROOF.md` reduces Conjecture 2 for $|V|\ge 3$ by setting $f(v) \equiv 2$, yielding $\phi(x) = c(x) + s_\omega(x)$ with even offsets $c(x) = 2 + 2\deg_G(x) \in 2\mathbb{Z}_{\ge 1}$, and proves Theorem 1 (Even-Offset 1-2-3 Theorem) by tracking $c(v)$ explicitly through Lemmas 1–8 and Cases 1–4. Every quantifier, parity check ($h(v) \ge 2$ guarantees positive odd sets $S(v_i)$ in Lemma 3), edge-modification offset ($c'(y)=c(y)+2$ in Case 1, $c'(z_y)=c(z_y)+2$ in Case 2 even with $z_x=z_y$, $c'(q)=c(q)+2$ in Case 3 joint $q$), and connectivity check matches rigorously.

## 2. Independent Mechanical Check

Written independently from `arXiv:2201.02781v1`, `arXiv:2303.02611v4`, and `PROOF.md` (without reading `verify.py` or any author `notes/`), implementing every constructive step of Lemmas 1–8 and Cases 1–4 in exact integer arithmetic:

- **Script:** `targets/chang-2201.02781-conj2/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/chang-2201.02781-conj2/notes/check-check-2.py
  ```
- **Raw output (exit code 0):**
  ```text
  Sanity check K_2 impossible (all 27 3-colorings fail) & K_1 trivial: PASS
  Exhaustive n=3 (4 labeled connected graphs x 3 offset functions): PASS
  Exhaustive n=4 (38 labeled connected graphs x 3 offset functions): PASS
  Exhaustive n=5 (728 labeled connected graphs x 3 offset functions): PASS
  Exhaustive n=6 (26704 ALL labeled connected graphs, Def 1 f(v)=2): PASS
  Larger & structured graphs (283 graphs n=7..16 x 3 offsets): PASS
  Proof cases triggered (18): ['C1_even', 'C1_odd', 'C2_Beven_zyB', 'C2_Beven_zyR', 'C2_Bodd_zyB', 'C2_Bodd_zyR', 'C3_Bodd_degRx0', 'C3_Bodd_degRx_ge2', 'C3_Bodd_degRy0', 'C3_Bodd_degRy_ge2', 'C3_Bodd_disjoint_zyB', 'C3_Bodd_disjoint_zyR', 'C3_Bodd_joint_q', 'C4_Beven_Rx0_L6y', 'C4_Beven_Rx0_Ry0', 'C4_Beven_Rx0_tilde', 'C4_Beven_Ry0', 'C4_Beven_bothR']
  Lemma 6/7 sub-branches triggered (6): ['L6_i_gt_kx_x_lt_k', 'L6_i_le_kx', 'L6_x_eq_k', 'L7_11', 'L7_31', 'L7_33']
  PASS (all constructive proof & Conjecture 2 checks passed in 10.995s)
  ```

## 3. Gate 2 & Contest Status

- **Gate 2 receipts present:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md` (all PASS).
- **Contested status:** No `CONTESTED.md` present.
