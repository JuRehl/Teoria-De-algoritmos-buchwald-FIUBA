from grafo import Grafo
# conocidos: lista de pares de invitados que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    grafo = Grafo()

    for c in conocidos:
        for i in range(0, 2):
            if c[i] not in grafo:
                grafo.agregar_vertice(c[i])
        grafo.agregar_arista(c[0], c[1])

    while len(grafo) != 0:
        borrar = []
        for v in grafo.obtener_vertices():
            if len(grafo.adyacentes(v)) < 4:
                borrar.append(v)        

        if borrar == []:
            break

        for v in borrar:
            grafo.borrar_vertice(v) 

    return grafo.obtener_vertices()