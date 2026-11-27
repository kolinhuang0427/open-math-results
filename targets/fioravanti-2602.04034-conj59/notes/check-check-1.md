# Independent Check Report: `targets/fioravanti-2602.04034-conj59`

- **Verdict:** **PASS**
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/fioravanti-2602.04034-conj59/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2602.04034/main.tex` (Stefano Fioravanti, Michael Kompatscher, and Bernardo Rossi, *Clonoids over vector spaces*, `arXiv:2602.04034v1`).
- Confirmed `TARGET.md` reproduces **Conjecture 59** (`\label{conjecture:strong}`, Section 7, lines 1511–1515) and **Conjecture 1** (`\label{conjecture:main}`, Section 1, lines 221–223) verbatim, including the surrounding deduction paragraph (lines 1515) and ring/module conventions (Section 2.2, lines 321–325: unital associative rings, left modules, regular left $\mathbf{R}$-module).
- Verified all compiled theorem/lemma/definition/corollary numbers cited in `PROOF.md` against `main.tex`:
  - `Conjecture 1` (`conjecture:main`, L221), `Lemma 12` (`lemma:rkprod`, L366), `Definition 14` (`def:unifgen`, L403), `Definition 15` (`def:unifrep`, L411), `Lemma 17` (`lemma:urobs`, L432), `Theorem 18` (`theorem:unigen`, L469), `Corollary 20` (`corollary:unigen`, L535), `Proposition 21` (`proposition:ugproduct`, L544), `Corollary 23` (`corollary:fingen`, L603), `Lemma 27` (`lem:unifgenforpolyequiv`, L676), `Lemma 30` (`lemma:ugsubalgebras`, L737), `Corollary 35` (`corollary:orbitsupport`, L806), `Theorem 49` (`theorem:main`, L1229), `Conjecture 59` (`conjecture:strong`, L1511).
- Confirmed mathematical soundness of every step in `PROOF.md`:
  - Central ring homomorphism $\iota : \mathbb{Z}[1/p] \to Z(\mathbf{R})$ whenever $p \cdot 1_R \in R^\times$ (including trivial ring).
  - Lemma 1 (higher-codimension subspace Radon inversion via $q$-Pascal `(P1)` and Cauchy series `(C1)`–`(C2)`), Lemma 2 (subgroup-peeling via $(U_{i,\nu}, V_{i,\nu})$ factor lifting so inner rank $\le k$ is preserved in $\mathbb{Z}/p^e\mathbb{Z}$), Steps 1–4 of Theorem 1 ($k(\mathbf{A}) = \max(1, \log_p |\mathbf{A}|)$), and Theorem 2 (CRT direct-product clone factorization + `Proposition 21` + `Corollary 35` + Mayr–Wynne 2024 `Theorem 1.3`).

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/fioravanti-2602.04034-conj59/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Lemma 1:** Verified `(P1)` vs product formula ($p \in \{2,3,5\}$, $1 \le n \le 10$), `(C1)` and `(C2)` in $\mathbb{Z}[t]/(t^{10})$ ($p \in \{2,3,5\}$, $0 \le n \le 7$, $1 \le M \le 5$), Lemma 1(1) across $p \in \{2,3,5\}$, $1 \le s \le 4$, $s+1 \le m \le s+4$, $0 \le r \le s$, and exhaustive subspace/matrix checks of Lemma 1(2)–(3) for $(p, s, m) \in \{(2, 2, 5), (2, 3, 4), (3, 2, 4)\}$.
2. **Theorem 1 full inductive operator checks (`SNF` inner rank $\le k$ verified):**
   - $\mathbb{Z}_2$ ($m=2$, $4$ points, $10$ matrices, $\mathrm{rk} \le 1$): PASS.
   - $\mathbb{Z}_3$ ($m=2$, $9$ points, $21$ matrices, $\mathrm{rk} \le 1$): PASS.
   - $\mathbb{F}_2^2$ ($m=3$, $64$ points, $204$ matrices, $\mathrm{rk} \le 2$): PASS.
   - $\mathbb{Z}_4$ ($m=3$, $64$ points, $5437$ matrices, $\mathrm{rk} \le 2$): PASS.
   - $\mathbb{Z}_9$ ($m=3$, $729$ points, $1629$ $A_{H_0}$ matrices, $\mathrm{rk} \le 2$, full Steps 1–4 linear operator): PASS.
3. **Mixed / higher-exponent checks:**
   - $\mathbb{Z}_4 \times \mathbb{Z}_2$ ($m=4$, $k=3$, $3$ maximal subgroups, $81992$ $A_{H_0}$ matrices, inner $\mathrm{rk} \le 3$, Step 1 & Step 2 Case 1 / Case 2): PASS.
   - $\mathbb{Z}_8 \times \mathbb{Z}_2$ ($m=5$, $k=4$, all $65536$ pairs $(W', U')$, inner $\mathrm{rk} \le 4$, Step 2 Case 1 & Case 2 collapse): PASS.
4. **Theorem 2 & noncommutative transfer:**
   - CRT + `Proposition 21` verified on $\mathbb{Z}_6$ ($36$ points, $210$ matrices, $\mathrm{rk} \le 1$) and $\mathbb{Z}_{12}$ ($1728$ points, $\mathrm{rk} \le 2$).
   - Raw uncollapsed transfer to the noncommutative ring $\mathbf{R} = M_2(\mathbb{Z}/5\mathbb{Z})$ verified across all $36$ points of $\mathbb{Z}_6^2$ ($210$ matrices) and all $64$ points of $\mathbb{Z}_4^3$ ($5437$ matrices), plus trivial ring case.

## 3. Gate 2 Novelty Status
- Passed by `watch-6` (`#1464`), `watch-5` (`#1466`), and `watch-1` (`#1467`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).
