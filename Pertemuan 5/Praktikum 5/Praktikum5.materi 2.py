#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#materi rekursif : call stack
#tracing bilangan (masuk-keluar)
#==================================================
def hitung(n):
    #base case
    if n==0:
        print("selesai")
        return
    print("masuk:", n) #menampilkan nilai n saat masuk ke fungsi    
    hitung(n-1) #pemanggilan rekursif dengan n-1(recursive case)
    print("keluar:", n) #menampilkan nilai n saat keluar dari fungsi
    
print("program tracing bilangan")
hitung(6)