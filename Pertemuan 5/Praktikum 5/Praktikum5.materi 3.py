#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#materi rekursif : menjumlahkan elemen list
#==================================================
def  jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    #recursive case
    else:
        return data[index] + jumlah_list(data, index+1)
print("=======program jumlah list=======")
print(jumlah_list([2,4,5]))
