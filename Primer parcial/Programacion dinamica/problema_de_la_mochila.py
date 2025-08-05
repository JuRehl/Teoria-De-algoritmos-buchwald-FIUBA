# cada elemento i de la forma (valor, peso)
def mochila(elementos, W): #OPT(n,w)=max(OPT[n-1,w],OPT[n-1,w-pi]+Vi)
    n=len(elementos)
    dp= [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        valor, peso=elementos[i-1]
        for j in range(W+1):
            if peso>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-peso]+valor)
    return reconstruir(elementos, W, dp)

def reconstruir(elementos, W, dp):
    result=[]
    i,j=len(elementos),W
    while i>0 and j>0:
        if dp[i][j]!=dp[i-1][j]:
            result.append(elementos[i-1])
            j-=elementos[i-1][1]
        i-=1
    result.reverse()
    return result