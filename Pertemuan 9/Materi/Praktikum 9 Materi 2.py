#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 2 : membuat node Tree dengan child
#==================================================
#class node digunakan untuk dasar  dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B") #child kiri root
root.right = Node("C") #child kanan root

#membuat child level 2
root.left.left = Node("D") #child kiri B
root.left.right = Node("E") #child kanan B
root.right.left = Node("F") #child kiri C
root.right.right = Node("G") #child kanan C

#menampilkan isi node
print("Data pada root", root.data) # Output: A
print("Child kiri root", root.left) # Output: B
print("Child kanan root", root.right) # Output: C
print("Data child kiri B", root.left.left.data) # Output: D
print("Data child kanan B", root.left.right.data) # Output: E
print("Data child kiri C", root.right.left.data) # Output: F
print("Data child kanan C", root.right.right.data) # Output: G

#Pembahasan kode
#1. Kelas Node: Kelas ini tetap sama seperti pada latihan sebelumnya, mendefinisikan struktur dasar dari sebuah node dalam tree.
#2. Membuat Root: Kita membuat sebuah node root dengan nilai "A".
#3. Membuat Child Level 1: Kita menambahkan dua anak ke root, yaitu "B" sebagai child kiri dan "C" sebagai child kanan.
#4. Membuat Child Level 2: Kita menambahkan anak-anak ke node "B" dan "C". Node "B" memiliki anak "D" (kiri) dan "E" (kanan), sedangkan node "C" memiliki anak "F" (kiri) dan "G" (kanan).
#5. Menampilkan Isi Node: Kita mencetak data pada root, child kiri dan kanan