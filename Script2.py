class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
            else:
                nodo_actual.izquierdo = Nodo(valor)
        else:
            if nodo_actual.derecho:
                self._agregar_recursivo(valor, nodo_actual.derecho)
            else:
                nodo_actual.derecho = Nodo(valor)

    def recorrido_preorden(self):
        return self._recorrido_preorden_recursivo(self.raiz)

    def _recorrido_preorden_recursivo(self, nodo):
        if not nodo:
            return []
        return [nodo.valor] + self._recorrido_preorden_recursivo(nodo.izquierdo) + self._recorrido_preorden_recursivo(nodo.derecho)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        if not nodo:
            return []
        return self._recorrido_inorden_recursivo(nodo.izquierdo) + [nodo.valor] + self._recorrido_inorden_recursivo(nodo.derecho)

    def recorrido_postorden(self):
        return self._recorrido_postorden_recursivo(self.raiz)

    def _recorrido_postorden_recursivo(self, nodo):
        if not nodo:
            return []
        return self._recorrido_postorden_recursivo(nodo.izquierdo) + self._recorrido_postorden_recursivo(nodo.derecho) + [nodo.valor]

def contar_valles_montanas(recorrido):
    nivel = 0
    valles = 0
    montanas = 0

    for paso in recorrido:
        if paso == 'U':
            nivel += 1
        elif paso == 'D':
            nivel -= 1

        if paso == 'U' and nivel == 0:
            valles += 1
        elif paso == 'D' and nivel == -1:
            montanas += 1

    return valles, montanas

def menu():
    print("1. Contar valles y montañas en el recorrido")
    print("2. Realizar recorrido preorden en un árbol binario")
    print("3. Realizar recorrido inorden en un árbol binario")
    print("4. Realizar recorrido postorden en un árbol binario")
    return int(input("Ingrese su elección: "))

opcion = menu()

if opcion == 1:
    # Solicitar al usuario que ingrese la lista de pasos
    recorrido_usuario = input("Ingrese la lista de pasos (U para arriba, D para abajo): ").strip().upper()

    # Contar los valles y montañas en el recorrido proporcionado por el usuario
    valles, montanas = contar_valles_montanas(recorrido_usuario)

    print("Número de valles:", valles)
    print("Número de montañas:", montanas)
elif opcion >= 2 and opcion <= 4:
    # Crear un árbol binario ordenado
    arbol = ArbolBinarioOrdenado()
    # Solicitar al usuario que ingrese los valores de los nodos del árbol
    valores_arbol = input("Ingrese los valores de los nodos del árbol separados por espacios: ").strip().split()
    # Agregar los valores del árbol
    for valor in valores_arbol:
        arbol.agregar(int(valor))

    # Realizar el recorrido correspondiente según la opción seleccionada
    if opcion == 2:
        print("Recorrido preorden:", arbol.recorrido_preorden())
    elif opcion == 3:
        print("Recorrido inorden:", arbol.recorrido_inorden())
    else:
        print("Recorrido postorden:", arbol.recorrido_postorden())
else:
    print("Opción no válida.")
