# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 2: Implementasi Dijkstra

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Jarak terpendek dari A ke B:
#    = 4

# 2. Jarak terpendek dari A ke C:
#    = 2

# 3. Jarak terpendek dari A ke D:
#    Ada dua jalur:
#    A -> B -> D = 4 + 5 = 9
#    A -> C -> D = 2 + 1 = 3
#    Jadi jarak terpendek = 3

# 4. Jarak A ke D lebih kecil melalui C dibandingkan melalui B
#    karena total bobot jalur melalui C (2 + 1 = 3)
#    lebih kecil dibandingkan melalui B (4 + 5 = 9)

# 5. Fungsi priority_queue dalam algoritma Dijkstra:
#    Untuk menyimpan node yang akan diproses berdasarkan
#    jarak terkecil terlebih dahulu.

# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif
#    karena hasil perhitungan bisa menjadi tidak akurat.

# Kesimpulan:
# Algoritma Dijkstra mencari jalur terpendek berdasarkan total bobot terkecil.
