# Independent Check Report: `godard-2605.21866-prob3`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2605.21866/godard-reis.tex` (`arXiv:2605.21866v1`, 2026-05-21):
  - Definition (`line 100`), $Q_b(X,Y) := X^2 + bXY + Y^2$ with $b \in \mathbb{F}_{q^n}^*$ (`line 114`), and Section 5 Problem 3 (`lines 363–368`) match `TARGET.md` and `PROOF.md` verbatim.
  - Note on minor parenthetical label numbers in `PROOF.md` (purely editorial; `PROOF.md` proves all cited facts self-containedly): because `godard-reis.tex` shares the `[theorem]` counter across theorems, lemmas, and remarks (`lines 31–42`), `rem:disc` is Remark 1.6 (cited as `Remark 1.2` on `PROOF.md` L31), `lem:indicator` is Lemma 2.3 (`Lemma 2.1` on L45), `lem:boundaffine` is Lemma 2.4 (`Lemma 2.2` on L48), and `lem:GS` is Lemma 2.5 (`Lemma 2.3` on L54).

## 2. Proof & Independent Mechanical Verification
- Checked all sections of `PROOF.md`:
  - **Section 1:** Explicit disconnections at $\dim_{\mathbb{F}_q} V = n/p_0(n)$ for all $n \ge 4$, odd $q \ge 3$ (even $n$: nonsquare coset $\alpha\mathbb{F}_{q^{n/2}}$ isolates $0$; odd $n$: subfield $\mathbb{F}_{q^{d_0}}$ with $b \in \mathbb{F}_{q^{d_0}}^*$ is closed under edges since $2 \nmid p_0$).
  - **Section 2:** Exact character-sum bound gives $\#A \ge q^{2k} - 2q^{2k-1} + 2q^k > \frac{1}{2}q^{2k}$ for all even $n = 2k \ge 4$ and odd $q \ge 5$.
  - **Section 3:** Odd $n \ge 5$, $b = \pm 2$ handled via $S_V$, Weil's bound on $N(v_1 + tv_2)$, and Kummer theory over $\overline{\mathbb{F}_q}(t)$ ($\mathrm{Gal} \cong (\mathbb{Z}/2\mathbb{Z})^n$).
  - **Section 4:** Odd $n \ge 5$, $b \notin \{0, \pm 2\}$ proved via diagonalization, Lemma 4.1 (pairwise independence of $L_i$), Lemma 4.2 (normality of $R$ via $R_1 + S_2$, flatness of $p_1, p_2$), Lemma 4.3 (Jacobian rank growth to $n$ by $k_0 = n - s + 1$, separability, Bézout bound $d_{k_0} \le 2^{k_0(n-s)}$), Lemmas 4.4–4.7 (DVR base-change étaleness, purity + $\tau_i$ unramifiedness, Kummer coordinate-line triviality, EGA IV$_3$ descent forcing $d_K = 1$ by $K = (n-s+1)^2$), and Theorem 4.9 (Noetherian induction over $\mathbb{Z}[1/2]$ + Schwartz–Zippel + Lang–Weil).
- Wrote independent exact-arithmetic verifier `targets/godard-2605.21866-prob3/notes/check-check-1.py` (pure `int` and $\mathbb{F}_{p^n}$ arithmetic, zero floats, without reading `verify.py` or author notes).
- Command: `.venv/bin/python targets/godard-2605.21866-prob3/notes/check-check-1.py`
- Results (`PASS`):
  - **Check 1:** Verified Section 1 disconnections for even $(n,p) \in \{(4,3),(4,5),(6,3),(8,3)\}$ and odd $(n,p) \in \{(5,3),(5,5),(7,3),(9,3)\}$, plus exact subfield closure for $(15,3)$.
  - **Check 2:** Verified even-$n$ integer inequality for $k \in [2, 20]$, $q \in \{5,7,9,11,13,17,19,25\}$ and BFS connectedness on $\mathbb{F}_{5^4}$ and $\mathbb{F}_{3^6}$.
  - **Check 3:** Verified odd-$n$ threshold inequality ($n=5..23$) and $b = \pm 2$ primitive ratio, Weil bound, $\mathrm{span}(S_V) = \mathbb{F}_{q^n}$, and BFS connectedness on $\mathbb{F}_{5^5}$ and $\mathbb{F}_{7^5}$.
  - **Check 4:** Verified Lemma 4.1 over $\mathbb{F}_{5^5}, \mathbb{F}_{3^7}, \mathbb{F}_{3^9}$; $\tau_i$ identity and Lemma 4.3 Jacobian rank growth reaching $\dim U_{k_0} = n$ over $\mathbb{F}_{1000003}$ for $(n,s) \in \{(5,2),(7,2),(9,4)\}$; and BFS connectedness on $\mathbb{F}_{5^5}$ ($s=2$) and $\mathbb{F}_{3^7}$ ($s=3$).

## 3. Gate 2 Novelty Status
- Gate 2 passed (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`). Ready for blind audit.
