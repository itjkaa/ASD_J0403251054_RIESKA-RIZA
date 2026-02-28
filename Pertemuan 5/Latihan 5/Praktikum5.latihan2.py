#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Latihan 2: Tracing Rekursi

def countdown(n):

    # Base Case
    if n == 0:
        print("Selesai")
        return

    # Proses sebelum rekursi
    print("Masuk:", n)

    # Recursive call
    countdown(n - 1)

    # Proses setelah rekursi
    print("Keluar:", n)


countdown(3)


# ==========================
# Penjelasan:
# "Masuk" dicetak sebelum rekursi.
# "Keluar" dicetak setelah rekursi selesai.
# Karena rekursi memakai stack (LIFO),
# maka output "Keluar" muncul terbalik.