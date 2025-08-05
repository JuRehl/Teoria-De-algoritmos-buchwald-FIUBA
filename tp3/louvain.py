import random
from collections import deque
from grafo import Grafo
import auxiliares
import sys

def algoritmo_louvain_completo(grafo, k):
    grafo_actual = grafo
    comunidad_total = {v: v for v in grafo}

    while True:
        comunidad_parcial = fase_1_louvain(grafo_actual, k)
        comunidad_parcial = renombrar_comunidades(comunidad_parcial)

        nueva_comunidad_total = {
            v: comunidad_parcial[comunidad_total[v]] for v in comunidad_total
        }

        if nueva_comunidad_total == comunidad_total:
            break

        comunidad_total = nueva_comunidad_total
        grafo_actual = crear_grafo_colapsado(grafo_actual, comunidad_parcial)

    diametro = diametro_maximo_clusters(grafo, comunidad_total)
    return comunidad_total, diametro


def fase_1_louvain(grafo, max_clusters):
    comunidad = {v: i for i, v in enumerate(grafo)}
    m2 = grafo.peso_total_aristas() * 2
    grados = {v: grafo.suma_pesos_adyacentes(v) for v in grafo}

    while len(set(comunidad.values())) > max_clusters:
        sum_totales = {}
        for v, c in comunidad.items():
            sum_totales[c] = sum_totales.get(c, 0) + grados[v]

        comunidades_ordenadas = sorted(sum_totales.items(), key=lambda x: x[1])

        c1, _ = comunidades_ordenadas[0]
        c2, _ = comunidades_ordenadas[1]

        for v in comunidad:
            if comunidad[v] == c2:
                comunidad[v] = c1

    sum_in = {}
    sum_tot = {}

    for v in grafo:
        c = comunidad[v]
        sum_tot[c] = sum_tot.get(c, 0) + grados[v]
        for w in grafo.adyacentes(v):
            if comunidad[w] == c:
                sum_in[c] = sum_in.get(c, 0) + grafo.peso_arista(v, w)
    for c in sum_in:
        sum_in[c] /= 2

    mejorado = True
    while mejorado:
        mejorado = False
        vertices = list(grafo)
        random.shuffle(vertices)
        comunidades_activas = set(comunidad.values())

        for v in vertices:
            c_actual = comunidad[v]

            sum_tot[c_actual] = sum_tot.get(c_actual, 0) - grados[v]
            conexiones_c_actual = sum(
                grafo.peso_arista(v, w) for w in grafo.adyacentes(v) if comunidad[w] == c_actual
            )
            sum_in[c_actual] = sum_in.get(c_actual, 0) - 2 * conexiones_c_actual

            conexiones_comunidades = {}
            for w in grafo.adyacentes(v):
                c_w = comunidad[w]
                conexiones_comunidades[c_w] = conexiones_comunidades.get(c_w, 0) + grafo.peso_arista(v, w)

            max_delta = float('-inf')
            mejor_c = c_actual

            opciones = set(conexiones_comunidades.keys())
            opciones.add(c_actual)

            puede_crear_nueva = len(comunidades_activas) < max_clusters
            nueva_com_id = max(comunidades_activas, default=-1) + 1 if puede_crear_nueva else None
            if puede_crear_nueva:
                opciones.add(nueva_com_id)

            for c in opciones:
                if c == nueva_com_id and not puede_crear_nueva:
                    continue
                k_i_in = conexiones_comunidades.get(c, 0)
                sum_tot_c = sum_tot.get(c, 0)
                delta_q = (k_i_in / m2) - (grados[v] * sum_tot_c) / (m2 * m2)

                if delta_q > max_delta:
                    max_delta = delta_q
                    mejor_c = c

            comunidad[v] = mejor_c
            sum_tot[mejor_c] = sum_tot.get(mejor_c, 0) + grados[v]
            sum_in[mejor_c] = sum_in.get(mejor_c, 0) + 2 * conexiones_comunidades.get(mejor_c, 0)

            if mejor_c != c_actual:
                mejorado = True

    return comunidad


def crear_grafo_colapsado(grafo_original, comunidad_actual):
    nuevo_grafo = Grafo(es_dirigido=False)
    comunidad_a_nodos = {}

    for nodo, com in comunidad_actual.items():
        comunidad_a_nodos.setdefault(com, set()).add(nodo)
        nuevo_grafo.agregar_vertice(com)

    for com1 in comunidad_a_nodos:
        for com2 in comunidad_a_nodos:
            if com1 > com2:
                continue

            peso_total = 0
            for v in comunidad_a_nodos[com1]:
                for w in comunidad_a_nodos[com2]:
                    if grafo_original.estan_unidos(v, w):
                        peso_total += grafo_original.peso_arista(v, w)

            if com1 == com2:
                peso_total //= 2  

            if peso_total > 0:
                nuevo_grafo.agregar_arista(com1, com2, peso_total)

    return nuevo_grafo


def renombrar_comunidades(comunidad):
    nueva_comunidad = {}
    mapa = {}
    contador = 0
    for nodo in comunidad:
        c = comunidad[nodo]
        if c not in mapa:
            mapa[c] = contador
            contador += 1
        nueva_comunidad[nodo] = mapa[c]
    return nueva_comunidad


def bfs(grafo, inicio, nodos_validos):
    visitados = {inicio: 0}
    cola = deque([inicio])
    while cola:
        actual = cola.popleft()
        for vecino in grafo.adyacentes(actual):
            if vecino in nodos_validos and vecino not in visitados:
                visitados[vecino] = visitados[actual] + 1
                cola.append(vecino)
    return visitados

def diametro_subgrafo(grafo, vertices_comunidad):
    max_distancia = 0
    for v in vertices_comunidad:
        distancias = bfs(grafo, v, set(vertices_comunidad))
        if distancias:
            max_distancia = max(max_distancia, max(distancias.values()))
    return max_distancia

def diametro_maximo_clusters(grafo, comunidad_total):
    clusters = {}
    for nodo, cluster in comunidad_total.items():
        clusters.setdefault(cluster, []).append(nodo)

    diametros = []
    for vertices in clusters.values():
        diam = diametro_subgrafo(grafo, vertices)
        diametros.append(diam)
    return max(diametros, default=0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 louvain.py <archivo_grafo> <k>")
        sys.exit(1)

    archivo = sys.argv[1]
    k = int(sys.argv[2])

    grafo = auxiliares.construir_grafo(archivo)
    comunidades, diametro = algoritmo_louvain_completo(grafo, k)

    print(f"{archivo} {k}")
    print("Asignación:")

    clusters = {}
    for nodo, cluster_id in comunidades.items():
        clusters.setdefault(cluster_id, []).append(nodo)

    for cluster_id in sorted(clusters):
        nodos = sorted(clusters[cluster_id], key=int)
        print(f"Cluster {cluster_id} : {nodos}")

    print(f"Maxima distancia dentro del cluster: {diametro}")
