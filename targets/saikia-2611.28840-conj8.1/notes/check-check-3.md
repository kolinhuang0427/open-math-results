# Independent Check Report: `targets/saikia-2611.28840-conj8.1/`

- **Checker:** `@check-3`
- **Target:** `targets/saikia-2611.28840-conj8.1/TARGET.md` (`arXiv:2611.28840v1`, Section 8, Conjecture 8.1 `\label{conj:sharp}`)
- **Proof checked:** `targets/saikia-2611.28840-conj8.1/PROOF.md` (answer: **YES**, plus exact best-possible sharpness for all $k \ge 3$)
- **Gate 2 Watch:** **PASS** (`watch-5` `#1651`, `watch-6` `#1652`, `watch-1` `#1654`; `#1655` `@watch-6` cross-check of two newly spotted repos in progress)

## 1. Primary Source Verification

- **arXiv version check:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2611.28840` confirms `2611.28840v1` is the sole arXiv version (`published: 2026-11-21T14:45:07Z`).
- **Cached TeX:** `tools/.arxiv_cache/eprint/2611.28840v1/final.tex` (1,077 lines).
- **Statement match (`final.tex` L931–941):**
  > *"For any $k\geq3$, there exists an odd integer $\lambda_k$ such that \eqref{eq:sharp} holds for any $n\geq0$."*
  where `\eqref{eq:sharp}` is $\mathrm{PDO}_{\mathrm{t}}(3\times 2^{k+2}n) \equiv 8\lambda_k\,\mathrm{PDO}_{\mathrm{t}}(3\times 2^k n) \pmod{2^{\lfloor 7(k+1)/2 \rfloor}}$ (`\PDO` = $\mathrm{PDO}_{\mathrm{t}}$ at L39). Matches `TARGET.md` verbatim.
- **Auxiliary references verified:** `eq:gf` (L79), `eq:aux` (L240–246), `(P1)`–`(P2)` / `eq:A1`–`eq:A3` (L441–450), `Theorem 4.1` / `thm:gf` / `eq:gfm` (L490–503), `Lemma 5.1` / `lem:valPhi` (L558–580), and `Lemma 5.2` / `lem:refined` (L590–641).

## 2. Proof Audit Summary

- **Step 1 (Lemma 1):** Support $\lfloor (i+3)/4 \rfloor \le j \le 4i+3$, valuation $\nu_2(B_{i,j}) \ge 2j - \lfloor i/2 \rfloor$, and explicit low entries/valuations of $B = A^2$ verified.
- **Step 2 (Lemma 2 & Theorem 3):** Banach algebra bounds on $\mathcal{B}_2(K)$, $\mathcal{E}_2(K)$, $\mathcal{R}_2(K)$ hold; exact conjugation identity `(7)` and Atkin–Lehner lift identities `(12)`–`(17)` yield $W^2 = I$ and $W A = -A W$ on $\mathcal{E}_2(K)$.
- **Step 3 (Lemmas 4–6 & Theorem 7):** Strict $2^2$-contraction $\Phi$ on $S(K)$ yields unique $\mathbf{u}_2 \in S(\mathbb{Q}_2)$ with $\Lambda \in 8\mathbb{Z}_2^\times$; $\|B_{YY}\| \le 2^{-5}$ and Schur complement $M(t)$ give Weierstrass root $z_0$ ($|z_0|_2 = 2^{-3}$); anti-commutation $W A = -A W$ forces even nullity $\dim_K \ker(B - z_0 I) = 2$, hence $S(z_0) = 0$, $z_0 = \Lambda$, and $(\mathbf{u}_2 B)_1 = 0$.
- **Steps 4–5 (Lemma 8 & Propositions 9–10):** Projection modulo $\mathrm{span}(\mathbf{u}_1, \mathbf{u}_2)$ gives contraction $\nu_2(M(e_k)_j) \ge 7 + 2j - 2k$ ($k,j \ge 3$), and odd/even inductions establish both `\eqref{eq:sharp}` modulo $2^{\lfloor 7(k+1)/2 \rfloor}$ and exact sharpness ($\nu_2(\text{defect}_3) = \lfloor 7(k+1)/2 \rfloor$) for every $k \ge 3$.

## 3. Exact Mechanical Verification (`check-check-3.py`)

Command:
```sh
.venv/bin/python -u targets/saikia-2611.28840-conj8.1/notes/check-check-3.py && .venv/bin/python -c "import ast; tree = ast.parse(open('targets/saikia-2611.28840-conj8.1/notes/check-check-3.py').read()); floats = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]; calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'float']; print('FLOAT_COUNT:', len(floats), 'FLOAT_CALLS:', len(calls))"
```

Exact output:
```text
Part 1 (Lemma 5.1 & Lemma 1 support, bounds, low entries of B): OK
Part 2 (direct q-series PDO_t(n) up to q^4650, Thm 4.1 m=1..5, eq:sharp & sharpness k=3..7): OK
Part 3 (Lemma 2, Theorem 3 algebraic identities (8),(12)-(17) & 2-adic W A = -A W): OK
Part 4 (Lemma 5(3) exact Schur complement M(t) & det g(t) up to t^5): OK
Part 5 (Phi^28 contraction, Thm 7 (u_2 B)_1==0 mod 2^56, Lemma 8, Props 9-10, k=3..25 congruence & sharpness): OK
PASS
FLOAT_COUNT: 0 FLOAT_CALLS: 0
```

Verdict: **PASS**.
