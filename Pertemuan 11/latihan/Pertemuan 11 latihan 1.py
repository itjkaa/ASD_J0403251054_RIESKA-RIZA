#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Implementasi BFS pada Graph
#==================================================

from collections import deque

# representasi graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran BFS pada graph
    # graph: dictionary yang menyimpan struktur graph
    # start: node awal
    
    # queue digunakan untuk menyimpan node yang akan diproses
    queue = deque()
    # visited untuk menyimpan node yang sudah dikunjungi
    visited = set()
    
    # masukkan node awal ke queue
    queue.append(start)
    # tandai node awal sudah dikunjungi
    visited.add(start)

    while queue:
        # ambil node paling depan dari queue
        node = queue.popleft()
        # tampilkan node yang sedang dikunjungi
        print("Mengunjungi node:", node)
        
        # cek semua tetangga dari node
        for neighbor in graph[node]:
            # jika belum dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan ke queue
                queue.append(neighbor)

# menjalankan BFS dari node "Rumah"
print("BFS dari Rumah:")
bfs(graph, 'Rumah')


#==================================================
# Jawaban Pertanyaan Analisis BFS
#==================================================
# 1. Node pertama yang dikunjungi adalah "Rumah",
# karena BFS dimulai dari node awal.

# 2. BFS cocok untuk mencari jalur terdekat karena
# menelusuri graph secara melebar (level per level),
# sehingga node terdekat dikunjungi lebih dulu.

# 3. Jika urutan neighbor diubah,
# maka urutan hasil BFS juga bisa berubah
# karena bergantung pada isi queue.