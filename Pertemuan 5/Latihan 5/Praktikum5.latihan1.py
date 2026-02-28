#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 1: Rekursi Pangkat
# Tujuan: Memahami base case dan recursive case

def pangkat(a, n):
    # Base Case:
    # Jika pangkat = 0, hasilnya 1 (aturan matematika)
    if n == 0:
        return 1

    # Recursive Case:
    # a^n = a * a^(n-1)
    return a * pangkat(a, n - 1)


# Contoh pemanggilan
print("Hasil:", pangkat(2, 4))  # Output: 16


# ==========================
# Penjelasan:
# Base case menghentikan rekursi saat n == 0.
# Recursive call terus memanggil fungsi dengan n-1
# sampai mencapai 0.
# Proses kembali (return) terjadi dari bawah ke atas.