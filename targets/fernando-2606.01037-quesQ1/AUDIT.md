# Blind Audit: `targets/fernando-2606.01037-quesQ1/` (`@audit-1`)

**Verdict:** **PASS**
**Target:** Neranga Fernando & Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, `arXiv:2606.01037v1` (31 May 2026), Section 6 (`draftMay31.tex`, lines 893–895, `\label{Q1}`, **Question 6.1**).
**Answer Verified:** For even $q = 2^m > 2$ ($m \ge 2$), even $e > 0$, and $n = (q - 1) + (q - 1)q^{e/2} + q^e$, the polynomial $g_{n,q} = S_1 + S_{e/2}^{q^{e/2}} + S_e \cdot S_{e/2}^{q-1}$ is a permutation polynomial (PP) of $\mathbb{F}_{q^e}$ **if and only if** either (1) $q = 4$ and $4 \mid e$, **or** (2) $e = 4$ and $m \not\equiv 3 \pmod 4$.
**Audited artifacts (blind):** Primary source `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex` (confirmed `v1` is the sole latest live arXiv version at `https://arxiv.org/abs/2606.01037`), `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, and `notes/check-check-3.py`. (Author `verify.py` and author `notes/` were strictly unread.)

---

## 1. Primary-Source Statement Fidelity & Compiled Numbering

Verified verbatim against `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex`:
- Preamble uses `\newtheorem{thm}{Theorem}[section]`, `\newtheorem{ques}[thm]{Question}`, `\numberwithin{equation}{section}` (L20–35).
- Compiled labels verified:
  - Eq. `(1.1)` (`\label{AB1}`, L74–76): $\sum_{a \in \mathbb{F}_q} (\mathtt{X} + a)^n = g_{n,q}(\mathtt{X}^q - \mathtt{X})$.
  - Section 2, L119: $S_k = \mathtt{X} + \mathtt{X}^q + \cdots + \mathtt{X}^{q^{k-1}}$ ($k \ge 1$), $S_0 = 0$, $S_1 = \mathtt{X}$, $\mathrm{Tr}_{q^e/q} = S_e$.
  - **Question 6.1** (`\label{Q1}`, L893–895, first numbered environment in Section 6):
    *"Let $q>2$ be even, $e>0$ be even, and $n=(q-1)\cdot q^0+(q-1)\cdot q^{e/2}+1\cdot q^e$. Then $g_{n,q}=S_1+S_{e/2}^{q^{e/2}}+S_e\cdot S_{e/2}^{q-1}$. Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}.$"*
  - Appendix Table 1 (`\label{Tb3}`, L1051–1072): desirable triple $(n, e; q) = (307, 4; 4)$ explicitly linked to Question 6.1 (`\ref{Q1}`).
- Both `TARGET.md` and `PROOF.md` match Question 6.1 and all definitions verbatim.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

**Every step across Lemmas 2.1–2.2 and Cases 1–4 is SOUND and complete:**

- **Lemma 2.1 (Explicit formula for $g_{n,q}$, L23–41):**
  - Characteristic-$2$ telescoping $S_r(Y) = X^{q^r} + X$ for $Y = X^q + X$, reduction $g_{l+q^{2k}, q}(Y) = g_{l+1, q}(Y) + S_{2k}(Y)g_{l,q}(Y)$, Lucas expansion $(Z + a)^{q-1} = \sum_{j=0}^{q-1} Z^j a^{q-1-j}$, and exact $\mathbb{F}_q$ power-sum evaluation (critically using $q > 2$ so $(q - 1) \nmid q$ at $j = 0$ in $g_{l+1,q}$) rigorously yield $g_{l,q}(Y) = 1 + S_k(Y)^{q-1}$, $g_{l+1,q}(Y) = Y + S_k(Y)$, and $g_{n,q}(X) = X + S_k(X)^{q^k} + S_{2k}(X) S_k(X)^{q-1}$ in $\mathbb{F}_2[X]$.
- **Lemma 2.2 (Reduction to $\Phi$ on $V_k = \mathrm{im}(S_k)$, L45–61):**
  - $S_k(x) = 0 \iff x \in \ker(\mathrm{Tr}_{q^k/q}) \subset \mathbb{F}_{q^k}$ gives $|\ker(S_k)| = q^{k-1}$, $|V_k| = q^{k+1}$, and $V_k = \{y \in \mathbb{F}_{q^{2k}} : t(y) := y + y^{q^k} \in \mathbb{F}_q\}$ by exact counting ($q$ values of $t \in \mathbb{F}_q$, each with $q^k$ solutions to $y^{q^k} + y = t$).
  - Fiber bijection $x \leftrightarrow y = S_k(x)$ with explicit inverse $x = b + y^{q^k} + t(y) y^{q-1}$ establishes $\#\{x \in \mathbb{F}_{q^{2k}} : g_{n,q}(x) = b\} = \#\{y \in V_k : \Phi(y) = S_k(b)\}$ for all $b$, proving $g_{n,q}$ is a PP on $\mathbb{F}_{q^{2k}}$ iff $\Phi$ is bijective on $V_k$; $\mathbb{F}_q$-homogeneity of $\Phi$ is verified at both $c \in \mathbb{F}_q^*$ and $c = 0$ ($q - 1 \ge 3$).
- **Case 1 ($e \equiv 2 \pmod 4$, $k$ odd $\implies$ never PP, L69–75):**
  - On $\mathbb{F}_{q^k}$, $S_{2k}(x) = 0$ and $g_{n,q}(x) = x + \mathrm{Tr}_{q^k/q}(x)$. Choosing $x \in \mathbb{F}_{q^k}$ with $c := \mathrm{Tr}_{q^k/q}(x) \neq 0$ and $x' = x + c \neq x$ gives $\mathrm{Tr}_{q^k/q}(x') = c + k c = 0$ and $g_{n,q}(x') = g_{n,q}(x)$.
- **Case 2 ($q = 4$, $4 \mid e$, $k \ge 2$ even $\implies$ always PP, L79–127):**
  - Step 2.1: $\Phi|_{\mathbb{F}_{4^k}}(y) = y + \mathrm{Tr}_{4^k/4}(y)$ is an involution since $k$ is even.
  - Step 2.2: For $t = t(y) \in \mathbb{F}_4^*$, $s(y) = t + t^2 S_k(y)^2 + S_k(y)$; setting $z = S_k(y)/t$ gives $z^4 + z = 1$, $r = z^2 + z \in \{\omega, \omega^2\}$, and $s(y)/t = 1 + r \in \{\omega, \omega^2\}$, so $s(y) \notin \{0, t\}$.
  - Step 2.3: Exact invariant $\Phi(y)^4 + \Phi(y) = (y^2 + ty)^2$ forces $y_1^2 + t_1 y_1 = y_2^2 + t_2 y_2$ on any collision $\Phi(y_1) = \Phi(y_2)$.
    - $t_1 = t_2$: $y_2 = y_1 + t_1 = y_1^{4^k}$ contradicts $\Phi(y_1^{4^k}) = \Phi(y_1)^{4^k} = \Phi(y_1) + s \neq \Phi(y_1)$ (using $\Phi \in \mathbb{F}_2[y]$).
    - $t_1 \neq t_2$: scaling by $1/t_1$ ($\mathbb{F}_4$-homogeneity) and applying $\mathbb{F}_2$-Frobenius normalizes to $(t_1, t_2, s) = (1, \omega, \omega^2)$. Setting $A = y_1^2 + y_1 = y_2^2 + \omega y_2 \in \mathbb{F}_{4^k}$ ($S_k(A) = \omega$) yields exact closed forms $\Phi(y_1) = \omega^2 y_1 + \omega + P(A) + Q(A)$ and $\Phi(y_2) = \omega y_2 + 1 + P(A) + \omega Q(A)$, whose sum gives $W = \omega^2 y_1 + \omega y_2 = \omega^2(1 + Q(A))$ and $Q(A)^2 + Q(A) = \omega^2 A$, contradicting the algebraic identity $1 + Q(A) + Q(A)^2 = a_0 \sum_{j=0}^{k-1} a_j^2 = \omega^2 A$ (verified for all even $k \ge 2$).
- **Case 3 ($q \ge 8$, $4 \mid e$, $e \ge 8$, $k \ge 4$ even $\implies$ never PP, L131–155):**
  - On $y = u + \alpha$ ($\alpha^{q^k} = \alpha + 1$, $u \in \mathbb{F}_{q^k}$), $s(u + \alpha) = 1 + \mathrm{Tr}_{q^k/q}(f(u))$ where $f(u) = (u + \alpha)^{q-1} + (u + \alpha + 1)^{q-1} = \sum_{j=0}^{q-2} (u + \alpha)^j \in \mathbb{F}_{q^k}[u]$ (coefficientwise $q^k$-Frobenius-invariant since $\alpha \leftrightarrow \alpha + 1$ swaps the two summands) has $u^{q-2}$ and $u^{q-3}$ coefficients equal to $1$.
  - Trace-preserving reduction $a_{2r} u^{2r} \mapsto a_{2r}^{1/2} u^r$ maps all even-degree terms of $c f(u)$ ($c \in \mathbb{F}_q^*$) to degree $\le q/2 - 1 < q - 3$ (valid for all $q \ge 8$), leaving exact odd degree $q - 3 \ge 5$, so $\gcd(q - 3, q^k) = 1$.
  - Lidl–Niederreiter Theorem 5.38 (Carlitz–Uchiyama bound) applies directly and gives $|\sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(c f(u))}| \le (q - 4) q^{k/2}$. Character orthogonality yields $q \cdot \#\{u : s(u + \alpha) = 0\} \ge q^{k/2}(q^{k/2} - (q^2 - 5q + 4)) > 0$ for all $k \ge 4, q \ge 8$, producing a collision with the bijection $\Phi|_{\mathbb{F}_{q^k}}$.
- **Case 4 ($e = 4$, $k = 2$, $q = 2^m > 2 \implies$ PP iff $m \not\equiv 3 \pmod 4$, L158–206):**
  - On $U = \{u \in \mathbb{F}_{q^4} : u^{q^2} = u + 1\}$, the involution $u \leftrightarrow x = u/(u + 1)$ gives a bijection $U \xrightarrow{\sim} \mu_{q^2 + 1} \setminus \{1\}$ and transforms $\Phi(u) = \frac{x + y^2}{xy(x + 1)(y + 1)}$ ($y = x^q$) to satisfy $\Phi(u)^{q^2} = x^{q + 2}\Phi(u)$ and $s(u) = (1 + x^{q + 2})\Phi(u)$.
  - Exact Euclidean identities $4(q^2 + 1) = (2q - 1)(2q + 1) + 5$ and $q^2 + 1 = (q + 2)(q - 2) + 5$ show $\gcd(2q - 1, q^2 + 1) = \gcd(q + 2, q^2 + 1)$ equals $5$ if $m \equiv 3 \pmod 4$ and $1$ otherwise.
  - $m \equiv 3 \pmod 4$: any order-$5$ element $x \in \mu_{q^2 + 1} \setminus \{1\}$ gives $x^{2q - 1} = 1 \implies \Phi(u) = 0 = \Phi(0)$, so not PP.
  - $m \not\equiv 3 \pmod 4$: $\Phi(u) \neq 0$ and $s(u) \neq 0$ on all of $U$; $\Psi(u) = \Phi(u)/s(u) = 1/(1 + x^{q + 2}) \in U$ conjugates to the automorphism $x \mapsto x^{-(q + 2)}$ of $\mu_{q^2 + 1} \setminus \{1\}$, hence $\Psi : U \to U$ is bijective; combined with $\mathbb{F}_q$-homogeneity and $\Phi|_{\mathbb{F}_{q^2}}(y) = y^q$, $\Phi : V_2 \to V_2$ is bijective.
- **Exhaustive case partition (Section 4, L210–217):** Cases 1–4 cleanly partition all $(q, e)$ with even $q = 2^m > 2$ and even $e \ge 2$, agreeing at the overlap $(q, e) = (4, 4)$.

---

## 3. Exact Computational Verification

- **Independent checker (`notes/check-check-3.py`):**
  - AST audit confirmed zero floating-point literals, zero `float()` calls, and zero `/` operators (`FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: []`).
  - Auditor additionally ran Rabin's exact irreducibility test over $\mathbb{F}_2$ on all 16 defining polynomials in `IRRED_MODS` ($N \in \{2, \dots, 32\}$): all 16 confirmed genuinely irreducible over $\mathbb{F}_2$.
  - Executed `.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py`: exited `0`, raw output `PASS` (verified Lemma 2.1 exact polynomial identity, Lemma 2.2 + exhaustive PP checks up to $N = 16$ + Table 1 triple `(307, 4; 4)`, Case 1 collisions, Case 2 Steps 2.1–2.3 & $P(A), Q(A)$ identities for $k \in \{2, 4, 6\}$, Case 3 Lucas/odd-degree/Weil bound & explicit collisions for $(8, 8)$ and $(16, 8)$, and Case 4 unit-circle conjugation & exact gcd split for $m = 2, \dots, 8$ up to $\mathbb{F}_{2^{32}}$).

---

## 4. Handoff

- **Result Label:** `written proof, internally audited`
- **Verification Command:** `.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py`
- **Files:** `targets/fernando-2606.01037-quesQ1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Handing off directly to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness (`< 1h`) and subsequent `@coordinator` reporting.
