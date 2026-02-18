#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#pertemuan 4: implementasi dasar : queue pada linked list
# ==================================================
#queue berbasis linked list
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke node berikutnya (awal=None)

#Queue dengan 2 pointer: head (depan) dan tail (belakang)
class Queuell:
    def __init__(self):
        self.front = None #pointer ke depan (head)
        self.rear = None #pointer ke belakang (tail)

    def is_empty(self): 
        return self.front is None #cek apakah queue kosong (front=None)

    def enqueue(self, data):
        #Menambah data di belakang (rear) queue
        nodeBaru = Node(data) #membuat node baru dengan data yang diberikan
        
        #jika queue kosong, front dan rear menunjuk ke node baru
        if self.is_empty(): #jika queue kosong, front dan rear menunjuk ke node baru
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queue tidak kosong, rear lama menunjuk ke node baru
        self.rear.next = nodeBaru #rear saat ini menunjuk ke node baru
        #rear pindah ke node baru
        self.rear = nodeBaru #rear sekarang menunjuk ke node baru

    def dequeue(self):
        #Menghapus data dari depan (front) queue
        # 1) lihat data yang paling depan
        data_terhapus = self.front.data #simpan data yang akan dihapus
        # 2) Geser front ke node berikutnya
        self.front = self.front.next #front pindah ke node berikutnya (node setelah front)
        # 3) Jika setelah geser front menjadi none, maka queue menjadi kosong
        #maka rear juga harus di-set ke None
        if self.front is None: 
            self.rear = None
    def tampilkan(self):
        
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        #print("None <- Rear di node terakhir")
        print("Rear")

#Instantiasi objek ke class Queuell
q = Queuell()

q.enqueue("A") #menambahkan data "A" ke queue
q.enqueue("B") #menambahkan data "B" ke queue
q.enqueue("C") #menambahkan data "C" ke queue
q.tampilkan() #menampilkan isi queue
q.dequeue() #menghapus data paling depan (front) dari queue
q.tampilkan() #menampilkan isi queue setelah dequeue