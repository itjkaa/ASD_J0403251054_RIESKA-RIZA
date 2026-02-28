#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 4: Kombinasi Huruf (Backtracking Dasar)

def kombinasi(n, hasil=""):

    # Base Case:
    # Jika panjang hasil sudah n
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")


kombinasi(2)


# ==========================
# Penjelasan:
# Setiap posisi memiliki 2 pilihan (A atau B).
# Total kombinasi = 2^n.
# Untuk n = 2 → 2^2 = 4 kombinasi.