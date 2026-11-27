# Adversarial Audit Helper Report: OEIS A286044

- **Target:** `targets/oeis-A286044/` (OEIS A286044 rev 8, Velin Yanev Feb 16 2026 conjecture)
- **Checked (UTC):** `2026-11-27T07:24Z` – `2026-11-27T07:36Z`
- **Directory & Isolation Check:** `ls -la targets/oeis-A286044/` shows `PROOF.md`, `TARGET.md`, `verify.py`, and `notes/`. **No `CONTESTED.md` present.**

---

## 1. Live OEIS Primary-Source Verification

All five sequences were fetched live from `https://oeis.org/search?q=id:<SEQ>&fmt=json` using `User-Agent: curl/8.7.1` and `--max-time 15` at `~2026-11-27T07:25Z`–`07:35Z`.

### `A286044`
- **Revision:** `8`
- **Last-modified (`time`):** `2026-02-19T22:02:10-05:00` (created `2017-05-07T21:35:19-04:00`; author `_Clark Kimberling_, May 07 2017`)
- **Offset:** `"1"`
- **Verbatim Name:**
  > `{011->0}-transform of the Thue-Morse word A010060.`
- **Verbatim Comment:**
  > `This is also the {110->1}-transform of A010060.`
- **Verbatim Formula:**
  > `Conjecture: a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160. - _Velin Yanev_, Feb 16 2026`
- **Verbatim Example:**
  > `As a word, A010060 = 0110100110010110100101100..., and replacing each 011 by 0 gives 00100001001001000010000100001...`
- **Program / Mathematica:** No `program` field present; `mathematica` field verbatim:
  - `s = Nest[Flatten[# /. {0 -> {0, 1}, 1 -> {1, 0}}] &, {0}, 9] (* Thue-Morse, A010060 *)`
  - `w = StringJoin[Map[ToString, s]]`
  - `w1 = StringReplace[w, {"011" -> "0"}]`
  - `st = ToCharacterCode[w1] - 48 (* A286044 *)`
  - `Flatten[Position[st, 0]]  (* A286045 *)`
  - `Flatten[Position[st, 1]]  (* A003157 *)`
  - `Most[SequenceReplace[Array[ThueMorse, 2^9, 0], {0, 1, 1} -> 0]] (* _Velin Yanev_, Feb 16 2026 *)`
- **Match Check:** Yanev's Feb 16 2026 formula is **still explicitly marked `Conjecture:`** on live OEIS `A286044` rev 8 and matches `PROOF.md` (`a(n) = b(b(n-2)) - b(b(n-3))` for `n > 3`, `a = A286044`, `b = A003160`) and `TARGET.md` verbatim. Kimberling's Mathematica program defines the `{011->0}`-transform via `StringReplace[w, {"011" -> "0"}]` (left-to-right non-overlapping replacement, unambiguous since `011` occurrences in Thue–Morse are pairwise disjoint).

### `A003160`
- **Revision:** `61`, **Last-modified:** `2026-03-10T09:26:09-04:00`, **Offset:** `"1,4"`
- **Verbatim Name:** `a(1) = a(2) = 1, a(n) = n - a(a(n-1)) - a(a(n-2)).`
- **Comments:**
  - `Sequence of indices n where a(n-1) < a(n) appears to be given by A003156. - _Joerg Arndt_, May 11 2010`
  - `The number n appears A080426(n+1) times. - _John Keith_, Dec 31 2020`
- **Formulas:**
  - `a(n) is asymptotic to n/2.`
  - `a(n) = A003159(n + 1) - (n + 1). - _Velin Yanev_, Jan 27 2026`
- **Notes:** `b(n) = A003159(n + 1) - (n + 1)` IS already recorded in `A003160`'s Formula section (Jan 27 2026, _Velin Yanev_); `PROOF.md` (§3) proves this identity from first principles rather than assuming it. `A286044` is **not** mentioned anywhere in `A003160`.

### `A010060`, `A003159`, `A003157`
- **`A010060`:** rev `619`, **Last-modified:** `2026-10-18T01:10:44-04:00`, **Offset:** `"0,1"`, **Name:** `Thue-Morse sequence: let A_k denote the first 2^k terms; then A_0 = 0 and for k >= 0, A_{k+1} = A_k B_k, where B_k is obtained from A_k by interchanging 0's and 1's.` Does not mention `A286044` or `Yanev`.
- **`A003159`:** rev `238`, **Last-modified:** `2026-05-30T16:39:44-04:00`, **Offset:** `"1,2"`, **Name:** `Numbers whose binary representation ends in an even number of zeros.` Does not mention `A286044` or `Yanev`.
- **`A003157`:** rev `38`, **Last-modified:** `2025-11-26T15:59:32-05:00`, **Offset:** `"1,1"`, **Name:** `A self-generating sequence (see Comments in A003156 for the definition).` Mentions `A286044` only in Kimberling's May 07 2017 comment/example/Mathematica/xref (`positions of 1 in A286044`); does not mention `Yanev` or `A003160`.

---

## 2. Deep Novelty Check (through `2026-11-27T07:36Z`)

- **Local snapshots (`tools/novelty_grep.py A286044 286044 "Velin Yanev" A003160 "011->0"`):**
  - 2 lines across 2/542 files:
    1. `watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/files.txt:718` (`conjectures/phase0/A286044.txt`).
    2. `watch/snapshots/discovered/the-omega-institute__trureturing-tools.json:1486` (unrelated `A034448` conjecture by Velin Yanev).
  - Case-insensitive scan across all `watch/snapshots/**` also flagged `003160` in `watch/snapshots/discovered/the-omega-institute__trureturing-source-theories.json` — verified via GitHub tree to be a SHA-256 hex filename prefix (`Meta/Digestion/atoms/sha256/00316041434b7fbee5d415a30f526e9a0e1c87fee3e612c441e1d5d9a0f9591f`).
- **arXiv (`tools/arxiv_fetch.py query`):**
  - `all:A286044 OR (all:"Velin Yanev" AND all:A003160)` → `total_results: 0`.
  - `all:"b(b(n - 2)) - b(b(n - 3))" OR (all:"011->0" AND all:"Thue-Morse")` → `total_results: 0`.
- **Zenodo API (`zenodo.org/api/records`):**
  - `q=A286044` → `0` hits; `q="Velin Yanev" A003160` → `0` hits; `q="b(b(n - 2)) - b(b(n - 3))"` → `0` hits; `q="011->0" "Thue-Morse"` → `628` general Thue-Morse hits (top 10 inspected, none on `A286044` or `A003160`).
- **Crossref API (`api.crossref.org/works`):**
  - `query=A286044` → `0` hits; `query=Velin+Yanev+A003160` → unrelated musicology/biology/branching-process DOIs; `query="b(b(n - 2)) - b(b(n - 3))"` & `query="011->0" "Thue-Morse"` → tokenized general hits, none on `A286044` or `A003160`.
- **Web search (`search_web`):**
  - Queries `"A286044" OR ("Velin Yanev" "A003160")`, `"b(b(n - 2)) - b(b(n - 3))" OR ("011->0" "Thue-Morse")`, and `"A003160" "A003159" "Velin Yanev"` returned only the OEIS pages (`A286044`, `A003160`, `A003159`, `A003157`); no proof or paper found.
- **Competing GitHub repositories (read-only `gh api` trees/commits/issues + file inspection + global `gh search`):**
  - **`joaquimmj/oeis-conjectures`** (`pushed=2026-11-19T16:39:12Z`):
    - Inspected `conjectures/phase0/A286044.txt` directly: verbatim raw OEIS entry `#8 Feb 19 2026 22:02:10` containing `%F A286044 Conjecture: a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160. - _Velin Yanev_, Feb 16 2026`. **Open-conjecture listing only, NOT a proof.**
    - Inspected `conjectures/yanev/proof.md`: solves 9 unrelated Yanev conjectures (`A129527`, `A173614`, `A023887`, `A055210`, `A367865`, `A090079`, `A163617`, `A285385`, `A179504`); no mention of `A286044` or `A003160`.
    - Inspected `conjectures/kimberling/proof.md` & `tm_limits.py`: proves Kimberling's asymptotic density conjecture `a(n)/n -> 4` on `A003157` (`"Pour A003157, l'identification « positions de 1 dans A286044 » est celle de l'entrée, contrôlée sur ses données"`); does not prove Yanev's `A286044` / `A003160` recurrence identity.
  - **`the-omega-institute/trureturing*`** (checked `trureturing`, `trureturing-books`, `trureturing-books-template`, `trureturing-experiments`, `trureturing-film`, `trureturing-intuition`, `trureturing-lean-eval`, `trureturing-live`, `trureturing-live-template`, `trureturing-mdbook`, `trureturing-outreach-engine`, `trureturing-pages`, `trureturing-requests`, `trureturing-source-theories`, `trureturing-tools`, `trureturing-visualize`, plus `automath`, `mathesis`, `newmath`):
    - Inspected `trureturing` `Blueprint/D5/S1/Digit/YanevBinaryReversalPositionIdentity.md`, `YanevRunCompressionClosedForm.md`, `D5/S3/Arith/YanevMaxExponentRadicalRecurrence.md`, `YanevSigmaRadicalIdentity.md`, `Recurrence/MetaFibonacci/` (`SobolewskiUlasParityPositions.md`), `Recurrence/FloorCounts/`, `Words/Hofstadter/`, `Words/ParityCode/`, `Words/TwoBlockSubstitution/`; also checked `trureturing-experiments` (`003081-003160.json` is an Erdős 7 filename range). No proof or mention of `A286044` or `A003160`.
  - **`1337isnot1337/solved-conjectures`** (`pushed=2026-11-27T07:30:24Z`, 211 result dirs): `results/gawron-miska-ulas-thue-morse-{sign-density,valuation}` are unrelated; `0` matches in `results/`, recent commits, or issues for `A286044`, `A003160`, or `Yanev`.
  - **Other competing repos** (`aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond` [issue #124 is unrelated Yanev unitary-prime/square-divisor identities], `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `openai/math` [`pushed=2026-11-25T00:18:51Z`, 55,175 files]): `0` hits for `A286044`, `A003160`, or Yanev's conjecture in trees/recent commits/issues. (Note: `trureturing`, `atlas-lean`, `CrocSwap/integer-mult-bounds`, `openai/math`, and `trureturing-source-theories` exceed GitHub's recursive tree cap and returned `truncated: true`, mitigated by checking local watch snapshots, recent commits, and `trureturing` subtrees directly.)
  - **Global `gh search`:**
    - `gh search code A286044` → `30` hits, limited to pre-2026 OEIS sequence libraries/benchmarks (`archmageirvine/joeis`, `loda-lang/loda-programs`, `ai4reason/oeis-atp-benchmark/pb/A286044.smt2` inspected and confirmed definition-only without Yanev's formula) and unrelated hex/hashes.
    - `gh search code "b(b(n - 2)) - b(b(n - 3))"` → `0`; `gh search code "011->0" "Thue-Morse"` → `0`; `gh search code "Velin Yanev" A003160` → `0`.
    - `gh search issues A286044` → `0`; `gh search issues "Velin Yanev" A003160` → `0`; `gh search repos A286044` → `0`.
- **Not covered:** Closed-access journals/preprints, unindexed private repositories, and files in >50k-file GitHub trees omitted by GitHub's recursive tree truncation outside checked subtrees/snapshots/recent commits.

---

## 3. Independent Computation Rerun

Command:
```bash
/usr/bin/time -p .venv/bin/python -u targets/oeis-A286044/notes/check-check-2.py
```

- **Exit code:** `0`
- **Runtime:** `real 0.43`, `user 0.33`, `sys 0.04` (script internal timer: `0.383s`)
- **Raw output:**
```text
[OEIS A286044 prefix + literal 011->0] PASS (86 OEIS terms, computed 160138 terms)
[Section 1 Fact 1 & Fact 2] PASS up to 240200
[Section 2 indicator & 2v(m)+m positions] PASS for 1<=n<=120000 (29999 surviving 1s)
[Section 3 A003160 recurrence, prefix, closed form & I_y blocks] PASS for 1<=n<=120004
[Main Theorem: a(n) = b(b(n-2)) - b(b(n-3))] PASS for ALL 4<=n<=120000
PASS (all independent checks passed in 0.383s)
```
