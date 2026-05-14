# ==========================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : TPL/B2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 4 - Jaringan Kabel Antar Gedung
# ==========================================================

# ==========================================================
# DATA EDGE GEDUNG
# ==========================================================

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# ==========================================================
# SORTING EDGE
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

print("=== MST JARINGAN GEDUNG ===")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Algoritma yang digunakan adalah Kruskal.

# 2. Edge yang dipilih:
#    - GedungC - GedungD
#    - GedungA - GedungC
#    - GedungB - GedungD

# 3. Total biaya minimum adalah 6.

# 4. MST cocok digunakan karena dapat menghubungkan
#    seluruh gedung dengan biaya minimum tanpa cycle.
