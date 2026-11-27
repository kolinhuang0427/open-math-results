# Independent Check Report: `bui-2508.04602-conj8.1`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2508.04602/article.tex` (`arXiv:2508.04602v1`, Section 8.2 *Matching Problem and Acyclicity of State Graph*, `lines 1188–1212`):
  - Point set $Q$ in general position with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$ (which forces $n \ge 3$), hull vertices $Q_1, \dots, Q_n$ in cyclic order, interior points $B_1, \dots, B_n$.
  - State graph $G$ on $S_n$ with directed edge $\pi \to \rho$ for swapping $i \neq j$ when $T_i(\pi)$ and $T_j(\pi)$ intersect (nontrivially, i.e., beyond a shared hull vertex in $\{Q_i, Q_{i+1}\} \cap \{Q_j, Q_{j+1}\}$).
  - Conjecture (`lines 1194–1196, 1211`): the algorithm terminates / $G$ is acyclic for all order types $Q$ in general position; `PROOF.md` also verifies the parenthetical remark (`lines 1208–1209`) that post-swap triangles do not intersect.

## 2. Proof & Independent Mechanical Verification
- Checked all steps in `PROOF.md`:
  - **Lemma 1:** General position (no 3 collinear) + $B_a \neq B_b$ ensures boundary intersection outside shared hull vertices occurs only at transverse crossings $\mathrm{relint}(e_i) \cap \mathrm{relint}(e_j)$ with $\overline{e_i} \neq \overline{e_j}$, giving $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$.
  - **Lemma 2:** $\ell_k(X) = \det(Q_{k+1} - Q_k, X - Q_k)$ is affine, vanishes on $Q_k, Q_{k+1}$, and is strictly positive on $B_r$ and all $Q_m$ ($m \notin \{k, k+1\}$); for $i \neq j$ ($n \ge 3$), $\ell_j(Q_i), \ell_j(Q_{i+1}) \ge 0$ with $\ell_j(Q_i) + \ell_j(Q_{i+1}) > 0$.
  - **Lemma 3 & Theorem:** Barycentric expansion of $Z \in \mathrm{int}(T_i(\pi)) \cap \mathrm{int}(T_j(\pi))$ yields $\ell_i(Z)/\ell_j(Z) < \ell_i(B_{\pi_i})/\ell_j(B_{\pi_i})$ and $\ell_j(Z)/\ell_i(Z) < \ell_j(B_{\pi_j})/\ell_i(B_{\pi_j})$, forcing $\ell_i(B_{\pi_j})\ell_j(B_{\pi_i}) < \ell_i(B_{\pi_i})\ell_j(B_{\pi_j})$ and hence $\Phi(\rho) < \Phi(\pi)$ strictly (and $T_i(\rho), T_j(\rho)$ non-intersecting).
- Wrote independent exact-integer verifier `targets/bui-2508.04602-conj8.1/notes/check-check-1.py` (pure `int` orientation predicates, zero floats, without reading `verify.py`).
- Command: `.venv/bin/python targets/bui-2508.04602-conj8.1/notes/check-check-1.py`
- Results (`PASS`):
  - Verified 34 general-position integer point sets across $n=3$ (10), $n=4$ (10), $n=5$ (8), $n=6$ (4), $n=7$ (2) in random, clustered, and double-circle-like geometries.
  - Exhaustively checked all $S_n$ states and all $96,940$ directed swap edges: Lemma 2(1)–(4), Lemma 3 inequality, post-swap non-intersection, and strict decrease $\Phi(\rho) < \Phi(\pi)$ held on every edge, with $\ge 1$ sink per instance.

## 3. Gate 2 Novelty Status
- Gate 2 `watch-1` passed (`notes/novelty-gate2-watch-1.md`); `watch-5`/`watch-6` Gate 2 requested in #150.
