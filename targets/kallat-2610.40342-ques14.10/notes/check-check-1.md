# Independent Check Report: `targets/kallat-2610.40342-ques14.10`

- **Verdict:** **PASS**
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/kallat-2610.40342-ques14.10/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2610.40342/paper1_valuation_calculus.tex` (Ahaan Kallat, *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, `arXiv:2610.40342v1`).
- Confirmed `TARGET.md` reproduces **Question 14.10** (`\label{prob:gcdr}`, Section 14, lines 1220–1222; `\newtheorem{problem}[theorem]{Question}`) verbatim, and matches the referenced results in the primary LaTeX:
  - **Theorem 5.1** (`\label{thm:gcdfamily}`, line 350) and eq. `(5.2)` (`\label{eq:sameg}`, line 378).
  - **Theorem 11.1** (`\label{thm:counter}`, line 914), **Proposition 11.2** (`\label{prop:lead}`, line 924), and **Proposition 11.3** (`\label{prop:globalgcd}`, line 937).
- Confirmed honest scope in `PROOF.md`:
  - **Q1** ($r=3$: $g_3(n) \ne G_3(n) \iff n \equiv 30 \pmod{81},\, n \ge 111$): **YES** (proved for all $n \ge 5$, with $G_3(n)/g_3(n) = 3$).
  - **Q2** ($g_r(n) = G_r(n)$ for all $r \ge 4,\, n \ge r+2$): **NO (Disproved)** at $n = 1248$ for all $64 \le r \le 79$ ($v_2(g_r(1248)) = v_2(\Lambda_r(1248)) = 1169 < 1170 = v_2(G_r(1248))$, witnessed by $S = \mathbb{N} \setminus \{96\}$).
  - **Q3** & **Q4**: Completely proved for $r = 3$ (all $n \ge 5$), with general $r \ge 4$ explicitly noted as remaining open.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/kallat-2610.40342-ques14.10/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Theorem 2 & Lemmas 2.1–2.2 (Q2 Disproof):**
   - Verified $\Delta(m) \ge 0$ for all $65 \le m \le 5000$, with zeros solely at $\{80, 96, 128\}$ and unique value $\le 1$ outside $\{80, 96, 128\}$ at $m = 72$ ($\Delta(72) = 1/2$).
   - Exhaustive integer DP on $\mathcal{P}_{>64}(1248)$ confirmed $\max \mathrm{cost}_2(\lambda) = 75$ and exactly the four partitions `96^13`, `96^1 128^9`, `80^6 96^8`, `80^8 96^1 128^4`.
   - Direct permutation-recurrence computation modulo $2^{1173}$ for every $r \in [64, 79]$ at $n = 1248$ confirmed $v_2(G_r(1248)) = 1170$ while $v_2(a_{\mathbb{N}\setminus\{96\}}(1248)) = 1169$.
2. **Lemmas 4.1–4.3 ($p = 3$ Calculus):**
   - Verified the $6^3 \leftrightarrow 9^2$ trade identity and $\Delta_{\mathrm{trade}}(Y', t)$ characterizations for $0 \le 2t \le Y' \le 45$, $x_0 \in \{0, 1, 2\}$.
   - Verified Lemma 4.2(1) for $4 \le m < 200$ ($m \notin \{6, 9\}$), computed exact $\mu_{\max}(w)$ for $0 \le w \le 30$, and verified every entry of the Lemma 4.2(3) classification table across $\rho \in \{0, \dots, 8\}$.
   - Verified exact $\tau_t(x_0, y) \in \mathbb{Z}_{(3)}$ and $S(x_0, y) \bmod 9$ for $x_0 \in \{1, 2\}$ and all $y \equiv 2 \pmod 3$, $5 \le y \le 149$.
3. **Theorems 1, 3, and 4 ($r = 3$, all $n \ge 5$):**
   - Brute-force partition enumeration of $\mathcal{P}_{>3}(n)$ for all $5 \le n \le 42$ (plus brute-force over all $2^{n-3}$ subsets $S \supseteq \{1, 2, 3\}$ for $5 \le n \le 16$) confirmed exact formulas for $v_2$, $v_3$, and primes $q \ge 5$ across $\Lambda_3(n)$, $g_3(n)$, and $G_3(n)$.
   - Exact DP + low-valuation $f_P(n)$ enumeration + exact permutation-recurrence checks for $43 \le n \le 134$ (and $n \in \{138, 165, 192, 213, 273, 354\}$) confirmed Theorems 1, 3, 4, Kallat Theorem 11.1 (`G_3(111) = 147259794302866275623239680`, $v_3(G_3(111)) = 28$, $v_3(a_{\mathbb{N}\setminus\{4,9\}}(111)) = 27$), and all rational constants (`5/32`, `11/128`, `33/32`, `653/4480`).

## 3. Gate 2 Novelty Status
- Passed by `watch-6` (`#1523`), `watch-1` (`#1524`), and `watch-5` (`#1525`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).
