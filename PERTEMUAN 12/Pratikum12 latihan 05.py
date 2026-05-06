# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra

import heapq

# ==========================================================
# 1. Representasi graph berbobot (dictionary)
# ==========================================================
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# ==========================================================
# 2. Fungsi Dijkstra
# ==========================================================
def dijkstra(graph, start):
    # Inisialisasi jarak awal semua node tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak ke node awal = 0
    distances[start] = 0

    # Priority queue untuk memilih jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika bukan jarak terbaik
        if current_distance > distances[current_node]:
            continue

        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ==========================================================
# 3. Node awal
# ==========================================================
start_node = 'Bogor'

# ==========================================================
# 4. Menjalankan program dan output
# ==========================================================
hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")
for node, distance in hasil.items():
    print("Bogor ->", node, "=", distance)


# ==========================================================
# 5. Jawaban Analisis
# ==========================================================

# 1. Node awal yang digunakan:
#    Bogor

# 2. Node dengan jarak paling kecil dari node awal:
#    Depok = 2

# 3. Node dengan jarak paling besar dari node awal:
#    Bandung = 8

# 4. Cara kerja algoritma Dijkstra pada kasus ini:
#    - Dimulai dari Bogor dengan jarak 0
#    - Mengecek semua tetangga (Jakarta dan Depok)
#    - Memilih jalur dengan jarak terkecil terlebih dahulu (Depok)
#    - Dari Depok, menghitung jalur baru ke Jakarta dan Bandung
#    - Membandingkan semua kemungkinan jalur
#    - Terus mengupdate jarak jika ditemukan yang lebih kecil
#    - Hasil akhir adalah jarak terpendek ke semua kota

# Kesimpulan:
# Dijkstra mencari jalur tercepat dengan memilih jalur
# dengan total bobot terkecil secara bertahap.
