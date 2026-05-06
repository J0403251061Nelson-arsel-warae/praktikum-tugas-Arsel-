# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
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
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi yang paling dekat dari Gerbang:
#    Kantin = 2 menit (paling kecil dibanding lainnya)

# 2. Waktu tempuh terpendek dari Gerbang ke Aula:
#    Jalur:
#    Gerbang -> Kantin -> Lab -> Aula
#    = 2 + 4 + 1 = 7 menit

# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil
#    Contoh:
#    Gerbang -> Kantin -> Aula = 2 + 7 = 9 menit
#    Tetapi jalur lain:
#    Gerbang -> Kantin -> Lab -> Aula = 7 menit (lebih cepat)
#    Jadi jalur tidak langsung bisa lebih efisien

# 4. Dijkstra cocok digunakan pada kasus ini karena:
#    - Semua bobot bernilai positif (waktu tempuh)
#    - Ingin mencari jalur tercepat (terpendek)
#    - Algoritma ini efisien untuk kasus seperti peta lokasi

# Kesimpulan:
# Algoritma Dijkstra membantu menentukan jalur tercepat antar lokasi
# berdasarkan total waktu tempuh terkecil.
