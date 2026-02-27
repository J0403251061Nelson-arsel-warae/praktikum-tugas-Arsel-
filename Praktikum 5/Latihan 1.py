# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

# Fungsi rekursif untuk menghitung pangkat
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1)


# =======================
# Program Utama
# =======================

print("Program Menghitung Pangkat (Rekursi)")

# Input dari user
a = int(input("Masukkan angka dasar (a): "))
n = int(input("Masukkan pangkat (n): "))

# Memanggil fungsi
hasil = pangkat(a, n)

# Menampilkan hasil
print("\nHasil Perhitungan:")
print(a, "^", n, "=", hasil)
