from grafo import Grafo
"""Parcial del 24/06/2024 1er recu"""
from math import isqrt
#Ejercicio 2
"""Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
es completo. Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy."""

def viajante(grafo,v):
    visitados=set([v])
    actual=v
    result=[v]
    while len(visitados)<len(grafo.obtener_vertices()):
        adyacentes=grafo.adyacentes(actual)
        no_visitados=[w for w in adyacentes if w not in visitados]
        siguiente=min(no_visitados, key=lambda x:grafo.peso_arista(actual,x))
        result.append(siguiente)
        visitados.add(siguiente)
        actual=siguiente
    result.append(v)
    return result

#Ejercicio 4
"""Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de bn en tiempo O(log n). Justificar
adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia.
Por ejemplo, que a h · ak = a h+k"""

def potencia(b,n):
    if n==0:
        return 1
    if n==1:
        return b
    mitad=n//2
    pot_mitad=potencia(b,mitad)
    imparidad=b
    if n%2==0:
        imparidad=1
    return pot_mitad*pot_mitad*imparidad

#Ejercicio 5
"""Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
utilizando programación dinámica. Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es
fácil tentarse a dar una cota más alta de lo correcto). Implementar un algoritmo que permita reconstruir la solución.
Aclaración: siempre es posible escribir a n como suma de n términos de la forma 12, por lo que siempre existe solución.
Sin embargo, la expresión 10 = 32 + 12 es una manera más económica de escribirlo para n = 10, pues sólo tiene dos términos."""

def suma_cuadrados(num):
    dp=[0]*(num+1)
    for i in range(1,num+1):
        minimo=i #usar i terminos de i el peor caso
        for j in range(1,isqrt(i)+1):
            pot=j*j
            if 1+dp[i-pot]<minimo:
                minimo=1+dp[i-pot]
        dp[i]=minimo
    return dp[num]

# #Ejercicio 3 (inventado by nerea osea yo)
# def crear_grafo(invitados):
#     grafo=Grafo()
#     for inv1,inv2 in invitados:
#         grafo.agregar_vertice(inv1)
#         grafo.agregar_vertice(inv2)
#         if not grafo.estan_unidos(inv1,inv2):
#             grafo.agregar_arista(inv1,inv2)
#     return grafo

# def cumpleanios_Coty(invitados, n, k):
#     grafo=crear_grafo(invitados)

# def cumpleanios_coty_bt(grafo, vertices, v,mejor_sol, sol_parcial,k):
#     if len(sol_parcial)==k:
#         mejor_sol.clear()
#         mejor_sol.append(sol_parcial.copy())
#         return True
#     if v==len(vertices):
#         return False
#     ver=vertices[v]
#     if es_compatible(grafo,ver,sol_parcial):
#         sol_parcial.add(ver)
#         if cumpleanios_coty_bt(grafo,vertices,v+1,mejor_sol,sol_parcial,k):
#             return True
#         sol_parcial.remove(ver)
#     return cumpleanios_coty_bt(grafo,vertices,v+1,mejor_sol,sol_parcial)

# def es_compatible(grafo,vertice,sol_p):
#     for ady in grafo.adyacentes(vertice):
#         if ady in sol_p:
#             return False
#     return True

"""Parcial 08/07/2024 segundo recu"""
#Ejercicio 1
"""Definimos a un grafo ordenado como un grafo dirigido con vértices v1, · · · , vn en el que todos los vértices, salvo vn
tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
decir, las aristas tienen la forma (vi, vj ) con i < j). Implementar un algoritmo de programación dinámica que dado
un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál es la longitud del camino más
largo. Dar la ecuación de recurrencia correspondiente. Dar también el algoritmo de recontrucción de la solución. Indicar
y justificar la complejidad del algoritmo implementado. Se pone a continuación un ejemplo de un grafo ordenado."""

def camino_mas_largo(grafo, vertices): #OPT(vi)= 1 + max OPT(vj)
    opt=[0]*(len(vertices))
    predecesor=[-1]*(len(vertices))
    for i in range(1,len(vertices)):
        for j in range(i):
            if grafo.estan_unidos(vertices[j],vertices[i]):
                if opt[i]<1+opt[j]:
                    opt[i]=1+opt[j]
                    predecesor[i]=j
    return reconstruir(vertices,opt,predecesor)

def reconstruir(vertices,opt,predecesor):
    n=len(vertices)
    indice=0
    for i in range(n):
        if opt[i]>opt[indice]:
            indice=i
    result=[]
    while indice>-1:
        result.append(vertices[indice])
        indice=predecesor[indice]
    result.reverse()
    return result        

#Ejercicio 3
"""Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo."""

def max_independent_set(grafo):
    ver=grafo.obtener_vertices()
    puestos=set()
    bloqueados=set()
    for v in ver:
        if v not in bloqueados:
            puestos.add(v)
            for ady in grafo.adyacentes(v):
                bloqueados.add(ady)
    return list(puestos)

"""Parcial 04-11-2024"""
#Ejercicio 1
"""Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
máxima y cuyo peso no exceda el valor de W."""

def mochila(elementos,w,k): #los elementos vienen como (peso,valor)
    resultado=[]
    mejor_valor=[0]
    mochila_bt(elementos,0,w,k,[],0,0,resultado,mejor_valor)
    return resultado
def mochila_bt(elementos, indice, w,k,sol_p,peso_actual,valor_actual,sol,mejor_valor):
    if peso_actual>w:
        return
    if len(sol_p)+(len(elementos)-indice)<k:
        return 
    if peso_actual<=w and len(sol_p)>=k:
        if valor_actual>mejor_valor[0]:
            sol.clear()
            sol.extend(sol_p)
            mejor_valor[0]=valor_actual
    if indice==len(elementos):
        return
    peso,valor=elementos[indice]
    sol_p.append(elementos[indice])
    mochila_bt(elementos,indice+1,w,k,sol_p,peso_actual+peso,valor_actual+valor,sol,mejor_valor)
    sol_p.pop()
    mochila_bt(elementos,indice+1,w,k,sol_p,peso_actual,valor_actual,sol,mejor_valor)

#Ejercicio 3
"""Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es la de maximizar la ganancia dada por p[k] − p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. Indicar y
justificar la complejidad del algoritmo implementado."""

def compra_venta(p):
    mejores_compras=obtener_mejor_compra(p)
    dp=[0]*len(p)
    for i in range(1,len(p)):
        mejor=max(p[i]-mejores_compras[i],dp[i-1])
        dp[i]=mejor
    return reconstruccion(dp,p)
def reconstruccion(dp,p):
    n=len(dp)-1
    venta=0
    while n>0:
        if dp[n]>dp[n-1]:
            venta=n
            break
        else:
            n-=1
    i=venta
    compra=venta
    while i>=0:
        if p[i]<=p[compra]:
            compra=i
        i-=1
    return compra,venta
def obtener_mejor_compra(p):
    dp=[0]*len(p)
    dp[0]=p[0]
    for i in range(1,len(p)):
        mejor=min(dp[i-1],p[i])
        dp[i]=mejor
    return dp

#Ejercicio 5 (by facu)
"""Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. Indicar y justificar adecuadamente la
complejidad del algoritmo implementado. Es probable que la complejidad de ambas soluciones no quede igual, no te
estreses por ello."""

def compra_venta(p):
    dia_compra, dia_venta, _ = dyc_compra_venta(p, 0, len(p) - 1)
    if dia_venta < dia_compra or p[dia_venta] - p[dia_compra] < 0:
        return 0, 0
    return dia_compra, dia_venta

def dyc_compra_venta(p, inicio, fin):
    if inicio >= fin:
        return inicio, inicio, 0
    medio = (inicio + fin) // 2
    izq, izqv, gizq = dyc_compra_venta(p, inicio, medio - 1)
    der, derv, gder = dyc_compra_venta(p, medio + 1, fin)
    minimo = p[inicio]
    dia_compra = inicio
    for i in range(inicio, medio + 1):
        if p[i] < minimo:
            minimo = p[i]
            dia_compra = i
        
    maximo = p[medio]
    dia_venta = medio
    for i in range(medio, fin + 1):
        if p[i] > maximo:
            maximo = p[i]
            dia_venta = i
        
    ganancia = maximo - minimo

    if gizq >= gder and gizq >= ganancia:
        return izq, izqv, gizq
    if gizq <= gder and gder >= ganancia:
        return der, derv, gder
    return dia_compra, dia_venta, ganancia

"""05/12/2024"""
#Ejercicio 2
"""Tati empezó a trabajar en un laboratorio químico, donde trabaja con compuestos que se vaporizan o subliman muy rápidamente, por lo que suelen estar almacenados en congeladores. ¿El problema? Su predecesora, Nerea, tenía un
único trabajo y lo hizo mal: en vez de almacenar todos los compuestos en un único congelador, guardó cada compuesto en un congelador por separado.La empresa no puede sostener un costo tan elevado, y deben deshacerse de todos los congeladores (salvo 1). Esto se
resuelve tan simple como pasar todos los compuestos a un único congelador, pero desde el momento que uno de estos se abre, se empieza a perder contenido de los compuestos que lleva dentro porque se vuelven gas, y desean minimizar las
pérdidas que esto produzca. Lo que se puede hacer es, en una unidad de tiempo, abrir dos congeladores A y B, y mover todo lo que haya en el congelador A al B. Se perderá en el medio el equivalente de lo que pierde cada componente por
unidad de tiempo (dato conocido para cada uno). Se puede seleccionar cualquier par de congeladores para hacer lo antes mencionado. Ejemplo: si tengo el congelador A con el compuesto c1 que pierde 5 por unidad de tiempo, y el
congelador B con el compuesto c2 que pierde 3 por unidad de tiempo, mover lo del congelado A al B nos implica una pérdida de 5 + 3 = 8. Si ahora movemos lo que hay en el congelador B al congelador C (que tiene los componentes c3,
c4 y c5 con pérdidas de 7, 4 y 1 respectivamente), el costo de ese movimiento será 5 + 3 + 7 + 4 + 1 = 20, lo cual se suma, obviamente, a cualquier otra pérdida anterior antes incurrida. Implementar un algoritmo greedy que obtenga el mínimo de pérdida que se puede lograr para terminar con un único
congelador. A fines del parcial no es necesario indicar cómo es este proceso, sólo el valor final. Indicar y justificar la complejidad del algoritmo. Justificar por qué el algoritmo implementado es, en efecto, un algoritmo greedy. ¿Es el
algoritmo implementado óptimo? Si es, dar una breve explicación, si no lo es dar un contraejemplo."""

def unir_congeladores(congeladores):
    perdida=0
    perdidas = [sum(congelador) for congelador in congeladores]
    
    while len(perdidas)>1:
        min1=min(perdidas)
        perdidas.remove(min1)
        min2=min(perdidas)
        perdidas.remove(min2)
        
        total=min1+min2
        perdida+=total
        perdidas.append(total)
        
    return perdidas

#Ejercicio 4
"""Implementar un algoritmo que, por programación dinámica, resuelva el problema de la mochila con una variante:
ahora se puede poner una cantidad ilimitada de un mismo elemento (es decir, se puede repetir), siempre y cuando
aún haya lugar. Por ejemplo, si yo tengo un elemento de tamaño 3 y una mochila de tamaño 10, yo podría guardar
3 veces dicho elemento, si así lo quisiera (también menos cantidad). Escribir y describir la ecuación de recurrencia
de la solución, y la complejidad del algoritmo implementado. Implementar o explicar (la que prefieran) cómo sería el
algoritmo de reconstrucción de la solución, indicando su complejidad."""

def mochila_repeticion(elementos,w): #OPT(i,n)=max(OPT(i-1,n),OPT(i,n-pesoi)+valori)
    n=len(elementos)
    dp=[[0]*(w+1) for _ in range(n+1)]
    for i in range(1,n+1):
        peso,valor=elementos[i-1]
        for j in range(w+1):
            if peso>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-peso]+valor)
    return dp
def reconstruir(elementos, W, dp):
    result = []
    i, j = len(elementos), W
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1  # no usaste el elemento, bajás de fila, antes bajaba siempre 
        else:
            result.append(elementos[i-1])
            j -= elementos[i-1][0]  
            # NO bajas i acá, porque podés seguir usando el mismo elemento
    result.reverse()
    return result

"""19/12/2024"""
#Ejercicio 1
"""Imaginá que estamos organizando un torneo de guardias en un castillo. El castillo tiene un suelo dividido en una
cuadrícula de tamaño n x m, y cada celda puede estar ocupada por un guardia o estar vacía. Los guardias tienen la
habilidad de vigilar todas las celdas adyacentes a su posición, incluidas las diagonales, es decir, pueden ver las celdas
vecinas que están justo al lado, arriba, abajo, a la izquierda, a la derecha o en las esquinas.
Se nos pide colocar la mayor cantidad posible de guardias en el castillo sin que ninguno pueda vigilar a otro. Esto
significa que no podemos colocar dos guardias en celdas adyacentes, ya que estarían vigilándose mutuamente.
Implementar un algoritmo greedy que permita colocar el mayor número posible de guardias en el castillo sin que se
vigilen entre sí. Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo
greedy. El algorimto, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo."""

def castillo(castillo):
    filas=len(castillo)
    columnas=len(castillo[0])
    for i in range(filas):
        for j in range(columnas):
            if castillo[i][j]==0: #si la pos es libre
                if i>0 and castillo[i-1][j]!=0: #arriba
                    continue
                if i<filas-1 and castillo[i+1][j]!=0: #abajo
                    continue
                if j>0 and castillo[i][j-1]!=0:#izquierda
                    continue
                if j<columnas-1 and castillo[i][j+1]!=0: #derecha
                    continue
                if i>0 and j>0 and castillo[i-1][j-1]!=0: #diag arriba izq
                    continue
                if i<filas-1 and j>0 and castillo[i+1][j-1]!=0: #diag abajo izq
                    continue
                if i>0 and j<columnas-1 and castillo[i-1][j+1]!=0: #diag arriba der
                    continue
                if i<filas-1 and j<columnas-1 and castillo[i+1][j+1]: #diag abajo der
                    continue
                castillo[i][j]=1
    return castillo

#Ejercicio 2
"""Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar
cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada
moneda, sino una cantidad específica (y esto hace que pueda no haber solución). Suponer que la función a invocar
es cambio(n, monedas, cantidad_x_monedas), donde n sea el valor a devolver en cambio, monedas sea una lista
ordenada de los valores de las monedas, y cantidad_x_monedas un diccionario."""

def cambio(n,monedas, cantidad_x_monedas):
    sol=[]
    cambio_bt(n,monedas,cantidad_x_monedas,[],0,sol)
    return sol
def cambio_bt(n,monedas,cantidad_x_monedas, sol_p, suma,sol):
    if suma==n:
        if not sol or len(sol_p) < len(sol): 
            sol.clear()
            sol.extend(sol_p)
        return
    for moneda in monedas:
        if suma + moneda > n:
            continue
        if cantidad_x_monedas[moneda] == 0:
            continue
        if sol and len(sol_p) >= len(sol):
            continue
        sol_p.append(moneda)
        cantidad_x_monedas[moneda] -= 1 
        cambio_bt(n, monedas, cantidad_x_monedas, sol_p, suma + moneda, sol)  
        sol_p.pop()  
        cantidad_x_monedas[moneda] += 1

#Ejercicio 5
"""Dado un Grafo dirigido, acíclico y pesado, y dos vértices s y t, implementar un algoritmo que, por programación
dinámica, permita encontrar el camino de peso máximo. Indicar y justificar la complejidad del algoritmo implementado.
Escribir y describir la ecuación de recurrencia de la solución, y la complejidad del algoritmo implementado. Implementar
el algoritmo de reconstrucción de la solución, indicando su complejidad."""
def camino_mas_largo(grafo,s,t): #dp[v] = max(dp[u] + peso(u, v)) para todos los u adyacentes a v
    vertices=grafo.obtener_vertices()
    dp=[0]*len(vertices)
    e={v:[] for v in vertices}
    for ver in range(len(vertices)):
        for ady in grafo.adyacentes(vertices[ver]):
            e[ady].append(ver)
    dp[s]=0 #el origen
    for i in range(len(dp)):
        if vertices[i]==s:
            continue
        ver_actual=vertices[i]
        entradas=e[ver_actual]
        dp[i] = max(grafo.peso_arista(vertices[entradas[j]], ver_actual) + dp[entradas[j]] for j in range(len(entradas)))
    return recons(grafo,s,t,dp,vertices)
def recons(grafo,s,t,dp,vertices):
    result=[]
    actual=t
    while actual!=s:
        result.append(actual)
        for ver in grafo.adyacentes(vertices[actual]):
            if dp[actual]==grafo.peso_arista(ver,vertices[actual])+dp[ver]:
                actual=ver
                break
    result.append(s)
    result.reverse()
    return result


"""10/02/2025"""
#Ejercicio 1
"""Dada una expresión representada por una cadena con aperturas y cierres de paréntesis, es sencillo implementar un
algoritmo que, utilizando una pila, determine si la expresión se encuentra balanceada, o no (esto es un algoritmo sencillo
de la materia anterior). Por ejemplo, la secuencia ()(), se encuentra balanceada, así como (()) también lo está, pero
((), no lo está, ni )()(. Implementar un algoritmo greedy que reciba una cadena y determine el largo del prefijo
balanceado más largo (es decir, el largo de la subsecuencia balanceada más larga que sí o sí comienza en el inicio de
la cadena). Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo greedy.
El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.Ejemplo: para ()())(())()((), la respuesta es 4."""

def cant_subsecuencia_balanceada(cadena):
    abierto=0
    cerrado=0
    longitud=0

    for caracter in cadena:
        if caracter=="(":
            abierto+=1
        elif caracter==")":
            cerrado+=1
        if abierto==cerrado:
            longitud=max(longitud,abierto+cerrado)
        elif cerrado>abierto:
            break
    return longitud

#Ejercicio 2
"""Resolver el problema anterior, pero esta vez para encontrar el largo de la subsecuencia balanceada más larga de
una expresión (en este caso, no necesariamente comenzando en el inicio). Para esto, utilizar programación dinámica. La
solución a este problema no dista mucho al planteo de la parte 2 del TP. Escribir y describir la ecuación de recurrencia
de la solución, e indicar y justificar la complejidad del algoritmo implementado.Para el ejemplo anterior, la respuesta es 6 (comenzando en la posición 5)."""

#cadena[i] == ')' y cadena[i-1] == '(' --> opt[i]=opt[i−2]+2
#cadena[i] == ')' y abierto '('en la posición i - opt[i-1] - 1 --> opt[i]=opt[i−1]+opt[i−opt[i−1]−2]+2
#sino opt[i]=0
def balanceados(cadena): 
    n=len(cadena)
    dp=[0]*n
    maximo=0
    for i in range(1,n):
        if cadena[i]==")":
            if cadena[i-1]=="(":
                if i<2:
                    dp[i]=2
                else:
                    dp[i]=dp[i-2]+2
            elif cadena[i-dp[i-1]-1]=="(" and i-dp[i-1]-1>=0:
                dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
            maximo=max(maximo,dp[i])
    return maximo

#Ejercicio 3
"""Dado un arreglo de enteros ordenado, un elemento y un valor entero k, implementar una función que, usando división
y conquista, encuentre los k valores del arreglo más cercanos al elemento en cuestión (que bien podría estar en el
arreglo, o no). La complejidad de la función implementada debe ser menor a O(n), suponiendo que k < n. Justificar
adecuadamente la complejidad del algoritmo implementado."""

def elementos_cercanos(arr,elemento,k):#O(logn + k)
    indice=elementos_cercanos_dyc(arr,elemento,k,0,len(arr)-1) #O(log n)
    return expandir(arr,indice,k)#O(k)
def elementos_cercanos_dyc(arr,elemento,k,ini,fin):
    if ini==fin:
        return ini
    medio=(ini+fin)//2
    if arr[medio]==elemento:
        return medio
    if arr[medio]>elemento:
        return elementos_cercanos_dyc(arr,elemento,k,ini,medio-1)
    return elementos_cercanos_dyc(arr,elemento,k,medio+1,fin)
def expandir(arr,medio,k):
    izq=medio-1
    der=medio+1
    result=[arr[medio]]
    while len(result)<k:
        if izq<=0:
            result.append(arr[der])
            der-=1
        elif der>=len(arr):
            result.append(arr[izq])
            izq-=1
        else:
            if abs(arr[izq] - arr[medio]) <= abs(arr[der] - arr[medio]):
                result.append(arr[izq])
                izq -= 1
            else:
                result.append(arr[der])
                der += 1
    return result

def main():
    # grafo = Grafo(es_dirigido=True,vertices_init=["A","B","C","D","E"])
    # grafo.agregar_arista("A", "B", 1)
    # grafo.agregar_arista("A", "D", 1)
    # grafo.agregar_arista("B", "D", 1)
    # grafo.agregar_arista("B", "E", 1)
    # grafo.agregar_arista("C", "D", 1)
    # grafo.agregar_arista("D", "E", 1)
    # camino = camino_mas_largo(grafo,["A","B","C","D","E"])
    # #print(f"Longitud del camino más largo: {longitud}")
    # print(f"Camino más largo: {camino}")

    # congeladores = [[5],  [2], [7,4,1] ]
    # num= unir_congeladores(congeladores)
    # print(num)

    # monedas = [1, 2, 5]
    # cantidad_x_monedas = {1: 2, 2: 1, 5: 1}
    # n = 15
    # print(cambio(n, monedas, cantidad_x_monedas))

    subsec="()())(())()(()"
    print(cant_subsecuencia_balanceada(subsec))

if __name__ == "__main__":
    main()