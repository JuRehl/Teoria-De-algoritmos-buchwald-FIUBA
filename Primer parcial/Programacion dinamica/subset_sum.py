#opt(n,v)=max(opt(n-1,v),opt(n-1,v-vi,vi))
def subset_sum(elementos, v):
    dp=[[0]*(v+1) for _ in range(len(elementos)+1)] #asi tomo todo
    for i in range(1,len(elementos)+1):
        vi=elementos[i-1]
        for j in range(1,v+1):
            if vi>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-vi]+vi)
    return reconstruir(elementos,v,dp)

def reconstruir(elementos,v,dp):
    result=[]
    i,j=len(elementos),v
    for r in range(i,0,-1):
        if dp[r][j]!=dp[r-1][j]:
            result.append(elementos[r-1])
            j-=elementos[r-1]
    result.reverse()
    return result