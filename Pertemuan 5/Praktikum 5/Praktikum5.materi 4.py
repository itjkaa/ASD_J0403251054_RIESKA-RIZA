#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#materi 4: Backtracking kombinasi biner (n)
#==================================================
def biner(n, hasil=""):
    # Fungsi untuk menghasilkan semua kombinasi bilangan biner
    # n     : panjang digit biner yang diinginkan
    # hasil : string sementara untuk menyimpan kombinasi yang sedang dibentuk

    # Base case (kondisi berhenti)
    # Jika panjang string sudah sama dengan n,
    # berarti kombinasi sudah lengkap → cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Recursive case (proses rekursif)
    # Choose + Explore:
    # Tambahkan '0' ke hasil, lalu panggil fungsi lagi
    biner(n, hasil + "0")

    # Choose + Explore:
    # Tambahkan '1' ke hasil, lalu panggil fungsi lagi
    biner(n, hasil + "1")
# Pemanggilan fungsi
# Akan menghasilkan semua kombinasi biner dengan panjang 3
biner(3)