# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 1: Weighted Graph dan Perhitungan Jalur

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Total bobot A -> B -> D = 4 + 5 = 9
# 2. Total bobot A -> C -> D = 2 + 1 = 3
# 3. Jalur terpendek = A -> C -> D
# 4. Jalur terpendek tidak berdasarkan jumlah edge,
#    tetapi berdasarkan total bobot terkecil.

# Penjelasan:
# Program menghitung dua jalur berbeda dan membandingkan hasilnya.

# Kesimpulan:
# Jalur terbaik adalah yang memiliki total bobot paling kecil.
