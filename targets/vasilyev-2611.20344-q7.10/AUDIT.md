# Blind Audit: `targets/vasilyev-2611.20344-q7.10/` (`@audit-1`)

**Verdict:** **PASS (re-audit after `#1730`/`#1733` fixes)**
**Target:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (`updown.tex`), Subsection 5.4 (`\subsection{Uniform descent}\label{sec:uniform}`, lines 1486–1622) and Section 7, **Question 7.10** (`q:supremum`, lines 2049–2052).
**Answer Verified:** **YES** — $\sup_{S, C} \pi_C(S) = \log_3 2$ over all uniformly descending sets $S \subseteq \mathbb{N}$ periodic modulo a power of $2$ and all closed classes $C$ of $\mathcal{R}_k(S)$.
**Audited artifacts (blind):** Primary source `tools/.arxiv_cache/eprint/2611.20344/updown.tex` (confirmed `v2` is still the latest live arXiv version at `https://arxiv.org/abs/2611.20344`), `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, and `notes/check-check-2.py`. (Author `verify.py` and author `notes/` were strictly unread.)

---

## 1. Primary-Source Statement Fidelity & Compiled Numbering

Verified verbatim against `tools/.arxiv_cache/eprint/2611.20344/updown.tex`:
- Preamble uses `\newtheorem{theorem}{Theorem}[section]` (shared counter reset per section) and `\numberwithin{table}{section}` (L13–24).
- Exact compiled labels in `updown.tex`:
  - `def:TS` = **Definition 1.1** (L98)
  - `def:residue` = **Definition 5.3** (L1265, in Subsection 5.2 `sec:fresh`)
  - `def:pi` = **Definition 5.8** (L1382, in Subsection 5.3)
  - `sec:uniform` = **Subsection 5.4** (*Uniform descent*, L1486–1622)
  - `def:uniform` = **Definition 5.10** (L1491)
  - `thm:uniform` = **Theorem 5.11** (L1512)
  - `tab:uniformcount` = **Table 5.3** (L1607–1622)
  - `q:supremum` = **Question 7.10** (L2049–2052): *"Is the supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ equal to $\log_3 2$? Modulo $16$ the largest value is $73/174=0.420$ (Table 5.3)."*
- Scope check: In `updown.tex`, both `Definition 5.8` (`def:pi`) and `Definition 5.10` (`def:uniform`) are defined exclusively for sets $S \subseteq \mathbb{N}$ periodic modulo a power of $2$ ($M = 2^k$, $k \ge 1$). Thus restricting to periodic sets modulo $2^k$ matches Question 7.10 verbatim.
- All three `#1729` citation/hygiene fixes verified in place:
  1. `TARGET.md` L2 (`Subsection 5.4 (sec:uniform, lines 1486–1622)`) and L17 (`Table 5.3`).
  2. `PROOF.md` L45 (`Vasilyev §5.4`).
  3. `PROOF.md` §7: unverified/unspecified mod-256 witness item 4 removed cleanly; items 1–3 match the independently verified results.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md` (Sections 1–6)

**Every mathematical step in Sections 1–6 is SOUND and complete:**

- **Section 1 (Preliminaries & Part 1 Upper Bound, L21–46):**
  - The extension of $U(x) = (3x + e)/2$, $D(x) = (x + e)/2$ to $x \in \mathbb{Z}$ agrees with Vasilyev's $\hat{r} \in \{1, \dots, 2^k\}$ representative modulo $2^{k-1}$ for all $k \ge 1$, including $r = 0$ ($\hat{r} = 2^k$).
  - Since every vertex in $\mathcal{R}_k(S)$ has out-degree $2$, the finite graph has at least one sink SCC $C$ and at least one simple directed cycle, so $\mu^* < \log_3 2$ is well-defined.
  - The Bellman potential $h(u) = \inf\{\sum_{i=0}^{t-1}(\mu^* - \mathbf{1}_{u_i \in S}) : t \ge 0,\text{ walks in } C\}$ is finite in $(-\infty, 0]$ (every walk decomposes into a simple path of length $< |C|$ and simple cycles of weight $\ge 0$), satisfies $\mathbf{1}_{u \in S} - \mu^* \le h(v) - h(u)$ on every edge $u \to v$ in $C$, and integrating against $\mu_C$ yields $\pi_C(S) \le \mu^* < \log_3 2$.
- **Section 2 (Dyadic-Shell Base Sets & Lemma 1, L49–99):**
  - For $m \ge 2$ and $J \subseteq \{0, \dots, m - 2\}$, the membership condition $x \bmod 2^m \in S_0(J)$ is rigorously equivalent on all of $\mathbb{Z}_2$ (including $x = 0$, $v_2(0) = \infty \notin J$) to "$x$ odd, or $x = 2u$ with $v_2(u) \in J$". Exact density $\lambda(S_0) = 1/2 + \sum_{j \in J} 2^{-(j+2)}$ sweeps all dyadic rationals in $[1/2, 1)$.
  - **Lemma 1(a):** Forward $2$-Lipschitz bound $x \equiv x' \pmod{2^d} \implies T_{S_0}(x) \equiv T_{S_0}(x') \pmod{2^{d-1}}$ holds for all $d \ge 1$ (crucially including $1 \le d < m$ because even-branch multipliers depend only on $v_2(u)$).
  - **Lemma 1(b):** Both preimage branches $x_1(y) = 3^{-1}(2y - 1)$ and $x_0(y) \in \{2 \cdot 3^{-1} y, 2y\}$ are unique and satisfy $v_2(x_b(y) - x_b(y')) = 1 + v_2(y - y')$ for all $y, y' \in \mathbb{Z}_2$ (verified including $y = 0$, $y = y'$, and distinct valuations via the strong ultrametric triangle inequality).
  - **Lemma 1(c):** Well-definedness and bijectivity of $\Phi_n : \mathbb{Z}/2^n\mathbb{Z} \to \{0, 1\}^n$ for all $n \ge 1$ follow by induction from (a)–(b). For $n \ge m$, $\Phi_n$ conjugates $P_0$ to the binary De Bruijn random walk, yielding $P_0^n = \mathbf{1}\lambda_n^\top$.
- **Section 3 (Barina First-Exit Sieve & Lemma 2, L102–145):**
  - With $n = m + L - 1 \ge m$, $W_j(r)$ ($1 \le j \le L$) is well-defined on $\mathbb{Z}/2^n\mathbb{Z}$, and $B_n \subseteq S_0^{(n)}$ since $r \notin S_0^{(n)} \implies W_1(r) = -\mu < 0$.
  - **Lemma 2(a):** Induction on $s \in \{0, \dots, \tau(r) - 1\}$ (vacuous inductive step when $\tau(r) = 1$, including $L = 1$) checks all modulus bounds ($n - s + 1 \ge m + 1 \ge 3$ and $n - s - i \ge m + L - \tau(r) \ge m \ge 2$), giving $W_{\tau(r) - s}(u_s) = W_{\tau(r)}(r) - W_s(r) < 0 \implies u_s \notin B_n$, and total weight $W_{\tau(r)}(r) < 0$.
  - **Lemma 2(b):** Pigeonhole cycle decomposition on $a_0 < a_1 < \dots < a_\ell$ yields $d \ge 1$ full traversals partitioned into $q - p \ge 1$ negative-weight blocks, proving $a/\ell < \mu < \log_3 2$.
- **Section 4 (Hoeffding Bound & Lemma 3, L148–169):**
  - Disjointness of $m$-bit windows on each residue class $I_r$ ($0 \le r < m$, $|I_r| \ge \lfloor L/m \rfloor \ge 1$ for $L \ge m$), self-contained cumulant bound $\psi''(t) = q(t)(1 - q(t)) \le 1/4 \implies \psi(t) \le t^2/8$, choice $t = 4\delta$, and union bound over $m$ classes are completely rigorous.
- **Section 5 (Path-Multiplicity Bound — Lemmas 4 & 5, L172–225):**
  - **Lemma 4(a):** Forward determination of $x_t \bmod 2^{n-t}$ (hence parity $p_t$) from $(y, \mathcal{T} \cap \{0, \dots, t - 1\})$ holds cleanly for both $t \in \mathcal{T}$ (using $D(a) - D(b) = (a-b)/2$) and $t \notin \mathcal{T}$ (using Lemma 1(a)).
  - **Lemma 4(b):** Backward uniqueness from $t = n$ down to $0$ works for both $t \in \mathcal{T}$ ($x_t \equiv 2x_{t+1} - p_t \pmod{2^n}$, valid including $r = 0$ and $r = 2^n - 1$) and $t \notin \mathcal{T}$ ($x_t \equiv x_{p_t}(x_{t+1}) \pmod{2^n}$ via Lemma 1(b)).
  - **Lemma 5(a)–(c):** If $A_1, A_2 \in \mathcal{F}_0(y)$ first disagree at $t \in A_1 \setminus A_2$ ($0 \le t \le L - 1$, vacuous at $t = 0$), Lemma 4(a) gives $x_t^{(2)} \equiv x_t^{(1)} \pmod{2^{n-t}}$, Lemma 1(a) preserves congruence mod $2^m$ through $i = L - 1 - t$ (since $n - t - i \ge m$), forcing $W_j(x_t^{(2)}) = W_j(x_t^{(1)}) \ge 0$ for $1 \le j \le L - t$ and hence $\tau(x_t^{(2)}) \ge L - t + 1$. Extending the subpath from $x_t^{(2)}$ to length $\tau(x_t^{(2)})$ if needed (out-degree $2 \ge 1$) and applying Lemma 2(a) forces $x_u^{(2)} \notin B_n$ for all $u \in \{t, \dots, L - 1\}$. Thus $\mathcal{F}_0(y)$ is totally ordered by inclusion ($|\mathcal{F}_0(y)| \le L + 1$), $|\mathcal{F}(y)| \le 2^{m-1}(L + 1)$, and $P_n^n(y, z) \le 2^{-n} \cdot 2^{m-1}(L + 1)$.
- **Section 6 (Theorem 6 & Completion of Part 2, L228–260):**
  - All three inequalities ($\mu_C(B_n) \le 2^{m-1}(L+1)\lambda_n(B_n)$, $\|\mu_C - \lambda_n\|_1 \le 2n\mu_C(B_n)$ via De Bruijn telescoping $\mu_C(P_n^n - P_0^n)$ and row-stochastic $\ell_1$-contraction, and $\pi_C(S_n) \ge \lambda(S_0) - (n + 1)\mu_C(B_n)$) and the asymptotic limit as $L \to \infty$ are completely rigorous.

---

## 3. Exact Computational Verification

- **Independent checker (`notes/check-check-2.py`):**
  - AST audit confirmed zero floating-point literals or `float()` calls (`FLOATS: []`, `FLOAT_CALLS: []`; all 5 `/` operators on lines 51, 343, 345, 346, 348 are exact `Fraction` divisions).
  - Executed `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py`: exited `0`, raw output `PASS` (verified primary-source numbering & `Subsection 5.4`/`Table 5.3`/`Vasilyev §5.4` fixes, Table 5.3 baseline mod 4/8 + mod-16 optimal witness `73/174`, Lemma 1 across 6 base sets, and Lemmas 2–5 + Theorem 6 exhaustively over `57,344` length-$n$ paths across 5 Barina sieve instances up to $N = 128$).
- **Auditor's independent adversarial stress test:**
  - Wrote and ran a from-scratch exact `Fraction` test covering the $L = 1$ edge cases ($m = 2, 3$), high-density base set $(m = 3, J = \{1\}, \lambda = 5/8, \mu = 63/100)$ for $L = 1, \dots, 5$ ($n = 3, \dots, 7$), and Collatz base set $(m = 2, J = \emptyset, \lambda = 1/2, \mu = 3/5)$ for $L = 1, \dots, 8$ ($n = 2, \dots, 9$, up to $N = 512$). Every assertion of Lemmas 1, 2(a)–(b), 4(a)–(b), 5(a)–(c), and Theorem 6 passed with zero violations (`Command exited with code 0`, `ALL ADVERSARIAL TESTS PASSED!`).

---

## 4. Handoff

- **Result Label:** `written proof, internally audited`
- **Verification Command:** `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py`
- **Files:** `targets/vasilyev-2611.20344-q7.10/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
- Handing off directly to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness (`< 1h`) and subsequent `@coordinator` reporting.
