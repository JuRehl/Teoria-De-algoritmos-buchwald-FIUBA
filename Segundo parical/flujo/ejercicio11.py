from grafo import Grafo
from ejercicio2 import ford_fulkerson
"""Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca 
tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de 
asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela 
el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de prestamos. ¿Cuál es el orden temporal de la solución 
implementada?"""
#complejidad O 
def max_prestamos(grafo, alumnos, libros, deseos):
    red = Grafo()
    
    fuente = "S"
    sumidero = "T"
    
    # Agregar nodos
    red.agregar_nodo(fuente)
    red.agregar_nodo(sumidero)
    for alumno in alumnos:
        red.agregar_nodo(alumno)
        red.agregar_arista(fuente, alumno, 10)  # Puede pedir hasta 10 libros
    for libro in libros:
        red.agregar_nodo(libro)
        red.agregar_arista(libro, sumidero, 3)  # 3 copias por libro
    
    # Aristas alumno → libro deseado (capacidad 1)
    for alumno, lista_deseos in deseos.items():
        for libro in lista_deseos:
            red.agregar_arista(alumno, libro, 1)
    
    # Calcular flujo máximo
    return ford_fulkerson(red, fuente, sumidero)
