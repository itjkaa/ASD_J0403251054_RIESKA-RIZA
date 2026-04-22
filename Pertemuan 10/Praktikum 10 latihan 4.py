#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# =================================================

# Class Node untuk menyimpan data BST
class Node:  # Mendefinisikan class Node yang merepresentasikan setiap node dalam Binary Search Tree
    def __init__(self, data):  # Konstruktor untuk menginisialisasi node baru
        self.data = data      # Menyimpan nilai data pada node ini
        self.left = None      # Pointer ke child kiri, diinisialisasi sebagai None
        self.right = None     # Pointer ke child kanan, diinisialisasi sebagai None


# Fungsi insert untuk BST
def insert(root, data):  # Fungsi rekursif untuk menyisipkan data ke dalam BST
    # Jika root kosong, buat node baru
    if root is None:  # Mengecek apakah root adalah None, artinya tree kosong
        return Node(data)  # Membuat dan mengembalikan node baru dengan data tersebut

    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:  # Jika data lebih kecil dari data root, sisipkan ke kiri
        root.left = insert(root.left, data)  # Rekursif ke subtree kiri

    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:  # Jika data lebih besar dari data root, sisipkan ke kanan
        root.right = insert(root.right, data)  # Rekursif ke subtree kanan

    return root  # Mengembalikan root setelah penyisipan


# Fungsi preorder untuk melihat bentuk tree
def preorder(root):  # Fungsi traversal preorder untuk menampilkan data dalam urutan root-left-right
    if root is not None:  # Mengecek apakah root tidak None
        print(root.data, end=" ")  # Cetak data root
        preorder(root.left)  # Traversal ke subtree kiri
        preorder(root.right)  # Traversal ke subtree kanan


# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi untuk menampilkan struktur tree dengan indentasi
    if root is not None:  # Mengecek apakah root tidak None
        print("   " * level + f"{posisi}: {root.data}")  # Cetak posisi dan data dengan indentasi berdasarkan level
        tampil_struktur(root.left, level + 1, "L")  # Rekursif ke kiri dengan level +1 dan posisi "L"
        tampil_struktur(root.right, level + 1, "R")  # Rekursif ke kanan dengan level +1 dan posisi "R"


# -----------------------------
# Program utama
# -----------------------------
root = None  # Inisialisasi root sebagai None, menandakan tree kosong
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]  # List data yang akan disisipkan dalam urutan naik
for data in data_list:  # Loop untuk setiap data dalam list
    root = insert(root, data)  # Sisipkan data ke BST menggunakan fungsi insert

print("Preorder BST:")  # Cetak label untuk output preorder
preorder(root)  # Panggil fungsi preorder untuk menampilkan traversal
print("\n\nStruktur BST:")  # Cetak label untuk output struktur
tampil_struktur(root)  # Panggil fungsi tampil_struktur untuk menampilkan struktur tree

# Penjelasan:
# - Tree condong ke kanan: Karena data dimasukkan dalam urutan naik (10, 20, 30),
#   semua node baru akan dimasukkan ke subtree kanan, sehingga tree menjadi condong ke kanan.
# - Semakin panjang tree, pencarian bisa makin lambat: Dalam tree yang tidak seimbang seperti ini,
#   pencarian dapat mencapai kompleksitas O(n) dalam kasus terburuk, bukan O(log n) seperti pada tree seimbang.
# - BST tidak selalu seimbang: Binary Search Tree tidak menjamin keseimbangan otomatis;
#   keseimbangan tergantung pada urutan penyisipan data.
