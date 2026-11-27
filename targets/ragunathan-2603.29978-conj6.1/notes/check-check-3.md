# Independent Check Report: targets/ragunathan-2603.29978-conj6.1/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2603.29978v2` (`2026-08-19T19:41:32Z`, latest version of 2), *"The van der Waerden Simplicial Complex and its Lefschetz Properties"* by Naveena Ragunathan and Adam Van Tuyl, cached TeX source `tools/.arxiv_cache/eprint/2603.29978/van_der_Waerden_complex_and_the_Lefschetz_Properties_final.tex`.
- **Exact definitions & conjecture match:**
  - Section 1 (lines 192–195): $A({\tt vdw}(n,k)) := K[x_1,\dots,x_n]/(I_{{\tt vdw}(n,k)} + \langle x_1^2,\dots,x_n^2 \rangle)$.
  - Section 2 (lines 511–529): `${\tt vdw}(n,k)` ($n > k \ge 1$) on $X = \{x_1,\dots,x_n\}$ has facets $\{x_i, x_{i+d}, \dots, x_{i+kd}\}$ ($k$ jumps, $k+1$ elements per facet, pure $k$-dimensional, jump factor $d \ge 1$).
  - Section 4 (lines 916–920): `Theorem \ref{thm.casek=3}` (Theorem 4.2) proves $A({\tt vdw}(n,3))$ has WLP iff $n \in \{4,5,6\}$ over $\mathrm{char}(K)=0$.
  - Section 6 (lines 1384–1393), Conjecture 6.1 (`\label{conjecture}`):
    > Suppose ${\rm char}(K) = 0$. Fix an integer $k \geq 3$.
    > 1. If $k$ is odd, then there exists an $m$ such that $A({\tt vdw}(n,k))$ fails to have the WLP for $n \geq m$.
    > 2. If $k$ is even, then $A({\tt vdw}(n,k))$ has the WLP for all $n > k$.
- **Fidelity:** `TARGET.md` and `PROOF.md` match `arXiv:2603.29978v2` verbatim with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical & Mathematical Check

- Independently wrote `targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py` (strictly without reading `verify.py` or `notes/*`), verifying using exact `int` and `fractions.Fraction` arithmetic:
  1. **Lemma 2 (Boolean lattice commutator):** Exact integer matrix verification of $D_{s+1} U_s - U_{s-1} D_s = (N - 2s) I$ for all $1 \le N \le 8$ and $0 \le s \le N$.
  2. **Part (2) (Even $k = 2m \ge 2$):** Exact rational matrix ranks confirm WLP for $(k=2, 3\le n\le 9)$, $(k=4, 5\le n\le 9)$, and $(k=6, 7\le n\le 9)$; exhaustive check of Lemma 4 (unique jump factor $d = g(T)$) and Proposition 5 isolation ($T \subseteq I$ for every $T \supset S$ with $g(T) \le d_{\max}$ and $L(T) \le L_{\max}$ when $g(T) = d_{\max}$) on $(k=4, n=15)$ and $(k=6, n=14)$.
  3. **Part (1), $k = 3$:** Exact rational rank confirms WLP holds iff $n \in \{4,5,6\}$ for $4 \le n \le 10$; direct enumeration confirms $|F_3|$ formula for $7 \le n \le 25$, $|F_2| = |F_3| = 24$ at $n=8$, $|F_3| > |F_2|$ for $n \ge 9$, explicit $z \in \ker(M_2) \setminus \{0\}$ ($z(\{a,b\}) = (-1)^{v_2(b-a)} 2^{v_2(b-a)}$) satisfies $M_2 z = 0$ identically for $7 \le n \le 25$, and the $n \ge 40$ quadratic bound holds for $40 \le n \le 119$.
  4. **Part (1), odd $k = 2m - 1 \ge 5$:**
     - **Proposition 7:** Exact rational verification of $v \in \ker(M_m^T) \setminus \{0\}$ for $(k, n) \in \{(3,8), (5,12), (5,16), (7,16), (9,20)\}$.
     - **Proposition 8:** Exact formulas for $|F_m|$ and $|F_{m+1}|$ match direct face enumeration for $(m=3, n\le 14)$, $(m=4, n\le 13)$, $(m=5, n\le 13)$; exact Catalan difference identity $|F_m| - |F_{m+1}| > 0$ verified for all $3 \le m \le 20$ and $2m \le n \le 80$ (covering threshold $n \ge 4m = 2k+2$).

- **Command run:**
```bash
.venv/bin/python -u targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py
```

- **Raw output:**
```text
Lemma 2 PASS: DU - UD == (N - 2s)I verified exactly for 1 <= N <= 8, 0 <= s <= N.
Even Part PASS: exact rational WLP (k=2,4,6; n<=9) and Lemma 4 / Prop 5 isolation verified.
Odd k=3 PASS: exact WLP iff n in {4,5,6} (n<=10), M_2 z == 0 (n=7..25), and n>=40 bound verified.
Odd k>=5 PASS: Prop 7 (M_m^T v == 0) and Prop 8 (|F_m| > |F_{m+1}| & Catalan diff) verified.
PASS
```
