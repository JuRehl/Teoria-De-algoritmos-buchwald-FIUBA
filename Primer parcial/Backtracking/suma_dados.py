def sumatoria_dados(n, s):
    return sumatoria_dados_bt(s,n,[],[])

def sumatoria_dados_bt(s, cant_faltan,parcial,resultado):
    if sum(parcial)==s and cant_faltan==0:
        resultado.append(parcial.copy())
        return resultado
    if sum(parcial)+cant_faltan>s:
        return resultado
    if sum(parcial)+cant_faltan*6<s:
        return resultado
    for num in range(1,7):
        parcial.append(num)
        resultado=sumatoria_dados_bt(s,cant_faltan-1,parcial,resultado)
        parcial.pop()
    return resultado