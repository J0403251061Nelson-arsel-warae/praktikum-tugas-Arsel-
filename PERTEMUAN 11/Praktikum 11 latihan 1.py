#=================================================
#Nama : Nelson Arsel Warae 
#=================================================
from collections import deque

# Data graph lokasi
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

# Fungsi BFS
def bfs(graph, start):
    visited = set()          # Menyimpan node yang sudah dikunjungi
    queue = deque([start])   # Queue untuk BFS
    visited.add(start)

    urutan = []  # Menyimpan urutan kunjungan

    while queue:
        node = queue.popleft()   # Ambil node dari depan queue
        urutan.append(node)      # Simpan ke hasil

        # Cek semua tetangga
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return urutan

# Menjalankan BFS
hasil = bfs(graph, 'Rumah')

# Menampilkan hasil
print("BFS dari Rumah:")
for node in hasil:
    print(node, end=" ")

#1. Node mana yang dikunjungi pertama?
Node yang pertama dikunjungi adalah Rumah, karena BFS selalu dimulai dari node awal (start).

#2. Mengapa BFS cocok untuk mencari jalur terdekat?
#BFS cocok karena:
#BFS menjelajah per level (tingkat)
#Node yang paling dekat akan dikunjungi terlebih dahulu
#Sehingga BFS dapat menemukan jalur dengan langkah paling sedikit (terpendek)

#3. Apa perbedaan urutan BFS jika struktur graph diubah?
#Jika struktur graph diubah, maka:
#Urutan kunjungan BFS juga akan berubah
#Hal ini tergantung pada:
#hubungan antar node
#urutan tetangga dalam list
#Contoh: Jika 'Rumah': ['Toko', 'Sekolah'], maka urutan BFS menjadi: Rumah → Toko → Sekolah → Pasar → Perpustakaan
