from grafo import Grafo
from ejercicio2 import ford_fulkerson
"""Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar juntos para ir 
a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos! Sólo aceptan pasar por 
las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la escuela quedan en esquinas, pero no está seguro si 
es posible enviar a sus 5 hijos a la misma escuela. No se puede asumir que la ciudad tenga alguna forma en específico, por ejemplo, no 
hay que asumir que todas las calles sean cuadradas. Utilizando lo visto en la materia, formular este problema y resolverlo. Indicar y 
justificar la complejidad del algoritmo."""
#O(V*E) donde V son las esquinas y E las cuadras o calles
def carlos_puede_enviar_a_sus_hijos(grafo, casa, escuela):
    grafo_flujo = Grafo(dirigido=True)

    for v in grafo.obtener_vertices():
        grafo_flujo.agregar_vertice(v)

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            # Si el grafo es no dirigido, evitamos duplicar
            if not grafo.es_dirigido() and grafo_flujo.estan_unidos(w, v):
                continue
            grafo_flujo.agregar_arista(v, w, 1)

    flujo = ford_fulkerson(grafo_flujo, casa, escuela)
    return flujo >= 5