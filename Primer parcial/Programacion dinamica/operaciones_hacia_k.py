MAS="mas1"
POR="por2"
def operaciones(k): #OPT(k) = min(OPT(k -1), OPT(k //2) si k es par, sino k) + 1(operacion)
    if k==0:
        return []
    dp=[0]*(k+1)
    prev=[0]*(k+1)
    op=['']*(k+1)
    for i in range(1,k+1):
        dp[i]=dp[i-1]+1
        prev[i]=i-1
        op[i]=MAS
        if i%2==0 and dp[i//2]+1<dp[i]:
            dp[i]=dp[i//2]+1
            prev[i]=i//2
            op[i]=POR
    return reconstruir(k,op,prev)

def reconstruir(k,op,prev):
    operaciones=[]
    actual=k
    while actual>0:
        operaciones.append(op[actual])
        actual=prev[actual]
    operaciones.reverse()
    return operaciones

# def operaciones(k):
#     if k == 0:
#         return []

#     opt = [0] * (k + 1)

#     for i in range(1, k + 1):
#         if i % 2 == 0:
#             mejor_opcion = min(opt[i - 1], opt[i // 2])
#         else:
#             mejor_opcion = min(opt[i - 1], k)
        
#         opt[i] = mejor_opcion + 1

#     return reconstruir_operaciones(opt, k)

# def reconstruir_operaciones(opt, k):
#     i = k
#     resultado = []

#     while i > 0:
#         if i % 2 == 0 and opt[i] == opt[i//2] + 1:
#             resultado.append("por2")
#             i //= 2
#         else:
#             resultado.append("mas1")
#             i -= 1

#     resultado.reverse()
#     return resultado