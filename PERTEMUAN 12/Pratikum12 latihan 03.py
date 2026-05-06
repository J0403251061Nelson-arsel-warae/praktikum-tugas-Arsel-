# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 3: implementasi Bellman-Ford

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for tetangga, bobot in graph[node].items():
                if distances[node] + bobot < distances[tetangga]:
                    distances[tetangga] = distances[node] + bobot

    return distances

hasil = bellman_ford(graph, 'A')

for n, d in hasil.items():
    print(n, "=", d)

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. A ke B langsung = 5
# 2. A -> C -> B = 2
# 3. Jalur terbaik lewat C
# 4. Bisa handle bobot negatif
# 5. Relaksasi = update jarak lebih kecil
# 6. Bedanya dengan Dijkstra ada di bobot negatif

# Penjelasan:
# Bellman-Ford mengecek semua edge berulang kali.

# Kesimpulan:
# Cocok untuk graph dengan bobot negatif.
