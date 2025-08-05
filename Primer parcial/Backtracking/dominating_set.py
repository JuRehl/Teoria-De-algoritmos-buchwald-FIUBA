def dominating_set_min(grafo):
    vertices=grafo.obtener_vertices()
    return list(dominating_set_min_bt(grafo,vertices,0,set(vertices),set([])))

def dominating_set_min_bt(grafo, vertices, vertice_actual, mejor_sol, sol_parcial):
    if len(sol_parcial)>=len(mejor_sol):
        return mejor_sol
    if es_set_min(grafo,sol_parcial):
        return set(sol_parcial)
    if len(vertices)==vertice_actual:
        return mejor_sol
    v=vertices[vertice_actual]
    sol_parcial.add(v)
    mejor_sol=dominating_set_min_bt(grafo,vertices,vertice_actual+1,mejor_sol,sol_parcial)
    sol_parcial.remove(v)
    return dominating_set_min_bt(grafo,vertices,vertice_actual+1,mejor_sol,sol_parcial)
     

def es_set_min(grafo, sol_parcial):
    for v in grafo.obtener_vertices():
        if v in sol_parcial:
            continue
        ady=False
        for a in grafo.adyacentes(v):
            if a in sol_parcial:
                ady= True
                break
        if not ady:
            return False
    return True