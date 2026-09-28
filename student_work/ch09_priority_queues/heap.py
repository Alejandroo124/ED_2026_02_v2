class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo = len(self.arreglo) -1
        hijo = self.arreglo[indice_hijo]
        indice_padre = indice_hijo // 2
        padre = self.arreglo[indice_padre]

        while hijo < padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = self.arreglo[indice_padre], self.arreglo[indice_hijo]
            indice_hijo = indice_padre
            indice_padre = indice_hijo // 2
            hijo = self.arreglo[indice_hijo]
            padre = self.arreglo[indice_padre]

        def remove_smallest(self):
            if len(self.arreglo) == 1:
                raise IndexError("El heap está vacío")

            menor = self.arreglo[1]
            ultimo = self.arreglo.pop()

            if len(self.arreglo) > 1:
                self.arreglo[1] = ultimo

                indice = 1

                while True:
                    hijo_izquierdo = indice * 2
                    hijo_derecho = indice * 2 + 1

                    if hijo_izquierdo >= len(self.arreglo):
                        break

                    menor_hijo = hijo_izquierdo

                    if (hijo_derecho < len(self.arreglo) and
                        self.arreglo[hijo_derecho] < self.arreglo[hijo_izquierdo]):
                        menor_hijo = hijo_derecho

                    if self.arreglo[indice] <= self.arreglo[menor_hijo]:
                        break

                    self.arreglo[indice], self.arreglo[menor_hijo] = (
                        self.arreglo[menor_hijo],
                        self.arreglo[indice]
                    )

                    indice = menor_hijo

            return menor

    def build_heap(self, lista):
        self.arreglo = [float('-inf')]

        for valor in lista:
            self.insert(valor)
