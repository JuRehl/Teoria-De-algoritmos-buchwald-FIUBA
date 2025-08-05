import os
import subprocess
import time
from pathlib import Path
import random
from matplotlib import pyplot as plt
import numpy as np
from sys import stdin

VECES = 20
RUTA_CARPETA = Path("pruebas_mediciones")

CANTIDAD_DICT = 1000
CANTIDADES_ENTRADA = [10, 25, 50, 100, 150, 250, 500, 1000, 1500, 2000, 3000, 5000, 10000, 25000, 50000, 100000]

def generar_test_volumen():
    with open("0_palabras_todas.txt", "r") as file:
        palabras = set(line.strip() for line in file if line.strip())
    
    palabras_seleccionadas = random.sample(list(palabras), CANTIDAD_DICT)
    nombre_archivo = f"{RUTA_CARPETA}/diccionario.txt"
    with open(nombre_archivo, "w") as file:
        file.write('\n'.join(palabras_seleccionadas))
    
    return palabras_seleccionadas

def generar_cadenas(diccionario, largo_cadena):
    cadenas = []
    cadena = []
    
    for _ in range(largo_cadena):
        cadena.append(random.choice(diccionario))
    cadenas.append("".join(cadena)) # cadena que esta bien
    cadenas.append("w".join(cadena)) # cadena que esta mal

    
    with open(f"{RUTA_CARPETA}/{largo_cadena}_in.txt", "w") as file:
        for cadena in cadenas:
            file.write(f"{cadena}\n")


def ejecutar_pruebas_volumen():
    archivos = [f"{RUTA_CARPETA}/{archivo.name}" for archivo in RUTA_CARPETA.iterdir() if (archivo.is_file() and archivo.name.endswith("_in.txt"))]
    comando = ["python3", "tp2.py", f"{RUTA_CARPETA}/diccionario.txt"]
    promedios = {}
    for archivo in archivos:
        total = 0
        for _ in range(VECES):
            start = time.time()
            with open(archivo, "r") as file:
                subprocess.run(comando, stdin=file, capture_output=True, text=True)
            stop = time.time()
            tiempo = stop - start
            total+=tiempo
        promedios[archivo] = float(total) / VECES
    return promedios

def generar_graficos_y_error(promedios):
    valores_x = []
    valores_y = []
    for clave, valor in promedios.items():
        _, cantidad = clave.split("/")
        cantidad, _ = cantidad.split("_")
        valores_x.append(int(cantidad))
        valores_y.append(valor)

    x = np.array(valores_x)
    y = np.array(valores_y)
    x_ajustado = np.linspace(min(x), max(x), 200)

    # Ajuste cuadrático
    A_cuadratico = np.vstack([x**2, x, np.ones_like(x)]).T
    coef_cuadratico, _, _, _ = np.linalg.lstsq(A_cuadratico, y, rcond=None)
    a2, a1, a0 = coef_cuadratico
    y_ajustado_cuadratico = a2 * x_ajustado**2 + a1 * x_ajustado + a0

    # Ajuste cúbico
    A_cubico = np.vstack([x**3, x**2, x, np.ones_like(x)]).T
    coef_cubico, _, _, _ = np.linalg.lstsq(A_cubico, y, rcond=None)
    b3, b2, b1, b0 = coef_cubico
    y_ajustado_cubico = b3 * x_ajustado**3 + b2 * x_ajustado**2 + b1 * x_ajustado + b0


    print(f"Función cuadrática ajustada: f(x) ≈ {a2:.3e}x² + {a1:.3e}x + {a0:.3e}\n")
    print(f"Función cúbica ajustada: f(x) ≈ {b3:.3e}x³ + {b2:.3e}x² + {b1:.3e}x + {b0:.3e}\n")

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='red', label='Datos originales')
    plt.plot(x_ajustado, y_ajustado_cuadratico, color='blue', label='Ajuste cuadrático')
    plt.plot(x_ajustado, y_ajustado_cubico, color='green', label='Ajuste cúbico')
    plt.title(f'Ajuste cuadrático: f(x) ≈ {a2:.3e}x² + {a1:.3e}x + {a0:.3e}\nAjuste cúbico: f(x) ≈ {b3:.3e}x³ + {b2:.3e}x² + {b1:.3e}x + {b0:.3e}')
    plt.xlabel('Palabras por mensaje')
    plt.ylabel('Promedio en segundos')
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    for i in range(len(x)):
        plt.text(x[i], y[i], f"{x[i]:.0f}", fontsize=10, va='top', rotation=-20, ha='left')
    plt.savefig("graficos/ajuste_minimos_cuadrados.png")
        
    plt.show()

    # Error de ajuste
    y_pred_cuadratico = a2 * x**2 + a1 * x + a0
    errores_cuadratico = np.abs(y - y_pred_cuadratico)
    error_cuadratico_total = np.sum(np.power(errores_cuadratico, 2))

    y_pred_cubico = b3 * x**3 + b2 * x**2 + b1 * x + b0
    errores_cubico = np.abs(y - y_pred_cubico)
    error_cubico_total = np.sum(np.power(errores_cubico, 2))

    orden = np.argsort(x)
    x_ordenado = x[orden]
    errores_cuadratico_ordenados = errores_cuadratico[orden]
    errores_cubico_ordenados = errores_cubico[orden]


    plt.figure(figsize=(8, 6))
    plt.scatter(x_ordenado, errores_cuadratico_ordenados, color='blue')
    plt.scatter(x_ordenado, errores_cubico_ordenados, color='green')
    plt.plot(x_ordenado, errores_cuadratico_ordenados, color='blue', label='Error de ajuste cuadrático')
    plt.plot(x_ordenado, errores_cubico_ordenados, color='green', label='Error de ajuste cúbico')
    plt.title(f'Error de ajuste cuadrático: {error_cuadratico_total}secs²\nError de ajuste cúbico: {error_cubico_total}secs²') 
    plt.xlabel('Palabras por mensaje')
    plt.ylabel('Error absoluto (segundos²)')
    plt.grid(True)
    plt.xscale("log")
    plt.legend()
    for i in range(len(x_ordenado)):
        plt.text(x_ordenado[i], errores_cuadratico_ordenados[i], f"{x_ordenado[i]:.0f}", fontsize=8, va='bottom', rotation=5, ha='left')
        plt.text(x_ordenado[i], errores_cubico_ordenados[i], f"{x_ordenado[i]:.0f}", fontsize=8, va='bottom', rotation=5, ha='left')
    plt.savefig("graficos/error_ajuste.png")
    plt.show()

    print("El error cuadrático total del ajuste es: ", error_cuadratico_total )
    print("El error cúbico total del ajuste es: ", error_cubico_total )


def main():
    ini = time.time()
    diccionario=generar_test_volumen()
    for cantidad in CANTIDADES_ENTRADA:
        generar_cadenas(diccionario, cantidad)

    promedios=ejecutar_pruebas_volumen()
    print(promedios)

    fin = time.time()

    print("\n")
    print(f"Tiempo total de ejecución sin graficar: {fin-ini} segundos")    
    print("\n")

    generar_graficos_y_error(promedios)
    
if __name__ == "__main__":
    main()