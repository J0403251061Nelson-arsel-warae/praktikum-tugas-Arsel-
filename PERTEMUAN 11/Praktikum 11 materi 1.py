#=========================================================
#Nama : Nelson Arsel Warae 
#Implementasi Dasar graph
#=======================================================


graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, "->", graph[node])
