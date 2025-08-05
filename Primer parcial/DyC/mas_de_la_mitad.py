def mas_de_la_mitad(arr):
    if not arr:
        return False
    posible= _mas_de_la_mitad(arr,0,len(arr)-1)
    return posible[1]>len(arr)//2

def _mas_de_la_mitad(arr, ini,fin):
    if ini==fin:
        return arr[ini],1
    medio=(ini+fin)//2
    izq,contizq= _mas_de_la_mitad(arr, ini,medio)
    der,contder=_mas_de_la_mitad(arr,medio+1,fin)
    if izq==der:
        return izq, contder+contizq
    izqC=contador(arr,izq,ini,fin)
    derC=contador(arr,der,ini,fin)
    if izqC>derC:
        return izq,izqC
    return der,derC
    

def contador(arr, num,ini,fin):
    contador=0
    for i in range(ini,fin+1):
        if arr[i]==num:
            contador+=1
    return contador