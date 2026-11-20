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

    while queue:
        u = queue.pop_min()
        if key[u] == inf:
            return None
        total += key[u]
        for v, weight in graph[u]:
            if v in queue and weight < key[v]:
                key[v] = weight
                parent[v] = u
                queue.decrease_key(v, key[v])

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

    while queue:
        u = queue.pop_min()
        if distance[u] == inf:
            break
        for v, weight in graph[u]:
            if v in queue:
                candidate = distance[u] + weight
                if candidate < distance[v]:
                    distance[v] = candidate
                    parent[v] = u
                    queue.decrease_key(v, distance[v])

    return distance, parent


if __name__ == "__main__":
    from lab_checks import check_weighted_graphs

    raise SystemExit(check_weighted_graphs(prim, dijkstra))
