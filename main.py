from search_algorithms import bfs, dfs, Nodo

def main():
    estado_final = (1, 0, 1, 0, 0, 0, 2, 0, 2)
    estado_inicial = (2, 0, 2, 0, 0, 0, 1, 0, 1)

    #Menú principal
    print("Este programa encuentra la solución al 4 knights puzzle")
    print("El estado inicial del juego es: ")
    (Nodo(estado_inicial, None, 0)).imprimir_nodo()
    print("\n¿Qué algoritmo desea correr? Escriba:")
    print("\t\"bfs\" para correr Breadth First Search")
    print("\t\"dfs\" para correr Depth First Search")
    print("\tCualquier otra cosa para terminar el programa.")
    algoritmo = input("Su elección: ")

    #Selección de algoritmo
    if algoritmo == "bfs" or algoritmo == "BFS":
        nodos_camino = bfs(estado_inicial, estado_final)

    elif algoritmo == "dfs" or algoritmo == "DFS":
        print("\n¿Establecer un límite de profundidad?")
        print("Establezca un numero para el limite")
        profundidad_max = int(input("Profundidad: "))
        nodos_camino = dfs(estado_inicial, estado_final, profundidad_max)

    else:
        return 0

    #Se imprime el camino si existe y si el usuario lo desea.
    if nodos_camino:
        print("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = (input("¿Desea imprimir dicho camino? s/n: "))

        if imprimir_camino == "s" or imprimir_camino == "S":
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, 0)).imprimir_nodo()

            for nodo in nodos_camino:
                print("")
                print("")
                nodo.imprimir_nodo()
    else:
        print("\nNo se encontró un camino con las condiciones dadas.")


if __name__ == "__main__":
    main()
