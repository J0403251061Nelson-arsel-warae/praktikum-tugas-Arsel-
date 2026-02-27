# ==========================================================
# Latihan 4: Kombinasi Huruf (Backtracking)
# ==========================================================

# Fungsi untuk membuat kombinasi huruf A dan B
def kombinasi(n, hasil=""):
    # Base case
    if len(hasil) == n:
        print(hasil)
        return 1  # menghitung jumlah kombinasi

    # Choose + Explore
    jumlah = 0
    jumlah += kombinasi(n, hasil + "A")
    jumlah += kombinasi(n, hasil + "B")

    return jumlah


# =======================
# Program Utama
# =======================

print("Program Kombinasi Huruf A dan B")

# Input dari user
n = int(input("Masukkan panjang kombinasi: "))

print("\nKombinasi yang dihasilkan:\n")

# Memanggil fungsi
total = kombinasi(n)

# Menampilkan jumlah kombinasi
print("\nTotal kombinasi:", total)
