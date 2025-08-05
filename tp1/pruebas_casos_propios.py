import random
from pathlib import Path
import subprocess

#Test timestamps del sospechoso dispersos
def generar_test_es_distribuidos():
    sospechosos=[]
    transacciones=[]
    cantidad = 200
    base=1000
    for i in range(cantidad):
        num=base+i*500
        timestamp=num+random.randint(-5,5)
        error=random.randint(1,5)
        sospechosos.append(num)
        transacciones.append((timestamp,error))

    sospechosos.sort()
    with open("pruebas_propias/prueba_timestamp_distribuido.txt", "w")  as file:
        file.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        file.write(f"{str(cantidad)}\n")
        for t in transacciones:
            file.write(f"{t[0]},{t[1]}\n")
        for s in sospechosos:
            file.write(f"{str(s)}\n")

#Test timestamp del sospechoso en un rango pequeño
def generar_test_concentrados():
    generar_archivo_pruebas("pruebas_propias/prueba_timestamp_concentrados.txt",200,1000,1020,1,5)

#Test muchas transacciones repetidas
def generar_test_repetidas():
    random.seed(0)
    with open("pruebas_propias/prueba_transacciones_repetidas.txt", 'w') as archivo:
        archivo.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        archivo.write(str(200) + "\n")

        transacciones = []
        repeticiones = 0.8

        for i in range(200):
            if i > 0 and random.random() < repeticiones:
                transaccion = random.choice(transacciones)
            else:
                tiempo = random.randint(600, 700)
                error = random.randint(0, 10)
                transaccion = (tiempo, error)
            transacciones.append(transaccion)
            archivo.write(f"{transaccion[0]},{transaccion[1]}\n")

        sospechosos = [t[0] + random.randint(-t[1], t[1]) for t in transacciones]
        sospechosos.sort()
        for sospechoso in sospechosos:
            archivo.write(f"{sospechoso}\n")
    

#Test timestamps de transacciones únicas
def generar_test_unicas():
    random.seed(0)
    with open("pruebas_propias/prueba_transacciones_unicas.txt", 'w') as archivo:
        archivo.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        archivo.write(str(200) + "\n")

        tiempos = random.sample(range(1000, 5000), 200)
        transacciones = []

        for tiempo in tiempos:
            error = random.randint(0, 20)
            transacciones.append((tiempo, error))
            archivo.write(f"{tiempo},{error}\n")

        sospechosos = [tiempo + random.randint(-error, error) for tiempo, error in transacciones]
        sospechosos.sort()
        for sospechoso in sospechosos:
            archivo.write(f"{sospechoso}\n")



#Test valores de error pequeños
def generar_test_error_pequeño():
    generar_archivo_pruebas("pruebas_propias/prueba_error_pequeño.txt",200,350,450,1,5)

#Test valores de error amplios
def generar_test_error_amplio():
    generar_archivo_pruebas("pruebas_propias/prueba_error_amplio.txt",200,350,450,1,100)

def generar_archivo_pruebas(ruta,cantidad,rango_min,rango_max,error_min,error_max):
    with open(ruta,'w') as archivo:
        archivo.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        archivo.write(str(cantidad)+"\n")
        transacciones=[]
        for _ in range(cantidad):
            tiempo = random.randint(rango_min,rango_max)
            error = random.randint(error_min,error_max)
            archivo.write(f"{tiempo},{error}\n")
            transacciones.append((tiempo,error))
        sospechosos=[]
        for t in transacciones:
            sospechoso = random.randint(t[0]-t[1],t[0]+t[1])
            sospechosos.append(sospechoso)
        for sospechoso in sorted(sospechosos):
            archivo.write(f"{sospechoso}\n")

def correr_tests():
    ruta_carpeta = Path("pruebas_propias")
    archivos = [f"{ruta_carpeta}/{archivo.name}" for archivo in ruta_carpeta.iterdir() if archivo.is_file()]

    for archivo in archivos:
        comando = ["python3", "tp1.py", archivo]
        print(f"Ejecutando: {' '.join(comando)}")
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print(f"Salida:\n{resultado.stdout}")

def main():
    generar_test_es_distribuidos()
    generar_test_concentrados()
    generar_test_repetidas()
    generar_test_unicas()
    generar_test_error_pequeño()
    generar_test_error_amplio()

    correr_tests()

if __name__ == "__main__":
    main()