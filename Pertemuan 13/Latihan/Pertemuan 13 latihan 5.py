# ==========================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 5 - Kasus Jaringan Jalan Antar Kota
# ==========================================================

# ==========================================================
# DATA EDGE
# ==========================================================

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# ==========================================================
# MENGURUTKAN EDGE
# ==========================================================

edges.sort()

mst = []

total_weight = 0

connected = set()

# ==========================================================
# PROSES KRUSKAL
# ==========================================================

for weight, u, v in edges:

    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_weight += weight

        connected.add(u)
        connected.add(v)

# ==========================================================
# OUTPUT
# ==========================================================

print("=== MINIMUM SPANNING TREE ===")

for edge in mst:
    print(edge)

print("Total bobot minimum =", total_weight)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Kasus yang dipilih adalah jaringan jalan antar kota.

# 2. Algoritma yang digunakan adalah Kruskal.

# 3. Edge yang dipilih:
#    - Bogor - Depok
#    - Depok - Jakarta
#    - Depok - Bandung

# 4. Total bobot MST adalah 9.

# 5. Edge tertentu tidak dipilih karena dapat
#    menyebabkan cycle dan memiliki bobot lebih besar.