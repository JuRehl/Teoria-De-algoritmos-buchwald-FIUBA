import os
import subprocess
import time
from pathlib import Path
import random
from matplotlib import pyplot as plt
import numpy as np

VECES = 20
RUTA_CARPETA = Path("pruebas_mediciones")
ARCHIVOS = ["10.txt", "50.txt", "100.txt", "500.txt", "1000.txt", "5000.txt", "10000.txt", "25000.txt", "50000.txt", "75000.txt", "100000.txt", "250000.txt", "500000.txt", "750000.txt", "1000000.txt"]
RANGO_MIN = 1
ERROR_MIN = 1

def generar_test_volumen():
    for archivo in ARCHIVOS:
        cantidad = int(archivo.split(".")[0])
        if cantidad < 1000:
            rango_max = 1000
            error_max = 100
        elif cantidad < 10000:
            rango_max = 10000
            error_max = 1000
        elif cantidad < 100000:
            rango_max = 100000
            error_max = 10000
        else:
            rango_max = 1000000
            error_max = 100000
        ruta = f"{RUTA_CARPETA}/{archivo}"
        with open(ruta,'w') as archivo:
            archivo.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
            archivo.write(str(cantidad)+"\n")
            transacciones=[]
            for _ in range(cantidad):
                tiempo = random.randint(RANGO_MIN,rango_max)
                error = random.randint(ERROR_MIN,error_max)
                archivo.write(f"{tiempo},{error}\n")
                transacciones.append((tiempo,error))
            sospechosos=[]
            for t in transacciones:
                sospechoso = random.randint(t[0]-t[1],t[0]+t[1])
                sospechosos.append(sospechoso)
            for sospechoso in sorted(sospechosos):
                archivo.write(f"{sospechoso}\n")

def ejecutar_pruebas_volumen():
    archivos = [f"{RUTA_CARPETA}/{archivo.name}" for archivo in RUTA_CARPETA.iterdir() if archivo.is_file()]
    promedios = {}
    for archivo in archivos:
        comando = ["python3", "tp1.py", archivo]
        total = 0
        for _ in range(VECES):
            start = time.time()
            resultado = subprocess.run(comando, capture_output=True, text=True)
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
        cantidad, _ = cantidad.split(".")
        valores_x.append(int(cantidad))
        valores_y.append(valor)

    x = np.array(valores_x)
    y = np.array(valores_y)
    x_ajustado = np.linspace(min(x), max(x), 200)

    # Ajuste cuadrático
    A_cuadratico = np.vstack([x**2, x, np.ones_like(x)]).T
    coef_cuadratico, _, _, _ = np.linalg.lstsq(A_cuadratico, y, rcond=None)
    a, b, c = coef_cuadratico
    y_ajustado_cuadratico = a * x_ajustado**2 + b * x_ajustado + c

    # Ajuste cúbico
    A_cubico = np.vstack([x**3, x**2, x, np.ones_like(x)]).T
    coef_cubico, _, _, _ = np.linalg.lstsq(A_cubico, y, rcond=None)
    a3, a2, a1, a0 = coef_cubico
    y_ajustado_cubico = a3 * x_ajustado**3 + a2 * x_ajustado**2 + a1 * x_ajustado + a0

    print(f"Función cuadrática ajustada: f(x) ≈ {a:.3e}x² + {b:.3e}x + {c:.3e}\n")
    print(f"Función cúbica ajustada: f(x) ≈ {a3:.3e}x³ + {a2:.3e}x² + {a1:.3e}x + {a0:.3e}\n")

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='red', label='Datos originales')
    plt.plot(x_ajustado, y_ajustado_cuadratico, color='blue', label='Ajuste cuadrático')
    plt.plot(x_ajustado, y_ajustado_cubico, color='green', label='Ajuste cúbico')
    plt.title(f'Ajuste cuadrático: f(x) ≈ {a:.3e}x² + {b:.3e}x + {c:.3e}\nAjuste cúbico: f(x) ≈ {a3:.3e}x³ + {a2:.3e}x² + {a1:.3e}x + {a0:.3e}')
    plt.xlabel('Cantidad de transferencias')
    plt.ylabel('Promedio en segundos')
    plt.legend()
    plt.grid(True)
    plt.xscale("log")
    for i in range(len(x)):
        plt.text(x[i] + 0.02, y[i] - 0.02, f"{x[i]:.0f}", fontsize=10, va='top', rotation=-20, ha='left')
    plt.savefig("graficos/ajuste_minimos_cuadrados.png")
        
    plt.show()

    # Error de ajuste
    y_pred_cuadratico = a * x**2 + b * x + c
    errores_cuadratico = np.abs(y - y_pred_cuadratico)
    error_cuadratico_total = np.sum(np.power(errores_cuadratico, 2))

    y_pred_cubico = a3 * x**3 + a2 * x**2 + a1 * x + a0
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
    plt.xlabel('Cantidad de transferencias')
    plt.ylabel('Error absoluto (segundos)')
    plt.grid(True)
    plt.xscale("log")
    plt.ylim(0, max(errores_cubico) * 1.1)
    plt.legend()
    for i in range(len(x_ordenado)):
        plt.text(x_ordenado[i], errores_cuadratico_ordenados[i], f"{x_ordenado[i]:.0f}", fontsize=8, va='bottom', rotation=5, ha='left')
        plt.text(x_ordenado[i], errores_cubico_ordenados[i], f"{x_ordenado[i]:.0f}", fontsize=8, va='bottom', rotation=5, ha='left')
    plt.savefig("graficos/error_ajuste.png")
    plt.show()

    print("El error cuadrático total del ajuste es: ", error_cuadratico_total )
    print("El error cúbico total del ajuste es: ", error_cubico_total )

def main():
    ini=time.time()
    generar_test_volumen()
    promedios = ejecutar_pruebas_volumen()
    for archivo,promedio in promedios.items():
        print(f"{archivo.split('/')[1]}: {promedio} segundos")
    fin=time.time()

    print("\n")
    print(f"Tiempo total de ejecución sin graficar: {fin-ini} segundos")    
    print("\n")

    generar_graficos_y_error(promedios)
    
if __name__ == "__main__":
    main()