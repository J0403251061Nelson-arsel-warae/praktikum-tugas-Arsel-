# ==========================================================
# Rekursi 1: Faktorial
# ==========================================================

# Fungsi faktorial rekursif
def faktorial(n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return n * faktorial(n - 1)

# Program utama
angka = 5
hasil = faktorial(angka)

# Menampilkan hasil
print("Faktorial dari", angka, "adalah", hasil)
