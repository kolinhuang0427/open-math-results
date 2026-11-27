# Adversarial Audit Report (`audit-1`): `targets/oeis-A127276/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A127276` (rev. 33, Nov 25 2026 `15:43:26`) — R. J. Mathar's Dec 11, 2010 closed form $a(n) = 2^n - n(n+1)2^{n-2}$ and g.f. $-(4x-1)(x-1)/(2x-1)^3$ for the Hankel transform of `A127275` (rev. 18)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, live OEIS `A127276` rev. 33, `A127275` rev. 18, and `A178987` rev. 52 (`fmt=text`), `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A127276` (`#33 Nov 25 2026 15:43:26`):**
  - `%O`: `0,3`; `%S/%T/%U` ($n = 0..25$) match `TARGET.md` and `notes/check-check-2.py` verbatim.
  - `%N`: `Hankel transform of A127275.` — verbatim match.
  - `%F`: `Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2). - _R. J. Mathar_, Dec 11 2010` — verbatim match.
- **Live OEIS `A127275` (`#18 Jan 16 2023 11:15:29`):**
  - `%N`: `Expansion of (sqrt(1-4x)-x)/(1-4x).`; `%O`: `0,3`; `%S/%T/%U` ($n = 0..25$) match `notes/check-check-2.py` verbatim.
- **Snapshot cross-check:** `A127276` and `A127275` have `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.
- **Gate 2 novelty receipts:** Present from `watch-1` (`#1096`), `watch-5` (`#1084`), `watch-6` (`#1089`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Section 1 (Rank-2 decomposition, L18–27):**
  - $\frac{\sqrt{1-4x}-x}{1-4x} = (1-4x)^{-1/2} - \frac{x}{1-4x} = \sum_{m=0}^\infty \binom{2m}{m} x^m - \sum_{m=1}^\infty 4^{m-1} x^m$, giving $b_0 = 1$ and $b_m = \binom{2m}{m} - 4^{m-1}$ for all $m \ge 1$.
  - With $C_n = \bigl(\binom{2(i+j)}{i+j}\bigr)_{0 \le i,j \le n}$, $v = (1, 4, \dots, 4^n)^T$, $e_0 = (1, 0, \dots, 0)^T$: entrywise inspection confirms $M_n = C_n - \frac{1}{4} v v^T + \frac{1}{4} e_0 e_0^T = C_n + U V^T$ for every $n \ge 0$ (including $(0,0)$ where $-\frac{1}{4} + \frac{1}{4} = 0$).
- **Section 2 (Laurent–Chebyshev diagonalization of $C_n$, L31–60):**
  - $P_0(t)=1$, $P_1(t)=t-2$, $P_2(t)=(t-2)P_1(t)-2P_0(t)=t^2-4t+2$, $P_k(t)=(t-2)P_{k-1}(t)-P_{k-2}(t)$ ($k \ge 3$) are monic in $\mathbb{Z}[t]$.
  - Lemma 1: with $t(z) = z + 2 + z^{-1} = (1+z)^2/z \in \mathbb{Z}[z, z^{-1}]$, $[z^0](t(z)^m) = [z^m](1+z)^{2m} = \binom{2m}{m}$ ($m \ge 0$), $P_k(t(z)) = z^k + z^{-k}$ ($k \ge 1$, verified by induction from $k = 1, 2$), and substituting $z = 1$ ($t = 4$) and $z = -1$ ($t = 0$) gives $P_0(4)=P_0(0)=1$, $P_k(4)=2$, $P_k(0)=2(-1)^k$ ($k \ge 1$).
  - For unit lower-triangular $P = (p_{k,i})$, $(P C_n P^T)_{k,\ell} = [z^0](P_k(t(z)) P_\ell(t(z))) = d_k \delta_{k,\ell}$ with $d_0 = 1$, $d_k = 2$ ($k \ge 1$). Hence $C_n$ is invertible, $\det(C_n) = 2^n$, and $C_n^{-1} = P^T D^{-1} P$.
- **Section 3 (Weinstein–Aronszajn determinant, L63–78):**
  - $\det(M_n) = \det(C_n)\det(I_2 + V^T C_n^{-1} U) = 2^n \det(I_2 + V^T C_n^{-1} U)$.
  - Using $(Pv)_k = P_k(4)$ and $(Pe_0)_k = P_k(0)$: $v^T C_n^{-1} v = e_0^T C_n^{-1} e_0 = 1 + \sum_{k=1}^n \frac{4}{2} = 2n + 1$, and $v^T C_n^{-1} e_0 = e_0^T C_n^{-1} v = 1 + 2\sum_{k=1}^n (-1)^k = (-1)^n$ (valid for all $n \ge 0$, even and odd).
  - $\det\begin{pmatrix} 1 - \frac{2n+1}{4} & \frac{(-1)^n}{4} \\ -\frac{(-1)^n}{4} & 1 + \frac{2n+1}{4} \end{pmatrix} = 1 - \frac{(2n+1)^2 - 1}{16} = 1 - \frac{n(n+1)}{4}$.
  - Multiplying by $2^n$ yields $a(n) = 2^n - n(n+1)2^{n-2}$ for all $n \ge 0$.
- **Section 4 (Ordinary generating function, L82–87):**
  - Using $\sum_{n=0}^\infty \binom{n+1}{2} y^n = \frac{y}{(1-y)^3}$ at $y = 2x$ and $n(n+1)2^{n-2} = \frac{1}{2}\binom{n+1}{2} 2^n$ gives $\sum_{n=0}^\infty a(n)x^n = \frac{1}{1-2x} - \frac{x}{(1-2x)^3} = \frac{1 - 5x + 4x^2}{(1-2x)^3} = -\frac{(4x-1)(x-1)}{(2x-1)^3}$.

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A127276/notes/check-check-2.py`:
- Exit code `0`, output `PASS` (zero floats; pure Python `int`, `Fraction`, and exact integer Bareiss determinant).
- Independently verified `A127275` ($m = 0..50$, all 26 live OEIS terms), Lemma 1 and $P C_n P^T = \mathrm{diag}(1,2,\dots,2)$ ($n \le 25$), rank-2 decomposition, $C_n^{-1}$, Weinstein–Aronszajn, direct Bareiss $\det(M_n)$ against all 26 live OEIS `A127276` terms ($n = 0..25$), and the exact g.f. modulo $x^{41}$.
