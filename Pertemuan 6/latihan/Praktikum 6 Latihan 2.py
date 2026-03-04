#Latihan 2 . Melengkapi Potongan Kode 
#Ascending sort (sudah lengkap) (soal 1    )
def insertion_sort_ascending(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
        
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
        
        data[j + 1] = key
    
    return data 

#Descending sort (soal 2)
def insertion_sort_descending(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
        
        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j] 
            j -= 1 
        
        data[j + 1] = key
    
    return data
#Soal: 
#1. Lengkapi kondisi agar menjadi sorting ascending. 
#2. Ubah agar menjadi descending.