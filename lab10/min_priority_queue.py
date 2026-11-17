"""Provided indexed binary min-heap for Lab 10."""


class MinPriorityQueue:
    """Store each vertex once; break equal priorities by vertex number."""

    def __init__(self, priorities):
        self.priorities = list(priorities)
        self.heap = list(range(len(priorities)))
        self.position = list(range(len(priorities)))
        for index in range(len(self.heap) // 2 - 1, -1, -1):
            self._down(index)

    def __len__(self):
        return len(self.heap)

    def __contains__(self, vertex):
        return 0 <= vertex < len(self.position) and self.position[vertex] != -1

    def _less(self, i, j):
        u, v = self.heap[i], self.heap[j]
        return (self.priorities[u], u) < (self.priorities[v], v)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i]] = i
        self.position[self.heap[j]] = j

    def _down(self, index):
        while 2 * index + 1 < len(self.heap):
            child = 2 * index + 1
            if child + 1 < len(self.heap) and self._less(child + 1, child):
                child += 1
            if not self._less(child, index):
                break
            self._swap(index, child)
            index = child

    def pop_min(self):
        """Remove and return the vertex with the smallest priority."""
        if not self.heap:
            raise IndexError("empty priority queue")
        self._swap(0, len(self.heap) - 1)
        vertex = self.heap.pop()
        self.position[vertex] = -1
        if self.heap:
            self._down(0)
        return vertex

    def decrease_key(self, vertex, value):
        """Lower a queued vertex's priority and restore heap order."""
        if vertex not in self:
            raise ValueError("vertex must still be in the queue")
        if value > self.priorities[vertex]:
            raise ValueError("new priority must be no larger than the old one")
        self.priorities[vertex] = value
        index = self.position[vertex]
        while index > 0:
            parent = (index - 1) // 2
            if not self._less(index, parent):
                break
            self._swap(index, parent)
            index = parent
