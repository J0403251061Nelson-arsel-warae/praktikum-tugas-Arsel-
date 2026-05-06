# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Materi 1: Weighted Graph

# Contoh representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

print("Misalnya Weighted Graph:")
for node, edges in graph.items():
    print(node, "->", edges)


# ==========================================================
# Penjelasan:
# ==========================================================
# Graph adalah struktur data yang terdiri dari node (simpul)
# dan edge (hubungan antar node).
#
# Weighted graph adalah graph yang setiap edge-nya memiliki
# bobot (weight), misalnya jarak, waktu, atau biaya.
#
# Contoh:
# A ke B = 4 artinya jarak dari A ke B adalah 4
#
# Kegunaan weighted graph:
# - Menentukan jalur tercepat
# - Menentukan biaya paling kecil
# - Digunakan dalam navigasi (Google Maps, dll)
#
# Pada Python, graph dapat direpresentasikan menggunakan
# dictionary bersarang seperti contoh di atas.
#
# ==========================================================
# Kesimpulan:
# Weighted graph digunakan untuk menyimpan hubungan antar node
# yang memiliki nilai bobot tertentu.
