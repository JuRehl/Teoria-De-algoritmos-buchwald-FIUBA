from collections import deque
""" Dada una red residual, dar un algoritmo que encuentre un camino de aumento que minimice el número de aristas utilizadas."""
#Queremos encontrar un camino de aumento (de la fuente al sumidero) tal que use la menor cantidad de aristas posible, es decir, 
# el camino más corto en cantidad de pasos (no en peso/capacidad).

def camino_de_aumento(residual,s,t): #BFS complejidad O(V+E)
    padres={s: None}
    cola= deque([s])
    while cola:
        u=cola.popleft()
        for v in residual.adyacentes(u):
            if v not in padres and residual.peso_arista(u,v)>0:
                padres[v]=u
                cola.append(v)
                if v==t:
                    break
    if t not in padres:
        return None
    camino=[]
    actual=t
    while actual is not None:
        camino.append(actual)
        actual=padres[actual]
    return list(reversed(camino))
