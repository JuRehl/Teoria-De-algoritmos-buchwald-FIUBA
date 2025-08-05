import os
import time
import subprocess
import matplotlib.pyplot as plt
from collections import defaultdict

def obtener_categoria(nombre_archivo):
    return " ".join(nombre_archivo.replace(".txt", "").split("_")[1:])

def medir_tiempo(path):
    inicio = time.perf_counter()
    subprocess.run(["python3", "tp1.py", path], stdout=subprocess.DEVNULL)
    fin = time.perf_counter()
    return fin - inicio

def main():
    carpeta = "pruebas_propias"
    archivos = [a for a in os.listdir(carpeta) if a.endswith(".txt")]

    tiempos_por_categoria = defaultdict(list)

    for archivo in archivos:
        categoria = obtener_categoria(archivo)
        path = os.path.join(carpeta, archivo)
        tiempo = medir_tiempo(path)
        tiempos_por_categoria[categoria].append(tiempo)

    categorias = sorted(tiempos_por_categoria.keys())
    promedios = [sum(tiempos_por_categoria[cat]) / len(tiempos_por_categoria[cat]) for cat in categorias]

    plt.figure(figsize=(10, 6))
    barras = plt.bar(categorias, promedios, color="pink")

    for barra, tiempo in zip(barras, promedios):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height(), f"{tiempo:.4f}s",
                 ha='center', va='bottom', fontsize=9)

    plt.xlabel("Tipo de test")
    plt.ylabel("Tiempo promedio de ejecución (s)")
    plt.title("Tiempo de ejecución por tipo de test")
    plt.xticks(rotation=45)
    plt.ylim(0, max(promedios)*1.2)  
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    os.makedirs("graficos", exist_ok=True)
    plt.savefig("graficos/tiempo_por_tipo_de_test.png")
    plt.show()  
    plt.close()

if __name__ == "__main__":
    main()
