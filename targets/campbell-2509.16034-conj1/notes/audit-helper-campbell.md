# Audit Helper Report: `targets/campbell-2509.16034-conj1/`

- **Checked UTC**: 2026-11-27T01:44:26Z
- **Scope**: Rescoped Open Problems (c1) (explicit sign of $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$) and (c2) (explicit recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$, full recursion, and $2$-regularity) of Campbell–Currie–Rampersad (`arXiv:2509.16034v1`, *INTEGERS* 26 (2026) #A34).
- **Isolation**: Did not read `verify.py` or `notes/screen-*`; did not edit `TARGET.md` or `PROOF.md`.

---

## 1. Independent Rerun of `notes/check-check-1.py`

Command:
```sh
/usr/bin/time -p .venv/bin/python targets/campbell-2509.16034-conj1/notes/check-check-1.py
```

- **Exit code**: `0`
- **Runtime**: `real 3.09`, `user 2.27`, `sys 0.13`
- **Exact raw output**:
```text
Direct factor enumeration (1<=n<=120), paper prefix (1..19), Lemma 2/3, & Theorem 1 (1<=n<=20000): OK
2-kernel sizes: alpha=9, beta=10, alpha_{k+1}=8, beta_{k+1}=8
Rescoped Theorem 1 (odd/4n/4n+2 recurrences, 8-state 2-kernel, 2-regularity, unboundedness): OK
Rescoped Theorem 2 (exact sign, nonzero formula 2b_{n+1}-1, strong induction 1<=n<=4999): OK
PASS
```

---

## 2. Exact 8-State $2$-Kernel & DFAO Verification

Using $a'_k := m_{k+1} \bmod 2$ and $b'_k := M_{k+1} \bmod 2$ for $k \ge 0$ (so $a'_0=0, b'_0=0, a'_1=0, b'_1=1, a'_2=1, b'_2=0$):

1. **Four shifted identities ($0 \le k \le 5000$)**:
   - Tested $a'_{2k} = b'_k$, $b'_{2k} = a'_k$, $a'_{2k+1} = 1 - b'_{k+1}$, and $b'_{2k+1} = 1 - a'_k$ directly from the Lemma 2 recursion up to $N = 20010$.
   - Result: **0 exceptions** across all $0 \le k \le 5000$, including $k=0$ ($a'_0=b'_0=0$, $b'_0=a'_0=0$, $a'_1=0=1-b'_1$, $b'_1=1=1-a'_0$) and $k=1$.

2. **Exact closure of the 8-element set**:
   - States `(seq, shift, polarity)` representing $a'_k, b'_k, a'_{k+1}, b'_{k+1}, 1-a'_k, 1-b'_k, 1-a'_{k+1}, 1-b'_{k+1}$ close exactly under $k \mapsto 2k$ and $k \mapsto 2k+1$ (verified both symbolically and numerically for all $0 \le k \le 2500$):

| State | On bit `0` ($k \mapsto 2k$) | On bit `1` ($k \mapsto 2k+1$) | Output at $k=0$ |
|---|---|---|---|
| `('a', 0, +1)` ($a'_k$) | `('b', 0, +1)` | `('b', 1, -1)` | `0` |
| `('b', 0, +1)` ($b'_k$) | `('a', 0, +1)` | `('a', 0, -1)` | `0` |
| `('a', 1, +1)` ($a'_{k+1}$) | `('b', 1, -1)` | `('b', 1, +1)` | `0` |
| `('b', 1, +1)` ($b'_{k+1}$) | `('a', 0, -1)` | `('a', 1, +1)` | `1` |
| `('a', 0, -1)` ($1-a'_k$) | `('b', 0, -1)` | `('b', 1, +1)` | `1` |
| `('b', 0, -1)` ($1-b'_k$) | `('a', 0, -1)` | `('a', 0, +1)` | `1` |
| `('a', 1, -1)` ($1-a'_{k+1}$) | `('b', 1, +1)` | `('b', 1, -1)` | `1` |
| `('b', 1, -1)` ($1-b'_{k+1}$) | `('a', 0, +1)` | `('a', 1, -1)` | `0` |

3. **LSD DFAO verification ($1 \le n \le 4999$)**:
   - Reading the binary expansion of $n$ least-significant bit first from `('a', 0, +1)` and `('b', 0, +1)` through the 8-state transition table above (evaluating `out0` at termination) reproduces $(a'_n, b'_n) = (a_{n+1}, b_{n+1})$ and $b_{n+1} - a_{n+1} = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$ for **all** $1 \le n \le 4999$ with **0 mismatches**. (Note: the joint pair `(st_a, st_b)` automaton tracking $(a'_n, b'_n)$ simultaneously has $24$ reachable state pairs.)

---

## 3. Novelty Check (Newly Discovered Repos, Zenodo, Crossref, Web)

All searches below were read-only (`gh api`, `gh search`, `curl`, web search). **No solution to Open Problems (c1) or (c2) was found.**

| Source | Method / Queries | Findings | Relevance to (c1)/(c2) |
|---|---|---|---|
| `rainwangphy/aftd-platform` | `gh search` + full `git/trees/HEAD?recursive=1` grep (`campbell\|currie\|rampersad\|reduced\|thue\|2509\|abelian`) | Has `CampbellHowardConditions.lean` and `ThueMorseMinFactorCoveragesFinset.lean` / `ThueMorseRandomAttractorProb.lean` / `ThueMorseUnhitMean.lean`. | Unrelated topics (Campbell–Howard conditions, factor coverage / random attractors); 0 matches for `2509.16034` or reduced abelian complexity. |
| `valyuAI/research` | `gh search` + full tree grep | `s03_thue.mp3` (Cartesian-tree square-free words), `max_reduced_order.py` (spectral graph theory). | Unrelated; 0 matches. |
| `facebookresearch/atlas-lean` | `gh search` + full tree grep + `gh api` file inspection of `ReducedComplexities.lean`, `ReducedComplexitiesWanted.lean`, `ThueMorseReducedComplexity.lean`, `blueprint/.../reduced-factor-complexity/` | Formalizes Campbell–Currie–Rampersad results on $\rho^{\mathrm{red}}_{\mathbf{t}}$ (`rhoRed_thueMorse_odd`, `rhoRed_thueMorse_even`, `minAlt_maxAlt_two_mul`, `minAlt_maxAlt_four_mul`) and $\rho^{\mathrm{red}}_{\mathbf{f}}, \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{f}}$ for the paperfolding word (Theorem 3). | **Does not settle (c1) or (c2):** no theorems on $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}$. |
| `JENW1N/complete-math-solutions` | `gh search` + full tree grep | 0 matches for `campbell\|currie\|rampersad\|reduced\|thue\|2509\|abelian`. | Clear. |
| `TheJustinSunPrize/awards` | `gh search` + full tree grep + `gh api` issues search (`2509.16034`, `Campbell+abelian`, 100 recent issues) | 0 tree matches; 0 matching issues. | Clear. |
| `the-omega-institute/trureturing-mdbook` | Full tree grep + `gh api search/issues` (`2509.16034`, `reduced abelian`) | PR #5 (`Make the open problems page answer its own question`, closed) links to `the-omega-institute/trureturing`'s existing `ThueMorseReducedAbelianOdd.md` (`reducedAbelianComplexity_odd`, frozen 2026-09-06). `trureturing` tree check shows only `ThueMorseReducedAbelianOdd.lean` and `ThueMorseReducedAbelianEven.lean` (prior art already explicitly credited and excluded in `TARGET.md`/`PROOF.md`). | **Does not settle (c1) or (c2):** only cites the already-known Sept 2026 odd-index and `displayconjecture` results. |
| Zenodo API (`zenodo.org/api/records`) | `q=2509.16034`; `q="reduced abelian complexity"` | `total: 0` on both queries. | Clear. |
| Crossref API & Web Search | `query=Reduced complexities for sequences over finite alphabets`; `query.bibliographic=2509.16034`; web search for `"2509.16034" OR "reduced abelian complexity" "Thue-Morse" "INTEGERS" 2026 "A34"` and follow-ups | Confirms `arXiv:2509.16034` and publication in *INTEGERS* 26 (2026) #A34; 0 Crossref hits for the paper or any citing/subsequent work resolving (c1) or (c2). | Clear. |
