# Blind Audit: `targets/oeis-A188458/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/oeis-A188458/TARGET.md`, `targets/oeis-A188458/PROOF.md`, `targets/oeis-A188458/notes/check-check-3.md`, `targets/oeis-A188458/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON `https://oeis.org/search?q=id:A188458&fmt=json` (`rev. 54`, `2015-10-16T02:19:23-04:00`, offset `0,3`), `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits), and `watch/snapshots/zenodo-23114921-oeis-ids.md` (`0` hits).

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against live OEIS **A188458** (`rev. 54`, offset `0,3`):
- **Name (`%N`):** `Expansion of e.g.f. exp(x)/cosh(2*x).`
- **Data (`a(0)..a(20)`):** `1,1,-3,-11,57,361,-2763,-24611,250737,...,274613643571568682777` (all 21 terms match `TARGET.md` L22 verbatim).
- **Conjecture (`%F`, `_Sergei N. Gladkovskii_`, Nov 12 2013):** `G.f.: conjecture T(0)/(1-x), where T(k) = 1 - 4*x^2*(k+1)^2/(4*x^2*(k+1)^2 + (1-x)^2/T(k+1) ); (continued fraction).`

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

Audited every line (`L1–50`) of `PROOF.md`:
1. **Binomial transform reduction (`Lemma 1`, L7–16):**
   - Multiplying $\mathrm{sech}(2t) = \sum_{m=0}^\infty E_{2m} 2^{2m} t^{2m}/(2m)!$ ($E_{2m} \in \mathbb{Z}$) by $e^t$ gives $a(n) = \sum_{m=0}^{\lfloor n/2 \rfloor} \binom{n}{2m} 2^{2m} E_{2m} \in \mathbb{Z}$.
   - Expanding $(1-x)^{-(2m+1)} = \sum_{r=0}^\infty \binom{2m+r}{2m} x^r$ in $\mathbb{Z}[[x]]$ with $n = 2m + r$ yields $F(x) = \frac{1}{1-x} S\!\left(\frac{2x}{1-x}\right)$ where $S(u) = \sum_{m=0}^\infty E_{2m} u^{2m} \in \mathbb{Z}[[u^2]]$ and $u = \frac{2x}{1-x} \in x\mathbb{Z}[[x]]$. Exact.
2. **Self-contained formal-Laplace continued fraction for $S(u)$ (`Lemma 2`, L20–37):**
   - Formal Laplace operator $\mathcal{L}(\sum g_n t^n/n!) = \sum g_n u^n$ satisfies $\mathcal{L}(g')(u) = (\mathcal{L}(g)(u) - g(0))/u$ and $S(u) = \mathcal{L}(\mathrm{sech})(u)$.
   - For $f_k(t) = \tanh^k(t)\mathrm{sech}(t)$, parity and $\tanh(t) = t + O(t^3)$, $\mathrm{sech}(t) = 1 + O(t^2)$ give $J_k(u) = \mathcal{L}(f_k)(u) = k! u^k(1 + O(u^2))$ and $f_k(0) = \delta_{k,0}$; hence $T_k(u) := \frac{J_k(u)}{k u J_{k-1}(u)} = 1 + O(u^2) \in \mathbb{Q}[[u]]^\times$ ($k \ge 1$) and $T_0(u) := J_0(u) = S(u)$.
   - $k = 0$: $f_0' = -f_1$, $f_0(0)=1 \implies (J_0-1)/u = -J_1 \implies T_0(u) = (1 + u^2 T_1(u))^{-1}$.
   - $k \ge 1$: $f_k' = k f_{k-1} - (k+1) f_{k+1}$, $f_k(0)=0 \implies J_k/u = k J_{k-1} - (k+1) J_{k+1} \implies 1/T_k(u) = 1 + (k+1)^2 u^2 T_{k+1}(u)$. Exact.
3. **Equivalence with Gladkovskii's CF and $x$-adic convergence (`Theorem`, L41–50):**
   - Substituting $u = \frac{2x}{1-x}$ into $T_k(u)$ gives $\widetilde{T}_k(x) = 1 + O(x^2) \in \mathbb{Q}[[x]]^\times$, $F(x) = \widetilde{T}_0(x)/(1-x)$, and with $A = 4x^2(k+1)^2$, $B = (1-x)^2$ ($u^2 = A/B$, $A + B/\widetilde{T}_{k+1} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$), $1 - A/(A + B/\widetilde{T}_{k+1}) = (1 + (k+1)^2 u^2 \widetilde{T}_{k+1})^{-1} = \widetilde{T}_k(x)$. Exact.
   - For $\Phi_k(t) = (1 + (k+1)^2 u^2 t)^{-1}$, $\Phi_k(t_1) - \Phi_k(t_2) = -(k+1)^2 u^2(t_1-t_2)/((1+(k+1)^2 u^2 t_1)(1+(k+1)^2 u^2 t_2))$ raises $\mathrm{ord}_x$ by at least $2$, giving $\mathrm{ord}_x(\widetilde{T}^{(K)}(0) - \widetilde{T}_0(x)) \ge 2K + 3$ for any seed $1 + O(x) \in \mathbb{Q}[[x]]^\times$ and $\ge 2K + 4$ for $1 + O(x^2)$ (e.g. $t_{K+1}^{(K)} = 1$, where the convergents even lie in $\mathbb{Z}[[x]]$). Dividing by $1-x$ gives $\widetilde{T}^{(K)}(0)/(1-x) \to F(x)$ $x$-adically. *(Minor note: L43 writes "in $\mathbb{Z}[[x]]$" while allowing seeds in $\mathbb{Q}[[x]]^\times$; L50 accurately writes "in $\mathbb{Q}[[x]]$", and for the standard seed $1$ all convergents indeed lie in $\mathbb{Z}[[x]]$.)*

---

## 3. Independent Verification & Novelty Status

- Re-ran `.venv/bin/python -u targets/oeis-A188458/notes/check-check-3.py` (pure `int`/`Fraction`, zero floats): exit code `0`, raw `PASS`.
- Checked `watch/snapshots/zenodo-23112421-oeis-ids.md` and `zenodo-23114921-oeis-ids.md`: `0` hits.
- Gate 2 novelty PASS receipts present from `watch-1` (`#928`), `watch-5` (`#912`), and `watch-6` (`#925`).

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).
