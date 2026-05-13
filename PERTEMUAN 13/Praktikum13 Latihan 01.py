# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree


# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")

for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
# Jawab:
# Graph awal berisi semua edge yang ada pada graph.
# Sedangkan spanning tree hanya mengambil beberapa edge
# yang diperlukan untuk menghubungkan semua node tanpa cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Jawab:
# Karena spanning tree harus berbentuk tree.
# Jika ada cycle, maka graph tidak lagi menjadi tree.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jawab:
# Karena spanning tree hanya mengambil edge minimum
# untuk menghubungkan semua node.
# Pada graph dengan n node, spanning tree selalu memiliki
# n - 1 edge.
