from grafo import Grafo
from ejercicio2 import ford_fulkerson
def asignar_representantes(habitantes, clubs, partidos):
    # Crear grafo dirigido vacío
    grafo = Grafo()

    # Nodos especiales
    fuente = "S"
    sumidero = "T"
    
    # Agregar fuente y sumidero
    grafo.agregar_vertice(fuente)
    grafo.agregar_vertice(sumidero)

    n = len(habitantes)

    # 1. Fuente -> Clubes (capacidad 1)
    for club in clubs:
        grafo.agregar_vertice(club)
        grafo.agregar_arista(fuente, club, 1)

    # 2. Club -> Persona (capacidad 1)
    for persona in habitantes:
        grafo.agregar_vertice(persona["id"])
        for club in persona["clubs"]:
            # club puede asignar a esta persona
            grafo.agregar_arista(club, persona["id"], 1)

    # 3. Persona -> Partido (capacidad 1)
    for persona in habitantes:
        partido = persona["partido"]
        if partido not in grafo.vertices:
            grafo.agregar_vertice(partido)
        grafo.agregar_arista(persona["id"], partido, 1)

    # 4. Partido -> Sumidero (capacidad floor(n/2))
    limite_partido = n // 2
    for partido in partidos:
        if partido not in grafo.vertices:
            grafo.agregar_vertice(partido)
        grafo.agregar_arista(partido, sumidero, limite_partido)

    # Ejecutar Ford-Fulkerson
    flujo_max = ford_fulkerson(grafo, fuente, sumidero)

    # Verificar si se logró asignar un representante a cada club
    if flujo_max == len(clubs):
        print("Existe asignación válida")
        # Podés recuperar la asignación leyendo el flujo en aristas club->persona
    else:
        print("No existe asignación válida")

    return flujo_max
