#==================================================
# Nama  : Rieska Riza
# NIM   : J0403251054
# Kelas : B2 TPL
#==================================================
# Implementasi graph
# =================================================
graph = {   
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
for node in graph:
    print("node", node, "terhubung dengan", graph[node])