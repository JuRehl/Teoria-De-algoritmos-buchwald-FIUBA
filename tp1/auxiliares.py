MODO_LECTURA = "r"
class Robo:
    def __init__(self): 
        """
        Inicializa el objeto Robo con diccionario de transacciones, lista de transacciones, lista de sospechosos 
        y variable para las coincidencias.
        """
        self.dic_transacciones = {} 
        self.transacciones = []
        self.sospechoso = []
        self.matches = None
    """
    matchear(self)

    Ordena las transacciones por finalizacion del intervalo, luego empareja a los sospechosos con las transacciones 
    disponibles según un criterio de tiempo. Actualiza el diccionario de coincidencias 'matches' en el objeto actual
    y ajusta el contador de transacciones disponibles.
    Si no se encuentra una transacción adecuada para un sospechoso, establece 'matches' a None.
    """
    def matchear(self):
        self.transacciones.sort(key=lambda x: x[0] + x[1]) 
        
        matches = {}
        
        for transaccion_sospechoso in self.sospechoso:
            for transaccion in self.transacciones:
                momento, error = transaccion
                if momento + error < transaccion_sospechoso:
                    continue
                if momento - error > transaccion_sospechoso:
                    continue
                if self.dic_transacciones[transaccion] > 0:
                    match = (transaccion_sospechoso, transaccion)
                    matches[match] = matches.get(match, 0) + 1
                    self.dic_transacciones[transaccion] -= 1
                    break
            else: 
                matches = None
                
                break

        if matches:
            self.matches = matches
    """
    imprimir_rata(self)

    Imprime las transacciones asociadas a los sospechosos si hay coincidencias.Si no hay coincidencias, imprime que no
    es el sospecho.
    """
    def imprimir_rata(self):
        if self.matches is not None:
            for match in self.matches.keys():
                sospechoso, transaccion = match
                while self.matches[match] > 0:
                    self.matches[match] -= 1
                    print(f"{sospechoso} --> {transaccion[0]} ± {transaccion[1]}")
        else:
            print("No es el sospechoso correcto")

"""
    procesar_datos(ruta)

    Procesa un archivo de texto que contiene información sobre transacciones y sospechosos, y construye un objeto 
    de tipo Robo con estos datos.
    Parámetros: ruta->str(Ruta al archivo que contiene los datos.)
    Retorna: Robo(Objeto Robo con los datos cargados si el archivo está bien formateado). None(Si ocurre algún error 
    en el formato o no se puede abrir el archivo.)
"""
def procesar_datos(ruta):
    try:
        robo = Robo()
        with open(ruta, MODO_LECTURA) as archivo:
            next(archivo)
            cantidad = archivo.readline().strip()

            if cantidad.isdigit():
                cantidad = int(cantidad)
            else:
                return None

            for _ in range(cantidad):
                momento, error = archivo.readline().strip().split(",")
                if momento.isdigit() and error.isdigit():
                    transaccion = (int(momento), int(error))
                    robo.transacciones.append(transaccion)
                    robo.dic_transacciones[transaccion] = robo.dic_transacciones.get(transaccion, 0) + 1
                else:
                    return None
                
            for _ in range(cantidad):
                linea = archivo.readline().strip()
                if linea.isdigit():
                    robo.sospechoso.append(int(linea))
                else:
                    return None
                
        return robo
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

"""
    investigar(robo)

    Ejecuta el análisis del objeto Robo recibido, buscando coincidencias y mostrando el resultado.
    Parámetros: robo:Robo(Objeto previamente cargado con datos de transacciones y sospechosos)
    """
def investigar(robo: Robo):
    robo.matchear()
    robo.imprimir_rata()
