#=================================
#Nama :Nelson Arsel Warae 
#=================================
#===================================
# Data graph
#===================================
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi DFS
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Menjalankan DFS
visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)


# ================================
# Jawaban Pertanyaan Analisis
# ================================

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# Karena DFS menggunakan pendekatan rekursif (stack),
# sehingga algoritma akan terus masuk ke node berikutnya
# sampai mencapai node paling dalam sebelum kembali (backtracking).

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Jika urutan neighbor diubah, maka urutan kunjungan DFS juga berubah.
# Karena DFS mengikuti urutan list tetangga secara langsung.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# DFS: A B D E C F
# BFS: A B C D E F
# Perbedaannya:
# - DFS menelusuri sampai dalam dulu (depth-first)
# - BFS menelusuri per level (breadth-first)
