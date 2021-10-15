from collections import deque
from node import Nodo

#Algoritmo Breadth First Search.
def bfs(inicial, meta):
    visitados = set()
    frontera = deque()
    frontera.append(Nodo(inicial, None, 0))

    while frontera:  # Mientras haya nodos por explorar:
        nodo = frontera.popleft()  # Se toma el primer nodo de la cola.

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
        else:
            continue

        if nodo.estado == meta:
            print("\n¡Se encontró la meta!")
            return nodo.encontrar_camino()
        else:
            frontera.extend(nodo.encontrar_sucesores())

#Algoritmo Depth First Search.
def dfs(inicial, meta, profundidad_max):
    visitados = set()
    frontera = deque()
    frontera.append(Nodo(inicial, None, 0))

    while frontera:  # Mientras haya nodos por explorar:
        nodo = frontera.pop()  # Se toma el primer nodo de la pila.

        if nodo.estado not in visitados:
            visitados.add(nodo.estado)
        else:
            continue

        if nodo.estado == meta:
            print("\n¡Se encontró la meta!")
            return nodo.encontrar_camino()
        else:
            if profundidad_max > 0:  # Si se estableció una búsqueda con profundidad limitada
                if nodo.profundidad < profundidad_max:
                    frontera.extend(nodo.encontrar_sucesores())
            else:
                frontera.extend(nodo.encontrar_sucesores())
