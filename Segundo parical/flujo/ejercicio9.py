from ejercicio2 import ford_fulkerson
"""Dado un grafo no dirigido, un match es un subconjunto de las aristas en el cual para todo vértice v a lo sumo una arista del match 
incide en v (en el match, tienen grado a lo sumo 1). Decimos que el vértice v está matcheado si hay alguna arista que incida en él 
(sino, está unmatcheado). El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad 
posible). Dar una metodología para encontrar el matching máximo de un grafo, explicando en detalle cómo se modela el problema, cómo se 
lo resuelve y cómo se consigue el matching máximo. ¿Cuál es el orden temporal de la solución implementada?"""
#O(V*E) ya que es O(V*Iteraciones) como muhcoo V/2 iteraciones
def es_bipartito(grafo):
    color = {}
    for nodo in grafo:
        if nodo not in color:
            cola = [nodo]
            color[nodo] = 0
            while cola:
                actual = cola.pop(0)
                for vecino in grafo[actual]:
                    if vecino not in color:
                        color[vecino] = 1 - color[actual]
                        cola.append(vecino)
                    elif color[vecino] == color[actual]:
                        return False, None
    return True, color

def construir_red_de_flujo(grafo, color):
    red = {}  # diccionario de adyacencias con capacidades
    fuente = "fuente"
    sumidero = "sumidero"

    # inicializar nodos
    red[fuente] = []
    red[sumidero] = []

    for nodo in grafo:
        red.setdefault(nodo, [])
        if color[nodo] == 0:
            # Arista fuente → nodo (U)
            red[fuente].append((nodo, 1))
        else:
            # Arista nodo (V) → sumidero
            red[nodo].append((sumidero, 1))

    for u in grafo:
        for v in grafo[u]:
            if color[u] == 0 and color[v] == 1:
                red[u].append((v, 1))  # solo de U a V

    return red, fuente, sumidero

def matching_maximo(grafo):
    es_bip, color = es_bipartito(grafo)
    if not es_bip:
        raise ValueError("El grafo no es bipartito")

    red, fuente, sumidero = construir_red_de_flujo(grafo, color)

    # Llamada a Ford-Fulkerson (implementación asumida)
    return ford_fulkerson(red, fuente, sumidero)