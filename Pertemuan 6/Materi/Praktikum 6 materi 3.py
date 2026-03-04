#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
#merge sort (ascending)
#==================================================
def merge_sort(data):
    
    if len(data) <= 1: #base case: jika data hanya 1 atau kosong, sudah terurut
        return data 
    
    #Divide : membagi data menjadi dua bagian
    mid = len(data) // 2 #membagi data menjadi dua bagian
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan
    
    #recursive call
    left_sorted = merge_sort(left) #rekursif untuk bagian kiri
    right_sorted = merge_sort(right) #rekursif untuk bagian kanan
    
    return merge(left_sorted, right_sorted) #menggabungkan hasil sort kiri dan kanan

def merge(left, right):
    result = [] #list untuk menyimpan hasil penggabungan
    i = 0
    j = 0 #index untuk iterasi kiri dan kanan
    
#membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: #jika elemen kiri lebih kecil atau sama
            result.append(left[i]) #tambahkan ke hasil
            i += 1 #geser index kiri
            
        else: #jika elemen kanan lebih kecil atau sama
            result.append(right[j]) #tambahkan ke hasil
            j += 1 #geser index kanan
            
    #menambahkan sisa elemen kiri atau kanan jika ada
    result.extend(left[i:]) #tambahkan sisa elemen kiri
    result.extend(right[j:]) #tambahkan sisa elemen kanan
    return result
# Contoh penggunaan
angka = [13,7,28,5,19,36,4]
print("Hasil sort:", merge_sort(angka))  # Output: [4, 5, 7, 13, 19, 28, 36]