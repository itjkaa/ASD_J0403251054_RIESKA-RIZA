#Latihan 4 . Memahami Kode Program (Merge Sort)
from heapq import merge
def merge_sort(data): 
    if len(data) <= 1: 
        return data 
    
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
    
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
    
    return merge(left_sorted, right_sorted)

#Soal: 
#1. Apa yang dimaksud dengan base case? 
#   Base case adalah kondisi di mana fungsi berhenti memanggil dirinya sendiri. Dalam merge sort, base case adalah ketika panjang array kurang dari atau sama dengan 1, karena array dengan satu elemen atau kosong sudah terurut.
#2. Mengapa fungsi memanggil dirinya sendiri? 
#   Fungsi memanggil dirinya sendiri untuk membagi array menjadi bagian-bagian yang lebih kecil sampai mencapai base case, lalu menggabungkan kembali bagian-bagian tersebut secara terurut.
#3. Apa tujuan fungsi merge()?
#   Fungsi merge() bertujuan untuk menggabungkan dua array yang sudah terurut menjadi satu array terurut.