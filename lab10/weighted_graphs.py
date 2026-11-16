"""Complete Prim's algorithm and Dijkstra's algorithm for Lab 10."""

from math import inf

from min_priority_queue import MinPriorityQueue

EXAMPLE_GRAPH = [
    [(1, 2), (2, 3)],
    [(0, 2), (2, 1), (3, 4)],
    [(0, 3), (1, 1), (3, 5), (4, 6)],
    [(1, 4), (2, 5), (4, 7)],
    [(2, 6), (3, 7)],
]


def prim(graph, start=0):
    """Return (parent, total_weight) for an MST, or None if disconnected.

    The graph is undirected, with both directions listed. Weights may be negative.
    For an empty graph, return ([], 0). Otherwise start is a valid vertex.
    """
    n = len(graph)
    if n == 0:
        return [], 0
    key = [inf] * n
    parent = [None] * n
    key[start] = 0
    queue = MinPriorityQueue(key)
    total = 0

    # TODO 1.2: grow the tree and update the keys of queued neighbors
    raise NotImplementedError("Complete prim")

    return parent, total


def dijkstra(graph, source):
    """Return (distance, parent) for shortest paths from a valid source.

    The graph is nonempty and may be directed. All weights are nonnegative.
    Unreachable vertices keep distance inf and parent None.
    """
    distance = [inf] * len(graph)
    parent = [None] * len(graph)
    distance[source] = 0
    queue = MinPriorityQueue(distance)

    # TODO 2.2: finalize the closest vertex and relax its outgoing edges
    raise NotImplementedError("Complete dijkstra")

    return distance, parent


if __name__ == "__main__":
    from lab_checks import check_weighted_graphs

    raise SystemExit(check_weighted_graphs(prim, dijkstra))
