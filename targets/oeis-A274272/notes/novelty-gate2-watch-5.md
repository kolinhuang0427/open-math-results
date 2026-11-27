# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A274272/` (`OEIS:A274272` rev. 12, Colin Barker Jun 17 2016 conjectures on partitions of $5^n$ into $\le 4$ parts)
- **Timestamp (UTC):** `2026-11-27T11:37Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A274272`
   - Result: `0` lines across `0/658` files.
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A274272` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A274272&fmt=json`):**
   - `A274272` rev. `12` (`2016-06-23`) still lists Colin Barker's closed form, recurrence, and g.f. under `Conjectures (Start)`.
4. **Zenodo, `mylesparslow`, `gh search issues`, & `search_web`:**
   - Zenodo live API (`"A274272"`): `0` hits; `mylesparslow-collab.github.io`: `False`; `gh search issues "A274272"`: `0` hits; `search_web`: `0` proof hits.

## Coverage Limits

- `gh search code` skipped under earlier GitHub 429 cooldown; local `658`-file snapshot corpus and `gh search issues` are clear. No cited arXiv preprint for OpenAlex/S2 citing-paper traversal.
