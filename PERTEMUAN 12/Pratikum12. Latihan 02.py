# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 2: Dijkstra

import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        jarak, node = heapq.heappop(pq)

        if jarak > distances[node]:
            continue

        for tetangga, bobot in graph[node].items():
            jarak_baru = jarak + bobot
            if jarak_baru < distances[tetangga]:
                distances[tetangga] = jarak_baru
                heapq.heappush(pq, (jarak_baru, tetangga))

    return distances

hasil = dijkstra(graph, 'A')

for n, d in hasil.items():
    print(n, "=", d)

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. A ke B = 4
# 2. A ke C = 2
# 3. A ke D = 3
# 4. Karena lewat C lebih kecil (2+1)
# 5. Priority queue memilih jarak terkecil dulu
# 6. Tidak cocok untuk bobot negatif

# Penjelasan:
# Dijkstra bekerja dengan memilih node terdekat terlebih dahulu.

# Kesimpulan:
# Dijkstra efisien untuk graph berbobot positif.
