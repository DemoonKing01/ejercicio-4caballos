#Clase que define un nodo en el 4 knights puzzle.
class Nodo:
    def __init__(self, estado, padre, profundidad):
        self.estado = estado
        self.padre = padre
        self.profundidad = profundidad

    #Método para mover las piezas en direcciones posibles.
    def mover(self, sucesores, actual, op1, op2):
        estado = list(self.estado)

        def nuevo_estado(estado, actual, nuevo):
            estado[nuevo] = estado[actual]
            estado[actual] = 0
            sucesores.append(Nodo(tuple(estado), self, self.profundidad + 1))

        if estado[op1] == 0:
            nuevo_estado(estado, actual, op1)

        if estado[op2] == 0:
            nuevo_estado(estado, actual, op2)

    #Método que encuentra y regresa todos los nodos sucesores del nodo actual.
    def encontrar_sucesores(self):
        sucesores = []

        for i in range(len(self.estado)):
            if(self.estado[i] != 0):
                if i == 0:
                    self.mover(sucesores, i, 5, 7)
                elif i == 1:
                    self.mover(sucesores, i, 6, 8)
                elif i == 2:
                    self.mover(sucesores, i, 3, 7)
                elif i == 3:
                    self.mover(sucesores, i, 2, 8)
                elif i == 5:
                    self.mover(sucesores, i, 0, 6)
                elif i == 6:
                    self.mover(sucesores, i, 1, 5)
                elif i == 7:
                    self.mover(sucesores, i, 0, 2)
                elif i == 8:
                    self.mover(sucesores, i, 1, 3)

        sucesores = [nodo for nodo in sucesores if nodo.estado != None]
        return sucesores

    #Método que encuentra el camino desde el nodo inicial hasta el actual.
    def encontrar_camino(self):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    #Método que imprime ordenadamente el estado (piezas) de un nodo.
    def imprimir_nodo(self):
        print("| %i | %i | %i |" % (self.estado[0], self.estado[1], self.estado[2]))
        print("| %i | %i | %i |" % (self.estado[3], self.estado[4], self.estado[5]))
        print("| %i | %i | %i |" % (self.estado[6], self.estado[7], self.estado[8]))

