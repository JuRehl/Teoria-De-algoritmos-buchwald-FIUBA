#Ec-> C[monto]=1+min(para todo monto>=moneda,C[dinero-moneda])
def cambio(monedas, monto):
    if monto==0:
        return []
    cant=[0]*(monto+1)
    for i in range(1,monto+1):
        minimo=i
        for moneda in monedas:
            if moneda>i:
                continue
            cantidad=1+cant[i-moneda]
            if cantidad<minimo:
                minimo=cantidad
        cant[i]=minimo
    return reconstruir(monedas,monto,cant)

def reconstruir(monedas,monto,cant):
    result=[]
    while monto>0:
        for moneda in monedas:
            if moneda<=monto and cant[monto]==1+cant[monto-moneda]:
                result.append(moneda)
                monto-=moneda
                break
    return result