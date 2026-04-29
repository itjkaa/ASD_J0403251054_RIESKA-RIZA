#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Implementasi BFS pada Graph
# =================================================
#representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
    #Fungsi untuk melakukan penelusuran DFS pada graph
    #graph: dictionary yang menyimpan struktur dari graph
    #node: node saat ini yang sedang diproses dalam DFS
    #visited: menyimpan node yang sudah dikunjungi untuk menghindari siklus dan pengulangan
    
    #tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)
    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")
    
    #periksa setiap tetangga dari node yang sedang diproses
    for neighbor in graph[node]:
        #jika tetangga belum dikunjungi, lakukan DFS secara rekursif
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#set visited
visited = set()
#memanggil fungsi DFS dengan graph dan node awal 'A'
dfs(graph, "A", visited)