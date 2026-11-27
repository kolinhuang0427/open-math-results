# reyes-2310.16929-conj3.2

- source: M. A. Reyes, C. Dalfó, and M. A. Fiol, "On the spectra and spectral radii of token graphs", arXiv:2310.16929v1 [math.CO] (2023-10-25), Section 3 (The $k$-algebraic connectivity and $k$-spectral radius), Conjecture 3.2 (`\label{conjec-creix-alfa}`); also published in *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11 (DOI: 10.1007/s40590-023-00583-3)
- status: reported
- owner: scout-9
- updated: 2026-11-27T09:55:17Z
- started: 2026-11-27T09:53:11Z
- identifiers: arXiv:2310.16929v1, 10.1007/s40590-023-00583-3, math.CO, conjec-creix-alfa

## Exact Statement

From `tools/.arxiv_cache/eprint/2310.16929/Spectral_radius_tokens-revision-arXiv.tex`, Section 3 (lines 542–548 `\begin{conjecture}\label{conjec-creix-alfa}`):

> **Conjecture 3.2.** For any graph $G$,
> $$\alpha_1(G)\le \alpha_2(G)\le \cdots \le \alpha_{\lfloor n/2\rfloor}(G).$$

### Primary Definitions (Section 1, lines 182–184; Section 2.1, lines 255–267; Section 3, lines 490–505)

- $G = (V, E)$ is a simple (connected) graph on $n$ vertices.
- For $1 \le k \le n$, the *$k$-token graph* $F_k(G)$ is the graph whose vertex set consists of the $\binom{n}{k}$ subsets of $V(G)$ of size $k$, where two $k$-subsets $A, B$ are adjacent whenever their symmetric difference $A \triangle B = \{a, b\}$ satisfies $\{a, b\} \in E(G)$. By convention $F_0(G) = K_1$ and $F_1(G) \cong G$.
- In Section 3, $\mathrm{sp} F_k(G)$ denotes the multiset of eigenvalues of the Laplacian matrix $L = D - A$ of $F_k(G)$, satisfying $\mathrm{sp} F_0(G) \subset \mathrm{sp} F_1(G) \subset \cdots \subset \mathrm{sp} F_{\lfloor n/2 \rfloor}(G)$ (with multiplicities).
- **Definition 3.1 (lines 502–505):** Given $G$ on $n$ vertices and $1 \le k \le \lfloor n/2 \rfloor$, the *$k$-algebraic connectivity* $\alpha_k(G)$ is the minimum eigenvalue of the multiset difference $\mathrm{sp} F_k(G) \setminus \mathrm{sp} F_{k-1}(G)$.

## Gate 1 Novelty Check

- `tools/novelty_grep.py "2310.16929" "Reyes" "k-spectral radius" "k-algebraic connectivity" "conjec-creix-alfa"`: matched `the-omega-institute/trureturing` (`Library/Eigenstructure/reyes2023tokenspectra.md`, `Problems/reyes-dalfo-fiol-2024-new-laplacian-layer-maxima.md`, `Blueprint/D5/S3/Combinatorics/Graph/TokenGraph/NewLayerMaximaRefutation.lean`), which refutes **Conjecture 3.3** ($\rho_1 \le \rho_2 \le \dots$) and explicitly states: *"The neighboring Conjecture 3.2 concerns minima, and is a different claim."*
- `gh search code "reyes2023tokenspectra"`, `gh search code "conjec-creix-alfa"`, `gh search code "NewLayerMinima" -R the-omega-institute/trureturing`, `gh search issues "2310.16929"`: 0 hits settling Conjecture 3.2.
- `ls targets/`: no prior target for `reyes`, `2310.16929`, or `token` (`dalfo-2609.33718-conj2.4` is unrelated).
- `tools/arxiv_fetch.py query --id-list 2310.16929`: `2310.16929v1` only (2023-10-25).
- Zenodo API (`zenodo.org/api/records?q=2310.16929`): `total: 0`.
- Web search (`"On the spectra and spectral radii of token graphs" "Boletín"`, `"conjec-creix-alfa" OR ("alpha_1" "alpha_2" "alpha_3" "C_6" "token")`, `"k-algebraic connectivity" "token graph"`): confirms published in *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11 (`DOI: 10.1007/s40590-023-00583-3`) retaining Definition 3.1 and Conjecture 3.2, with no refutation of Conjecture 3.2 found.
