---
layout: default
title: Lab 10
nav_order: 11
---

# CSCI 3212 Lab 10: Prim's and Dijkstra's Algorithms

Last week, Kruskal's algorithm built a minimum spanning tree by sorting
edges. This week, Prim's algorithm grows a tree from one starting vertex.
We will then use a similar approach to find shortest paths with Dijkstra's
algorithm.

1. **Part 1: Prim's Algorithm:** Connect all vertices with minimum total edge weight.
2. **Part 2: Dijkstra's Algorithm:** Find the shortest distance from a source to each vertex.

## Files and deliverables

| File | Your work |
|---|---|
| `README.md` | Complete the short traces and analysis questions |
| `weighted_graphs.py` | Complete the two implementation TODOs |
| `min_priority_queue.py` | Provided priority queue |
| `lab_checks.py` | Provided automated checks |

- [ ] Part 1: Trace and implement Prim's algorithm.
- [ ] Part 2: Trace and implement Dijkstra's algorithm, then compare the two.

Vertices are numbered `0` through `n - 1`. Each entry in `graph[u]` is a
pair `(v, weight)`. For an undirected edge, both directions appear in the
adjacency lists. Keep the input graph unchanged. Assume valid endpoints
and finite numeric weights.

### The provided priority queue

Both algorithms repeatedly choose the vertex with the smallest value.
The provided binary min-heap supports these operations:

| Python | Meaning |
|---|---|
| `MinPriorityQueue(values)` | Build a queue with one entry per vertex |
| `queue.pop_min()` | Remove and return the minimum vertex |
| `queue.decrease_key(v, value)` | Lower the priority of vertex `v` |
| `v in queue` | Check whether `v` is still waiting |
| `while queue:` | Continue while vertices remain |

The queue copies the initial values. When a value improves, update your
array **and** call `decrease_key`. Equal priorities are settled by vertex
number, so `A` comes before `B`. Use strict `<` comparisons when updating;
an equal value keeps the existing parent.

---

## Part 1: Prim's Algorithm

### Background: Grow one tree

Start with one vertex. At each step, add the cheapest edge joining the
current tree to a vertex outside it. This edge crosses the cut between
the tree and the remaining vertices, so the cut property from last week
allows us to include it in an MST.

For each waiting vertex `v`, keep:

- `key[v]`: the lightest edge found so far from the tree to `v`.
- `parent[v]`: the tree vertex at the other end of that edge.

Initially, all keys are infinity except the starting vertex's key, which
is zero. Removing `u` from the queue adds it to the tree. Then check its
neighbors: an edge from `u` may give a waiting vertex a cheaper connection.

Use this undirected lecture graph for both parts. The labels
`A, B, C, D, E` correspond to `0, 1, 2, 3, 4`.

```text
A--B: 2    A--C: 3    B--C: 1    B--D: 4
C--D: 5    C--E: 6    D--E: 7
```

Starting at `A`, the first removal sets `key[B] = 2` and `key[C] = 3`,
with both parents set to `A`. The other keys remain infinity.
The next removal is `B`. Its edges may improve the keys again.

### Pseudocode

```text
PRIM(graph, start)
  if graph is empty: return ([], 0)
  key = array filled with infinity
  parent = array filled with NONE
  key[start] = 0
  Q = min-priority queue containing all vertices, using key
  total = 0

  while Q is not empty
    u = EXTRACT-MIN(Q)
    if key[u] = infinity: return NONE
    total = total + key[u]
    for each (v, weight) in graph[u]
      if v is in Q and weight < key[v]
        key[v] = weight
        parent[v] = u
        DECREASE-KEY(Q, v, key[v])

  return (parent, total)
```

An infinite key at removal means that the remaining vertices cannot be
reached from the starting vertex. This implementation returns `None` for
a disconnected graph.

### 1.1 Trace: Which connection improves?

**TODO 1.1:** Continue from the state after removing `A`. Fill each row
**after** checking the removed vertex's neighbors. An edge is written
using its two endpoint labels.

| Vertex removed | Edge added | `key[D]` | `key[E]` |
|---|---|---|---|
| `B` | TODO | TODO | TODO |
| `C` | TODO | TODO | TODO |
| `D` | TODO | TODO | TODO |

1. Which vertex becomes `C`'s parent, and what causes the change? 


2. After removing `E`, what are the tree's four edges and total weight? 



### 1.2 Implementation

**TODO 1.2:** Complete `prim` in `weighted_graphs.py` using the pseudocode.
Return `(parent, total_weight)`. The starting vertex's parent stays `None`.
For example, `parent[2] = 1` represents the tree edge `B--C`.

The initialization and empty-graph case are provided. Use queue membership
to track which vertices are still outside the tree. Prim's algorithm also
supports zero and negative edge weights.

---

## Part 2: Dijkstra's Algorithm

### Background: Find the shortest route

For a source vertex `s`, `distance[v]` is the shortest distance to `v`
found so far. Start with `distance[s] = 0` and infinity everywhere else.
The parent array records the previous vertex on each path.

When we remove the vertex `u` with the smallest distance, its distance is
final. For each waiting neighbor `v`, check whether going through `u`
would shorten the route:

```text
candidate = distance[u] + weight(u, v)
```

If `candidate < distance[v]`, update the distance and parent. This step is
called **relaxation**. All edge weights must be **nonnegative** for
Dijkstra's algorithm; zero-weight edges are allowed.

In the example, removing source `A` gives distances `B = 2` and `C = 3`.
After removing `B`, the route to `D` through `B` has length `2 + 4 = 6`,
so set `distance[D] = 6` and `parent[D] = B`.

### Pseudocode

```text
DIJKSTRA(graph, source)
  distance = array filled with infinity
  parent = array filled with NONE
  distance[source] = 0
  Q = min-priority queue containing all vertices, using distance

  while Q is not empty
    u = EXTRACT-MIN(Q)
    if distance[u] = infinity: break
    for each (v, weight) in graph[u]
      if v is in Q
        candidate = distance[u] + weight
        if candidate < distance[v]
          distance[v] = candidate
          parent[v] = u
          DECREASE-KEY(Q, v, distance[v])

  return (distance, parent)
```

If the next distance is infinity, the remaining vertices are unreachable.
They keep distance `inf` and parent `None`. To recover a reachable vertex's
path, follow its parents back to the source and reverse that sequence.

### 2.1 Trace: Does the route improve?

**TODO 2.1:** Use source `A` and the same graph. Complete these selected
relaxations in execution order. Record the distance and parent of `v`
after each check, including checks that leave them unchanged.

| Edge checked | Candidate | Distance of `v` | Parent of `v` |
|---|---|---|---|
| `B -> C` | TODO | TODO | TODO |
| `C -> D` | TODO | TODO | TODO |
| `C -> E` | TODO | TODO | TODO |
| `D -> E` | TODO | TODO | TODO |

Give the final distance array and the shortest path from `A` to `E`:

 **TODO**

### 2.2 Implementation

**TODO 2.2:** Complete `dijkstra` in `weighted_graphs.py`. Return
`(distance, parent)`. Assume a nonempty graph, a valid source, and
nonnegative weights. The function should work for directed and
undirected graphs, including graphs with unreachable vertices.

### 2.3 Compare and analyze

**TODO 2.3:** Answer briefly.

1. Change only the weight of `A--C` to `2.5`. Starting from `A`, what is
   `C`'s parent under each algorithm? What quantity does each algorithm
   minimize? 


2. Consider the directed edges `S -> A: 2`, `S -> B: 5`, and `B -> A: -4`.
   Starting from `S`, which distance does Dijkstra finalize too early?
   Give the actual shortest distance and explain why the negative edge
   causes a problem.


3. Let `V` and `E` be the numbers of vertices and edges. For the provided
   heap, building the queue takes `O(V)`, each removal or decrease takes
   `O(log V)`, and membership takes `O(1)`. For **each algorithm**, count
   removals and possible decreases, then derive the worst-case time and
   auxiliary space bounds. Exclude the input graph from space. What is
   the time bound if finding the minimum instead scans an unsorted array
   of vertices?


---

## Check your implementations

From the `lab10` folder, run:

```bash
python3 weighted_graphs.py
```

The provided checks cover the lecture graph, ties, changing priorities,
zero-weight edges, and unreachable vertices. Each unfinished function
reports `[TODO]`. Finish the two implementations and the written answers.
