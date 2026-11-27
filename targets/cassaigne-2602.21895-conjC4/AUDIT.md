# Adversarial Audit Report: `targets/cassaigne-2602.21895-conjC4/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T06:21Z` (re-audit after `@scout2-6` fix `#848`)
- **Target:** Julien Cassaigne, Bastián Espinoza, Michel Rigo, Manon Stipulanti, *"Symbols frequencies in the Thue--Morse word in base $3/2$ and related conjectures"*, `arXiv:2602.21895v1` (`2026-02-25`), Section 1.4, Dekking Conjecture `(C_4)`
- **Owner:** `scout2-6`
- **Checker:** `check-2` (`notes/check-check-2.md`, `notes/check-check-2.py`)
- **Audit Helper:** `cassaigne-audit-hlp` (`notes/audit-helper-cassaigne.md`, killed)
- **Strict Isolation Observed:** Read ONLY the primary source (`tools/.arxiv_cache/eprint/2602.21895/merge_version.tex` via `notes/audit-helper-cassaigne.md`), `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and `notes/audit-helper-cassaigne.md`. Did NOT read author `verify.py` or any author scratch notes. Did NOT edit `TARGET.md` or `PROOF.md`.
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against `arXiv:2602.21895v1` (`tools/.arxiv_cache/eprint/2602.21895/merge_version.tex`, `notes/audit-helper-cassaigne.md` §1):
- **Latest arXiv version:** `2602.21895v1` (`2026-02-25`, sole version, no journal-ref/DOI).
- **Definitions (`eq:t32relations` lines 411–417, `lem:morphic_image` lines 436–446):** $\mathbf{t}_{3/2} = (t_n)_{n\ge 0}$ satisfies $t_0 = {\tt 0}$, $t_{3n} = t_{3n+1} = t_{2n}$, $t_{3n+2} = 1 - t_{2n+1}$ ($n \ge 0$), and $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`OEIS A357448`) where $\varphi({\tt 0}) = {\tt 010}$, $\varphi({\tt 1}) = {\tt 101}$.
- **Verbatim Conjecture $(C_4)$ (Section 1.4, lines 493–495):**
  > $(C_4)$ It is conjectured that frequencies of the words $w \in \mathcal{A}^*$ occurring in $\mathbf{t}'$ exist. It is also conjectured that $w$ and its reversal have the same frequency. Similar questions can also be asked for $\mathbf{t}_{3/2}$.
- **Verified foundation in `2602.21895v1` (`thm:existence_freqs_iff_mun_exist`, lines 1265–1273):** Unconditionally proves $\lim_{N\to\infty} C_n(c,k,N)/N = 2^{-n-1}$ for all $n \ge 0$, $c \in \{{\tt 0}, {\tt 1}\}$, $k \in \mathbb{Z}$. Section 7 (lines 2090–2121) explicitly leaves Conjecture `(C_4)` open for all factor lengths $|w| \ge 2$ and for reversal symmetry of frequencies.
- No `CONTESTED.md` exists in `targets/cassaigne-2602.21895-conjC4/`.

---

## 2. Adversarial Line-by-Line Mathematical Audit

All steps of `PROOF.md` (including `@scout2-6`'s fixes to lines 30–32, 45, and 51) were checked independently from scratch:

1. **Desubstitution & Lemma 1 (lines 15–32):**
   - $t_m = t_{S(m)} \oplus \varepsilon(m)$ and $S(3j+m) = 2j + S(m)$, $\varepsilon(3j+m) = \varepsilon(m)$ hold for all $j, m \in \mathbb{Z}$; $S(I_r) = [a_r, b_r] \cap \mathbb{Z}$ is contiguous with $a_0 = a_1 = 0$, $a_2 = 1$.
   - Re-audit of fixed lines 30–32: splitting $s \in \{0, 1\}$ vs $s = 2$ gives $2q+1 < 3q+1 \le L$ and $2q+2 < 3q+3 = L$ for $r = 0, q \ge 1$; $2q+1 < 3q \le L$ and $2q+2 < 3q+2 = L$ for $r = 1, q \ge 2$; and $2q < 3q-1 \le L$ and $2q+1 < 3q+1 = L$ for $r = 2, q \ge 2$. Every inequality now holds strictly with zero boundary flaws.
2. **Lemma 2 (lines 34–45):**
   - Congruence inversion $3q_n \equiv 1 \pmod{2^{n+1}}$ yields $k_0 = 2q_n k$ (even), $k_1 = 2q_n k - 2q_n$ (even), $k_2 = 2q_n k - q_n$ (odd), giving exact bijections on residue classes mod $2^n$ vs $2^{n+1}$.
   - Verified algebraically and exhaustively (`notes/audit-helper-cassaigne.md` §3.2) that the actual boundary error satisfies $E \in \{0, 1\}$ (hence $|E| \le 1 \le 3L + 3$) for all $N \ge 3, L \ge 2, n \ge 0$, including $N < 3L$ (now explicitly noted at line 45).
   - Dividing by $N / 2^n$ gives uniform error $O_L(2^n / N)$ (verified even when $2^n \gg N$ since $|\lfloor 2N/3 \rfloor/(2N) - 1/3| \cdot 2^{n+1}/\lfloor 2N/3 \rfloor \le 2^n / N$ for $N \ge 3$).
3. **Section 2 & Proposition 1 (lines 49–83):**
   - Empty word $L = 0$ now cleanly handled at line 51 ($f(\varepsilon) = 1$).
   - Direct calculation verified for all four $L = 2$ words and all $L = 3$ words ($f(w) = \frac{9}{8}(g(w) + \frac{1}{3}g(w'))$ solves $f(w) - \frac{1}{3}f(w') = g(w)$ uniquely); $f(w) \in \mathbb{Q} \cap [0, 1]$ for all $w \in \{0, 1\}^*$.
   - Strong induction on $L \ge 1$: base case $L = 1$ holds unconditionally by `thm:existence_freqs_iff_mun_exist` of `arXiv:2602.21895v1`; for $L \ge 2$, any increasing $M_t \to \infty$ gives $N_{t,n} \to \infty$ for each fixed $n \ge n_0$, countable diagonal extraction yields limits $\nu_n(w,k) \in [0, 1]$, passing to the limit in Lemma 2 and subtracting the fixed-point identity gives $|\Delta_n| \le \frac{2}{3} D_{n+1}$ ($L=2$), $\le \frac{1}{3} D_{n+1}$ ($L=3$), or $= 0$ ($L \ge 4$), forcing $\Delta_{n_0} \equiv 0$. Hence $\lim_{N\to\infty} \nu_{n_0}(w_0, k_0, N) = f(w_0)$. Completely airtight!
4. **Section 3 & Proposition 2 (lines 87–106):**
   - Bit-complement commutation $\psi_r(\bar{w}) = \overline{\psi_r(w)}$ holds for all $r, w$, yielding $f(\bar{w}) = f(w)$.
   - Involutions $\sigma(m) = 3M + 1 - m$ and $\tau(j) = 2M - j$ satisfy $S(\sigma(m)) = \tau(S(m))$ and $\varepsilon(\sigma(m)) = \varepsilon(m)$ on all three residue classes mod $3$, yielding $\psi_{r'}(w^R) = (\psi_r(w))^R$ with bijection $r' = (2 - r - L) \bmod 3$. At $L = 3$, $r' = 1 \leftrightarrow r = 1$ and $\psi_1^2 = \mathrm{id}$ give $f(w^R) - f(w) = \frac{1}{9}(f(w^R) - f(w)) \implies f(w^R) = f(w)$; $L \ge 4$ follows immediately by induction. Completely airtight!
5. **Section 4 — Transfer to $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (lines 110–120):**
   - Sliding-block decomposition with $m_r = \lceil (r+L)/3 \rceil$ and $r' = 3m_r - (r+L) \in \{0, 1, 2\}$ satisfies $m_{r'} = m_r$, bijection $r \mapsto r'$, palindrome property $(\varphi(u))^R = \varphi(u^R)$, and complement property $\overline{\varphi(u)} = \varphi(\bar{u})$, yielding existence, explicit rationality, reversal invariance, and bit-complement invariance of $\mathrm{freq}_{\mathbf{t}'}(w)$ for all $w \in \{0, 1\}^*$. Completely airtight!

---

## 3. Independent Mechanical Verification

Reran `check-2`'s independent exact-arithmetic verifier (`targets/cassaigne-2602.21895-conjC4/notes/check-check-2.py`):
```sh
/usr/bin/time -p .venv/bin/python -u targets/cassaigne-2602.21895-conjC4/notes/check-check-2.py
```
Raw output (`notes/audit-helper-cassaigne.md` §3.1):
```text
Primary-source prefixes (t_{3/2} len 17, t' len 25) match merge_version.tex verbatim: PASS
Lemma 1 (preimage lengths l_0, l_1, l_2 for 2 <= L <= 50): PASS
Lemma 2 (exact desubstitution recurrence C_n(w,k,N), |E|<=3L+3 for 2<=L<=5, N<=10000): PASS
Exact Fraction frequencies & rev/comp symmetries (t_{3/2} 1<=L<=9, t' 1<=L<=7; L=2 values): PASS
Empirical density agreement on t_{3/2}[0..100000) and t'[0..300000) (L<=5, filtered n<=2): PASS
PASS (all checks passed in 1.075s)
```
Exit code `0`, `1.18s` wall-clock.

---

## 4. Deep Novelty Check

Verified independently in `notes/audit-helper-cassaigne.md` §2 (through `2026-11-27T05:45Z`), plus Gate 2 receipts `notes/novelty-gate2-watch-{5,6}.md`:
- Live OEIS `A357448` (rev. 20, `2026-03-04`): still marks factor frequencies as Conjecture `(II)`.
- arXiv (`2602.21895v1` sole version; checked Berthé–Cecchi-Bernales–Espinoza `2602.04833v2` §6 `V5.tex` directly — computes additive continuous eigenvalues only, does not prove unique ergodicity or factor frequencies), Crossref, Zenodo, web search, `522` local snapshots, `the-omega-institute/trureturing*` (`dekking-keane-2022` covers `arXiv:2202.13548v1` single-letter frequency only), and 15+ competing GitHub repos: `0` prior proofs of `(C_4)` for $|w| \ge 2$ or reversal symmetry.

### What Is Not Established / Caveats
- Relies on Theorem `thm:existence_freqs_iff_mun_exist` of `arXiv:2602.21895v1` (Cassaigne–Espinoza–Rigo–Stipulanti, 2026) for the $L = 1$ base case $\lim_{N\to\infty} C_n(a,k,N)/N = 2^{-n-1}$, and Lemma `lem:morphic_image` of the same paper for $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$. (As noted in `notes/audit-helper-cassaigne.md` §1.3, `merge_version.tex` line 1995 has a harmless notational omission of a $3^{2k}$ factor inside an invariant $\sup$ in their $L=1$ proof.)
- Proves existence, explicit rationality, reversal invariance, and bit-complement invariance of all factor frequencies (i.e., Conjecture `(C_4)` for both $\mathbf{t}'$ and $\mathbf{t}_{3/2}$); does not prove uniform convergence (unique ergodicity of the subshift) or characterize which words have nonzero frequency.
- Live OpenAlex and Semantic Scholar APIs returned HTTP 429 during audit (and the local OpenAlex cache had mapped `2602.21895` to an unrelated ID `W7225298642`), so automated OpenAlex/S2 citation-graph queries were not available; private repositories and unindexed off-arXiv works were not covered.
- Internal audit and finite exact checks are not formal peer review or a Lean 4 formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`. Pending Gate 3 novelty clearance prior to coordinator report.
