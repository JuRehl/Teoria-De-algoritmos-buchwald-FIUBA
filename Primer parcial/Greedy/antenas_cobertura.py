def cobertura(casas, R, K):
    if not casas:
        return []
    casasOrd=sorted(casas)
    result=[]
    minimo=casasOrd[0]
    min_antena = min(minimo + R, K)
    result.append(min_antena)
    for casa in casasOrd:
        if not (result[-1] - R <= casa <= result[-1] + R):
            min_antena = min(casa + R, K)
            result.append(min_antena)
    return result