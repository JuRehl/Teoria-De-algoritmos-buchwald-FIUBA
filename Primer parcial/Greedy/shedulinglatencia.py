def minimizar_latencia(L_deadline, T_tareas):
    tareas_ordenadas = sorted(zip(L_deadline, T_tareas)) 
    result=[]
    tiempo=0
    for deadline, duracion in tareas_ordenadas:
        fin=tiempo+duracion
        latencia=max(0,fin-deadline)
        result.append((duracion,latencia))
        tiempo=fin
    return result