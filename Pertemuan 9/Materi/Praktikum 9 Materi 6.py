#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 6 : Struktur Organisasi Perusahaan
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
        
#membuat tree struktur organisasi perusahaan
root = Node("Direktur")

#Child level 1
root.left = Node("Manajer A") #child kiri direktur
root.right = Node("Manajer B") #child kanan direktur

#Child level 2
root.left.left = Node("Staff1") #child kiri Manajer A
root.left.right = Node("Staff2") #child kanan Manajer A

root.right.right = Node("Staff3") #child kanan Manajer B

#menjalankan traversal preorder untuk menampilkan struktur organisasi
print("Struktur Organisasi Perusahaan (Preorder):")
preorder(root) # Output: Direktur Manajer A Staff1 Staff2 Manajer B Staff3

#Pembahasan kode
#1. Kelas Node: Kelas ini tetap sama seperti pada latihan sebelumnya, mendefinisikan struktur dasar dari sebuah node dalam tree.
#2. Fungsi Preorder: Fungsi ini melakukan traversal preorder pada tree. Pertama, ia mengunjungi node saat ini (root), kemudian secara rekursif mengunjungi child kiri, dan akhirnya child kanan.    
#3. Membuat Tree Struktur Organisasi: Kita membuat sebuah tree yang merepresentasikan struktur organisasi perusahaan. Root adalah "Direktur", dengan dua child "Manajer A" dan "Manajer B". "Manajer A" memiliki dua child "Staff1" dan "Staff2", sedangkan "Manajer B" memiliki satu child "Staff3".
#4. Menjalankan Traversal Preorder: Kita memanggil fungsi preorder dengan root
