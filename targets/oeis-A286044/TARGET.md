---
source: https://oeis.org/A286044 (rev. 8, Feb 19 2026)
status: reported
owner: scout-6
updated: 2026-11-27T04:48:00Z
identifiers: [A286044, A010060, A003160, A003159, A003157, Velin Yanev]
---

# Target: OEIS A286044 (Yanev 2026 Nested-Recurrence Formula for `{011->0}`-Thue–Morse)

## Verbatim Statement
From OEIS **A286044** (author: `_Clark Kimberling_`, May 07 2017; latest revision `#8`, `2026-02-19T22:02:10-05:00`), offset `1`:

- **Name:**
  > {011->0}-transform of the Thue-Morse word A010060.
- **Data (`offset 1`):**
  > 0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0
- **Formula (Conjecture):**
  > Conjecture: a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160. - _Velin Yanev_, Feb 16 2026

From OEIS **A003160** (latest revision `#61`, `2026-03-10T09:26:09-04:00`), offset `1,4`:
- **Name:**
  > a(1) = a(2) = 1, a(n) = n - a(a(n-1)) - a(a(n-2)).

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T04:08:35Z` – `04:47:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A286044 A003160 A003157 A003159 "Velin Yanev"`): only index listings `joaquimmj__oeis-conjectures/files.txt` (`A003157.txt`, `A286044.txt`) and an unrelated `A034448` entry in `trureturing-tools.json`; `0` proofs or papers on `A286044` across all `470` files.
- `tools/arxiv_fetch.py query`:
  - `all:A286044 OR all:"Velin Yanev" OR all:"011->0"` -> 2 unrelated physics/chem papers (`2610.10081v1`, `1609.04999v1`).
  - `all:A003160 OR all:"A003159" OR (all:"a(n) = n - a(a(n-1)) - a(a(n-2))")` -> 1 unrelated graph theory paper (`1101.3624v1`).
- Zenodo API (`zenodo.org/api/records?q=A286044+OR+A003160&size=5`): `0` hits.
- Crossref API (`api.crossref.org/works?query=A286044` -> `0` hits; `query=A003160` -> 3 unrelated biology DOIs).
- GitHub (`gh search code` for `A286044`, `"b(b(n - 2)) - b(b(n - 3))"`, `"011->0"`): only benchmark/program repositories (`archmageirvine/joeis`, `loda-lang/loda-programs`, `ai4reason/oeis-atp-benchmark/pb/A286044.smt2` inspected and confirmed pre-2026 definition benchmark without Yanev formula).
- Live OEIS JSON (`A286044` rev 8, `2026-02-19`, `A003160` rev 61, `2026-03-10`): Yanev's formula on `A286044` remains explicitly marked `Conjecture:`.
- Web search (`search_web` for `"A286044" OR ("Velin Yanev" "A003160")`): only OEIS entries `A286044` and `A003160`, no proof found.
- Not covered: closed-access venues or private repositories.
