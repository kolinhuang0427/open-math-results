# Independent Check Report: `targets/fernando-2606.01037-quesQ1/`

- **Checker:** `@check-3`
- **Target:** `targets/fernando-2606.01037-quesQ1/TARGET.md` (`arXiv:2606.01037v1`, Section 6, Question 6.1 `\label{Q1}`)
- **Proof checked:** `targets/fernando-2606.01037-quesQ1/PROOF.md` (complete iff classification: $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff ($q = 4$ and $4 \mid e$) or ($e = 4$ and $m \not\equiv 3 \pmod 4$))
- **Gate 2 Watch:** **PASS** (`watch-1` `#1779`, `watch-6` `#1780`, `watch-5` `#1781`)

## 1. Primary Source Verification

- **arXiv version check:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2606.01037` confirms `2606.01037v1` is the sole arXiv version (`published: 2026-05-31T06:04:17Z`).
- **Cached TeX:** `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex` (1,167 lines).
- **Statement match (`draftMay31.tex` L893–895):**
  > **Question 6.1 (`\label{Q1}`):** *"Let $q>2$ be even, $e>0$ be even, and $n=(q-1)\cdot q^0+(q-1)\cdot q^{e/2}+1\cdot q^e$. Then $g_{n,q}=S_1+S_{e/2}^{q^{e/2}}+S_e\cdot S_{e/2}^{q-1}$. Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}.$"*
  Matches `TARGET.md` verbatim.
- **Auxiliary references verified:** Eq. `(1.1)` (`\label{AB1}`, L74–76), desirable triple definition & Table 1 `(n,e;q) = (307,4;4)` (`L82`, `L1072`), and $S_k$ definition (`L119`).

## 2. Proof Audit Summary

- **Lemmas 2.1–2.2:** Characteristic-$2$ Lucas formula and $Y = X^q + X$ reduction yield $g_{n,q}(X) = X + S_k(X)^{q^k} + S_{2k}(X)S_k(X)^{q-1}$, and $g_{n,q}$ is a PP on $\mathbb{F}_{q^{2k}}$ iff the $\mathbb{F}_q$-homogeneous map $\Phi(y) = y + S_k(y) + k\cdot t(y) + t(y)S_k(y^{q-1})$ is a bijection on $V_k = \{y \in \mathbb{F}_{q^{2k}} : t(y) := y + y^{q^k} \in \mathbb{F}_q\} = \mathrm{im}(S_k)$.
- **Case 1 ($e \equiv 2 \pmod 4$, $k$ odd):** Collides on $\mathbb{F}_{q^k}$ via $x' = x + \mathrm{Tr}_{q^k/q}(x)$ when $\mathrm{Tr}_{q^k/q}(x) \neq 0$.
- **Case 2 ($q = 4, 4 \mid e$):** $\Phi|_{\mathbb{F}_{4^k}}$ is an involution; on $V_k \setminus \mathbb{F}_{4^k}$, $s(y)/t(y) \in \{\omega, \omega^2\}$ avoids $0$ and $t(y)$, and $\Phi(y)^4 + \Phi(y) = (y^2 + ty)^2$ rules out both $t_1 = t_2$ and $t_1 \neq t_2$ collisions via the quadratic $Q(A)^2 + Q(A) = \omega^2 A$ vs $1 + Q(A) + Q(A)^2 = \omega^2 A$ contradiction.
- **Case 3 ($q \ge 8, 4 \mid e, e \ge 8$):** For $y = u + \alpha$ ($t(\alpha)=1$), $f(u) = \sum_{j=0}^{q-2}(u+\alpha)^j$ reduces under $\mathrm{Tr}_{q^k/2}$ to exact odd degree $q-3 \ge 5$, so Carlitz–Uchiyama gives $\#\{u : s(u+\alpha)=0\} \ge q^{k/2-1}(q^{k/2} - (q^2 - 5q + 4)) > 0$, colliding with $\Phi|_{\mathbb{F}_{q^k}}$.
- **Case 4 ($e = 4$):** Unit-circle map $x = u/(u+1)$ conjugates $\Phi(u)$ to satisfy $\Phi(u)^{q^2} = x^{q+2}\Phi(u)$ and $\Psi(u) = \Phi(u)/s(u) \leftrightarrow x^{-(q+2)}$ on $\mu_{q^2+1} \setminus \{1\}$, splitting cleanly by $\gcd(2q-1, q^2+1) = \gcd(q+2, q^2+1) \in \{1, 5\}$ at $m \equiv 3 \pmod 4$.

## 3. Exact Mechanical Verification (`check-check-3.py`)

Command:
```sh
.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py && .venv/bin/python -c "import ast; tree = ast.parse(open('targets/fernando-2606.01037-quesQ1/notes/check-check-3.py').read()); floats = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]; calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'float']; print('FLOAT_COUNT:', len(floats), 'FLOAT_CALLS:', len(calls))"
```

Exact output:
```text
Part 1 (Lemma 2.1 exact polynomial identity sum (X+a)^n = g_{n,q}(X^q+X)): OK
Part 2 (Lemma 2.2 V_k=im(S_k), exhaustive g_{n,q} & Phi checks N<=16, Case 1, triple (307,4;4)): OK
Part 3 (Case 2 q=4, k in {2,4,6} Steps 2.1-2.3 & P(A), Q(A) identities): OK
Part 4 (Case 3 (q=8,e=8) & (q=16,e=8) Weil bound, odd deg q-3, explicit s(u+alpha)=0): OK
Part 5 (Case 4 e=4, m=2..6 full & m=7..8 sampled up to GF(2^32): Phi^{q^2}=x^{q+2}Phi, Psi conj & gcd split): OK
PASS
FLOAT_COUNT: 0 FLOAT_CALLS: 0
```

Verdict: **PASS**.
