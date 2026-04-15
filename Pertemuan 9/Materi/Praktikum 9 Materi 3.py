#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 3 : membuat Traversal Preorder
#==================================================
#class node digunakan untuk dasar  dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Preorder : Root ==> Left ==> Right
def preorder(node):
    if node is not None: #jika node tidak kosong
        print(node.data, end=" ") #kunjungi root
        preorder(node.left) #rekursif ke child kiri
        preorder(node.right) #rekursif ke child kanan

#membuat tree
#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B") #child kiri root
root.right = Node("C") #child kanan root

#membuat child level 2
root.left.left = Node("D") #child kiri B
root.left.right = Node("E") #child kanan B

#menjalankan traversal preorder
print(" Hasil Traversal Preorder:")
preorder(root) # Output: A B D E C

#Pembahasan kode
#1. Kelas Node: Kelas ini tetap sama seperti pada latihan sebelumnya, mendefinisikan struktur dasar dari sebuah node dalam tree.
#2. Fungsi Preorder: Fungsi ini melakukan traversal preorder pada tree. Pertama, ia mengunjungi node saat ini (root), kemudian secara rekursif mengunjungi child kiri, dan akhirnya child kanan.    
#3. Membuat Tree: Kita membuat sebuah tree dengan root "A", child "B" dan "C", serta child "D" dan "E" di bawah "B".
#4. Menjalankan Traversal Preorder: Kita memanggil fungsi preorder dengan root sebagai argumen, yang menghasilkan urutan kunjungan A B D E C sesuai dengan aturan preorder.
