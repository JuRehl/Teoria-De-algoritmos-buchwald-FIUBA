def independent_set(grafo):
    return list(independent_set_bt(grafo, grafo.obtener_vertices(),0,set(),set()))

def independent_set_bt(grafo, vertices, vertice_actual, sol_p,sol_op):
    if vertice_actual==len(vertices):
        if len(sol_p)>len(sol_op):
            return set(sol_p)
        return sol_op
    vertice=vertices[vertice_actual]
    if es_independent(grafo, sol_p, vertice):
        sol_p.add(vertice)
        sol_op=independent_set_bt(grafo,vertices,vertice_actual+1,sol_p,sol_op)
        sol_p.remove(vertice)
    return independent_set_bt(grafo, vertices,vertice_actual+1,sol_p,sol_op)

def es_independent(grafo, sol_p,v):
    for ady in grafo.adyacentes(v):
        if ady in sol_p:
            return False
    return True