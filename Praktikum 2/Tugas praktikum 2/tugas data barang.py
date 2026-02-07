# ==================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin
# Penyimpanan data menggunakan file teks (.txt)
#
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# ==================================================


# --------------------------------------------------
# Konstanta untuk nama file penyimpanan data stok
# --------------------------------------------------
NAMA_FILE = "stok_kantin.txt"


# --------------------------------------------------
# Fungsi untuk membaca data stok dari file
# Data disimpan dalam dictionary
# --------------------------------------------------
def baca_stok(barang):
    stok_dict = {}  # Dictionary untuk menyimpan data barang

    try:
        # Membuka file dalam mode baca
        with open(barang, "r") as f:
            for baris in f:
                # Memisahkan data berdasarkan koma
                bagian = baris.strip().split(",")
                kode = bagian[0]
                nama = bagian[1]
                stok = int(bagian[2])

                # Menyimpan data ke dictionary
                stok_dict[kode] = {"nama": nama, "stok": stok}

    except FileNotFoundError:
        # Jika file belum ada
        print("File stok belum ada. File akan dibuat saat data disimpan.")

    return stok_dict


# --------------------------------------------------
# Fungsi untuk menyimpan data stok ke file
# --------------------------------------------------
def simpan_stok(barang, stok_dict):
    # Membuka file dalam mode tulis (overwrite)
    with open(barang, "w") as f:
        for kode, data in stok_dict.items():
            # Menulis data dengan format: kode,nama,stok
            f.write(f"{kode},{data['nama']},{data['stok']}\n")


# --------------------------------------------------
# Fungsi untuk menampilkan seluruh data barang
# --------------------------------------------------
def tampilkan_semua(stok_dict):
    # Mengecek apakah stok kosong
    if not stok_dict:
        print("Stok barang kosong.")
        return

    # Header tampilan
    print("=" * 40)
    print(f"{'Kode Barang':<12} | {'Nama Barang':<20} | Stok")
    print("-" * 40)

    # Menampilkan setiap data barang
    for kode, data in stok_dict.items():
        print(f"{kode:<12} | {data['nama']:<20} | {data['stok']}")

    print("=" * 40)


# --------------------------------------------------
# Fungsi untuk mencari barang berdasarkan kode
# --------------------------------------------------
def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        data = stok_dict[kode]
        print("\nDetail Barang")
        print(f"Kode : {kode}")
        print(f"Nama : {data['nama']}")
        print(f"Stok : {data['stok']}")
    else:
        print("Barang tidak ditemukan.")


# --------------------------------------------------
# Fungsi untuk menambahkan barang baru ke stok
# --------------------------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    # Mengecek apakah kode sudah ada
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        # Validasi input stok
        print("Stok harus berupa angka.")
        return

    # Menambahkan data barang ke dictionary
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print("Barang berhasil ditambahkan.")


# --------------------------------------------------
# Fungsi untuk mengubah stok barang (tambah / kurangi)
# --------------------------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    # Menu pilihan update stok
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    # Proses update stok
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambah.")

    elif pilihan == "2":
        stok_baru = stok_dict[kode]["stok"] - jumlah
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] = stok_baru
            print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")


# --------------------------------------------------
# Fungsi utama program
# --------------------------------------------------
def main():
    # Membaca data awal dari file
    stok_barang = baca_stok(NAMA_FILE)

    # Perulangan menu utama
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        # Percabangan menu
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


# Menjalankan program utama
if __name__ == "__main__":
    main()