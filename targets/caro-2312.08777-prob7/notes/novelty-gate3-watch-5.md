# Gate 3 Novelty & Pre-Report Verification — `caro-2312.08777-prob7` (`watch-5`)

- **Target:** `targets/caro-2312.08777-prob7/` — Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *"Flip colouring of graphs"*, `arXiv:2312.08777v1` / *Graphs and Combinatorics* 40 (106), 2024 (`DOI:10.1007/s00373-024-02838-w`), Section 7 final Problem ($b(t) = 3$ for all $t \ge 1$).
- **Checked UTC:** `2026-11-27T18:06:43Z`–`2026-11-27T18:06:55Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`18:06Z`)
1. **Local snapshots (`watch/snapshots/**`, 760 files):**
   - `.venv/bin/python tools/novelty_grep.py "2312.08777" "Mifsud" "Zarb" --max-per-file 10 --max-total 40`: `0` lines across `0/760` files.
2. **Live GitHub (`gh`):**
   - `gh search issues "2312.08777"` & `gh search prs "2312.08777"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34939`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs (`18:06:54Z`):**
   - `arXiv` API (`id_list=2312.08777,2609.37978`): `2312.08777v1` (`2023-12-14`) sole version; 5th S2 citer `2609.37978v3` (*There is no $8$-regular $K_3$-irregular graph*) is unrelated to $b(t)$ ($t$-neighbourhood flip graphs).
   - `OpenAlex` (`W4403238211`): `cited_by_count: 4` unchanged from Gate 2 (`2401.02315`, `2403.04401`, `2507.14473`, `2602.23517`, all inspected in Gate 2 via TeX eprint and confirmed unrelated to $b(t)$ for $t \ge 2$).
   - `Zenodo` (`q=2312.08777`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py`
- Exit code: `0` (`Primary source arXiv:2312.08777v1 verbatim statement & definitions verified`, `Lower bound b(t) >= 3 algebra & triangle identities verified`, `Layer recurrence & e_{1,s} > e_{2,s} verified in exact ints for 1 <= s <= 200`, `Explicit ([1],(3,4)) (128v), ([2],(3,4)) (2048v), and ([3],(3,4)) (34952v, sampled 203v) verified`, `PASS`).
- Verified files present: `targets/caro-2312.08777-prob7/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** `2401.02315`, `2403.04401`, `2507.14473`, `2602.23517`, `2609.37978` address $t=1$ flip graphs or $K_3$-regularity, not $b(t)$ ($t \ge 2$).
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T18:06:55Z` are not covered.
