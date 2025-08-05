def max_subarray(arr):
    if not arr:
        return []
    max_suma, inicio, fin = max_subarray_util(arr, 0, len(arr) - 1)
    return arr[inicio:fin + 1]
    
def suma_cruzada_maxima(arr, izquierda, medio, derecha):
    suma_izquierda = float('-inf')
    suma = 0
    inicio_izquierda = medio
    for i in range(medio, izquierda - 1, -1):
        suma += arr[i]
        if suma > suma_izquierda:
            suma_izquierda = suma
            inicio_izquierda = i
    suma_derecha = float('-inf')
    suma = 0
    fin_derecha = medio + 1
    for i in range(medio + 1, derecha + 1):
        suma += arr[i]
        if suma > suma_derecha:
            suma_derecha = suma
            fin_derecha = i
    return suma_izquierda + suma_derecha, inicio_izquierda, fin_derecha

def max_subarray_util(arr, izquierda, derecha):
    if izquierda == derecha:
        return arr[izquierda], izquierda, derecha
    medio = (izquierda + derecha) // 2
    max_izquierda, inicio_izquierda, fin_izquierda = max_subarray_util(arr, izquierda, medio)
    max_derecha, inicio_derecha, fin_derecha = max_subarray_util(arr, medio + 1, derecha)
    max_cruzada, inicio_cruzada, fin_cruzada = suma_cruzada_maxima(arr, izquierda, medio, derecha)

    if max_izquierda >= max_derecha and max_izquierda >= max_cruzada:
        return max_izquierda, inicio_izquierda, fin_izquierda
    elif max_derecha >= max_izquierda and max_derecha >= max_cruzada:
        return max_derecha, inicio_derecha, fin_derecha
    return max_cruzada, inicio_cruzada, fin_cruzada