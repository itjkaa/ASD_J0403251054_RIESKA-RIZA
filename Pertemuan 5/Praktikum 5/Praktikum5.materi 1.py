#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#materi rekursif : faktorial
#recursive case => contoh: 5! = 5 x 4 x 3 x 2 x 1
#base case => 0 berhenti
#==================================================
def faktorial(n):
    #base case
    if n == 0:
        return 1
    #recursive case
    else:
        return n * faktorial(n-1)
print("=======program faktorial=======")
angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
hasil = faktorial(angka)
print(f"Faktorial dari {angka} adalah {hasil}")