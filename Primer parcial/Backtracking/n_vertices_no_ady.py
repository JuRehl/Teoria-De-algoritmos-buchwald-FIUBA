def no_adyacentes(grafo, n):
    sol=set()
    if no_adyacentes_bt(grafo,n,sol,0,grafo.obtener_vertices()):
        return list(sol)
    return None

def no_adyacentes_bt(grafo,n, subconj, vertice_actual,vertices):
    if len(subconj)==n:
        return True
    if vertice_actual>=len(vertices):#si ya nos pasamos no es!!!!
        return False
    if no_adyacentes_bt(grafo,n,subconj,vertice_actual+1,vertices):
        return True
    v=vertices[vertice_actual]
    if es_compatible(grafo,v,subconj):
        subconj.add(v)
        if no_adyacentes_bt(grafo,n,subconj,vertice_actual+1,vertices):
            return True
        subconj.remove(v)
    return False
    

def es_compatible(grafo, vertice,subconj):
    for ady in grafo.adyacentes(vertice):
        if ady in subconj:
            return False
    return True