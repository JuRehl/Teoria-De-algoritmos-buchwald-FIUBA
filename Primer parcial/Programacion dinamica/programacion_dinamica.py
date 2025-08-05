def pd(productos, W, P):
    n = len(productos)
    opt = [[[0] * (P+1) for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        valor, precio, peso = productos[i-1]
        for w in range(W+1):
            for p in range(P+1):
                if peso > w or precio > p:
                    opt[i][w][p] = opt[i-1][w][p]
                else:
                    opt[i][w][p] = max(opt[i-1][w][p], opt[i-1][w-peso][p-precio] + valor)
    return reconstruir(productos, W, P, opt)

def reconstruir(elementos, W, P, opt):
    n = len(elementos)
    j = W
    k = P
    resultado = []

    for i in range(n, 0, -1):
        if opt[i][j][k] != opt[i - 1][j][k]:
            resultado.append(elementos[i - 1])  
            j -= elementos[i - 1][2]
            k -= elementos[i-1][1]

    resultado.reverse()
    return resultado

productos = [
    (10, 4, 5),
    (400, 10, 4),
    (30, 5, 6),
    (50, 10, 10)
]

W = 10
P = 10 
print(pd(productos, W, P))

def calcular_seguro_minimo(etapas, costos):
    E = len(etapas)  # Cantidad de etapas
    # opt[i][j] = costo mínimo para llegar a la ciudad j en la etapa i
    opt = []
    # padre[i][j] = índice del nodo en etapa i-1 desde donde se llegó a ciudad j en etapa i
    padre = []
    opt.append([0])      # costo 0 para Ezeiza
    padre.append([None]) # no tiene padre
    for i in range(1, E):
        opt_i = []
        padre_i = []
        for j in range(len(etapas[i])):  # para cada ciudad u en etapa i
            mejor_costo = float('inf')
            mejor_padre = None
            u = etapas[i][j]
            for k in range(len(etapas[i-1])):  # para cada ciudad v en etapa i-1
                v = etapas[i-1][k]
                costo_arista = costos[i-1][v].get(u, float('inf'))
                costo_total = opt[i-1][k] + costo_arista
                if costo_total < mejor_costo:
                    mejor_costo = costo_total
                    mejor_padre = k

            opt_i.append(mejor_costo)
            padre_i.append(mejor_padre)

        opt.append(opt_i)
        padre.append(padre_i)
    ultima_etapa = opt[-1]
    indice_final = min(range(len(ultima_etapa)), key=lambda j: ultima_etapa[j])
    costo_total = ultima_etapa[indice_final]
    ruta = []
    etapa = E - 1
    indice = indice_final
    while etapa >= 0:
        ruta.append(etapas[etapa][indice])
        indice = padre[etapa][indice]
        etapa -= 1
    ruta.reverse()
    return costo_total, ruta


# Ejemplo de uso

etapas = [
    ['Ezeiza'],
    ['Villegas', 'Bolivar', 'Azul'],
    ['Santa Rosa', 'Olavarria'],
    ['Neuquen'],
    ['Bariloche']
]

costos = [
    {'Ezeiza': {'Villegas': 57, 'Bolivar': 82, 'Azul': 39}},
    {'Villegas': {'Santa Rosa': 90}, 'Bolivar': {'Santa Rosa': 120}, 'Azul': {'Olavarria': 60}},
    {'Santa Rosa': {'Neuquen': 70}, 'Olavarria': {'Neuquen': 80}},
    {'Neuquen': {'Bariloche': 150}}
]

costo, ruta = calcular_seguro_minimo(etapas, costos)
print("Costo mínimo de seguro:", costo)
print("Ruta:", " → ".join(ruta))

def stock_productos(productos, K):
    #Opt(i) = max(opt(i), opt(i-peso) + precio)
    opt = [0] * (len(productos) + 1)
    #opt=[[0]*(k+1) for _ in range(len(productos)+1) ]
    opt[0] = sum(p[0] for p in productos) #Caso base: arranco con al menos 1 producto de esos
    for i in range(1, len(productos) + 1):
        peso, precio = productos[i]
        for k in range(K  + 1):
            if peso <= k:
                opt[i] = max(opt[i], opt[i - peso] + precio) 
    return opt
def reconstruccion(opt, productos):
    resultado = []
    n = len(productos) + 1
    while n > 0:
        if opt[n] != opt[n-1]:
            resultado.append(productos[n-1])
            n -= productos[n-1][0]
        else:
            n -= 1
    return resultado[::-1]

def max_precio_con_todos(productos, K):
    n = len(productos)
    
    # Paso 1: Verificar si es posible incluir al menos uno de cada producto
    peso_minimo = sum(p[0] for p in productos)
    if peso_minimo > K:
        return -1  # No hay solución
    
    # Paso 2: Incluir obligatoriamente 1 unidad de cada producto
    precio_base = sum(p[1] for p in productos)
    peso_restante = K - peso_minimo
    
    # Paso 3: Resolver problema de mochila ilimitada con el peso restante
    dp = [0] * (peso_restante + 1)
    
    for peso, precio in productos:
        for k in range(peso, peso_restante + 1):
            dp[k] = max(dp[k], dp[k - peso] + precio)
    
    return precio_base + dp[peso_restante]

def menor_costo_seguro(rutas, inicio, fin, max_distancia=400):
    # Inicializar el costo mínimo para cada ciudad
    n = len(rutas)
    dp = [float('inf')] * n
    dp[inicio] = 0  # Costo para llegar al inicio es 0
    # Iterar sobre cada ciudad
    for i in range(n):
        for j in range(n):
            if i != j and rutas[i][j][0] <= max_distancia:  # Si hay una ruta y está dentro de la distancia
                costo_seguro = rutas[i][j][1]
                dp[j] = min(dp[j], dp[i] + costo_seguro)
    return dp[fin] if dp[fin] != float('inf') else -1 

def costo_minimo(origen, destino, rutas, costos):
    memo = {}
    
    def dp(ciudad):
        if ciudad == destino:
            return 0
        if ciudad in memo:
            return memo[ciudad]
        
        min_costo = float('inf')
        for vecina, distancia in rutas.get(ciudad, []):
            if distancia <= 400:
                costo_total = costos[vecina] + dp(vecina)
                min_costo = min(min_costo, costo_total)
        
        memo[ciudad] = min_costo
        return min_costo

    return dp(origen)

def trabajos_estres(trabajos_bajo, trabajos_alto, n):
    # Caso base: si no hay semanas, retornar 0
    if n == 0:
        return 0
    
    # Inicializar el arreglo de DP
    dp = [0] * (n + 1)
    
    # Semana 1: podemos elegir bajo estrés o alto estrés (sin restricción previa)
    dp[1] = max(trabajos_bajo[0], trabajos_alto[0])
    
    for i in range(2, n + 1):
        # Opción 1: Elegir trabajo de bajo estrés en la semana i
        # Puede venir de cualquier estado anterior (i-1)
        opcion_bajo = dp[i-1] + trabajos_bajo[i-1]
        
        # Opción 2: Elegir trabajo de alto estrés en la semana i
        # Requiere que en la semana i-1 no se haya hecho nada (i-2)
        opcion_alto = (dp[i-2] if i >= 2 else 0) + trabajos_alto[i-1]
        
        # Opción 3: No hacer nada en la semana i (útil para semanas futuras)
        opcion_nada = dp[i-1]
        
        # Tomar la mejor opción
        dp[i] = max(opcion_bajo, opcion_alto, opcion_nada)
    
    return dp[n]

def trabajos_estres(trabajos_bajo, trabajos_alto, n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    decision = [0] * (n + 1)  # Arreglo para almacenar decisiones
    if trabajos_bajo[0] > trabajos_alto[0]:
        dp[1] = trabajos_bajo[0]
        decision[1] = 1  # 1 significa "bajo estrés"
    else:
        dp[1] = trabajos_alto[0]
        decision[1] = 2  # 2 significa "alto estrés"
    for i in range(2, n + 1):
        # Opción 1: Elegir trabajo de bajo estrés en la semana i
        opcion_bajo = dp[i-1] + trabajos_bajo[i-1]
        opcion_alto = (dp[i-2] if i >= 2 else 0) + trabajos_alto[i-1]
        opcion_nada = dp[i-1]
        if opcion_bajo >= opcion_alto and opcion_bajo >= opcion_nada:
            dp[i] = opcion_bajo
            decision[i] = 1  # 1 significa "bajo estrés"
        elif opcion_alto >= opcion_bajo and opcion_alto >= opcion_nada:
            dp[i] = opcion_alto
            decision[i] = 2  # 2 significa "alto estrés"
        else:
            dp[i] = opcion_nada
            decision[i] = 0  # 0 significa "ninguno"
    plan = []
    i = n
    while i > 0:
        if decision[i] == 1:
            plan.append(f"bajo estrés semana {i}")
            i -= 1
        elif decision[i] == 2:
            plan.append(f"alto estrés semana {i}")
            i -= 1  # Saltar la semana anterior
            plan.append(f"no hago nada en la semana {i}")
            i -= 1
        else:
            plan.append("ninguno")
            i -= 1
    plan.reverse()  # Invertir el plan para que esté en orden cronológico
    return dp[n], plan

trabajos_bajo = [10, 10, 10, 10]
trabajos_alto = [5, 50, 5, 100]
n = 4
costo_maximo, plan_optimo = trabajos_estres(trabajos_bajo, trabajos_alto, n)
print(f"Costo máximo: {costo_maximo}")
print("Plan óptimo:", plan_optimo)

# Tarea = (t_i, d_i)
def max_schedulable_subset(tareas):
    n = len(tareas)
    tareas.sort(key=lambda x: x[1]) 
    finish = [0] * n
    for i in range(n):
        if i == 0:
            finish[i] = tareas[i][0]  # arranca en 0
        else:
            finish[i] = max(finish[i-1], 0) + tareas[i][0]
    dp = [0] * n
    prev = [-1] * n  # para reconstruir la solución
    for i in range(n):
        if i == 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]
            prev[i] = i-1
        start_time = 0
        if i > 0:
            start_time = finish[i-1]
        finish_i = start_time + tareas[i][0]
        if finish_i <= tareas[i][1]:  # si puede cumplir deadline
            j = -1
            for k in range(i-1, -1, -1):
                if finish[k] <= start_time:
                    j = k
                    break
            if j == -1:
                candidate = 1
            else:
                candidate = dp[j] + 1
            if candidate > dp[i]:
                dp[i] = candidate
                prev[i] = j
    i = dp.index(max(dp))
    resultado = []
    while i != -1:
        prev_i = prev[i]
        if dp[i] != dp[prev_i]:
            resultado.append(i)
        i = prev_i
    resultado.reverse()
    return max(dp), [tareas[i] for i in resultado]


def longitud_balanceada_maxima(s):
    n = len(s)
    dp = [0] * n
    maximo = 0
    
    for i in range(1, n):
        if s[i] == ')':
            j = i - 1 - dp[i-1]
            if j >= 0 and s[j] == '(':
                dp[i] = dp[i-1] + 2
                if j - 1 >= 0:
                    dp[i] += dp[j-1]
                maximo = max(maximo, dp[i])
    return maximo