from grafo import Grafo
from collections import deque

def clustering(grafo, k):
    vertices = grafo.obtener_vertices()
    clusters = [set() for _ in range(k)]
    distancias = calcular_distancias(grafo)
    mejor_max_diametro = [float("inf")]
    mejor_asignacion = [None]
    backtracking(0, vertices, clusters, k, distancias, mejor_max_diametro, mejor_asignacion)
    return mejor_asignacion[0], mejor_max_diametro[0]


def backtracking(indice, vertices, clusters, k, distancias, mejor_max_diametro, mejor_asignacion):
    if indice == len(vertices):
        diametros = [diametro_cluster(cluster, distancias) for cluster in clusters if cluster]
        max_diam = max(diametros)
        if max_diam < mejor_max_diametro[0]:
            mejor_max_diametro[0] = max_diam
            mejor_asignacion[0] = [set(cluster) for cluster in clusters]
        return

    v = vertices[indice]
    for i in range(k):
        clusters[i].add(v)

        if len(clusters[i]) == 1 and any(len(clusters[j]) == 0 for j in range(i)):
            clusters[i].remove(v)
            continue

        diametros = [diametro_cluster(cluster, distancias) for cluster in clusters if cluster]
        if max(diametros) < mejor_max_diametro[0]:
            backtracking(indice + 1, vertices, clusters, k, distancias, mejor_max_diametro, mejor_asignacion)
        elif indice + 1 == len(vertices):  
            backtracking(indice + 1, vertices, clusters, k, distancias, mejor_max_diametro, mejor_asignacion)

        clusters[i].remove(v)


def calcular_distancias(grafo):
    distancias = {}
    for v in grafo.obtener_vertices():
        distancias[v] = bfs_distancias(grafo, v)
    return distancias


def bfs_distancias(grafo, origen):
    dist = {v: float("inf") for v in grafo.obtener_vertices()}
    dist[origen] = 0
    q = deque([origen])
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if dist[w] == float("inf"):
                dist[w] = dist[v] + 1
                q.append(w)
    return dist


def diametro_cluster(cluster, distancias):
    if len(cluster) <= 1:
        return 0
    max_dist = 0
    lista = list(cluster)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            d = distancias[lista[i]][lista[j]]
            if d == float("inf"):
                return float("inf")
            max_dist = max(max_dist, d)
    return max_dist



def construir_grafo(ruta):
    grafo=Grafo(False)
    with open(ruta, "r") as file:
        next(file)
        for linea in file:
            v1, v2 = linea.strip().split(",")
            if v1 not in grafo:
                grafo.agregar_vertice(v1)
            if v2 not in grafo:
                grafo.agregar_vertice(v2)
            grafo.agregar_arista(v1,v2,1)
    return grafo

if __name__ == "__main__":
    grafo = construir_grafo("pruebas_catedra/10_3.txt")
    print(grafo)
    print(calcular_distancias(grafo))
    print(clustering)