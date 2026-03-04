#Latihan 5 . Melengkapi Fungsi Merge 
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
    result.extend(left[i:]) 
    result.extend(right[j:]) 
    return result 
#Soal:
#1. Lengkapi kondisi agar menjadi ascending. 
#   Kondisi jika sudah lengkap : left[i] < right[j] menghasilkan urutan ascending.
#2. Jelaskan fungsi result.extend(). 
#   Fungsi result.extend() digunakan untuk menambahkan semua elemen dari list yang diberikan ke akhir list result. Dalam konteks merge sort, ini digunakan untuk menambahkan sisa elemen dari left atau right ke result setelah salah satu dari keduanya habis.