# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree


# ==========================================================
# Latihan 5 - Tugas Mandiri MST
# Kasus 1 : Jaringan Jalan Antar Kota
# Menggunakan Algoritma Kruskal
# ==========================================================


# Daftar edge: (bobot, node1, node2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal sederhana
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal bobot minimum =", total_weight)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Kasus apa yang dipilih?
# Jawab:
# Kasus yang dipilih adalah Jaringan Jalan Antar Kota.

# 2. Algoritma apa yang digunakan?
# Jawab:
# Algoritma yang digunakan adalah algoritma Kruskal.

# 3. Edge mana saja yang dipilih dalam MST?
# Jawab:
# Edge yang dipilih adalah:
# Bogor - Depok = 2
# Depok - Jakarta = 3
# Depok - Bandung = 4

# 4. Berapa total bobot MST?
# Jawab:
# Total bobot MST adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
# Jawab:
# Karena edge tersebut dapat membentuk cycle
# atau memiliki bobot lebih besar dibandingkan
# edge lain yang sudah dipilih.
