# Independent Check Report: `targets/orzechowski-2611.34308-q3.9`

- **Verdict:** **PASS**
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/orzechowski-2611.34308-q3.9/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` / `sympy.QQ` only)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2611.34308/Measurable-equidecompositions-in-Q_p_n.tex` (Kamil Orzechowski, *Measurable equidecomposability and the Banach--Ruziewicz problem over locally compact non-Archimedean valued fields*, `arXiv:2611.34308v1`).
- Confirmed `TARGET.md` reproduces **Question 3.9** (`\label{q:prime_residue_field}`, lines 621–623) and the primary definitions verbatim:
  - Locally compact non-Archimedean valued fields & `[UC, Corollary 12.2]` (lines 159–171).
  - Domain of expansion (`Definition 2.8`, `\label{def:domain_of_exp}`, lines 321–334), expanding action (`Definition 2.10`, `\label{def:expanding_action}`, lines 342–344), `Remark 2.11` (`\label{rem:expanding_one_set}`, lines 346–349), local spectral gap (`Definition 2.13`, `\label{def:local_spectral_gap}`, lines 359–367), metric invariance of Haar measure (`[Christensen, Theorem 1]`, line 386), Salehi Golsefidy's theorem (`Theorem 2.15`, `\label{thm:Golsefidy's_theorem}`, lines 393–398), and `Lemma 2.16` (`\label{lem:LSG=domain}`, lines 403–411).
- Confirmed mathematical soundness of all four proof steps for arbitrary characteristic ($0$ or $p$):
  1. **Step 1:** $\mathbb{L} = \bigcup_{n \ge 0} \pi^{-n}\mathcal{O}_{\mathbb{L}}$ is Polish and $m_{\mathbb{L}}$ is a $\sigma$-finite Radon measure nonzero on nonempty open sets; every $g \in \mathrm{Iso}(\mathbb{L})$ preserves $m_{\mathbb{L}}$ via metric invariance and $g(\mathcal{O}_{\mathbb{L}}) = g(0) + \mathcal{O}_{\mathbb{L}}$.
  2. **Step 2:** $K_m / K_{m+1} \xrightarrow{\theta_m} \mathfrak{sl}_2(\mathbb{F}_p)$ ($m \ge e$, $e=1$ for $p \ge 3$, $e=2$ for $p=2$) yields a normal chain $U_0 > U_1 > \dots$ of index-$p$ open subgroups with $\bigcap_k U_k = \{I\}$, giving a surjective isometry & normalized-Haar measure isomorphism $\Phi : U_0 \to \mathcal{O}_{\mathbb{L}}$; left translations $L_g$ extend via identity on $\mathbb{L} \setminus \mathcal{O}_{\mathbb{L}}$ to surjective isometries $\tilde{\alpha}_g \in \mathrm{Iso}(\mathbb{L})$.
  3. **Step 3:** Applies `Theorem 2.15` to $\Gamma = \ker(\mathrm{SL}_2(\mathbb{Z}) \to \mathrm{SL}_2(\mathbb{Z}/q\mathbb{Z}))$ ($\Gamma_p = U_0$, Zariski closure $\mathrm{SL}_2$), deriving local spectral gap wrt $\mathcal{O}_{\mathbb{L}}$ and hence domain-of-expansion via `Lemma 2.16`.
  4. **Step 4:** Both via `Remark 2.11` and via an explicit finite-covering reduction directly from `Definition 2.8(i)` (including $\eta \ge 1$), every $C \in \mathcal{B}_{m_{\mathbb{L}}} \cap \mathcal{C}(\mathrm{Iso}(\mathbb{L}) \curvearrowright \mathbb{L})$ is a domain of expansion.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/orzechowski-2611.34308-q3.9/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Step 2(1) pro-$p$ filtration:** Enumerated $K_m / K_{m+1}$ for $p \in \{2, 3, 5, 7\}$, $m \in \{e, e+1\}$, verified $\mathrm{tr}(A) \equiv 0 \pmod p$, $|K_m/K_{m+1}| = p^3$, exact $\det \equiv 1 \pmod{p^{m+3}}$ and $\mathbb{F}_p$-spanning for the $3$ explicit lifts, and built the index-$p$ flag $U_0 > \dots > U_6$ inside $U_0/K_{e+2}$ for $p \in \{2, 3, 5\}$ verifying normality in $U_0$.
2. **Step 2(2)–(3) ultrametric tree $\Phi$ and extension $\tilde{\alpha}_g$:** Constructed the level-$3$ coset-tree bijection $\Phi : U_0/U_3 \to \{0, \dots, p-1\}^3$ for $p \in \{2, 3\}$, verified exact ultrametric isometry and $L_g$-invariance over all pairs, and verified $\tilde{\alpha}_g$ preserves ultrametric valuations across $\mathcal{O}_{\mathbb{L}}$ and $\pi^{-2}\mathcal{O}_{\mathbb{L}} \setminus \mathcal{O}_{\mathbb{L}}$.
3. **Step 3 surjectivity & finite-quotient spectral gap:** Verified $\mathrm{SL}_2(\mathbb{Z}) \to \mathrm{SL}_2(\mathbb{Z}/p^k\mathbb{Z})$ surjectivity by BFS on transvections for $(p,k) \in \{(2,2),(2,3),(3,1),(3,2),(5,1)\}$, and verified connectedness and exact `QQ` eigenvalue spectrum on $L^2_0(U_0/K_{e+1})$ via SymPy Sturm root counting for $p \in \{2, 3, 5\}$ (both pure generators $S_{\mathrm{gens}}$ and lazy $S_{\mathrm{gens}} \cup \{I\}$ strictly in $(-1, 1)$).
4. **Step 4 covering-transfer inequalities:** Verified the exact rational bounds in `Fraction` arithmetic across parameter grids.

## 3. Gate 2 Novelty Status
- Passed by `watch-1` (`#1577`), `watch-5` (`#1582`), and `watch-6` (`#1584`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).
