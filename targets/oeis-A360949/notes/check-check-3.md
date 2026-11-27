# Independent Check Report: targets/oeis-A360949/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary sources checked:**
  - Live OEIS JSON API for `A360949` (revision `15`, timestamp `2023-03-05T12:37:19-05:00`, offset `0,2`).
  - Live OEIS JSON API for `A161674` (revision `21`, timestamp `2021-01-30T04:23:15-05:00`, offset `1,3`).
- **Exact statement match:**
  - `A360949` Name: `G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.`
  - `A360949` Data: `1,2,8,50,376,3124,27804,260496,2539616,25556330,263922884,2785341186,29948035032,327315887046,3630399545244,40813503158790,464662514679168,5354222585965310,62419468527625408,736098528973804246,8781173950238637928,105987886325647341056`
  - `A360949` Comment: `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the Thue-Morse sequence.`
  - `A161674` Name: `Positions n such that A010060(n) + A010060(n+2) = 1.`
  - `A161674` Data starts: `0,1,4,5,6,7,8,9,12,13,16,17,20,21,22,23,24,25,...`
  - `TARGET.md` and `PROOF.md` match the live OEIS definitions, offsets (`0`-indexed `A360949` and `A010060`; `1`-indexed `A161674`), and conjecture statement verbatim with zero drift.

## 2. Independent Mechanical & Mathematical Check

- Independently wrote `targets/oeis-A360949/notes/check-check-3.py` (without reading `verify.py` or `notes/explore.py`), verifying:
  1. Exact rational series `A(x) in Q[[x]]` (`n = 0..35`) solving `1 = Sum_{n>=0} (-x/2)^n (A(x)^n + (-1)^n)^n`: confirms `a(0..21)` match OEIS `A360949` verbatim and `B(x) = (A(x)-1)/2` lies in `x Z[[x]]` for `n = 0..35` (consistent with the `PROOF.md` Step 1 term-by-term valuation argument).
  2. Exact `F_2[[x]]` and `F_2[[y]]` (`y = x^2`) identities from `PROOF.md` Step 2:
     - `(1 + x^2) B(x) == x + x^3 B(x)^2` over `F_2[[x]]`.
     - Even-part vanishing `B_0(y) == 0` (yielding `a(2k) == 0 (mod 4)` for `k >= 1`) and `y^2 C(y)^2 + (1 + y) C(y) + 1 == 0` where `B(x) = x C(x^2)` over `F_2[[x]]`.
  3. Exact `F_2[[y]]` identities from `PROOF.md` Step 3:
     - Thue-Morse `T(y) = sum_{n>=0} t_n y^n` satisfies `(1 + y)^3 T(y)^2 + (1 + y)^2 T(y) + y == 0` over `F_2[[y]]`.
     - `C_tilde(y) = sum_{m>=0} (t_m + t_{m+2}) y^m` satisfies `y^2 C_tilde(y)^2 + (1 + y) C_tilde(y) + 1 == 0` over `F_2[[y]]` and agrees identically with `C(y)` up to degree `80`.
     - `A161674(k)` (`1 <= k`, up to `m <= 104`) matches indices `m` where `t_m + t_{m+2} == 1`, and `a(n) mod 4` for `1 <= n <= 35` matches the conjecture verbatim.

- **Command run:**
```bash
.venv/bin/python targets/oeis-A360949/notes/check-check-3.py
```

- **Raw output:**
```text
Step 1 & Data PASS: A360949 (n=0..35) and A161674 (m<=104) verified via exact Q[[x]] functional equation.
Steps 2 & 3 PASS: all F_2[[x]] / F_2[[y]] identities and C(y) == C_tilde(y) verified up to deg 80.
PASS
```
