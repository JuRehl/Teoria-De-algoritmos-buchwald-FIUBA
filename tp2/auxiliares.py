NO_ES_MENSAJE = "No es un mensaje"

def cargar_diccionario(ruta_archivo):
    palabras = set()
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            palabra = linea.strip()
            if palabra:
                palabras.add(palabra)
    return palabras

def analizar_texto(texto, diccionario):
    mensajes = []
    for linea in texto:
        linea = linea.strip()
        mensaje = es_mensaje_valido(linea,diccionario)
        mensajes.append(mensaje)
    return mensajes        

def es_mensaje_valido(cadena, diccionario):
    n = len(cadena)
    dp = [False] * (n + 1)
    dp[0] = True
    prev=[-1] *(n + 1)
    max_len = max(len(palabra) for palabra in diccionario)

    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and cadena[j:i] in diccionario:
                dp[i] = True
                prev[i]=j
                break
    
    return reconstruccion_palabras(prev, cadena) if dp[-1] else None

def reconstruccion_palabras(prev, cadena):
    palabras = []
    i = len(cadena)
    while i > 0:
        j = prev[i]
        palabras.append(cadena[j:i])
        i = j
    palabras.reverse()
    return palabras

def imprimir_mensajes(mensajes):
    for mensaje in mensajes:
        if mensaje is None:
            print(NO_ES_MENSAJE)
        else:
            mensaje = " ".join(mensaje)
            print(mensaje)
