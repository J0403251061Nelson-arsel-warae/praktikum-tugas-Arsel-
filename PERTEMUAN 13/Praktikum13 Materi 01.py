# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : B2
# ==========================================================
# PRAKTIKUM 13 - BAGIAN 6 (MATERI 1)
# Spanning Tree, Kruskal, Prim
# ==========================================================

# ==========================================================
# LATIHAN 1 - SPANNING TREE
# ==========================================================

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("=== LATIHAN 1 ===")
print("Edge pada graph:")
for e in edges:
    print(e)

print("\nSpanning Tree:")
for e in spanning_tree:
    print(e)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================================
# LATIHAN 2 - KRUSKAL
# ==========================================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

edges.sort()

mst = []
total = 0
connected = set()

for w, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, w))
        total += w
        connected.add(u)
        connected.add(v)

print("\n=== LATIHAN 2 (KRUSKAL) ===")
for e in mst:
    print(e)

print("Total =", total)


# ==========================================================
# LATIHAN 3 - PRIM
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []

    for n, w in graph[start].items():
        heapq.heappush(edges, (w, start, n))

    mst = []
    total = 0

    while edges:
        w, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            total += w

            for n, weight in graph[v].items():
                if n not in visited:
                    heapq.heappush(edges, (weight, v, n))

    return mst, total


mst, total = prim(graph, 'A')

print("\n=== LATIHAN 3 (PRIM) ===")
for e in mst:
    print(e)

print("Total =", total)
