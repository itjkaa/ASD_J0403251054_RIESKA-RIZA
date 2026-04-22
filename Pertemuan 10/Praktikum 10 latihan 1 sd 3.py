#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 1 : BST (Binary Search Tree)
#==================================================
class Node:  # Mendefinisikan class Node untuk merepresentasikan node dalam BST
    def __init__(self, data):  # Konstruktor untuk inisialisasi node
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan
        
def insert(root, data):  # Fungsi rekursif untuk menyisipkan data ke BST
    if root is None:  # Jika root kosong, buat node baru
        return Node(data)  # Mengembalikan node baru
    
    if data < root.data:  # Jika data lebih kecil dari root, sisipkan ke kiri
        root.left = insert(root.left, data)  # Rekursif ke subtree kiri
    elif data > root.data:  # Jika data lebih besar dari root, sisipkan ke kanan
        root.right = insert(root.right, data)  # Rekursif ke subtree kanan
    return root  # Mengembalikan root setelah penyisipan

# mengisi data ke dalam BST
root = None  # Inisialisasi root sebagai None
data_list = [50, 30, 70, 20, 40, 50, 80]  # List data yang akan disisipkan

for data in data_list:  # Loop untuk setiap data dalam list
    root = insert(root, data)  # Sisipkan data ke BST

print("BST berhasil dibuat")  # Cetak pesan bahwa BST berhasil dibuat

#==================================================
# Latihan 2 : Traversal inorder pada BST
#==================================================
# alur fungsi inorder:
# 1. Basis Kasus: Jika node saat ini (root) adalah None, fungsi akan berhenti dan kembali ke pemanggil sebelumnya.
# 2. Rekursi Kiri: Fungsi memanggil dirinya sendiri untuk menelusuri subtree kiri dari node saat ini. Ini memastikan bahwa semua node di subtree kiri akan diproses terlebih dahulu.
# 3. Proses Node: Setelah menyelesaikan penelusuran subtree kiri, fungsi akan mencetak data dari node saat ini. Ini adalah titik di mana kita mengakses nilai node setelah memastikan bahwa semua node di sebelah kiri telah diproses.
# 4. Rekursi Kanan: Setelah mencetak data node saat ini, fungsi memanggil dirinya sendiri untuk menelusuri subtree kanan dari node saat ini. Ini memastikan bahwa semua node di subtree kanan akan diproses setelah node saat ini.
def inorder(root):  # Fungsi traversal inorder untuk menampilkan data dalam urutan kiri-root-kanan
    if root is not None:  # Mengecek apakah root tidak None
        inorder(root.left)  # Rekursif ke subtree kiri
        print(root.data, end=' ')  # Cetak data root
        inorder(root.right)  # Rekursif ke subtree kanan
        
print("hasil inorder: ")  # Cetak label untuk hasil inorder
inorder(root)  # Panggil fungsi inorder, Output: 20 30 40 50 70 80
#==================================================
# Latihan 3 : searching pada BST
#==================================================
def search(root, key):  # Fungsi rekursif untuk mencari key dalam BST
    if root is None:  # Jika root None, key tidak ditemukan
        return False  # Mengembalikan False
    
    if root.data == key:  # Jika data root sama dengan key, ditemukan
        return True  # Mengembalikan True
    
    elif key < root.data:  # Jika key lebih kecil, cari di subtree kiri
        return search(root.left, key)  # Rekursif ke kiri
    
    else:  # Jika key lebih besar, cari di subtree kanan
        return search(root.right, key)  # Rekursif ke kanan

# uji pencarian
key = 40  # Key yang akan dicari

if search(root, key):  # Jika search mengembalikan True
    print("Data ditemukan:")  # Cetak bahwa data ditemukan
else:  # Jika False
    print("Data tidak ditemukan")  # Cetak bahwa data tidak ditemukan
