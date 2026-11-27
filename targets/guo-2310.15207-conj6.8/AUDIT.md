# Blind Audit: `targets/guo-2310.15207-conj6.8/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (`written proof, internally audited`)
- **Audited Files:** `targets/guo-2310.15207-conj6.8/TARGET.md`, `targets/guo-2310.15207-conj6.8/PROOF.md`, `targets/guo-2310.15207-conj6.8/notes/check-check-2.md`, `targets/guo-2310.15207-conj6.8/notes/check-check-2.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Source Checked:** `tools/.arxiv_cache/eprint/2310.15207v1_dir/main.tex` (Victor J. W. Guo, *"Dwork-type $q$-congruences through the $q$-Lucas theorem"*, `arXiv:2310.15207v1`, 2023-10-23; `0` `\iffalse` blocks; `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}`).

---

## 1. Primary-Source & Statement Fidelity

- Verified Section 6 (`Open problems and concluding remarks`, `main.tex` L672) numbering: `Conjecture 6.1` (`conj:1`, L692) through **`Conjecture 6.8`** (`\label{conj:8}`, L812–818).
- Verified verbatim match between `main.tex` L812–818 and `TARGET.md` L18–21, including all notation from `main.tex` Section 1 (L67, L95–106): $(a;q)_k$, $[n] = (1-q^n)/(1-q)$, $(x)_k$, $\Phi_n(q)$, and Guo's definition of congruence modulo $\Phi_n(q)^2$ in $\mathbb{Z}[q]$ (which, by Gauss's Lemma since $\Phi_n(q)$ is monic and irreducible in $\mathbb{Z}[q]$, is equivalent to congruence modulo $\Phi_n(q)^2$ in $\mathbb{Q}[q]_{(\Phi_n(q))}$).
- Verified the $n = 1$ boundary remark (`TARGET.md` L25, `PROOF.md` L5): at $n = 1$, $\Phi_1(q) = q - 1$, $m = 1$ gives $1 \equiv 1$, whereas $m = 2$ gives $1 - \frac{(1+q+q^2+q^3+q^4)q}{(1+q)^3} \equiv \frac{3}{8} - \frac{15}{16}(q-1) \not\equiv \frac{3}{8} \pmod{(q-1)^2}$. `PROOF.md` explicitly documents $n = 1$ and proves Conjecture 6.8 unconditionally for all $m \ge 1$ and all odd integers $n \ge 3$.

---

## 2. Adversarial Line-by-Line Proof Audit (`PROOF.md`)

1. **Section 1 (Block decomposition & $\Phi_n$-adic vanishing):**
   - For odd $n \ge 3$ and $N = (n-1)/2 \ge 1$, $1 - q$ is coprime to $\Phi_n(q)$, so $v_{\Phi_n}([4k+1]) \ge 0$.
   - Exact counting of $\Phi_n(q)$-divisible factors in $(q; q^2)_{rn+s}$ ($r$ factors for $0 \le s \le N$; $r+1$ factors for $N+1 \le s \le n-1$) and $(q^2; q^2)_{rn+s}$ ($r$ factors for all $0 \le s \le n-1$, since $\gcd(2, n) = 1$) proves $v_{\Phi_n}(A_{rn+s}) \ge 3$ for $s > N$ and $v_{\Phi_n}(A_{rn+s}) \ge 0$ for $0 \le s \le N$, reducing Conjecture 6.8 to the per-block congruence Eq. (1). **Verified.**
2. **Section 2 (Linearization modulo $\Phi_n(q)^2$):**
   - With $z = 1 - q^n = (1-q)[n]$ ($v_{\Phi_n}(z) = 1$, $z^2 \equiv 0 \pmod{\Phi_n^2}$):
     - Item 1: cancelling the common $z$ factor before reducing modulo $\Phi_n^2$ yields $\bigl(\frac{(q^n; q^{2n})_r}{(q^{2n}; q^{2n})_r}\bigr)^3 \equiv \frac{(1/2)_r^3}{r!^3}(1 + \frac{3r}{2}z) \pmod{\Phi_n^2}$ (including $r = 0$). **Verified.**
     - Item 2: $P_r(q) \equiv 1 \pmod{\Phi_n}$ by residue-class bijection modulo $n$ ($\gcd(2, n) = 1$), and because $v_{\Phi_n}(z) = 1$ with $\Phi_n$ irreducible, $P_r(q)^3 \equiv 1 + C_r z \pmod{\Phi_n^2}$ for a polynomial $C_r \in \mathbb{Q}[q]$ independent of $s$. **Verified.**
     - Item 3: $s$-tail factors for $0 \le i < s \le N$ have exponents in $[1, n-1]$ (invertible mod $\Phi_n^2$), expanding cleanly to $6rz\sum_{i=0}^{s-1}\bigl(\frac{q^{2i+1}}{1-q^{2i+1}} - \frac{q^{2i+2}}{1-q^{2i+2}}\bigr)$. **Verified.**
     - Item 4 & Eq. (2)–(3): $(-1)^{rn+s} = (-1)^r (-1)^s$, $q^{(rn+s)^2} \equiv q^{s^2}(1 - (r^2 n + 2rs)z)$, $[4rn+4s+1] \equiv [4s+1] + 4r q^{4s+1}[n]$, and $[4s+1]z = (1 - q^{4s+1})[n]$ assemble cleanly into Eq. (2) and $\Delta_8(q)$ in Eq. (3). **Verified.**
3. **Section 3 ($B_0(q) \bmod \Phi_n(q)^2$ via Watson's transformation):**
   - Checked Gasper–Rahman (III.18) and its $e \to \infty$ rational-function limit Eq. (4) term-by-term.
   - Checked specialization $Q = q^2, a = q, b = q^{1+n}, c = q, d = q^2$: cancellations $(d;q^2)_s = (Q;q^2)_s$, $(aQ/d;q^2)_s = (a;q^2)_s$, $(d;q^2)_k = (aQ/c;q^2)_k$, weight $(-1)^s q^{s^2}$, denominator exponents disjoint from $n\mathbb{Z}$, and $(1-q^{m+n})(1-q^{m-n}) \equiv (1-q^m)^2 \pmod{\Phi_n^2}$ reduce the LHS to $B_0(q) \pmod{\Phi_n^2}$.
   - On the RHS, $q$-Chu–Vandermonde (GR (II.7)) with $\beta = q^{1-n}, \gamma = q^{2-n}$ ($\gamma Q^N/\beta = q^n$) gives $[n]\frac{(q;q^2)_N}{(q^{2-n};q^2)_N}$, and reindexing $j \mapsto N-1-j$ modulo $\Phi_n(q)$ gives $(-1)^N q^{-N(N+1)} \equiv (-1)^N q^{N^2} \pmod{\Phi_n(q)}$ (since $N^2 + N(N+1) = Nn$). Multiplying by $[n]$ yields Eq. (5) modulo $\Phi_n(q)^2$ and $z B_0(q) \equiv 0 \pmod{\Phi_n(q)^2}$. **Verified.**
4. **Section 4 ($\Delta_8(q) \bmod \Phi_n(q)$ via $t$-deformation):**
   - Checked specialization $Q = q^2, a = t^4 q, b = t^2 q, c = t^4 q, d = q^2$ multiplied by $(1 - t^4 q)$, yielding Eq. (6) identically in $\mathbb{Q}(q, t)$.
   - Verified every denominator factor at $t = 1$ is coprime to $\Phi_n(q)$, so reducing modulo $\Phi_n(q)$ commutes with $-\frac{\partial}{\partial t}\big|_{t=1}$. Checked the product rule on $L_s(t) = (1 - t^4 q^{4s+1}) F_s(t)$ carefully (valid even when $n \mid (4s+1)$, where $1 - q^{4s+1} \equiv 0 \pmod{\Phi_n(q)}$, since logarithmic differentiation is only needed on the nonvanishing factor $F_s(t)$), recovering $\Delta_8(q) \bmod \Phi_n(q)$ identically.
   - On the RHS, $-\frac{d}{dt}(1 - t^4)\big|_{t=1} = 4$, and $q$-Chu–Vandermonde at $t = 1$ with $\beta = q, \gamma = q^2$ ($\gamma Q^N/\beta = q^n$) gives Eq. (7): $\Delta_8(q) \equiv 4(-1)^N q^{N^2} \pmod{\Phi_n(q)}$. **Verified.**
5. **Section 5 (Conclusion):**
   - Substituting (5), $z B_0 \equiv 0 \pmod{\Phi_n^2}$, and (7) into (2) gives Eq. (1) directly; summing over $0 \le r \le m-1$ completes the proof. **Verified.**

---

## 3. Independent Computation Check

- Inspected `targets/guo-2310.15207-conj6.8/notes/check-check-2.py` via AST: zero float literals or `float()` calls; every `/` operates strictly on exact `sympy` expressions or `fractions.Fraction`.
- Independently executed `.venv/bin/python -u targets/guo-2310.15207-conj6.8/notes/check-check-2.py`: exited with code `0` and raw `PASS` (covering $n=1$ boundary, symbolic + exact `Fraction` Watson (4), symbolic + `Fraction` + dual-number Eq. (6)–(7) vs $\Delta_8(q)$, and full block vanishing mod $\Phi_n^3$ + Eq. (1) + Conjecture 6.8 mod $\Phi_n^2$ for odd $n \in \{3, 5, 7, 9, 11, 13, 15\}$).

---

## 4. Handoff

**PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`), instructing them to mention `@coordinator` on PASS with verifier command `.venv/bin/python -u targets/guo-2310.15207-conj6.8/notes/check-check-2.py` and paths `targets/guo-2310.15207-conj6.8/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.
