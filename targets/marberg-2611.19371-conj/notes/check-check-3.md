# Check Report — `marberg-2611.19371-conj` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** `tools/.arxiv_cache/eprint/2611.19371v1/involution_pipe_dream_shifted_rpp_arxiv_v1.tex` (Marberg–Morales–Yu, `arXiv:2611.19371v1`):
  - Section 3.3, lines 2865–2890 (`\label{iG-conj}`, $\widehat{\mathrm{kwt}}(D)$, $x_{i\oplus j}$); also Section 1.2, lines 595–604.
  - Section 2.3, lines 1002–1053 ($\partial_i$, $\overline{\partial}_i$, Definition 2.7).
  - Section 1.2 / 3.5, lines 460–505 and 3520–3540 ($\mathsf{InvBPD}_K(z)$, $\ell_{\mathrm{inv}}(z)$, $\mathrm{double}(D)$).
  - Section 7.1, lines 6800–6811 (`\label{iG-conj-cor}`).
- **`TARGET.md` & `PROOF.md` check:** Every quantifier ($n \ge 1$, $z \in I_n$), weight formula $\beta^{|\mathrm{blank}(D)| - \ell_{\mathrm{inv}}(z)} \widehat{\mathrm{kwt}}(D)$, divided-difference characterization, and tile/pipe-dream conventions match the primary source verbatim.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–357:
  - **Section 1 (Change of variables & folded lattice model):** Substitution $u_i = 1 + \beta x_i$ converts $\beta^{\ell_{\mathrm{inv}}(z)} R_z(\beta, \mathbf{x})$ cleanly into $\widetilde{R}_z(\mathbf{u}) \in \mathbb{Z}[u_1,\dots,u_n]$ with bulk vertex $W(u,v)$ satisfying transpose symmetry (5) and diagonal vertex $K(u)$.
  - **Section 2 (Lemma 1):** Unfolding lower-triangle folded states to symmetric bumpless pipe dreams $\mathrm{double}(D)$ and diagonal-by-diagonal Demazure propagation establish $Z(\mathrm{id}, z; \mathbf{u}) = \widetilde{R}_z(\mathbf{u})$ ($z \in I_n$) and $Z(s_i, w; \mathbf{u}) = \sum_{s_i \circ y = w} \widetilde{R}_y(\mathbf{u})$.
  - **Section 3 (Lemmas 2 & 3):** Explicit $0$-Hecke folded $R$-matrices $R(u_1,u_2)$ and $R_V(u_1,u_2)$ satisfy both the Horizontal and Vertical Bulk YBE (20 occupancy patterns across $k \in \{0,1,2,3\}$) and the $2 \times 2$ Diagonal Reflection Equation (16 occupancy patterns across $k \in \{0,1,2,3,4\}$).
  - **Section 4 (Lemma 4):** Three-stage train argument yields (14), cancelling $u_{i+1}$ in Case 1 ($w(i)<w(i+1) \implies \widetilde{R}_w(s_i\mathbf{u}) = \widetilde{R}_w(\mathbf{u})$) and decomposing $F_1 \sqcup F_2 = \{w, y_0\}$ in Case 2 ($w(i)>w(i+1)$) to prove $\overline{\partial}_i R_{s_i \circ z \circ s_i} = R_z$ in $\mathbb{Z}[\beta, x_1,\dots,x_n]$.
  - **Section 5 (Lemma 5 & Induction):** Downward induction on column $k = n, \dots, 1$ proves $|\mathsf{InvBPD}_K(w_0^{(n)})| = 1$ with blank set $\mathrm{iD}(w_0^{(n)})$ and empty upturns; downward induction on $\ell_{\mathrm{inv}}(z)$ proves $R_z = \widehat{\mathfrak{G}}_z^{(\beta)}$ for all $n \ge 1$ and $z \in I_n$ (and $\beta = 1$ recovers Proposition 7.1 `iG-conj-cor`).

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/marberg-2611.19371-conj/notes/check-check-3.py) (pure `int` and `SymPy` polynomial arithmetic in $\mathbb{Z}[u_1, u_2, v]$ and $\mathbb{Z}[\beta, x_1,\dots,x_n]$, `FLOAT_COUNT: 0`).
- Checks performed directly from `involution_pipe_dream_shifted_rpp_arxiv_v1.tex` definitions:
  1. Exhaustive verification of Horizontal and Vertical Bulk YBE (Lemma 2) over all `n = 2` edge color pairs $(a,b) \in [2]^2$ plus 3-color distinct $k = 3$ states.
  2. Exhaustive verification of the $2 \times 2$ Diagonal Reflection Equation (Lemma 3) over all `n = 2` states across $k = 0..4$ plus 4-color distinct $k = 4$ states.
  3. Independent enumeration of symmetric $K$-theoretic bumpless pipe dreams on $[n]\times[n]$ and exact polynomial verification of `iG-conj`, Lemma 5 uniqueness at $w_0^{(n)}$, and Proposition 7.1 (`iG-conj-cor`) for all involutions $z \in I_n$ across $n = 1, 2, 3, 4$.
- Output:
  ```
  [1/3] Checking Horizontal & Vertical Bulk YBE (Lemma 2)...
  [2/3] Checking 2x2 Diagonal Reflection Equation (Lemma 3)...
  [3/3] Checking iG-conj & iG-conj-cor exhaustively for n = 1, 2, 3, 4...
  PASS
  FLOAT_COUNT: 0
  ```
