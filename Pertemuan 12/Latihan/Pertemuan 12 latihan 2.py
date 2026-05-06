#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# Praktikum 12 - Graph II: Shortest Path
#==================================================
# Latihan 2: Implementasi Dijkstra
#==================================================

# Implementasi Dijkstra untuk mencari jarak terpendek dari node A ke semua node lainnya
import heapq  # heapq digunakan untuk membuat priority queue berbasis min-heap

# representasi graph (berbobot)
# graph disimpan sebagai dictionary, di mana setiap node memiliki dictionary tetangganya
# dan nilai bobot edge menuju tetangga tersebut
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# fungsi Dijkstra
def dijkstra(graph, start):
    # inisialisasi jarak seluruh node dengan nilai tak hingga
    # artinya pada awalnya jarak ke semua node dianggap sangat besar
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # jarak dari node awal ke dirinya sendiri adalah 0

    # priority queue berisi pasangan (jarak, node)
    # ini menjamin node dengan jarak terkecil diproses lebih dulu
    pq = [(0, start)]

    # proses utama Dijkstra, selama masih ada node di queue
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # jika jarak yang diambil dari queue sudah lebih besar dari jarak terbaik saat ini,
        # maka kita lewati karena sudah ada jalur yang lebih pendek
        if current_distance > distances[current_node]:
            continue

        # cek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # hitung jarak baru melalui current_node ke neighbor
            distance = current_distance + weight

            # jika jarak baru lebih pendek, perbarui jarak dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

# menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

#==================================================
# Jawaban Analisis
#==================================================
# 1. A ke B = 4
# 2. A ke C = 2
# 3. A ke D = 3
# 4. Karena lewat C lebih kecil (2 + 1 = 3 < 4 + 5)
# 5. priority_queue untuk ambil jarak terkecil dulu
# 6. Karena tidak bisa handle bobot negatif