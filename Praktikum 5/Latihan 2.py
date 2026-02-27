# ==========================================================
# Latihan 2: Tracing Rekursi (Countdown)
# ==========================================================

# Fungsi rekursif countdown
def countdown(n):
    # Base case
    if n == 0:
        print("Selesai")
        return

    # Fase masuk (stacking)
    print("Masuk :", n)

    # Pemanggilan rekursif
    countdown(n - 1)

    # Fase keluar (unwinding)
    print("Keluar:", n)


# =======================
# Program Utama
# =======================

print("Program Tracing Rekursi Countdown")

# Input dari user
angka = int(input("Masukkan angka awal: "))

print("\nProses Rekursi:\n")
# Memanggil fungsi
countdown(angka)
