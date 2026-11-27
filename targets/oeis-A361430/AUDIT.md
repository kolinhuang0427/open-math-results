# Adversarial Audit Report (`audit-1`): `targets/oeis-A361430/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A361430` (rev. 41, Jul 05 2026) & `A298826` (rev. 125, Jun 10 2025) — Vaclav Kotesovec (`a(n) = abs(A298826(n))`), Werner Schulte (`A298826` multiplicative with `a(p^e) = (-1)^p*(e-1)`), and Ridouane Oudra (`A298826(n) = (-1)^(n+1)*Sum_{d|n} mu(d)*tau(d)*tau(n/d)`) conjectures
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and live OEIS `A361430` (rev. 41), `A298826` (rev. 125), `A298825` (rev. 29), `A298674` (rev. 38)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS JSON:
  - **`A361430` (rev. 41, `2026-07-05T01:48:31-04:00`, offset `1,8`):** `NAME`: `Multiplicative with a(p^e) = e - 1.`; `FORMULA`: `Conjecture: a(n) = abs(A298826(n)).`
  - **`A298826` (rev. 125, `2025-06-10T08:41:46-04:00`, offset `1,8`):** `NAME`: `a(n) = A298825(n)/n.`; `FORMULA` includes all three quoted conjectures (Oudra Nov 19 2019, Kotesovec Mar 12 2023, Schulte Jun 09 2025) verbatim.
  - **Primary matrix definition (`A298674` rev. 38, `A298825` rev. 29, and `A298826` PARI program):** `matA[u,d] = 1_{d|u}`, `matB[d,v] = 1_{d|v} mu(d) d`, `matT = matA * matB` gives $T(u, v) = \sum_{d \mid \gcd(u,v)} \mu(d)d = T(v, u)$ (symmetric), and `matD[m, n] = sum_{k|n} T(m, k) T(m+2, n/k)`, so $c(n) = \frac{1}{n}\sum_{m=1}^n \sum_{k \mid n} T(n/k, m) T(k, m+2)$ matches `PROOF.md` L6–8 identically.
- Absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)
- **Section 2 (L17–36, CRT reduction):** Expanding $T(n/k, m) T(k, m+2)$ and swapping finite sums gives $\frac{1}{n}\sum_{k|n}\sum_{d_1|(n/k)}\sum_{d_2|k}\mu(d_1)d_1\mu(d_2)d_2 \sum_{1\le m\le n,\, d_1|m,\, d_2|(m+2)} 1$. Since $d_1 d_2 \mid n$, $L = \mathrm{lcm}(d_1, d_2) = d_1 d_2/\gcd(d_1, d_2) \mid n$. By CRT, $m \equiv 0 \pmod{d_1},\, m \equiv -2 \pmod{d_2}$ is solvable iff $\gcd(d_1, d_2) \mid 2$, yielding $n/L = n\gcd(d_1, d_2)/(d_1 d_2)$ solutions in $\{1,\dots,n\}$ (and $0$ otherwise). Cancelling $n$ and $d_1 d_2$ and grouping by $j = d_1 d_2 \mid n$ via the bijection $k = d_2 r \leftrightarrow r \mid (n/j)$ yields $c = \tau * b$ for all $n \ge 1$, where $b(j) = \sum_{d_1 d_2 = j,\, \gcd(d_1, d_2) \mid 2} \mu(d_1)\mu(d_2)\gcd(d_1, d_2)$. Airtight.
- **Section 3 (L39–66, Multiplicativity & prime powers):**
  - *Lemma (multiplicativity of $b$):* $b(1) = 1$; for $\gcd(u, v) = 1$, unique factorization $d_1 = d_1'd_1'', d_2 = d_2'd_2''$ makes $g' = \gcd(d_1', d_2') \mid u$ and $g'' = \gcd(d_1'', d_2'') \mid v$ coprime, so $g' g'' \mid 2 \iff (g' \mid 2 \text{ and } g'' \mid 2)$, factoring $b(uv) = b(u)b(v)$. Thus $c = \tau * b$ is multiplicative.
  - *Odd prime $p$:* $b(1) = 1, b(p) = -2, b(p^e) = 0$ ($e \ge 2$, since $\gcd(p, p) = p \nmid 2$ and $\mu(p^r) = 0$ for $r \ge 2$), giving $c(p^e) = (e+1) - 2e = -(e-1) = (-1)^p(e-1)$ for all $e \ge 1$.
  - *Prime $p = 2$:* $b(1) = 1, b(2) = -2, b(4) = \mu(2)^2 \cdot 2 = 2, b(2^e) = 0$ ($e \ge 3$), giving $c(2) = 2 - 2 = 0 = (-1)^2(1-1)$ and $c(2^e) = (e+1) - 2e + 2(e-1) = e - 1 = (-1)^2(e-1)$ for $e \ge 2$.
  - Proves Schulte's conjecture for all $n \ge 1$. Airtight.
- **Section 4 (L69–83, Kotesovec & Oudra):**
  - Comparing prime powers ($e_i - 1 \ge 0$) gives $|c(n)| = \prod_i (e_i - 1) = \mathrm{A361430}(n)$ for all $n \ge 1$ (including $n = 1$).
  - For $g = (\mu \cdot \tau) * \tau$, multiplicativity and $g(p^e) = (e+1) - 2e = -(e-1)$ give $g(n) = c(n) = 0$ when $n$ is non-powerful, and for powerful $n$ (including $n = 1$), $g(n) = (-1)^{\omega(n)}\prod(e_p - 1)$ vs $c(n) = (-1)^{\omega_{\text{odd}}(n)}\prod(e_p - 1)$. Whether $n$ is odd ($\omega = \omega_{\text{odd}}$, $(-1)^{n+1} = 1$) or even ($\omega = \omega_{\text{odd}} + 1$, $(-1)^{n+1} = -1$), $(-1)^{n+1} g(n) = c(n)$ holds for all $n \ge 1$. Airtight.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A361430/notes/check-check-1.py` -> exit `0`, `PASS` (pure Python `int`, zero floats; verified primary matrix definition against OEIS `A298826` `%S` $n=1..108$ and `A361430` `%S` $n=1..87$, CRT convolution $c = \tau * b$ and $b = \mathrm{A306653}$, and Schulte/Kotesovec/Oudra identities through $n = 150$ primary and $n = 2000$ mutual).
- **Gate 2 novelty receipts:** All three clear (`watch-1` `#893`, `watch-5` `#891`, `watch-6` `#887`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).
