# Blind Audit: `targets/guo-2310.15207-conj6.4/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/guo-2310.15207-conj6.4/TARGET.md`, `targets/guo-2310.15207-conj6.4/PROOF.md`, `targets/guo-2310.15207-conj6.4/notes/check-check-3.md`, `targets/guo-2310.15207-conj6.4/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Source Verified:** Victor J. W. Guo, *"Dwork-type $q$-congruences through the $q$-Lucas theorem"*, `arXiv:2310.15207v1` (`2023-10-23`, sole arXiv version; published in *Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. (RACSAM)* 119 (2025), no. 4, DOI `10.1007/s13398-025-01762-9`, Crossref verified), TeX source `tools/.arxiv_cache/eprint/2310.15207v1_dir/main.tex` (944 lines, `0` `\iffalse` blocks).

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against `main.tex` (shared `\newtheorem{theorem}{Theorem}[section]` counter):
- **Section 2, Lemma 2.3 (`\label{lem:3}`, L277–283, `\label{eq:lem3}`):** exact match to `TARGET.md` L31–32.
- **Section 6 (*Open problems and concluding remarks*), Conjecture 6.3 (`\label{conj:3}`, L749–751) & Conjecture 6.4 (`\label{conj:4}`, L754–760):** exact verbatim match to `TARGET.md` L20–30, including all quantifiers ($n \equiv 1 \pmod 4$, $n > 1$, positive integers $r > s$), $q$-shifted factorial notation, and modulus $\Phi_{n^s}(q)^2$.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

Audited all 124 lines of `PROOF.md`:
1. **Setup & Telescoping Reduction (§1, L9–22):**
   - $N = n^s \equiv 1 \pmod 4$, $z = 1 - q^N$, $\Phi_N(q) \mid z \implies z^2 \equiv 0 \pmod{\Phi_N(q)^2}$.
   - Eq. (1): $1 - q^{a+KN} \equiv (1-q^a)(1 + K\frac{q^a}{1-q^a}z) \pmod{\Phi_N(q)^2}$ for $K \ge 0$, $1 \le a < N$, with $1 - q^a$ invertible modulo $\Phi_N(q)^2$ since $\Phi_N(q)$ is irreducible over $\mathbb{Q}$ and $1 \le a < N$. Because $\Phi_N(q)^2 \in \mathbb{Z}[q]$ is monic, congruence in $\mathbb{Q}[q]/(\Phi_N(q)^2)$ with denominator coprime to $\Phi_N(q)$ implies congruence in $\mathbb{Z}[q]$ after clearing denominators.
   - Eq. (2): $\frac{q^a}{1-q^a} + \frac{q^{N-a}}{1-q^{N-a}} \equiv -1 \pmod{\Phi_N(q)}$ ($1 \le a < N$) is exact.
   - Inductive telescoping from $R(n,s;q)$ via $T(n,r;q) = R(n,r;q)/R(n,r-1;q) \equiv 1 \pmod{\Phi_N(q)^2}$ ($r \ge s+1$) is exact.
2. **Conjecture 6.4 (§2, L26–86):**
   - **Step 2.1 (Coprimality):** All exponents in $R_4(n,s;q)$ lie in $[1, N-1]$ (including empty product when $s=1$), so both numerator and denominator are coprime to $\Phi_N(q)$.
   - **Step 2.2 (Cancellation of $n$-multiples, Eq. (3)):** Exact bounds for odd $2j+1$ and even $2j+2$ using $n^{r-2} \equiv n^{r-1} \equiv 1 \pmod 4$ (verified including edge case $r = 2$, $j_0 = 0$) cancel all $n$-multiples identically, leaving every remaining exponent coprime to $n$ and hence to $N$.
   - **Step 2.3 (Block decomposition & $\Delta Q_4(a)$, Eq. (4)):** Verified $k_1 - k_0 = MN$ ($K_0 = n^{r-1-s} \equiv 1 \pmod 4$, $c = (K_0-1)/2 \in 2\mathbb{Z}_{\ge 0}$), exact residue coverage ($\gcd(2,N)=1$), exact case analysis for $q_{\text{num}}(a), q_{\text{den}}(a) \in \{0,1,2\}$, and $\Delta Q_4(a) = (-1)^{a-1}$ on $[1,(N-1)/2]$ and $(-1)^a$ on $[(N+1)/2, N-1]$.
   - **Step 2.4 (Pairing cancellation):** Fixed-point-free involution $a \leftrightarrow N-a$ on $\{1 \le a < N : n \nmid a\}$ satisfies $\Delta Q_4(N-a) = \Delta Q_4(a)$, reducing the $z$-coefficient to $-\sum_{1 \le a \le (N-1)/2,\, n \nmid a} (-1)^{a-1} \pmod{\Phi_N(q)}$. Both $(N-1)/2$ and $(N/n - 1)/2$ are even (with empty sum for $s=1$), so the sum vanishes identically, giving $T_4(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$.
3. **Conjecture 6.3 (§3, L90–124):**
   - **Step 3.1 (Coprimality):** For $s=1$, the unique $n$-multiple in $(q^5;q^4)_{(n-1)/2}$ is $n$ (at $j=(n-5)/4$), which cancels the numerator of $[n] = (1-q^n)/(1-q)$; for $s \ge 2$, the unique $N$-multiple in $(q^5;q^4)_{(N-1)/2}$ cancels the $N$-multiple in $(q^{5n};q^{4n})_{(N/n-1)/2}$ (at $i=(N/n-5)/4$), while $[n]$ and $(q^{3n};q^{4n})_{(N/n-1)/2}$ are coprime to $\Phi_N(q)$. *(Minor non-blocking note: the exact maximum exponents are $2n-1, 2N-1, 2N-3n$ rather than the slightly looser upper bounds $2n+1, 2N+1, 2N-n$ written in L96–97; every stated inclusion and coprimality conclusion holds strictly.)*
   - **Step 3.2 (Cancellation of $n$-multiples, Eq. (5)):** Exact cancellation of $n(4j+3)$ and $n(4j+5)$ for $w_0 \le j \le v_0 - 1$ (verified including $r = 2, w_0 = 0$). *(Minor non-blocking note: at $k = v_1 - 1$, $4k+3 = 2n^r - 3$ and $4k+5 = 2n^r - 1$, so L101–102's upper bounds $2n^r-1$ and $2n^r+1$ are loose by $+2$; every stated inequality and equivalence still holds strictly because $n(2n^{r-1}-3) \le 2n^r-15 < 2n^r-3$ and $n(2n^{r-1}-1) \le 2n^r-5 < 2n^r-1$.)*
   - **Step 3.3 (Block decomposition & $\Delta Q_3(a)$, Eq. (6)):** Verified $v_1 - v_0 = M_3 N$, $\gcd(4, N) = 1$, $q_1(a) \equiv 1-a \pmod 4$, $q_2(a) \equiv 3-a \pmod 4$ in $\{0,1,2,3\}$, giving $\Delta Q_3(a) = -2$ for $a \equiv 0,1 \pmod 4$ and $+2$ for $a \equiv 2,3 \pmod 4$. Since $N \equiv 1 \pmod 4$, $\Delta Q_3(N-a) = \Delta Q_3(a)$, and on $\{1,\dots,(N-1)/2\}$ each consecutive pair $\{2m-1, 2m\}$ ($1 \le m \le (N-1)/4$) contributes $(-2)+(+2)=0$ (odd $m$) or $(+2)+(-2)=0$ (even $m$), and likewise for multiples of $n$ since $n \equiv 1 \pmod 4$ preserves $\Delta Q_3$ and $(N/n-1)/2$ is even. Thus $T_3(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$.

---

## 3. Independent Verification & Novelty Status

- Re-ran independent checker script (pure SymPy `ZZ[q]` polynomial & cyclotomic arithmetic, zero floats):
  - Command: `.venv/bin/python -u targets/guo-2310.15207-conj6.4/notes/check-check-3.py`
  - Result: exit code `0`, raw `PASS`.
- Independent auditor script additionally verified exact exponent multisets, $\Delta Q_4(a)$, $\Delta Q_3(a)$, pairing symmetry, and pair-by-pair $\{2m-1, 2m\}$ cancellation across $n \in \{5, 9, 13, 17\}$, $s \in \{1, 2\}$, $r \in \{2, 3\}$.
- Gate 2 novelty PASS receipts present from `watch-1` (`#892`), `watch-5` (`#899`), and `watch-6` (`#885`).

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Handing off directly to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).

---

## 5. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27`) — PASS

- **Module:** `lean/OpenMath/Guo231015207Conj64.lean` (imported at `lean/OpenMath.lean` L29).
- **Primary-Source Fidelity (`tools/.arxiv_cache/eprint/2310.15207v1_dir/main.tex`, `arXiv:2310.15207v1`):**
  - `qPoch a q m := ∏ k ∈ Finset.range m, (1 - a * q ^ k)`, `qNum n := ∑ k ∈ Finset.range n, X ^ k`, and `Phi N := Polynomial.cyclotomic N ℚ` match `main.tex` L96–102 verbatim (`(a;q)_0 = 1`, `[n]_q = (1 - q^n)/(1 - q)`).
  - `RatCongMod A₁ B₁ A₂ B₂ M` (L63–68) establishes `B₁ ≠ 0`, `B₂ ≠ 0`, reduced representations `P₁/Q₁ = A₁/B₁` and `P₂/Q₂ = A₂/B₂` with `Q₁, Q₂` coprime to `M = Φ_{n^s}(q)^2`, and `M ∣ P₁ * Q₂ - P₂ * Q₁` in `ℚ[q]`. Since `A₁, B₁, A₂, B₂ ∈ ℤ[q]` and `Φ_{n^s}(q)^2 ∈ ℤ[q]` is monic, divisibility of the reduced numerator of `A₁/B₁ - A₂/B₂` by `Φ_{n^s}(q)^2` in `ℚ[q]` is strictly equivalent to divisibility in `ℤ[q]` (`main.tex` L104–106), while additionally certifying regularity of each side modulo `Φ_{n^s}(q)^2`.
  - `num4`, `den4`, and `guo_conjecture_6_4` (L71–76, L1043–1045) match **Conjecture 6.4** (`\label{conj:4}`, `main.tex` L754–760) verbatim for all `n % 4 = 1`, `1 < n`, `1 ≤ s`, `s < r` (with exact integer divisions `(n^k - 1)/4` since `n^k % 4 = 1`).
  - `num3`, `den3`, and `guo_conjecture_6_3` (L79–86, L1789–1791) match **Conjecture 6.3** (`\label{conj:3}`, `main.tex` L749–751; referencing **Lemma 2.3** `\label{lem:3}`, `eq:lem3`, L277–283) verbatim under the exact same quantifiers.
- **Forbidden Token Audit:** `grep -nE "\b(sorry|admit|axiom|native_decide|unsafe|implemented_by|extern|set_option)\b"` returned `0` matches.
- **Standalone Lean 4 Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Guo231015207Conj64.lean`
  - Result: `EXIT=0`, `0` warnings.
  - `#print axioms`: both `guo_conjecture_6_4` and `guo_conjecture_6_3` depend strictly on `[propext, Classical.choice, Quot.sound]`.
- **Lean 4 Audit Verdict:** **PASS** (eligible for upgrade to `"Lean-verified"`).
