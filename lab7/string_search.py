"""Complete the string-search algorithms and prefix helper for Lab 7."""


def naive_search(text, pattern):
    """Return all matching starting indices, including overlapping matches.

    Inputs are ASCII strings and pattern is nonempty.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []
    matches = []

    # TODO 1.2: compare characters at each shift and collect complete matches
    raise NotImplementedError("Complete naive_search")

    return matches


def rabin_karp(text, pattern, d=256, q=101):
    """Return all matching starting indices using a rolling hash.

    Inputs are ASCII strings, pattern is nonempty, and q is a positive prime.
    Use ord(character) for character codes and verify every hash hit.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []
    matches = []
    h = pow(d, m - 1, q)
    p = 0
    t = 0

    # TODO 2.2: build the initial hashes, verify hits, and roll to each next window
    raise NotImplementedError("Complete rabin_karp")

    return matches


def compute_prefix_function(pattern):
    """Return the longest proper border length for each pattern prefix.

    pattern is nonempty. pi[j] describes pattern[0:j + 1].
    """
    m = len(pattern)
    pi = [0] * m
    k = 0

    # TODO 3.2A: extend each border, following prefix links on a mismatch
    raise NotImplementedError("Complete compute_prefix_function")

    return pi


def kmp_search(text, pattern):
    """Return all matching starting indices using the prefix table.

    Inputs are ASCII strings and pattern is nonempty.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []
    matches = []
    pi = compute_prefix_function(pattern)
    q = 0

    # TODO 3.2B: scan the text with prefix fallbacks and record all matches
    raise NotImplementedError("Complete kmp_search")

    return matches


if __name__ == "__main__":
    from lab_checks import check_string_search

    raise SystemExit(check_string_search(
        naive_search, rabin_karp, compute_prefix_function, kmp_search
    ))
