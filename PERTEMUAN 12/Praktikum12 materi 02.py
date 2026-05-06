# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Materi 2: Shortest Path (Jalur Terpendek)

# Contoh sederhana jalur:
# A -> B -> D
# A -> C -> D

# ==========================================================
# Penjelasan:
# ==========================================================
# Shortest path adalah jalur dengan total bobot paling kecil
# dari satu node ke node lain.
#
# Dalam weighted graph, kita tidak mencari jumlah langkah
# paling sedikit, tetapi jumlah bobot paling kecil.
#
# Contoh:
# A -> B -> D = 4 + 5 = 9
# A -> C -> D = 2 + 1 = 3
# Maka jalur terpendek adalah A -> C -> D
#
# Algoritma yang digunakan:
#
# 1. Dijkstra
#    - Digunakan untuk graph dengan bobot positif
#    - Lebih cepat dan efisien
#
# 2. Bellman-Ford
#    - Digunakan untuk graph dengan bobot negatif
#    - Lebih fleksibel tetapi lebih lambat
#
# Perbedaan utama:
# - Dijkstra tidak bisa menangani bobot negatif
# - Bellman-Ford bisa menangani bobot negatif
#
# ==========================================================
# Kesimpulan:
# Shortest path adalah konsep penting untuk menentukan
# jalur tercepat atau paling efisien dalam suatu graph.
