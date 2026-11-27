# Blind Audit: `targets/oeis-A101035/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/oeis-A101035/TARGET.md`, `targets/oeis-A101035/PROOF.md`, `targets/oeis-A101035/notes/check-check-3.md`, `targets/oeis-A101035/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON for `A101035` (`rev. 37`, `2022-12-06`, offset `1,2`) and `A018804` (`rev. 270`, `2026-10-29`, offset `1,2`), plus `watch/snapshots/zenodo-23112421-oeis-ids.md` and `zenodo-23114921-oeis-ids.md` (`0` hits in both).

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against live OEIS JSON:
- **OEIS `A101035`** (`rev. 37`, offset `1,2`):
  - **Name (`%N`):** `Dirichlet inverse of the gcd-sum function (A018804).`
  - **Data (`a(1)..a(72)`):** `1,-3,-5,1,-9,15,-13,...,4` (all 72 terms match `TARGET.md` L22 verbatim).
  - **Conjecture (`%F`, `_Benedict W. J. Irwin_`, Jul 26 2017):** `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))).`
- **OEIS `A018804`** (`rev. 270`, offset `1,2`): `Pillai's arithmetical function: Sum_{k=1..n} gcd(k, n).`

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

Audited all 33 lines of `PROOF.md`:
1. **Step 1 (Dirichlet factorization, L13–23):**
   - Grouping $j \in \{1,\dots,m\}$ by $d = \gcd(j,m)$ yields $g(m) = \sum_{d \mid m} d \varphi(m/d) = (\mathrm{id} * \varphi)(m) = (\mathrm{id} * \mathrm{id} * \mu)(m)$ since $\varphi * 1 = \mathrm{id}$.
   - Direct check $(\mathrm{id} * (\mathrm{id}\cdot\mu))(m) = m \sum_{d \mid m}\mu(m/d) = m\varepsilon(m) = \varepsilon(m)$ proves $\mathrm{id}^{-1} = \mathrm{id}\cdot\mu$; together with $\mu^{-1} = 1$, commutativity and associativity of Dirichlet convolution give $a = g^{-1} = (\mathrm{id}\cdot\mu)*(\mathrm{id}\cdot\mu)*1$, i.e., $a(m) = \sum_{nkr=m} n\mu(n)\,k\mu(k)$ for all $m \ge 1$. Exact.
2. **Step 2 (LGF coefficient extraction, L25–33):**
   - In $\mathbb{Q}[[x]]$, $\log(1/(1 - x^{nk})) = \sum_{r=1}^\infty x^{nkr}/r \in x^{nk}\mathbb{Q}[[x]]$, and for any $M \ge 1$ only finitely many $(n, k) \in \mathbb{Z}_{\ge 1}^2$ satisfy $nk \le M$, so the double sum converges $x$-adically in $\mathbb{Q}[[x]]$.
   - Collecting $[x^m]$ ($m \ge 1$) yields $\sum_{nkr=m} \mu(n)\mu(k)/r = \frac{1}{m}\sum_{nkr=m} n\mu(n)\,k\mu(k) = a(m)/m$, proving $\sum_{n,k\ge 1} \mu(n)\mu(k)\log(1/(1-x^{nk})) = \sum_{m=1}^\infty a(m) x^m/m$ identically in $\mathbb{Q}[[x]]$. Exact.

Zero gaps, zero edge-case defects.

---

## 3. Independent Verification & Novelty Status

- Re-ran `.venv/bin/python -u targets/oeis-A101035/notes/check-check-3.py` (pure `int`/`Fraction`, zero floats): exit code `0`, raw `PASS` (verified Pillai's $g$, Dirichlet inverse $a$, all 72 OEIS data terms, multiplicative prime-power formula, Step 1 convolution, and LGF coefficients through $x^{120}$).
- Checked `watch/snapshots/zenodo-23112421-oeis-ids.md` and `zenodo-23114921-oeis-ids.md`: `0` hits.
- Gate 2 novelty PASS receipts present from `watch-1` (`#928`), `watch-5` (`#912`), and `watch-6` (`#925`).

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).
