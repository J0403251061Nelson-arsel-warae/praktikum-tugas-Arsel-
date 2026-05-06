# ==========================================================
# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : TPL-B2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# Latihan 1: Weighted Graph dan Perhitungan Jalur

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Total bobot jalur A -> B -> D adalah:
#    A ke B = 4, B ke D = 5
#    Total = 4 + 5 = 9

# 2. Total bobot jalur A -> C -> D adalah:
#    A ke C = 2, C ke D = 1
#    Total = 2 + 1 = 3

# 3. Jalur yang dipilih sebagai jalur terpendek adalah:
#    A -> C -> D, karena memiliki total bobot lebih kecil (3 < 9)

# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit
#    karena setiap edge memiliki bobot (weight) yang berbeda.
#    Bisa saja jalur dengan lebih banyak edge memiliki total bobot lebih kecil.
#    Jadi, yang dihitung adalah total bobot, bukan jumlah langkah/jalur.
