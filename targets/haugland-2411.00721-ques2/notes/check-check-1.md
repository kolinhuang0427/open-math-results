# Independent Check Report: `haugland-2411.00721-ques2`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2411.00721v2/haugland-omland-reversible-v2.tex` (`arXiv:2411.00721v2`, updated 2026-11-01):
  - Definitions of induced shift-invariant map $F \colon \mathbb{F}_2^n \to \mathbb{F}_2^n$, diameter $k$ (depends on both $x_1$ and $x_k$), $(k, n)$-lifting, and proper lifting (`lines 89–95`) match `TARGET.md` and `PROOF.md` exactly (index shift $x_r^{\text{new}} = x_{r+1}^{\text{old}}$ is cleanly accounted for).
  - Section 2 Question (`lines 327–331`, numbered 2.3 under `[theorem]` counter after 2.1 Prop and 2.2 Question) and Section 4 Open Problem (iii) (`line 455`) match `TARGET.md` verbatim.
  - Note on scope: `PROOF.md` settles Question 2.3 and the existence part of Open Problem (iii) in the negative; the secondary question in Open Problem (iii) ("what is the minimal possible degree as a function of diameter?") is explicitly noted as out of scope.
  - Proposition references in `PROOF.md`: `Proposition 1.2` (`line 108`, affine proper iff diameter 1) and `Proposition 1.5` (`line 133`, referenced inside Question 2.3 quote) match the `[theorem]`-numbered environments in Section 1 (`lines 108, 114, 133, 165, 175, 219, 245` — wait: if Proposition 1.1 is at line 108, that's minor label drift in the prose citation `Proposition 1.2` at `PROOF.md` line 40, while the quoted mathematical fact itself — "An affine Boolean function is a proper lifting if and only if it has diameter 1" — is verbatim at line 109).

## 2. Independent Mechanical Verification
- Wrote independent exact-arithmetic $\mathbb{F}_2$ / polynomial verifier `targets/haugland-2411.00721-ques2/notes/check-check-1.py` directly from primary source definitions and `PROOF.md` (zero floating-point arithmetic, without reading `verify.py` or author notes).
- Command: `.venv/bin/python targets/haugland-2411.00721-ques2/notes/check-check-1.py`
- Results (`PASS`):
  - **Check 1:** Verified $2k \le N \le 4k - 4$ and $2^t + k - 1 < N$ for all $2 \le k \le 500$ and $0 \le t \le s_{\max} = \lceil \log_2 k \rceil$.
  - **Check 2:** Verified Eq. (3) $(w+1)\sum_{t=0}^{L-1} w^t = (w+1)^L$ in $\mathbb{F}_2[w]$ for $L = 2^0, \dots, 2^5$.
  - **Check 3–5:** Implemented Lemma 3's explicit polynomial ring formula $X(z) = z^{k-1} R(z)^{-1} (z+1)^{N - 2^s - e} \widetilde{V}(z) \pmod{z^N + 1}$ and Theorem 1's double-induction witness construction (checking Eqs. (1), (2), (6), (8), and $w_m = \binom{P-1-e}{m} \bmod 2$ at every step). Verified explicit collisions $F_N(x+u) = F_N(x)$ ($u \neq 0$) on:
    - Exhaustive $k=2$ (all $8$ degree-2 functions) and $k=3$ (all $112$ degree-2 functions);
    - $k=4$ (all $63$ nonzero $Q \times 16$ linear/constant choices = $1008$ functions);
    - $k=5..12$ ($100$ random diameter-$k$ degree-2 functions each = $800$ functions).
  - **Check 6 (Section 4 Sharpness):** For $f_m$ at $m=1,2,3$ ($k=4,6,10$), verified $f_m$ has diameter $k$, $F_{2^{m+1}}$ is an involution (exhaustive bijection check for $m=1,2$; $2000$ random inputs for $m=3$), and Theorem 1 constructs a genuine collision at $N = 2^{m+2}$.

## 3. Gate 2 Novelty Status
- Not yet present in `targets/haugland-2411.00721-ques2/notes/` (`watch-1`/`watch-5`/`watch-6` queued in #20). Pinging `@watch-1` alongside audit handoff.
