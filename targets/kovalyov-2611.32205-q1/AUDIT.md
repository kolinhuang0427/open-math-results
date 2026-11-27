# Independent Blind Audit: `targets/kovalyov-2611.32205-q1/` (`@audit-3`)

**Verdict:** **PASS** (re-audit after `#1757` / `#1758` patches; initial audit failed on 2 blocking `PROOF.md` defects + `check-check-2.py` $r=1$ collision bug, all now verified resolved — see §6 below).

*(Initial Audit Verdict — FAIL, superseded by §6: Core mathematical idea — countable recursive saturation reduction + finite linear game $G_{n,M}(\mathcal{M}^+)$ with scale-separated bases $V_r$ and lexicographic invariant $\mathcal{I}_k$ — was sound for $n \ge 2$, but `PROOF.md` had 2 blocking defects and `notes/check-check-2.py` had a broken $r = 1$ collision implementation.)*

---

## 1. Blindness & Primary-Source Verification

- **Strict isolation observed:** Read ONLY `tools/.arxiv_cache/eprint/2611.32205/main.tex` (plus live arXiv metadata check), `targets/kovalyov-2611.32205-q1/TARGET.md`, `targets/kovalyov-2611.32205-q1/PROOF.md`, `targets/kovalyov-2611.32205-q1/notes/check-check-2.md`, and `targets/kovalyov-2611.32205-q1/notes/check-check-2.py`. Did NOT inspect `verify.py` or author scratch notes.
- **Primary source (`arXiv:2611.32205v1`, `2026-11-24`, Konstantin Kovalyov, *Some conservativity results for weak arithmetic theories in a language with exponentiation*, `math.LO`):**
  - Live arXiv query confirms `2611.32205v1` is the sole version (`journal_ref: ""`, `doi: ""`).
  - Verified verbatim in `tools/.arxiv_cache/eprint/2611.32205/main.tex`:
    - `(\mathrm{Exp})` (lines 120–122): $\exp(1) = 2$, $\exp(x+y) = \exp(x)\exp(y)$, $\exp(x) > x$.
    - $\mathsf{IOpen}$ (lines 232–238): $\mathsf{DOSR}$ plus quantifier-free induction **over $\mathcal{L}_{\mathrm{OSR}}$-formulas only**, with $\mathsf{IOpen} \vdash \mathbb{Z}\text{-}\mathsf{DOSR}$ (line 241). Hence any expansion $(\mathcal{M}^+, \exp)$ of $\mathcal{M}^+ \models \mathsf{IOpen}$ satisfying $(\mathrm{Exp})$ automatically models $\mathsf{IOpen} + (\mathrm{Exp})$.
    - Section 3 (`\section{Conservativity results for \IOpen + (\Exp)}`, line 421): Theorem 3.1, Proposition 3.2, Corollary 3.3, unlabeled Corollary 3.4, **Question 3.5** (lines 499–505):
      - `(1)` *Is $\mathsf{IOpen} + (\mathrm{Exp})$ conservative over $\mathsf{IOpen}$?*
      - `(2)` *More generally, what is the $\mathcal{L}_{\mathrm{OSR}}$-fragment of $\mathsf{IOpen} + (\mathrm{Exp})$?*
  - `TARGET.md` and `PROOF.md` match the primary source verbatim and accurately cite Question 3.5(1)–(2).
  - Snapshot grep confirms `0` settlement hits; Gate 2 PASS receipts present from `watch-{1,5,6}`.

---

## 2. Independent Verification of Core Proof Structure

- **§1 (Recursive saturation & Lemma 1, `PROOF.md` L11–39):** Sound. Every complete consistent theory $T^* = \mathrm{Th}_{\mathcal{L}_{\mathrm{OSR}}}(\mathcal{M}_0^+)$ in the finite language $\mathcal{L}_{\mathrm{OSR}}$ admits a countable recursively saturated model $\mathcal{M}^+ \models T^*$; $\mathrm{Win}_{n, M}$ and $\sigma^k_{n, M}$ are uniformly computable finite $\mathcal{L}_{\mathrm{OSR}}$-formulas; monotonicity of $\sigma^k_{n, M}$ in $(n, M)$ holds; $\Gamma_k(x)$ is recursive and finitely satisfiable. *(Minor fixes needed at L30 and L36; see §4 below.)*
- **§2.1–2.2 (Parameters, bases $V_r$, and $\mathcal{I}_n \implies \mathrm{Win}_{n, M}$, `PROOF.md` L49–79):**
  - Verified $K = n M \max(E_n, E_{0, n}) + M + 10$ strictly exceeds $|v_0|$ and $|v_r|$ for all $(c_0, \dots, c_n) \in [-M, M]^{n+1}$, and $V_r = U_r \cdot 2^K \prod_{j < r} V_j^K$ clears all negative powers of $2, V_1, \dots, V_{r-1}$ while retaining $U_r > T_{r, n} \ge L(\vec{a})$.
  - Verified $b_k \in M^{>0}$ holds immediately at round $k$ (by $\mathcal{I}_k$ on $L = a_k$) and is unaffected by subsequent base creations ($e_{k, s+1} := 0$).
  - Verified Step 1 (L85–88) in both branches ($s_{\mathrm{old}} \ge 1$ and $s_{\mathrm{old}} = 0$), including $N_k \le (n - k + 1) B_k$ and $3 B_1 B_{k-1} > B_k^2 + B_k N_k$.
  - Verified Step 2 (L92–99) for all $k \ge 2$ and Step 3 $r = 1$ collision elimination (L108, L112) in $\mathbb{Z}\text{-}\mathsf{DOR}$ (exact divisibility in $\mathbb{Z}$ and congruence mod $\mu_k$).
  - Stress-tested an independent exact-arithmetic simulator of the full strategy across 15 targeted adversarial trajectories and 120 randomized nonstandard $\mathbb{Z}[\omega_1, \omega_2]$ plays for $n = 2, 3$ (exercising pinned, unpinned, $r=1$ collisions, and $r \ge 2$ weak-weak equalities) checking ALL tuples including $c_k = 0$: all $n \ge 2$ plays satisfy $\mathcal{I}_k$ cleanly.

---

## 3. Blocking Defects

### Defect 1 (BLOCKING — `PROOF.md` L50–51, L75, L95–99): Step 2 at $k = 1$ violates $\mathcal{I}_1(2)$ for $n = 1$ (all $M \ge 1$) and invokes undefined $B_0, N_0, \mathcal{I}_0$ for all $n \ge 1$

1. **Concrete counterexample to $\mathcal{I}_1(2)$ (L75) as stated:**
   Take $n = 1$ and any $M \ge 1$. Then $B_1 = N_1 = M$, so the bound asserted by $\mathcal{I}_1(2)$ is $(2 B_1)^1 N_1 = 2 M^2$.
   Let Challenger play $a_1 := 2 M$ (e.g., $n = 1, M = 1, a_1 = 2$; or $n = 1, M = 2, a_1 = 4$):
   - Step 1 creates $V_1$ ($s = 1$) since $B_1 a_1 + B_1 = 2 M^2 + M > M = N_1$.
   - Step 2 (Pinned) triggers via $L_1(\vec{a}) = -M + 1 \cdot a_1 = M = N_1 \in [0, N_1]$, setting $e_{1, 1} = 0$ and $e_{1, 0} = 2 M$.
   - Now evaluate $(c_0, c_1) = (M, M) \in [-B_1, B_1]^2$:
     $$L(\vec{a}) = M + M a_1 = 2 M^2 + M > N_1, \qquad v_1(L) = 0, \qquad v_0(L) = 2 M^2 + M.$$
   - **Violation:** $L(\vec{a}) = 2 M^2 + M > 2 M^2 = (2 B_1)^1 N_1$ (at $M = 1$: $3 > 2$; at $M = 2$: $10 > 8$). Running `check-check-2.py`'s own `run_game(1, 1, [(2,)])` or `run_game(1, 2, [(4,)])` fails `assert ... L[0] <= (2 * B[1]) ** k * N[1]` on line 207.
2. **Undefined base-case objects at $k = 1$ (L95–99):**
   Section 2.1 (L50–51) defines $B_k, N_k$ only for $k \in \{1, \dots, n\}$ (and $T_{r, j}$ only for $j \in \{1, \dots, n\}$, L61). Yet Step 2's verification of $\mathcal{I}_k$ (L95–99) unconditionally forms $L^*$ and applies $\mathcal{I}_{k-1}$ with $B_{k-1}, N_{k-1}, T_{r, k-1}$ for all $k \in \{1, \dots, n\}$, which are undefined at $k = 1$ (for every $n \ge 1$).
3. **Required fix:**
   - Replace $(2 B_1)^k N_1$ by $(3 B_1)^k N_1$ in `PROOF.md` L54 ($E_{0, k}$), L75 ($\mathcal{I}_k(2)$), L97, L98, and L112 (note $T_{r, j} > (4 B_1)^{j+1} N_1 > (3 B_1)^j N_1$ and $(B_k + 1)(3 B_1)^{k-1} N_1 \le (3 B_1)^k N_1$ remain valid).
   - Add an explicit 2-line **$k = 1$ base case** in Step 2 (L95): if $k = 1$ is pinned via $c_0^{(1)} + c_1^{(1)} a_1 = d_1 \in [0, N_1]$ ($c_1^{(1)} \ne 0$), then $a_1 \in \mathbb{Z}_{\ge 0}$ with $a_1 \le N_1 + B_1$, $e_{1, r} = 0$ ($r \ge 1$), and $e_{1, 0} = a_1 \le N_1 + B_1 \le \mu_0 + N_1 = E_{0, 1}$ (since $B_1 \le B_1! \le \mu_0$); hence every $(c_0, c_1) \in [-B_1, B_1]^2$ has $v_r(L) = 0$ ($r \ge 1$), $v_0(L) = L(\vec{a}) \in \mathbb{Z}$, and $L(\vec{a}) \le B_1 + B_1(N_1 + B_1) = B_1(N_1 + B_1 + 1) \le 3 B_1 N_1 = (3 B_1)^1 N_1$ (since $1 \le B_1 \le N_1$). Then restrict the elimination argument in L95–99 to $k \ge 2$.

### Defect 2 (BLOCKING — `PROOF.md` L106–109): Step 3 ($r \ge 2$) open-interval wording fails when weak bounds coincide alongside strict bounds, and omits one-sided/empty bound selection

- At level $r \ge 2$ in Step 3, it is possible for a weak lower bound and a weak upper bound to coincide ($\alpha_w = \beta_w$) while strict lower bounds ($< \alpha_w$) and strict upper bounds ($> \beta_w$) are also present (e.g., $n = 3, M = 1$, $a_1 = \omega_1$, $a_2 = \omega_2 + \omega_1 + 8$, $a_3 = \omega_2 + \omega_1 + 4$).
- In this case there is NO "open interval" between the tightest lower and upper bounds as stated in L107; the feasible set is the closed singleton $\{ \alpha_w \}$.
- **Required fix:** Write the exact rational endpoints $\alpha(L) := (-\sum_{i<k} c_i e_{i, r})/c_k$ ($c_k > 0$) and $\beta(L') := (\sum_{i<k} c'_i e_{i, r})/m_k$ ($c'_k = -m_k < 0$), both multiples of $2 B_k! F_{k+1}$ (hence of $F_{k+1}$) with $|\alpha|, |\beta| \le B_k(k-1)E_{k-1}$. State explicitly that for $x \in F_{k+1}\mathbb{Z}$, strict bounds correspond to $x \ge \alpha + F_{k+1}$ / $x \le \beta - F_{k+1}$ and weak bounds to $x \ge \alpha$ / $x \le \beta$. By the four pairwise checks (strict-strict, strict-weak, weak-strict have $\beta - \alpha \ge 2 F_{k+1}$; weak-weak has $\beta - \alpha \ge 0$), the closed interval
  $$I_r := \big[\max(\max_{\text{weak}} \alpha,\; \max_{\text{strict}}(\alpha + F_{k+1})),\;\; \min(\min_{\text{weak}} \beta,\; \min_{\text{strict}}(\beta - F_{k+1}))\big]$$
  is nonempty and its finite endpoint(s) are multiples of $F_{k+1}$ of magnitude $\le B_k(k-1)E_{k-1} + F_{k+1} \le E_k$; choose $x$ to be the left endpoint if lower bounds exist, the right endpoint if only upper bounds exist, or $0$ if $\mathcal{A}_r = \emptyset$. Also note the one-sided / empty-set choice for $r = 1$ (L108).

---

## 4. Minor Precision Fixes to Include in the Same Patch (`PROOF.md`)

1. **L30 (Lemma 1 induction hypothesis):** "$n \ge k - 1$" evaluates to $n \ge 0$ at $k = 1$, whereas Lemma 1 assumes $n \ge 1$; change to "$n \ge \max(1, k - 1)$".
2. **L36 (Lemma 1 additivity):** Fix an injective enumeration (bijection) $M^+ = \{a_1, a_2, \dots\}$ (or note $a_i = a_j \implies b_i = b_j$) and explicitly cover the index-coincidence cases $i = \ell \ne j$ ($y = 0 \implies \exp(y) = 1$ by L37) and $j = \ell \ne i$ ($x = 0 \implies \exp(x) = 1$ by L37).
3. **L64 ($T_{r, j-1}$ range):** "$T_{r, j} - B_j N_j > T_{r, j-1}$ for all $j \ge 1$" references undefined $T_{r, 0}$ at $j = 1$; restrict to $j \in \{2, \dots, n\}$.
4. **L90–101 ($c_k = 0$ tuples & $s \ge 1$ in Step 3):** Add one sentence confirming that tuples with $c_k = 0$ inherit $\mathcal{I}_k$ directly from $\mathcal{I}_{k-1}$ (since $B_k \le B_{k-1}$, $N_k \le N_{k-1}$, $T_{r, k-1} < T_{r, k}$, and $e_{i, s} = 0$ for $i < k$ on any newly created base), and that $s \ge 1$ holds in Step 3 (since $s = 0 \implies B_k a_k + B_k \le N_k \implies a_k \le N_k$, which enters Step 2).
5. **L97 (Step 2 lower bound on $L^*$):** Note explicitly that $L(\vec{a}) > N_k$ gives $L^*(\vec{a}) = c_k^{(1)} L(\vec{a}) - c_k d_1 > N_k - B_k N_k > -N_{k-1}$, so $L^*(\vec{a}) \le N_{k-1}$ implies $|L^*(\vec{a})| \le N_{k-1}$ as needed to invoke $\mathcal{I}_{k-1}(1)$.
6. **L112 ($r = 1$ collision elimination):** Note that $L^{**} = c_k^\dagger L'' - c_k'' L^\dagger$ may be negative, so applying $\mathcal{I}_{k-1}$ to $\pm L^{**}$ gives $|L^{**}(\vec{a})| \le (3 B_1)^{k-1} N_1$ and $v_0(L^{**}) = L^{**}(\vec{a})$, whence $L''(\vec{a}) \le (B_k + 1)(3 B_1)^{k-1} N_1 \le (3 B_1)^k N_1$.

---

## 5. Blocking Defects in Independent Verifier (`notes/check-check-2.py`, for `@check-2`)

1. **Missed $n = 1$ invariant violation:** `check-check-2.py` only ran `run_game(1, 1, [(1,)])` and `run_game(1, 2, [(1,)])`; calling `run_game(1, 1, [(2,)])` or `run_game(1, 2, [(4,)])` crashes line 207.
2. **Broken $r = 1$ collision logic (L158–169):** `check-check-2.py` shifts strict bounds by `+1`/`-1` *before* comparing `max_lb` and `min_ub`, so on any genuine $r = 1$ collision (e.g., `run_game(3, 1, [(0, 1), (8, 1), (4, 1)])` or `run_game(2, 1, [(8,), (4,)])`), `max_lb = alpha + 1 > alpha - 1 = min_ub` and line 169 `assert max_lb <= min_ub` crashes. None of the 10 existing plays exercised an $r = 1$ collision or an $r \ge 2$ weak-weak equality.
3. **Incomplete invariant verification (L199):** Only checks `Tk` ($c_k \ne 0, L \ge 0$), omitting $c_k = 0$ tuples and $\mathcal{I}_k(3)$.

After `@scout-9` patches `PROOF.md`, `@check-2` should update `notes/check-check-2.py` to: (i) use the patched $(3 B_1)^k N_1$ bound, (ii) compute exact rational endpoints $\alpha, \beta$ and handle $r = 1$ collisions and $r \ge 2$ weak/strict closed intervals accurately, (iii) verify ALL tuples (including $c_k = 0$) and $\mathcal{I}_k(3)$, and (iv) include `run_game(1, 1, [(2,)])`, `run_game(1, 2, [(4,)])`, an $r = 1$ collision play (`(3, 1, [(0, 1), (8, 1), (4, 1)])`), and an $r \ge 2$ weak-weak equality play (`(3, 1, [(0, 1, 0), (8, 1, 1), (4, 1, 1)])`).

---

## 6. Re-Audit Verdict (`#1757` / `#1758`) — **PASS**

Re-read the full patched `targets/kovalyov-2611.32205-q1/PROOF.md` (119 lines), `targets/kovalyov-2611.32205-q1/notes/check-check-2.py` (277 lines), and `targets/kovalyov-2611.32205-q1/notes/check-check-2.md` (30 lines) under strict blindness.

1. **Defect 1 resolved (`PROOF.md` L54, L75, L94, L96–101, L113, L116):**
   - Standard upper bound raised uniformly to $(3 B_1)^k N_1$ in $E_{0, k}$, $\mathcal{I}_k(2)$, Step 2, and Step 3 (`(4 B_1)^{j+1} N_1 > (3 B_1)^j N_1` and `(B_k + 1)(3 B_1)^{k-1} N_1 \le (3 B_1)^k N_1` verified).
   - Explicit Step 2 base case $k = 1$ added on L96: $a_1 \in \mathbb{Z}_{\ge 0}$ with $a_1 \le N_1 + B_1 \le \mu_0 + N_1 = E_{0, 1}$, $e_{1, r} = 0$, $e_{1, 0} = a_1$, and $L(\vec{a}) \le B_1(N_1 + B_1 + 1) \le 3 B_1 N_1 = (3 B_1)^1 N_1$ for all $n \ge 1, M \ge 1$. Inductive step L97–101 cleanly restricted to $k \ge 2$.
2. **Defect 2 resolved (`PROOF.md` L107–113):**
   - Exact rational endpoints $\alpha(L), \beta(L') \in 2 B_k! F_{k+1}\mathbb{Z}$ with $|\alpha|, |\beta| \le B_k(k-1)E_{k-1}$ defined explicitly.
   - Closed interval $I_r$ (L111) verified across all four strict/weak pairings for $r \ge 2$, including colliding weak bounds alongside strict bounds, with explicit left/right/$0$ endpoint choices and $|x| \le E_k$; $r = 1$ (L113) cleanly handles both non-colliding $I_1$ and exact $\mathrm{LB} = \mathrm{UB}$ collision.
3. **All §4 minor precision fixes resolved:**
   - L30: bijection $M^+ = \{a_1, a_2, \dots\}$ and $n \ge \max(1, k - 1)$.
   - L36: all five index-coincidence cases for $a_i = x, a_j = y, a_\ell = x + y$ covered in $\mathrm{Win}_{n, 2}$.
   - L64: $T_{r, j} - B_j N_j > T_{r, j-1}$ restricted to $j \in \{2, \dots, n\}$.
   - L90 & L103: $c_k = 0$ inheritance and $s \ge 1$ in Step 3 stated explicitly.
   - L99 & L116: lower bound $L^*(\vec{a}) > -N_{k-1}$ and $\pm L^{**}$ negative handling stated explicitly.
4. **Independent verifier (`notes/check-check-2.py`) verified:**
   - AST check confirms `floats: []`, `float_calls: []`, `divs: []` (exact `int` / `fractions.Fraction` only).
   - Fixed $r = 1$ exact collision check before $\pm F_{k+1}$ shift, closed interval $I_r$ for $r \ge 2$, full tuple verification including $c_k = 0$, $\mathcal{I}_k(3)$, and all 14 standard/nonstandard $\mathbb{Z}\text{-}\mathsf{DOSR}$ plays (including `n=1, a1=2M`, `r=1` collision `(3,1,[(0,1),(8,1),(4,1)])`, and `r>=2` weak-weak equality `(3,1,[(0,1,0),(8,1,1),(4,1,1)])`).
   - Re-executed `.venv/bin/python -u targets/kovalyov-2611.32205-q1/notes/check-check-2.py` -> exit code `0`, `PASS`.

**Final Verdict:** **PASS** (Charter label: `written proof, internally audited`). Ready for Gate 3 freshness check (`<1h`) by `@watch-1 @watch-5 @watch-6`.
