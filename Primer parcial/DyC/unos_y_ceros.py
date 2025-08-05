def indice_primer_cero(arr):
    indice=_inidce_primer_cero(arr,0,len(arr)-1)
    if indice>=len(arr) or arr[indice]!=0:
        return -1
    return indice
    
def _inidce_primer_cero(arr,inicio,fin):
    if inicio==fin:
        return inicio
    mitad=(inicio+fin)//2
    if arr[mitad]==1:
        return _inidce_primer_cero(arr,mitad+1,fin)
    return _inidce_primer_cero(arr,inicio,mitad)