import sys
import auxiliares as aux

def main():
    diccionario = aux.cargar_diccionario(sys.argv[1])
    mensajesDesencriptados = aux.analizar_texto(sys.stdin, diccionario)
    aux.imprimir_mensajes(mensajesDesencriptados)

if __name__=="__main__":
    main()
