#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# =================================================
# Implementasi Prim
# =================================================

import heapq 
# Definisi graf dalam bentuk adjacency list dengan bobot (weight)
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

# Fungsi Prim untuk mencari Minimum Spanning Tree
def prim(graph, start): 
    # Set untuk menyimpan node yang sudah dikunjungi
    visited = set([start]) 
    # Heap untuk menyimpan edge dengan format (weight, node_awal, node_tujuan)
    edges = [] 
    # Masukkan semua edge dari node awal ke dalam heap
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    # List untuk menyimpan edge-edge yang termasuk dalam MST
    mst = [] 
    # Variabel untuk menghitung total bobot
    total_weight = 0 
    # Proses selama masih ada edge di dalam heap
    while edges: 
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges) 
        # Jika node tujuan belum dikunjungi
        if v not in visited: 
            # Tambahkan node tujuan ke dalam set visited
            visited.add(v) 
            # Tambahkan edge ke dalam MST
            mst.append((u, v, weight)) 
            # Akumulasi total bobot
            total_weight += weight 
            # Masukkan semua edge dari node tujuan ke dalam heap
            for neighbor, w in graph[v].items(): 
                # Hanya masukkan jika node neighbor belum dikunjungi
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
    # Kembalikan MST dan total bobot
    return mst, total_weight 
# Jalankan algoritma Prim dimulai dari node 'A'
mst, total = prim(graph, 'A') 
# Tampilkan hasil MST
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
# Tampilkan total bobot MST
print("Total bobot =", total)