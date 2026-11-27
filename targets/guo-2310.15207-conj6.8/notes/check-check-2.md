# Blind Check Report — `targets/guo-2310.15207-conj6.8/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty: PASS per `#953`, `#957`, `#966`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary source checked:** [tools/.arxiv_cache/eprint/2310.15207v1_dir/main.tex](file:///Users/kolinhuang/Documents/open-math/tools/.arxiv_cache/eprint/2310.15207v1_dir/main.tex) lines 1–40 (`\newtheorem{conjecture}[theorem]{Conjecture}`) and lines 795–835 (`\label{conj:8}`, Conjecture 6.8 in Section 6).
- **`TARGET.md` comparison:** Matches verbatim — claims that for all positive integers $m \ge 1$ and odd integers $n \ge 3$ (with $N = (n-1)/2$ and $\Phi_n(q)$ the $n$-th cyclotomic polynomial),
  $$\sum_{k=0}^{mn-1} (-1)^k [4k+1] \frac{(q;q^2)_k^3}{(q^2;q^2)_k^3} q^{k^2} \equiv (-1)^N q^{N^2} [n] \sum_{r=0}^{m-1} (-1)^r (4r+1) \frac{(\frac{1}{2})_r^3}{r!^3} \pmod{\Phi_n(q)^2}.$$
  The $n=1$ boundary remark in `PROOF.md` matches the odd-$n \ge 3$ hypothesis ($m=1$ holds; $m=2$ fails modulo $(q-1)^2$).

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/guo-2310.15207-conj6.8/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/guo-2310.15207-conj6.8/notes/check-check-2.py) (zero floating-point arithmetic; uses `fractions.Fraction` and `sympy` over $\mathbb{Q}[q]/(\Phi_n(q)^2)$, $\mathbb{Q}[q]/(\Phi_n(q))^3$, $(\mathbb{Q}[q]/(\Phi_n(q)))[u]/(u^2)$, and $\mathbb{Q}(Q,a,b,c,d)$).
- **Command & result:** `.venv/bin/python -u targets/guo-2310.15207-conj6.8/notes/check-check-2.py` exited with code `0` (`PASS`):
  1. `$n=1$ boundary remark`: $m=1$ gives $1 \equiv 1 \pmod{(q-1)^2}$, while $m=2$ gives $\frac{3}{8} - \frac{15}{16}(q-1) \not\equiv \frac{3}{8} \pmod{(q-1)^2}$.
  2. `Watson $e\to\infty$ identity (4)`: verified symbolically in $\mathbb{Q}(Q,a,b,c,d)$ for $N=1$ and across exact `Fraction` evaluations for $N=1..6$.
  3. `Parametric identity (6), logarithmic derivative vs $\Delta_8$ (3), and Eq. (7)`: verified symbolically in $\mathbb{Q}(q,t)$ at $n=3$, across exact `Fraction` points for $n \in \{3,5,7,9,11\}$, and via exact dual-number arithmetic at $t = 1+u$ ($u^2=0$) in $(\mathbb{Q}[q]/(\Phi_n(q)))[u]/(u^2)$ confirming $-\frac{\partial}{\partial t}\big|_{t=1}\mathrm{LHS}(6) \equiv \Delta_8(q) \equiv 4(-1)^N q^{N^2} \pmod{\Phi_n(q)}$ for $n \in \{3,5,7,9,11\}$.
  4. `Block vanishing, Eq. (1), $B_0$ vanishing mod $\Phi_n$, and full Conjecture 6.8`: for odd $n \in \{3,5,7,9,11\}$ ($m=1..5$) and $n \in \{13,15\}$ ($m=1..3$), verified $A_{rn+s}(q) \equiv 0 \pmod{\Phi_n(q)^3}$ for every $N+1 \le s \le n-1$, Eq. (1) for every block $B_r(q) \pmod{\Phi_n(q)^2}$, $B_0(q) \equiv 0 \pmod{\Phi_n(q)}$ and $z B_0(q) \equiv 0 \pmod{\Phi_n(q)^2}$, and the full Conjecture 6.8 congruence $\pmod{\Phi_n(q)^2}$.
