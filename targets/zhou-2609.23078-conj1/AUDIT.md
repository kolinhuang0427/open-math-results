# Independent Adversarial Audit: `targets/zhou-2609.23078-conj1/`

- **Auditor:** `@audit-1`
- **Target:** You Zhou, *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, `arXiv:2609.23078v1` (confirmed sole version on `arxiv.org/abs/2609.23078` as of 2026-11-27), Section 1 Conjecture 1 / Section 4 Conjecture 4.1 (`\label{conj:main1-all-types}`).
- **Candidate Artifacts Inspected (blind):** Primary source `tools/.arxiv_cache/eprint/2609.23078/MAXIMAL_PROPER_EXTREMAL_SUBSET_IN_THE_CRYSTAL_BASIS_OF_A_FINITE-DIMENSIONAL_IRREDUCIBLE_MODULE.tex`, `TARGET.md`, `PROOF.md`, `notes/check-check-2.py`, `notes/check-check-2.md`.
- **Verdict:** **PASS** (re-audit after `#1581`/`#1586` fixes; verification label: `"written proof, internally audited"`).

---

## 1. Mathematical Audit — PASS (Zero Mathematical Gaps)

Every mathematical step in `PROOF.md` has been checked line-by-line against primary definitions and independently stress-tested:

1. **Conventions & Hong–Kang Tensor Rule (`PROOF.md` L39–47):** Verified verbatim against Zhou §2 (`\cite[\S 4.4]{hongkong}`, L212) and Proposition 3.12 (`prop:eimax-to-chkw`, L391–421); Langlands dual relations $[x, e_j^\vee] = \langle x, \alpha_j^\vee \rangle e_j^\vee$, $[x, f_j^\vee] = -\langle x, \alpha_j^\vee \rangle f_j^\vee$, $[e_i^\vee, f_j^\vee] = \delta_{ij} \alpha_i$ match $A^\vee = A^\top$.
2. **Lemma 1 (Non-negative Chevalley Realization in $\mathfrak{g}^\vee$, L52–76):**
   - *Simply-laced case:* Lusztig (*Introduction to Quantum Groups*, 1993, Ch. 14 & Theorem 22.1.7) establishes $E_j, F_j$ act on the canonical basis $\mathbf{B}(\Lambda)$ with coefficients in $\mathbb{N}[v, v^{-1}]$, specializing at $v = 1$ to $\mathbb{Z}_{\ge 0}$ entries with standard Chevalley signs. Highest/lowest weight spaces are $1$-dimensional, giving (1)–(3).
   - *Non-simply-laced case:* Diagram-automorphism folding $\mathfrak{g}^\vee = (\tilde{\mathfrak{g}}^\vee)^\sigma$ ($D_{n+1}\to B_n$, $A_{2n-1}\to C_n$, $E_6\to F_4$, $D_4\to G_2$) has pairwise non-adjacent orbit elements, giving exact $A^\vee = A^\top$ relations; $\mathrm{wt}_{\mathfrak{g}^\vee}(v_+) = \varpi_k^\vee$; the embedded $w_\circ \in W \hookrightarrow \tilde{W}^\sigma$ maps the $\sigma$-fixed regular dominant element $\sum_{j \in I} \varpi_j$ into the open anti-dominant chamber of $\tilde{\mathfrak{g}}^\vee$, forcing $w_\circ = \tilde{w}_\circ$ in $\tilde{W}$ and $\mathrm{wt}_{\mathfrak{g}^\vee}(v_-) = w_\circ \varpi_k^\vee$. Weight grading forces $\dim (V_k)_{w_\circ \varpi_k^\vee} = 1$, hence $v_- \in U(\mathfrak{g}^\vee) v_+ \cong V_{\mathfrak{g}^\vee}(\varpi_k^\vee)$ and $\mathcal{W}_k \ne \varnothing$ with $m = \mathrm{ht}(\varpi_k^\vee - w_\circ \varpi_k^\vee) \in \mathbb{Z}_{\ge 1}$. **Airtight.**
3. **Lemma 2 (Dyson Expansion, Concatenation, Exact Gauge Identity, L89–126):**
   - Finite-order Picard–Dyson expansion for $U(\psi)$, positivity in $\mathbf{B}_k$, ODE $(\ast)$ $\dot{g}(\psi) = (\dot{\psi} + \sum_{r\in I} e_r^\vee) g(\psi)$, and concatenation $g(\psi_1 * \psi_2)(2) = g(\psi_2)(1) g(\psi_1)(1)$ verified completely.
   - Exact gauge identity $g(\psi_u)(t) = y_j(a(t)) g(\psi)(t) y_j(-b)$ re-derived from scratch: $\mathrm{Ad}(\exp(a f_j^\vee))(\dot{\psi}) = \dot{\psi} + a\dot{h}f_j^\vee$, $\mathrm{Ad}(\exp(a f_j^\vee))(e_r^\vee) = e_r^\vee$ ($r \ne j$), $\mathrm{Ad}(\exp(a f_j^\vee))(e_j^\vee) = e_j^\vee - a\alpha_j - a^2 f_j^\vee$, and $\dot{a} + a\dot{h} - a^2 = 0$, $-a = u'/u$ all hold identically; $u \in C^1([0, T])$ globally since $h$ is continuous. **Airtight.**
4. **Lemma 3 (Laplace Tropical Limit & Uniform Stability, L136–153):** Upper/lower Laplace bounds on $\Delta_m(T)$ ($T > 0, m \ge 1$), uniform $L_k \|\eta^{(\beta)} - \zeta\|_\infty$ stability, and dominant-path evaluation $M_k(\zeta) = \langle \zeta(T), \varpi_k^\vee \rangle$ verified completely. **Airtight.**
5. **Littelmann Path Model & Lemma 4 (Pitman Invariance & Highest-Weight Formula, L156–207):**
   - Envelope formulas for $\tilde{e}_j, \tilde{f}_j$ verified verbatim against Littelmann (1995) §1.1 (including explicit mutual inverse check $\tilde{e}_j \tilde{f}_j = \mathrm{id}$ and Hong–Kang §4.4 tensor-rule alignment on $\mathcal{P}(\mu) * \mathcal{P}(\lambda)$).
   - Lemma 4(1) uniform convergence $\tilde{\eta}_j^{(\beta)} \to \mathcal{P}_j \eta$ on $[0, T]$ (splitting $[0, \delta_0]$ and $[\delta_0, T]$) and $Z_k(\beta; \tilde{\eta}_j^{(\beta)}) = Z_k(\beta; \eta)$ via $b = -1$ verified completely.
   - Lemma 4(2) induction on $q = -Q_j \in \mathbb{Z}_{\ge 0}$ and identity $\max(0, c-x) - \max(x, c) = -x$ verified completely.
   - Lemma 4(3) $\langle H(a \otimes b), \varpi_k^\vee \rangle = M_k(\pi_1 * \pi_2)$ verified completely (including Littelmann integrality for every intermediate $\eta^{(r)} \in \mathcal{P}(\mu) * \mathcal{P}(\lambda)$). **Airtight.**
6. **Theorem 1 (General Tensor Dominance Monotonicity, L213–254):**
   - Step 1: $b_\beta > 0$, $u_\beta \in [e^{-\beta}, 1]$, $g(\beta \pi_2)(1) = y_i(-a_\beta(1)) g(\beta \pi_{2,\beta})(1) y_i(+b_\beta)$, $\langle v_+ | y_i(-a_\beta(1)) = \langle v_+ |$, and $\exp(+b_\beta f_i^\vee) \ge I$ entrywise yield $Z_k(\beta; \pi_1 * \pi_2) \ge Z_k(\beta; \pi_1 * \pi_{2,\beta})$ for all $\beta > 0$.
   - Step 2: Uniform convergence $-\frac{1}{\beta}\log u_\beta(t) \to \min(1, M(t) - Q)$ on $[0, 1]$ (using $h(1) \ge Q + 1$ to stay uniformly away from $1$ on $K_\varepsilon$) verified with zero gaps, including edge cases.
   - Step 3: $\langle H(a \otimes b) - H(a \otimes \tilde{f}_i b), \varpi_k^\vee \rangle \ge 0$ for all $k \in I$ with difference in $Q$ gives $H(a \otimes b) \ge H(a \otimes \tilde{f}_i b)$; dual proof for (2) $H(\tilde{f}_i a \otimes b) \ge H(a \otimes b)$ via $y_i(-b_\beta) v_- = v_-$ and $y_i(+a_\beta(1)) \ge I$ verified completely. **Airtight.**
7. **Theorem 2 (Conjecture 1 in All Finite Types, L260–306):**
   - Edge case $\lambda = 0$ verified.
   - Step 1 ($\mathrm{wt}(\check{e}_{w_\circ}(b)) \ge \mathrm{wt}(\check{e}_{w_\circ}(\tilde{f}_i b))$), Step 2 Part 1 (every HW element has form $b_\rho \otimes d$ with $\eta \ge \nu_0$), Step 2 Part 2 ($\nu_0 = \overline{\rho + w_\circ \lambda}$ via PRV 1967 Theorem 2.1), Step 2 Part 3 (self-contained cyclic-vector proof $U(\mathfrak{g})(v_\rho \otimes v_{w_\circ \lambda}) = V(\rho) \otimes V(\lambda) \implies \mathrm{mult}_{V(\rho)\otimes V(\lambda)}(V(\nu_0)) \le \dim V(\nu_0)_{\rho+w_\circ\lambda} = 1$), Step 3 ($\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$), and Step 4 ($\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$ and unique maximal proper extremal subset $\mathcal{B}(\lambda) \setminus \mathcal{F}(b_\star)$) are all **100% airtight**.

---

## 2. Independent Verification & Adversarial Stress Test — PASS

- **AST & exactness audit of `notes/check-check-2.py`:** `FLOATS: []`, `FLOAT_CALLS: []`; all 7 `/` expressions (L49, L149, L169, L580, L598, L609, L616) divide `Fraction` by `Fraction`.
- **Execution:** `.venv/bin/python -u targets/zhou-2609.23078-conj1/notes/check-check-2.py` exited `0`, raw output `PASS` (31 crystals across $A_2, C_2, G_2, A_3, B_3, C_3, D_4, F_4$, 11,643 tensor monotonicity checks, full Step 2 minimality/PRV/mult-1 checks, and Lemma 1/2(3) exact Taylor series in $\mathrm{Mat}_4(\mathbb{Q}[t]/(t^{11}))$).
- **Auditor's independent adversarial test:** Explicitly constructed the folded $A_3 \to C_2^\vee$ modules $V_0 = \bigwedge^2 \mathbb{C}^4$ (dim 6, reducible $5 \oplus 1$, $\mathcal{W}_0 = \{(0,1,1,0): 2\}$) and $V_1 = \mathbb{C}^4$ (dim 4, $\mathcal{W}_1 = \{(1,0,1): 1\}$) and directly evaluated $M_k(\pi_1 * \pi_2)$ by exact rational DP over all path breakpoints; confirmed $\langle H(a \otimes b), \varpi_k^\vee \rangle = M_k(\pi_1 * \pi_2)$ identically on every pair $(a, b)$ in $\mathcal{B}(1,0)\otimes\mathcal{B}(0,1)$, $\mathcal{B}(1,1)\otimes\mathcal{B}(1,0)$, and $\mathcal{B}(1,1)\otimes\mathcal{B}(1,1)$ (`[ADVERSARIAL PASS]`).

---

## 3. Blocking Defects (Citation / Compiled LaTeX Numbering & Cross-References)

Running an exact LaTeX counter audit on the primary source `MAXIMAL_PROPER_EXTREMAL_SUBSET_IN_THE_CRYSTAL_BASIS_OF_A_FINITE-DIMENSIONAL_IRREDUCIBLE_MODULE.tex` (`\newtheorem{theorem}{Theorem}[section]` shared across `lemma`, `proposition`, `corollary`, `conjecture`, `definition`, `remark`; Sections 1–7 + Appendix A) reveals systematic off-by-one section/proposition numbers in `PROOF.md` (and `TARGET.md` / `notes/check-check-2.md`), plus a dangling internal reference:

| Primary-source `\label` (line) | Actual compiled number in `arXiv:2609.23078v1` | Incorrect citation currently in files |
|---|---|---|
| `\section{Main result}` (`sec:main-theorems`, L509) & `\label{conj:main1-all-types}` (L516) | **Section 4**, **Conjecture 4.1** (= Conjecture 1) | `PROOF.md` L5 (`§1 & §3`); `TARGET.md` L2, L7, L10, L14 (`Section 3 Conjecture 3.1`); `check-check-2.md` L7 (`Conjecture 3.1`) |
| `\label{prop:eimax-indep}` (L234) | **Proposition 2.2** (§2; L222 is Definition 2.1) | `PROOF.md` L206 (`Zhou, Proposition 2.1`) |
| `\label{prop:max-proper-extremal}` (L307) | **Proposition 3.7** (§3.1) | `PROOF.md` L300 (`Propositions 2.6 ...`); `TARGET.md` L17 (`Proposition 2.6`) |
| `\label{prop:eimax-to-chkw}` (L391) | **Proposition 3.12** (§3.2) | `PROOF.md` L10, L267 (`Proposition 2.11`); `check-check-2.md` L8 (`Proposition 2.11`) |
| `\label{prop:reduction}` (L525) | **Proposition 4.2** (§4) | `PROOF.md` L300 (`... and 3.2 of Zhou`); `check-check-2.md` L8 (`Proposition 3.3`) |
| `\label{thm:main1}` (L574) | **Theorem 4.4** (= Theorem 1, §4) | (note for completeness alongside `Theorem 1`) |
| `\label{prop:w0Tgew0fiT}` (L1078) | **Proposition 7.2** (§7) | `PROOF.md` L22, L266 (`Proposition 6.2`); `check-check-2.md` L8 (`Proposition 6.2`) |
| `\cite{khare2012}` in proof of Theorem 1 (L1143, L1172) | **Section 7** | `PROOF.md` L279 (`cited in Zhou §6`) |

Additional internal cross-reference / cleanup items in `PROOF.md`:
1. **`PROOF.md` L34 (dangling internal reference):** Proof Overview item 4 cites `(Lemma 5 & Theorem 1)`, but `PROOF.md` has no Lemma 5 (Sections 1–5 contain Lemmas 1–4, Theorem 1, Theorem 2). Fix to `(Theorem 1)`.
2. **`PROOF.md` L41 (raw TeX bibkey typo):** Cites `` `[hongkong, §4.4]` `` (Zhou's raw TeX bibkey typo for Hong–Kang). Replace with `Hong–Kang (2002, §4.4)`.

---

## 4. Re-Audit Resolution (`#1581`, `#1586`) — PASS

All Section 3 citation, compiled-LaTeX numbering, and internal cross-reference items were fixed and independently re-verified across `TARGET.md`, `PROOF.md`, and `notes/check-check-2.md`:
- `TARGET.md`: Section 1 Conjecture 1 / Section 4 Conjecture 4.1 (`conj:main1-all-types`), Proposition 3.7 (`prop:max-proper-extremal`), Theorem 1 / Theorem 4.4 (`thm:main1`), Sections 1–4.
- `PROOF.md`: §1 & §4 Conjecture 4.1 (L5), Proposition 3.12 (L10, L41, L267), Theorem 1 / Theorem 4.4 (L22), Proposition 7.2 (L22, L266), `(Theorem 1)` replacing dangling `Lemma 5` (L34), `Hong–Kang 2002, §4.4` (L41), Proposition 2.2 (L206), Zhou §7 (L279), Propositions 3.7 and 4.2 (L300).
- `notes/check-check-2.md`: §4 Conjecture 4.1, Propositions 2.2/3.7/3.12/4.2/7.2.
- `notes/check-check-2.py`: unchanged, pure exact arithmetic (`FLOATS: []`, all `/` are `Fraction/Fraction`), exit `0` `PASS`.

**Final Verdict: PASS** — ready for Gate 3 freshness (`<1h`) and Coordinator reporting (`"written proof, internally audited"`).

