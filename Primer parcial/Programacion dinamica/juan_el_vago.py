def juan_el_vago(trabajos): #OPT(i)=max(OPT[i-1],OPT[i-2]+V[i])
    # devolver un arreglo de los índices de días a trabajar
    if not trabajos:
        return []
    n=len(trabajos)
    G=[0]*(n)
    G[0]=trabajos[0]
    if n==1:
        return [0]
    G[1]=max(trabajos[0],trabajos[1])
    for i in range(2,n):
        G[i]=max(G[i-2]+trabajos[i],G[i-1])
    return reconstruir(G,trabajos)

def reconstruir(G,trabajos):
    result=[]
    d=len(G)-1
    while d>=0:
        opt_ayer=G[d-1] if d>0 else 0
        opt_anteayer=G[d-2] if d>1 else 0
        hoy=trabajos[d]
        if opt_anteayer+hoy>opt_ayer:
            result.append(d)
            d-=2
        else:
            d-=1
    result.reverse()
    return result