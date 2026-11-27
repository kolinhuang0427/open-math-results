# Check Report — `cooper-2302.00757-conj11.2`

- Checker: `check-1`
- Checked UTC: `2026-11-27T00:11:06Z`
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source: `arXiv:2302.00757v2` (updated `2024-05-08T00:29:10Z`), local cache `tools/.arxiv_cache/eprint/2302.00757/main.tex`
  - Section 5 (lines 1611–1635): modular parametrization $(X, Z)$ on $\Gamma_0(11)$ via $\eta(\tau)\eta(11\tau)$, four-term recurrence for $T(n) = T_{11}(n)$, and first 11 terms `1, 4, 28, 268, 3004, 36784, 476476, 6418192, 88986172, 1261473136, 18200713168`.
  - Section 11.1 (lines 2557–2567): Conjecture 11.2 (`\label{c11}`), claiming $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod{3^2}$ and $T_{11}(5n) \equiv T_{11}(n) \pmod{5^2} \iff 5 \mid n$, with the paper reporting counts $c(3)=333$ and $c(5)=200$ for $0 \le n < 1000$ (or equivalently checking $0 \le n \le 1000$).
- Comparison against `TARGET.md` and `PROOF.md`: exact match with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Verification

- Verifier script: `targets/cooper-2302.00757-conj11.2/notes/check-check-1.py`
  - Independently implements Cooper's four-term recurrence for $T_{11}(n)$ in exact integers and verifies the first 11 terms and both congruences directly for $0 \le n \le 1000$, including $c(3)=333$ and $c(5)=200$.
  - Verifies the exact $q$-series identity $U_1 = E_{2,11} + \frac{8}{5} V_1$ and $Z(X_1) = U_1 \pmod{9}, \pmod{25}$ where $Z(X_1) = \sum T_{11}(n) q^n$.
  - Verifies $\Gamma_0(33)$ weight-30 form $G_3 \equiv 0 \pmod{9}$ up to $q^{130}$ (past Sturm bound $120$) and Step 2.4 mod-9 congruence.
  - Verifies $\Gamma_0(55)$ weight-10 form $G_{5,\text{luc}} \equiv 0 \pmod{5}$ up to $q^{80}$ (past Sturm bound $60$) and weight-66 form $G_5 \equiv 0 \pmod{25}$ up to $q^{405}$ (past Sturm bound $396$).
- Command:
  ```bash
  .venv/bin/python targets/cooper-2302.00757-conj11.2/notes/check-check-1.py
  ```
- Raw output (exit code `0`):
  ```text
  T11 recurrence, Cooper first 11 terms, & direct checks (0<=n<=1000): OK
  q-series U1, V1, E_{2,11} identity, & Z(X1)==U1 mod 9, 25: OK
  Gamma_0(33) G3 == 0 mod 9 up to q^130 (Sturm 120) & Step 2.4: OK
  Gamma_0(55) G_{5,luc} == 0 mod 5 up to q^80 (Sturm 60) & G5 == 0 mod 25 up to q^405 (Sturm 396): OK
  PASS
  ```
