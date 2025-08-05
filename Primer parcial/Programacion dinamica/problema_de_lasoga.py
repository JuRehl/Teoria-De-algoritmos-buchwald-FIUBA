# dp[n] = max( i * (n - i), i * dp[n - i] ) para todo 1 <= i < n
def problema_soga(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        max_prod = 0
        for j in range(1, i):  
            sin_cortar = j * (i - j)
            con_corte = j * dp[i - j]
            max_prod = max(max_prod, sin_cortar, con_corte)
        dp[i] = max_prod
    return dp[n]