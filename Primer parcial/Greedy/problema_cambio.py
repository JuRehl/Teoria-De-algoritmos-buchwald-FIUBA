def cambio(monedas, monto):
    monedasOrdenadas=sorted(monedas, reverse=True)
    montoConteo=0
    result=[]
    while montoConteo<monto:
        for moneda in monedasOrdenadas:
            if montoConteo+moneda<=monto:
                result.append(moneda)
                montoConteo+=moneda
                break
    return result