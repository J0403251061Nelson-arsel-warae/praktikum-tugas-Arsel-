def merge_sort(data):
    # Base case: jika data hanya 1 atau kosong, sudah dianggap terurut
    if len(data) <= 1:
        return data
    
    # Divide: Membagi data menjadi dua bagian (kiri dan kanan)
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    # Rekursif: Urutkan bagian kiri dan kanan
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Conquer: Gabungkan kembali kedua bagian tersebut
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    
    # Bandingkan elemen dari kedua list dan masukkan yang terkecil ke result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Ambil sisa elemen jika ada (karena salah satu list mungkin lebih panjang)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# --- Pengujian ---
angka = [38, 27, 43, 3, 9, 82, 10]
print("Data sebelum diurutkan:", angka)
hasil = merge_sort(angka)
print("Data setelah diurutkan:", hasil)






#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?


# jawaban 
#1.Base case adalah kondisi paling sederhana yang menghentikan proses rekursif (perulangan fungsi). Dalam Merge Sort, base case terjadi saat sebuah list hanya memiliki 1 elemen atau kosong (len(data) <= 1).
#Logikanya: List dengan 1 angka sudah pasti terurut, jadi tidak perlu dibagi lagi dan fungsi bisa langsung mengembalikan (return) nilainya.

#2. Proses ini disebut Rekursi. Fungsi merge_sort memanggil dirinya sendiri untuk memecah masalah besar menjadi sub-masalah yang lebih kecil secara terus-menerus.
#Tujuannya: Agar kita bisa terus membagi list menjadi dua bagian (kiri dan kanan) sampai mencapai base case. Setelah semuanya pecah menjadi satuan kecil, barulah proses penggabungan yang teratur bisa dimulai.

#3. Fungsi merge() adalah inti dari tahap Conquer (Taklukkan/Gabungkan). Tujuannya adalah mengambil dua buah list yang sudah terurut (hasil pecahan tadi), lalu menyatukannya kembali menjadi satu list baru yang tetap terurut.
#Cara kerjanya: Fungsi ini membandingkan elemen terdepan dari list kiri dan list kanan, mengambil yang terkecil, dan menyusunnya satu per satu ke dalam hasil akhir.
#Ilustrasi Proses
#Sebagai analogi:
#Merge Sort (Rekursi): Seperti menebang pohon besar menjadi kayu-kayu kecil agar mudah diangkut.
#Base Case: Kayu sudah berukuran sekecil mungkin sehingga tidak bisa dipotong lagi.
#Merge: Seperti menyusun kembali kayu-kayu kecil tadi menjadi sebuah meja yang rapi.
