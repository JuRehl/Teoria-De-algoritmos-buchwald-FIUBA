def escalones(n): #E(i)=E(i-1)+E(i-2)+E(i-3)
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    dp=[1]*(n+1)
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]
