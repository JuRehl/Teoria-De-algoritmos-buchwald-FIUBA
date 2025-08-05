def camino_hamiltoniano(grafo):
    resultado=[]
    visitados=set()
    for vertice in grafo.obtener_vertices():
        if camino_hamiltoniano_dfs(grafo,vertice,visitados,resultado):
            return resultado
    return None

def camino_hamiltoniano_dfs(grafo,vertice, visitados, camino):
    visitados.add(vertice)
    camino.append(vertice)
    if len(visitados)==len(grafo):
        return True
    for ady in grafo.adyacentes(vertice):
        if ady not in visitados:
            if camino_hamiltoniano_dfs(grafo,ady,visitados,camino):
                return True
    visitados.remove(vertice)
    camino.pop()
    return False