# -*- coding: utf-8 -*-
"""
Created on Tue May 21 01:14:47 2024

@author: krismad10
"""
# 8!=40320
import itertools

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8},
    'B': {'A': 2, 'C': 9, 'D': 10, 'E': 11, 'F': 12, 'G': 13, 'H': 14},
    'C': {'A': 3, 'B': 9, 'D': 15, 'E': 16, 'F': 17, 'G': 18, 'H': 19},
    'D': {'A': 4, 'B': 10, 'C': 15, 'E': 20, 'F': 21, 'G': 22, 'H': 23},
    'E': {'A': 5, 'B': 11, 'C': 16, 'D': 20, 'F': 24, 'G': 25, 'H': 26},
    'F': {'A': 6, 'B': 12, 'C': 17, 'D': 21, 'E': 24, 'G': 27, 'H': 28},
    'G': {'A': 7, 'B': 13, 'C': 18, 'D': 22, 'E': 25, 'F': 27, 'H': 29},
    'H': {'A': 8, 'B': 14, 'C': 19, 'D': 23, 'E': 26, 'F': 28, 'G': 29}
}

# Obtener todos los nodos del grafo
nodos = list(grafo.keys())

# Generar todas las posibles permutaciones de los nodos
permutaciones = itertools.permutations(nodos)

# Mostrar todas las permutaciones (caminos posibles)
for perm in permutaciones:
    print(perm)
