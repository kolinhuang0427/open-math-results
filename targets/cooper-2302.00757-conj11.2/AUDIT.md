# Adversarial Audit — `targets/cooper-2302.00757-conj11.2/`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-27T01:45Z` (Gate 3 pending)
- **Target:** Shaun Cooper, *"Apéry-like sequences defined by four-term recurrence relations"*, `arXiv:2302.00757v2` (updated 2024-05-08; published in *Contemporary Mathematics* **818**, AMS 2025, pp. 137–179, DOI `10.1090/conm/818/16373`), Section 11.1 **Conjecture 11.2** (sequence $T_{11}(n) = \mathrm{OEIS}\ \mathrm{A284756}(n)$).
- **Isolation:** Inspected ONLY primary source (`arXiv:2302.00757v2`, `tools/.arxiv_cache/eprint/2302.00757/main.tex`, plus OEIS `A284756` and cited literature via helper), `TARGET.md`, `PROOF.md`, independent checker files (`notes/check-check-1.md`, `notes/check-check-1.py`), Gate 2 receipts (`notes/novelty-gate2-watch-{1,2,5}.md`), and adversarial helper report (`notes/audit-helper-cooper.md`). Did **not** read `verify.py` or author scratch `notes/`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Fidelity & Definition Verification

Verified directly against `tools/.arxiv_cache/eprint/2302.00757/main.tex` and `notes/audit-helper-cooper.md` §1:

1. **Exact definition & modular parametrization (`main.tex` Section 3 Theorem 3.1 `\label{interesting}`, Tables 3–5, Section 5 lines 1607–1635):**
   - $Z(q) = U_1(q) = \left(\sum_{j,k \in \mathbb{Z}} q^{j^2 + jk + 3k^2}\right)^2$, $V_1(q) = \eta_1^2 \eta_{11}^2 = q \prod_{m \ge 1}(1-q^m)^2(1-q^{11m})^2$, $X_1(q) = V_1(q)/U_1(q)$.
   - Applying Theorem 3.1 (`\ref{interesting}`) with level-11 data $B^2 = 1 - 20X + 56X^2 - 44X^3$ and $H = 4X(1 - 8X + 11X^2)$ (Tables 3–4, citing Cooper 2017 and Cooper–Ge–Ye 2015) rigorously yields $U_1(q) = \sum_{n=0}^\infty T_{11}(n) X_1(q)^n$ with $T_{11}(n) \in \mathbb{Z}$, $T_{11}(0) = 1$, and the exact four-term recurrence in `PROOF.md` line 4 (`1, 4, 28, 268, 3004, 36784, ...` = OEIS `A284756`).
2. **Exact Conjecture 11.2 numbering and wording (`main.tex` lines 2536–2567):**
   - Section 11 contains six `conjecture` environments sharing the `[theorem]` counter (zero other theorem-like environments): Conjecture 11.1 (`\label{c11}`, lines 2537–2549) and **Conjecture 11.2** (unlabelled, lines 2557–2565):
     $$T_{11}(3n) \equiv T_{11}(n) + 3n \pmod{3^2} \quad\text{and}\quad T_{11}(5n) \equiv T_{11}(n) \pmod{5^2} \iff 5 \mid n.$$
   - Implicit quantifier from lines 2539, 2555–2567: all positive integers $n$ (also holds trivially at $n = 0$ since $T_{11}(0) = 1$).
   - `TARGET.md` and `PROOF.md` match the primary source verbatim with zero quantifier or definition drift. *(Minor harmless note: `notes/check-check-1.md` line 11 misattributed `\label{c11}` to Conjecture 11.2 rather than 11.1; neither `TARGET.md` nor `PROOF.md` has this slip.)*

---

## 2. Adversarial Line-by-Line Mathematical Audit of `PROOF.md`

Audited every lemma, modular weight/level/character claim, Sturm bound (including the $p \mid N$ and prime-power $p^2$ cases!), $p$-adic Taylor expansion, homogenization, and coefficient extraction with zero gaps found:

- **Lemma 1 (Modular forms on $\Gamma_0(11)$ and $\Gamma_0(11p)$, lines 19–25):**
  - Binary quadratic form $Q(j,k) = j^2+jk+3k^2$ has even integral Gram matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 6 \end{pmatrix}$ with $\det A = 11$ and $11 A^{-1} = \begin{pmatrix} 6 & -1 \\ -1 & 2 \end{pmatrix}$ even integral, so $f(\tau) \in M_1(\Gamma_0(11), (\frac{\cdot}{11}))$ and $U_1 = f^2 \in M_2(\Gamma_0(11))$ (trivial character).
  - $V_1 = \eta(\tau)^2\eta(11\tau)^2 \in S_2(\Gamma_0(11))$ (trivial character: $\frac{1}{2}(2+2) = 2$, $2(1+11) = 24 \equiv 0 \pmod{24}$, $1^2 \cdot 11^2 = \square$, order $1$ at cusps $\infty$ and $0$).
  - Since $\dim M_2(\Gamma_0(11)) = 2$ (basis $E_{2,11} = \frac{11 E_2(11\tau) - E_2(\tau)}{10} = 1 + \frac{12}{5}\sum_{n\ge 1}(\sigma_1(n)-11\sigma_1(n/11))q^n$ and $V_1 = q - 2q^2 + \cdots$), matching $q^0, q^1$ proves $U_1 = E_{2,11} + \frac{8}{5} V_1$ unconditionally.
  - Standard $V_p$-operator sends $M_2(\Gamma_0(11)) \to M_2(\Gamma_0(11p))$ with trivial character, so any degree-$d$ homogeneous integer polynomial in $(U_1, V_1, U_p, V_p)$ lies in $M_{2d}(\Gamma_0(11p)) \cap \mathbb{Z}[[q]]$.
  - $X_1(q) = V_1(q)/U_1(q) \in q + q^2 \mathbb{Z}[[q]]$ ensures injectivity of $A(X) \mapsto A(X_1(q))$ on $(\mathbb{Z}/m\mathbb{Z})[[X]]$. Complete.
- **Lemma 2 (Sturm's theorem for $p \mid N$ and $m = p^2$, lines 27–30):**
  - Adversarially verified the two subtleties:
    1. **Prime $p \mid N$ ($p=3 \mid 33$, $p=5 \mid 55$):** Even though $G |_k \gamma$ for $\gamma \in \Gamma_0(N) \backslash \mathrm{SL}_2(\mathbb{Z})$ can acquire negative $\mathfrak{p}$-adic valuations at other cusps, rescaling each factor $g_i = G |_k \gamma_i$ ($i \ge 2$) by a uniformizer power $\pi^{-d_i}$ to valuation $0$ multiplies the norm $\prod_{i=1}^m g_i \in M_{mk}(\mathrm{SL}_2(\mathbb{Z}))$ by a single scalar, yielding $F \in M_{mk}(\mathrm{SL}_2(\mathbb{Z})) \cap \mathcal{O}_{\mathfrak{p}}[[q]]$ with $F \not\equiv 0 \pmod{\mathfrak{p}}$ and $\mathrm{ord}_q(G \bmod p) \le \mathrm{ord}_q(F \bmod \mathfrak{p}) \le \lfloor mk/12 \rfloor$ (via the level-1 Victor Miller $\mathbb{Z}$-basis). Thus Sturm's bound holds unconditionally for $p \mid N$.
    2. **Prime powers $m = p^2$ ($9, 25$):** $[q^j] G \equiv 0 \pmod{p^2}$ for $j \le B(k, N)$ implies $G \equiv 0 \pmod p$, hence $H := G/p \in M_k(\Gamma_0(N)) \cap \mathbb{Z}[[q]]$ satisfies $[q^j] H \equiv 0 \pmod p$ for $j \le B(k, N)$, so $H \equiv 0 \pmod p$ and $G \equiv 0 \pmod{p^2}$.
  - Subgroup indices $[\mathrm{SL}_2(\mathbb{Z}):\Gamma_0(N)] = 12, 48, 72$ for $N = 11, 33, 55$, giving $B(k, 11) = k$, $B(k, 33) = 4k$ ($B(30, 33) = 120$), and $B(k, 55) = 6k$ ($B(10, 55) = 60$, $B(66, 55) = 396$). Complete.
- **Section 2 (Part (1): $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod 9$, lines 34–70):**
  - Step 2.1: $U_1 - V_1 = E_{2,11} + \frac{3}{5} V_1 \equiv 1 \pmod{3\mathbb{Z}[[q]]} \implies (1-X)Z(X) \equiv 1 \pmod 3 \implies T_{11}(n) \equiv 1 \pmod 3$, $Z(X) = (1-X)^{-1} + 3 F(X)$, and $Z'(X) \equiv (1-X)^{-2} \pmod 3$.
  - Step 2.2: $X_1(q)^3 = X_3(q) + 3\Delta_3(q)$ ($\Delta_3 \in q^3\mathbb{Z}[[q]]$) gives $Z(X_1^3) \equiv U_3 + \frac{X_1^3 - X_3}{(1-X_3)^2} \pmod{9\mathbb{Z}[[q]]}$.
  - Step 2.3: Every term of $G_3$ (line 58) is verified homogeneous of degree $15$ (exact weight $30$ on $\Gamma_0(33)$), $D_3$ (line 56) is a unit in $\mathbb{Z}[[q]]$ of weight $28$, and $G_3/D_3$ reproduces line 54 with $(U_1 - V_1) \equiv 1 \pmod 3$ multiplying only mod-3-divisible terms (valid mod 9). Checking $[q^j] G_3 \equiv 0 \pmod 9$ through $q^{130} > 120$ gives $G_3 \equiv 0 \pmod 9$, yielding $(1-X)Z(X) - (1-X^3)Z(X^3) \equiv 3 \frac{N_3(X)}{(1-X^3)^2} \pmod 9$. *(Minor prose nit: line 62 starts with `"Wait:"` — harmless.)*
  - Step 2.4: Dividing by $3(1-X)$ and using $(1-X)(X^3 - X^5 + X(1-X^3)) \equiv N_3(X) \pmod 3$ gives $F(X) - (1+X+X^2)F(X^3) \equiv \sum_{k \ge 0}(k X^{3k} + X^{3k+1} - k X^{3k+2}) \pmod 3$; reading $[X^{3n}]$ yields $f(3n) - f(n) \equiv n \pmod 3$, hence $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod 9$. Complete.
- **Section 3 (Part (2): $T_{11}(5n) \equiv T_{11}(n) \pmod{25} \iff 5 \mid n$, lines 74–103):**
  - Step 3.1: $G_{5,\text{luc}} = U_1^5 - \widetilde{P}_5(U_1, V_1) U_5 \in M_{10}(\Gamma_0(55)) \cap \mathbb{Z}[[q]]$ vanishes mod $5$ through $q^{80} > B(10,55) = 60$, yielding $Z(X) \equiv P_5(X) Z(X^5) \pmod 5$. Thus $T_{11}(k) \not\equiv 0 \pmod 5$ for all $k \ge 0$ (since $T_{11}(0..4) \equiv 1,4,3,3,4 \pmod 5$) and $Z'(X) \equiv \frac{P_5'(X)}{P_5(X)} Z(X) \pmod 5$.
  - Step 3.2: $X_1^5 = X_5 + 5\Delta_5$ yields $Z(X_1^5) \equiv U_5 + (X_1^5 - X_5) \frac{P_5'(X_5)}{P_5(X_5)} U_5 \pmod{25\mathbb{Z}[[q]]}$; reducing $P_5'(X) = 4+6X+9X^2+16X^3 \equiv 4+X+4X^2+X^3 \pmod 5$ inside the $5\Delta_5$ term preserves exact validity mod $25$.
  - Step 3.3: Every term of $G_5$ (line 94) is verified homogeneous of degree $33$ (exact weight $66$ on $\Gamma_0(55)$), $D_5 = U_1^{24} U_5^4 \widetilde{P}_5(U_5, V_5)$ is a unit in $\mathbb{Z}[[q]]$ of weight $64$, and $G_5/D_5$ reproduces line 96 identically. Checking $[q^j] G_5 \equiv 0 \pmod{25}$ through $q^{405} > B(66,55) = 396$ yields $G_5 \equiv 0 \pmod{25}$, and substituting $U_5/P_5(X_5) \equiv Z(X_5^5) \equiv Z(X_1^{25}) \pmod 5$ inside the $5 R_{25}$ term gives $Z(X) \equiv P_5(X) Z(X^5) + 5 R_{25}(X) Z(X^{25}) \pmod{25}$.
  - Step 3.4: For $n = 5k+r$ ($0 \le r \le 4$), since $\deg P_5 = 4 < 5$ and $\deg R_{25} = 24 < 25$, extracting $[X^{5n}] = [X^{25k+5r}]$ yields $T_{11}(5n) \equiv T_{11}(n) + 5 r_{5r} T_{11}(k) \pmod{25}$. With $T_{11}(k) \not\equiv 0 \pmod 5$ and $(r_0, r_5, r_{10}, r_{15}, r_{20}) = (0, 1, 3, 4, 2)$, this vanishes mod $25$ iff $r = 0$, i.e. $5 \mid n$. Complete and airtight.

---

## 3. Independent Computational & Symbolic Verification

1. **Independent checker execution (`notes/check-check-1.py`):**
   - Command: `time .venv/bin/python targets/cooper-2302.00757-conj11.2/notes/check-check-1.py`
   - Result: **PASS**, exit code `0`, wall time `0.686s` (`notes/audit-helper-cooper.md` §3.1).
   - Verified Cooper's recurrence & direct checks for $0 \le n \le 1000$ ($c(3)=333, c(5)=200$), $U_1 = E_{2,11} + \frac{8}{5}V_1$, $Z(X_1) = U_1 \pmod{9, 25}$, $G_3 \equiv 0 \pmod 9$ up to $q^{130}$, $G_{5,\text{luc}} \equiv 0 \pmod 5$ up to $q^{80}$, $G_5 \equiv 0 \pmod{25}$ up to $q^{405}$, and $R_{25}$ coefficients.
2. **Independent SymPy symbolic check (`notes/audit-helper-cooper.md` §3.2):**
   - Confirmed exact uniform weights (`G_3`: weight 30; `G_5`: weight 66), exact symbolic quotients `G_3/D_3` and `G_5/D_5`, Step 2.4 mod-3 polynomial identity, and `P_5'(X)` mod-5 reduction.

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-cooper.md` §1–§2, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,2,5}.md`) confirmed:
- **No prior proof of Conjecture 11.2 found** across arXiv, OEIS `A284756` (rev. 44), Crossref, Zenodo, web search, `367` local watch snapshots, and competing GitHub repos (`the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `openai/math`, global GitHub).
- **Important related works verified distinct:**
  - Beukers–Tsai–Ye (`arXiv:2408.16616v2`, *Bull. LMS* 2025) prove the mod-$p$ **Lucas congruences** for $T_{11}(n)$ (Section 5 conjecture), NOT the mod-9 / mod-25 supercongruences of Conjecture 11.2 (`PROOF.md` Steps 2.1 and 3.1 reprove the $p=3,5$ mod-$p$ cases self-containedly as lemmas).
  - Beukers (`arXiv:2403.03301v3`, *Alg. Number Th.* 2026) and `eliottcassidy2000/math` treat 3-term sequences ($s_7, s_{10}, s_{18}$), not $T_{11}$.
  - Campbell (`arXiv:2610.00551v1`) proves a double binomial sum for $T_{11}(n)$ with no supercongruences; Caruso–Fürnsinn–Vargas-Montoya–Zudilin (`arXiv:2510.23298v1`) treat mod-$p$ Galois groups only.
  - `rbajaj5/a183068-supercongruence` (`related-results/CooperLevel11RarePrimes.md`, Jul 2026) explicitly cites Cooper's Conjecture 11.2 as an **unproved** computational target.
- **No `CONTESTED.md`** exists in `targets/cooper-2302.00757-conj11.2/`.
- **What Is Not Established / Caveats:**
  - Proves Conjecture 11.2 ($p=3 \bmod 9$ and $p=5 \bmod 25$) only; does **not** settle Conjecture 11.1 ($p \in \{2, 59, 5581\}$) or Conjectures 11.3–11.6.
  - Depends on Cooper's published Theorem 3.1 + Table 3/4/5 modular parametrization ($U_1 = \sum T_{11}(n) X_1^n$), Sturm's theorem on $\Gamma_0(33)$ / $\Gamma_0(55)$, and exact finite $q$-series checks (`notes/check-check-1.py`) up to $q^{130} / q^{80} / q^{405}$.
  - The paywalled AMS *Contemp. Math.* **818** (2025) PDF was not directly opened (mitigated by post-referee `2302.00757v2` and Campbell `2610.00551` citing the 2025 volume without any Section 11 proof); OpenAlex & Semantic Scholar were HTTP 429 rate-limited; `JENW1N/complete-math-solutions` and `TheJustinSunPrize/awards` will be covered in Gate 3.
  - Internal audit and exact computation are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`.

- **Gate 3 Novelty Clearance (`2026-11-27T02:00Z`–`03:09Z`):** **PASS** across all four watcher receipts (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-3.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`), covering live arXiv `2302.00757v2`, OpenAlex citing check (`arXiv:2604.14219v2` verified unrelated level-8), Zenodo, `413` watch snapshots, `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, and `DomTheDeveloper/ProofPlaygrond`. Cleared for coordinator verification.
