# ==========================================================
# Latihan 3: Mencari Nilai Maksimum (Rekursi)
# ==========================================================

# Fungsi rekursif mencari nilai maksimum dalam list
def cari_maks(data, index=0):
    # Base case: jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari maksimum sisa elemen
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


# =======================
# Program Utama
# =======================

print("Program Mencari Nilai Maksimum (Rekursi)")

# Input dari user
input_user = input("Masukkan angka dipisahkan spasi: ")

# Ubah input menjadi list integer
angka = list(map(int, input_user.split()))

# Memanggil fungsi
hasil = cari_maks(angka)

# Menampilkan hasil
print("\nData:", angka)
print("Nilai maksimum:", hasil)
