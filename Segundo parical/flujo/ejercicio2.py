"""(★★) Implementar el algoritmo de Ford-Fulkerson, asumiendo que ya está implementada una función actualizar_grafo_residual, 
definida como actualizar_grafo_residual(grafo_residual, u, v, valor), que recibe el grafo residual, una arista dirigida dada 
por los vértices u y v, y el nuevo valor del flujo a través de la arista (u,v) y actualiza el grafo residual ya teniendo en 
cuenta el peso anterior de la arista, y su antiparalela. Devolver un diccionario con los valores de los flujos para todas las 
aristas del grafo original."""
def ford_fulkerson(grafo, s,t):#O(V*E²)
    flujo={}
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo[(v,w)]=0
    grafo_residual=0 #aca iría tipo copiar_grafo()
    camino=0#lo agrego para que no joda el visual
    while flujo: #aca iria  while camino=grafo.obtener_camino(s,t) is not None:
        capacidad_residual_camino= min(grafo_residual,camino)
        for i in range(1,len(camino)):
            if grafo.hay_arista(camino[i-1],camino[i]):
                flujo[(camino[i-1],camino[i])]+= capacidad_residual_camino
            else:
                flujo[(camino[i],camino[i-1])]-=capacidad_residual_camino
            actualizar_grafo_residual(grafo_residual,camino[i-1],camino[i],capacidad_residual_camino)
    return flujo

from collections import deque

def bfs_camino_residual(grafo_residual, s, t, padres):
    visitado = set()
    queue = deque([s])
    visitado.add(s)

    while queue:
        u = queue.popleft()
        for v in grafo_residual.get(u, {}):
            capacidad = grafo_residual[u][v]
            if v not in visitado and capacidad > 0:
                padres[v] = u
                if v == t:
                    return True
                visitado.add(v)
                queue.append(v)
    return False

def ford_fulkerson(grafo, s, t):
    grafo_residual = {u: dict(vs) for u, vs in grafo.items()}  # Copia profunda
    flujo = { (u, v): 0 for u in grafo for v in grafo[u] }

    def actualizar_grafo_residual(g, u, v, delta):
        g[u][v] -= delta
        if g[u][v] == 0:
            del g[u][v]
        g.setdefault(v, {})
        g[v][u] = g[v].get(u, 0) + delta

    padres = {}
    while bfs_camino_residual(grafo_residual, s, t, padres := {}):
        # Determinar el cuello de botella
        camino = []
        v = t
        flujo_camino = float('inf')
        while v != s:
            u = padres[v]
            flujo_camino = min(flujo_camino, grafo_residual[u][v])
            camino.append((u, v))
            v = u

        # Actualizar el grafo residual y el flujo
        for u, v in camino:
            actualizar_grafo_residual(grafo_residual, u, v, flujo_camino)
            if (u, v) in flujo:
                flujo[(u, v)] += flujo_camino
            else:
                flujo[(v, u)] -= flujo_camino

    return flujo
