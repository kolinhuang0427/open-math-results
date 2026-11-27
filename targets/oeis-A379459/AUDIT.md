# Adversarial Audit — `targets/oeis-A379459/`

- **Auditor:** `@audit-2` (blind adversarial audit; did NOT read author `verify.py` or author scratch notes)
- **Date (UTC):** `2026-11-27T11:48Z`
- **Verdict:** **PASS (Rescoped strictly to `A379459(n, 0) = A006351(n + 2)`)** *(re-audit `2026-11-27T11:52Z` — see §5 contest ruling `partial-overlap-still-open` and §6 re-audit PASS; label: `written proof, internally audited`)*

---

## 1. Statement & Primary-Source Fidelity

Verified verbatim against the official OEIS data mirror (`github.com/oeis/oeisdata`):
- **`A379459.seq`** (`#4 Jan 03 2025 02:03:22`, offset `0,1`, 45 listed terms):
  - `NAME`: `Array read by downward antidiagonals: A(n,k) = A(n-1,k+1) + 2*(k+1)!*Sum_{j=0..k} A(n-1,j)/j! with A(0,k) = 2*(k+1)!, n >= 0, k >= 0.` — matches `TARGET.md` L14 verbatim.
  - `FORMULA`: `Conjecture: A(n,0) = A006351(n+2).` — matches `TARGET.md` L17 verbatim.
- **`A379460.seq`** (`#4 Jan 03 2025 02:03:31`, offset `0,3`, 55 listed terms):
  - `NAME`: `Array read by downward antidiagonals: A(n,k) = A(n,k-1) + (k+1)*(A(n-1,k) + A(n-1,k+1)) with A(n,0) = A(n-1,0) + A(n-1,1), A(0,k) = 1, n >= 0, k >= 0.` — matches `TARGET.md` L19 verbatim.
  - `FORMULA`: `Conjecture: A(n,0) = A006351(n+1).` — matches `TARGET.md` L22 verbatim.
- **`A006351.seq`** (`M1885 #195 Oct 30 2026 09:37:07`, offset `1,2`, 20 listed terms):
  - `NAME`: `Number of series-parallel networks with n labeled edges. Also called yoke-chains by Cayley and MacMahon.` — matches `TARGET.md` L24 verbatim.
  - `FORMULA`: `E.g.f. is reversion of 2*log(1+x)-x.` and `Conjecture: a(n) = A379459(n-2,0) = A379460(n-1,0) for n > 1 with a(1) = 1. - _Mikhail Kurkov_, Jan 16 2025` — matches `TARGET.md` L27–28 verbatim.

---

## 2. Novelty & Compendia Cross-Check

- **Gate 2 receipts:** All three independent Gate 2 checks passed (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`), noting `the-omega-institute/trureturing#27785` is solely an open preregistration with `0` comments and `0` PRs.
- **OEIS compendia snapshots:** Independently checked all 7 OEIS compendia snapshots under `watch/snapshots/` (`zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`, `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, `zenodo-2026-oeis-compendia-ids.md`): **`0` hits** for `A379459` and `A379460`.
- **Official OEIS mirror status:** All three conjectures remain unmarked by proof in `A379459.seq`, `A379460.seq`, and `A006351.seq`.

---

## 3. Line-by-Line Proof Audit (`PROOF.md`)

1. **Row EGF for $A_{459}$ (§1.1, L22–28):**
   - $H_n(y) = \sum_{k \ge 0} \frac{A_{459}(n,k)}{k!} y^k \in \mathbb{Q}[[y]]$ gives $H_0(y) = \sum_{k \ge 0} 2(k+1) y^k = \frac{2}{(1-y)^2}$.
   - Dividing the defining recurrence by $k!$ gives $\frac{A_{459}(n,k)}{k!} = (k+1)\frac{A_{459}(n-1,k+1)}{(k+1)!} + 2(k+1)\sum_{j=0}^k \frac{A_{459}(n-1,j)}{j!}$. Since $\sum_{k \ge 0} (k+1)(\sum_{j=0}^k c_j) y^k = \partial_y(\frac{y}{1-y}\sum_{j \ge 0} c_j y^j)$, summing over $k \ge 0$ gives $H_n(y) = \partial_y H_{n-1}(y) + \partial_y(\frac{2y}{1-y} H_{n-1}(y)) = \partial_y(\frac{1+y}{1-y} H_{n-1}(y))$ for all $n \ge 1$.
2. **Row OGF for $A_{460}$ & equivalence (§1.2, L32–44):**
   - With $P_n(y) = \sum_{k \ge 0} A_{460}(n,k) y^k$ and $\widetilde{W}_n(y) = (1-y)P_n(y)$, we have $\widetilde{W}_0(y) = 1$.
   - For $n \ge 1$, $[y^0]\widetilde{W}_n(y) = A_{460}(n,0) = A_{460}(n-1,0) + A_{460}(n-1,1)$ and for $k \ge 1$, $[y^k]\widetilde{W}_n(y) = A_{460}(n,k) - A_{460}(n,k-1) = (k+1)(A_{460}(n-1,k) + A_{460}(n-1,k+1))$, which uniformly matches $[y^k]\partial_y((1+y)P_{n-1}(y))$ for all $k \ge 0$.
   - Hence $\widetilde{W}_n(y) = \partial_y(\frac{1+y}{1-y}\widetilde{W}_{n-1}(y))$ for all $n \ge 1$, and $\widetilde{W}_1(y) = \partial_y(\frac{1+y}{1-y}) = \frac{2}{(1-y)^2} = H_0(y)$.
   - Induction gives $\widetilde{W}_n(y) = H_{n-1}(y)$ in $\mathbb{Q}[[y]]$ for all $n \ge 1$, whence $A_{460}(n,0) = \widetilde{W}_n(0) = H_{n-1}(0) = A_{459}(n-1,0)$ for all $n \ge 1$, alongside $A_{460}(0,0) = 1 = \mathrm{A006351}(1)$.
3. **Formal transport PDE & identification with `A006351` (§2, L50–67):**
   - $G(x,y) = \sum_{n \ge 0} H_n(y)\frac{x^n}{n!}$ and $W(x,y) = \frac{1+y}{1-y} G(x,y)$ satisfy $W(x,0) = G(x,0) = \sum_{n \ge 0} A_{459}(n,0)\frac{x^n}{n!}$ and the formal IVP $\partial_x W = \frac{1+y}{1-y}\partial_y W$, $W(0,y) = \frac{2(1+y)}{(1-y)^3}$.
   - Uniqueness in $\mathbb{Q}[[x,y]]$ is immediate from $(n+1)[x^{n+1}]U = \frac{1+y}{1-y}\partial_y([x^n]U)$.
   - Since $\Phi(u) = 2\ln(1+u) - u \in u\mathbb{Q}[[u]]$ has $\Phi'(u) = \frac{1-u}{1+u}$ with $\Phi'(0) = 1$, $\eta(x,y) := \Phi^{-1}(\Phi(y)+x) \in \mathbb{Q}[[x,y]]$ is well-defined with $\eta(0,0)=0$, $\eta(0,y)=y$, and $\partial_x\eta = \frac{1+y}{1-y}\partial_y\eta$.
   - Thus $U(x,y) = \frac{2(1+\eta)}{(1-\eta)^3} \in \mathbb{Q}[[x,y]]$ solves the same IVP, so $W(x,y) = \frac{2(1+\eta)}{(1-\eta)^3}$.
   - Setting $y = 0$ gives $\Phi(\eta(x,0)) = x \implies \eta(x,0) = B(x) = \sum_{m \ge 1} \mathrm{A006351}(m)\frac{x^m}{m!}$. Differentiating $\Phi(B)=x$ twice yields $B' = \frac{1+B}{1-B}$ and $B'' = \frac{2B'}{(1-B)^2} = \frac{2(1+B)}{(1-B)^3} = W(x,0) = G(x,0)$.
   - Extracting $[\frac{x^n}{n!}]$ yields $A_{459}(n,0) = \mathrm{A006351}(n+2)$ for all $n \ge 0$, and hence $A_{460}(n,0) = \mathrm{A006351}(n+1)$ for all $n \ge 0$, settling all three conjectures unconditionally.

No gaps, edge-case errors, or hidden assumptions found.

---

## 4. Independent Verifier Audit (`notes/check-check-2.py`)

- **AST float audit:** `FLOAT_CONSTANTS: 0 []`, `FLOAT_CALLS: 0 []` (strictly exact `int` and `fractions.Fraction` formal power series).
- **Execution:** Re-ran `.venv/bin/python -u targets/oeis-A379459/notes/check-check-2.py` -> exit code `0`, `PASS`.
- **Checks confirmed:** Downward antidiagonal recurrences match all 45 official `A379459` `DATA` terms and all 55 official `A379460` `DATA` terms; exact compositional inverse $B(x)$ of $2\ln(1+t)-t$ matches all 20 official `A006351` `DATA` terms and satisfies $B'$ and $B''$ ODEs mod $x^{19}$; operator recursions & $\widetilde{W}_n(y) = H_{n-1}(y)$ ($n=1..11$) and $A_{460}(n,0) = A_{459}(n-1,0)$ ($n=1..16$); bivariate transport PDE in $\mathbb{Q}[[x,y]]$ through total degree 12 and $A_{459}(n,0) = \mathrm{A006351}(n+2)$, $A_{460}(n,0) = \mathrm{A006351}(n+1)$ for $n=0..16$.

---

## 5. Contest Ruling (`2026-11-27T11:51Z`) — **`partial-overlap-still-open`** (Audit **HOLD / FAIL** Pending Rescope)

Following `@watch-6`'s Sweep 6 alert (`CONTESTED.md`, `#1344`), inspected `insorrowmeow/oeis-sequence-proofs` commit `62bc0904513720ccfc9c27b08ec42de31ba695f4` (`2026-11-27T11:08:09Z`) verbatim:
- **`A379460(n, 0) = A006351(n + 1)` — `resolved-elsewhere`:** `proofs/research-batch-09/YokeRows.md` and `proofs/research-batch-09/YokeRows.lean` (citing MO `481674`) prove this exact identity in full (zero `sorry`/`axiom` in Lean 4), committed 31 minutes before `targets/oeis-A379459/` was started (`11:39:36Z`).
- **`A379459(n, 0) = A006351(n + 2)` — STILL OPEN:** Not claimed or settled anywhere in `insorrowmeow/oeis-sequence-proofs` (`A217061.md`/`FactorialSweep.lean` only treats the all-ones initial row `A379458`, not $A_{459}(0, k) = 2(k+1)!$). Moreover, §§1.1 and 2 of our `PROOF.md` prove `A379459(n, 0) = A006351(n + 2)` directly without depending on `A379460`.
- **Required Fix:** `@scout-6` must rescope `TARGET.md` and `PROOF.md` strictly to `A379459(n, 0) = A006351(n + 2)` (and the `a(n) = A379459(n-2, 0)` half of `A006351`), explicitly citing `insorrowmeow/oeis-sequence-proofs` (`62bc090`, `YokeRows.{md,lean}`) as prior settlement of `A379460(n, 0) = A006351(n + 1)` and dropping any novelty claim on `A379460`. Ping `@audit-2` once rescoped for quick re-audit PASS.

---

## 6. Re-Audit Verdict (`2026-11-27T11:52Z`) — **PASS (Rescoped)**

Verified `@scout-6`'s rescoped `TARGET.md` and `PROOF.md` (`#1349`):
- `TARGET.md` (L1–29) removes `OEIS:A379460` from `Identifiers`, adds an explicit `## Scope Note` crediting `insorrowmeow/oeis-sequence-proofs` (`62bc090`, `2026-11-27T11:08:09Z`, `proofs/research-batch-09/YokeRows.{md,lean}`) for `A379460(n, 0) = A006351(n + 1)`, and scopes strictly to `A379459(n, 0) = A006351(n + 2)` ($n \ge 0$, equivalently `A006351(n) = A379459(n - 2, 0)` for $n > 1$).
- `PROOF.md` (L1–46) drops all `A379460` claims, carries the explicit Scope Note, and proves `A379459(n, 0) = A006351(n + 2)` directly via §1 ($H_0(y) = 2/(1-y)^2$, $H_n = \partial_y(\frac{1+y}{1-y} H_{n-1})$) and §2 (formal transport PDE $W(x, y) = \frac{2(1+\eta)}{(1-\eta)^3}$ yielding $G(x, 0) = W(x, 0) = B''(x)$).
- Zero-float `notes/check-check-2.py` already verified every step of this proof (all 45 `A379459` `DATA` terms, `A006351` reversion & $B''$, $H_n$ operator, bivariate transport PDE to degree 12, and $A_{459}(n, 0) = \mathrm{A006351}(n + 2)$ for $n = 0..16$).

**Final Verdict:** **PASS** (rescoped strictly to `A379459(n, 0) = A006351(n + 2)`). Ready for Gate 3 re-check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting.
