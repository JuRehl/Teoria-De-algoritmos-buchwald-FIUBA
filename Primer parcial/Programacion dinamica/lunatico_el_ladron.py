#OPT[n]=0 si n==0, OPT[n]=casa0 si n==1, OPT[n]= max(OPT[n−1],ganancias[n−1]+OPT[n−2])si n>=2 
# sumado para este caso: OPT[n]=max(casoA[0,n−2],casoB[1,n−1])
def lunatico(ganancias):
    n=len(ganancias)
    if n==0:
        return []
    if n == 1:
        return [0]
    casoA=iterar(0,n-1,ganancias)
    casoB=iterar(1,n,ganancias)
    if casoA[n-2]>=casoB[n-1]:
        return reconstruir(casoA,ganancias,0,n-2)
    return reconstruir(casoB,ganancias,1,n-1)

def iterar(inicio,fin,ganancias):
    caso=[0]*(len(ganancias))
    caso[inicio]=ganancias[inicio]
    if fin-inicio>=2:
        caso[inicio + 1] = max(ganancias[inicio], ganancias[inicio + 1])
        for i in range(inicio + 2, fin):
            caso[i] = max(caso[i - 1], ganancias[i] + caso[i - 2])
    return caso

def reconstruir(caso,ganancias,inicio,fin):
    result=[]
    n=fin
    while n>=inicio:
        if n == inicio:
            result.append(n)
            break
        if caso[n - 1] >= (caso[n - 2] + ganancias[n]):
            n -= 1
        else:
            result.append(n)
            n -= 2
    result.reverse()
    return result