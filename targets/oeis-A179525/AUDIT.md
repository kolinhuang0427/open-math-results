# Adversarial Audit Report (`audit-1`): `targets/oeis-A179525/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A179525` (rev. 74, `2026-04-28T18:58:30-04:00`) — Sergei N. Gladkovskii's May 13, 2013 continued fraction conjecture and Peter Bala's May 16, 2017 even-product generating function conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, live OEIS `A179525` rev. 74 (`fmt=json`), `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A179525` (rev. 74, `2026-04-28T18:58:30-04:00`):**
  - `OFFSET`: `0,3`; first 26 `DATA` terms (`1, 1, 2, 5, 16, 61, ...`) match `TARGET.md` and `notes/check-check-2.py` verbatim.
  - `NAME`: `G.f.: Sum_{n>=0} Product_{k=1..n} ((1+x)^k - 1).` matches `PROOF.md` L5–6 verbatim.
  - Gladkovskii May 13, 2013 `FORMULA` entry (`G.f.: Q(0), where Q(k) = 1 - (1 - (1+x)^(2*k+1))/(1 - (1 - (1+x)^(2*k+2))/(1 - (1+x)^(2*k+2) - 1/Q(k+1))); (conjectured).`) matches `PROOF.md` Theorem 1 (L20–21) verbatim.
  - Bala May 16, 2017 `FORMULA` entry (`Conjectural g.f.: A(x) = Sum_{n >= 0} (1+x)^(2*n+1) * Product_{k = 1..2*n} (1 - (1+x)^k).`) matches `PROOF.md` Theorem 2 (L40–41) verbatim, and `TARGET.md` explicitly scopes out Bala's separate $q^{-n-1}$ line.
- **Snapshot cross-check:** `A179525` has `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.
- **Gate 2 novelty receipts:** Present from `watch-1`, `watch-5`, `watch-6` (`#948`, `#950`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Setup (L5–6):** With $q = 1+x \in \mathbb{Z}[[x]]$, $q^j - 1 \in x\mathbb{Z}[[x]]$ for all $j \ge 1$, so $\prod_{j=1}^n (q^{m+j}-1) \in x^n\mathbb{Z}[[x]]$ and every infinite series converges $x$-adically in $\mathbb{Z}[[x]]$. $Q(k) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ for all $k \ge 0$, with $Q(0) = A(x)$.
- **Section 1 — Lemma 1 & Theorem 1 (L8–36):**
  - Splitting $n = 0, 1$ and reindexing $n = m + 2$, $j = j' + 2$ yields $Q(k) = 1 + (q^{2k+1}-1) + (q^{2k+1}-1)(q^{2k+2}-1) Q(k+1)$ for all $k \ge 0$.
  - With $a = 1 - q^{2k+1}, b = 1 - q^{2k+2} \in x\mathbb{Z}[[x]]$ and any unit $g \in \mathbb{Z}[[x]]^\times$ (so $g(0) \in \mathbb{Z}^\times = \{\pm 1\}$): $D_2 = b - 1/g = (bg - 1)/g = -1/g(0) + O(x) \in \mathbb{Z}[[x]]^\times$, $D_1 = 1 - b/D_2 = 1/(1-bg) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$, and $1 - a/D_1 = 1 - a + abg = 1 + (q^{2k+1}-1) + (q^{2k+1}-1)(q^{2k+2}-1)g$. At $g = Q(k+1)$ this equals $Q(k)$ by Lemma 1.
  - Contraction: $T_k(g_1) - T_k(g_2) = (q^{2k+1}-1)(q^{2k+2}-1)(g_1 - g_2) \in x^2(g_1 - g_2)\mathbb{Z}[[x]]$. Iterating $k = K, \dots, 0$ gives $Q^{(K)}(0) - Q(0) \in x^{2K+2}\mathbb{Z}[[x]]$ for any unit seed $q_{K+1}^{(K)} \in \mathbb{Z}[[x]]^\times$, improving to $x^{2K+3}\mathbb{Z}[[x]]$ when $q_{K+1}^{(K)} = 1 + O(x)$ since $q_{K+1}^{(K)} - Q(K+1) \in x\mathbb{Z}[[x]]$. Thus $Q^{(K)}(0) \to A(x)$ $x$-adically in $\mathbb{Z}[[x]]$.
- **Section 2 — Theorem 2 (L38–46):**
  - For every $n \ge 0$, $\prod_{k=1}^{2n}(1 - q^k) = (-1)^{2n} P_{2n} = P_{2n}$, and $q^{2n+1} P_{2n} = P_{2n} + (q^{2n+1}-1)P_{2n} = P_{2n} + P_{2n+1}$.
  - Because $P_m \in x^m\mathbb{Z}[[x]]$, summing over $n \ge 0$ converges $x$-adically in $\mathbb{Z}[[x]]$ to $\sum_{m \ge 0} P_m = A(x)$.

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A179525/notes/check-check-2.py`:
- Exit code `0`, output `PASS` (pure Python `int` / `Fraction` arithmetic modulo $x^{36}$, zero floats).
- Independently verified all 26 live OEIS `A179525` terms, Lemma 1 (`k = 0..8`), Theorem 1 recurrence & truncation convergence ($K = 0..16$, both `1` and non-unit-constant-1 unit seeds), and Theorem 2 through $x^{35}$.
