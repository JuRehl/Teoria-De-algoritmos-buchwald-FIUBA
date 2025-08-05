def cajas(capacidad, libros):
    libros.sort(reverse=True)
    resultado = []
    caja = []

    for libro in libros:
        if sum(caja) + libro <= capacidad:
            caja.append(libro)
        else:
            resultado.append(caja)
            caja = [libro]

    if caja:
        resultado.append(caja)

    return resultado