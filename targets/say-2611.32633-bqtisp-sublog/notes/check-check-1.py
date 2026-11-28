"""Independent exact-integer verifier for targets/say-2611.32633-bqtisp-sublog."""

from __future__ import annotations

import math
import pathlib
import re
import tarfile


def bin_len(n: int) -> int:
    if n == 0:
        return 1
    return n.bit_length()


def floor_log2(n: int) -> int:
    assert n >= 1
    return n.bit_length() - 1


def ceil_log2(n: int) -> int:
    assert n >= 1
    if n == 1:
        return 0
    return (n - 1).bit_length()


def verify_lemma1() -> None:
    # Exact string length identity for k = 1..5000
    running_len = 1  # "0"
    for k in range(1, 5001):
        running_len += 1 + bin_len(k)  # "$" + bin(k)
        m = bin_len(k)
        formula = (k + 1) * (m + 1) - (1 << m) + 1
        assert running_len == formula, f"k={k}: len={running_len} != {formula}"

    # Bit-length estimate bounds for k = 128..35000 (m >= 8)
    for k in range(128, 35001):
        m = bin_len(k)
        assert m >= 8
        n_k = (k + 1) * (m + 1) - (1 << m) + 1
        t = ceil_log2(m + 1) + 3
        assert t <= m - 1
        shift = m - t
        k_top = k >> shift
        a_val = k_top * (m + 1) - (1 << t)
        assert a_val * (1 << shift) <= n_k < 2 * a_val * (1 << shift)
        r_tilde = shift + floor_log2(a_val)
        fl = floor_log2(n_k)
        assert r_tilde <= fl <= r_tilde + 1
        assert (1 << r_tilde) <= n_k < (1 << (r_tilde + 2))
        assert r_tilde >= m + 1
    print("LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True")


def verify_concrete_sublog_families() -> None:
    def s_sqrt(n: int) -> int:
        return math.isqrt(floor_log2(n))

    def s_log_over_loglog(n: int) -> int:
        # Exact floor(lg / log_2(lg)) via largest q with lg^q <= 2^lg (zero floats)
        lg = floor_log2(n)
        pow2_lg = 1 << lg
        q = 1
        cur = lg
        while cur * lg <= pow2_lg:
            cur *= lg
            q += 1
        return q

    def s_three_quarter_log(n: int) -> int:
        lg = floor_log2(n)
        # floor((lg)^3/4) = isqrt(isqrt(lg^3))
        x = lg * lg * lg
        r1 = math.isqrt(x)
        return math.isqrt(r1)

    def s_loglog_logloglog(n: int) -> int:
        llg = floor_log2(floor_log2(n))
        lllg = floor_log2(llg)
        return llg * lllg

    families = [
        ("sqrt_log", s_sqrt, 2, 16),
        ("three_quarter_log", s_three_quarter_log, 2, 16),
        ("log_div_loglog", s_log_over_loglog, 2, 16),
        ("loglog_mul_logloglog", s_loglog_logloglog, 4, 16),
    ]

    for name, s_fn, c_const, r0 in families:
        # Check across k = 4096..12000 (where r_tilde >= 13; test large r via bit-shifts too)
        for exp in range(r0, 400):
            n1 = 1 << exp
            n2 = 1 << (exp + 1)
            assert s_fn(n1) <= s_fn(n2) <= c_const * s_fn(n1)
            assert 1 <= s_fn(n1) <= exp - 2

        for k in range(2048, 8001):
            m = bin_len(k)
            t = ceil_log2(m + 1) + 3
            shift = m - t
            k_top = k >> shift
            a_val = k_top * (m + 1) - (1 << t)
            r_tilde = shift + floor_log2(a_val)
            n_k = (k + 1) * (m + 1) - (1 << m) + 1
            n_next = (k + 2) * (bin_len(k + 1) + 1) - (1 << bin_len(k + 1)) + 1
            if r_tilde < r0:
                continue
            l_k = s_fn(1 << r_tilde)
            j_k = 1 << l_k
            assert j_k <= n_k // 4
            assert l_k <= s_fn(n_k)
            # Check gap smoothness for endpoints of [N_k, N_{k+1}-1]
            if n_k >= 2 * (n_next - n_k):
                for n_probe in (n_k, n_next - 1):
                    assert n_probe < 8 * (1 << r_tilde)
                    assert s_fn(n_probe) <= (c_const**3) * l_k

        print(f"FAMILY_{name}: PASS")


def verify_source_and_docs() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2611.32633.src"
    target_md = (
        root / "targets" / "say-2611.32633-bqtisp-sublog" / "TARGET.md"
    ).read_text(encoding="utf-8")
    proof_md = (
        root / "targets" / "say-2611.32633-bqtisp-sublog" / "PROOF.md"
    ).read_text(encoding="utf-8")

    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            main_tex = tf.extractfile("main.tex").read().decode("utf-8")

        # Check numbered sections up to Concluding remarks (before duplicate/draft appendix content after \end{document})
        body_end = main_tex.find("\\section*{AI use}")
        assert body_end != -1
        numbered_secs = re.findall(r"(?m)^\\section\{([^}]+)\}", main_tex[:body_end])
        conc_idx = numbered_secs.index("Concluding remarks") + 1
        if f"Section {conc_idx}" not in target_md:
            failures.append(
                f"TARGET.md section mismatch: 'Concluding remarks' is Section {conc_idx} "
                f"(sections={numbered_secs}), whereas TARGET.md cites a different section number"
            )
        if f"Section {conc_idx}" not in proof_md:
            failures.append(
                f"PROOF.md section mismatch: 'Concluding remarks' is Section {conc_idx}, "
                f"whereas PROOF.md cites a different section number"
            )

    # Check exact quote in TARGET.md
    if "We believe that similar separations can be obtained for more general space functions throughout" not in target_md:
        failures.append("TARGET.md missing exact quote from main.tex L1924-1928")

    return failures


def main() -> int:
    verify_lemma1()
    verify_concrete_sublog_families()
    failures = verify_source_and_docs()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
