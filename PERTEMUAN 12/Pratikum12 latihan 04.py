# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 4: Studi Kasus Kampus jalur terpendek lokasi kampus 
# Algoritma:Di jkstra

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
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

hasil = dijkstra(graph, 'Gerbang')

for n, d in hasil.items():
    print(n, "=", d, "menit")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Kantin paling dekat (2 menit)
# 2. Ke Aula = 7 menit
# 3. Jalur langsung tidak selalu terbaik
# 4. Dijkstra cocok karena bobot positif

# Penjelasan:
# Program mencari waktu tercepat antar lokasi kampus.

# Kesimpulan:
# Jalur tercepat tidak selalu jalur langsung.
