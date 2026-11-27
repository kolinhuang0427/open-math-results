# Gate 3 Novelty Check (<1h) — targets/guo-2310.15207-conj6.4/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:03:52Z`
- **Target:** `targets/guo-2310.15207-conj6.4/` (label: `"written proof, internally audited"`) — Victor J. W. Guo (`arXiv:2310.15207v1` / *RACSAM* 119 (2025) §6) **Conjecture 6.4** (`conj:4`) and companion **Conjecture 6.3** (`conj:3`) modulo $\Phi_{n^s}(q)^2$ for $n \equiv 1 \pmod 4$ ($n > 1$) and $r > s \ge 1$.
- **Verdict:** **PASS** (clear within `<1h` freshness window).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2310.15207" "conj:4" "Conjecture 6.4" "conj:3" "Conjecture 6.3"`
   - Result: `19` lines across `12/651` files — inspected completely; all matches are unrelated `Conjecture 6.3`/`6.4` entries (Pantone–Bóna, Caro–Petruševski–Škrekovski, Liu, Billey–Fahrbach–Talmage, Aragão–Chapman–Ortega–Souza, Fractional Planks); `0` matches for `2310.15207`, `conj:4`, or `conj:3`.
2. **Live arXiv (`all:2310.15207`):**
   - `http://arxiv.org/abs/2310.15207v1` (`2023-10-23T12:51:42Z`) remains the sole arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222310.15207%22&size=5`):** `zenodo_hits: 0`.
4. **GitHub Search (`gh search repos "2310.15207"`, `gh search issues "2310.15207"`):** Both returned `[]`.

## Coverage Limits
- Re-verified local snapshots (`651` files incl. Sweep 5 & Zenodo `23114921`), live arXiv, Zenodo API, and GitHub repos/issues since Gate 2 (`targets/guo-2310.15207-conj6.4/notes/novelty-gate2-watch-6.md`); `gh search code` skipped under secondary-rate-limit budget.
