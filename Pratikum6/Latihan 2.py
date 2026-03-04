def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # Mengisi bagian kosong pertama: Syarat perbandingan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        # Mengisi bagian kosong kedua: Penempatan key
        data[j + 1] = key
    
    return data


#Soal:
#1. Lengkapi kondisi agar menjadi sorting ascending.
#2. Ubah agar menjadi descending.


# jawaban
#1.Kondisi untuk Sorting Ascending (Kecil ke Besar)
#Untuk mengurutkan dari nilai terkecil ke terbesar, kita harus menggeser angka ke kanan jika angka di sebelah kiri lebih besar daripada key.
#Potongan Kode:while j >= 0 and data[j] > key:
#Penjelasan: Simbol > berarti jika angka di kiri (data[j]) lebih besar, maka ia akan minggir ke kanan untuk memberi jalan bagi angka yang lebih kecil (key).

#2.Kondisi untuk Sorting Descending (Besar ke Kecil)
#Untuk mengurutkan dari nilai terbesar ke terkecil, kita cukup membalik logika perbandingannya. Kita menggeser angka ke kanan jika angka di sebelah kiri lebih kecil daripada key.
#Potongan Kode:while j >= 0 and data[j] < key:
#Penjelasan: Simbol < berarti jika angka di kiri lebih kecil, maka ia akan digeser ke belakang agar angka yang lebih besar (key) bisa menempati posisi depan.
