import subprocess
from pathlib import Path
import random

CANTIDAD_DICC_GENERAL = 50
TAMAÑO_PALABRAS_GENERAL = float("+inf")
CANT_MENSAJES_GENERAL = 7
CANT_PALABRAS_MSJ = 13

def generar_test_volumen(cantidad_dict, tamaño_palabras_dict):
    with open("0_palabras_todas.txt", "r") as f:
        todas = set(line.strip() for line in f if line.strip())
    validas = [p for p in todas if len(p) <= tamaño_palabras_dict]
    seleccionadas = random.sample(validas, cantidad_dict)
    return seleccionadas

def generar_cadenas(diccionario, cant_palabras_mensaje,cant_msj):
    mensajes = []
    for _ in range(cant_msj):
        msj = "".join(random.choice(diccionario) for _ in range(cant_palabras_mensaje))
        mensajes.append(msj)
    return mensajes

def generar_archivo_pruebas(cantidad_dict, tamaño_palabras_dict, ruta_dict, cantidad_mensajes, cant_palabras_mensajes, ruta_mensajes):
    dicc = generar_test_volumen(cantidad_dict, tamaño_palabras_dict)
    
    Path(ruta_dict).parent.mkdir(exist_ok=True, parents=True)
    with open(ruta_dict, "w") as f:
        f.write("\n".join(dicc))
    
    msjs = generar_cadenas(dicc, cant_palabras_mensajes,cantidad_mensajes)
    
    Path(ruta_mensajes).parent.mkdir(exist_ok=True, parents=True)
    with open(ruta_mensajes, "w") as f:
        f.write("\n".join(msjs))

    return dicc, msjs
      
def diccionario_muchas_palabras():
    ruta_dict = "pruebas_propias/diccionarios/diccionario_dicc_muchas_palabras.txt"
    ruta_msj= "pruebas_propias/dicc_muchas_palabras.txt"
    generar_archivo_pruebas(1500, TAMAÑO_PALABRAS_GENERAL, ruta_dict, CANT_MENSAJES_GENERAL, CANT_PALABRAS_MSJ,ruta_msj)

def diccionario_pocas_palabras():
    ruta_dict = "pruebas_propias/diccionarios/diccionario_dicc_pocas_palabras.txt"
    ruta_msj= "pruebas_propias/dicc_pocas_palabras.txt"
    generar_archivo_pruebas(10, TAMAÑO_PALABRAS_GENERAL,ruta_dict, CANT_MENSAJES_GENERAL, CANT_PALABRAS_MSJ, ruta_msj)

def mensajes_corto():
    ruta_dict="pruebas_propias/diccionarios/diccionario_mensajes_corto.txt"
    ruta_msj="pruebas_propias/mensajes_corto.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL, TAMAÑO_PALABRAS_GENERAL, ruta_dict, CANT_MENSAJES_GENERAL, 3,ruta_msj)

def mensajes_largos():
    ruta_dict="pruebas_propias/diccionarios/diccionario_mensajes_largos.txt"
    ruta_msj="pruebas_propias/mensajes_largos.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL,TAMAÑO_PALABRAS_GENERAL,ruta_dict,CANT_MENSAJES_GENERAL,25,ruta_msj)

def palabras_dicc_largas():
    ruta_dict="pruebas_propias/diccionarios/diccionario_palabras_largas.txt"
    ruta_msj="pruebas_propias/palabras_largas.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL,TAMAÑO_PALABRAS_GENERAL,ruta_dict,CANT_MENSAJES_GENERAL,CANT_PALABRAS_MSJ,ruta_msj)

def palabras_dicc_cortas():
    ruta_dict="pruebas_propias/diccionarios/diccionario_palabras_cortas.txt"
    ruta_msj= "pruebas_propias/palabras_cortas.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL,4,ruta_dict,CANT_MENSAJES_GENERAL,CANT_PALABRAS_MSJ,ruta_msj)

def muchos_mensajes():
    ruta_dict="pruebas_propias/diccionarios/diccionario_cantidad_grande_mensajes.txt"
    ruta_msj="pruebas_propias/cantidad_grande_mensajes.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL,TAMAÑO_PALABRAS_GENERAL,ruta_dict,100,CANT_PALABRAS_MSJ,ruta_msj)

def pocos_mensajes():
    ruta_dict="pruebas_propias/diccionarios/diccionario_cantidad_pequeña_mensajes.txt"
    ruta_msj="pruebas_propias/cantidad_pequeña_mensajes.txt"
    generar_archivo_pruebas(CANTIDAD_DICC_GENERAL,TAMAÑO_PALABRAS_GENERAL,ruta_dict,2,CANT_PALABRAS_MSJ,ruta_msj)

def correr_tests():
    ruta_diccionarios = Path("pruebas_propias/diccionarios")
    ruta_entradas    = Path("pruebas_propias")

    entradas = {f.name: f for f in ruta_entradas.iterdir() if f.is_file()}

    for dicc in ruta_diccionarios.iterdir():
        if not dicc.is_file(): 
            continue
        sufijo = dicc.name.replace("diccionario_", "", 1)
        archivo_entrada = entradas[sufijo]
        comando = ["python3", "tp2.py", str(dicc)]
        print(f"Ejecutando: {' '.join(comando)} < {archivo_entrada.name}")
        resultado = subprocess.run(
            comando,
            stdin=archivo_entrada.open('r'),
            capture_output=True,
            text=True
        )
        print(resultado.stdout)
        

def main():
    diccionario_muchas_palabras()
    diccionario_pocas_palabras()
    mensajes_corto()
    mensajes_largos()
    palabras_dicc_cortas()
    palabras_dicc_largas()
    muchos_mensajes()
    pocos_mensajes()

    correr_tests()

if __name__ == "__main__":
    main()