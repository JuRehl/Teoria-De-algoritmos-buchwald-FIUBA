import math 

def precios_inflacion(R):
    ROrdenado=sorted(R,reverse=True)
    j=0
    result=0
    for i in range (len(ROrdenado)):
        result+=math.pow(ROrdenado[i],j+1)
        j+=1
    return result