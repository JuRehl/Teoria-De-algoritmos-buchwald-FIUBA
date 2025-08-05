import sys
import auxiliares
import time
import programacion_lineal
import louvain
import aproximacion

def main():
    ini=time.time()
    grafo=auxiliares.construir_grafo(sys.argv[1])
    k=int(sys.argv[2])
    # clusters, max_diametro = auxiliares.clustering(grafo,k)
    # clusters, max_diametro = programacion_lineal.clustering_pulp(grafo, k)
    # clusters, max_diametro = louvain.algoritmo_louvain_completo(grafo, k)
    clusters, max_diametro = aproximacion.aproximacion(grafo,k) # No calcula el maximo diámetro, siempre es None
    fin=time.time()
    print(clusters, max_diametro)
    print("Tiempo de ejecución:", fin - ini)

if __name__=="__main__":
    main()