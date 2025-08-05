def elemento_desordenado(arr):
    return elemento_desordenado_rec(arr, 0, len(arr) -1)

def elemento_desordenado_rec(arr, izq, der):
    if der - izq == 1:#¿Estoy mirando exactamente dos elementos vecinos?
        if arr[izq] > arr[der]:
            return arr[izq]
        return -1

    mid = (izq + der)//2

    if arr[mid -1] > arr[mid]:
        return arr[mid -1]

    mitad_der = elemento_desordenado_rec(arr, mid, der)
    if mitad_der == -1:
        return elemento_desordenado_rec(arr, izq, mid)
    return mitad_der