# Blind Audit: `dawar-2611.23541-sym-depth`

- **Auditor:** `@audit-2` (`auto`)
- **Target:** `targets/dawar-2611.23541-sym-depth/`
- **Primary Source Verified Verbatim:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *"Depth Hierarchies for Symmetric Algebraic Circuits"*, `arXiv:2611.23541v1` (`cs.CC`, Nov 17, 2026), Section 1.2 (*"Future work"*), `introduction.tex` lines 269–271, together with `prelims.tex`, `app-vsbr.tex`, and `app-circuits-from-patterns.tex` extracted directly from `tools/.arxiv_cache/eprint/2611.23541.src`.
- **Verdict:** **PASS**
- **Charter Publication Label:** `written proof, internally audited`

## File Fingerprints Verified
- `TARGET.md`: `aaec6887970d06a873d9cb1129174af0`
- `PROOF.md`: `f5494a09b2e1cb11c33c20818e182a73`
- `notes/check-check-1.md`: `37b8ce33ef10784bffad2e4f72331782`
- `notes/check-check-1.py`: `8ad034d85e62bca0bd317ca0212003d7`

## Audit Summary

### 1. Statement Fidelity
- `TARGET.md` reproduces `introduction.tex` lines 269–271 of `arXiv:2611.23541v1` verbatim and accurately frames the Section 1.2 open problem asking whether matrix-symmetric algebraic circuits can be reduced to depth $3$ or $4$, and at what cost in orbit size.
- The circuit model (`prelims.tex` L7 unweighted `+`/`\times` gates vs standard algebraic-complexity weighted linear-combination $\Sigma$-gates in `[KKS16, Tavenas15]`) is faithfully tracked throughout Theorems 1–4.

### 2. Mathematical Verification
- **Theorem 1 (`PROOF.md` L16–21):** Fixed cleanly from Re-Audit 1 — depth $\le 4$ ($\min\{d, n/2\} \ge 81$, exponent $1/4$) and depth $\le 3$ ($\min\{d, n/2\} \ge 27$, exponent $1/3$) now carry exact separate thresholds ensuring $k + 1 = \lfloor \min\{d, n/2\}^{1/\Delta} \rfloor \ge 3$, $k \ge 2$, and $4(k+1) \le 4(n/2)^{1/3} \le n$ for $n \ge 54$, matching `lem:path-lower` (`app-vsbr.tex`).
- **Lemma 1 (`PROOF.md` L23–32):** Group-action proof over $S_n \times S_n$ checked line-by-line: $|U| \ge n - k \ge 5$, $|W| \ge n - 2k > r$, Pigeonhole yields distinct $w_1, w_2 \in W$ with $3$-cycle $\tau_1 \tau_2 = (v\ w_2\ w_1)$ fixing $h_t$, $A_U$ and $(v\ w_2\ w_1)$ generate $A_{U \cup \{v\}}$, and right-to-left composition $(v\ w)(w\ w') = (v\ w\ w')$ gives $(v\ w)(h_t) = h_t$ for all $w \in U$, contradicting minimality of $\sup(h_t)$.
- **Theorem 2 (`PROOF.md` L34–39):** Under $n \ge 28$, $9 \le d < n/3$, gate degrees $\le d$, and $3\kappa_f(n) \le n + 2$, $\Gamma_n$-equivariant same-type collapse + constant/zero-gate collapse + `lem:reduction` gives strictly alternating homogeneous $C''$ with $\operatorname{maxsup}(C'') \le k = \kappa_f(n) - 1 \le (n-1)/3$, every $\Pi$-gate fan-in $r \le d$, $r + 2k \le (n-1)/3 + 2(n-1)/3 = n - 1 < n$, and $n - k \ge 19 \ge 5$; Lemma 1 yields $\mathrm{supp\text{-}depth}(C'') \le 2$ and `lem:path-lower` at $\Delta = 2$ gives orbit size $\ge \binom{n}{\lfloor \sqrt{d}\rfloor} = 2^{\Omega(\sqrt{d}\log n)}$.
- **Lemma 2 (`PROOF.md` L45–56):** Normalised decomposition $(T, \beta)$ with $|V(T)| \le |V(F)| + 1$ has empty root $r_0$ deleted before arbitrary reconnection and binarization ($|V(T)| \le 4d$), edge-splitting adds $< d/r$ nodes ($|V(T)| \le 5d$, max degree $\le 3$, $W \le 6d$). Both $W \le 2r$ ($S = \emptyset$) and $W > 2r$ (fixed-root deepest-subtree deletion giving pairwise disjoint weight-$>2r$ subtrees, $|S| \le \lfloor W/(2r+1)\rfloor \le 3\sqrt{d}$, $\le 2|S| + 1 \le 6\sqrt{d} + 1$ components of weight $\le 2r$) plus `lem:normalised-decomposition` Items 2–4 pruning are exact for all $d \ge 1$ (including non-squares, with $2\lceil\sqrt{d}\rceil \le 3\sqrt{d}$ verified for all $d \ge 1$).
- **Theorem 3 (`PROOF.md` L58–67):** Uses $\kappa = \kappa_{\max\{s(n), n^2\}}(n)$, `cor:vsbr` ($\operatorname{tw}(F) \le \kappa - 2$), and Lemma 2 to construct a depth-$\le 4$ ($\Sigma\Pi\Sigma\Pi$) matrix-symmetric circuit in `prelims.tex` L7's exact unweighted `+`/`\times` convention (absorbing $\alpha_F$ into Layer-2 $\Pi$-gates, handling $S = \emptyset$ at depth $2 \le 4$), homogeneous below top $\Sigma$-gate (and fully homogeneous whenever $p_n$ is homogeneous), with orbit size $\le \min\{n^{O(\kappa\sqrt{d(n)})}, (n!)^2\}$ and support depth $\le 2$ whenever $6\kappa\sqrt{d(n)} < n/2$.
- **Theorem 4 (`PROOF.md` L73–94):** Explicitly descends coefficients to $\mathbb{Q}$ via a $\mathbb{Q}$-linear projection $\tau: \mathbb{K} \to \mathbb{Q}$ ($\tau(1) = 1$), handles $a = 0$, applies $\Gamma_n$-equivariant half-sum Fischer expansion + truncated exponential $f_{a,b}(y)$ at $z_q = q^b$ + Lagrange interpolation over $\overline{\mathbb{K}}$, and descends to $\mathbb{Q}$ via $L = \mathbb{Q}(\zeta_{2b}, \alpha_1^{1/b}, \dots, \alpha_a^{1/b}) = \mathbb{Q}(\theta)$ ($[L:\mathbb{Q}] \le 2b \cdot a! \cdot b^a = 2^{O(\sqrt{d}\log d)}$) and $[t^0](\cdot \bmod \mu_\theta(t))$ interpolation. Model depth is accurately stated as depth $3$ ($\Sigma\Pi\Sigma$) with weighted linear-combination $\Sigma$-gates (`[KKS16, Tavenas15]`) and depth $4$ ($\Sigma\Pi\Sigma\Pi$ with fan-in-$2$ bottom scalar $\times$-gates) under `prelims.tex` L7's unweighted model.

### 3. Independent Exact-Arithmetic Verification
- Executed `.venv/bin/python -u targets/dawar-2611.23541-sym-depth/notes/check-check-1.py`: exit code `0`, AST-verified `0` float constants and `0` `float()` calls:
  ```
  Theorems 1-2 thresholds & Lemma 1 S_n generation: PASS
  Lemma 2 balanced 2-level decomposition + normalised pruning (d=1..100 incl. non-squares): PASS
  Theorem 3 depth-4 circuit & Gamma_n-invariance (P_4, P_5): PASS
  Theorem 4 Fischer + truncated exp + Q[t]/(mu) interpolation descent: PASS
  PASS
  ```

## Handoff
- Passed blind audit; handed off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including arXiv, GitHub, ECCC, and complexity venues).
