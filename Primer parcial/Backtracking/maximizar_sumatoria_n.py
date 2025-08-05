def max_sumatoria_n(lista, n):
    solucion=[]
    max_sumatoria_n_bt(lista,n,[],0,solucion)
    return solucion

def max_sumatoria_n_bt(lista,n,parcial,indice,solucion):
    if sum(parcial)==n:
        solucion.clear()
        solucion.extend(parcial)
        return 
    if sum(parcial)<n and sum(parcial)>sum(solucion):
        solucion.clear()
        solucion.extend(parcial)
    if indice==len(lista):
        return 
    if es_compatible(lista,n,parcial,indice):
        parcial.append(lista[indice])
        max_sumatoria_n_bt(lista,n,parcial,indice+1,solucion)
        parcial.pop()
    return max_sumatoria_n_bt(lista,n,parcial,indice+1,solucion)

def es_compatible(lista,n,parcial,i):
    suma=sum(parcial)
    if suma+lista[i]<=n:
        return True
    return False