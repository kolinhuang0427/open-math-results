# Check Report — `iverson-2506.20778-conjPaley`

- Checker: `check-1`
- Checked UTC: `2026-11-27T07:02:27Z`
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source: `arXiv:2506.20778v1` (published `2025-06-25T19:09:29Z`, sole version), `tools/.arxiv_cache/eprint/2506.20778/2025.06.25.tex`:
  - Section 1 (`defn:SIC`, lines 50–68): sesquilinear form $(x, y) = x^* y$ and $(a, b, c)$-SIC axioms (a)–(d).
  - Section 2 (`thm.main` Theorem 2, `lem.gram matrix` Lemma 3, lines 87–172): $(12, 16, 96)$-SIC $x_{ij} = h_j \circ (\mathbf{1} + z e_i)$ ($z = -2(1+\mathrm{i})$) and exact Gram matrix cases I, II, III.
  - Section 3 (`Definition 11`, `Definition 13` / `defn:SIC equivalence`, `thm:sandwich` Theorem 15, `lem:omegas` Lemma 16, `prop:AutCompute` Proposition 17, lines 334–762): $\mathrm{Aut}_w(H)$, $\mathrm{Aut}_s(\tilde{H})$, $\tilde{H}_{(i,j),(k,l)} = H_{k,j} H_{i,l}$, $\iota(\mathrm{Aut}_w(H)) \le \mathrm{Aut}_s(\{x_{ij}\}) \le \mathrm{Aut}_w(\{x_{ij}\}) \le \mathrm{Aut}_s(\tilde{H})$, and Kantor (1969) reference (line 820).
  - Section 4 (`conj:Paley` Conjecture 22, lines 829–840): exact verbatim statement of parts (a) and (b).
- Comparison against `TARGET.md` and `PROOF.md`: exact match with zero quantifier, hypothesis, edge-case, or definition drift (including all internal theorem/lemma/definition numbering verified directly in `2025.06.25.tex`).

## 2. Independent Mechanical Verification

- Verifier script: `targets/iverson-2506.20778-conjPaley/notes/check-check-1.py` (written strictly from `2025.06.25.tex` definitions and `PROOF.md`, without reading `verify.py` or author `notes/`).
- Verified directly in exact finite-field and integer arithmetic:
  1. **Lemma 1 ($q \in \{19, 23, 27=3^3, 31\}$):** Paley I matrix identities ($S^\top = -S$, $H^\top = 2I - H$, $HH^\top = dI$, $S^2 = -qI$, $H^2 = 2S - (q-1)I$, zero row sums on $\mathbb{F}_q$), Galois invariance $\chi(a^3) = \chi(a)$ on $\mathbb{F}_{27}$, and $P\Gamma L(2,q)$ action formula $H_{g(a),g(b)} = \varepsilon_a \varepsilon_b H_{a,b}$ (for $\eta(g)=+1$) or $\varepsilon_a \varepsilon_b H_{b,a}$ (for $\eta(g)=-1$).
  2. **Lemma 2 & Lemma 4 ($q=19, 23, 27$):** $\Delta$-signature inner products $\langle v_{ij}, v_{ji} \rangle = d - 4$ and $|\langle v_{ij}, v_{uv} \rangle| \le 2\sqrt{q}+4 < d - 4$ across all off-diagonal pairs; exhaustive $T_4^{\mathrm{col}}(\infty, 0, r_1, r_2)$ check at $q=19$ confirming $16$ orbits of $(F_{19}^\times)^2$ in $\{\pm 4\}$, unique orbit $\{1, 12\}$ with $+12$, exact matching of $R_1 \cap R_3$, $R_3 \setminus R_1$, $R_1 \setminus R_3$ for both signs, and elimination of all $190$ column pairs across all $(i_1, i_3)$ choices.
  3. **Theorem 2 & Non-Transitive SICs ($(q,p) \in \{(19,3), (31,3), (83,19), (343=7^3, 7)\}$):** Exact SIC construction in $\mathbb{F}_{p^2}^d$, full Gram matrix / `lem.gram matrix` Cases I–III / Definition 1(a)–(c) check for $q=19, p=3$, spanning rank $d$ over $\mathbb{F}_{p^2}$ via Gaussian elimination ($d \le 90$), exact Step 1 conjugation relation $\bigl(x_{\pi(i,j)}, x_{\pi(k,l)}\bigr) = \omega_{i,j}\omega_{k,l}\overline{(x_{i,j},x_{k,l})}$ on all $400^2$ pairs for $q=19, p=3$, and Step 2 triple products $T(u_1,v_1,w_1) = 64 \not\equiv 0$ and $T(u_2,v_2,w_2) = \pm 64\mathrm{i} \not\equiv 0$ over $\mathbb{F}_{p^2}$ (for all $4$ pairs $(q,p)$, including $p=3$ and prime-power $q=343=7^3$).

### Command & Raw Output

```bash
.venv/bin/python -u targets/iverson-2506.20778-conjPaley/notes/check-check-1.py
```

Raw output (exit code `0`):
```text
Lemma 1 (Paley I properties & PGammaL(2,q) embedding, q=19,23,27,31): OK
Lemma 2 & Lemma 4 q=19 (Hasse bounds, T4^col orbits, 190 col-pair eliminations): OK
Theorem 2 SIC & Aut_s != Aut_w (q=19/p=3, q=31/p=3, q=83/p=19, q=343/p=7): OK (49.79s)
PASS
```
