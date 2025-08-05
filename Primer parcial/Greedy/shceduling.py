def charlas(horarios):
    ordenarFin = sorted(horarios, key=lambda charla: charla[1])
    resultado = []
    for charla in ordenarFin:
        if len(resultado) == 0 or not hay_interseccion(resultado[-1], charla):
            resultado.append(charla)
    return resultado

def hay_interseccion(charla1, charla2):
    return charla2[0] < charla1[1]