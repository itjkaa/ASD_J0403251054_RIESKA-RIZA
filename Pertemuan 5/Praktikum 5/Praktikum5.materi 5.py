#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#materi 5: Backtracking kombinasi biner dengan batas jumlah '1'
#==================================================
def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi untuk menghasilkan kombinasi biner sepanjang n
    # dengan jumlah angka '1' tidak boleh melebihi batas
    #
    # n        : panjang digit biner
    # batas    : maksimum jumlah angka '1' yang diperbolehkan
    # hasil    : string sementara yang sedang dibentuk
    # jumlah_1 : menghitung berapa banyak '1' dalam hasil

    # Pruning (pemangkasan)
    # Jika jumlah '1' sudah melebihi batas,
    # tidak perlu lanjut rekursi (langsung berhenti)
    if jumlah_1 > batas:
        return

    # Base case (kondisi berhenti)
    # Jika panjang hasil sudah sama dengan n,
    # cetak hasil karena sudah valid
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case (choose + explore)

    # Pilih '0'
    # jumlah_1 tidak bertambah karena tidak menambah '1'
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1'
    # jumlah_1 bertambah 1 karena menambahkan '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


# Pemanggilan fungsi
# Panjang biner = 4
# Maksimal jumlah '1' = 2
biner_batas(4, 2)