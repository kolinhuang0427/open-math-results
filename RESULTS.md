# Verified Results

Results listed here have cleared all gates in `CHARTER.md`:
1. Exact statement quoted from the primary source (with version/section) and confirmed by a checker.
2. Mechanical verification (`verify.py` / exact computation or lemma check) where applicable.
3. Independent Pro audit (`AUDIT.md`), without seeing the author's commentary.
4. Third novelty gate passed in the hour before reporting.
5. Coordinator verification run and inspected.

Allowed labels:
- `counterexample, verified by exact computation`
- `written proof, internally audited`
- `Lean-checked` (no `sorry`, no axioms beyond `propext`, `Classical.choice`, and `Quot.sound`)

None of these labels constitutes peer review, and each entry states what is not established.

---

### `ferrero-2511.16335-conj1.8` — Counterexample to Ferrero–Hall–Hogben–Hunnell–Small Conjecture 1.8

- **Summary**: Ferrero, Hall, Hogben, Hunnell, and Small conjectured that every connected graph whose upper standard zero forcing propagation time equals 1 must be a "standard fast join" (either a complete graph or a join of edgeless graphs and double cliques). We refuted this conjecture by exhibiting the 12-vertex, 24-edge circulant graph $C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$, which is connected and satisfies $\overline{\mathrm{PT}}(G) = 1$ yet has a connected complement and zero forcing number $8 < n - 2$, so it is not a standard fast join. We further proved that the entire infinite family of cycle blowups $C_6[r_0 K_1, \dots, r_5 K_1]$ with $r_i \ge 2$ gives counterexamples.
- **Exact statement & source**:
  - Source: Daniela Ferrero, H. Tracy Hall, Leslie Hogben, Mark Hunnell, Ben Small, *"Zero forcing propagation time intervals and graphs with fixed propagation time"*, `arXiv:2511.16335v1` (`NewFixedPropTime.tex`, Section 1, Definition 1.5 lines 275–276 and Conjecture 1.8 `\label{c:std}` lines 293–296; verified verbatim in *Australasian Journal of Combinatorics*, Vol. 96(2), 2026, pp. 374–394, revised 2 June 2026).
  - Definition 1.5: *"A graph $G$ of order $n\geq 2$ is a standard fast join if $G\cong K_n$ or $G=\bigvee_{i=1}^t G_i$ where $t\geq 2$ and each graph $G_i$ satisfies $G_i\cong n_iK_1$ or $G_i\cong K_{n_i}\dot{\cup} K_{m_i}$ with $n_i,m_i\geq 2$."*
  - Conjecture 1.8: *"Let $G$ be a connected graph. If $\overline{\mathrm{PT}}(G)=1$, then $G$ is a standard fast join."*
- **Label**: `Lean-checked` (no `sorry`, and no axioms beyond `propext`, `Classical.choice`, and `Quot.sound`; formalizes both the explicit 12-vertex witness $C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$ in `refutes_conjecture_1_8_circ12` / `not_ferrero_conjecture_1_8` and the infinite family $C_6[r_0 K_1, \dots, r_5 K_1]$, $r_i \ge 2$, in `refutes_conjecture_1_8_infinite_family`; file: `lean/OpenMath/Ferrero251116335Conj18.lean`, audited for statement fidelity in board `#200` and coordinator-verified). Also supported by `counterexample, verified by exact computation` (`notes/check-check-2.py`) and `written proof, internally audited` (`AUDIT.md`).
- **Verification command**: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake build OpenMath.Ferrero251116335Conj18` (and Python witness check: `.venv/bin/python targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py`)
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T20:20:58Z`–`20:21:30Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing` (issue `#8371` closed `2026-09-16` as terminal OPEN with no resolution), GitHub search, live arXiv API (`2511.16335v1` unchanged), OpenAlex `W4416550551` (`cited_by_count: 0`), AJC Vol. 96(2) revised PDF, and web search; 0 prior resolutions found.
- **What is not established**: Global minimality of $n = 12$ across all connected graphs of order $n \le 11$ is not proved (only minimality within the $C_6[r_0 K_1, \dots, r_5 K_1]$ with $r_i \ge 2$ family). Internal auditing and exact computation are not external peer review.

---

### `wei-2310.17337-conj1.5` — Counterexample to Wei–Zhang–Zhao Conjecture 1.5

- **Summary**: Wei, Zhang, and Zhao conjectured that for every connected graph $G \ncong C_k$ of size $m$, the $C_k$-isolation number satisfies $\iota(G, C_k) \le (m + 1)/(k + 2)$, having proved $k = 4$ and building on Borg–Fenech–Kaemawichanurat's $k = 3$ theorem. We refuted this conjecture at $k = 8$ using the 12-vertex, 18-edge truncated tetrahedral graph, for which deleting the closed neighborhood of any single vertex leaves an 8-cycle subgraph so $\iota(G, C_8) = 2 > 19/10 = (m+1)/(k+2)$. The generalized Petersen graphs $GP(9, 2)$ (at $k = 14$, $\iota = 2 > 7/4$) and $GP(11, 2)$ (at $k = 18$, $\iota = 2 > 17/10$) also refute the bound.
- **Exact statement & source**:
  - Source: Xiaohua Wei, Gang Zhang, Biao Zhao, *"On the $C_4$-isolation number of a graph"*, `arXiv:2310.17337v1` (`C_4-isolation.tex`, Section 1, Conjecture 1.5 `\label{conj1.5}`, lines 119–121, and Abstract line 67).
  - Statement: *"If $G \ncong C_k$ is a connected graph of size $m$, then $\iota(G, C_k) \le \frac{m+1}{k+2}$."*
- **Label**: `Lean-checked` (no `sorry`, no `native_decide`, and no axioms beyond `propext`, `Classical.choice`, and `Quot.sound`; formalizes the 12-vertex, 18-edge truncated tetrahedral graph at $k = 8$ in `refutes_wei_conjecture_1_5_witness` and `not_wei_conjecture_1_5`; file: `lean/OpenMath/Wei231017337Conj15.lean`, audited for statement fidelity in board `#227` and coordinator-verified). Also supported by `counterexample, verified by exact computation` (`notes/check-check-1.py`).
- **Verification command**: `cd lean && export PATH="$HOME/.elan/bin:$PATH" && lake build OpenMath.Wei231017337Conj15` (and Python witness check: `.venv/bin/python targets/wei-2310.17337-conj1.5/notes/check-check-1.py`)
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T20:23:09Z`–`20:24:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live `1337isnot1337/solved-conjectures`, GitHub code/repo/issue searches, live arXiv API (`2310.17337v1` unchanged), OpenAlex `W7163506673` (`cited_by_count: 3`: Borg–Scicluna `10.1016/j.dam.2026.08.006`, Liang–Wu `10.1016/j.dam.2025.06.058`, `10.12677/aam.2025.149398`), Crossref `10.1142/s1793830926500679`, and web search; no prior refutation or settlement found.
- **What is not established**:
  - **Published DMAA journal version caveat (`AUDIT.md` §4):** `arXiv:2310.17337v1` was later published in *Discrete Mathematics, Algorithms and Applications* (online `2026-07-21`, DOI `10.1142/s1793830926500679`). The published DMAA abstract replaces the closing statement of Conjecture 1.5 with *"For general $k$, it is worth noting that the problem on $C_k$-isolation remains open,"* and because the DMAA full-text PDF is paywalled, it is unverified whether Section 1 of the published journal text retained, modified, or dropped Conjecture 1.5; this refutation applies strictly to `arXiv:2310.17337v1` (Section 1, Conjecture 1.5).
  - Does not settle whether $\iota(G, C_k) \le (m+1)/(k+2)$ holds for the small individual values $k \in \{5, 6, 7\}$, and does not refute the girth-restricted bound $\iota(G, \mathcal{C}) \le (m+1)/(g+2)$ studied by Liang & Wu (2026) (the truncated tetrahedron has girth $3 < 8$ and $GP(9,2)$ has girth $5 < 14$).
  - Internal audit and exact computation are not external peer review.

---

### `oeis-A100691` — Proof of Mathar's 2022 Formula for OEIS `A100691` and Triangular-Strip SAW Discrepancy ($s(5) = 160 \ne 158$)

- **Summary**: R. J. Mathar conjectured in 2022 that OEIS `A100691(n)` (listed as counting $n$-step self-avoiding paths on the triangular lattice strip $\mathbb{Z} \times \{0,1\}$) equals `A193641(n+2) - 3` for all $n > 0$. We resolved both readings of the entry: first, we proved the empirical recurrence `A193641(n) = 2*A193641(n-1) + A193641(n-3)` ($n \ge 3$) via an exact 3-state partition and showed it implies `a_OEIS(n) = A193641(n+2) - 3` for all $n \ge 1$ for the stored OEIS `A100691` sequence. Second, under the combinatorial definition in `A100691`'s title (rooted $n$-step self-avoiding walks from $(0,0)$ on $\mathbb{Z} \times \{0,1\}$), we showed the actual count $s(n)$ satisfies $s(5) = 160 \ne 158 = \text{A100691}(5)$ and proved via an exact 3-edge-cut column transfer matrix that $F_{\mathrm{SAW}}(z) - G_{\mathrm{OEIS}}(z) = 2z^5 / ((1-z)^2 (1-2z-z^3))$, so $s(n) > \text{A193641}(n+2) - 3$ for all $n \ge 5$.
- **Exact statement & source**:
  - Source: OEIS `A100691` (revision 11, 2022-07-22, Emeric Deutsch / R. J. Mathar) and OEIS `A193641` (revision 48, 2026-09-16, R. H. Hardin / Alois P. Heinz).
  - `A100691` title & data: *"Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."* (`1,4,12,30,70,158,352,780,1724,3806,...`, G.f. $(1+z^2)(1+z+z^2)/((1-z)(1-2z-z^3))$).
  - Mathar's 2022 conjecture (`A100691`, Formula): *"Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022"*.
  - `A193641` title & empirical recurrence: *"Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."* (`1,1,3,7,15,33,73,161,355,...`; `Empirical: a(n) = 2*a(n-1) + a(n-3).`).
- **Label**: `Lean-checked` (no `sorry`, no `native_decide`, and no axioms beyond `propext`, `Classical.choice`, and `Quot.sound`; formalizes Part 1 for all $n \ge 1$ in `A193641_recurrence`, `aOEIS_gf_identity`, and `aOEIS_eq_A193641_sub_three`, plus Part 2's combinatorial SAW refutation $s(5) = 160 \ne 158$ in `sawCount_eq_length_sawPaths`, `sawCount_five`, `refutes_combinatorial_reading_at_five`, and `not_mathar_combinatorial_conjecture`; file: `lean/OpenMath/OeisA100691.lean`, coordinator-verified). Also supported by `written proof, internally audited` (`AUDIT.md`, including the all-$n \ge 5$ transfer-matrix proof) and exact symbolic/enumeration checks (`notes/check-check-3.py`).
- **Verification command**: `cd lean && export PATH="$HOME/.elan/bin:$PATH" && lake build OpenMath.OeisA100691` (and Python transfer-matrix/enumeration check: `.venv/bin/python targets/oeis-A100691/notes/check-check-3.py`)
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T21:12:06Z`–`21:14:45Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live OEIS `A100691` (rev 11) and `A193641` (rev 48), live OEIS searches for `s(n)`, live arXiv API, GitHub code/repo/issue searches (`1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing`), Zenodo API, Crossref, and web search; 0 prior proofs of `A193641`'s recurrence or reports of `s(5) = 160` found (Gate 2 OpenAlex check clear at `20:18Z`; Gate 3 OpenAlex returned HTTP 429).
- **What is not established**:
  - **Labelle (1996) print-only caveat (`AUDIT.md` §3.3):** J. Labelle, *"Paths in the Cartesian, triangular and hexagonal lattices"*, *Bull. ICA* 17 (1996), 47–61 is print-only and was not directly inspected, so we cannot attribute whether the single `-z^5` vs `+z^5` sign discrepancy originated in Labelle (1996) or in Deutsch's 2004 OEIS submission (though sibling sequences `A038577`, `A100692`, and `A100693` confirm Labelle's rooted-SAW strip definition).
  - Internal auditing and exact symbolic/finite computation are not external peer review.

---

### `dris-2202.08116-conj5.1` — Proof of Dris Conjecture 5.1 (`AsymptoticDensity2`)

- **Summary**: Jose Arnaldo Bebita Dris conjectured that the set $A$ of positive integers $m$ satisfying $\gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))$ has asymptotic density $0$, after proving an upper bound of $7/9$ and citing an unproved heuristic of Aaron Meyerowitz. We proved this conjecture completely by combining a prime-power divisibility criterion for primes $p \equiv 1 \pmod 6$ with a finite CRT truncation separating main residue exclusions from bad sets where fewer than two root-of-unity primes $q \in \mathcal{Q}_p$ exactly divide $m$. Using Dirichlet's theorem on primes in arithmetic progressions and Chebyshev's inequality on finite CRT blocks to show each bad set has density $0$, and taking $k \to \infty$ via $\sum_{p \equiv 1 \pmod 6} 1/p = \infty$, we established $\overline{d}(A) = 0$ and hence $d(A) = 0$.
- **Exact statement & source**:
  - Source: Jose Arnaldo Bebita Dris, *"A new approach to odd perfect numbers via GCDs"*, `arXiv:2202.08116v1` (`main.tex`, Section 5, Conjecture 5.1 `\label{AsymptoticDensity2}`, lines 386–391; also Abstract lines 57–59; published in *Octogon Mathematical Magazine* 30(2), Oct 2022, pp. 883–895).
  - Statement: *"The asymptotic density $\mathscr{A}$ of positive integers $m$ with $\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))$ satisfies $\mathscr{A} = 0$."*
- **Label**: `written proof, internally audited` (supported by exact integer and `Fraction` verification of primary-source counts and Lemmas 1–3 in `notes/check-check-2.py`).
- **Verification command**: `.venv/bin/python targets/dris-2202.08116-conj5.1/notes/check-check-2.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T21:27:55Z`–`21:29:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live `1337isnot1337/solved-conjectures`, GitHub code/repo/issue searches, live arXiv API (`2202.08116v1` unchanged), Zenodo API, and web search (with Gate 2 live Stack Exchange API check of MO `Q369441` / Meyerowitz heuristic Answer `369521` and OpenAlex `W4226357996` `cited_by_count: 0`; Gate 3 OpenAlex returned HTTP 429); 0 prior proofs found.
- **What is not established**:
  - Proves qualitative asymptotic density $d(A) = 0$ only, not an explicit quantitative decay rate for $|A \cap [1, X]| / X$ (which decays very slowly, $\approx 92.35\%$ at $X = 10^6$).
  - Does not settle Dris's Section 7 conjecture that $\gcd(\sigma(q^k), \sigma(n^2)) \neq \gcd(n^2, \sigma(n^2))$ for odd perfect numbers $N = q^k n^2$.
  - Internal audit and small-case exact checks are not formal peer review or a formal Lean proof.

---

### `oeis-A250917` — Proof of Mathar's 2020 D-Finite Recurrence for OEIS `A250917`

- **Summary**: R. J. Mathar conjectured in 2020 that the coefficients $a(n)$ of the exponential generating function $F(x) = \exp(x C(x)^3)$, where $C(x) = (1 - \sqrt{1-4x})/(2x)$ is the Catalan generating function, satisfy an explicit order-5 polynomial-coefficient recurrence. We proved that this recurrence holds for all $n \ge 5$ (and also at $n = 3, 4$, while failing at $n = 0, 1, 2$) by translating it into a linear differential operator $L = \sum_{r=0}^5 Q_r(\theta) (d/dx)^{5-r}$ acting on $F(x)$. Working in the differential field $\mathcal{A} = \mathbb{Q}(x)[S]/(S^2 - (1-4x))$ with $S = \sqrt{1-4x}$, we showed symbolically in exact rational arithmetic that $L[F](x)/F(x) = 0$ identically on $|x| < 1/4$, forcing every Taylor coefficient of $L[F]$ to vanish.
- **Exact statement & source**:
  - Source: OEIS `A250917` (revision 20, 2025-03-15).
  - Name: *"Expansion of e.g.f. exp( x*C(x)^3 ) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, A000108."* (offset `0,3`).
  - Conjecture (Formula section): *"Conjecture D-finite with recurrence: +2*a(n) +(-11*n+20)*a(n-1) +(n^3+9*n^2-116*n+164)*a(n-2) +(-4*n^4+35*n^3+n^2-317*n+342)*a(n-3) -6*(n-3)*(6*n^3-50*n^2+147*n-176)*a(n-4) +12*(n-5)*(2*n-9)*(n-3)*(n-4)*a(n-5)=0. - _R. J. Mathar_, Jan 25 2020"* (proved for its natural domain $n \ge 5$, as well as $n = 3, 4$; fails at $n = 0, 1, 2$).
- **Label**: `written proof, internally audited` (supported by exact SymPy rational/polynomial verification of $L[F]/F = 0$ in $\mathcal{A}$ and series check through $n = 25$ in `notes/check-check-2.py`).
- **Verification command**: `.venv/bin/python targets/oeis-A250917/notes/check-check-2.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T21:37:27Z`–`21:56:30Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live OEIS `A250917` (rev 20), live `1337isnot1337/solved-conjectures` & `trureturing`, GitHub code/repo/issue searches, live arXiv API, Zenodo API, and web search (with Gate 2 OpenAlex check confirming 0 hits; Gate 3 OpenAlex/Crossref/S2 returned HTTP 429); 0 prior proofs found.
- **What is not established**:
  - **Symbolic-computation & `joeis`/`gfis/OEIS-mat` near-miss caveats (`AUDIT.md` §4):** The algebraic cancellation $R(x, S) = (0, 0)$ in $\mathbb{Q}(x)[S]/(S^2 - (1-4x))$ relies on exact computer-algebra verification (`notes/check-check-2.py`) rather than a term-by-term hand expansion in `PROOF.md`. `gfis/OEIS-mat` (`holrec/rectopost.man`) and `archmageirvine/joeis` (`A250917.java`) record an unproved Maple `sumrecursion` order-3 recurrence guess on the OEIS binomial sum formula (of which Mathar's order-5 recurrence is a $\mathbb{Q}(n)$-left-multiple) without proof, creative-telescoping certificate, or equivalence proof to $\exp(x C(x)^3)$.
  - Internal audit and SymPy exact symbolic verification are not formal peer review or a formal Lean proof.

---

### `oeis-A108430` — Proof of Mathar's 2022 D-Finite Recurrence for OEIS `A108430`

- **Summary**: R. J. Mathar conjectured in 2022 that OEIS `A108430(n)` (the total number of $d = (1,-1)$ steps in first-quadrant lattice paths from $(0,0)$ to $(3n,0)$ using steps $u = (2,1)$, $U = (1,2)$, and $d = (1,-1)$) satisfies an explicit order-3 polynomial-coefficient recurrence. Using the bivariate path decomposition $G(t,z) = 1 + t z G(t,z)^2(1 + t G(t,z))$ and Lagrange inversion to recover the generating function $A(z) = \left.\frac{\partial G}{\partial t}\right|_{t=1}$, we translated the recurrence into a differential operator acting on $A(z)$ inside the degree-3 algebraic field $\mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$. Exact symbolic reduction shows $\Phi(z) = -42291 z - 49573 z^2$, which forces every coefficient $[z^n]\Phi(z) = 0$ and thus proves Mathar's recurrence for all $n \ge 3$.
- **Exact statement & source**:
  - Source: OEIS `A108430` (revision 14, 2025-11-05).
  - Name: *"Number of d steps in all paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1), U=(1,2), or d=(1,-1)."* (offset `1,1`).
  - Conjecture (Formula section): *"Conjecture D-finite with recurrence n*(2*n+1)*(23982*n-28681)*a(n) +(-640736*n^3+1168048*n^2-901220*n+247035)*a(n-1) +(1196488*n^3-6448608*n^2+10992587*n-5911365)*a(n-2) +2*(2*n-5)*(28283*n-6993)*(n-3)*a(n-3)=0. - _R. J. Mathar_, Jul 24 2022"* (proved for all $n \ge 3$, with boundary terms $a(0)=a(-1)=a(-2)=0$ and $c_3(3)=0$).
- **Label**: `written proof, internally audited` (supported by exact combinatorial/Lagrange inversion check and exact differential-algebraic reduction in $\mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$ in `notes/check-check-1.py`).
- **Verification command**: `.venv/bin/python targets/oeis-A108430/notes/check-check-1.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T21:46:56Z`–`22:18:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live OEIS `A108430` (rev 14), live `1337isnot1337/solved-conjectures` & `trureturing`, GitHub code/issue/repo searches, live arXiv API, Zenodo API, Crossref, and web search (Gate 3 OpenAlex/S2 returned HTTP 429); 0 prior proofs found.
- **What is not established**:
  - **Exact symbolic reduction caveat (`AUDIT.md` §3.3):** The reduction of $\Phi(z) = \sum_{r=0}^3 c_r(\theta)[z^r A(z)]$ to $-42291 z - 49573 z^2$ in $\mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$ relies on exact computer-algebra verification (`notes/check-check-1.py`) rather than an expanded hand derivation of the intermediate 3-component rational expressions in `PROOF.md`.
  - **Deutsch (2000) print JSTOR caveat (`TARGET.md` & Gate 3 receipts):** The print-only JSTOR full text of Emeric Deutsch (*Amer. Math. Monthly* 107, 2000, Problem 10658, pp. 368–370), which established the path enumeration and binomial sum formula prior to Mathar's 2022 recurrence conjecture, was not downloaded.
  - Internal audit and SymPy exact symbolic verification are not formal peer review or a formal Lean proof.

---

### `linusson-2512.24346-conj1` — Proof of Linusson–Özdemir Conjecture 1 (`conj:complement`)

- **Summary**: Svante Linusson and Alperen Özdemir conjectured that the stationary distribution $\pi$ of the finite $k$-Plancherel Markov chain on $\mathcal{R}_k$ satisfies the complement symmetry $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$ for all $\lambda \in \mathcal{R}_k$. We proved this conjecture for all $k \ge 1$ by establishing an explicit product formula $\pi(\lambda) \propto \frac{d_\lambda^{(k)} d_{\lambda^{\mathrm{comp}}}^{(k)}}{|\lambda|! |\lambda^{\mathrm{comp}}|!}$ and proving exact $R$-reversibility under the involution $R(\lambda) = \lambda^{\mathrm{comp}}$. Using a Maya-diagram bijection with $k$-TASEP configurations and Lapointe–Morse's $k$-rectangle theorem, we showed that every weak cover translates into an adjacent swap whose complement reverses the transition with identical $k$-rectangle weights, while constructive 3-phase paths prove irreducibility.
- **Exact statement & source**:
  - Source: Svante Linusson and Alperen Özdemir, *"The $k$-Plancherel Measure and a Finite Markov Chain"*, `arXiv:2512.24346v1` (`Kplancherel.tex`, Section 3.4, Conjecture 1 `\label{conj:complement}`, lines 641–645).
  - Statement: *"For a $\lambda\in\mathcal{R}_k$, let $\lambda^{\mathrm{comp}}\in\mathcal{R}_k$ be such that $\lambda \cup \lambda^{\mathrm{comp}} = (k-1,(k-2)^2,\ldots,i^{k-i},\ldots,2^{k-2},1^{k-1})$, that is $l_i(\lambda)+l_i(\lambda^{\mathrm{comp}})=k-i$. Conjecture (Symmetry of complements): For all $\lambda\in\mathcal{R}_k$, $\pi(\lambda)=\pi(\lambda^{\mathrm{comp}})$."*
- **Label**: `written proof, internally audited` (supported by exact integer/`Fraction` verification of Lemmas 1–4, $R$-reversibility, stationarity, and $k=1..5$ tables in `notes/check-check-2.py`).
- **Verification command**: `.venv/bin/python targets/linusson-2512.24346-conj1/notes/check-check-2.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T23:05:24Z`–`23:10:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**` (333 files), `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*` (`SCREENED-OUT*.md`), `aliromman/math`, `alp-oz/kcore-chain`, live arXiv API (`2512.24346v1` unchanged), OpenAlex (`cited_by_count: 0`), Zenodo, Crossref, and web search; 0 prior proofs found.
- **What is not established**:
  - Does not settle the authors' remaining sibling conjectures in `arXiv:2512.24346v1` (`conj:lcd`, `conj:minimum`, `conj:rho`).
  - Internal audit and small-$k$ ($k \le 5$) exact checks are not external peer review or a Lean formalization.

---

### `oeis-A006255` — Proof of Corneth/Padhi Conjecture on Graham's Sequence (`A006255`)

- **Summary**: On OEIS `A006255`, David A. Corneth (2016) and Jaideep Padhi (2026) conjectured that for Graham's sequence $a(n)$ and $b(n) = \mathrm{A006530}(\mathrm{A007913}(n))$, whenever $b(n)^2 \ge 2n$ one has $a(n) = n + b(n)$ except at $n \in \{2, 3, 10, 171\}$. We proved this conjecture unconditionally for all $n \ge 1$ by reducing $b(n)^2 \ge 2n$ to $n = kp$ with $p$ prime and $1 \le k \le (p-1)/2$, giving a short 4-element proof for $k \le (p-3)/2$, and handling the boundary $n = p(p-1)/2$ via a 78-leaf polynomial odd-cycle covering tree modulo $2520$ plus $10$ explicit finite witnesses. We also proved directly that $a(n) > n + b(n)$ at the four exceptional values $n \in \{2, 3, 10, 171\}$.
- **Exact statement & source**:
  - Source: OEIS `A006255` (revision 106, 2026-06-19, Comments section), referencing `A007913` (rev. 213) and `A006530` (rev. 248).
  - Statement: *"Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"*
- **Label**: `written proof, internally audited` (supported by exact integer/`Fraction` verification in `notes/check-check-1.py`).
- **Verification command**: `.venv/bin/python targets/oeis-A006255/notes/check-check-1.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T23:05:24Z`–`23:10:00Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**`, live OEIS `A006255` (rev. 106), `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, live arXiv API, Zenodo, Crossref, and web search (OpenAlex/S2 returned HTTP 429); 0 prior proofs found.
- **What is not established**:
  - **78-leaf script verification caveat (`AUDIT.md` §4):** The congruence integrality, thresholds $M_0, M_0'$, disjoint $1152/1152$ residue coverage mod $2520$, and enumeration of the $10$ uncovered primes below $M_0$ in Table 1 and the $10$ Table 2 witnesses are verified by exact integer/rational computation (`notes/check-check-1.py`), not by hand calculation of all 78 rows.
  - Does not determine $a(n)$ outside the regime $b(n)^2 \ge 2n$, nor address Corneth's separate question on `A277624`.
  - Internal audit and exact computation are not external peer review or a Lean formalization.

---

### `oeis-A386251` — Counterexample to Hohn's 3-Segment Closed Walk Conjecture (`A386251`)

- **Summary**: Charles L. Hohn conjectured on OEIS `A386251` that for all dimensions $n \ge 6$, the shortest closed walk of noncongruent primitive all-nonzero lattice diagonals in $\mathbb{Z}^n$ is always achieved by a 3-segment walk. We disproved this conjecture for an infinite family of dimensions $n = m^2 - 30$ ($m \ge 92$, starting at $n = 8434$) by constructing an explicit 4-segment non-self-intersecting closed walk of four pairwise noncongruent primitive vectors of length $m$ each, giving total length $4m$. We then proved elementarily that every valid 3-segment closed walk in dimension $n = m^2 - 30$ ($m \ge 92$) has length at least $4m + 2$, so $a(m^2 - 30) = 4m$ is never realized by a 3-segment walk.
- **Exact statement & source**:
  - Source: OEIS `A386251` (revision 22, 2025-08-06, Charles L. Hohn).
  - Name & Comment: *"Consider the graph whose vertices are the points of the n-dimensional cubic lattice with points connected by all integer-length diagonals that traverse all n dimensions and do not intersect intermediate points. a(n) is the total length of the shortest possible closed walk in this graph via noncongruent diagonals."* / *"It is provable that all such walks must be even in total length. It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks."*
- **Label**: `written proof, internally audited` (an explicit infinite family of 4-segment witnesses for $n = m^2 - 30$, $m \ge 92$ verified by exact integer computation in `notes/check-check-3.py`, paired with an internally audited elementary proof that every 3-segment walk has length $\ge 4m + 2$).
- **Verification command**: `.venv/bin/python targets/oeis-A386251/notes/check-check-3.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T23:07:13Z`–`23:16:07Z`, `notes/novelty-gate3-watch-3.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**` (333 files), live OEIS `A386251` (rev. 22), `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, live arXiv API, Zenodo, Crossref, and web search; 0 prior refutations found.
- **What is not established**:
  - Does not identify the smallest dimension $n \ge 6$ where a 3-segment walk fails to attain $a(n)$ (the specific $m^2 - 30$ family begins at $m = 92, n = 8434$).
  - Internal audit and finite exact checks are not external peer review or a Lean formalization.

---

### `yip-2309.10950-rem3.1` — Proof of Yip's $d = 2$ van Lint–MacWilliams Conjecture (`arXiv:2309.10950v2` Theorem 1.7 / Remark 3.3)

- **Summary**: Chi Hoi Yip conjectured in Section 3.2 (Remark 3.3) of `arXiv:2309.10950v2` (*Canad. J. Math.* 78 (2026), 594–618) that Theorem 1.7 extends to $d = 2$ for every odd square $q \ge 49$: any $A \subset \mathbb{F}_q$ satisfying $A \hat{+} A \subset S_2 \cup \{0\}$ has $|A| \le \sqrt{q}$, with equality if and only if $A = \alpha \mathbb{F}_{\sqrt{q}}$ for some $\alpha \in S_2$. We proved this conjecture completely for all odd squares $q = r^2 \ge 49$, settling the sumset case via spectral bounds and Blokhuis (1984) and handling restricted sumsets via a weighted Stepanov polynomial family $H_k(Y)$ forcing non-squares onto a norm circle or affine line. Applying Hasse's theorem to the resulting genus-1 curves closes all $r \ge 11$ unconditionally, and explicit orbit and characteristic-3 witness reductions rule out non-canonical equality sets at $r = 7$ ($q = 49$) and $r = 9$ ($q = 81$).
- **Exact statement & source**:
  - Source: Chi Hoi Yip, *"Restricted sumsets in multiplicative subgroups"*, `arXiv:2309.10950v2` (`main.tex`, Section 1 Theorem 1.7 `\label{thm:VLM}` lines 105–107 and Section 3.2 Remark 3.3 lines 405–407; published in *Canad. J. Math.* 78(2) (2026), 594–618, DOI `10.4153/S0008414X24000920`).
  - Theorem 1.7 & Remark 3.3: *"Let $d \geq 3$. Let $q \equiv 1 \pmod d$ be an odd prime power and a square. If $A \subset \mathbb{F}_q$ such that $A\hat{+}A \subset S_d \cup \{0\}$, then $|A| \leq \sqrt{q}$, with the equality holds if and only if $d \mid (\sqrt{q}+1)$ and $A=\alpha \mathbb{F}_{\sqrt{q}}$, where $\alpha \in S_d$."* / *"Nevertheless, we conjecture that when $q$ is an odd square and $q \geq 49$, the statement of Theorem 1.7 also extends to the case $d=2$."*
- **Label**: `written proof, internally audited` (supported by exact finite-field checks of Lemma 2.2–2.3, norm-circle sums, Hasse bounds, and the $r = 7, 9$ witnesses in `notes/check-check-2.py`).
- **Verification command**: `.venv/bin/python targets/yip-2309.10950-rem3.1/notes/check-check-2.py`
- **Latest novelty receipt**: Gate 3 PASS (`2026-11-26T23:27:07Z`–`23:32:30Z`, `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`): checked all `watch/snapshots/**` (356 files), `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, live arXiv API (`2309.10950v2` sole version), OpenAlex (`cited_by_count: 0` in Gate 3 snapshot), Zenodo, Crossref, and web search; 0 prior proofs found.
- **What is not established**:
  - Relies on Blokhuis (1984) and Hasse (1933) as external classical theorems, and uses exact finite-field computation (`notes/check-check-2.py`) for verification of small-case witnesses at $r = 7, 9$ and lemma sanity checks.
  - Internal audit and exact finite-field testing are not external peer review or a Lean formalization.





