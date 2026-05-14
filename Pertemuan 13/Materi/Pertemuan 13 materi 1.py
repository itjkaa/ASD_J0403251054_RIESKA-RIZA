#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# ========================================================== 
# Implementasi Kruskal 
# Algoritma untuk mencari Minimum Spanning Tree (MST)
# ========================================================== 

# Daftar edge: (bobot, node1, node2) 
# Setiap tuple berisi berat edge dan dua node yang terhubung
edges = [ 
(1, 'C', 'D'), 
(2, 'A', 'C'), 
(3, 'B', 'D'), 
(4, 'A', 'B'), 
(5, 'A', 'D') 
]
# Mengurutkan edge berdasarkan bobot 
edges.sort() 

# List untuk menyimpan edge yang termasuk dalam MST
mst = [] 
# Variabel untuk menghitung total bobot MST
total_weight = 0 

# Set sederhana untuk menyimpan node yang sudah dipilih
connected = set() 

# Iterasi setiap edge mulai dari bobot terkecil
for weight, u, v in edges: 

    # Jika edge tidak membentuk cycle sederhana 
    if u not in connected or v not in connected: 

        # Tambahkan edge ke MST
        mst.append((u, v, weight)) 
        # Tambahkan bobot edge ke total
        total_weight += weight 

        # Tandai kedua node sebagai sudah dipilih
        connected.add(u) 
        connected.add(v) 

# Tampilkan hasil MST
print("Minimum Spanning Tree:") 

# Cetak setiap edge dalam MST
for edge in mst: 
    print(edge) 

# Cetak total bobot MST
print("Total bobot =", total_weight)