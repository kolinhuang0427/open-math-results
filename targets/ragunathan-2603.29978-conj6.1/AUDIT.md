# Adversarial Audit Report: `targets/ragunathan-2603.29978-conj6.1/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T03:09Z`
- **Target:** Naveena Ragunathan and Adam Van Tuyl, *"The van der Waerden Simplicial Complex and its Lefschetz Properties"*, `arXiv:2603.29978v2` (`2026-08-19`), Section 6, Conjecture 6.1 (`\label{conjecture}`)
- **Owner:** `attack-1`
- **Checker:** `check-3` (`notes/check-check-3.md`, `notes/check-check-3.py`)
- **Audit Helper:** `ragunathan-audit-hlp` (`notes/audit-helper-ragunathan.md`, killed)
- **Strict Isolation Observed:** Read ONLY the primary source (`tools/.arxiv_cache/eprint/2603.29978/van_der_Waerden_complex_and_the_Lefschetz_Properties_final.tex` via `notes/audit-helper-ragunathan.md`), `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, `notes/novelty-gate2-watch-{2,5}.md`, and `notes/audit-helper-ragunathan.md`. Did NOT read author `verify.py` or any author scratch notes (`notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, etc.). Did NOT edit `TARGET.md` or `PROOF.md`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against `arXiv:2603.29978v2` (`van_der_Waerden_complex_and_the_Lefschetz_Properties_final.tex`, `notes/audit-helper-ragunathan.md` §1):
- **Latest arXiv version:** `2603.29978v2` (submitted `2026-03-31`, revised `2026-08-19`, `math.AC`, no journal-ref or DOI).
- **Definitions (lines 192–195, 261–296, 351–370, 511–529):**
  - ${\tt vdw}(n, k)$ ($n > k \ge 1$) is the pure $k$-dimensional simplicial complex on $[n]$ whose facets are the $(k+1)$-element arithmetic progressions $\{i, i+d, \dots, i+kd\} \subseteq [n]$ with jump factor $d \ge 1$.
  - $A({\tt vdw}(n, k)) = K[x_1, \dots, x_n]/(I_{{\tt vdw}(n, k)} + \langle x_1^2, \dots, x_n^2 \rangle)$, with the Weak Lefschetz Property (WLP) defined by maximal rank of $\times \ell : A_i \to A_{i+1}$ for a general linear form $\ell$ and all $i \ge 0$.
- **Theorem 4.2 (`\label{thm.casek=3}`, lines 916–920):** Over $\mathrm{char}(K) = 0$, $A({\tt vdw}(n, 3))$ has the WLP iff $n \in \{4, 5, 6\}$ (so fails for all $n \ge 7$).
- **Verbatim Conjecture 6.1 (`\label{conjecture}`, lines 1384–1393):**
  > Suppose $\mathrm{char}(K) = 0$. Fix an integer $k \ge 3$.
  > 1. If $k$ is odd, then there exists an $m$ such that $A({\tt vdw}(n, k))$ fails to have the WLP for $n \ge m$.
  > 2. If $k$ is even, then $A({\tt vdw}(n, k))$ has the WLP for all $n > k$.
- No `CONTESTED.md` exists in `targets/ragunathan-2603.29978-conj6.1/`.
- `TARGET.md` and `PROOF.md` match the primary source verbatim with zero quantifier, characteristic, or convention drift.

---

## 2. Adversarial Line-by-Line Mathematical Audit

Every lemma, proposition, edge case, and inequality in `PROOF.md` was checked independently from scratch:

1. **Section 1 — Preliminaries (Lemmas 1–2, lines 25–53):**
   - **Lemma 1:** Since $\mathrm{char}(K) = 0$, $K$ is infinite, $U = \{c \in K^n : c_1 \cdots c_n \neq 0\}$ is nonempty Zariski-open in irreducible $K^n$, and diagonal rescaling $\phi_c(x_j) = c_j^{-1} x_j$ preserves the monomial ideal $I_\Delta + \langle x_1^2, \dots, x_n^2 \rangle$ and maps $\ell_c \mapsto \ell_1 = \sum x_j$. Since maximal rank is a Zariski-open condition, WLP holds iff $\times \ell_1$ has maximal rank in every degree $0 \le r \le \dim \Delta$, i.e., iff each $\{0, 1\}$-incidence matrix $M_r$ has maximal rank over $\mathbb{R}$ (rank of an integer matrix is invariant across fields of characteristic $0$). Airtight.
   - **Lemma 2:** Verified $D_{s+1} = U_s^T$ ($0 \le s \le N-1$) and $D_{s+1} U_s - U_{s-1} D_s = (N - 2s) I_{V_s}$ for all $0 \le s \le N$, including boundary cases $s = 0$ ($D_1 U_0 = N I$, $D_0 = 0$) and $s = N$ ($U_{N-1} D_N = N I$, $U_N = 0$). Inner product identity $\|U_s v\|_2^2 - \|D_s v\|_2^2 = (N - 2s)\|v\|_2^2$ immediately gives injectivity of $U_s$ when $2s < N$ and of $D_s$ when $2s > N$. Airtight.

2. **Section 2 — Part (2), Even $k = 2m \ge 2$ (Propositions 3 & 5, Lemma 4, lines 57–106):**
   - **Proposition 3 ($0 \le r \le m$):** For $z \in \ker(M_r)$ and any facet $F$ ($|F| = 2m + 1$), all subsets of $F$ are faces, so restricting $z$ to $\binom{F}{r}$ satisfies $U_r(z|_F) = 0$. Since $2r \le 2m < 2m + 1$, Lemma 2(1) gives $z|_F = 0$. Purity of ${\tt vdw}(n, 2m)$ ensures every $r$-face lies in some facet $F$, so $z = 0$. Airtight (valid even at $r = 0$, $m = 1$).
   - **Lemma 4 ($m + 1 \le r \le 2m$):** For $T \in F_{r+1}$ contained in a jump-$d$ facet, $d \mid g(T)$, writing $g(T) = q d$ gives $(m+1)qd \le r q d \le \max T - \min T \le 2md < 2(m+1)d$, forcing $q = 1$ and $d = g(T)$ uniquely. Airtight.
   - **Proposition 5 ($m + 1 \le r \le 2m$):** For a nonzero $v \in \ker(M_r^T)$, maximizes $d_{\max} = \max\{g(T) : v(T) \neq 0\}$ and then $L_{\max} = \max\{(\max T - \min T)/d_{\max} : g(T) = d_{\max}, v(T) \neq 0\} \in \{r, \dots, 2m\}$. Picks witness $T_0$, sets $a = \min T_0$, $b = \max T_0$, $I = (a + d_{\max}\mathbb{Z}) \cap [a, b] \subseteq F$ (every subset of $I$ is a face of $\Delta$), $I^\circ = I \setminus \{a, b\}$ ($|I^\circ| = L_{\max} - 1 \ge r - 1 \ge m \ge 1$). For any $S^\circ \in \binom{I^\circ}{r-2}$ ($0 \le r-2 < |I^\circ|$) and $S = \{a, b\} \cup S^\circ \in F_r(\Delta)$, let $T \supset S$ with $v(T) \neq 0$ and $d' = g(T) \le d_{\max}$:
     - **Case 1 ($L_{\max} = 2m$):** $2m d_{\max} = b - a \le \max T - \min T \le 2m d' \implies d' = d_{\max}$. (Covers the $m = 1, r = 2$ boundary case with $S^\circ = \emptyset$ cleanly.)
     - **Case 2 ($r \le L_{\max} \le 2m - 1$, hence $m \ge 2$ and $|S| = r \ge m+1 \ge 3$):** $S \subseteq I$ has $\min S = a, \max S = b$, so $g(S) = q d_{\max}$ satisfies $mq d_{\max} \le (r-1) q d_{\max} \le L_{\max} d_{\max} \le (2m-1)d_{\max} \implies q = 1 \implies g(S) = d_{\max}$. By Lemma 4, $S \subset T$ lies in a jump-$d'$ facet so $d' \mid g(S) = d_{\max}$; if $d' < d_{\max}$ then $d' \le d_{\max}/2$ gives $(m+1)d_{\max} \le b - a \le 2m d' \le m d_{\max}$, contradiction. Thus $d' = d_{\max}$.
     - Maximality of $L_{\max}$ forces $\min T = a, \max T = b$, hence $T \subseteq I$. Equation $(\star)$ over all $S^\circ \in \binom{I^\circ}{r-2}$ reduces exactly to $D_{r-1} w = 0$ on $I^\circ$ with $N' = L_{\max} - 1 \ge 1$, $1 \le s = r - 1 \le N'$, and $2s - N' = 2r - L_{\max} - 1 \ge 2(m+1) - 2m - 1 = 1 > 0$. By Lemma 2(2), $w = 0$, contradicting $w(T_0 \setminus \{a,b\}) = v(T_0) \neq 0$. Completely airtight!

3. **Section 3 — Part (1), Odd $k \ge 3$ (Lemma 6, §3.1, Propositions 7 & 8, lines 110–234):**
   - **Lemma 6:** Checked $g_1 = \lfloor n/(k+1) \rfloor \le g_2 = \lfloor (n-1)/k \rfloor$ (valid since $n \ge k+1$), $I_t = [1 + tg, n - (k-t)g]$ ($0 \le t \le k-L$), overlap/abutment for $1 \le g \le g_1$ (giving $|[1, n-Lg]| = n - Lg$), strict disjointness for $g_1 < g \le g_2$ (giving $(k-L+1)(n-kg)$), empty for $g > g_2$, and boundary $L = k$ (single interval $I_0$). Airtight.
   - **Section 3.1 ($k = 3$):** Both Theorem 4.2 of `2603.29978v2` ($n \ge 7$) and the self-contained $n \ge 40$ argument are verified exact: unique jump $d = g(T)$ for $T \in F_3$, exact 3 primitive shapes $(0,1,2), (0,1,3), (0,2,3)$, closed form $|F_3| = (4ng_2 - 6g_2^2 - 6g_2) + (2g_1^2 - ng_1 + 2g_1)$, exact algebraic lower bound $|F_3| - |F_2| \ge |F_3| - \binom{n}{2} \ge (n^2 - 36n - 144)/24 > 0$ for $n \ge 40$, and nonzero kernel vector $z(\{a,b\}) = (-1)^{v_2(b-a)} 2^{v_2(b-a)} \in \ker(M_2)$ (since pairwise differences $\{d, d, 2d\}$ and $\{d, 2d, 3d\}$ have $2$-adic valuation multiset $\{v, v, v+1\}$). Airtight.
   - **Proposition 7 (Odd $k = 2m - 1 \ge 5$, $n \ge 4m = 2k + 2$):** Verified all four sets $A, B, C, D$ (size $m$, pairwise disjoint in $[4m] \subseteq [n]$), all four facets $F_1, F_2, F_{\mathrm{odd}}, F_{\mathrm{even}}$ (jumps $1, 1, 2, 2$), pairwise intersections of size $0$ or $m < m+1$ (so the four $\binom{F_*}{m+1}$ families are pairwise disjoint), well-definedness and nonvanishing of $v$ ($v(A \cup \{2\}) = (-1)^m \neq 0$), binomial weight identity $(m-j)w(j+1) + j w(j) = 0$ ($1 \le j \le m-1$), unique facet containment for $S \notin \{A, B, C, D\}$ (Case 1), and exact two-facet cancellation for each $S \in \{A, B, C, D\}$ (Case 2). Completely airtight!
   - **Proposition 8 ($m \ge 3$, $k = 2m - 1$, $n > k$):**
     - Verified unique $(a_1, g, P)$ encoding, $q = 1$ forced for $r = m+1$ (and all tuples primitive), $q \in \{1, 2\}$ for $r = m \ge 3$ (using $2m - 1 < 3(m-1)$), $q = 2 \iff P = P_0 = (0, 1, \dots, m-1)$, and $(0, 2, \dots, 2m-2)$ is the unique non-primitive tuple of size $m$ with span $\le 2m - 1$.
     - Verified jump-$2d$ facet containment implies $n \ge 1 + (4m-2)d > 2md = (k+1)d \implies d \le g_1$, so every $a_1 \in [1, n - (2m-2)d]$ lies in a jump-$d$ facet; cancellation of $\pm N_1(2m-2; n, k)$ leaves $|F_m| = \sum_{L=m-1}^{2m-1} \binom{L-1}{m-2} N_1(L; n, k) - N_{1,\mathrm{even}}(m-1; n, k)$.
     - Verified exact hockey-stick cancellation, Catalan number coefficient $C_m = \frac{1}{m+1}\binom{2m}{m}$ with exact positive sign, $k - (m-1) + 1 = m + 1$, induction $C_m \ge m + 2 > m + 1$ and $2C_m \ge 3m + 1$ for $m \ge 3$, $(g_1, g_2]$ nonnegativity, and both parity subcases $g_1 = 2h$ ($h \ge 1$) and $g_1 = 2h+1$ ($h \ge 0$) of the $[1, g_1]$ lower bound (including exact $-h + h = 0$ cancellation and $g_1 = 1 \implies h = 0$ boundary).
     - Combined with Proposition 7 and Lemma 1, yields WLP failure in degree $m = (k+1)/2$ for all odd $k \ge 5$ and all $n \ge 2k + 2$.

**Minor non-blocking technical nit:** Lemma 6 (line 115) states $\gcd(p_2, \dots, p_r) = 1$ as a hypothesis, whereas Proposition 8 (line 205) invokes Lemma 6 on the non-primitive tuple $P' = (0, 2, 4, \dots, 2m - 2)$ (which has $\gcd = 2$, span $2m - 2$). However, the proof of Lemma 6 (lines 124–128) never uses $\gcd(p_2, \dots, p_r) = 1$ — containment of $a_1 + d \cdot P'$ in a jump-$d$ facet depends solely on the endpoints $a_1$ and $a_1 + (2m-2)d$, and is literally identical to containment of the primitive tuple $(0, 1, 2m-2)$ of span $2m-2$. Thus the deduction in Proposition 8 is completely valid.

---

## 3. Independent Mechanical Verification

Reran `check-3`'s independent exact-arithmetic verifier (`targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py`):
```sh
/usr/bin/time -p .venv/bin/python -u targets/ragunathan-2603.29978-conj6.1/notes/check-check-3.py
```
Raw output (`notes/audit-helper-ragunathan.md` §3.1):
```text
Lemma 2 PASS: DU - UD == (N - 2s)I verified exactly for 1 <= N <= 8, 0 <= s <= N.
Even Part PASS: exact rational WLP (k=2,4,6; n<=9) and Lemma 4 / Prop 5 isolation verified.
Odd k=3 PASS: exact WLP iff n in {4,5,6} (n<=10), M_2 z == 0 (n=7..25), and n>=40 bound verified.
Odd k>=5 PASS: Prop 7 (M_m^T v == 0) and Prop 8 (|F_m| > |F_{m+1}| & Catalan diff) verified.
PASS
```
Exit code `0`, `0.49s` real. In addition, `ragunathan-audit-hlp` independently verified the Section 3.1 ($k=3, n=4..100$) and Proposition 8 ($m=3, n=6..25$; $m=4, n=8..16$, including boundary cases $n = k + 1 = 2m$) exact formulas against brute-force face enumeration (`notes/audit-helper-ragunathan.md` §3.2): all `PASS`.

---

## 4. Deep Novelty Check

Verified independently in `notes/audit-helper-ragunathan.md` §2 (through `2026-11-27T03:02Z`), plus Gate 2 receipts `notes/novelty-gate2-watch-{2,5}.md`:
- **OpenAlex / arXiv / Zenodo / Crossref / web:** `arXiv:2603.29978v2` (`W7147123883`) has `cited_by_count: 0`; Ragunathan's Dec 2025 McMaster M.Sc. thesis (`W7214395421`) is cited solely by `2603.29978`; zero follow-up preprints, papers, or MO/MSE solutions.
- **`413` local watch snapshots + all inspected competing GitHub repos** (`the-omega-institute/trureturing*`, `mathesis-papers/*`, `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `openai/math`, `google-deepmind/formal-conjectures`): `0` competing proofs or claims. Confirmed `chy4pro/automath` line 61 is solely a raw triage-pool listing with no solution.

### What Is Not Established / Caveats
- Proves Part (2) for all even $k \ge 2$ and $n > k$, and Part (1) with explicit threshold $m = 2k + 2$ for odd $k \ge 5$ (and $n \ge 40$ self-contained / $n \ge 7$ via Theorem 4.2 of `2603.29978v2` for $k = 3$); does **not** establish the exact minimal failing $n$ conjectured in the paper's Remark (lines 1406–1409) for $k \equiv 3 \pmod 4$ (where the remark suggests $2k + 1$, e.g. $n = 15$ for $k = 7$ and $n = 23$ for $k = 11$, nor WLP for $k < n < 2k+1$ when $k \ge 5$ is odd).
- Does not address positive characteristic ($\mathrm{char}(K) > 0$) or the Strong Lefschetz Property (SLP).
- Semantic Scholar and repeated Crossref calls were rate-limited (`HTTP 429`), and private repositories / unindexed off-arXiv works were not covered.
- Internal audit and finite exact checks are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`.

- **Gate 3 Novelty Clearance (`2026-11-27T03:34Z`–`04:10Z`):** **PASS** across `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-3.md`, and `notes/novelty-gate3-watch-5.md` (`watch-3` co-covering `watch-6`), covering live arXiv `2603.29978v2`, OpenAlex citing cache (`citing_count: 0`), Zenodo, `470` snapshots, and all 15+ competing GitHub repos. Cleared for coordinator verification.
