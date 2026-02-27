# ==========================================================
# Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return

    # Fase masuk (stacking)
    print("Masuk:", n)

    # Pemanggilan rekursif
    hitung(n - 1)

    # Fase keluar (unwinding)
    print("Keluar:", n)


# Program utama
hitung(3)
