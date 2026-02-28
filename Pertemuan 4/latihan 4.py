#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Studi Kasus: Sistem Antrian Bengkel
# Konsep: Queue (FIFO - First In First Out)
# Kendaraan datang duluan -> dilayani duluan
#==================================================


# Node = 1 kendaraan dalam antrian
class Node:
    def __init__(self, no_polisi, nama_pemilik):
        self.no_polisi = no_polisi        # nomor polisi kendaraan
        self.nama_pemilik = nama_pemilik  # nama pemilik kendaraan
        self.next = None                  # pointer -> kendaraan berikutnya


# Queue untuk antrian bengkel
class AntrianBengkel:
    def __init__(self):
        self.front = None   # kendaraan paling depan -> dilayani dulu
        self.rear = None    # kendaraan paling belakang -> baru datang

    # cek apakah antrian kosong
    def is_empty(self):
        return self.front is None

    # kendaraan datang -> masuk ke belakang
    def tambah_antrian(self, no_polisi, nama_pemilik):
        kendaraan_baru = Node(no_polisi, nama_pemilik)

        if self.is_empty():
            self.front = kendaraan_baru
            self.rear = kendaraan_baru
        else:
            self.rear.next = kendaraan_baru  # rear lama -> kendaraan baru
            self.rear = kendaraan_baru

    # kendaraan dipanggil -> keluar dari depan
    def layani_kendaraan(self):
        if self.is_empty():
            print("Antrian bengkel masih kosong.")
            return None

        kendaraan_dilayani = self.front
        self.front = self.front.next  # front -> kendaraan berikutnya

        if self.front is None:
            self.rear = None

        return kendaraan_dilayani

    # tampilkan isi antrian
    def tampilkan_antrian(self):
        print("\nDaftar kendaraan dalam antrian (front -> rear):")

        if self.is_empty():
            print("Belum ada kendaraan yang menunggu.")
            return

        current = self.front
        no = 1

        while current is not None:
            print(f"{no}. {current.no_polisi} - {current.nama_pemilik}")
            current = current.next
            no += 1


#==============================
# Program utama
#==============================
def main():
    bengkel = AntrianBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah kendaraan -> masuk antrian")
        print("2. Layani kendaraan -> keluar antrian")
        print("3. Lihat daftar antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            no_polisi = input("Masukkan nomor polisi kendaraan: ").strip()
            nama_pemilik = input("Masukkan nama pemilik: ").strip()
            bengkel.tambah_antrian(no_polisi, nama_pemilik)
            print(f"Kendaraan {no_polisi} atas nama {nama_pemilik} masuk ke antrian.")

        elif pilihan == "2":
            kendaraan = bengkel.layani_kendaraan()
            if kendaraan is not None:
                print(f"Kendaraan {kendaraan.no_polisi} atas nama {kendaraan.nama_pemilik} sedang dilayani.")

        elif pilihan == "3":
            bengkel.tampilkan_antrian()

        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Menu tidak tersedia, coba lagi.")


if __name__ == "__main__":
    main()