# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 5: Studi Kasus Dengan Program shortest path

import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        jarak, node = heapq.heappop(pq)

        if jarak > distances[node]:
            continue

        for t, b in graph[node].items():
            jb = jarak + b
            if jb < distances[t]:
                distances[t] = jb
                heapq.heappush(pq, (jb, t))

    return distances

hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for n, d in hasil.items():
    print("Bogor ->", n, "=", d)

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Node awal = Bogor
# 2. Paling dekat = Depok (2)
# 3. Paling jauh = Bandung (8)
# 4. Dijkstra bekerja dengan memilih jarak terkecil dulu

# Penjelasan:
# Program mencari jalur tercepat antar kota.

# Kesimpulan:
# Jalur terbaik adalah yang memiliki total bobot terkecil.
