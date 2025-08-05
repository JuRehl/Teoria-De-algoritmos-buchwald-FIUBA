def precios_deflacion(R):
    rOrd=sorted(R)
    result=0
    j=1
    for i in range(len(rOrd)):
        result+=rOrd[i]/j
        j*=2
    return result