def scheduling(charlas): #OPT(i)=max(OPT[i-1],OPT(p(i))+V(i))
    if not charlas:
        return []
    charlas.sort(key=lambda x: x[1])
    n=len(charlas)
    p=[]
    for j in range(n):
        pj=-1
        for i in range(j-1,-1,-1):
            if charlas[i][1]<=charlas[j][0]:
                pj=i
                break
        p.append(pj)
    sche=[0]*(n+1)
    for j in range(1,n+1):
        sche[j]=max(charlas[j-1][2]+sche[p[j-1]+1],sche[j-1])
    return reconstruir(n,charlas,sche,p)

def reconstruir(n,charlas,sche,p):
    result=[]
    j=n
    while j>0:
        if charlas[j - 1][2] + sche[p[j - 1] + 1] > sche[j - 1]:
            result.append(charlas[j - 1])
            j = p[j - 1] + 1
        else:
            j -= 1
    result.reverse()
    return result
