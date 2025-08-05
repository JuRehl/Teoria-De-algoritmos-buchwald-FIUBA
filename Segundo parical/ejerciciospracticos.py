from grafo import Grafo
from ejercicio2 import ford_fulkerson

"""Parcial 16/02/2024 2024c0-0"""
#Ejercicio1, complejidad:
def validador_subset_sum(lista,k,sol):
    suma=0
    set1=set(lista)
    for elem in sol:
        if elem not in set1:
            return False
        suma+=elem
    return suma==k

#Ejercicio 4, complejidad: O(V*E²)
def tuberia_a_destruir(plano, rios, zonas_riego):
    super_fuente = "S"
    super_sumidero = "T"
    grafo = Grafo(es_dirigido=True)
    for punto in plano.obtener_puntos():
        if punto not in grafo.obtener_vertices():
            grafo.agregar_vertice(punto)
            for conexion in plano.conexiones(punto):
                if plano.estan_unidos(punto, conexion):
                    grafo.agregar_vertice(conexion)
                    grafo.agregar_arista(punto, conexion, capacidad=1)
    grafo.agregar_vertice(super_fuente)
    grafo.agregar_vertice(super_sumidero)
    for rio in rios:
        grafo.agregar_arista(super_fuente, rio, float('inf'))
    for zona in zonas_riego:
        grafo.agregar_arista(zona, super_sumidero, float('inf'))
    residual = ford_fulkerson(grafo, super_fuente, super_sumidero)
    visitados = set()
    cola = [super_fuente]
    while cola:
        u = cola.pop(0)
        visitados.add(u)
        for w, cap_res in residual.get(u, {}).items():
            if cap_res > 0 and w not in visitados:
                cola.append(w)
    mejor_arista = None
    max_reduccion = 0
    for u in visitados:
        for v in grafo.adyacentes(u):
            if v not in visitados:
                capacidad = grafo.peso_arista(u, v)
                if residual.get(u, {}).get(v, 0) == 0:
                    if capacidad > max_reduccion:
                        max_reduccion = capacidad
                        mejor_arista = (u, v)
    return mejor_arista

"""Parcial 04/03/2024"""
#Ejercicio 3, complejidad: O(n*m) donde n es la cantidad de subconjuntos de S y m el tamaño maximo de un subconjunto si
def validador_hitting_set(U,s,k,H):
    if not set(H).issubset(U):
        return False
    if len(H)>k:
        return False
    for si in s:
        if set(H).isdisjoint(si):
            return False
    return True

"""Parcial 24/06/2024"""
#Ejercicio 3, complejidad:
def validador_cumpleaños_coty(invitados, conocidos, k, regalos):
    if len(regalos)>k:
        return False
    regalo=set(regalos)
    for persona1,persona2 in conocidos:
        if persona1 not in regalo and persona2 not in regalo:
            return False
    return True

"""Parcial 08/07/2024 2024c1-2"""
#Ejercicio 2, complejidad: O(V*E²) de FF pero V=n+p y E<=n+p+n*p donde n+p es despreciable a comparación de n*p
def definir_ambulancias(ambulancias, pedidos, km_abulancias):
    super_sumidero="T"
    super_fuente="S"
    grafo=Grafo(es_dirigido=True)
    grafo.agregar_vertice(super_fuente)
    grafo.agregar_vertice(super_sumidero)
    for pedido in pedidos:
        grafo.agregar_vertice(pedido)
        grafo.agregar_arista(pedido,super_sumidero,1)
    for ambulancia in ambulancias:
        grafo.agregar_vertice(ambulancia)
        grafo.agregar_arista(super_fuente,ambulancia,1)
        for pedido_posible in km_abulancias[ambulancia]: #supongo que km ambulancia diccionario con los pedidos que llega segun km
            grafo.agregar_arista(ambulancia,pedido_posible,1)
    
    flujo=ford_fulkerson(grafo,super_fuente,super_sumidero)
    flujo_total=0
    for ambulancia in ambulancias:
        arista=(super_fuente,ambulancia)
        if arista in flujo:
            flujo_total+=flujo[arista]
    
    return flujo_total==len(pedidos)

#Ejercicio 4, complejidad: O(v²) polinomial (v es la cantidad de vertices de g2)
def validador_subgrafo_isomorfo(g1,g2,mapeo):
    if len(set(mapeo.values())) != len(mapeo):
        return False
    for u in g2:
        for v in g2:
            arista_G2 = g2.obtener_arista(u,v)
            arista_G1 = g1.obtener_arista(mapeo[u], mapeo[v])
            if arista_G2 != arista_G1:
                return False
    return True

"""Parcial 04/11/2024 20242C-0"""
#Ejercicio 2, complejidad: O(n²) siendo n la cantidad de vértices del grafo
def validador_R_cliques(grafo, subconjuntos,R):
    if len(subconjuntos)>R:
        return False
    vertices=set()
    for subconjunto in subconjuntos:
        for v in subconjunto:
            if v in vertices:
                return False
            vertices.add(v)
    if vertices!=set(grafo.obtener_vertices()):
        return False
    for subconjunto in subconjuntos:
        for i in range(len(subconjunto)):
            for j in range(i+1,len(subconjunto)):
                v,w=subconjunto[i],subconjunto[j]
                if not grafo.estan_unidos(v,w):
                    return False
    return True

"""Parcial 05/12/2024 20242C-1"""
#Ejercicio 1, complejidad:

#Ejercicio 3, complejidad: O(m+n²) siendo m las amistades y n los invitados
def validador_antonina(invitados,amistades,mesas,k):
    if len(mesas)>k:
        return False
    invitaados_en_mesa=set()
    for mesa in mesas:
        for invitado in mesa:
            if invitado in invitaados_en_mesa:
                return False
            invitaados_en_mesa.add(invitado)
    if invitaados_en_mesa!=set(invitados):
        return False
    amistad=set()
    for a,b in amistades:#ordeno alfabeticamente para que sea más facil
        if a<b:
            amistad.add((a,b))
        else:
            amistad.add((b,a))
    for mesa in mesas:
        for i in range(len(mesa)):
            for j in range(i+1,len(mesa)):
                a,b=mesa[i],mesa[j]
                par = (a, b) if a < b else (b, a)
                if par not in amistad:
                    return False
    return True

"""Parcial 19/12/2024 20242C-2"""
#Ejercicio 3, complejidad: O(k*n) siendo k la cantidad de vértices del ciclo y n la cantidad de vértices del grafo
def validador_k_ciclo(grafo,k,ciclo):
    if len(ciclo)<k:
        return False
    if ciclo[0]!=ciclo[-1]:
        return False
    for v in ciclo:
        if v not in grafo.obtener_vertices():
            return False
    for i in range(len(ciclo)-1):
        u,v=ciclo[i],ciclo[i+1]
        if not grafo.estan_unidos(u,v):
            return False
    if len(set(ciclo[:-1])) != len(ciclo) - 1:
        return False
    return True

"""Parcial 10/02/2025 20242C-3"""
#Ejercicio 5, complejidad: O(n) siendo n la cantidad de vértices del grafo
def validador_hc(grafo, k,s,ciclo):
    if len(s)<k:
        return False
    vertices = list(grafo.obtener_vertices())
    n = len(vertices)
    if len(ciclo) != n + 1:
        return False
    if ciclo[0] != ciclo[-1]:
        return False
    visitados = set()
    for v in ciclo[:-1]:
        if v in visitados:
            return False
        visitados.add(v)
    if visitados != set(vertices):
        return False
    for i in range(len(ciclo) - 1):
        u, w = ciclo[i], ciclo[i+1]
        if not hay_arista_completado(grafo, s, u, w):
            return False
    return True
def hay_arista_completado(G, S, u, v):
    if (u, v) in S or (v, u) in S:
        return True
    return G.hay_arista(u, v)

"""Parcial 24/02/2025 20242C-4"""
#Ejercicio 4, complejidad: O(n) siendo n la cantidad de alumnos 
def validador_fila_primario(alumnos, amistades,fila):
    if len(fila)!=len(alumnos):
        return False
    for i in range(len(fila)-1):
        alumno=fila[i]
        siguiente=fila[i+1]
        if  siguiente in set(amistades[alumno]):
            return False
    return True
