# Blind Audit Report: `targets/minac-2411.01768-rem5.14/` (`@audit-2`)

**Verdict: PASS**

---

## 1. Primary Source & Statement Fidelity

- **Live arXiv query:** `arXiv:2411.01768v2` (`2026-08-03`, Ján Mináč, Tung T. Nguyen, and Nguyễn Duy Tân, *"Isomorphic gcd-graphs over polynomial rings"*, to appear in *The Journal of the Australian Mathematical Society*) is the latest version on arXiv.
- **Verbatim TeX verification (`tools/.arxiv_cache/eprint/2411.01768v2_dir/JAust_isomorphic_gcd_revised.tex`):**
  - Preamble (L48–64): `\newtheorem{thm}{Theorem}[section]` shared by `prop`, `lem`, `cor`, `definition`, `expl`, `conj`, `rem`, etc.
  - Sequential environment count in Section 5 (`\section{Isomorphic gcd-graphs}`, L838; Subsection 5.2, L931) confirms 14 environments (`5.1`–`5.14`), so `\label{rem:same_degree}` (L1095–1099) is **exact Remark 5.14** in Section 5.2.
  - Definition 1.1 (`L269–278`), Definition 2.2 (`L316–323`), and Remark 5.14 (`L1095–1099`) in `TARGET.md` match `JAust_isomorphic_gcd_revised.tex` verbatim.
  - Remark 5.14 asks whether So's conjecture holds for $G_f(D)$ over $\mathbb{F}_q[x]$ under the sole additional assumption that the irreducible factors of $f$ have pairwise different degrees (no squarefree or connectivity restriction is assumed; `COUNTEREXAMPLE.md` nevertheless refutes Remark 5.14 even for squarefree $f$ and connected gcd-graphs).

---

## 2. Line-by-Line Audit of `COUNTEREXAMPLE.md`

- **§1 Minimal Counterexample ($16$ vertices over $\mathbb{F}_2[x]$, L7–24):**
  - $f(x) = x^2(x^2+x+1)$ has monic irreducible factors $x$ (deg $1$) and $x^2+x+1$ (deg $2$, no roots in $\mathbb{F}_2$), of distinct degrees $1 \neq 2$.
  - $\mathrm{Div}(f) \setminus \{f\} = \{1, x, x^2, x^2+x+1, x(x^2+x+1)\}$ is complete ($3 \cdot 2 - 1 = 5$ proper monic divisors).
  - $D_1 = \{x^2\}$ gives $S_{D_1} = (x^2)/(f) \setminus \{0\}$ (nonzero elements of an order-$4$ ideal), so $G_f(D_1) \cong 4 K_4$.
  - $D_2 = \{x^2+x+1, x(x^2+x+1)\}$ gives $S_{D_2} = (x^2+x+1)/(f) \setminus \{0\}$ (nonzero elements of an order-$4$ ideal), so $G_f(D_2) \cong 4 K_4 \cong G_f(D_1)$ with $D_1 \neq D_2$.
  - Complements $\widetilde{D}_1 \neq \widetilde{D}_2$ in $\mathrm{Div}(f) \setminus \{f\}$ yield connected 12-regular isomorphic graphs $G_f(\widetilde{D}_1) \cong K_{4,4,4,4} \cong G_f(\widetilde{D}_2)$. **PASS.**
- **§2 Minimal Squarefree Counterexample ($64$ vertices over $\mathbb{F}_2[x]$, L28–36):**
  - $f(x) = x(x^2+x+1)(x^3+x+1)$ is squarefree with monic irreducibles of pairwise distinct degrees $1, 2, 3$ ($x^3+x+1$ has no roots in $\mathbb{F}_2$).
  - $D_1 = \{P_1 P_2\}$ and $D_2 = \{P_3, P_1 P_3, P_2 P_3\}$ yield ideals $(P_1 P_2)/(f)$ and $(P_3)/(f)$ of equal order $2^3 = 8$, giving $G_f(D_1) \cong 8 K_8 \cong G_f(D_2)$ and connected complements $K_{8,8,8,8,8,8,8,8}$. **PASS.**
- **§3 General Proposition Over Every $\mathbb{F}_q$ (L40–58):**
  - For $f = gh$ with $\gcd(g, h) = 1$ and $\deg g = \deg h = d \ge 1$: $D_1 = \{g u : u \in \mathrm{Div}(h) \setminus \{h\}\}$ and $D_2 = \{h v : v \in \mathrm{Div}(g) \setminus \{g\}\}$ are proper subsets of $\mathrm{Div}(f) \setminus \{f\}$, disjoint (any $z \in D_1 \cap D_2$ is divisible by both $g$ and $h$, hence by $gh = f$ since $\gcd(g,h)=1$, impossible in $\mathrm{Div}(f)\setminus\{f\}$) and distinct ($g \in D_1 \setminus D_2$).
  - Under the CRT ring isomorphism $\theta : \mathbb{F}_q[x]/f \xrightarrow{\sim} \mathbb{F}_q[x]/(g) \times \mathbb{F}_q[x]/(h)$, $\gcd(a-b, f) \in D_1 \iff x_1 = x_2 \land y_1 \neq y_2$ and $\gcd(a-b, f) \in D_2 \iff y_1 = y_2 \land x_1 \neq x_2$. Picking any bijection $\psi : \mathbb{F}_q[x]/(g) \xrightarrow{\sim} \mathbb{F}_q[x]/(h)$ (both of size $q^d$), the map $\Phi$ sending $(x, y) \mapsto (\psi^{-1}(y), \psi(x))$ in CRT coordinates is an explicit graph isomorphism $G_f(D_1) \xrightarrow{\sim} G_f(D_2) \cong q^d K_{q^d}$ and $G_f(\widetilde{D}_1) \xrightarrow{\sim} G_f(\widetilde{D}_2) \cong K_{q^d,\dots,q^d}$. *(Minor non-blocking notation remark on L56: writing $\Phi = \theta^{-1} \circ (\psi^{-1} \times \psi) \circ \theta$ omits the coordinate swap $\tau(x,y)=(y,x)$ before $\psi^{-1}\times\psi$, though the immediately following explicit formula $(x, y) \mapsto (\psi^{-1}(y), \psi(x))$ makes the bijection unambiguous.)*
  - Existence of monic irreducibles of every degree $m \ge 1$ over every $\mathbb{F}_q$: $S(m, q) = \frac{1}{m}\sum_{k \mid m}\mu(m/k)q^k \ge \frac{1}{m}(q^m - \sum_{1 \le k \le m/2} q^k) > 0$ holds for all $m \ge 1$ and all $q \ge 2$, yielding both $f = P_1^a P_2$ ($\deg P_2 = a \deg P_1$, $a \ge 2$) and squarefree $f = P_1 P_2 P_3$ (degrees $1, 2, 3$) over every finite field $\mathbb{F}_q$. **PASS.**

---

## 3. Independent Checker & Gate 2 Verification

- Re-ran `.venv/bin/python -u targets/minac-2411.01768-rem5.14/notes/check-check-2.py`: `exit 0`, AST `FLOAT_CONSTANTS: 0`, raw output `PASS` (verified exact finite-field Cayley gcd-graphs, clique/multipartite structure, and full vertex-pair CRT isomorphism $\Phi$ on $\mathbb{F}_2[x]$ §1 (16v) and §2 (64v), plus $\mathbb{F}_3[x]$ (81v), $\mathbb{F}_4[x]$ (256v), $\mathbb{F}_5[x]$ (625v), and exact Möbius bound $S(m,q)>0$ for $2 \le q \le 50, 1 \le m \le 20$).
- Gate 2 novelty receipts verified (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`): all 3 PASS.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

---

## 4. Independent Lean 4 Statement-Fidelity Audit (`2026-11-27T13:43Z`) — **PASS**

- **Auditor:** `audit-3` (`auto`)
- **Lean Module:** `lean/OpenMath/Minac241101768Rem514.lean` (imported on L27 of `lean/OpenMath.lean`)
- **Charter Label:** `machine-checked counterexample in Lean 4`
- **Primary-Source Fidelity (`arXiv:2411.01768v2`, `JAust_isomorphic_gcd_revised.tex` L269–278, L316–323, L1095–1099):**
  - `PolyQuot f`, `monicDivisors f`, `properMonicDivisors f`, `monicGCD a f` (`normalize (EuclideanDomain.gcd a f)`), `gcdGraph hf D hD` (proved representative-independent via `monicGCD_eq_of_sub_dvd` / `gcdGraph_adj_mk`, symmetric via `monicGCD_neg`, loopless via `f ∉ D` & `monicGCD_zero`), and `IrredFactorsDistinctDegrees f` (monic irreducible divisors of equal degree coincide) match Definition 1.1, Definition 2.2, and Remark 5.14 (`rem:same_degree`) verbatim with zero weakening or shortcuts.
  - `gcdGraph_iso_of_coprime_same_deg` proves the general CRT + degree-$d$ remainder coordinate-swap isomorphism for arbitrary fields $F$ and coprime monic $g, h \in F[x]$ of equal degree $d \ge 1$ (both $D_1 \neq D_2$ and connected complement graphs $G_f(D_1^c) \simeq_g G_f(D_2^c)$).
  - `refutes_minac_remark_5_14_deg4` ($f = x^2(x^2+x+1)$ over $\mathbb{F}_2[x]$, degrees $1, 2$), `refutes_minac_remark_5_14_squarefree` (squarefree $f = x(x^2+x+1)(x^3+x+1)$ over $\mathbb{F}_2[x]$, degrees $1, 2, 3$, connected isomorphic gcd-graphs), and `not_minac_remark_5_14` directly refute Remark 5.14 even under the stronger squarefree restriction.
- **Type-Check & Axiom Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Minac241101768Rem514.lean`
  - Exit code: `0`, zero warnings, zero `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern`/`set_option`.
  - `#print axioms` strictly `[propext, Classical.choice, Quot.sound]` for all 4 main theorems (`gcdGraph_iso_of_coprime_same_deg`, `refutes_minac_remark_5_14_deg4`, `refutes_minac_remark_5_14_squarefree`, `not_minac_remark_5_14`).
