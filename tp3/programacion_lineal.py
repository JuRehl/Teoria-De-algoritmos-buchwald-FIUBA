import pulp
from itertools import combinations
from collections import deque
import sys
import auxiliares

def clustering_pulp(grafo, k):
    nodos = list(grafo.obtener_vertices())
    distancias = calcular_distancias(grafo)
    pares = list(combinations(nodos, 2))

    model = pulp.LpProblem("Clustering_bajo_diametro", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("x", ((v, c) for v in nodos for c in range(k)), cat='Binary')
    z = pulp.LpVariable.dicts("z", ((u, v, c) for u, v in pares for c in range(k)), cat='Binary')
    d = pulp.LpVariable.dicts("d", range(k), lowBound=0, cat='Continuous')
    D_max = pulp.LpVariable("D_max", lowBound=0, cat='Continuous')

    for v in nodos:
        model += pulp.lpSum(x[v, c] for c in range(k)) == 1

    for u, v in pares:
        for c in range(k):
            model += z[u, v, c] <= x[u, c]
            model += z[u, v, c] <= x[v, c]
            model += z[u, v, c] >= x[u, c] + x[v, c] - 1

    for u, v in pares:
        for c in range(k):
            dist = distancias.get((u, v), float('inf'))
            model += d[c] >= dist * z[u, v, c]

    for c in range(k):
        model += D_max >= d[c]

    model += D_max

    solver = pulp.PULP_CBC_CMD(msg=False)
    model.solve(solver)

    if pulp.LpStatus[model.status] != 'Optimal':
        return [[] for _ in range(k)], float('inf')

    clusters = [[] for _ in range(k)]
    for v in nodos:
        for c in range(k):
            if pulp.value(x[v, c]) > 0.5:
                clusters[c].append(v)

    diametro = pulp.value(D_max)
    return clusters, diametro


def calcular_distancias(grafo):
    nodos = grafo.obtener_vertices()
    distancias = {}
    for inicio in nodos:
        distancias[(inicio, inicio)] = 0
        queue = deque([inicio])
        visitados = set([inicio])
        while queue:
            actual = queue.popleft()
            for vecino in grafo.adyacentes(actual):
                if vecino not in visitados:
                    distancias[(inicio, vecino)] = distancias[(inicio, actual)] + 1
                    distancias[(vecino, inicio)] = distancias[(inicio, vecino)]
                    visitados.add(vecino)
                    queue.append(vecino)
    return distancias

def main():
    grafo=auxiliares.construir_grafo(sys.argv[1])
    k=int(sys.argv[2])
    clusters, diametro = clustering_pulp(grafo, k)
    print(f"Clusters encontrados (k={k}):")
    for i, c in enumerate(clusters):
        print(f"Cluster {i+1}: {c}")
    print(f"Diámetro máximo: {diametro}")

if __name__ == "__main__":
    main()