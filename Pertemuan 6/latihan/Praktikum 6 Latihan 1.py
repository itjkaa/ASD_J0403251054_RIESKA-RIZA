#Latihan 1 . Memahami Kode Program (Insertion Sort) 
def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 

        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
        
        data[j + 1] = key 
    
    return data 
#Soal: 
#1. Mengapa perulangan dimulai dari indeks 1? 
#   Karena elemen pertama (indeks 0) dianggap sudah terurut, jadi tidak perlu diproses.
#2. Apa fungsi variabel key? 
#   Variabel key menyimpan nilai dari elemen saat ini yang akan disisipkan ke dalam bagian terurut.
#3. Mengapa digunakan while, bukan for? 
#   Karena kita perlu terus memindahkan elemen-elemen yang lebih besar ke kanan sampai menemukan posisi yang tepat untuk key.
#4. Operasi apa yang terjadi di dalam while?
#   Di dalam while, elemen-elemen yang lebih besar dari key dipindahkan satu posisi ke kanan.