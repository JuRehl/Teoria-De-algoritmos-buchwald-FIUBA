import networkx as nx
import random
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_PRUEBAS = os.path.join(BASE_DIR, "pruebas_propias")
CARPETA_PRUEBAS_VOL = os.path.join(BASE_DIR, "pruebas_volumen")

os.makedirs(CARPETA_PRUEBAS, exist_ok=True)
os.makedirs(CARPETA_PRUEBAS_VOL, exist_ok=True)

def guardar_grafo_formato_tp(G, nombre, carpeta=CARPETA_PRUEBAS):
    ruta = os.path.join(carpeta, f"{nombre}.txt")
    with open(ruta, "w") as f:
        f.write("# grafo generado automáticamente para TP3\n")
        for u, v in G.edges():
            f.write(f"{u},{v}\n")

def k_para_erdos(n, p):
    if p < 0.3:
        return max(2, n // 3)
    else:
        return max(1, n // 5)



def generar_grafo_estrella():
    G = nx.Graph()
    G.add_edges_from([(0, i) for i in range(1, 6)])
    nombre = "estrella"
    guardar_grafo_formato_tp(G, nombre)
    return nombre, 2  

def generar_grafo_ciclo():
    G = nx.cycle_graph(6)
    nombre = "ciclo"
    guardar_grafo_formato_tp(G, nombre)
    return nombre, 2  

def generar_grafo_clique():
    G = nx.complete_graph(5)
    nombre = "clique"
    guardar_grafo_formato_tp(G, nombre)
    return nombre, 1  


def generar_grafos_aleatorios():
    tamaños = [10, 15]
    probabilidades = [0.2, 0.5]
    seeds = [1, 2]
    resultados = []
    for n in tamaños:
        for p in probabilidades:
            for s in seeds:
                G = nx.erdos_renyi_graph(n, p, seed=s)
                nombre = f"erdos_n{n}_p{int(p*10)}_s{s}"
                guardar_grafo_formato_tp(G, nombre)
                k = k_para_erdos(n, p)
                resultados.append((nombre, k))
    return resultados


def generar_grafo_con_comunidades(cantidad=3, tamaño=5, conexiones=2, volumen=False):
    G = nx.Graph()
    offset = 0
    comunidades = []

    for _ in range(cantidad):
        C = nx.complete_graph(tamaño)
        mapping = {n: n + offset for n in C.nodes()}
        C = nx.relabel_nodes(C, mapping)
        G.add_edges_from(C.edges())
        comunidades.append(list(C.nodes()))
        offset += tamaño

    for i in range(cantidad):
        for j in range(i + 1, cantidad):
            for _ in range(conexiones):
                u = random.choice(comunidades[i])
                v = random.choice(comunidades[j])
                G.add_edge(u, v)
    if volumen:
        nombre = f"volumen_{cantidad}x{tamaño}_inter{conexiones}"
        guardar_grafo_formato_tp(G, nombre, CARPETA_PRUEBAS_VOL)
    else:
        nombre = f"comunidades_{cantidad}x{tamaño}_inter{conexiones}"
        guardar_grafo_formato_tp(G, nombre)
    return nombre, cantidad  


CANT_GRAFOS_VOL = [
    (300, 20, 2),
    (200, 15, 2),
    (150, 12, 3),
    (120, 9, 4),
    (100, 10, 3),
    (60, 7, 5),
    (50, 8, 4),
    (50, 5, 2),
    (40, 6, 6),
    (35, 5, 8),
    (30, 4, 3),
    (25, 4, 10),
    (25, 3, 6),
    (20, 3, 7),
    (15, 3, 4),
    (12, 2, 6),
    (10, 2, 5),
    (9, 2, 7),
    (8, 1, 10),
    (6, 1, 8)
]

def generar_pruebas_volumen():
    resultados = []
    for cantidad, tamaño, conexiones in CANT_GRAFOS_VOL:
        nombre, k = generar_grafo_con_comunidades(cantidad, tamaño, conexiones, True)
        resultados.append((nombre, k))
    return resultados


def main():
    k_por_grafo = {}
    k_por_grafo_volumen = {}

    nombre, k = generar_grafo_estrella()
    k_por_grafo[nombre] = k

    nombre, k = generar_grafo_ciclo()
    k_por_grafo[nombre] = k

    nombre, k = generar_grafo_clique()
    k_por_grafo[nombre] = k

    resultados_aleatorios = generar_grafos_aleatorios()
    for nombre, k in resultados_aleatorios:
        k_por_grafo[nombre] = k

    nombre, k = generar_grafo_con_comunidades()
    k_por_grafo[nombre] = k

    resultados_volumen = generar_pruebas_volumen()
    for nombre, k in resultados_volumen:
        k_por_grafo_volumen[nombre] = k

    ruta_k = os.path.join(CARPETA_PRUEBAS, "k_por_grafo.json")
    with open(ruta_k, "w") as f:
        json.dump(k_por_grafo, f, indent=4)

    ruta_k_volumen = os.path.join(CARPETA_PRUEBAS_VOL, "k_por_grafo_volumen.json")
    with open(ruta_k_volumen, "w") as f:
        json.dump(k_por_grafo_volumen, f, indent=4)

    print(f"Generación de grafos terminada.")

if __name__ == "__main__":
    main()
