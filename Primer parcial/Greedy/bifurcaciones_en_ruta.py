def bifurcaciones_con_patrulla(ciudades):
    ciudades_ord = sorted(ciudades, key=lambda x: x[1])
    patrullas = []
    i = 0
    n = len(ciudades_ord)
    while i < n:
        km_patrulla = ciudades_ord[i][1] + 50
        j = i
        while j < n and ciudades_ord[j][1] <= km_patrulla:
            j += 1

        patrullas.append(ciudades_ord[j-1])
        km_patrulla = ciudades_ord[j-1][1] + 50
        
        while i < n and ciudades_ord[i][1] <= km_patrulla:
            i += 1

    return patrullas