def vertex_cover_min(grafo):
    return list(vertex_cover_min_bt(grafo, grafo.obtener_vertices(),0,set(grafo.obtener_vertices()),set()))

def vertex_cover_min_bt(grafo, vertices, vertice_actual, mejor_solucion, solucion_parcial):
    if vertice_actual==len(vertices):
        if es_solucion(grafo,solucion_parcial) and len(solucion_parcial)<len(mejor_solucion):
            return set(solucion_parcial)
        return mejor_solucion
    v=vertices[vertice_actual]
    solucion_parcial.add(v)
    mejor_solucion=vertex_cover_min_bt(grafo,vertices,vertice_actual+1,mejor_solucion,solucion_parcial)
    solucion_parcial.remove(v)
    mejor_solucion=vertex_cover_min_bt(grafo,vertices,vertice_actual+1,mejor_solucion,solucion_parcial)
    return mejor_solucion
    
def es_solucion(grafo, solucion_parcial):
    for v in grafo.obtener_vertices():
        for ady in grafo.adyacentes(v):
            if v not in solucion_parcial and ady not in solucion_parcial:
                return False
    return True