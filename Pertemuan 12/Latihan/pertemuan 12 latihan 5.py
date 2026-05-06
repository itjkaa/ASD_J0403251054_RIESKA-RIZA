#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# Praktikum 12 - Graph II: Shortest Path
#==================================================
# Latihan 5: Studi Kasus Kota
#==================================================

# Implementasi Dijkstra untuk mencari jarak terpendek dari Bogor ke semua kota lainnya
# heapq digunakan untuk membuat priority queue di Python.
import heapq

# representasi graph (berbobot)
# Setiap kota disimpan sebagai node, dan setiap tetangga disimpan dengan bobot jarak.
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# fungsi Dijkstra untuk menghitung jarak terpendek dari titik awal ke semua node lain
def dijkstra(graph, start):
    # inisialisasi jarak semua node dengan tak hingga
    distances = {node: float('inf') for node in graph}
    # jarak dari start ke dirinya sendiri adalah 0
    distances[start] = 0

    # priority queue dengan elemen (jarak, node)
    # node dengan jarak terkecil diproses terlebih dahulu
    pq = [(0, start)]

    # proses utama Dijkstra
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # jika jarak yang diambil lebih besar dari jarak terbaik yang sudah diketahui, lewati
        if current_distance > distances[current_node]:
            continue

        # periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # jika jarak baru lebih kecil, perbarui jarak dan masukkan ke antrean
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# jalankan algoritma Dijkstra dari Bogor
hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)


#==================================================
# Jawaban Analisis
#==================================================
# 1. Node awal: Bogor
# 2. Paling kecil: Depok (2)
# 3. Paling besar: Bandung (8)
# 4. Dijkstra memilih jarak terkecil dulu,
# lalu update ke tetangga sampai semua optimal