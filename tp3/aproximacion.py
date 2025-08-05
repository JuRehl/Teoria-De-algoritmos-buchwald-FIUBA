from collections import deque
import sys
import auxiliares

def bfs_distancias(grafo, inicio):
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    cola = deque([inicio])
    while cola:
        u = cola.popleft()
        for w in grafo.adyacentes(u):
            if distancias[w] == float('inf'):
                distancias[w] = distancias[u] + 1
                cola.append(w)
    return distancias

def todas_distancias(grafo):
    return {v: bfs_distancias(grafo, v) for v in grafo}

def se_pueden_formar_clusters(distancias, k, C):
    sin_asignar = set(distancias.keys())
    clusters = []
    while sin_asignar:
        v = sin_asignar.pop()
        cluster = {v}
        agregado = True
        while agregado:
            agregado = False
            por_agregar = set()
            for u in sin_asignar:
                if all(distancias[u][w] <= C and distancias[w][u] <= C for w in cluster):
                    por_agregar.add(u)
            if por_agregar:
                cluster.update(por_agregar)
                sin_asignar.difference_update(por_agregar)
                agregado = True
        clusters.append(cluster)
        if len(clusters) > k:
            return False
    return True

def encontrar_min_C(grafo, k):
    distancias = todas_distancias(grafo)
    max_dist = max(max(d.values()) for d in distancias.values() if d.values())
    bajo, alto = 0, max_dist
    resultado = alto
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if se_pueden_formar_clusters(distancias, k, medio):
            resultado = medio
            alto = medio - 1
        else:
            bajo = medio + 1
    return resultado

def formar_clusters(distancias, k, C):
    sin_asignar = set(distancias.keys())
    clusters = []
    while sin_asignar:
        v = sin_asignar.pop()
        cluster = {v}
        agregado = True
        while agregado:
            agregado = False
            por_agregar = set()
            for u in sin_asignar:
                if all(distancias[u][w] <= C and distancias[w][u] <= C for w in cluster):
                    por_agregar.add(u)
            if por_agregar:
                cluster.update(por_agregar)
                sin_asignar.difference_update(por_agregar)
                agregado = True
        clusters.append(cluster)
        if len(clusters) > k:
            return None 
    return clusters

def aproximacion(grafo,k):
    C_opt = encontrar_min_C(grafo, k)
    print(f"Valor mínimo de C para {k} clusters: {C_opt}")

    distancias = todas_distancias(grafo)
    clusters = formar_clusters(distancias, k, C_opt)

    return clusters, None
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 script.py <archivo_grafo> <k>")
        sys.exit(1)

    archivo = sys.argv[1]
    k = int(sys.argv[2])

    grafo = auxiliares.construir_grafo(archivo)

    # Encontrar el mínimo C
    C_opt = encontrar_min_C(grafo, k)
    print(f"Valor mínimo de C para {k} clusters: {C_opt}")

    # Formar clusters con C_opt
    distancias = todas_distancias(grafo)
    clusters = formar_clusters(distancias, k, C_opt)

    if clusters is None:
        print("No fue posible formar clusters con el valor mínimo encontrado (esto no debería ocurrir).")
    else:
        print("Asignación:")
        for i, cluster in enumerate(clusters):
            nodos = sorted(cluster, key=int)
            print(f"Cluster {i} : {nodos}")

        print(f"Maxima distancia dentro del cluster: {C_opt}")