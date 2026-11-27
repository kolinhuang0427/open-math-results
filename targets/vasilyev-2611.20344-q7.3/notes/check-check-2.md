# Check Report: `targets/vasilyev-2611.20344-q7.3/` (`@check-2`)

**Verdict:** `PASS` (exact verification against `arXiv:2611.20344v2` `updown.tex`; zero floats).

## 1. Primary-Source Alignment (`arXiv:2611.20344v2`)
- Verified verbatim against `tools/.arxiv_cache/eprint/2611.20344/updown.tex`:
  - Section 1 (`\N = {1, 2, 3, ...}`, `U(x) = \ceil{3x/2}`, `D(x) = \ceil{x/2}`, `T_S`), Section 2 (`Lemma 2.1` `lem:steps`, `Definition 2.2` `def:G`, `Proposition 2.3` `prop:dict`), Section 4 (`Remark 4.4` `rem:types`), and Section 7 (`Question 7.3` `q:types`, lines 1991–1993: *"Is there a map with infinitely many cycles and a divergent orbit (Remark 4.4)?"*).
- **Gate 2 status:** `PASS` (`#1482` `watch-1`, `#1483` `watch-6`, `#1485` `watch-5`; receipts in `targets/vasilyev-2611.20344-q7.3/notes/novelty-gate2-watch-{1,5,6}.md`).

## 2. Independent Exact Verifier (`check-check-2.py`)
Executed `.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/notes/check-check-2.py` (pure exact integer arithmetic, zero floats, `Command exited with code 0`):
- **Elementary identities & Lemma 1 (Closed-Box Trap Lemma):** Verified $\mathrm{Im}(U) \cap [1, 2000] = \{z \in [2, 2000] : z \not\equiv 1 \pmod 3\}$, monotonicity/bounds on $U$ and $D$, and all trap box bounds $B+1 < C-1 < 2B < 3B-1$ for every $B \equiv 5 \pmod 6$ in $[5, 600]$.
- **Lemma 3 (Admissible Stage Extension):** Independently implemented Phase 1 / Phase 2 (`A`, `B1`, `B2a`, `B2b`, `B3a`, `B3b` loop) / Phase 3 and exhaustively verified on all $9{,}996$ heads $H \in [5, 10000]$ (branch distribution `{'A': 4995, 'B3a': 836, 'B2b': 1268, 'B2a': 1239, 'B1': 1658}`, max `B3b` depth `4`, plus targeted high-$v_2(5q+3)$ adversarial tests): admissibility, pairwise distinctness, $> H$, gap clearance $P \cap [B+1, C-1] = \emptyset$, and $H' = \max(P) > 3B$ all hold.
- **15-stage global construction & exhaustive $T_S$ simulation:** Built $P_0 = (1, 2, 3, 5)$ through Stage $15$ ($H_3 = 1{,}182{,}213$), verified global $U$-invariance of $\mathbb{N} \setminus R$ on $[1, H_2]$, verified strict disjointness across all $15$ intervals $[B_m+1, 3B_m-1]$, verified exhaustive Lemma 1 invariants on Stages 1–2, extracted exact simple cycles $C(B_1), \dots, C(B_4)$ (lengths `43, 363, 10857, 35752`), and classified every starting integer $x \in [1, 1{,}182{,}213]$ under $T_S$ (`ray_basin=327659`, `cycle_basins=[680166, 157196, 17192]`, sum $= 1{,}182{,}213$, zero anomalies).
