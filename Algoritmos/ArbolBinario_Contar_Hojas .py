class NodoArbol:
    def __init__(self, valor):
        self.valor = valor  
        self.izquierdo = None  
        self.derecho = None  


class ArbolBinario:
    def __init__(self):
        self.raiz = None  
    
    def insertar(self, valor):
        """Inserta un valor en el árbol binario."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)  
        else:
            self._insertar_recursivo(self.raiz, valor)  
    
    def _insertar_recursivo(self, nodo, valor):
        """Método recursivo para insertar un valor en el árbol."""
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
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
            return 0  
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1  
        else:
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
print(arbol.contar_hojas())  

