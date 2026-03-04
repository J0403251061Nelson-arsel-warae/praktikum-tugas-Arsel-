def merge(left, right):
    result = []
    i = 0
    j = 0
    
    # Membandingkan isi kedua list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Menambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(data):
    # Base case (jika data tinggal 1 atau kosong)
    if len(data) <= 1:
        return data
    
    # Membagi list menjadi dua bagian
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    # Menggabungkan kembali dengan fungsi merge
    return merge(left, right)


# Contoh penggunaan
data = [38, 27, 43, 3, 9, 82, 10]
hasil = merge_sort(data)

print("Data sebelum sorting:", data)
print("Data setelah sorting :", hasil)



#Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#2. Jelaskan fungsi result.extend().



#jawaban 

#1, Kondisi untuk Ascending
#Agar list terurut dari yang terkecil ke terbesar (ascending), kamu harus memastikan bahwa angka yang lebih kecil "menang" dan masuk ke list hasil lebih dulu.
#Isian yang benar:if left[i] < right[j]:
#Penjelasan: Program akan mengecek, "Apakah elemen di list kiri lebih kecil dari elemen di list kanan?". Jika Ya, maka elemen kiri diambil. Jika Tidak (berarti elemen kanan lebih kecil atau sama), maka elemen kanan yang diambil.

#2, Fungsi result.extend()
#Fungsi result.extend() digunakan untuk menyalin semua elemen yang tersisa dari list left atau right ke dalam result.
#Mengapa ini sangat penting?
#Dalam proses perbandingan di dalam while, perulangan akan berhenti segera setelah salah satu list (left atau right) habis. Namun, hampir selalu ada sisa elemen di list yang satunya lagi karena panjang list yang berbeda atau karena angka-angkanya memang lebih besar.
#result.extend(left[i:]): Mengambil semua sisa elemen di list kiri mulai dari indeks i sampai habis.
#result.extend(right[j:]): Mengambil semua sisa elemen di list kanan mulai dari indeks j sampai habis.
#Simulasi Sederhana
#Misalkan kita punya:
#left = [1, 5]
#right = [2, 3, 4]
#<!-- end list -->
#Bandingkan 1 dan 2 -> result = [1], i jadi 1.
#Bandingkan 5 dan 2 -> result = [1, 2], j jadi 1.
#Bandingkan 5 dan 3 -> result = [1, 2, 3], j jadi 2.
#Bandingkan 5 dan 4 -> result = [1, 2, 3, 4], j jadi 3.
#Stop! List right sudah habis (j = 3), tapi angka 5 di list left masih tertinggal.
#result.extend(left[1:]) akan mengambil angka 5 tersebut dan memasukkannya, sehingga hasil akhirnya lengkap: [1, 2, 3, 4, 5].
