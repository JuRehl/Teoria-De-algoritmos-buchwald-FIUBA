def sumatorias_n(lista, n):
    return sumatorias_n_bt(lista,n,[],[],0)

def sumatorias_n_bt(lista,n,solucion,parcial,indice):
    if sum(parcial)==n:
        solucion.append(parcial.copy())
        return solucion
    for i in range(indice,len(lista)):
        if es_compatible(lista,i,parcial,n):
            parcial.append(lista[i])
            solucion=sumatorias_n_bt(lista,n,solucion,parcial,i+1)
            parcial.pop()
    return solucion

def es_compatible(lista,indice,parcial,n):
    if sum(parcial)+ lista[indice]<=n:
        return True
    return False