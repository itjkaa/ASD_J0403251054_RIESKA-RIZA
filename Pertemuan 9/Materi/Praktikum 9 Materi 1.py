#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 1 : membuat node Tree
#==================================================
#class node digunakan untuk dasar  dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        
#membuat root
root = Node("A")
    
#menampilkan isi node
print("Data pada root", root.data) # Output: A
print("Child kiri root", root.left) # Output: None
print("Child kanan root", root.right) # Output: None

#Pembahasan kode
#1. Kelas Node: Kelas ini mendefinisikan struktur dasar dari sebuah node dalam tree. Setiap node memiliki atribut data untuk menyimpan nilai, serta left dan right untuk menyimpan referensi ke anak kiri dan kanan.
#2. Konstruktor __init__: Konstruktor ini digunakan untuk menginisialisasi objek Node. Saat sebuah node dibuat, data disimpan, dan left serta right diatur ke None.
#3. Membuat Root: Kita membuat sebuah node root dengan nilai "A". Ini adalah titik awal dari tree kita.
#4. Menampilkan Isi Node: Kita mencetak data pada root, serta child kiri dan kanan. Karena kita belum menambahkan anak ke root, child kiri dan kanan akan tetap None.