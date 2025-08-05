from collections import deque

def bfs(grafo, ini, vertices_permitidos):
    padres = {v: float('inf') for v in vertices_permitidos}
    padres[ini] = 0
    cola = deque([ini])
    while cola:
        u = cola.popleft()
        for v in grafo.adyacentes(u):
            if v in vertices_permitidos and padres[v] == float('inf'):
                padres[v] = padres[u] + 1
                cola.append(v)
    return padres

def es_particion_valida(clusters, vertices):
    asignados = set()
    for cluster in clusters:
        for v in cluster:
            if v in asignados:
                return False
            asignados.add(v)
    return asignados == set(vertices)

def validador(grafo, clusters, C):
    vertices = grafo.obtenervertices()
    if not es_particion_valida(clusters, vertices):
        return False

    for cluster in clusters:
        for u in cluster:
            cluster_set=set(cluster)
            distancias = bfs(grafo, u, cluster_set)
            for v in cluster:
                if distancias[v] > C:
                    return False
    return True
