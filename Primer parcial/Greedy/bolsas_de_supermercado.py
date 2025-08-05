def bolsas(capacidad, productos):
    prodOrden=sorted(productos)
    resultado=[]
    while prodOrden:
        bolsa=[]
        peso_actual=0
        i=0
        while i<len(prodOrden):
            if peso_actual+prodOrden[i]<=capacidad:
                bolsa.append(prodOrden[i])
                peso_actual+=prodOrden[i]
                prodOrden.pop(i)
            else:
                break  
        resultado.append(bolsa)
    return resultado