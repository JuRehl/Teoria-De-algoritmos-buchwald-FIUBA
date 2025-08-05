def obtener_combinaciones(materias):
    combinaciones = []
    obtener_combinaciones_bt(materias,combinaciones,[],0)
    return combinaciones

def obtener_combinaciones_bt(materias,combinaciones, parcial,indice):
    if len(parcial)==len(materias):
        combinaciones.append(parcial.copy())
        return 
    for i in range(indice,len(materias)):
        for curso in materias[i]:
            if es_compatible(curso,parcial):
                parcial.append(curso)
                obtener_combinaciones_bt(materias,combinaciones,parcial,i+1)
                parcial.pop()

def es_compatible(curso, parcial):
    for materia in parcial:
        if not son_compatibles(materia,curso):
            return False
    return True

def son_compatibles(materia1,materia2):
    return True