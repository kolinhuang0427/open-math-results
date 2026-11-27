# Adversarial Audit Report: `targets/haugland-2411.00721-ques2/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T08:59Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Primary source verbatim: `tools/.arxiv_cache/eprint/2411.00721v2/haugland-omland-reversible-v2.tex` (`arXiv:2411.00721v2`, updated `2026-11-01`, DOI `10.1007/s10623-026-01869-z`, verified via live arXiv API).
- `targets/haugland-2411.00721-ques2/TARGET.md`
- `targets/haugland-2411.00721-ques2/PROOF.md`
- `targets/haugland-2411.00721-ques2/notes/check-check-1.md` and `targets/haugland-2411.00721-ques2/notes/check-check-1.py`
- Confirmed no `targets/haugland-2411.00721-ques2/CONTESTED.md` exists, and Gate 2 PASS receipts posted by `watch-1` (`#40`), `watch-5` (`#51`), and `watch-6` (`#77`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Fidelity Audit (PASS)

- Verified word-for-word against `haugland-omland-reversible-v2.tex`:
  - Definitions of induced shift-invariant map $F \colon \mathbb{F}_2^n \to \mathbb{F}_2^n$, diameter $k$, $(k,n)$-lifting, proper lifting, and equivalence with reversible binary cellular automata via Kari's Theorem 7 (lines 89–101).
  - Exact numbering under `\newtheorem{...}[theorem]` with `[section]` counter: Remark 1.1 (L103), **Proposition 1.2** (L108: *"An affine Boolean function is a proper lifting if and only if it has diameter 1"*), Proposition 1.3 (L114), Example 1.4 (L127), **Proposition 1.5** (L133, `\label{shift-product}`), Proposition 2.1 (L282), Question 2.2 (L323), **Question 2.3** (L327–331), and Section 4 **Open Problem (iii)** (L455). Every internal cross-reference in `PROOF.md` (`Question 2.3`, `Proposition 1.2`, `Proposition 1.5`, `Open Problem (iii)`) matches the compiled paper numbering exactly.
  - Scope is accurately stated: Question 2.3 and the existence question in Open Problem (iii) are settled completely in the negative, while the secondary question in Open Problem (iii) (*"what is the minimal possible degree as a function of diameter?"*) is explicitly noted as outside scope.

---

## 3. Line-by-Line Mathematical Audit (PASS)

1. **Theorem 1 & Corollary 2 (Lines 31–41):**
   - Index shift $x_r^{\text{new}} = x_{r+1}^{\text{old}}$ ($r \in \mathbb{Z}/n\mathbb{Z}$) cleanly conjugates the paper's 1-based definition to $F_n(x)_r = f(x_r, \dots, x_{r+k-1})$.
   - For $k = 1$, every Boolean function $f \colon \mathbb{F}_2^1 \to \mathbb{F}_2$ has algebraic degree $\le 1$. For $k \ge 2$, Theorem 1 shows every degree-2 Boolean function $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ fails bijectivity at $N = 2^{\lceil \log_2 k \rceil + 1} \ge 2k > k$, hence is not a proper lifting. Combined with Proposition 1.2 and Kari's Theorem 7, Corollary 2 follows cleanly.
2. **Section 3.1 — Directional Derivatives (Lines 46–56):**
   - Verified ANF representation with symmetric zero-diagonal matrix $Q = (q_{ij})$ and exact expansion $(F_n(x+u) + F_n(x))_r = \sum_{j=0}^{k-1} C_j(r) x_{r+j} + v(u)_r$ over $\mathbb{F}_2$ with $v(u) = F_n(u) + F_n(0)$ and $C_j(r) = \sum_{i=0}^{k-1} q_{ij} u_{r+i}$.
3. **Section 3.2 — Lemma 3 (Lines 58–89):**
   - Verified $N = 2^M \ge 2^s + k - 1$ implies $N \ge k$ and $2^s \mid N$ (for $k \ge 1, s \ge 0$).
   - Verified ring identification $R_N = \mathbb{F}_2[z]/(z^N + 1) = \mathbb{F}_2[z]/((z+1)^N)$, exact shift correspondence $\sum_r x_{r+j} z^r = z^{-j} X(z)$ and $\sum_j \gamma_j z^{-j} X(z) = z^{-(k-1)} \widetilde{P}(z) X(z)$ with $\deg \widetilde{P} \le k - 1$.
   - Verified $2^s$-periodicity of $v(u)$ yields $V(z) = (z+1)^{N - 2^s} \widetilde{V}(z)$ in $R_N$ via $(w+1)\sum_{t=0}^{L-1} w^t = (w+1)^L$ in $\mathbb{F}_2[w]$ (valid for all $L = 2^{M-s} \ge 1$).
   - Verified factorization $\widetilde{P}(z) = (z+1)^e R(z)$ with $0 \le e \le k - 1$ and $R(1) = 1 \implies R(z) \in R_N^\times$, nonnegativity $N - 2^s - e \ge (k-1) - e \ge 0$, and explicit solution $X(z) = z^{k-1} R(z)^{-1} (z+1)^{N - 2^s - e} \widetilde{V}(z) \in R_N$ producing $F_N(x+u) = F_N(x)$ with $u \neq 0$ (including edge cases $R(z) = 1$ and $V(z) = 0$). Completely airtight.
4. **Section 3.3 — Double Induction (Lines 90–140):**
   - Verified $2k \le N \le 4k - 4$ and $2^t + k - 1 < N$ for all $k \ge 2$ and $0 \le t \le s_{\max} = \lceil \log_2 k \rceil$ (including boundary $k = 2$, $s_{\max} = 1$, $N = 4$).
   - Verified base case $s = 0$ with all-ones $u$.
   - Verified outer step $s \to s+1$ ($0 \le s < s_{\max}$, $P = 2^s$, $2P \mid N$): $a_j(b+P) = a_j(b)$, well-definedness and nonzeroness of the $2P$-periodic lift $u$ from $w \in \mathbb{F}_2^P \setminus \{0\}$, $u_m + u_{m+P} = w_{m \bmod P}$, Eq. (7), and Eq. (8) $[T^{r \bmod P}](W(T) A_j^*(T)) = C_j(r)$ in $R_P = \mathbb{F}_2[T]/((T+1)^P)$.
   - Verified inner induction on $e \in \{0, \dots, P\}$ (including edge case $s = 0, P = 1$): $W(T) = (T+1)^{P-1-e}$ has degree $< P$ and is nonzero; $(T+1)H_j(T) = 0$ in $R_P$ forces $H_j(T) = \gamma_j (T+1)^{P-1} = \gamma_j \sum_{r=0}^{P-1} T^r$, so $C_j(r) = \gamma_j$ is independent of $r$, and Lemma 3 forces $\gamma_j = 0$ for all $j$.
   - At $s = s_{\max}$, $2^{s_{\max}} \ge k$ separates all $0 \le i \le k-1$, forcing $q_{ij} = 0$ for all $i, j$, contradicting $\deg(f) = 2$.
5. **Section 4 — Sharpness Remark (Lines 144–150):**
   - Verified $f_m(y_0, \dots, y_{2^m+1}) = y_0 + (y_0 + y_{2^m})(y_1 + y_{2^m+1})$ ($m \ge 1$, $k = 2^m + 2$) has degree 2, diameter $k$, and induces an involution $F_{2^{m+1}}^2 = \mathrm{id}$ at $n = 2^{\lceil \log_2 k \rceil}$.

---

## 4. Independent Verifier Re-Execution (PASS)

Re-executed `.venv/bin/python targets/haugland-2411.00721-ques2/notes/check-check-1.py`:
- Exit code `0`
- Raw output: `PASS` (exhaustive $k = 2, 3$; 1,008 functions at $k = 4$; 800 random diameter-$k$ functions for $k = 5..12$; constructive Lemma 3 collisions verified; sharpness family $m = 1, 2, 3$ verified).

---

## 5. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python targets/haugland-2411.00721-ques2/notes/check-check-1.py` and paths `targets/haugland-2411.00721-ques2/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
