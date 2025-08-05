def parte_entera_raiz(n):
    return _parte_entera_raiz(n,0,n)

def _parte_entera_raiz(n, inicio, fin):
    if inicio>fin:
        return fin
    
    mitad=(inicio + fin)//2

    if mitad*mitad==n:
        return mitad
    elif mitad*mitad>n:
        return _parte_entera_raiz(n,inicio,mitad-1)
    else:
       return _parte_entera_raiz(n,mitad+1,fin)