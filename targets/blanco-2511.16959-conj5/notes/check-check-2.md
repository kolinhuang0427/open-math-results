# Independent Check Report: `targets/blanco-2511.16959-conj5/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** `arXiv:2511.16959v3` (Saúl A. Blanco, Mikhail P. Golubyatnikov, Elena V. Konstantinova, Natalia V. Maslova, Luka A. Nikiforov, *"Generating the symmetric group by three prefix reversals"*, *DMTCS* **28:1** (2026), Paper #7, DOI `10.46298/dmtcs.16975`; confirmed latest version via `tools/arxiv_fetch.py query --id-list 2511.16959,2610.30892`), TeX file `tools/.arxiv_cache/eprint/2511.16959/Final-DMTCS-Format.tex`.
- **Exact sections/lines verified:**
  - Section 1 (`Final-DMTCS-Format.tex` lines 135–143): definition of prefix reversal $r_i \in \mathrm{Sym}_n$ for $1 < i \le n$ and disjoint-transposition decomposition ($\lfloor i/2 \rfloor$ transpositions).
  - Section 4.1 (`Final-DMTCS-Format.tex` lines 838–960): verified compiled numbering — four conjectures at lines 844, 874, 879, 884 precede `\begin{conjecture}\label{con:F_k(n)}` at lines 948–960, confirming Conjecture 5 verbatim:
    $F_k(n) = \{m : k < m < n,\, \langle r_n, r_m, r_k \rangle = \mathrm{Sym}_n\}$, $\max_{n > k+1} |F_k(n)| = k + 1$ ($k$ even), $\frac{k+1}{2}$ ($k$ odd).
  - Also confirmed `arXiv:2610.30892v1` (Lei–Zhao–Zhu–Wu) treats Conjectures 2–4 only.
- **Comparison with `TARGET.md` and `PROOF.md`:**
  - `TARGET.md` and `PROOF.md` match `arXiv:2511.16959v3` verbatim with zero quantifier or domain drift (all integers $k \ge 2$).
  - Every step of `PROOF.md` is verified self-contained and gap-free:
    - Section 1 (Propositions 1.1 & 1.2): forest $H = (\Omega, E_m \cup E_k)$ with $c(H) = n - \lfloor m/2 \rfloor - \lfloor k/2 \rfloor$, bipartite quotient $Q$ blocking $n$ even ($m+k < n$) and $n$ odd ($m+k < n-1$), plus odd-$k$ odd/even index-partition invariant forcing $m$ even when $k$ is odd.
    - Section 2 (Lemmas 2.1–2.3): right-to-left single-overlap commutator $[g, g'] = (a\ g(a)\ g'(a))$, constructive $3$-cycle spread in $2$-transitive groups, and self-contained second-moment $\sqrt{n}$ minimal-degree bound ($n > (s-1)^2 + 1 \implies \mathrm{Alt}_n \le G$).
    - Section 3 (Proposition 3.1 & Theorem 3.2): CRT modulus $Q = 4\prod_{3 \le q \le k+1} q$, $R \equiv 3 \pmod 4$, Dirichlet prime $n > k^2 + 2$, coprimality $\gcd(a, b) = 1$, exact transitivity via $r_m r_n$ ($y \mapsto y - a$) and $r_n r_k$ ($x \mapsto x + b$), exclusion from $\mathrm{AGL}_1(n)$ via $\ge 2$ fixed points of $r_k$ ($n - k \ge 2$), Burnside's prime-degree theorem giving $2$-transitivity, Lemma 2.3 giving $\mathrm{Alt}_n \le G$, and $n \equiv 3 \pmod 4 \implies r_n \notin \mathrm{Alt}_n$, so $G = \mathrm{Sym}_n$.

## 2. Independent Mechanical Check

Written independently from `arXiv:2511.16959v3` (`Final-DMTCS-Format.tex`) and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/blanco-2511.16959-conj5/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/blanco-2511.16959-conj5/notes/check-check-2.py
  ```
- **Raw output (exit code 0):**
  ```text
  Exhaustive Schreier-Sims F_k(n) + Prop 1.1 & Prop 1.2 for all 4 <= n <= 10: PASS
  Section 2 Lemmas (2.1 single-overlap commutator, 2.3 AGL_1(p) exact moments): PASS
  Section 3 CRT + Dirichlet prime lower-bound construction (k=2..12):
    k= 2: Q=12, n=7, |M_k(n)|=3, Prop3.1 transitive + Schreier-Sims Sym_n: PASS
    k= 3: Q=12, n=19, |M_k(n)|=2, Prop3.1 transitive + Schreier-Sims Sym_n: PASS
    k= 4: Q=60, n=71, |M_k(n)|=5, Prop3.1 transitive + 2-transitive + Lemma2.3 + odd => Sym_n: PASS
    k= 5: Q=60, n=31, |M_k(n)|=3, Prop3.1 transitive + 2-transitive + Lemma2.3 + odd => Sym_n: PASS
    k= 6: Q=420, n=127, |M_k(n)|=7, Prop3.1 transitive + 2-transitive + Lemma2.3 + odd => Sym_n: PASS
    k= 7: Q=420, n=71, |M_k(n)|=4, Prop3.1 transitive + 2-transitive + Lemma2.3 + odd => Sym_n: PASS
    k= 8: Q=420, n=331, |M_k(n)|=9, Prop3.1 transitive + Thm3.2 bounds: PASS
    k= 9: Q=420, n=211, |M_k(n)|=5, Prop3.1 transitive + Thm3.2 bounds: PASS
    k=10: Q=4620, n=3851, |M_k(n)|=11, Prop3.1 transitive + Thm3.2 bounds: PASS
    k=11: Q=4620, n=6007, |M_k(n)|=6, Prop3.1 transitive + Thm3.2 bounds: PASS
    k=12: Q=60060, n=46411, |M_k(n)|=13, Prop3.1 transitive + Thm3.2 bounds: PASS
  PASS (all checks passed in 1.673s)
  ```

## 3. Gate 2 & Contest Status

- **Gate 2 receipts present:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-2.md`, `notes/novelty-gate2-watch-5.md` (all PASS).
- **Contested status:** No `CONTESTED.md` present.
