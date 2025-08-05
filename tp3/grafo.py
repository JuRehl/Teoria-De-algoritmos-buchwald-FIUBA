import random 

class Grafo:
    def __init__(self, es_dirigido, vertices = None):
        self.vertices={}
        if vertices is not None:
            for v in vertices:
                self.vertices[v] = {}
        self.es_dirigido=es_dirigido
    

    def agregar_vertice(self, vértice):
        if vértice not in self.vertices:
            self.vertices[vértice]={}        

    def agregar_arista(self,v,w,peso):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("Los vértices no están en el Grafo")
        if w in self.vertices[v] or v in self.vertices[w]:
            return
        self.vertices[v][w]=peso
        if not self.es_dirigido:
            self.vertices[w][v]=peso


    def borrar_vertice(self,v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no se encuentra en el Grafo")
        for ady in list(self.vertices[v].keys()):
            self.vertices[ady].pop(v)
        self.vertices.pop(v)
    

    def borrar_arista(self,v,w):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("No existen esos vértices en el Grafo")
        if w in self.vertices[v]:
            del self.vertices[v][w]
        if not self.es_dirigido and v in self.vertices[w]:
            del self.vertices[w][v] 


    def estan_unidos(self,v,w):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("No existen esos vértices en el Grafo")
        return w in self.vertices[v]
    

    def peso_arista(self,v,w):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("No existen esos vértices en el Grafo")
        return self.vertices[v][w]
    

    def obtener_vertices(self):
        return list(self.vertices.keys())
    

    def vertice_aleatorio(self):
        if self.vertices:
            return random.choice(self.obtener_vertices())
        return None
    

    def adyacentes(self,v):
        if v in self.vertices:
            return list(self.vertices[v].keys())
        raise ValueError("El vértice no esta en el Grafo")

    def __str__(self):
        resultado = []
        if self.es_dirigido:
            for v, ady in self.vertices.items():
                for w, peso in ady.items():
                    resultado.append(f"{v} -> {w} (peso: {peso})")
        else:
            visitados = set()
            for v, ady in self.vertices.items():
                for w, peso in ady.items():
                    if (w,v) not in visitados:
                        visitados.add((v,w))
                        resultado.append(f"{v} -- {w} (peso: {peso})")
        return "\n".join(resultado)
    
    def peso_total_aristas(self):
        total = 0
        for v in self.vertices:
            total += sum(self.vertices[v].values())
        return total if self.es_dirigido else total // 2
    
    def suma_pesos_adyacentes(self, v):
        return sum(self.vertices[v].values())

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, v):
        return v in self.vertices

    def __iter__(self):
        return iter(self.vertices)