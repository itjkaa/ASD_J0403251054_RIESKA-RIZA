#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#pertemuan 4: implementasi dasar : node pada linked list
# ==================================================
#membuat class Node untuk merepresentasikan setiap node dalam linked list
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke node berikutnya (awal=None)

#  1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node-node tersebut
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

# 3) menentukan head (awal) dari linked list
head = nodeA #head menunjuk ke nodeA

# 4) Traversal: menampilkan data dari setiap node dalam linked list
current = head #mulai dari head
while current is not None: #selama current tidak kosong
    print(current.data) #tampilkan data dari node saat ini
    current = current.next #pindah ke node berikutnya

#================================================
#Implementasi dasar : linked list + insert awal
#================================================
class linkedlist:
    def __init__(self):
        self.head = None #inisialisasi head (awal) dari linked list sebagai None (kosong)
    def insert_awal(self, data):
        # 1) Membuat node baru dengan data yang diberikan
        nodeBaru = Node(data) #panggil class Node untuk membuat node baru dengan data yang diberikan
        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head #node baru menunjuk ke head saat ini
        # 3) head pindah ke node baru
        self.head = nodeBaru #head sekarang menunjuk ke node baru

    def hapus_awal(self):
        data_terhapus = self.head.data #simpan data yang akan dihapus
        #menggeser head ke node berikutnya
        self.head = self.head.next #head pindah ke node berikutnya (node setelah head
        print("node yang dihapus adalah :", data_terhapus) #tampilkan data yang dihapus

    def tampilkan(self):
        current = self.head #mulai dari head
        while current is not None: #selama current tidak kosong
            print(current.data) #tampilkan data dari node saat ini
            current = current.next #pindah ke node berikutnya

print("======List Baru======")
ll = linkedlist() #instantiasi objek ke class linkedlist
ll.insert_awal("X") #masukkan data "X" ke linked list
ll.insert_awal("Y") #masukkan data "Y" ke linked list
ll.insert_awal("Z") #masukkan data "Z" ke linked list
ll.tampilkan() #tampilkan isi linked list
ll.hapus_awal() #hapus node pertama (head)
ll.tampilkan() #tampilkan isi linked list setelah penghapusan
