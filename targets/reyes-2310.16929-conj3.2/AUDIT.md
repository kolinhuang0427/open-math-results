# Blind Adversarial Audit Report: `targets/reyes-2310.16929-conj3.2/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T10:13Z`
- **Verdict:** **PASS**
- **Files Audited (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2310.16929/Spectral_radius_tokens-revision-arXiv.tex` (`arXiv:2310.16929v1`), `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (`arXiv:2310.16929v1` / *Bol. Soc. Mat. Mex.* 30 (2024), Art. 11)

- **Latest Version Check:** Live arXiv query (`tools/arxiv_fetch.py query --id-list 2310.16929`) confirms `2310.16929v1` (`2023-10-25`, M. A. Reyes, C. Dalfó, and M. A. Fiol, *"On the spectra and spectral radii of token graphs"*) is the sole arXiv version; published in *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11 (`DOI: 10.1007/s40590-023-00583-3`).
- **Numbering Check (`Spectral_radius_tokens-revision-arXiv.tex`):** All theorem-like environments (`theorem`, `proposition`, `lemma`, `corollary`, `conjecture`, `definition`, etc.) share the `[theorem]` counter per `\section` (L18–28). In Section 3 (`\section{The $k$-algebraic connectivity and $k$-spectral radius}`, L487):
  - L502–505: **Definition 3.1** ($\alpha_k(G), \rho_k(G)$ as minimum and maximum eigenvalues of the **multiset** $\mathrm{sp} F_k(G) \setminus \mathrm{sp} F_{k-1}(G)$ for Laplacian $L = D - A$).
  - L542–548: **Conjecture 3.2** (`\label{conjec-creix-alfa}`): *"For any graph $G$, $\alpha_1(G) \le \alpha_2(G) \le \cdots \le \alpha_{\lfloor n/2 \rfloor}(G)$."*
  - L557–562: Conjecture 3.3 ($\rho_1(G) \le \rho_2(G) \le \cdots \le \rho_{\lfloor n/2 \rfloor}(G)$, which is distinct and was refuted elsewhere in `the-omega-institute/trureturing`).
- **Verbatim Match & Graph Class:** `TARGET.md` and `COUNTEREXAMPLE.md` match Section 1 (L171, L182–184), Section 2.1 (L255, L263), and Section 3 (L490–505, L542–548) verbatim. The counterexample $G = C_6$ is simple, connected, 2-regular, bipartite, distance-regular, and vertex-transitive (satisfying every possible standing graph assumption in the paper; notably the paper itself tested $P_6$ and $C_7$ on L509–522 and skipped $C_6$).

---

## 2. Adversarial Verification of the Counterexample ($G = C_6$)

- **Exact Laplacian Characteristic Polynomials:** Re-ran `.venv/bin/python targets/reyes-2310.16929-conj3.2/notes/check-check-1.py` directly (exit code `0`, `FLOAT_CONSTANTS: 0` by AST check; pure SymPy `ZZ` matrices and `ZZ[x]` polynomials):
  - $P_0(x) = x$,
  - $P_1(x) = x(x-1)^2(x-3)^2(x-4) \implies Q_1(x) = P_1/P_0 = (x-1)^2(x-3)^2(x-4) \implies \alpha_1(C_6) = 1$,
  - $Q_2(x) = P_2/P_1 = (x-2)(x-5)^2(x^2-10x+20)(x^2-7x+8)^2 \implies \alpha_2(C_6) = \frac{7 - \sqrt{17}}{2} \approx 1.4384471\dots$,
  - $Q_3(x) = P_3/P_2 = (x-4)^2(x-6)(x^2-10x+12) \implies \alpha_3(C_6) = 5 - \sqrt{13} \approx 1.3944487\dots$.
- **Robustness to Multiset vs. Set Difference:** Neither $\alpha_2(C_6) = \frac{7-\sqrt{17}}{2}$ nor $\alpha_3(C_6) = 5 - \sqrt{13}$ lies in any lower token-graph spectrum ($x^2-7x+8 \nmid P_1$ and $x^2-10x+12 \nmid P_2$). Thus $C_6$ refutes Conjecture 3.2 under **both** multiset difference (as stated in Definition 3.1) and set difference.
- **Pure Integer Inequality Proof (`COUNTEREXAMPLE.md` L47–53):** Verified step by step:
  $$5 - \sqrt{13} < \frac{7-\sqrt{17}}{2} \iff 3 + \sqrt{17} < 2\sqrt{13} \iff 26 + 6\sqrt{17} < 52 \iff 3\sqrt{17} < 13 \iff 153 < 169.$$
- **Auxiliary Minimality Remark (`COUNTEREXAMPLE.md` L11):** Independently verified across all $1{,}245$ graphs in `nx.graph_atlas_g()` on $4 \le n \le 7$ vertices (both connected and disconnected): $C_6$ (`G105`) is indeed the unique counterexample on $4 \le n \le 7$ vertices.

---

## 3. Raw Verifier Output & Gate 2 Novelty

- **Verifier Command:** `.venv/bin/python targets/reyes-2310.16929-conj3.2/notes/check-check-1.py` (exit code `0`):
  ```text
  alpha_1(C_6) = 1
  alpha_2(C_6) = 7/2 - sqrt(17)/2 = 7/2 - sqrt(17)/2
  alpha_3(C_6) = 5 - sqrt(13) = 5 - sqrt(13)
  Strict inequality alpha_3(C_6) < alpha_2(C_6): True
  PASS
  ```
- **Gate 2 Novelty Receipts:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, and `notes/novelty-gate2-watch-6.md` all report **PASS** (`the-omega-institute/trureturing` explicitly refutes Conjecture 3.3 on $\rho_k$ maxima only and notes Conjecture 3.2 is a distinct claim; `watch-5` inspected all $7$ Semantic Scholar citing papers including `2610.00500v1` `main.tex`, finding zero resolutions of Conjecture 3.2).

**Conclusion:** Counterexample $G = C_6$ is elementary, exact, completely rigorous, and independently verified. Ready for Gate 3 freshness check (`<1h`) before reporting.

---

## 4. Independent Lean 4 Statement-Fidelity Audit (`2026-11-27T12:01Z`) — **PASS**

- **Auditor:** `audit-3` (`auto`)
- **Lean Module:** `lean/OpenMath/Reyes231016929Conj32.lean` (imported on L23 of `lean/OpenMath.lean`)
- **Charter Label:** `machine-checked counterexample in Lean 4`
- **Primary-Source Fidelity (`arXiv:2310.16929v1` / *Bol. Soc. Mat. Mex.* 30 (2024), Art. 11, `Spectral_radius_tokens-revision-arXiv.tex` L171, L182–184, L255–267, L490–505, L542–548):**
  - `tokenGraph G k` defines adjacency on $k$-subsets via `∃ a b, G.Adj a b ∧ symmDiff A.1 B.1 = {a, b}`, which is strictly equivalent to requiring `a ∈ A.1 ∧ b ∈ B.1` since $|A| = |B| = k$ and $a \ne b$ force $|A \setminus B| = |B \setminus A| = 1$ and $G.\mathrm{Adj}$ is symmetric; at $k = 0$, `tokenGraph G 0 ≅ K_1` as stipulated on L490.
  - `laplacianMatrix` is literally $L = D - A$; `laplacianSpec`, `newLayerSpec`, and `algConnK` faithfully encode the multiset difference $\mathrm{sp} F_k(G) \setminus \mathrm{sp} F_{k-1}(G)$ and its minimum $\alpha_k(G)$ from Definition 3.1 (and for $C_6$ at $k = 1, 2, 3$ the multiset difference is proved nonempty, so the `0` fallback is never hit).
  - `C6` is the simple 6-cycle on `Fin 6`, proved connected (`C6_connected`), with exact Laplacian characteristic polynomials `charpoly_C6_token0`..`charpoly_C6_token3`, exact `algConnK_C6_one` ($= 1$), `algConnK_C6_two` ($= (7 - \sqrt{17})/2$), `algConnK_C6_three` ($= 5 - \sqrt{13}$), `alpha3_lt_alpha2_C6`, `refutes_reyes_conjecture_3_2_C6`, and `not_reyes_conjecture_3_2` directly negating Conjecture 3.2 (`\label{conjec-creix-alfa}`) even when restricted to connected simple graphs.
- **Type-Check & Axiom Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Reyes231016929Conj32.lean`
  - Exit code: `0`, zero warnings, zero `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern` (sole occurrence of `native_decide` is in the L30 docstring comment).
  - `#print axioms` strictly `[propext, Classical.choice, Quot.sound]` for all 9 main theorems (`charpoly_C6_token0`..`charpoly_C6_token3`, `algConnK_C6_one`..`algConnK_C6_three`, `refutes_reyes_conjecture_3_2_C6`, `not_reyes_conjecture_3_2`).
