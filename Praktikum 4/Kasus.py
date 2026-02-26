#=====================================================================================================
#nama :Nelson Arsel warae
#Nim :J0403251061
#Kelas :B2
#=======================================================================================================

#======================================================================================================
#study kasus: sistem antrian layanan akademik 
#impementasi Queue =>
#Enqueue : memindahkan pointer rear (data baru di belakang)
#Dequeue : memindahkan data front (menghapus data dari depan)
# front ->  A -> B -> C -> rear
#======================================================================================================


#1) mendefinisikan node (unit dasar linked list)
class node:
    def __init__(self, nim, nama):   #  perbaikan __init__
        self.nim   = nim
        self.nama  = nama
        self.next  = None


#2) mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):   #  perbaikan __init__
        self.front = None
        self.rear = None

    def is_empty(self):   #  keluar dari __init__
        return self.front is None

    def enqueue(self, nim, nama):   #  perbaikan parameter
        Nodebaru = node(nim, nama)

        if self.is_empty():
            self.front = Nodebaru
            self.rear = Nodebaru
            return

        self.rear.next = Nodebaru
        self.rear = Nodebaru

    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():   #  perbaikan penulisan
            print("Antrian kosong. tidak ada mahasiswa dilayani")
            return None
        
        Node_dilayani = self.front
        self.front = self.front.next

        if self.front is None:   #  perbaikan None
            self.rear = None

        return Node_dilayani

    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")

        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1


#program utama 
def main():

    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim, nama)   #  perbaikan pemanggilan
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":   #  perbaikan duplikat menu
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. Terima Kasih")
            break

        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")


#penanda eksekusi file utama
if __name__ == "__main__":
    main()
