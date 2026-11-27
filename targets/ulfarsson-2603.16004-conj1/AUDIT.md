# Adversarial Audit Report (`audit-1`): `targets/ulfarsson-2603.16004-conj1/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Henning Ulfarsson, *A Permutation Avoidance Game with Reverse Replies and Monotone Traps*, `arXiv:2603.16004v1` (2026-03-16), Section 2, **Conjecture 2.9** (`\label{conj:general-reverse}`)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2603.16004v1/ItsAllFunAndGamesUntilMonotonicity.tex` (verified live arXiv latest version is `2603.16004v1`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Statement Fidelity
- Verified verbatim against `ItsAllFunAndGamesUntilMonotonicity.tex` (shared `[theorem]` counter across all environments in L16–27):
  - **Definition 1.1** (L59–64): normal-play impartial game PAP with pattern length $k \ge 1$ on subsets $X \subseteq S_n$.
  - **Definition 2.1** (L120–131) & L133–134: Sprague–Grundy value $\mathrm{sg}(X)$ and $\mathrm{sg}(S_n, k)$.
  - **Conjecture 2.9** (`\label{conj:general-reverse}`, L371–375): *"For every $k \geq 3$, there exists $n_0(k)$ such that the reverse strategy is a winning strategy for Player II on $S_n$ for all $n \geq n_0(k)$. In particular, $\mathrm{sg}(S_n, k) = 0$ for all such $n$."*
  - **Definition 2.10** (L380–385), **Lemma 2.11** (L387–391), **Proposition 2.12** (L397–402), and **Corollary 2.13** (L417–422) match every section/environment citation in `TARGET.md` and `PROOF.md` verbatim.
  - Checked all later references to `\ref{conj:general-reverse}` (L1464, L1783): no hidden hypotheses or later caveats; the paper explicitly remarks that general $k$ likely requires a new idea beyond the $k = 4$ witness-family analysis.

## 2. Adversarial Line-by-Line Mathematical Audit
- **Threshold arithmetic (`PROOF.md` §1–2, L11–34):** $n_0(k) = k + ((2k+1)(k-1))^2 + 1 = 4k^4 - 4k^3 - 3k^2 + 3k + 2$ verified algebraically; for all $k \ge 3$ and $n \ge n_0(k)$, $n > (k-1)^2 + 1$, $n - k \ge ((2k+1)(k-1))^2 + 1 > 2k - 2 > k$, and $n - k + 1 > n - k > k$ all hold unconditionally.
- **Proposition 1 (Monotone Trap & Conditional Reverse-Reply Criterion, L38–47):** Self-contained and airtight: maintains reverse-closed monotone-free invariant $F$ (using $p^r(1) = p(k) \neq p(1)$ for $k \ge 3$), handles Case B monotone move via $\mathrm{id}_n^r \in \mathrm{Av}_n(F \cup \{\mathrm{id}_k\})$ (noting $n \ge (k-1)^2 + 1 > k$ for $k \ge 3$) and Erdős–Szekeres termination $\mathrm{Av}_n(F \cup \{\mathrm{id}_k, \mathrm{id}_k^r\}) = \emptyset$, and proves $\mathrm{sg}(S_n, k) = 0$ by strong induction on finite $|X|$.
- **Lemma 0 (Monotone 1-Point Inflations, L53–79):**
  - (1) Reversal identity $(I_t(\gamma, j, \varepsilon))^r = I_t(\gamma^r, m+1-j, -\varepsilon)$: exact.
  - (2) Shadow stabilization $\mathrm{Sh}_k(I_t(\gamma, j, \varepsilon)) = \mathrm{Sh}_k(I_k(\gamma, j, \varepsilon))$ for $t \ge k$: exact (including $r = 0$, $r = k$, $m = 1$).
  - (3) Contiguous monotone-block inflation $\mathrm{std}((R \cap A) \cup B') = I_t(\tau, j, \varepsilon)$ for $s = |R \cap B| \ge 1$ and $|B'| = t + s - 1$: both $\varepsilon = +$ and $\varepsilon = -$ cases verified verbatim (including $s = 1$ and $s = m$).
- **Lemma 1 (Erdős–Szekeres 1-Point Inflation Extraction, L85–110):** Exact: $|U| = n - k \ge ((2k+1)(k-1))^2 + 1$ yields a monotone subset $M \subseteq U$ of length $(2k+1)(k-1)+1$; the strictly increasing invariant $a(z)+b(z) \in \{0,\dots,2k\}$ ($\varepsilon = +$) or $a(z)-b(z) \in \{-k,\dots,k\}$ ($\varepsilon = -$) bounds the number of visited grid cells by $2k+1$; pigeonhole produces a $k$-point subset $Q \subseteq M$ in one cell $(a_0, b_0)$; Lemma 0(3) and Lemma 0(2) (using $n - k \ge k$) yield $\sigma = I_{n-k}(\beta, i_0, \varepsilon) \in \mathrm{Av}_n(F)$ with $\Gamma(\sigma) = P_0 \sqcup B_0$, $\mathrm{std}(P_0) = p$, $|B_0| = n - k$.
- **Lemma 2 (Reduction to Self-Inflation Dichotomy, L116–148):** Airtight across all branches:
  - Case 1 ($p \notin \mathrm{Sh}_k(\sigma^r)$): $\sigma^r$ directly witnesses legality of $p^r$ from $F \cup \{p\}$.
  - Case 2 ($p \in \mathrm{Sh}_k(\sigma^r)$): $p^r = \mathrm{std}(R_1) \in \mathrm{Sh}_k(\sigma)$ forces $1 \le s_1 = |R_1 \cap B_0| \le k - 1$ (ruling out $s_1 = 0$ by $p^r \neq p$ and $s_1 = k$ by non-monotonicity of $p$); hence $k + s_1 - 1 \le 2k - 2 \le |B_0|$, producing $\omega_1 = I_{n-k+1}(p^r, j_1, \varepsilon) \in \mathrm{Av}_n(F)$ with $p^r \le \omega_1$.
  - Subcase 2a ($p \notin \mathrm{Sh}_k(\omega_1)$): $\omega_1$ witnesses legality.
  - Subcase 2b ($p \in \mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon))$): selecting $P_2 \subseteq (R_1 \cap P_0) \cup B'$ with $\mathrm{std}(P_2) = p$ forces $s_2 = |P_2 \cap B_0| \ge s_1 \ge 1$ (since $|R_1 \cap P_0| = k - s_1$) and $s_2 \le k - 1$ (non-monotonicity); reflecting via $\rho$ produces $R_2 = \rho(P_2) \subseteq \Gamma(\sigma^r)$ with $\mathrm{std}(R_2) = p^r$ and $|R_2 \cap B_0^r| = s_2 \in [1, k-1]$, yielding $\omega_2 = I_{n-k+1}(p^r, j_2, -\varepsilon) \in \mathrm{Av}_n(F)$ with $p^r \le \omega_2$, and Theorem 3 excludes $p \in \mathrm{Sh}_k(\omega_2)$.
- **Theorem 3 (Self-Inflation Dichotomy, Claims 3A–3B, L153–223):**
  - Claim 3A: $2 \le t = |S \cap W| \le k - 1$ (ruling out $t = 0$ by $|A| = k-1$, $t = 1$ by $p \neq p^r$, $t = k$ by non-monotonicity); collapsing $S \cap W$ to its leftmost point $w_0$ yields $q \in S_m$ ($2 \le m \le k-1$) with $q^r \le p$, exact ascent/descent preservation (checked left boundary $a = 1$, internal deleted pairs, and right boundary $a + t \le k$ vs $a + t = k + 1$), and exact endpoint order preservation $p(1) < p(k) \iff q(1) < q(m)$ (since $|B| = t \le k - 1$ prevents $B$ from containing both $1$ and $k$).
  - Claim 3B: Disjoint index intervals $\{r_j, \dots, r_{j+1}-1\}$ give $\mathrm{asc}(\tau) \le \mathrm{asc}(\pi)$ and, upon equality, force zero ascents in $\{1, \dots, r_1 - 1\}$ and $\{r_m, \dots, k - 1\}$, hence $\pi(1) \ge \pi(r_1)$ and $\pi(r_m) \ge \pi(k)$; complementation $\pi^c$ yields the symmetric descent statement.
  - Theorem 3 conclusion: Cyclic chain $\mathrm{des}(p) = \mathrm{des}(q_+) = \mathrm{asc}(q_+^r) \le \mathrm{asc}(p) = \mathrm{asc}(q_-) = \mathrm{des}(q_-^r) \le \mathrm{des}(p)$ forces equality throughout; Claim 3B rigidity plus Claim 3A(3) contradicts both $p(1) < p(k)$ ($p(1) \ge p(r_1) > p(r_{m_+}) \ge p(k)$) and $p(1) > p(k)$ ($p(1) \le p(u_1) < p(u_{m_-}) \le p(k)$).
- **Main Theorem (§7, L229):** Combines Theorem 3, Lemma 2, and Proposition 1 cleanly without gaps.

## 3. Independent Verification & Novelty Status
- **Independent checker:** Executed `.venv/bin/python -u targets/ulfarsson-2603.16004-conj1/notes/check-check-2.py` -> exit code `0`, `PASS` (verified $n_0(k)$ for $k=3..500$, Lemma 0(1)–(3), Lemma 2 witness constructions exhaustively for $k=3,4$, Claims 3A/3B & Theorem 3 exhaustively for $k=3..6$, and exact PAP Sprague–Grundy/reverse-strategy game trees for $k=3, n=3..6$).
- **Gate 2 novelty receipts:** `notes/novelty-gate2-watch-1.md` (`#552`), `notes/novelty-gate2-watch-6.md` (`#561`), and `notes/novelty-attack.md` all clear; live arXiv confirmed `2603.16004v1` is still latest.
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
