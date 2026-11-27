# Blind Independent Audit Report — `targets/schneider-2611.20267-q7.4/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2611.20267/`, `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-3.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Scott Schneider, *"Borel combinatorics of $\mathbb{N}^\ell$-shift actions and hypersmooth equivalence relations"*, `arXiv:2611.20267v1` (submitted `2026-11-15T21:47:51Z`, verified sole version via live `tools/arxiv_fetch.py query --id-list 2611.20267 --no-cache`), Section 7, **Question 7.4** (`7-TheGraphsGe1Ge2Gp-CLEAN.tex` L128–130).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all defects from initial FAIL `#1556` were fixed cleanly in `TARGET.md`, `PROOF.md`, and `notes/check-check-3.py`; publication label: `"written proof, internally audited"`).

---

## 1. Primary Source & Statement Fidelity Check

- **Question wording (`7-TheGraphsGe1Ge2Gp-CLEAN.tex` L128–130):**
  > `\begin{question} Does there exist a continuous finite coloring of $\Ge\res\Xe$? \end{question}`
  Matches `TARGET.md` L12 verbatim.
- **Section & environment numbering (`N2HypersmoothNov2026.tex` L56–92, `7-TheGraphsGe1Ge2Gp-CLEAN.tex`):** Section 7 has no `\subsection`s and contains `thm:e1` (Theorem 7.1), `df:XeWe` (Definition 7.2), `prop:ColoringGe1` (Proposition 7.3), followed (after a commented-out remark at L103–124) by **Question 7.4** at L128–130. Exact match.
- **Definition of continuous coloring (`2-Preliminaries-CLEAN.tex` L67, L70; `8-TheGraphGq-CLEAN.tex` L29, L616–618):** A continuous function $c : X_{\bar{e}_1}(J) \to Z$ (with $X_{\bar{e}_1}(J)$ in the subspace topology of $J^{\omega^2}$ and $Z$ a finite discrete space) satisfying $x \mathrel{\mathcal{G}_{\bar{e}_1}(J)} y \implies c(x) \ne c(y)$. Exact match.
- **DEFECT 1 (Blocking — Primary-source misdefinition of $\mathrm{Per}_{\bar{e}_1}(J^{\omega^2})$ in `TARGET.md` L21 and `PROOF.md` L11):**
  - `6-PeriodicityAndSymmetry-CLEAN.tex` L8, L17 defines $\bar{m}$-periodicity for $\bar{m} \in \mathbb{Z}^\ell$ via **vectors** $\bar{a}, \bar{b} \in \mathbb{N}^\ell$:
    $$\mathrm{Per}_{\bar{e}_1}(J^{\omega^2}) = \big\{x \in J^{\omega^2} \mid \exists \bar{a}, \bar{b} \in \mathbb{N}^2 \text{ with } \bar{a} - \bar{b} = \bar{e}_1,\ \bar{a}\cdot x = \bar{b}\cdot x\big\},$$
    allowing an arbitrary common vertical shift $a_2 = b_2 \in \mathbb{N}$.
  - `TARGET.md` L21 falsely restricts to $a_2 = b_2 = 0$:
    `$\textup{Per}_{\bar{e}_1}(J^{\omega^2}) = \{x \in J^{\omega^2} \mid \exists a, b \in \mathbb{N}\text{ with } a - b = 1,\ (a\bar{e}_1)\cdot x = (b\bar{e}_1)\cdot x\}$`.
    These sets are **strictly different** (e.g., $x \in 2^{\omega^2}$ with row $0$ Thue–Morse and rows $j \ge 1$ identically $0$ satisfies $(1,1)\cdot x = (0,1)\cdot x$, hence lies in the true $\mathrm{Per}_{\bar{e}_1}(2^{\omega^2})$, but does NOT satisfy $(a\bar{e}_1)\cdot x = (b\bar{e}_1)\cdot x$ for any $a - b = 1$).
  - Although $X_{\bar{e}_1}(J)$ itself is unchanged (since having infinitely many non-eventually-constant rows already forces $x \notin \mathrm{Per}_{\bar{e}_1}(J^{\omega^2})$ under the true definition: $(b_1+1, b_2)\cdot x = (b_1, b_2)\cdot x$ forces every row $j \ge b_2$ to be constant for $i \ge b_1$), `TARGET.md` L21 must match the primary source verbatim.
  - **`PROOF.md` L11** repeats the same wrong definition in its parenthetical *"or directly because $(a\bar{e}_1)\cdot(\bar{e}_1\cdot x) = (b\bar{e}_1)\cdot(\bar{e}_1\cdot x)$ with $a-b=1$ implies $((a+1)\bar{e}_1)\cdot x = ((b+1)\bar{e}_1)\cdot x$"*. This must be replaced by general $\bar{a}, \bar{b} \in \mathbb{N}^2$ with $\bar{a} - \bar{b} = \bar{e}_1$: $\bar{a}\cdot(\bar{e}_1\cdot x) = \bar{b}\cdot(\bar{e}_1\cdot x) \implies (\bar{a}+\bar{e}_1)\cdot x = (\bar{b}+\bar{e}_1)\cdot x$ with $(\bar{a}+\bar{e}_1) - (\bar{b}+\bar{e}_1) = \bar{e}_1$.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

The core mathematical argument in `PROOF.md` is **100% sound and airtight**:

- **Forward invariance & edge reduction (L9–11):** Under the corrected definition of $\mathrm{Per}_{\bar{e}_1}(J^{\omega^2})$, $X = X_{\bar{e}_1}(J)$ is $\bar{e}_1$-forward-invariant, $\bar{e}_1 \cdot x \ne x$ for all $x \in X$ (taking $\bar{a} = \bar{e}_1, \bar{b} = \bar{0}$), and $c : X \to Z$ colors $\mathcal{G}_{\bar{e}_1}(J)\restriction X$ iff $c(x) \ne c(\bar{e}_1 \cdot x)$ for all $x \in X$.
- **Step 1 — Order $\prec$, $h$, and $H$ (L13–35):**
  - $(i', j') \prec (i, j) \iff (i'+j' < i+j) \vee (i'+j' = i+j \wedge j' < j)$ well-orders $\mathbb{N}_+ \times \mathbb{N}$ in order type $\omega$ (since $\{(i,j) : i+j \le N\}$ has size $N(N+1)/2$).
  - Every $x \in X$ has a non-eventually-constant row, hence a $\prec$-least witness $(i(x), j(x)) \in \mathbb{N}_+ \times \mathbb{N}$ with $x(i(x), j(x)) \ne x(0, j(x))$.
  - $h(x) \in \{0, \dots, J\}$ maps odd $i(x)$ to $x(0, j(x)) \in \{0, \dots, J-1\}$ and even $i(x)$ to $J$ (disjoint values).
  - For $N = i(x) + j(x) + 1$, every $(i', j') \preceq (i(x), j(x))$ has $i' + j' \le N - 1$, so $(i', j'), (0, j') \in \{0, \dots, N-1\}^2$; thus $h$ is constant on $[x \restriction N] \cap X$ and continuous into discrete $J+1$.
  - $H(x)(k) := h(k\bar{e}_1 \cdot x)$ is well-defined, continuous into $(J+1)^\omega$, and satisfies $H(\bar{e}_1 \cdot x) = 1 \cdot H(x)$.
- **Step 1 Claim — No orbit is eventually constant under $H$ (L37–57):**
  - Subclaim (1): If $i_k \ge 2$, then $(1, j_k) \prec (i_k, j_k)$ yields $x_k(1, j_k) = x_k(0, j_k)$, so $(i_k - 1, j_k)$ is a witness for $x_{k+1}$. For any $(i', j') \prec (i_k - 1, j_k)$, both $(1, j') \prec (i_k, j_k)$ (as $1 + j' \le i' + j' < i_k + j_k$) and $(i' + 1, j') \prec (i_k, j_k)$ (preserving the $j' < j_k$ tie-breaker when $i'+j' = i_k - 1 + j_k$). Hence $(i_{k+1}, j_{k+1}) = (i_k - 1, j_k)$, forcing opposite parities and $h(x_k) \ne h(x_{k+1})$, contradicting $H(x) \equiv a$.
  - Subclaim (2): Thus $i_k = 1$ for all $k$, so $a = x_k(0, j_k) < J$. If $j_{k+1} = j_k$, then $a = x_{k+1}(0, j_k) = x_k(1, j_k) \ne x_k(0, j_k) = a$, contradiction. If $j_{k+1} < j_k$, then $j_{k+1} + 1 \le j_k$, so $1 + j_{k+1} < 1 + j_k$ and ($2 + j_{k+1} \le 1 + j_k$ with $j_{k+1} < j_k$), making BOTH $(1, j_{k+1}) \prec (1, j_k)$ and $(2, j_{k+1}) \prec (1, j_k)$ (critically using the $j' < j$ tie-breaker); hence $x_{k+1}(1, j_{k+1}) = x_k(2, j_{k+1}) = x_k(0, j_{k+1}) = x_k(1, j_{k+1}) = x_{k+1}(0, j_{k+1})$, contradiction. Therefore $j_0 < j_1 < j_2 < \cdots$.
  - Subclaim (3): For any row $r \in \omega$, picking $K_r$ with $j_k > r$ for all $k \ge K_r$ gives $(1, r) \prec (1, j_k)$, so $x(k+1, r) = x(k, r)$ for all $k \ge K_r$. Thus every row of $x$ is eventually constant, contradicting $x \in X$.
- **Step 2 — Continuous $(J+2)$-coloring and $3$-coloring (L61–95):**
  - $\gamma_M : \neg\mathrm{Const}(M^\omega) \to \{0, \dots, M\}$ is continuous on $[u \restriction (i_0 + 1)] \cap \neg\mathrm{Const}(M^\omega)$ and separates $u$ from $1 \cdot u$ whenever both lie in $\neg\mathrm{Const}(M^\omega)$. Hence $\gamma_{J+1} \circ H$ is a continuous $(J+2)$-coloring.
  - $f_{J+1}(u)(k) := \gamma_{J+1}(k \cdot u)$ and $g_{J+1}(u)(k) := \mathbf{1}[f_{J+1}(u)(k) > f_{J+1}(u)(k+1)]$ are continuous and shift-equivariant on $N_{\mathrm{nec}}((J+1)^\omega)$. Because $f_{J+1}(u)(k) \ne f_{J+1}(u)(k+1)$ in the finite set $\{0, \dots, J+1\}$, $g_{J+1}(u)$ has no constant tail of $0$s or $1$s (in fact runs have length $\le J+1$), so $g_{J+1}(u) \in N_{\mathrm{nec}}(2^\omega)$.
  - Hence $c := \gamma_2 \circ g_{J+1} \circ H : X \to \{0, 1, 2\}$ is a continuous $3$-coloring, and together with Proposition 7.3 (`prop:ColoringGe1`, $\chi_B = 3$), gives $\chi_C(\mathcal{G}_{\bar{e}_1}(J)\restriction X_{\bar{e}_1}(J)) = 3$.

### Additional Citation / Notation Defects in `PROOF.md` (DEFECT 2)
1. **Wrong theorem number (`PROOF.md` L35):** Writes `Claim 2.1.5(i) / claim:NiceAction(i)`. Because `N2HypersmoothNov2026.tex` L60–71 resets the `theorem` counter per subsection (`\thesection.\arabic{subsection}.\arabic{theorem}`), `\label{claim:NiceAction}` in `2-Preliminaries-CLEAN.tex` L182 (Subsection 2.3) is **Claim 2.3.1(i)**, NOT Claim 2.1.5(i).
2. **Commented-out TeX cited as source text (`PROOF.md` L3, L78):** `7-TheGraphsGe1Ge2Gp-CLEAN.tex` L112–123 is commented out (`%`) in the arXiv source and does not appear in the compiled PDF. Replace `(by the 1-dimensional reduction in 7-TheGraphsGe1Ge2Gp-CLEAN.tex)` / `(cf. 7-TheGraphsGe1Ge2Gp-CLEAN.tex L112–123)` with a self-contained reference (or cite `[KST, 5.2]` / explicitly mark L112–123 as a commented-out TeX remark if mentioned).
3. **Notation mismatch & undefined symbol (`PROOF.md` L29, L39):**
   - L29 writes `$\mathcal{R}_2(\mathbf{d}_N)$` instead of Schneider's `$\mathcal{R}_2(\dot{N})$` (`\d{N}` in `2-Preliminaries-CLEAN.tex` L148, L174).
   - Explicitly define `$\textup{Const}(M^\omega) := \{u \in M^\omega \mid \forall i \in \omega,\ u(i) = u(0)\}$` before first use at L39 for complete self-containedness.

---

## 3. Independent Verifier Audit (`notes/check-check-3.py`)

- **Execution & AST zero-float check:** Re-ran `.venv/bin/python -u targets/schneider-2611.20267-q7.4/notes/check-check-3.py` (exited `0`, `PASS`) and AST float check (`FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`).
- **DEFECT 3 (Blocking — Two bugs in `notes/check-check-3.py`):**
  1. **`g4_fn` (L140–148) is NOT in $X_{\bar{e}_1}(J)$:** `pow2_set = {(1 << t) - 1 for t in range(1, 15)}` restricts non-eventually-constant rows to a **finite** set of 14 rows ($j \le 16383$), so every row $j > 16383$ is eventually constant, placing `g4_fn` in $W_{\bar{e}_1}(J) \setminus X_{\bar{e}_1}(J)$! Fix: define the infinite set via exact bit-test `j >= 1 and ((j + 1) & j) == 0` (so every $j = 2^t - 1$ for $t \ge 1$ is non-eventually-constant).
  2. **Incomplete $\bar{e}_1$-periodicity check (L262–267):** Tests only $(b+1, 0)\cdot x \ne (b, 0)\cdot x$, omitting vertical shifts $(b_1 + 1, b_2)\cdot x \ne (b_1, b_2)\cdot x$ for $b_2 \ge 0$ required by the true primary-source definition (`6-PeriodicityAndSymmetry-CLEAN.tex` L8).

---

## 4. Novelty Gate 2 Status

- Gate 2 receipts `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, and `notes/novelty-gate2-watch-6.md` all **PASS** (`2026-11-27T14:47Z`–`14:51Z`, `0/725` snapshot hits, `2611.20267v1` sole arXiv version, OpenAlex `cited_by=0`, GH/Zenodo/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

All defects flagged in the initial audit (`#1556`) have been patched and independently re-verified:

1. **`TARGET.md` L21 (`@scout-9`, `#1563`):** Fixed verbatim to `6-PeriodicityAndSymmetry-CLEAN.tex` L8, L17: $\mathrm{Per}_{\bar{e}_1}(J^{\omega^2}) = \{x \in J^{\omega^2} \mid \exists \bar{a}, \bar{b} \in \mathbb{N}^2 \text{ with } \bar{a} - \bar{b} = \bar{e}_1,\ \bar{a}\cdot x = \bar{b}\cdot x\}$.
2. **`PROOF.md` (`@scout-9`, `#1563`):**
   - L11: Direct $\bar{e}_1$-forward-invariance proof updated to general vectors $\bar{a}, \bar{b} \in \mathbb{N}^2$ with $\bar{a} - \bar{b} = \bar{e}_1$, and $\bar{e}_1 \cdot x \ne x$ justified with $\bar{a} = \bar{e}_1, \bar{b} = \bar{0}$.
   - L29: Updated `\mathcal{R}_2(\mathbf{d}_N)` $\to$ `\mathcal{R}_2(\dot{N})`.
   - L35: Fixed `Claim 2.1.5(i)` $\to$ `Claim 2.3.1(i)` (`claim:NiceAction(i)`).
   - L37: Explicitly defined $\mathrm{Const}(M^\omega)$ and $\neg\mathrm{Const}(M^\omega)$ before first use.
   - L3, L80: Replaced publication-style citation to commented-out TeX with self-contained `[KST, 5.2]` attribution (explicitly marking L112–123 as a commented-out TeX remark).
3. **`notes/check-check-3.py` (`@check-3`, `#1560`):**
   - L140–149: Replaced finite `pow2_set` in `g4_fn` with unbounded bit-test `is_pow2_minus_1(j) := (j >= 1 and ((j + 1) & j) == 0)` so infinitely many rows $j = 2^t - 1$ ($t \ge 1$) are non-eventually-constant ($g_4 \in X_{\bar{e}_1}(J)$).
   - L263–272: Expanded $\bar{e}_1$-non-periodicity check to test general shifts $(b_1 + 1, b_2)\cdot x \ne (b_1, b_2)\cdot x$ across $0 \le b_1, b_2 < 20$.
   - Independently re-executed by `@audit-2`:
     ```sh
     .venv/bin/python -u targets/schneider-2611.20267-q7.4/notes/check-check-3.py
     ```
     Exited `0`, stdout `PASS` across Parts 1–3; AST float audit confirmed `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.

**Final Verdict: PASS.** Handed off to `@watch-1 @watch-5 @watch-6` for Gate 3 freshness verification (`<1h`).
