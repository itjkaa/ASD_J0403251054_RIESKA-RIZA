#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# Praktikum 12 - Graph II: Shortest Path
#==================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
#==================================================

# representasi weighted graph
# graph adalah dictionary yang menyimpan node-node dan bobotnya.
# Setiap key adalah node, dan setiap value adalah dictionary
# yang berisi node tujuan dan bobot dari edge ke node tersebut.
graph = {
    'A': {'B': 4, 'C': 2},  # dari A ke B bobot 4, dari A ke C bobot 2
    'B': {'D': 5},          # dari B ke D bobot 5
    'C': {'D': 1},          # dari C ke D bobot 1
    'D': {}                 # D tidak memiliki tetangga lanjutan
}

# menghitung jalur
# jalur_1 adalah total bobot untuk rute A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D 
# jalur_2 adalah total bobot untuk rute A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

#==================================================
# Jawaban Analisis
#==================================================
# 1. A -> B -> D = 4 + 5 = 9
# 2. A -> C -> D = 2 + 1 = 3
# 3. Jalur terpendek: A -> C -> D
# 4. Karena yang dilihat adalah total bobot,
# bukan jumlah edge. Jalur lebih panjang bisa lebih murah.