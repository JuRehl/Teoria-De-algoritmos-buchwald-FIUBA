def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mitad=len(arr)//2
    izq=arr[:mitad]
    der=arr[mitad:]
    izq=merge_sort(izq)
    der=merge_sort(der)
    return _merge_sort(izq,der)

def _merge_sort(izq,der):
    resultado=[]
    i,j=0,0
    while i < len(izq) and j < len(der):
        if izq[i]<=der[j]:
            resultado.append(izq[i])
            i+=1
        else:
            resultado.append(der[j])
            j+=1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado