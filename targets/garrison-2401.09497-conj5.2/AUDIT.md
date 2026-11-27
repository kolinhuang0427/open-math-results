# Blind Audit Report: `garrison-2401.09497-conj5.2`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:20Z`
**Verdict:** **PASS** — Complete elementary proof for all $k \ge 1$ (`"written proof, internally audited"`).

## 1. Primary-Source Fidelity
Verified verbatim against `arXiv:2401.09497v1` (confirmed latest version via live arXiv API query on `2026-11-27`, published/updated `2024-01-17T05:11:33Z`), Thomas Garrison, Chris Seiler, and Andrew Knowles, *"Weakly Consecutive Sequences"*, `tools/.arxiv_cache/eprint/2401.09497/WCS.tex`:
- **Definition 1.1 (`\label{def:weak_consec}`, Section 1, lines 83–85):**
  > Let $\sigma : [k] \to [k]$ be a permutation for a natural number $k$. We say $\sigma$ is *weakly consecutive* if, for all $i,j \in [k]$ and integers $m$, if $m \mid \sigma(i)$ and $m \mid (i - j)$, then $m \mid \sigma(j)$.
- **Conjecture 5.2 (`\label{conj:1 at end}`, Section 5, lines 718–720):**
  > Any WCS either begins or ends with the term $1$ (in other words, $\sigma(1) = 1$ or $\sigma(k) = 1$).
- `TARGET.md` and `PROOF.md` match the primary source verbatim for all $k \ge 1$.

## 2. Line-by-Line Mathematical Audit of `PROOF.md`
Every step and edge case was checked independently with zero gaps found:
1. **Base cases ($k = 1, 2$):** Trivially verified; henceforth $k \ge 3$.
2. **Lemma 1 (Reversal):** $\sigma^{\mathrm{rev}}(i) = \sigma(k+1-i)$ preserves weak consecutiveness (since $(k+1-i)-(k+1-j) = -(i-j)$) and swaps $\sigma(1)$ with $\sigma(k)$. Rigorous.
3. **Lemma 2 (Residue-class characterization):** For every $m \in [k]$, $S_m^\sigma \subseteq T_m^\sigma$, $|T_m^\sigma| = \lfloor k/m \rfloor = q$, and $|S_m^\sigma|$ equals $q$ if $c_m > k \bmod m$ and $q+1$ otherwise (checked at boundary indices $t = -1, 0, q-1, q, q+1$ and at $m = 1, k$). Hence $c_m > k \bmod m$ and $S_m^\sigma = T_m^\sigma$. Rigorous.
4. **Lemma 3 (GCD representation):** CRT gives a unique $a \in \{0, \dots, L_k - 1\}$ with $a \equiv -c_{p^{e_p}} \pmod{p^{e_p}}$ for all primes $p \le k$. For any $p^e \le k$ ($1 \le e \le e_p$), evaluating at $i_0 = \sigma^{-1}(p^{e_p})$ gives $c_{p^e} \equiv i_0 \equiv c_{p^{e_p}} \equiv -a \pmod{p^e}$, so $p^e \mid \sigma(i) \iff p^e \mid (a+i)$. Since $a + i \ge 1$ for all $i \in [k]$ and every prime power dividing $\sigma(i)$ or $L_k$ is $\le k$, $\sigma(i)$ and $\gcd(a+i, L_k)$ have identical $p$-adic valuations for all primes $p$, yielding $\sigma(i) = \gcd(a+i, L_k)$ and $m \mid \sigma(i) \iff m \mid (a+i)$ for all $m \in [k]$. Rigorous.
5. **Case 1 (Even $k \ge 4$):** Reversing if needed sets $c_2 = 2$ ($\sigma(i) \equiv i \pmod 2$). For $m = k/2 + 1 \in (k/2, k)$, Lemma 2 restricts $j = \sigma^{-1}(m)$ to $\{k/2, k/2 + 1\}$; parity forces $j = k/2 + 1$. If $A = \sigma(1) > 1$, then $c_A = 1 \implies A \mid k$, and $A$ is odd $\implies A \mid k/2$; weak consecutiveness from $i = 1$ to $j = k/2 + 1$ gives $A \mid (k/2 + 1)$, forcing $A \mid 1$, contradiction. Rigorous.
6. **Case 2 (Odd $k \ge 3$):** Suppose $\sigma(1) > 1$ and $\sigma(k) > 1$.
   - *Step 1:* $k$ odd forces $c_2 = 2$, $2 \mid a$, and $\sigma(1), \sigma(k) \ge 3$ odd. Lemma 2 at $1$ and $k$ gives $\sigma(1) \mid k$, $\sigma(1) \mid (a+1)$, $\sigma(k) \mid k$, and $\sigma(k) \mid a$, hence $\gcd(\sigma(1), \sigma(k)) = 1$ and $\sigma(1) \neq \sigma(k)$. Reversing if needed gives $3 \le A := \sigma(1) < B := \sigma(k)$ odd coprime, $k = ABR$ with $R \ge 1$ odd ($BR \ge 5$, $k \ge 15$), $2 \mid a$, $a \equiv -1 \pmod A$, and $B \mid a$. Rigorous.
   - *Step 2:* $m = (k+A)/2 = A\frac{BR+1}{2} \in (k/2, k)$ has $k \bmod m = (k-A)/2$, so $j = \sigma^{-1}(m) \in [(k-A)/2 + 1, (k+A)/2]$. Since $A \mid m$ implies $j \equiv 1 \pmod A$ and $(k-A)/2 + 1 = A\frac{BR-1}{2} + 1 \equiv 1 \pmod A$, the interval of length $A-1$ pins $j = (k-A)/2 + 1$. Lemma 3 yields $m \mid (a + j) - m = a + 1 - A$, hence $\frac{BR+1}{2} \mid (a + 1 - A)$. Rigorous.
   - *Step 3:* Writing $BR + 1 = 2^s u$ ($s \ge 1$, $u \ge 1$ odd) and $i_1 = (A-1)BR \in [k]$, the exact identity $a + i_1 = (a+1-A) + (A-1)(BR+1)$ implies $u \mid (a+i_1)$ and $B \mid (a+i_1)$. If $2^s \mid (a+i_1)$, then since $\gcd(2^s, u) = 1$, $\gcd(B, BR+1) = 1$, $B < k$, and $BR + 1 < 3BR \le k$, we have $B(BR+1) \mid L_k$ and $B(BR+1) \mid (a+i_1)$, whence $B(BR+1) \mid \sigma(i_1) \le ABR$, contradicting $A < B$. Thus $2^s \nmid (a+i_1)$. Since $2^{s+1} \mid (A-1)(BR+1)$, $s = 1$ contradicts $2 \mid a$ and $2 \mid (A-1)$, forcing $s \ge 2$; and $2^{s-1} \mid (a+1-A)$ with $2^s \nmid (a+1-A)$ pins $a \equiv A - 1 + 2^{s-1} \pmod{2^s}$. Rigorous.
   - *Step 4:* Both $2^s \le BR+1 < k$ and $A < k$ divide $L_k$ and are coprime, so $2^s A \mid L_k$. For $0 \le t \le u - 1$ (checked including $u = 1$), $i_t = (2^{s-1} - 1)A + 1 + t \cdot 2^s A$ satisfies $4 \le i_0 \le i_t \le i_{u-1} = k - 2^{s-1} A + 1 \le k - 5 < k$, giving $u$ distinct indices in $[k]$. Since $A$ is odd, $2^{s-1} A \equiv 2^{s-1} \pmod{2^s}$, so $a + i_t \equiv 0 \pmod{2^s}$ and $a + i_t \equiv 0 \pmod A$, hence $2^s A \mid \gcd(a+i_t, L_k) = \sigma(i_t)$. Injectivity of $\sigma$ produces $u$ distinct positive multiples of $2^s A$ in $[k]$, contradicting $k = A(2^s u - 1) < u \cdot (2^s A)$. Complete and airtight.

## 3. Independent Mechanical Verification
Audited `targets/garrison-2401.09497-conj5.2/notes/check-check-1.py` (pure integer arithmetic, zero floats) and ran it directly:
- Command: `.venv/bin/python targets/garrison-2401.09497-conj5.2/notes/check-check-1.py`
- Result: exit `0`, raw `PASS` (exhaustive permutation verification for $k = 1 \dots 8$; exhaustive GCD search over all $0 \le a < L_k$ for $k = 3 \dots 12$; verification of Case 2 Steps 2–4 congruences, index bounds, and pigeonhole bound across all $46$ admissible odd composite triples $(A, B, R)$ with $k = ABR \le 150$).

## 4. Verdict & Handoff
**PASS.** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final coordinator verification.

---

## 5. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T11:57Z`) — **PASS**

- **Module audited:** `lean/OpenMath/Garrison240109497Conj52.lean` (imported in `lean/OpenMath.lean` L20).
- **Primary-source & `PROOF.md` fidelity:** Verified verbatim against `tools/.arxiv_cache/eprint/2401.09497/WCS.tex` (`arXiv:2401.09497v1`, Definition 1.1 `\label{def:weak_consec}` L83–85 & Conjecture 5.2 `\label{conj:1 at end}` L718–720) and `PROOF.md`:
  - `IsWeaklyConsecutive k σ` (L40–43) encodes `Set.BijOn σ (Set.Icc 1 k) (Set.Icc 1 k)` and `∀ i ∈ Set.Icc 1 k, ∀ j ∈ Set.Icc 1 k, ∀ m : ℤ, m ∣ (σ i : ℤ) → m ∣ ((i : ℤ) - (j : ℤ)) → m ∣ (σ j : ℤ)` (casting to `ℤ` prior to subtraction, avoiding `Nat` subtraction truncation, and quantifying over all integers `m : ℤ`).
  - `IsWeaklyConsecutivePerm σ` (L46–49) gives the equivalent 1-based formulation directly on `Equiv.Perm (Fin k)`.
  - Main theorems `garrison_conjecture_5_2` (`∀ {k : ℕ} (hk : 1 ≤ k) {σ : ℕ → ℕ}, IsWeaklyConsecutive k σ → σ 1 = 1 ∨ σ k = 1`, L892–893) and `garrison_conjecture_5_2_perm` (`(σ ⟨0, _⟩).val = 0 ∨ (σ ⟨k - 1, _⟩).val = 0`, L916–918) capture Conjecture 5.2 faithfully for all $k \ge 1$ with zero hidden hypotheses or edge-case omissions.
- **Hygiene & kernel verification:**
  - Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or `set_option`.
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Garrison240109497Conj52.lean` -> exit code `0`, zero warnings.
  - `#print axioms` on `wcs_residue_class`, `wcs_gcd_repr`, `garrison_conjecture_5_2`, and `garrison_conjecture_5_2_perm`: strictly `[propext, Classical.choice, Quot.sound]`.
- **Verdict:** **PASS** (upgrades status label to `machine-checked proof in Lean 4`).
