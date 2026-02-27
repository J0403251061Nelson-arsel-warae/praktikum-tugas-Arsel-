# ==========================================================
# Rekursi 3: Menjumlahkan Elemen List (Dengan Input & Tracing)
# ==========================================================

# Fungsi rekursif
def jumlah_list(data, index=0):
    # tracing saat fungsi dipanggil
    print("Masuk index ke-", index)

    # Base case
    if index == len(data):
        print("Mencapai akhir list -> kembali 0")
        return 0

    # Proses rekursif
    hasil = data[index] + jumlah_list(data, index + 1)

    # tracing saat kembali (unwinding)
    print("Keluar index ke-", index, "-> nilai sementara:", hasil)

    return hasil


# =======================
# Program Utama
# =======================

# Input dari user
input_user = input("Masukkan angka dipisahkan spasi: ")

# Mengubah input menjadi list integer
data_angka = list(map(int, input_user.split()))

# Memanggil fungsi rekursif
total = jumlah_list(data_angka)

# Menampilkan hasil akhir
print("\nData:", data_angka)
print("Jumlah semua elemen:", total)
