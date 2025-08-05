"""El problema del Independent Set se define como: dado un grafo no dirigido, obtener el máximo subconjunto de vértices del grafo tal 
que ningun par de vértices del subconjunto sea adyacente entre si. Dicho conjunto es un Independet Set. Definir el problema de decisión 
del Independent Set. Luego, implementar un verificador polinomial para este problema. ¿Cuál es la complejidad del verificador 
implementado? Justificar"""
#Complejidad O(n²) siendo n la cantidad de vertices en el grafo -> es polinomial por lo que cumple con np
def verificar_is(grafo,subconjunto,k):
    if len(subconjunto)<k:
        return False
    for i in range(len(subconjunto)):
        for j in range(i+1,len(subconjunto)):
            u,v=subconjunto[i],subconjunto[j]
            if grafo.estan_unidos(u,v):
                return False
    return True
