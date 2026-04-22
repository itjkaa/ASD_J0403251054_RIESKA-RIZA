#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
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


# Fungsi rotasi kanan
def rotate_right(y):  # Fungsi untuk melakukan rotasi kanan pada node y
    # y adalah root lama
    x = y.left        # x adalah child kiri y, akan menjadi root baru
    T2 = x.right      # T2 adalah subtree kanan milik x, disimpan sementara untuk dipindahkan

    # Proses rotasi
    x.right = y       # y menjadi child kanan dari x
    y.left = T2       # child kiri y diganti dengan T2

    # x menjadi root baru
    return x  # Mengembalikan x sebagai root baru setelah rotasi


# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10
root = Node(30)  # Membuat node root dengan data 30
root.left = Node(20)  # Menambahkan child kiri dengan data 20
root.left.left = Node(10)  # Menambahkan child kiri dari 20 dengan data 10, membuat tree condong kiri

print("Preorder sebelum rotasi kanan:")  # Cetak label untuk output preorder sebelum rotasi
preorder(root)  # Panggil fungsi preorder untuk menampilkan traversal sebelum rotasi
print("\n\nStruktur sebelum rotasi kanan:")  # Cetak label untuk output struktur sebelum rotasi
tampil_struktur(root)  # Panggil fungsi tampil_struktur untuk menampilkan struktur sebelum rotasi

# Melakukan rotasi kanan pada root
root = rotate_right(root)  # Lakukan rotasi kanan pada root dan simpan hasilnya

print("\nPreorder sesudah rotasi kanan:")  # Cetak label untuk output preorder setelah rotasi
preorder(root)  # Panggil fungsi preorder untuk menampilkan traversal setelah rotasi
print("\n\nStruktur sesudah rotasi kanan:")  # Cetak label untuk output struktur setelah rotasi
tampil_struktur(root)  # Panggil fungsi tampil_struktur untuk menampilkan struktur setelah rotasi
