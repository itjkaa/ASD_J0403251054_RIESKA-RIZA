#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 5 : membuat Trversal Postorder
#==================================================
#class node digunakan untuk dasar  dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#Fungsi Postorder : Left ==> Right ==> Root
def postorder(node):
    if node is not None: #jika node tidak kosong
        postorder(node.left) #rekursif ke child kiri
        postorder(node.right) #rekursif ke child kanan
        print(node.data, end=" ") #kunjungi root
        
#membuat tree
#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B") #child kiri root
root.right = Node("C") #child kanan root

#membuat child level 2
root.left.left = Node("D") #child kiri B
root.left.right = Node("E") #child kanan B

#menjalankan traversal postorder
print(" Hasil Traversal Postorder:")
postorder(root) # Output: D E B C A

#Pembahasan kode
#1. Kelas Node: Kelas ini tetap sama seperti pada latihan sebelumnya, mendefinisikan struktur dasar dari sebuah node dalam tree.
#2. Fungsi Postorder: Fungsi ini melakukan traversal postorder pada tree. Pertama, ia secara rekursif mengunjungi child kiri, kemudian secara rekursif mengunjungi child kanan, dan akhirnya mengunjungi node saat ini (root).    
#3. Membuat Tree: Kita membuat sebuah tree dengan root "A", child "B" dan "C", serta child "D" dan "E" di bawah "B".
#4. Menjalankan Traversal Postorder: Kita memanggil fungsi postorder dengan root sebagai argumen, yang menghasilkan urutan kunjungan D E B C A sesuai dengan aturan postorder.