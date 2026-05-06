#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
# Praktikum 12 - Graph II: Shortest Path
#==================================================
# Latihan 3: Implementasi Bellman-Ford
#==================================================

# Representasi graf berbobot sebagai dictionary Python.
# Setiap node memiliki dictionary tetangga dengan bobot edge.
# Contoh: graph['A']['B'] = 5 berarti ada edge A -> B dengan bobot 5.
graph = {
    'A': {'B': 5, 'C': 4},  # A terhubung ke B dengan bobot 5 dan ke C dengan bobot 4
    'B': {},                # B tidak memiliki edge keluar
    'C': {'B': -2}          # C terhubung ke B dengan bobot -2
}

def bellman_ford(graph, start):
    # Inisialisasi jarak ke semua node sebagai tak hingga.
    # Ini berarti kita belum mengetahui jarak terpendek ke node tersebut.
    distances = {node: float('inf') for node in graph}
    # Jarak ke node awal adalah 0 karena berada di titik awal.
    distances[start] = 0

    # Jalankan relaksasi sebanyak |V|-1 kali.
    # |V| adalah jumlah node dalam graf.
    # Jika graf tidak memiliki siklus negatif, proses ini cukup
    # untuk menemukan jarak terpendek ke semua node.
    for _ in range(len(graph) - 1):
        # Periksa setiap node di graf.
        for node in graph:
            # Periksa semua tetangga dari node saat ini.
            # Tetangga merupakan node yang dapat dicapai langsung dari node.
            for neighbor, weight in graph[node].items():
                # Hanya lakukan relaksasi jika node asal sudah terjangkau.
                if distances[node] != float('inf'):
                    # Hitung jarak melalui node saat ini ke tetangga.
                    new_distance = distances[node] + weight
                    # Jika jalur baru lebih pendek, perbarui jarak tetangga.
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


#==================================================
# Jawaban Analisis
#==================================================
# 1. A -> B = 5
# 2. A -> C -> B = 4 + (-2) = 2
# 3. Jalur terbaik lewat C
# 4. Karena bisa menangani bobot negatif
# 5. Relaksasi = update jarak jika lebih kecil
# 6. Dijkstra cepat tapi tidak bisa negatif,
#    Bellman-Ford lebih lambat tapi bisa negatif