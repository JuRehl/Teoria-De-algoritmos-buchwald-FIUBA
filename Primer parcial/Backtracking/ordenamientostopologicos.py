def contar_ordenamientos(grafo):
    visitados=set()
    resultado=[]
    contar_ordenamientos_bt(grafo,visitados,[],resultado)
    return len(resultado)

def contar_ordenamientos_bt(grafo,visitados,parcial,resultado):
    if len(parcial)==len(grafo):
        resultado.append(parcial.copy())
        return 
    for v in grafo.obtener_vertices():
        if v not in visitados and predecesores_visitados(grafo,v,visitados):
            visitados.add(v)
            parcial.append(v)
            contar_ordenamientos_bt(grafo,visitados,parcial,resultado)
            parcial.pop()
            visitados.remove(v)

def predecesores_visitados(grafo,v,visitados):
    for ver in grafo.obtener_vertices():
        if v in grafo.adyacentes(ver) and ver not in visitados:
            return False
    return True