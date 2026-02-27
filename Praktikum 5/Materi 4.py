# ==========================================================
# Backtracking 1: Kombinasi Biner (n)
# ==========================================================

# Fungsi backtracking untuk membuat kombinasi biner
def biner(n, hasil=""):
    # Base case: jika panjang string sudah sama dengan n
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore -> tambah '0'
    biner(n, hasil + "0")

    # Choose + Explore -> tambah '1'
    biner(n, hasil + "1")


# =======================
# Program Utama
# =======================

# Input dari user
n = int(input("Masukkan panjang kombinasi biner (n): "))

print("\nKombinasi biner yang dihasilkan:\n")

# Memanggil fungsi backtracking
biner(n)
