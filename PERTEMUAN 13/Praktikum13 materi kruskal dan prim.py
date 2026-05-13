# ==========================================================
# Implementasi Kruskal
# ==========================================================

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Urutkan edge berdasarkan bobot
edges.sort()

# Disjoint Set / Union Find
parent = {}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        parent[root_v] = root_u

# Inisialisasi parent
nodes = ['A', 'B', 'C', 'D']

for node in nodes:
    parent[node] = node

mst = []
total_weight = 0

for weight, u, v in edges:
    # Jika tidak membentuk cycle
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))
        total_weight += weight

print("Minimum Spanning Tree (Kruskal):")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)




# ==========================================================
# Implementasi Prim
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

    # Masukkan edge awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_weight += weight

            # Tambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Prim):")

for edge in mst:
    print(edge)

print("Total bobot =", total)
