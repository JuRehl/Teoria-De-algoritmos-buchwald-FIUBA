def bodegon_dinamico(P, W):
    n=len(P)
    dp=[[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        personas=P[i-1]
        for j in range(W+1):
            if personas>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-personas]+personas)
    return reconstruir(P,W,dp)

def reconstruir(P,W,dp):
    result=[]
    i,j=len(P),W
    while i>0 and j>0:
        if dp[i][j]!=dp[i-1][j]:
            grupo = P[i - 1]
            result.append(grupo)
            j -= grupo
        i-=1
    result.reverse()
    return result

#Ecuacion de recurrencia: OPT(n,W)--> max(OPT(n-1,W),OPT(n-1,W-pi)+pi)