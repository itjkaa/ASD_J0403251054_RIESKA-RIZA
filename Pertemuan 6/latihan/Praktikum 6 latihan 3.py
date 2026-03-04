#Latihan 3 . Tracing Insertion Sort 
#Buat program dengan menggunakan algoritma insertion sort 
#Tracing dengan  data = [5, 2, 4, 6, 1, 3]

def insertion_sort_with_tracing(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        shift_count = 0
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shift_count += 1
            j -= 1
        arr[j + 1] = key
        
        print(f"Iterasi i = {i}: {arr}, Shift count: {shift_count}")
        
        if i == 1:
            print(f"Jawaban Soal 1 - Isi list setelah iterasi i = 1: {arr}")
        elif i == 3:
            print(f"Jawaban Soal 2 - Isi list setelah iterasi i = 3: {arr}")
        elif i == 4:
            print(f"Jawaban Soal 3 - Jumlah pergeseran pada iterasi i = 4: {shift_count}")

data = [5, 2, 4, 6, 1, 3]
insertion_sort_with_tracing(data)
print(f"\nHasil akhir: {data}")

#Soal:
#1. Tuliskan isi list setelah iterasi i = 1. 
#  Setelah iterasi i = 1, list akan menjadi [2, 5, 4, 6, 1, 3] karena elemen 2 disisipkan sebelum 5.
#2. Tuliskan isi list setelah iterasi i = 3. 
#  Setelah iterasi i = 3, list akan menjadi [1, 2, 4, 5, 6, 3] karena elemen 1 disisipkan sebelum 2, 4, dan 5.
#3. Berapa kali pergeseran terjadi pada iterasi i = 4? 
# Pada iterasi i = 4, terjadi 3 kali pergeseran karena elemen 1 disisipkan sebelum 2, 4, dan 5.