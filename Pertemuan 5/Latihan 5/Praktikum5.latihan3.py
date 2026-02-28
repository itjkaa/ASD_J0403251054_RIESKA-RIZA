#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 3: Mencari Nilai Maksimum dengan Rekursi

def cari_maks(data, index=0):

    # Base Case:
    # Jika sudah di elemen terakhir
    if index == len(data) - 1:
        return data[index]

    # Recursive Case:
    # Cari maksimum dari sisa list
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# ==========================
# Penjelasan:
# Fungsi membandingkan elemen sekarang
# dengan maksimum dari sisa list.
# Proses berjalan sampai elemen terakhir,
# lalu kembali sambil membandingkan.