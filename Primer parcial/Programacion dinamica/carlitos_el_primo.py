# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P): #OPT(n,p)=max(OPT(n-1,p),OPT(n-1,p-ci)+gi)
    dp=[[0]*(P+1) for _ in range(len(c_publicitaria)+1)]

    for i in range(1,len(c_publicitaria)+1):
        ganancia, costo=c_publicitaria[i-1]
        for j in range(1,P+1):
            if costo>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-costo]+ganancia)
    return reconstruir(c_publicitaria,P,dp)

def reconstruir(c_publicitaria,P,dp):
    result=[]
    i,j=len(c_publicitaria),P
    for r in range(i,0,-1):
        if dp[r][j]!=dp[r-1][j]:
            result.append(c_publicitaria[r-1])
            j-=c_publicitaria[r-1][1]
    result.reverse()
    return result