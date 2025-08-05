from grafo import Grafo
from ejercicio2 import ford_fulkerson
"""Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices s y t, 
encontrar el máximo número de caminos disjuntos s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo 
se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. ¿Cuál es el orden temporal de la solución implementada?"""
def max_caminos_disjuntos(grafo, s, t):
    # Construir un nuevo grafo de capacidades
    red = Grafo()
    
    for u in grafo.obtener_vertices():
        red.agregar_vertice(u)
    
    for u in grafo.obtener_vertices():
        for v in grafo.adyacentes(u):
            red.agregar_arista(u, v, capacidad=1)
    
    flujo_maximo = ford_fulkerson(red, s, t)
    return flujo_maximo
