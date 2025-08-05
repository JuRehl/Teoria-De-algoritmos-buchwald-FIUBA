import os
import time
import subprocess
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path
import json

RUTA_PRUEBAS = Path("pruebas_propias")
VALORES_K = Path("pruebas_propias/k_por_grafo.json")
REPETICIONES = 5  # cantidad de veces que se ejecuta cada prueba

def obtener_categoria(nombre_archivo):
    return nombre_archivo.replace(".txt", "")

def medir_tiempo(archivo_grafo, k):
    inicio = time.perf_counter()
    subprocess.run(
        ["python3", "tp3.py", str(archivo_grafo), str(k)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return time.perf_counter() - inicio

def main():
    tiempos_por_categoria = defaultdict(list)

    with open(VALORES_K, "r") as archivo:
        datos = json.load(archivo)

    for archivo in RUTA_PRUEBAS.iterdir():
        if not archivo.is_file() or not archivo.name.endswith(".txt"):
            continue

        cat = obtener_categoria(archivo.name)

        k = datos[cat]
        tiempos = []

        for _ in range(REPETICIONES):
            t = medir_tiempo(archivo, k)
            tiempos.append(t)

        promedio = sum(tiempos) / REPETICIONES
        tiempos_por_categoria[cat].append(promedio)
        print(f"{cat:25s}: {promedio:.4f}s  (k = {k})")

    categorias = sorted(tiempos_por_categoria)
    etiquetas = [f"{cat}\nk={datos[cat]}" for cat in categorias]
    promedios = [sum(tiempos_por_categoria[c]) / len(tiempos_por_categoria[c]) for c in categorias]

    plt.figure(figsize=(10, 6))
    barras = plt.bar(etiquetas, promedios, color="skyblue")
    for b, p in zip(barras, promedios):
        plt.text(b.get_x() + b.get_width() / 2, b.get_height(), f"{p:.4f}s",
                 ha='center', va='bottom', fontsize=9)
    plt.xlabel("Archivo de prueba")
    plt.ylabel("Tiempo promedio (s)")
    plt.title(f"Tiempo de ejecución promedio (Programación Lineal)")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    os.makedirs("graficos", exist_ok=True)
    plt.savefig(f"graficos/tiempo_por_test_pl.png")
    plt.show()

if __name__ == "__main__":
    main()
