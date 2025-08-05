# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementosOrd=sorted(elementos, key=lambda x: x[0], reverse=True)
    result=[]
    pesoConteo=0
    for elemento in elementosOrd:
        if elemento[1]+pesoConteo<=W:
            result.append(elemento)
            pesoConteo+=elemento[1]
        if pesoConteo==W:
            break
    return result