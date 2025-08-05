# Trabajo Práctico 3: Comunidades NP-Completas

En este repositorio se encuentra el código fuente del **Trabajo Práctico 3** de la materia **75.29 Teoría de Algoritmos**, correspondiente al curso **Buchwald-Genender**.

## Autores
Barrasso Facundo, Nowenstein Mateo y Rehl Juana
 
## Contenido

Este trabajo práctico se enfoca en el estudio y resolución del **Problema de Clustering por Bajo Diámetro**, que consiste en particionar un grafo en clústeres minimizando el diámetro máximo dentro de cada comunidad. Para ello, el repositorio incluye:

- **Demostración de Complejidad**: Análisis formal y demostración de que el problema pertenece a la clase NP y es NP-Completo, incluyendo una reducción desde el problema de Separación en R Cliques.
- **Algoritmo Exacto por Backtracking**: Implementación de un algoritmo de backtracking para encontrar la solución óptima del problema en instancias de tamaño pequeño a mediano, con estrategias de poda para mejorar la eficiencia.
- **Modelado y Resolución por Programación Lineal**: Un modelo de programación lineal entera para la resolución óptima del problema, permitiendo la comparación de rendimiento con el algoritmo de backtracking.
- **Algoritmo Heurístico de Louvain**: Implementación del algoritmo de Louvain, una heurística basada en la maximización de la modularidad, para abordar el problema en grafos de gran escala donde las soluciones exactas no son computacionalmente viables.
- **Generación de Conjuntos de Prueba**: Scripts y datos para generar grafos con diversas topologías (estrellas, ciclos, cliques, grafos aleatorios de Erdős-Rényi y grafos con comunidades claras), utilizados para validar la correctitud y evaluar el rendimiento de los algoritmos.
- **Análisis Comparativo**: Herramientas y resultados para comparar la eficiencia y la calidad de las soluciones obtenidas por los diferentes enfoques (exactos vs. heurísticos).

## Requisitos

- Python 3.x  
- `matplotlib` (para visualización y generación de gráficos de rendimiento)  
- Un solver de Programación Lineal compatible (ej. **Gurobi**, **CPLEX**, **PuLP** con un solver como **GLPK/CBC**). La configuración específica del solver dependerá de la implementación particular.
-  `networkx`  

## Cómo ejecutar:

```bash
python3 tp3.py ruta_a_archivo/archivo.txt k
```
Para ejecutar los distintos algoritmos simplemente se pueden comentar y descomentar desde el main de  **tp3.py**. El k debe ser un entero positivo.

## Para generar los archivos para todas las pruebas:

```bash
python3 pruebas_propias.py
```

## Para generar los gráficos de rendimiento:
```bash
python3 graficar_test_variabilidad.py
```

## Instalación:

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install matplotlib

pip install pulp

pip install networkx
