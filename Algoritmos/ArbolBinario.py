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
    
    def recorrer_inorder(self):
        """Recorre el árbol en orden (inorder) y devuelve una lista de los valores."""
        valores = []
        self._recorrer_inorder_recursivo(self.raiz, valores)
        return valores
    
    def _recorrer_inorder_recursivo(self, nodo, valores):
        """Método recursivo para recorrer el árbol en orden."""
        if nodo:
            self._recorrer_inorder_recursivo(nodo.izquierdo, valores) 
            valores.append(nodo.valor) 
            self._recorrer_inorder_recursivo(nodo.derecho, valores)  
    
    def buscar(self, valor):
        """Busca un valor en el árbol binario y devuelve True si se encuentra, False si no."""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        """Método recursivo para buscar un valor en el árbol."""
        if nodo is None:
            return False 
        if valor == nodo.valor:
            return True 
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor) 
        else:
            return self._buscar_recursivo(nodo.derecho, valor)  


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

# Recorrer el árbol en orden (inorder)
print("Recorrido en orden (inorder):")
print(arbol.recorrer_inorder())  
# Buscar elementos
print("\nBuscar 7 en el árbol:")
print(arbol.buscar(7))  # True

print("\nBuscar 20 en el árbol:")
print(arbol.buscar(20))  

