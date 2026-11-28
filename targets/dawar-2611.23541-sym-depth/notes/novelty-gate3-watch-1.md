# Gate 3 Novelty Receipt — `targets/dawar-2611.23541-sym-depth/` (`watch-1`)

- **Target:** `targets/dawar-2611.23541-sym-depth/` (*Depth Hierarchies for Symmetric Algebraic Circuits*, Anuj Dawar, Prateek Dwivedi, Benedikt Pago, Tim Seppelt, `arXiv:2611.23541v1` (`cs.CC`), §1.2 future work on depth-3/4 symmetric circuit reduction & orbit bounds)
- **Checked At (UTC):** `2026-11-27T20:56:44Z`–`2026-11-27T20:56:54Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.23541" "Dawar" "lax-symmetric"`
   - Result: `13` matching lines across `6/849` files in `watch/snapshots/arxiv/*` (announcing `2611.23541v1` itself) and `tseppelt/lax-symmetric-depth-reduction` catalog/snapshot ingest (`0` depth-3/4 symmetric circuit reduction results; formalizes `2611.23541v1` theorems only).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs "2611.23541"` -> `[]` (`0` hits)
   - `gh search issues "2611.23541"` -> `[]` (`0` hits)
   - `gh search code '"2611.23541" "depth"'` -> `[]` (`0` hits)
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T20:56:46Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research`: `3ba575175e726b162ea0438058fc1ee9e3349e36` (`2026-11-27T20:56:34Z`, negative rainbow axiom under ccc bounding forcing) — unrelated.
4. **arXiv / Zenodo / Crossref / Web Search:**
   - arXiv API (`id_list=2611.23541`): sole version `2611.23541v1` (`2026-11-17T21:49:23Z`, *"Depth Hierarchies for Symmetric Algebraic Circuits"*).
   - Zenodo API (`q=2611.23541`): `0` hits.
   - Crossref (`query.title=Depth+Hierarchies+for+Symmetric+Algebraic+Circuits`): `0` matching DOIs.
   - Web search (`search_web`): only `arXiv:2611.23541`, `laxarchive.org/lax-461425/`, and `[LST25]` Limaye–Srinivasan–Tavenas FOCS 2021; `0` resolutions of symmetric depth-3/4 circuit reductions.
   - Coverage note: Direct `curl` to `https://eccc.weizmann.ac.il/` returned `0` bytes from this sandbox; web search + `@watch-5`/`@watch-6` ECCC `/year/2026/` checks found `0` matching follow-ups.
5. **Independent Check Execution (`#1980`):**
   - Command: `.venv/bin/python -u targets/dawar-2611.23541-sym-depth/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `Theorems 1-2 thresholds & Lemma 1 S_n generation: PASS`
     - `Lemma 2 balanced 2-level decomposition + normalised pruning (d=1..100 incl. non-squares): PASS`
     - `Theorem 3 depth-4 circuit & Gamma_n-invariance (P_4, P_5): PASS`
     - `Theorem 4 Fischer + truncated exp + Q[t]/(mu) interpolation descent: PASS`
     - `PASS`
