# Blind Audit Report: `targets/oeis-A123145/` (`@audit-2`)

**Verdict: PASS (re-audit after `#883`/`#897` patches)**

*(Initial audit failed solely on a false inequality on L23; patched and verified below — see §5.)*

---

## 1. Primary Source & Statement Fidelity

- **Primary source verified live:** `https://oeis.org/search?q=id:A123145&fmt=json` (OEIS `A123145`, **revision 31**, `2023-07-16T16:56:53-04:00`).
- **Verbatim check against `TARGET.md`:**
  - `NAME`: `a(1) = 1, a(n) = a(n-1) if n == 1 (mod 4), otherwise a(n) = n * a(n-1) for n >= 2.` — exact match.
  - `OFFSET`: `1,2` — exact match.
  - `DATA`: all 24 terms `a(1) = 1` through `a(24) = 2970855906213888000` — exact match.
  - `FORMULA` (Sergei N. Gladkovskii, Nov 26 2012): `Conjecture: E.g.f.: E(x)=d(G(0))/dx where G(k) = 1 + x/(4*k+1 - x*(4*k+1)/(1 + x - x/(1 + x - x/(x + 1/G(k+1) )))), or shift on 1 left G(0); (continued fraction,5-step).` — exact match.

---

## 2. Blocking Defect (Must Fix)

1. **False inequality in `PROOF.md` L23:**
   - L23 states: `because \prod_{j=0}^m (4k + 4j + 1) \ge 4^{m+1} m!, the series actually defines an entire function on \mathbb{C} for every k \ge 0.`
   - At $k = 0$, this inequality is **false** for $m = 0$ ($1 < 4$), $m = 1$ ($5 < 16$), $m = 2$ ($45 < 128$), and in fact for all $0 \le m \le 123$ (since the $j = 0$ factor is $1$, not $\ge 4$).
   - **Fix:** Replace $4^{m+1} m!$ with **`4^m m!`** (valid for all $k \ge 0, m \ge 0$ since $4k + 1 \ge 1$ at $j = 0$ and $4k + 4j + 1 > 4j$ for $1 \le j \le m$), which still immediately implies that $G(k)$ is entire on $\mathbb{C}$.

*Non-blocking polish (recommended while editing `PROOF.md`):* In L41 and L57–59, note explicitly that depth-$K$ truncations seeded with *any* unit $g_{K+1}^{(K)} \in \mathbb{Q}[[x]]^\times$ have well-defined unit denominators ($D_4(0) = g(0)^{-1} \neq 0$, $D_3(0) = D_2(0) = 1$, $D_1(0) = 4k+1$) and error $O(x^{4K+4})$ (improving to $O(x^{4K+5})$ when $g_{K+1}^{(K)} = 1 + O(x)$), so that the $O(x^{4K+4})$ clause stated in the Theorem (L41) is also justified in the proof.

---

## 3. Mathematical Audit of Core Proof (PASS modulo L23)

- **Lemma 1 (L10–17):** Induction on $m \ge 0$ proving $\frac{a(4m+r)}{(4m+r)!} = \frac{1}{\prod_{j=0}^m (4j+1)}$ for all $r \in \{1,2,3,4\}$ is exact.
- **Section 2 & Lemma 2 (L19–35):** $G(0) = 1 + \sum_{n \ge 1} a(n) x^n/n!$, $E(x) = \frac{d}{dx} G(0) = \sum_{n \ge 0} a(n+1) x^n/n!$, and $G(k) = 1 + \frac{x+x^2+x^3+x^4 G(k+1)}{4k+1}$ for all $k \ge 0$ are exact (except the false L23 lower bound above).
- **Section 3 & Theorem (L37–59):** Bottom-up evaluation $D_4 = \frac{1+xg}{g}$, $D_3 = \frac{1+x+x^2g}{1+xg}$, $D_2 = \frac{1+x+x^2+x^3g}{1+x+x^2g}$, $D_1 = \frac{4k+1}{1+x+x^2+x^3g}$, and $1 + x/D_1 = 1 + \frac{x+x^2+x^3+x^4 g}{4k+1} = G(k)$ are verified algebraically term-by-term. Depth-$K$ truncation error formula $G^{(K)}(0) - G(0) = \frac{x^{4(K+1)}}{\prod_{j=0}^K (4j+1)}(g_{K+1}^{(K)} - G(K+1))$ is exact and proves $x$-adic convergence $G^{(K)}(0) \to G(0)$ and $\frac{d}{dx}G^{(K)}(0) \to E(x)$.

---

## 4. Independent Verification & Gate 2 Novelty

- **Checker script:** Re-ran `.venv/bin/python -u targets/oeis-A123145/notes/check-check-3.py` — `exit 0`, raw output `PASS`, AST `FLOAT_CONSTANTS: 0` (exact `int`/`Fraction` FPS arithmetic mod $x^{42}$ checking all 24 OEIS `DATA` terms, Lemma 1, $G(0)$ & $E(x)$, 5-step CF identity for $k = 0..5$, and truncation error formula for $K = 0..8$).
- **Zenodo & Gate 2 receipts:** Independently verified `0` hits for `A123145` in `watch/snapshots/zenodo-23112421-oeis-ids.md`; all three Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) PASS.

---

## 5. Re-Audit Verification (`2026-11-27T10:55Z`) — **PASS**

Verified `#897` patches in `PROOF.md`:
1. **L23:** Fixed to $\prod_{j=0}^m (4k+4j+1) = (4k+1)\prod_{j=1}^m (4k+4j+1) \ge 4^m m!$ for all $k \ge 0, m \ge 0$ (exact).
2. **L57–59:** Now explicitly covers any unit seed $g_{K+1}^{(K)} \in \mathbb{Q}[[x]]^\times$ ($D_4(0) = 1/g(0) \neq 0$, error $\in x^{4K+4}\mathbb{Q}[[x]]$) and refines to $x^{4K+5}\mathbb{Q}[[x]]$ whenever $g_{K+1}^{(K)} = 1 + O(x)$.
3. **Checker (`notes/check-check-3.py`):** Exact `int`/`Fraction` FPS arithmetic (`FLOAT_CONSTANTS: 0`), verified `exit 0` / `PASS`.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.
