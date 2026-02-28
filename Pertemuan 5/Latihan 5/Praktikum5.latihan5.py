#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Studi Kasus: Generator PIN (Backtracking)

def buat_pin(panjang, hasil=""):

    # Base Case:
    # Jika panjang PIN sudah sesuai
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Explore semua kemungkinan angka
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(3)


# ==========================
# Penjelasan:
# Setiap digit memiliki 3 pilihan (0,1,2).
# Total kemungkinan = 3^3 = 27 PIN.
#
# Jika ingin mencegah angka yang sama berulang:
#
# for angka in ["0", "1", "2"]:
#     if angka not in hasil:
#         buat_pin(panjang, hasil + angka)
#
# Maka total menjadi 3! = 6 kombinasi unik.