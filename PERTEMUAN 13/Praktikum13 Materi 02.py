# ==========================================================
# PRAKTIKUM 13 - BAGIAN 6 (MATERI 2)
# Latihan 4 dan Latihan 5
# ==========================================================

import heapq

# ==========================================================
# LATIHAN 4 - STUDI KASUS GEDUNG (PRIM)
# ==========================================================

graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
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


mst, total = prim(graph, 'GedungA')

print("=== LATIHAN 4 ===")
for e in mst:
    print(e)

print("Total biaya =", total)


# ==========================================================
# LATIHAN 5 - KRUSKAL (JALAN KOTA)
# ==========================================================

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
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

print("\n=== LATIHAN 5 ===")
for e in mst:
    print(e)

print("Total =", total)
