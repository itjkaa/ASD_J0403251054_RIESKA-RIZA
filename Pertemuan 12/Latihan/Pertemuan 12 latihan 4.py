#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# Praktikum 12 - Graph II: Shortest Path
#==================================================
# Latihan 4: Studi Kasus Kampus
#==================================================

import heapq

# Representasi graf sebagai dictionary bersarang.
# Setiap node pada graf disimpan sebagai kunci di dictionary utama.
# Nilai untuk setiap node adalah dictionary lain yang memetakan tetangga
# dan bobot perjalanan menuju tetangga tersebut.
# Contoh: 'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}
# berarti dari Gerbang ke Perpustakaan memerlukan 6 menit,
# dan dari Gerbang ke Kantin memerlukan 2 menit.
# Bobot di sini merepresentasikan waktu tempuh dalam menit.
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

# Fungsi Dijkstra untuk mencari jarak terpendek dari node awal ke semua node lain.
# Parameter graph adalah representasi graf, start adalah node awal.
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


#==================================================
# Jawaban Analisis
#==================================================
# 1. Paling dekat: Kantin (2 menit)
# 2. Ke Aula = 7 menit (Gerbang -> Kantin -> Lab -> Aula = 2+4+1)
# 3. Tidak selalu, harus lihat total bobot
# 4. Karena semua bobot positif dan butuh shortest path