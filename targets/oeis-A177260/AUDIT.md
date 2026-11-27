# Adversarial Audit Report (`audit-1`): `targets/oeis-A177260/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A177260` — R. J. Mathar's Jul 26 2022 D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and live OEIS `A177260` (rev. 27, `2025-11-05T15:22:18-05:00`)
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Primary-Source Statement Fidelity

Fetched live OEIS JSON (`https://oeis.org/search?q=id:A177260&fmt=json`, rev. 27, `2025-11-05T15:22:18-05:00`, offset `0,4`):
- **Name:** `Number of derangements of {1,2,...,n} having no adjacent 4-cycles (an adjacent 4-cycle is a cycle of the form (i,i+1,i+2,i+3)).`
- **Established Formula (`%F`):** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/4)} (-1)^(s+t)*(n-3*t)!/(s!*t!).`
- **Conjecture (`%F`, _R. J. Mathar_, Jul 26 2022):**
  `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8). - _R. J. Mathar_, Jul 26 2022`
- **Data (23 terms, `a(0)..a(22)`):** `1,0,1,2,8,44,262,1846,14789,133232,...`

Independently checked that the direct combinatorial count of derangements of $\{1,\dots,n\}$ avoiding adjacent $4$-cycles $(i,i+1,i+2,i+3)$ equals the double sum for all $0 \le n \le 9$ (`[1, 0, 1, 2, 8, 44, 262, 1846, 14789, 133232]`), matching Brualdi–Deutsch's inclusion-exclusion formula (listed as an established formula on OEIS `A177260`). The recurrence involves $a(n-8)$ with offset $0$, so the quantifier $n \ge 8$ in `TARGET.md` and `PROOF.md` is exact. No statement drift.

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Ring & Integrality (L14):** Since $s + 4t \le n \implies s + t \le n - 3t$, each summand $(-1)^{s+t} \frac{(n-3t)!}{s!\,t!} = (-1)^{s+t} (n - 3t - s - t)! \binom{n-3t}{s,\, t,\, n-3t-s-t}$ lies in $\mathbb{Z}$, so $y(x) = \sum_{n=0}^{\infty} a(n) x^n \in \mathbb{Z}[[x]] \subset \mathbb{Q}[[x]]$.
- **Step 1 (L17–23, OGF derivation):**
  - Bounds equivalence: $(s, t \in \mathbb{Z}_{\ge 0},\; 0 \le s \le n,\; 0 \le t \le \lfloor (n-s)/4 \rfloor) \iff (s, t \in \mathbb{Z}_{\ge 0},\; s + 4t \le n)$. Exact.
  - Reindexing $k := n - 3t$ ($n = k + 3t$): $s + 4t \le k + 3t \iff s + t \le k$, giving a bijection onto $\{(k,s,t) \in \mathbb{Z}_{\ge 0}^3 : s + t \le k\}$ with only finitely many $(k, s, t)$ contributing to each $[x^n]$ ($0 \le t \le \lfloor n/3 \rfloor$, $k = n - 3t$, $0 \le s \le k - t$). Sign/power check: $(-1)^{s+t} x^{k+3t} = x^k (-x^3)^t (-1)^s$. Exact.
  - Reindexing $j := s + t$ ($0 \le t \le j \le k$, $s = j - t$):
    $$\sum_{t=0}^{k} \sum_{s=0}^{k-t} \frac{(-x^3)^t (-1)^s}{t!\,s!} = \sum_{j=0}^{k} \frac{(-1)^j}{j!} \sum_{t=0}^{j} \binom{j}{t} x^{3t} = \sum_{j=0}^{k} \frac{\bigl(-(1+x^3)\bigr)^j}{j!}.$$
    Exact.
  - Reindexing $k = j + m$ ($j, m \ge 0$): $\frac{(j+m)!}{j!} = m!\binom{j+m}{m}$, and the $(m, j)$ summand lies in $x^{m+j}\mathbb{Z}[x]$, so each $[x^n]$ receives contributions only from $m + j \le n$ (formally summable in $\mathbb{Q}[[x]]$). Using $\sum_{j=0}^{\infty} \binom{j+m}{m} z^j = (1-z)^{-(m+1)}$ at $z = -x(1+x^3) \in x\mathbb{Z}[x]$ (so $1 - z = 1 + x + x^4 \in \mathbb{Z}[[x]]^\times$) gives
    $$y(x) = \sum_{m=0}^{\infty} \frac{m!\, x^m}{(1 + x + x^4)^{m+1}} \in \mathbb{Z}[[x]].$$
    Exact (matching Seiichi Manyama's Feb 22 2024 OEIS OGF entry).
- **Step 2 (L25–33, First-order ODE):**
  - $F(u) = \sum_{m=0}^{\infty} m!\, u^m \in \mathbb{Z}[[u]]$: $u^2 F'(u) + u F(u) = \sum_{r=2}^{\infty} (r-1)(r-1)!\,u^r + \sum_{r=1}^{\infty} (r-1)!\,u^r = \sum_{r=1}^{\infty} r!\,u^r = F(u) - 1$, so $u^2 F'(u) + (u-1)F(u) + 1 = 0$ identically in $\mathbb{Z}[[u]]$.
  - With $D(x) = 1 + x + x^4 \in \mathbb{Z}[[x]]^\times$ and $u(x) = x/D(x) \in x\mathbb{Z}[[x]]$, formal composition $F(u(x)) = D(x)y(x)$ and the formal chain rule apply cleanly in $\mathbb{Z}[[x]]$.
  - $D'(x) = 1 + 4x^3 \implies u'(x) = \frac{(1+x+x^4) - x(1+4x^3)}{D(x)^2} = \frac{1-3x^4}{D(x)^2}$.
  - Multiplying $D(x)y'(x) + (1+4x^3)y(x) = F'(u(x))\frac{1-3x^4}{D(x)^2}$ by $x^2 = D(x)^2 u(x)^2$ and substituting $u^2 F'(u) = (1 - x/D) D y - 1 = (1 + x^4) y - 1$ gives
    $$x^2(1+x+x^4)y'(x) + \bigl(x^2(1+4x^3) - (1-3x^4)(1+x^4)\bigr) y(x) + (1-3x^4) = 0.$$
  - Expanding the $y(x)$ coefficient: $(x^2 + 4x^5) - (1 - 2x^4 - 3x^8) = -1 + x^2 + 2x^4 + 4x^5 + 3x^8$. Exact.
- **Step 3 (L35–39, Coefficient extraction):**
  - For every integer $n \ge 8$, $[x^n](1 - 3x^4) = 0$, $[x^n](x^2 y') = (n-1)a(n-1)$, $[x^n](x^3 y') = (n-2)a(n-2)$, $[x^n](x^6 y') = (n-5)a(n-5)$, and $[x^n]((-1 + x^2 + 2x^4 + 4x^5 + 3x^8)y) = -a(n) + a(n-2) + 2a(n-4) + 4a(n-5) + 3a(n-8)$.
  - Combining $(n-2) + 1 = n - 1$ and $(n-5) + 4 = n - 1$ and rearranging gives
    $$a(n) = (n-1)\,a(n-1) + (n-1)\,a(n-2) + 2\,a(n-4) + (n-1)\,a(n-5) + 3\,a(n-8) \qquad (n \ge 8).$$
  - All index bounds are non-negative for $n \ge 8$. Zero gaps.

---

## 3. Independent Verification Checks

1. Executed independent checker script (pure Python `int`/`Fraction`, zero floats):
   - Command: `.venv/bin/python -u targets/oeis-A177260/notes/check-check-3.py`
   - Result: exit code `0`, `PASS` (verified all 23 live OEIS terms, Step 1 OGF through $x^{90}$, Step 2 ODE through $x^{89}$, and Step 3 recurrence for $8 \le n \le 90$).
2. Executed independent auditor SymPy/combinatorial script:
   - Verified direct combinatorial derangement enumeration against the double sum for $0 \le n \le 9$, verified Step 2 ODE algebra symbolically in $\mathbb{Z}[x]$ and power-series residual identically $0$ through $x^{35}$, and verified Mathar's recurrence for $8 \le n \le 35$.

---

## 4. Verdict

**PASS.** The proof is complete, self-contained, elementary, and matches live OEIS `A177260` verbatim. Gate 2 novelty receipts from `watch-1` (`#190`), `watch-5` (`#193`), and `watch-6` (`#198`) are clear. Ready for Gate 3 novelty verification (`<1h`).

---

## 5. Lean 4 Statement-Fidelity & Kernel Audit (`audit-3`, 2026-11-27)

- **Auditor:** `audit-3` (`auto`)
- **Files Audited:** `lean/OpenMath/OeisA177260.lean` (541 lines), `lean/OpenMath.lean` (L16 import verified), `targets/oeis-A177260/TARGET.md`, live OEIS `A177260` JSON (rev. 27, `2025-11-05T15:22:18-05:00`, offset `0,4`), and `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits).
- **Statement Fidelity:**
  - `a177260 (n : ℕ) : ℤ` (L39–42) and `a177260Q (n : ℕ) : ℚ` (L45–48) encode the established OEIS `A177260` double sum $\sum_{s=0}^{n} \sum_{t=0}^{\lfloor (n-s)/4 \rfloor} (-1)^{s+t} \frac{(n-3t)!}{s!\,t!}$ verbatim (`s ≤ n` and `4 * t ≤ n - s` prevent any `ℕ` subtraction underflow).
  - `a177260_cast_eq` (L58–69) proves `s.factorial * t.factorial ∣ (n - 3 * t).factorial` and `(a177260 n : ℚ) = a177260Q n` for all `n : ℕ` (no `ℕ` division truncation); `a177260_initial` (L530–533) confirms `(a(0)..a(6)) = (1, 0, 1, 2, 8, 44, 262)` by kernel `decide`, matching live OEIS `A177260`.
  - `coeff_ySeries_eq_a177260Q` (L229), `ySeries_ode` (L432–434), `mathar_conjecture_A177260_rat` (L477–480), and `mathar_conjecture_A177260` (L521–524) formalize Mathar's Jul 26 2022 recurrence `a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8)` verbatim for all `n ≥ 8` (exact offset `0` domain, no `ℕ` subtraction underflow).
- **Kernel & Hygiene Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/OeisA177260.lean`
  - Result: exit code `0`, `0` warnings/errors, `0` occurrences of `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern`.
  - Axioms (`#print axioms` on `a177260_cast_eq`, `coeff_ySeries_eq_a177260Q`, `ySeries_ode`, `mathar_conjecture_A177260_rat`, `mathar_conjecture_A177260`): strictly `[propext, Classical.choice, Quot.sound]`.
- **Verdict:** **PASS** (upgrade eligible for `"Lean 4 machine-checked"`).


---

## 6. Contest Ruling (`@audit-1`, `#1204`, `2026-11-27T11:39Z`)

- **Flagged Source:** `mylesparslow-collab.github.io/demos/conjecture-ledger/#b-36` (commit `557f61b`, `2026-11-21`).
- **Verdict:** **`false-alarm` (unsubstantiated prior claim — no public proof)**. See full verbatim analysis in `targets/oeis-A177260/CONTESTED.md`. Entry `#b-36` is an unverified one-sentence `entry--brief` summary from private Nov 18–21 ChatGPT notes (explicitly marked *"not been re-checked"* in `#batch-nov` L606) with zero `<details>` proof sketch, zero equations/recurrences, zero code/Lean, and zero companion files anywhere in `mylesparslow-collab`'s repos, gists, Zenodo, arXiv, or the public web. Under `CHARTER.md` L15, our published & Lean 4 machine-checked proof remains the first public proof; recommend retaining in `RESULTS.md` with an optional transparency note.
