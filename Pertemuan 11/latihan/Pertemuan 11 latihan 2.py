#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Implementasi DFS pada Graph
#==================================================

# representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran DFS
    # graph: struktur graph
    # node: node yang sedang dikunjungi
    # visited: set untuk menyimpan node yang sudah dikunjungi
    
    # tandai node sebagai sudah dikunjungi
    visited.add(node)
    # tampilkan node
    print("Mengunjungi node:", node)
    
    # telusuri semua tetangga
    for neighbor in graph[node]:
        # jika belum dikunjungi
        if neighbor not in visited:
            # panggil DFS secara rekursif
            dfs(graph, neighbor, visited)

# inisialisasi visited
visited = set()

# menjalankan DFS dari node "A"
print("DFS dari A:")
dfs(graph, 'A', visited)


#==================================================
# Jawaban Pertanyaan Analisis DFS
#==================================================
# 1. DFS masuk ke node terdalam terlebih dahulu
# karena menggunakan rekursi (stack),
# sehingga terus turun sampai tidak ada cabang.

# 2. Jika urutan neighbor diubah,
# maka urutan traversal DFS juga berubah.

# 3. Perbandingan BFS dan DFS:
# BFS -> menyebar per level (shortest path)
# DFS -> masuk ke dalam dulu (eksplorasi jalur)
# hasil urutannya biasanya berbeda.