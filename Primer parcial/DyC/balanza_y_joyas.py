#from balanza import *

def encontrar_joya(joyas):
    return encontrar_joya_dyc(joyas, 0)

def encontrar_joya_dyc(joyas, idx):
    if len(joyas) == 1:
        return idx
    
    mid = len(joyas) // 2

    resultado = 1#balanza(joyas[:mid], joyas[mid:mid*2])
    if resultado == 0:
        return encontrar_joya_dyc(joyas[mid*2:], idx + mid*2)
    elif resultado == 1:
        return encontrar_joya_dyc(joyas[:mid], idx)
    return encontrar_joya_dyc(joyas[mid:mid*2], idx + mid)