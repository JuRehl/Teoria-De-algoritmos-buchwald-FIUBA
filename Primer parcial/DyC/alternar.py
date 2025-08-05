def alternar(arr):
    alteranar_rec(arr, 0)

def alteranar_rec(arr, iteracion):
    largo = len(arr)
    if iteracion == largo:
        return
    if iteracion + largo // 2 < largo:
        a = arr[iteracion]
        b = arr[iteracion+largo//2]
        alteranar_rec(arr, iteracion+1)
        arr[iteracion*2] = a
        arr[iteracion*2+1] = b
