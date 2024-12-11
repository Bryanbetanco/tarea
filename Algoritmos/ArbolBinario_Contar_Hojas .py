class NodoArbol:
    def __init__(self, valor):
        self.valor = valor  # Valor del nodo
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None  # Hijo derecho


class ArbolBinario:
    def __init__(self):
        self.raiz = None  # La raíz del árbol está inicialmente vacía
    
    def insertar(self, valor):
        """Inserta un valor en el árbol binario."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)  # Si el árbol está vacío, el nuevo nodo es la raíz
        else:
            self._insertar_recursivo(self.raiz, valor)  # Si no, se inserta de forma recursiva
    
    def _insertar_recursivo(self, nodo, valor):
        """Método recursivo para insertar un valor en el árbol."""
        if valor < nodo.valor:
            # Si el valor es menor, se inserta en el subárbol izquierdo
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            # Si el valor es mayor o igual, se inserta en el subárbol derecho
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)
    
    def contar_hojas(self):
        """Cuenta el número de nodos hoja en el árbol binario."""
        return self._contar_hojas_recursivo(self.raiz)
    
    def _contar_hojas_recursivo(self, nodo):
        """Método recursivo para contar los nodos hoja."""
        if nodo is None:
            return 0  # Si el nodo es None, no es una hoja
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1  # Si el nodo no tiene hijos, es una hoja
        else:
            # Recursión en ambos subárboles izquierdo y derecho
            return self._contar_hojas_recursivo(nodo.izquierdo) + self._contar_hojas_recursivo(nodo.derecho)


# Ejemplo de uso
arbol = ArbolBinario()

# Insertar elementos
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

# Contar las hojas
print("Número de hojas en el árbol:")
print(arbol.contar_hojas())  # Debe imprimir el número de nodos hoja

