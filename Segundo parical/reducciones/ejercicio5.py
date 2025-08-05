"""Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad. a. Dado un número por 
parámetro, si es la solución al problema de Búsqueda del máximo en un arreglo b. Dado un arreglo, si es la solución a tener el arreglo 
ordenado c. Dadas un arreglo de posiciones de Reinas, si es la solución de colocar al menos N-reinas en un tablero NxN"""

def busqueda_maximo(arreglo,numero): #O(n)
    for elem in arreglo:
        if elem>numero:
            return False
    return True

def arr_ordenado(arreglo): #O(n)
    for i in range(len(arreglo)-1):
        if arreglo[i]>arreglo[i+1]:
            return False
    return True

def nreinas(posiciones): #O(n²)
    for i in range(len(posiciones)):
        for j in range(i+1,len(posiciones)):
            if posiciones[i]==posiciones[j] or abs(posiciones[i]-posiciones[j])==abs(i-j):
                return False
    return True
