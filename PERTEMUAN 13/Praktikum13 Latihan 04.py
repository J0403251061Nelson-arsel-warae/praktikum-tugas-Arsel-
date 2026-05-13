# Nama : Nelson Arsel Warae
# NIM : J0403251061
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree


# ==========================================================
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Prim
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'GedungA': {
        'GedungB': 4,
        'GedungC': 2,
        'GedungD': 5
    },

    'GedungB': {
        'GedungA': 4,
        'GedungD': 3
    },

    'GedungC': {
        'GedungA': 2,
        'GedungD': 1
    },

    'GedungD': {
        'GedungA': 5,
        'GedungB': 3,
        'GedungC': 1
    }
}


# Fungsi algoritma Prim
def prim(graph, start):

    # Node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_cost = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_cost += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_cost


# Menjalankan algoritma Prim
mst, total = prim(graph, 'GedungA')

print("Jaringan Kabel Minimum:\n")

for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Algoritma apa yang digunakan?
# Jawab:
# Algoritma yang digunakan adalah algoritma Prim.

# 2. Edge mana saja yang dipilih?
# Jawab:
# Edge yang dipilih adalah:
# GedungA - GedungC = 2
# GedungC - GedungD = 1
# GedungD - GedungB = 3

# 3. Berapa total biaya minimum?
# Jawab:
# Total biaya minimum yang dihasilkan adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
# Jawab:
# Karena MST dapat menghubungkan semua gedung
# dengan biaya paling minimum tanpa membentuk cycle,
# sehingga pemasangan kabel menjadi lebih efisien.
