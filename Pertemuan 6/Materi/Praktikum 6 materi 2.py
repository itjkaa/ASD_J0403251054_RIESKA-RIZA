#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Insertion sort dengan tracing
#==================================================
def insertion_sort(data):
    #melihat data awal
    print("Data awal:", data)
    print("="*50)
    
    #loop mulai dari elemen kedua (index 1) hingga akhir
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
        
        print("Iterasi ke-", i)
        print("Nilai key =", key)
        print("Bagian kiri yang sudah terurut:", data[:i])
        print("Bagian kanan yang belum terurut:", data[i:])
        
        #geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key pada posisi yang benar
        data[j + 1] = key
        
        print("Data setelah disisipkan =", data)
        print("-"*50)
        
    return data
# Contoh penggunaan
data = [12, 11, 13, 5, 6] 
print("hasil sort:", insertion_sort(data))  # Output: [5, 6, 11, 12, 13]    