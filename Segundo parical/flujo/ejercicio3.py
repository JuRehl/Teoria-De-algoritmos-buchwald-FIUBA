from grafo import Grafo
""" Dada una red y un diccionario que representa los valores de los flujos para las aristas, todos valores que respetan 
la restricción de cada arista, construir la red residual que refleja el estado actual de la red en función a los valores 
de flujo dados."""

def reconstruccion(grafo, flujo): #O(V+E)
    residual=Grafo(es_dirigido=True)
    for u in grafo.obtener_vertices():
        residual.agregar_vertice(u)
        for v in grafo.adyacentes(u):
            capacidad=grafo.pesoarista(u,v)
            f=flujo.get((u,v),0)
            # Arista u → v con capacidad residual
            if capacidad-f>0:
                residual.agregar_arista(u,v,capacidad-f)
            # Arista v → u con capacidad residual (flujo inverso posible)
            if f>0:
                residual.agregar_vertice(v)
                residual.agregar_arista(v,u,f)
    return residual
