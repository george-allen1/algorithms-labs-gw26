"""Provided checks for Lab 10. No third-party packages required."""

from copy import deepcopy
from math import inf


def check_weighted_graphs(prim, dijkstra):
    """Run named checks and return zero when every check passes."""
    lecture = [
        [(1, 2), (2, 3)],
        [(0, 2), (2, 1), (3, 4)],
        [(0, 3), (1, 1), (3, 5), (4, 6)],
        [(1, 4), (2, 5), (4, 7)],
        [(2, 6), (3, 7)],
    ]
    changed = deepcopy(lecture)
    changed[0][1] = (2, 2.5)
    changed[2][0] = (0, 2.5)
    triangle = [[(2, 1), (1, 1)], [(0, 1), (2, 1)], [(0, 1), (1, 1)]]
    zero = [[(1, 0), (2, 4)], [(0, 0), (2, 2)], [(0, 4), (1, 2)]]
    negative = [[(1, -2), (2, 4)], [(0, -2), (2, -1)], [(0, 4), (1, -1)]]
    cases = [
        ("Prim: lecture", prim, (lecture,), ([None, 0, 1, 1, 2], 13)),
        ("Prim: different root", prim, (lecture, 4), ([1, 2, 4, 1, None], 13)),
        ("Prim: decimal weight", prim, (changed,), ([None, 0, 1, 1, 2], 13)),
        ("Prim: tied keys", prim, (triangle,), ([None, 0, 0], 2)),
        ("Prim: zero weight", prim, (zero,), ([None, 0, 1], 2)),
        ("Prim: negative weights", prim, (negative,), ([None, 0, 1], -3)),
        ("Prim: disconnected", prim, ([[(1, 2)], [(0, 2)], []],), None),
        ("Prim: isolated root", prim, ([[], [(2, 1)], [(1, 1)]],), None),
        ("Prim: single vertex", prim, ([[]],), ([None], 0)),
        ("Prim: empty", prim, ([],), ([], 0)),
        ("Dijkstra: lecture", dijkstra, (lecture, 0), ([0, 2, 3, 6, 9], [None, 0, 0, 1, 2])),
        ("Dijkstra: different source", dijkstra, (lecture, 4), ([9, 7, 6, 7, 0], [2, 2, 4, 4, None])),
        ("Dijkstra: decimal weight", dijkstra, (changed, 0), ([0, 2, 2.5, 6, 8.5], [None, 0, 0, 1, 2])),
        ("Dijkstra: tied routes", dijkstra, (triangle, 0), ([0, 1, 1], [None, 0, 0])),
        ("Dijkstra: zero weight", dijkstra, (zero, 0), ([0, 0, 2], [None, 0, 1])),
        ("Dijkstra: priority decreases", dijkstra,
         ([[(1, 9), (2, 2)], [(3, 1)], [(1, 1), (3, 8)], []], 0),
         ([0, 3, 2, 4], [None, 2, 0, 1])),
        ("Dijkstra: directed edges", dijkstra, ([[(1, 3)], []], 1), ([inf, 0], [None, None])),
        ("Dijkstra: unreachable vertex", dijkstra, ([[(1, 2)], [], []], 0), ([0, 2, inf], [None, 0, None])),
        ("Dijkstra: isolated source", dijkstra, ([[], [(2, 1)], []], 0), ([0, inf, inf], [None, None, None])),
        ("Dijkstra: single vertex", dijkstra, ([[]], 0), ([0], [None])),
        ("Dijkstra: zero cycle", dijkstra, ([[(1, 0)], [(2, 0)], [(0, 0)]], 0), ([0, 0, 0], [None, 0, 1])),
        ("Dijkstra: equal-priority order", dijkstra,
         ([[(2, 1), (1, 1)], [(3, 1)], [(3, 1)], []], 0),
         ([0, 1, 1, 2], [None, 0, 0, 1])),
    ]
    passed = unfinished = failed = 0
    for name, function, args, expected in cases:
        try:
            inputs = deepcopy(args)
            before = deepcopy(inputs)
            actual = function(*inputs)
            assert actual == expected, f"expected {expected!r}, got {actual!r}"
            assert inputs == before, "input graph was modified"
        except NotImplementedError:
            unfinished += 1
            print(f"[TODO] {name}")
        except Exception as error:
            failed += 1
            print(f"[FAIL] {name}: {error}")
        else:
            passed += 1
            print(f"[PASS] {name}")
    print(f"\n{passed} passed; {unfinished} unfinished; {failed} failed")
    return 0 if passed == len(cases) else 1
