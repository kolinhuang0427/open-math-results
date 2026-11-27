# Blind Audit Report: `oeis-A186997`

- **Auditor:** `audit-3` (blind Pro audit; author `notes/` and `verify.py` not read)
- **Audited at (UTC):** `2026-11-27T10:19Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A186997` (`https://oeis.org/search?q=id:A186997&fmt=json`, rev. `85`, `2026-08-30T09:47:33-04:00`, offset `0,3`), plus verified `0` matches in `watch/snapshots/zenodo-23112421-oeis-ids.md`.
- `targets/oeis-A186997/TARGET.md`
- `targets/oeis-A186997/PROOF.md`
- `targets/oeis-A186997/notes/check-check-3.md` and `targets/oeis-A186997/notes/check-check-3.py`
- Confirmed Gate 2 PASS receipts from `watch-1` (`#666`), `watch-5` (`#664`), and `watch-6` (`#660`), with no `CONTESTED.md`.

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Fidelity Audit (**PASS**)

- Live OEIS `A186997` (rev. `85`, offset `0,3`) matches `TARGET.md` and `PROOF.md` verbatim:
  - **NAME:** `G.f. satisfies: A(x) = 1 + x*A(x)^3 + x^2*A(x)^4.`
  - **COMMENTS (_Peter Bala_, Aug 02 2016):**
    `Conjectures (both checked up to n = 100):`
    `2-adic valuation of a(2*n+1) = 2-adic valuation of Catalan(2*n+1) (= 2-adic valuation of Catalan(n));`
    `2-adic valuation of a(2*n) = 3 + 2-adic valuation of Catalan(n-2) for n >= 2, where Catalan(n) = A000108(n).`
- Proof starts directly from the primary `NAME` functional equation $A(x) = 1 + x A(x)^3 + x^2 A(x)^4$ with offset $0$, and proves both conjectures on their exact quantified domains ($m \ge 0$ for odd indices $2m+1$; $m \ge 2$ for even indices $2m$).

---

## 3. Line-by-Line Mathematical Audit (**PASS**)

1. **Step 1 (Lagrange Inversion, L16–33) — PASS:** $A(x) \in \mathbb{Z}[[x]]$ is uniquely determined with $a(0)=1$. Setting $W(x) := x A(x^2)$ yields $W(x)(1 - W(x)^2) = x(1 + W(x)^4)$, so Lagrange inversion with $\phi(w) = (1+w^4)/(1-w^2)$ gives $(2k+1)a(k) = [z^k]\bigl((1-z) + \frac{2z}{1-z}\bigr)^{2k+1} = \sum_{j=0}^k t_j$ where $t_j = (-1)^{k-j} 2^j \binom{2k+1}{j}\binom{2k+1-2j}{k-j}$ (for $j > k$, $(2z)^j(1-z)^{2k+1-2j} \in z^j\mathbb{Z}[[z]]$ has zero $[z^k]$-coefficient; for $0 \le j \le k$, $2k+1-2j \ge 1$ and $k-j \le 2k+1-2j$). Since $2k+1$ is odd, $v_2(a(k)) = v_2(\sum_{j=0}^k t_j)$.
2. **Step 2 (Legendre/Kummer Valuations, L35–43) — PASS:** $v_2(C_m) = s_2(m) - v_2(m+1) = s_2(m+1) - 1$ for all $m \ge 0$; $v_2\binom{2k+1-2j}{k-j} = s_2(k+1-j) - 1$ for $0 \le j \le k$; hence $v_2(t_j) = j + v_2\binom{2k+1}{j} + s_2(k+1-j) - 1$, and $s_2(k+1-j) \ge s_2(k+1) - s_2(j)$.
3. **Step 3 (Odd $k = 2m+1$, $m \ge 0$, L45–56) — PASS:** $v_2(C_{2m+1}) = s_2(2m+2)-1 = s_2(m+1)-1 = v_2(C_m) = v_2(t_0)$. For $j = 1$, $|t_1| = (2k+1)(k+1)C_k$ has $v_2(t_1) = 1 + v_2(m+1) + v_2(C_k) > v_2(t_0)$. For $2 \le j \le k$ (vacuous at $m = 0$), $v_2(t_j) \ge v_2(C_m) + v_2(j!) \ge v_2(C_m) + 1 > v_2(t_0)$. Ultrametric domination gives $v_2(a(2m+1)) = v_2(C_{2m+1}) = v_2(C_m)$.
4. **Step 4 (Even $k = 2m$, $m \ge 2$, L58–80) — PASS:**
   - $t_0 + t_1 = \binom{2k+1}{k} - (k+1)\binom{2k+1}{k} = -k\binom{2k+1}{k}$, with $v_2(t_0 + t_1) = 1 + v_2(m) + s_2(m) = 3 + v_2(C_{m-2}) = s_2(m) + r - 1$ where $r := v_2(m) + 2 \ge 2$.
   - **Case A ($2 \le j \le 2^r - 1$):** Since $2^r \mid 4m$, $2^r - 1 \le 4m - 1$ and $4m - 1$ ends in $r$ binary ones, so $v_2\binom{4m-1}{i-1} = 0$ and $v_2\binom{4m}{i} = r - v_2(i)$ for all $1 \le i \le 2^r - 1$. Both $j$ and $j-1$ lie in $\{1, \dots, 2^r - 1\}$ with opposite parities, so Pascal's identity gives $v_2\binom{4m+1}{j} = r - \max(v_2(j), v_2(j-1))$. Verification of $j - s_2(j) - v \ge 0$ for all $j \ge 2$ (checking $j \in \{2,3\}$, $j = 2^v q$ even, and $j = 2^v q + 1$ odd, including $v=1 \implies q \ge 3$ and $v \ge 2 \implies 2^v - 1 \ge v + 1$) is completely rigorous and gives $v_2(t_j) \ge s_2(m) + r > v_2(t_0 + t_1)$.
   - **Case B ($j \ge 2^r$):** Writing $j = 2^b + d$ with $b \ge r \ge 2$ and $0 \le d < 2^b$ gives $j - s_2(j) \ge 2^b - 1 \ge 2^r - 1 \ge r + 1 > r - 1$, so $v_2(t_j) \ge s_2(m) + r + 1 > v_2(t_0 + t_1)$.
   - Ultrametric domination gives $v_2(a(2m)) = v_2(t_0 + t_1) = 3 + v_2(C_{m-2})$ for all $m \ge 2$.

---

## 4. Independent Mechanical Verification (**PASS**)

Re-executed `.venv/bin/python targets/oeis-A186997/notes/check-check-3.py` (exit code `0`, raw output):
```text
[1/4] Computing A(x) directly from A(x) = 1 + x*A^3 + x^2*A^4 up to k=250...
[2/4] Verifying Step 1 Lagrange inversion sum (2k+1)*a(k) = sum_j t_j and W(x) identity...
[3/4] Verifying Step 3 (odd k = 2m+1) & Step 4 (even k = 2m) ultrametric domination...
[4/4] Verifying symbolic power series identity W(x)*(1 - W(x)^2) = x*(1 + W(x)^4) mod x^60...
PASS
```

---

## 5. Handoff

Handed off directly to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`), instructing them to mention `@coordinator` on PASS with label `"written proof, internally audited"`, verifier command `.venv/bin/python targets/oeis-A186997/notes/check-check-3.py`, and paths `targets/oeis-A186997/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.
