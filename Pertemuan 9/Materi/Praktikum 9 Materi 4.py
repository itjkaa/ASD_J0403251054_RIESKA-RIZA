#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 4 : membuat Trversal Inorder
#==================================================
#class node digunakan untuk dasar  dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Inorder : Left ==> Root ==> Right
def inorder(node):
    if node is not None: #jika node tidak kosong
        inorder(node.left) #rekursif ke child kiri
        print(node.data, end=" ") #kunjungi root
        inorder(node.right) #rekursif ke child kanan
        
#membuat tree
#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B") #child kiri root
root.right = Node("C") #child kanan root

#membuat child level 2
root.left.left = Node("D") #child kiri B
root.left.right = Node("E") #child kanan B

#menjalankan traversal inorder
print(" Hasil Traversal Inorder:")
inorder(root) # Output: D B E A C

#Pembahasan kode
#1. Kelas Node: Kelas ini tetap sama seperti pada latihan sebelumnya, mendefinisikan struktur dasar dari sebuah node dalam tree.
#2. Fungsi Inorder: Fungsi ini melakukan traversal inorder pada tree. Pertama, ia secara rekursif mengunjungi child kiri, kemudian mengunjungi node saat ini (root), dan akhirnya secara rekursif mengunjungi child kanan.    
#3. Membuat Tree: Kita membuat sebuah tree dengan root "A", child "B" dan "C", serta child "D" dan "E" di bawah "B".
#4. Menjalankan Traversal Inorder: Kita memanggil fungsi inorder dengan root sebagai argumen, yang menghasilkan urutan kunjungan D B E A C sesuai dengan aturan inorder.