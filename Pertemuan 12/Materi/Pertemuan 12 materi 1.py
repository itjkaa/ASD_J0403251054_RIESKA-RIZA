#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Implementasi Algoritma Dijkstra
#==================================================

import heapq

# representasi graph (berbobot)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Fungsi untuk mencari jarak terpendek dari node awal
    # graph: dictionary berbobot
    # start: node awal

    # menyimpan jarak minimum ke setiap node
    distances = {node: float('inf') for node in graph}
    
    # jarak ke node awal = 0
    distances[start] = 0

    # priority queue untuk memilih jarak terkecil
    pq = [(0, start)]

    while pq:
        # ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # cek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # hitung jarak baru
            distance = current_distance + weight

            # jika jarak lebih kecil dari sebelumnya
            if distance < distances[neighbor]:
                # update jarak
                distances[neighbor] = distance
                # masukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# menjalankan algoritma dari node 'A'
hasil = dijkstra(graph, 'A')

# menampilkan hasil
print("Jarak terpendek dari node A:")
print(hasil)


#==================================================
# Analisis Singkat
#==================================================
# Dijkstra digunakan untuk mencari jarak terpendek
# dari satu node ke semua node lain pada graph berbobot.

# Pada graph ini:
# A -> B = 4
# A -> C = 2
# A -> D = 3 (melalui C, karena 2 + 1 lebih kecil dari 4 + 5)