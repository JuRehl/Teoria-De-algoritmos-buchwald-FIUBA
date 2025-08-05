import random 

class Grafo:
    def __init__(self,es_dirigido,vertices_init):
        self.diccionario_grafo={v: {} for v in vertices_init}
        self.es_dirigido=es_dirigido
    def agregar_vertice(self, vértice):
        if vértice in self.diccionario_grafo:
            raise ValueError("Ese vértice ya existe en el grafo")
        self.diccionario_grafo[vértice]={}
    def agregar_arista(self,v,w,peso):
        if v not in self.diccionario_grafo or w not in self.diccionario_grafo:
            raise ValueError("Los vértices no están en el grafo")
        self.diccionario_grafo[v][w]=peso
        if not self.es_dirigido:
            self.diccionario_grafo[w][v]=peso
    def borrar_vertice(self,v):
        if v not in self.diccionario_grafo:
            raise ValueError("El vértice no se encuentra en el diccionario")
        for ady in list(self.diccionario_grafo[v].keys()):
            self.diccionario_grafo[ady].pop(v)
        self.diccionario_grafo.pop(v)
    def borrar_arista(self,v,w):
        if v not in self.diccionario_grafo or w not in self.diccionario_grafo:
            raise ValueError("No existen esos vértices en el diccionario")
        if w in self.diccionario_grafo[v]:
            del self.diccionario_grafo[v][w]
        if not self.es_dirigido and v in self.diccionario_grafo[w]:
            del self.diccionario_grafo[w][v]
    def estan_unidos(self,v,w):
        if v not in self.diccionario_grafo or w not in self.diccionario_grafo:
            raise ValueError("No existen esos vértices en el diccionario")
        return w in self.diccionario_grafo[v]
    def peso_arista(self,v,w):
        if v not in self.diccionario_grafo or w not in self.diccionario_grafo:
            raise ValueError("No existen esos vértices en el diccionario")
        return self.diccionario_grafo[v][w]
    def obtener_vertices(self):
        return list(self.diccionario_grafo.keys())
    def vertice_aleatorio(self):
        if self.diccionario_grafo:
            return random.choice(self.obtener_vertices())
        return None
    def adyacentes(self,v):
        if v in self.diccionario_grafo:
            return list(self.diccionario_grafo[v].keys())
        raise ValueError("El vértice no esta en el grafo")
    def __str__(self):
        return str(self.diccionario_grafo)        