import matplotlib.pyplot as plt

class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen = False):
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

        if imagen:
            self._dibujar_heap()

    def remove_smallest(self,imagen = False):
        if len(self.arreglo) == 1:
            return None
        min = self.arreglo[1]
        ultimo = self.arreglo[-1]
        self.arreglo[-1] = min
        self.arreglo[1] = ultimo
        self.arreglo.pop()
        i = 1
        while i * 2 < len(self.arreglo):

            izquierdo = i * 2
            derecho = i * 2 + 1

            if derecho < len(self.arreglo):

                if self.arreglo[izquierdo] <= self.arreglo[derecho]:

                    if self.arreglo[i] > self.arreglo[izquierdo]:
                        self.arreglo[i], self.arreglo[izquierdo] = self.arreglo[izquierdo], self.arreglo[i]
                        i = izquierdo
                    else:
                        break

                else:

                    if self.arreglo[i] > self.arreglo[derecho]:
                        self.arreglo[i], self.arreglo[derecho] = self.arreglo[derecho], self.arreglo[i]
                        i = derecho
                    else:
                        break

            else:
                if self.arreglo[i] > self.arreglo[izquierdo]:
                    self.arreglo[i], self.arreglo[izquierdo] = self.arreglo[izquierdo], self.arreglo[i]
                    i = izquierdo
                else:
                    break
        if imagen:
            self._dibujar_heap()


        return min


    def build_heap(self, lista, imagen = False):
        heap = [float('-inf')]
        for i in lista:
            heap.append(i)

        numro_elementos = len(heap) - 1
        ultimo_padre = numro_elementos // 2

        for i in range(ultimo_padre, 0, -1):
            while i * 2 < len(heap):
                izquierdo = i * 2
                derecho = i * 2 + 1

                menor = izquierdo

                if derecho < len(heap) and heap[derecho] < heap[izquierdo]:
                    menor = derecho

                if heap[i] > heap[menor]:
                    heap[i], heap[menor] = heap[menor], heap[i]
                    i = menor
                else:
                    break

        self.arreglo = heap

        if imagen:
            self._dibujar_heap()

    def _dibujar_heap(self):
        if len(self.arreglo) <= 1:
            print("El heap está vacío")
            return

        n = len(self.arreglo) - 1
        niveles = n.bit_length()
        fig, ax = plt.subplots(figsize=(max(6, 2 ** (niveles - 1) * 0.7), niveles * 1.3))

        posiciones = {}
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1
            posicion = i - 2 ** nivel
            posiciones[i] = ((posicion + 0.5) / 2 ** nivel, -nivel)

        for i in range(2, n + 1):
            x1, y1 = posiciones[i // 2]
            x2, y2 = posiciones[i]
            ax.plot([x1, x2], [y1, y2], color="black", zorder=1)

        for i in range(1, n + 1):
            x, y = posiciones[i]
            ax.text(x, y, str(self.arreglo[i]), ha="center", va="center", zorder=2,
                        bbox=dict(boxstyle="circle,pad=0.4", fc="skyblue", ec="black"))

        ax.set_xlim(0, 1)
        ax.set_ylim(-niveles + 0.5, 0.5)
        ax.axis("off")
        plt.show()