#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Studi Kasus: Sistem Antrian Layanan Akademik
# Implementasi Queue menggunakan Linked List
# Enqueue  : menambahkan data dari belakang (rear)
# Dequeue  : menghapus data dari depan (front)
#==================================================


# 1) Mendefinisikan Node (unit dasar dari linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim        # menyimpan NIM mahasiswa
        self.nama = nama      # menyimpan nama mahasiswa
        self.next = None      # pointer ke node berikutnya (awal = None)


# 2) Mendefinisikan Queue (memiliki front dan rear)
class Queueakademik:
    def __init__(self):
        self.front = None     # pointer ke depan (head)
        self.rear = None      # pointer ke belakang (tail)

    # Mengecek apakah queue kosong
    def is_empty(self):
        return self.front is None   # jika front None → queue kosong

    # Menambahkan data baru ke belakang (rear) queue
    def enqueue(self, nim, nama):
        nodebaru = Node(nim, nama)  # membuat node baru dengan data yang diberikan

        # Jika queue kosong
        if self.is_empty():
            self.front = nodebaru   # front menunjuk ke node baru
            self.rear = nodebaru    # rear menunjuk ke node baru
        else:
            # Jika queue tidak kosong
            self.rear.next = nodebaru  # rear lama menunjuk ke node baru
            self.rear = nodebaru       # rear sekarang menjadi node baru

    # Menghapus data dari depan (front) queue
    def dequeue(self):
        # Jika queue kosong
        if self.is_empty():
            print("Queue kosong, tidak ada data yang bisa dihapus.")
            return None

        # Simpan node yang akan dilayani (dihapus)
        node_dilayani = self.front

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah digeser front menjadi None
        # berarti antrian sudah kosong -> rear juga harus None
        if self.front is None:
            self.rear = None

        return node_dilayani  # kembalikan data yang dilayani

    # Menampilkan isi antrian
    def tampilkan(self):
        print("Daftar antrian mahasiswa (front -> rear):")

        # Jika queue kosong
        if self.is_empty():
            print("Antrian kosong.")
            return

        current = self.front  # mulai dari front
        no = 1

        # Telusuri hingga node terakhir
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1


#==================================================
# Program Utama
#==================================================
def main():
    q = Queueakademik()  # membuat objek queue

    while True:
        print("\nMenu Antrian Layanan Akademik:")
        print("1. Tambah Antrian (Enqueue)")
        print("2. Layani Antrian (Dequeue)")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        # Menu 1 -> Tambah Antrian
        if pilihan == "1":
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()
            q.enqueue(nim, nama)
            print(f"Antrian untuk {nama} (NIM: {nim}) telah ditambahkan.")

        # Menu 2 -> Layani Antrian
        elif pilihan == "2":
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani is not None:
                print(f"Antrian untuk {mahasiswa_dilayani.nama} (NIM: {mahasiswa_dilayani.nim}) telah dilayani.")

        # Menu 3 -> Tampilkan Antrian
        elif pilihan == "3":
            q.tampilkan()

        # Menu 4 -> Keluar
        elif pilihan == "4":
            print("Program selesai, terimakasih.")
            break

        # Jika input tidak valid
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.")


# Menjalankan program
if __name__ == "__main__":
    main()