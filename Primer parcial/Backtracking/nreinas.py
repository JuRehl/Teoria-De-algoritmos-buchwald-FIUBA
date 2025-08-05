def nreinas(n):
    return nreinas_bt(n, [], 0)

def nreinas_bt(n, sol_parcial, fila):
    if fila == n:
        return sol_parcial
    for col in range(n):
        par = (fila, col)
        if es_compatible(sol_parcial, par):
            sol_parcial.append(par)
            solucion = nreinas_bt(n, sol_parcial, fila +1)
            if solucion:
                return solucion
            sol_parcial.pop()
    return []

def es_compatible(sol_parcial, par):
    x, y = par
    for (sx, sy) in sol_parcial:
        if sx == x or sy == y or abs(sx - x) == abs(sy - y):
            return False
    return True