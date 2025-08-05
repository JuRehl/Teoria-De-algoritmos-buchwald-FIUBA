def contar_inversiones(A, B):
    if len(B)==1:
        return 0
    mitad=len(B)//2
    izq=B[:mitad]
    der=B[mitad:]
    inv_izq=contar_inversiones(A,izq)
    inv_der=contar_inversiones(A,der)
    B,invB= _conteo(A,izq,der)
    return invB+inv_izq+inv_der


def _conteo(A,izq,der):
    result=[]
    i,j=0,0
    inversiones=0

    while i<len(izq) and j<len(der):
        if izq[i]<der[j]:
            result.append(izq[i])
            i+=1
        else:
            result.append(der[j])
            j+=1
            inversiones += len(izq) - i
    
    result.extend(izq[i:])
    result.extend(der[j:])

    return result,inversiones