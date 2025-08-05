def colorear(grafo, n):
    return colorear_bt(grafo,grafo.obtener_vertices(),0,n,{})

def colorear_bt(grafo,vertices, vertice_actual,n,colores):
    if len(colores)==len(vertices):
        return True
    vertice=vertices[vertice_actual]
    for color in range(n):
        colores[vertice]=color
        if not es_compatible(colores,grafo,vertice):
            continue
        if colorear_bt(grafo,vertices,vertice_actual+1,n,colores):
            return True
    del colores[vertice]
    return False

def es_compatible(colores,grafo,vertice):
    for ady in grafo.adyacentes(vertice):
        if ady in colores and colores[ady]==colores[vertice]:
            return False
    return True