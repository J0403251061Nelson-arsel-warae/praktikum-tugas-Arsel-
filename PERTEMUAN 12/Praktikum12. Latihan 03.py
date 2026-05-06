# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 3: Implementasi Bellman-Ford

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Bobot langsung dari A ke B:
#    = 5

# 2. Total bobot jalur A -> C -> B:
#    A ke C = 4
#    C ke B = -2
#    Total = 4 + (-2) = 2

# 3. Jalur yang menghasilkan jarak lebih kecil menuju B:
#    A -> C -> B (total = 2), lebih kecil dibanding langsung (5)

# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif
#    karena algoritma ini mengecek semua kemungkinan jalur berulang kali
#    (relaksasi), sehingga tetap bisa menemukan jarak minimum
#    meskipun ada bobot negatif.

# 5. Relaksasi edge adalah proses memperbarui jarak terpendek
#    jika ditemukan jalur baru yang lebih kecil.
#    Contoh:
#    jika jarak lama lebih besar dari jarak baru,
#    maka jarak diperbarui.

# 6. Perbedaan utama Bellman-Ford dan Dijkstra:
#    - Bellman-Ford:
#      Bisa menangani bobot negatif, tapi lebih lambat
#    - Dijkstra:
#      Lebih cepat, tapi tidak bisa menangani bobot negatif

# Kesimpulan:
# Bellman-Ford cocok digunakan untuk graph dengan bobot negatif
# karena mampu menemukan jalur terpendek secara akurat.
