def numeros_posibles(k, n): #OPT(k,n)= sum(OPT(vi,n-1))
    vecinos = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8]
    }
    dp=[[1]*(n+1) for _ in range(10)]
    for i in range(2,n+1):
        for j in range(10):
            dp[j][i]=sum(dp[v][i-1] for v in vecinos[j])
    return dp[k][n]