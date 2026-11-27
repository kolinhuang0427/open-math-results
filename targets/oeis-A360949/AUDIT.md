# Adversarial Audit — `targets/oeis-A360949/`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-27T01:40Z` (Gate 3 pending)
- **Target:** OEIS **A360949** (Paul D. Hanna, Mar 03 2023; rev. 15, `2023-03-05T12:37:19-05:00`), mod-4 Thue–Morse (`A161674` / `A010060`) conjecture.
- **Isolation:** Inspected ONLY live primary sources (OEIS `A360949` rev. 15, `A161674` rev. 21, `A010060` rev. 619, `A325574` rev. 10 via helper), `TARGET.md`, `PROOF.md`, independent checker files (`notes/check-check-3.md`, `notes/check-check-3.py`), Gate 2 receipts (`notes/novelty-gate2-watch-{1,3,5,6}.md`), and adversarial helper report (`notes/audit-helper-a360949.md`). Did **not** read `verify.py` or author scratch `notes/`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Fidelity & Definition Verification

Verified directly against live OEIS JSON (`notes/audit-helper-a360949.md` §1):
1. **OEIS `A360949` (rev. 15, `2023-03-05`, offset `0,2`):**
   - **Name:** `G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.`
   - **Data (terms `0..21`):** `1,2,8,50,376,3124,27804,260496,2539616,25556330,263922884,2785341186,29948035032,327315887046,3630399545244,40813503158790,464662514679168,5354222585965310,62419468527625408,736098528973804246,8781173950238637928,105987886325647341056`.
   - **Comment (verbatim):** `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the Thue-Morse sequence.`
   - **PARI/GP program:** Verified mathematically and numerically equivalent to the defining functional equation.
2. **OEIS `A161674` (rev. 21, `2021-01-30`, offset `1,3`):** `Positions n such that A010060(n) + A010060(n+2) = 1.` Data starts `0,1,4,5,6,7,8,9,12,13,...`.
3. **OEIS `A010060` (rev. 619, offset `0,1`):** Thue–Morse sequence $t_0 = 0, t_{2n} = t_n, t_{2n+1} = 1 - t_n \in \{0, 1\}$.
4. **Match:** `TARGET.md` and `PROOF.md` match live OEIS definitions, offsets (`0`-based `A360949`/`A010060`, `1`-based `A161674`), and conjecture statement verbatim with zero drift.

---

## 2. Adversarial Line-by-Line Mathematical Audit of `PROOF.md`

Audited every step of `PROOF.md` (lines 1–68) with zero gaps found:
- **Step 1 (Existence, uniqueness, and integrality of $B(x) = (A(x)-1)/2$, lines 15–33):**
  - The $n=0$ term is $(-x/2)^0(A(x)^0 + 1)^0 = 1$ (no $0^0$ ambiguity since $1+1=2$). Subtracting $1$ leaves $\sum_{n \ge 1} (-x/2)^n (A(x)^n + (-1)^n)^n = 0$ (formally convergent in $\mathbb{Q}[[x]]$ since the $n$-th summand lies in $x^n \mathbb{Q}[[x]]$).
  - Extracting $[x^1]$ gives $-\frac{1}{2}(a(0)-1) = 0 \implies a(0) = 1$ uniquely.
  - Writing $A(x) = 1 + 2 B(x)$ with $B(x) = \sum_{k \ge 1} b_k x^k \in x \mathbb{Q}[[x]]$:
    - $n = 1$: $-x B(x)$.
    - $n = 2m$ ($m \ge 1$): $+x^{2m} P_{2m}(B(x))^{2m}$ with $P_{2m}(B) = 1 + \sum_{r=1}^{2m} \binom{2m}{r} 2^{r-1} B^r \in \mathbb{Z}[B]$.
    - $n = 2m + 1$ ($m \ge 1$): $-x^{2m+1} Q_{2m+1}(B(x))^{2m+1}$ with $Q_{2m+1}(B) = \sum_{r=1}^{2m+1} \binom{2m+1}{r} 2^{r-1} B^r \in \mathbb{Z}[B]$.
  - Extracting $[x^{k+1}]$ ($k \ge 1$) isolates $-b_k$ from $n=1$ against a polynomial in $\mathbb{Z}[b_1, \dots, b_{k-1}]$ from $n \ge 2$ (checked directly at $k=1 \implies b_1 = 1, a(1)=2$ and $k=2 \implies b_2 = 4, a(2)=8$). Strong induction gives unique $B(x) \in x\mathbb{Z}[[x]]$, $a(k) = 2 b_k \in 2\mathbb{Z}$, and $a(k) \equiv 2 \pmod 4 \iff b_k \equiv 1 \pmod 2$. Complete.
- **Step 2 (Reduction modulo $2$ in $\mathbb{F}_2[[x]]$, lines 35–50):**
  - For $m \ge 1$, $P_{2m}(B) \equiv 1 \pmod 2$ (since $\binom{2m}{1}=2m$ and $2^{r-1}$ for $r \ge 2$ are even) and $Q_{2m+1}(B) \equiv B \pmod 2$ (since $2m+1$ is odd and $2^{r-1}$ for $r \ge 2$ is even). Including $n=1$ ($m=0$) gives $0 = \sum_{m \ge 1} x^{2m} + \sum_{m \ge 0} x^{2m+1} B^{2m+1} = \frac{x^2}{1+x^2} + \frac{x B}{1 + x^2 B^2}$ in $\mathbb{F}_2[[x]]$ (both sums converge formally since $B(0) = 0$ and $1+x^2 B^2 \in 1+x^4\mathbb{F}_2[[x]]$ is a unit).
  - Clearing denominators and dividing by $x$ in the integral domain $\mathbb{F}_2[[x]]$ yields $(1+x^2) B(x) = x + x^3 B(x)^2$.
  - Splitting $B(x) = B_0(x^2) + x B_1(x^2)$: $B(x)^2 = B_0(x^4) + x^2 B_1(x^4)$ is purely even, so $x + x^3 B(x)^2$ is purely odd. Equating even parts gives $(1+x^2) B_0(x^2) = 0 \implies B_0(x^2) = 0$ (hence $a(2k) \equiv 0 \pmod 4$ for all $k \ge 1$). Substituting $B(x) = x C(x^2)$ ($C := B_1 \in \mathbb{F}_2[[y]]$) gives $(1+x^2) x C(x^2) = x + x^5 C(x^2)^2$; dividing by $x$ and setting $y = x^2$ yields $y^2 C(y)^2 + (1+y) C(y) + 1 = 0$ in $\mathbb{F}_2[[y]]$, which uniquely determines $C(y)$ coefficient-by-coefficient ($c_0 = 1$, $c_m = c_{m-1} + [y^m](y^2 C(y)^2)$). Complete.
- **Step 3 (Identification with Thue–Morse `A161674`, lines 52–68):**
  - For $T(y) = \sum_{m \ge 0} t_m y^m \in \mathbb{F}_2[[y]]$, splitting even/odd terms and using $T(y^2) = T(y)^2$, $1+y^2 = (1+y)^2$ gives $T(y) = (1+y) T(y)^2 + \frac{y}{(1+y)^2}$, i.e., $(1+y)^3 T(y)^2 + (1+y)^2 T(y) + y = 0$.
  - Since $t_m, t_{m+2} \in \{0,1\}$, $t_m + t_{m+2} = 1$ in $\mathbb{Z}$ iff $t_m + t_{m+2} \equiv 1 \pmod 2$. With $t_0 = 0, t_1 = 1$, $\widetilde{C}(y) := \sum_{m \ge 0} (t_m + t_{m+2}) y^m = T(y) + \frac{T(y)+y}{y^2} = \frac{(1+y)^2 T(y) + y}{y^2}$, so $(1+y)^2 T(y) = y + y^2 \widetilde{C}(y)$ and $(1+y)^4 T(y)^2 = y^2 + y^4 \widetilde{C}(y)^2$.
  - Multiplying $(1+y)^3 T(y)^2 + (1+y)^2 T(y) + y = 0$ by $(1+y)$ and substituting cancels $y(1+y) + y(1+y) = 0$ in $\mathbb{F}_2[[y]]$, leaving $y^4 \widetilde{C}(y)^2 + y^2(1+y)\widetilde{C}(y) + y^2 = 0$; dividing by $y^2$ gives $y^2 \widetilde{C}(y)^2 + (1+y)\widetilde{C}(y) + 1 = 0$.
  - Uniqueness in $\mathbb{F}_2[[y]]$ forces $C(y) = \widetilde{C}(y)$, completing the proof. Complete and airtight.

---

## 3. Independent Computational Verification

Re-ran independent checker script `targets/oeis-A360949/notes/check-check-3.py` (`notes/audit-helper-a360949.md` §3):
- Command: `time .venv/bin/python targets/oeis-A360949/notes/check-check-3.py`
- Result: **PASS**, exit code `0`, wall time `2.529s`.
- Verified exact `Fraction` solution of the defining functional equation for $n = 0..35$ (matching all 22 OEIS `A360949` terms and $a(n) \bmod 4$ against `A161674` up to $m \le 104$) and all $\mathbb{F}_2[[x]] / \mathbb{F}_2[[y]]$ identities in Steps 2–3 up to degree 80.

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-a360949.md` §2, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,3,5,6}.md`) confirmed:
- **No prior proof found** on live OEIS (`A360949` rev. 15 still marked `Conjecture:`, sister sequence `A325574` rev. 10 and `A161674` rev. 21 contain no proof), across `367` local watch snapshots, all 16 `the-omega-institute/trureturing*` repos (confirmed the single `trureturing` code hit is a SHA-256 hex substring), all 223 `mathesis-papers` repos, `dvgyl/oeis-proofs`, `joaquimmj/oeis-conjectures`, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, global GitHub, arXiv, Zenodo, Crossref, and web search.
- **No `CONTESTED.md`** exists in `targets/oeis-A360949/`.
- **What Is Not Established / Caveats:**
  - Proves the mod-4 characterization of `A360949` (and equivalently the mod-$2^{n+2}$ congruence of `A325574(n) = 2^n A360949(n)`); does not investigate higher $2$-adic valuations (mod 8, etc.) or Formula (2) of `A360949`.
  - OpenAlex and Semantic Scholar APIs were rate-limited (`HTTP 429`) during Gate 2; `JENW1N/complete-math-solutions` and `TheJustinSunPrize/awards` will be covered in Gate 3.
  - Internal audit and finite exact checks are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`.

- **Gate 3 Novelty Clearance (`2026-11-27T02:00Z`–`03:09Z`):** **PASS** across all four watcher receipts (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-3.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`), covering live OEIS `A360949` rev. 15, Zenodo, `413` watch snapshots, `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, and `DomTheDeveloper/ProofPlaygrond`. Cleared for coordinator verification.

---

## 6. Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T09:29Z`) — **PASS**

- **Lean module:** `lean/OpenMath/OeisA360949.lean` (1,257 lines; imported in `lean/OpenMath.lean` line 12)
- **Primary sources verified verbatim against live OEIS JSON:**
  - `A360949` (rev. 15, `2023-03-05`, offset `0,2`): `G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.` Comment: `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the Thue-Morse sequence.`
  - `A161674` (rev. 21, `2021-01-30`, offset `1,3`): `Positions n such that A010060(n) + A010060(n+2) = 1.`
- **Statement-fidelity verification:**
  - `hannaTerm` and `SatisfiesA360949Eq` faithfully formalize $1 = \sum_{n \ge 0} (-X/2)^n (A^n + (-1)^n)^n$ in $\mathbb{Q}[[X]]$ (with `coeff_hannaTerm_eq_zero_of_lt` proving all $n > k$ terms vanish at $[X^k]$).
  - `existsUnique_a360949` and `coeff_ASeries` prove there is a unique solution `ASeries` in `PowerSeries ℚ` whose coefficients are the integers `a360949 : ℕ → ℤ`.
  - `thueMorse` satisfies `t(0) = 0`, `t(2n) = t(n)`, `t(2n+1) = 1 - t(n)` (`A010060`), `IsA161674 m := thueMorse m + thueMorse (m + 2) = 1` is proved infinite (`setOf_isA161674_infinite`), and `a161674 k := Nat.nth IsA161674 (k - 1)` matches offset-1 `A161674` for all $k \ge 1$.
  - `hanna_conjecture_A360949_A161674` (and `hanna_conjecture_A360949`) matches Hanna's OEIS conjecture verbatim: `a360949 0 = 1`, `a360949 (2 * a161674 k + 1) ≡ 2 [ZMOD 4]` for all `k ≥ 1`, and `a360949 n ≡ 0 [ZMOD 4]` for all other `n ≥ 1`.
- **Hygiene audit:** `grep -nE 'sorry|admit|axiom |native_decide|unsafe|implemented_by|extern |partial '` matched only docstring line 20 (zero `sorry`, zero `admit`, zero custom `axiom`, zero `native_decide`, zero `unsafe`). All 4 main theorems (`existsUnique_a360949`, `coeff_ASeries`, `hanna_conjecture_A360949`, `hanna_conjecture_A360949_A161674`) are checked by `#print axioms` (lines 1252–1255).
- **Verdict:** **PASS** (handed off directly to `@coordinator` for final `lake build` + `lake env lean` verification).
