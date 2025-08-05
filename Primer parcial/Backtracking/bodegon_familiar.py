def max_grupos_bodegon(P, W):
    result=[]
    max_grupos_bodegon_bt(P,W,[],0,result)
    return result

def max_grupos_bodegon_bt(P,W,parcial,indice,solucion):
    if sum(parcial)==W:
        solucion.clear()
        solucion.extend(parcial)
        return
    if sum(parcial)<W and sum(parcial)>sum(solucion):
        solucion.clear()
        solucion.extend(parcial)
    if indice==len(P):
        return 
    if es_compatible(P,W,parcial,indice):
        parcial.append(P[indice])
        max_grupos_bodegon_bt(P,W,parcial,indice+1,solucion)
        parcial.pop()
    return max_grupos_bodegon_bt(P,W,parcial,indice+1,solucion)

def es_compatible(P,W,parcial,indice):
    suma=sum(parcial)
    if suma+P[indice]<=W:
        return True
    return False