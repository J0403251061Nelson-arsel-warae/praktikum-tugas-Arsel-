# ==========================================================
# Studi Kasus: Generator PIN (Backtracking)
# ==========================================================

# Fungsi generator PIN TANPA angka berulang
def buat_pin(panjang, hasil="", tersedia=None):
    # daftar angka yang boleh dipakai
    if tersedia is None:
        tersedia = ["0", "1", "2"]

    # Base case
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Choose + Explore
    for angka in tersedia:
        # angka yang sudah dipakai tidak boleh dipakai lagi
        sisa = tersedia.copy()
        sisa.remove(angka)

        buat_pin(panjang, hasil + angka, sisa)


# =======================
# Program Utama
# =======================

print("Program Generator PIN (Tanpa Angka Berulang)")

# Input dari user
panjang = int(input("Masukkan panjang PIN: "))

print("\nPIN yang dihasilkan:\n")

buat_pin(panjang)
