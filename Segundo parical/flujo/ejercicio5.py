import ejercicio4
""" Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una artista 
(por ejemplo, a una arista de capacidad 3 se le aumenta a 4, permita obtener el nuevo flujo máximo en tiempo lineal en vértices 
y aristas. Indicar y justificar la complejidad del algoritmo implementado."""

def aumento_aristas(residual,grafo,flujo,s,t,u,v): #O(V+E)
    if residual.hay_arista(u,v):
        residual.modificar_peso(u,v,residual.peso_arista(u,v)+1)
    else:
        residual.agregar_arista(u,v,1)
    camino=ejercicio4.camino_mas_corto(residual,s,t)
    if not camino:
        return flujo
    for i in range(len(camino)-1):
        a,b=camino[i],camino[i+1]
        f=flujo.get((a,b),0)
        flujo[(a,b)]=f+1
        flujo[(b,a)]=flujo.get((b,a),0)-1
        capacidad=residual.peso_arista(a,b)
        residual.modificar_peso(a,b,capacidad-1)
        if residual.hay_arista(b,a):
            residual.modificar_peso(b,a,residual.peso_arista(b,a)+1)
        else:
            residual.agregar_arista(b,a,1)