def insertion_sort(data):
    # Dimulai dari indeks ke-1 karena elemen pertama dianggap sudah terurut
    for i in range(1, len(data)):
        key = data[i]  # Elemen yang akan disisipkan
        j = i - 1
        
        # Geser elemen yang lebih besar dari key ke posisi depan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        # Tempatkan key di posisi yang tepat
        data[j + 1] = key
    
    return data

# --- Bagian Pengujian ---
# Daftar angka yang belum terurut
angka = [12, 11, 13, 5, 6]

print("Data sebelum diurutkan:", angka)
hasil = insertion_sort(angka)
print("Data setelah diurutkan:", hasil)



#Soal:
#1. Mengapa perulangan dimulai dari indeks 1?
#2. Apa fungsi variabel key?
#3. Mengapa digunakan while, bukan for?
#4. Operasi apa yang terjadi di dalam while?


#jawaban
#1.Dalam algoritma Insertion Sort, kita mengasumsikan elemen pertama (indeks 0) sudah berada di posisi yang benar atau sudah "terurut" dengan sendirinya. Oleh karena itu, kita mulai mengambil elemen kedua (indeks 1) untuk dibandingkan dengan elemen-elemen sebelumnya.
#2.Variabel key berfungsi sebagai penampung sementara untuk nilai yang sedang kita ambil dari barisan data. Nilai ini perlu disimpan secara terpisah karena posisinya di dalam list/array mungkin akan ditimpa (di-overwritten) saat proses pergeseran angka lain berlangsung.
#3.Penggunaan while lebih fleksibel karena perulangan tersebut memiliki dua syarat sekaligus:
#Indeks j tidak boleh kurang dari 0 (batas kiri list).
#Nilai di posisi j harus lebih besar dari key.
#Jika salah satu syarat tersebut tidak terpenuhi, perulangan harus langsung berhenti. Menggunakan for akan lebih sulit karena for biasanya digunakan untuk jumlah iterasi yang sudah pasti.
#4.Operasi yang terjadi adalah Pergeseran (Shifting).
#Elemen yang lebih besar dari key digeser satu posisi ke kanan (data[j + 1] = data[j]). Hal ini dilakukan berulang kali sampai ditemukan posisi yang tepat (kosong) di mana key tidak lagi lebih kecil dari angka di kirinya.
