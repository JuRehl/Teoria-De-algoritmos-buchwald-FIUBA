"""El problema del Vertex Cover se define como: dado un grafo no dirigido, obtener el mínimo subconjunto de vértices del grafo tal que 
toda arista del grafo tenga al menos uno de sus vértices perteneciendo al subconjunto. Dicho conjunto es un Vertex Cover. Definir el 
problema de decisión del Vertex Cover. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del 
verificador implementado? Justificar"""
#Complejidad O(V+E) por lo que es polinomial y cumple con np
def es_vertex_cover(grafo,subconj,k):
    if len(subconj)>k:
        return False
    for vertice in grafo.obtener_vertices():
        for ady in grafo.adyacentes(vertice):
            if vertice not in subconj and ady not in subconj: #supongo que subconj es un set
                return False
    return True