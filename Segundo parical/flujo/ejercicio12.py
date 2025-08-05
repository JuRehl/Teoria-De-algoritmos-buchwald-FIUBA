from grafo import Grafo
from ejercicio2 import ford_fulkerson
"""Suponer que queremos schedulear cómo los aviones van de un aeropuerto a otro para cumplir sus horarios. Podemos decir que podemos 
usar un avión para un segmento/vuelo i y luego para otro j si se cumple alguna de las siguientes condiciones: a. El destino de i y el 
origen de j son el mismo. o b. Podemos agregar un vuelo desde el destino de i al origen de j con tiempo suficiente. Decimos que el vuelo 
j es alcanzable desde el vuelo i si es posible usar el avión del vuelo i y después para el vuelo j.Dados todos los vuelos con origen y 
destino, y el tiempo que tarda un avión entre cada par de ciudades queremos decidir: ¿Podemos cumplir con los m vuelos usando a lo sumo 
k aviones? Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se decide si es posible 
cumplir con la premisa. ¿Cuál es el orden temporal de la solución implementada?"""

def puede_cumplir_vuelos(grafo_vuelos, vuelos, k):
    grafo_flujo = Grafo(dirigido=True)

    # Crear nodos para cada vuelo
    for vuelo in vuelos:
        grafo_flujo.agregar_vertice(vuelo)

    # Agregar aristas entre vuelos alcanzables
    for v in vuelos:
        for w in vuelos:
            if v != w and vuelo_w_es_alcanzable_desde_vuelo_v(vuelos,v, w):
                grafo_flujo.agregar_arista(v, w, 1)

    # Agregar super fuente y super sumidero
    fuente = "S"
    sumidero = "T"
    grafo_flujo.agregar_vertice(fuente)
    grafo_flujo.agregar_vertice(sumidero)

    # Conectar fuente con vuelos iniciales (hasta k aristas)
    for vuelo in vuelos:
        if es_vuelo_inicial(vuelo, vuelos):
            grafo_flujo.agregar_arista(fuente, vuelo, 1)

    # Conectar vuelos finales con sumidero
    for vuelo in vuelos:
        if es_vuelo_final(vuelo, vuelos):
            grafo_flujo.agregar_arista(vuelo, sumidero, 1)

    # Límite de flujo total: agregamos nodo intermedio si queremos limitar a K
    # Alternativamente, sólo permitimos hasta K aristas desde la fuente

    flujo = ford_fulkerson(grafo_flujo, fuente, sumidero)
    return flujo >= len(vuelos)

def vuelo_w_es_alcanzable_desde_vuelo_v(vuelo,v, w):
    return v[1] == w[0] or hay_tiempo_para_conectar(vuelo,v, w)

def hay_tiempo_para_conectar(vuelo,v, w):
    return vuelo.tiempo_llegada(v) + vuelo.tiempo_de_transbordo(v[1], w[0]) <= vuelo.tiempo_salida(w)

def es_vuelo_inicial(v, vuelos):
    # No hay ningún vuelo que pueda preceder a v
    return not any(vuelo_w_es_alcanzable_desde_vuelo_v(vuelos,u, v) for u in vuelos if u != v)

def es_vuelo_final(v, vuelos):
    # No hay ningún vuelo que pueda continuar después de v
    return not any(vuelo_w_es_alcanzable_desde_vuelo_v(vuelos,v, u) for u in vuelos if u != v)
