# Independent Check Report (`@check-2`): `targets/kovalyov-2611.32205-q1/`

**Verdict:** `PASS` (re-checked after `#1755` audit fixes in `#1757`)

## 1. Primary Source & Restatement Verification
- **Primary source:** `tools/.arxiv_cache/eprint/2611.32205/main.tex` (`arXiv:2611.32205v1`, Section 3, Question 3.5(1)–(2), lines 499–505; axiom $(\mathrm{Exp})$ lines 346–350; $\mathsf{IOpen}$, $\mathcal{L}_{\mathrm{OSR}} = (+,\cdot,0,1,\le)$).
- **Match check:** `TARGET.md` states Question 3.5(1)–(2) verbatim and matches the primary source across all quantifiers, domain ($\mathcal{L}_{\mathrm{OSR}}$-sentences, $\mathsf{IOpen}$, $(\mathrm{Exp})$), and compiled numbering (Question 3.5).
- **`PROOF.md` (`#1755` / `#1757` re-check):** Verified patched `PROOF.md` fixes:
  - `(3 B_1)^k N_1` standard upper bound in $E_{0,k}$, $\mathcal{I}_k(2)$, Step 2, and Step 3 (`L54, L75, L90, L96, L99-100, L113, L116`).
  - Explicit Step 2 $k=1$ base case (`L94, L96`), Step 2 sign normalization (`L97`), Step 1 `s_old=0` bound (`L88`), `L30` index floor, `L36` coinciding indices, `L64` scale monotonicity for $j \in \{2,\dots,n\}$, and Step 3 `r=1` sign normalization + $\pm L^{**}$ negative handling (`L116`).
  - Step 3 $r \ge 2$ closed interval $I_r$ and explicit one-sided / $\mathcal{A}_r = \emptyset$ choices (`L110-113`).

## 2. Independent Exact Verifier (`notes/check-check-2.py`)
- **Methodology:** Zero-floating-point Python (`int` and `fractions.Fraction`) written directly from `arXiv:2611.32205v1` and `PROOF.md` (using `tools/.venv/bin/python` / `.venv/bin/python`), simulating Exp-er's full strategy in $G_{n,M}(\mathcal{M}^+)$ over nonstandard elements represented as $\mathbb{Z} \oplus \mathbb{Z}\omega_1 \oplus \mathbb{Z}\omega_2$ (a $\mathbb{Z}\text{-}\mathsf{DOSR}$).
- **Checks covered across 14 standard & nonstandard $\mathbb{Z}\text{-}\mathsf{DOSR}$ plays (including $n=1$ pinned/unpinned & $a_1=2M$, $n=2,3$ nonstandard jumps, $r=1$ strict-bound collision, $r \ge 2$ weak-weak boundary equality, and negative $L^{**}$):
  1. All tuples $(c_0, \dots, c_k) \in [-B_k, B_k]^{k+1}$ (including $c_k=0$ and negative $L(\vec{a})$) verified against $\mathcal{I}_k(1)$–$\mathcal{I}_k(3)$ at every round $k \in \{1, \dots, n\}$.
  2. Exact `Fraction` endpoint verification (`alpha(L)` / `beta(L')` divisibility by $F_{k+1}$, closed interval $I_r$ nonemptiness for $r \ge 2$, and exact collision $\mathrm{LB} = \mathrm{UB}$ handling at $r=1$ prior to $\pm F_{k+1}$ shift).
  3. Exponent caps ($|e_{i,r}| \le E_k$, $|e_{i,0}| \le E_{0,k}$), divisibility $F_{k+1} \mid e_{i,r}$, congruence $e_{i,0} \equiv a_i \pmod{\mu_k}$, and final $\mathrm{Win}_{n,M}$ checks.
- **Run command & output:**
  ```text
  .venv/bin/python -u targets/kovalyov-2611.32205-q1/notes/check-check-2.py
  [PASS] Primary source arXiv:2611.32205v1 verbatim statement, definitions, and Question 3.5 numbering verified.
  [PASS] Winning strategy I_k (incl. c_k=0, I_k(3), n=1 a1=2M, r=1 collision, r>=2 weak-weak equality) verified across 14 Z-DOSR plays.
  PASS
  ```
  (Exit code `0`.)

## 3. Gate Status
- Gate 1: `PASS` (recorded in `TARGET.md`).
- Gate 2: `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
