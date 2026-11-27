# Adversarial Audit Report (`audit-1`): `targets/oeis-A162481/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A162481` (rev. 23, Oct 09 2025 `23:21:43`) — R. J. Mathar's Dec 11, 2011 4-term D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, live OEIS `A162481` rev. 23 (`fmt=text`), `watch/snapshots/**` (658 files)
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A162481` (`#23 Oct 09 2025 23:21:43`):**
  - `%O`: `0,2`; all 24 `DATA` terms ($n = 0..23$) match `notes/check-check-3.py` verbatim.
  - `%N`: `Expansion of (1/(1-x)^3)*c(x/(1-x)^3), c(x) the g.f. of A000108.` and `%F` (Catalan binomial sum, Gutkovskiy's algebraic equation, Manyama's convolution recurrence, Kotesovec's radical g.f., and Mathar's Dec 11, 2011 4-term recurrence `Conjecture:`) match `TARGET.md` and `PROOF.md` verbatim.
- **Snapshot cross-check & Gate 2:** `.venv/bin/python tools/novelty_grep.py A162481` returned `0 lines across 0/658 files`; Gate 2 PASS receipts from `watch-1` (`#1207`) and `watch-5` (`#1208`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Section 1 (Algebraic equation & radical identity, L15–21):**
  - Substituting $u = x/(1-x)^3 \in x\mathbb{Z}[[x]]$ and $c(u) = (1-x)^3 A(x)$ into $u c(u)^2 - c(u) + 1 = 0$ and $(1 - 2u c(u))^2 = 1 - 4u$ yields $x(1-x)^3 A(x)^2 - (1-x)^3 A(x) + 1 = 0$ and $(1 - 2x A(x))^2 = (1 - 7x + 3x^2 - x^3)/(1-x)^3$ identically in $\mathbb{Z}[[x]]$.
- **Section 2 (First-order ODE & coefficient extraction, L25–49):**
  - Setting $z(x) = 1 - 2x A(x) \in 1 + x\mathbb{Z}[[x]] \subseteq \mathbb{Z}[[x]]^\times$, $Q(x) = 1 - 7x + 3x^2 - x^3$, $R(x) = (1-x)^3$: differentiating $R z^2 = Q$ and eliminating $z^2 = Q/R$ yields $2 Q R z' = (Q' R - Q R') z$.
  - Substituting $z = 1 - 2x A$, $z' = -2A - 2x A'$ and cancelling $4(1-x)^2$ in $\mathbb{Q}[[x]]$ gives $x(1 - 8x + 10x^2 - 4x^3 + x^4) A'(x) + (1 - 6x + 14x^2 - 4x^3 + x^4) A(x) = 1 + 2x$.
  - Extracting $[x^n]$ for every $n \ge 2$ (using $\deg(1+2x) = 1 < 2$, and $a(k) = 0$ for $k < 0$ at $n = 2, 3$) yields Mathar's exact 4-term recurrence $(n+1)a(n) + 2(1-4n)a(n-1) + 2(5n-3)a(n-2) + 4(2-n)a(n-3) + (n-3)a(n-4) = 0$ for all $n \ge 4$ (and $n = 2, 3$).

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A162481/notes/check-check-3.py`:
- Exit code `0`, output `PASS` (zero floats; pure exact `int` and SymPy `QQ[x]`/`QQ[n]` arithmetic).
- Verified all 24 live OEIS `A162481` terms, Catalan binomial sum ($n \le 40$), quadratic equation to $x^{60}$, symbolic ODE and recurrence polynomials, and Mathar's 4-term recurrence for $n = 2..60$.
