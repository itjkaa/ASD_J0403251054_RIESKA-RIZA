#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# =================================================

# Class Node
class Node:  # Mendefinisikan class Node yang merepresentasikan setiap node dalam Binary Search Tree
    def __init__(self, data):  # Konstruktor untuk menginisialisasi node baru
        self.data = data  # Menyimpan nilai data pada node ini
        self.left = None  # Pointer ke child kiri, diinisialisasi sebagai None
        self.right = None  # Pointer ke child kanan, diinisialisasi sebagai None


# Fungsi preorder untuk melihat isi tree
def preorder(root):  # Fungsi traversal preorder untuk menampilkan data dalam urutan root-left-right
    if root is not None:  # Mengecek apakah root tidak None
        print(root.data, end=" ")  # Cetak data root
        preorder(root.left)  # Traversal ke subtree kiri
        preorder(root.right)  # Traversal ke subtree kanan


# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi untuk menampilkan struktur tree dengan indentasi
    if root is not None:  # Mengecek apakah root tidak None
        print("   " * level + f"{posisi}: {root.data}")  # Cetak posisi dan data dengan indentasi berdasarkan level
        tampil_struktur(root.left, level + 1, "L")  # Rekursif ke kiri dengan level +1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R")  # Rekursif ke kanan dengan level +1 dan posisi "R"


# Fungsi rotasi kiri
def rotate_left(x):  # Fungsi untuk melakukan rotasi kiri pada node x
    # x adalah root lama
    y = x.right       # y adalah child kanan x, akan menjadi root baru
    T2 = y.left       # T2 adalah subtree kiri milik y, disimpan sementara untuk dipindahkan

    # Proses rotasi
    y.left = x        # x menjadi child kiri dari y
    x.right = T2      # child kanan x diganti dengan T2

    # y menjadi root baru
    return y  # Mengembalikan y sebagai root baru setelah rotasi


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)  # Membuat node root dengan data 10
root.right = Node(20)  # Menambahkan child kanan dengan data 20
root.right.right = Node(30)  # Menambahkan child kanan dari 20 dengan data 30, membuat tree condong kanan

print("Preorder sebelum rotasi kiri:")  # Cetak label untuk output preorder sebelum rotasi
preorder(root)  # Panggil fungsi preorder untuk menampilkan traversal sebelum rotasi
print("\n\nStruktur sebelum rotasi kiri:")  # Cetak label untuk output struktur sebelum rotasi
tampil_struktur(root)  # Panggil fungsi tampil_struktur untuk menampilkan struktur sebelum rotasi

# Melakukan rotasi kiri pada root
root = rotate_left(root)  # Lakukan rotasi kiri pada root dan simpan hasilnya

print("\nPreorder sesudah rotasi kiri:")  # Cetak label untuk output preorder setelah rotasi
preorder(root)  # Panggil fungsi preorder untuk menampilkan traversal setelah rotasi
print("\n\nStruktur sesudah rotasi kiri:")  # Cetak label untuk output struktur setelah rotasi
tampil_struktur(root)  # Panggil fungsi tampil_struktur untuk menampilkan struktur setelah rotasi
