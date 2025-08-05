def posicion_pico(v, ini, fin):
    if ini==fin:
        return fin
    medio=(ini+fin) // 2
    if v[medio]>v[medio-1] and v[medio]>v[medio+1]:
        return medio
    elif v[medio+1]>v[medio]:
        return posicion_pico(v,medio,fin)
    return posicion_pico(v, ini,medio)