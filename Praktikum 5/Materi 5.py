# ==========================================================
# Backtracking 2:
# Kombinasi Biner dengan Batas Jumlah '1' (Pruning)
# ==========================================================

# Fungsi backtracking
def biner_batas(n, batas, hasil="", jumlah_1=0):
    # -------------------------
    # PRUNING
    # Jika jumlah '1' melebihi batas, hentikan cabang ini
    # -------------------------
    if jumlah_1 > batas:
        return

    # -------------------------
    # BASE CASE
    # Jika panjang string sudah n, tampilkan hasil
    # -------------------------
    if len(hasil) == n:
        print(hasil, "(jumlah 1 =", jumlah_1, ")")
        return

    # -------------------------
    # CHOOSE + EXPLORE
    # Pilih '0'
    # -------------------------
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # -------------------------
    # Pilih '1'
    # -------------------------
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# =======================
# Program Utama
# =======================

print("Program Kombinasi Biner dengan Batas Jumlah '1'")

# Input dari user
n = int(input("Masukkan panjang biner (n): "))
batas = int(input("Masukkan batas maksimum jumlah '1': "))

print("\nHasil kombinasi:\n")

# Memanggil fungsi
biner_batas(n, batas)
