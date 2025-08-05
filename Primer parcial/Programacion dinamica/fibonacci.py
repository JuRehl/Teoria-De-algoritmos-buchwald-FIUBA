def fibonacci(n): #F(i)=F(i-1)+F(j-i)
    if n==0:
        return 1
    if n==1:
        return 1
    anterior=0
    actual=1
    for i in range(1,n+1):
        nuevo=actual+anterior
        anterior=actual
        actual=nuevo
    return actual