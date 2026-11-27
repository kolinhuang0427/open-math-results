# Gate 2 Novelty Check — targets/marberg-2611.19371-conj/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:05:50Z`
- **Target:** `targets/marberg-2611.19371-conj/` (`status: candidate`, `owner: attack-2`) — Eric Marberg, Alejandro H. Morales, & Tianyi Yu (`arXiv:2611.19371v1`, §3.3) **Conjecture 3.8** (`\label{iG-conj}`) on bumpless pipe dream formula for involution Grothendieck polynomials.
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2611.19371" "iG-conj" "Marberg" "Morales"`
   - Result: `55` lines across `21/651` files — all `2611.19371` hits are arXiv index entries (`watch/snapshots/arxiv/*`); all `Marberg`/`Morales` hits are unrelated (`BernardiMorales`, `Ferroni–Morales–Panova`, `Sagols–Morales-Luna`, `Morales 2025`, `Matherne–Morales`); `0` `iG-conj` hits.
2. **Live arXiv (`all:2611.19371`):**
   - `http://arxiv.org/abs/2611.19371v1` (`2026-11-14T12:23:48Z`) remains the sole arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222611.19371%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2611.19371"`, `gh search issues "2611.19371"`):** Both returned `[]`.
5. **Web Search (`search_web`):** Only `arXiv:2611.19371v1` itself (verified computationally up to $n=8$ in the paper).

## Coverage Limits
- `gh search code` skipped under secondary rate-limit budget (previously checked clear in `notes/novelty-attack.md` at `10:44:02Z`); near-miss Hamaker–Weigandt `2611.34697v1` checked in `TARGET.md`/`notes/novelty-attack.md` (restricts to $\mathrm{Sp}_{2n}$).
