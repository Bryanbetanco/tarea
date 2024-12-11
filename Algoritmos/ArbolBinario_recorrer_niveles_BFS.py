from collections import deque

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
    
    def recorrer_inorder(self):
        """Recorre el árbol en orden (inorder) y devuelve una lista de los valores."""
        valores = []
        self._recorrer_inorder_recursivo(self.raiz, valores)
        return valores
    
    def _recorrer_inorder_recursivo(self, nodo, valores):
        """Método recursivo para recorrer el árbol en orden."""
        if nodo:
            self._recorrer_inorder_recursivo(nodo.izquierdo, valores)  # Recorrido en el subárbol izquierdo
            valores.append(nodo.valor)  # Agregamos el valor del nodo
            self._recorrer_inorder_recursivo(nodo.derecho, valores)  # Recorrido en el subárbol derecho
    
    def buscar(self, valor):
        """Busca un valor en el árbol binario y devuelve True si se encuentra, False si no."""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        """Método recursivo para buscar un valor en el árbol."""
        if nodo is None:
            return False  # El nodo es None, no hemos encontrado el valor
        if valor == nodo.valor:
            return True  # Hemos encontrado el valor
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)  # Buscar en el subárbol izquierdo
        else:
            return self._buscar_recursivo(nodo.derecho, valor)  # Buscar en el subárbol derecho
    
    def recorrido_por_niveles(self):
        """Recorre el árbol por niveles (BFS) e imprime los valores en cada nivel."""
        if not self.raiz:
            return  # Si el árbol está vacío, no hacemos nada
        
        cola = deque([self.raiz])  # Cola inicializada con la raíz
        
        while cola:
            nodo = cola.popleft()  # Sacamos el primer nodo de la cola
            print(nodo.valor, end=" ")  # Imprimimos el valor del nodo
            
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)  # Añadimos el hijo izquierdo a la cola
            if nodo.derecho:
                cola.append(nodo.derecho)  # Añadimos el hijo derecho a la cola


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

# Mostrar el recorrido por niveles (BFS)
print("Recorrido por niveles (BFS):")
arbol.recorrido_por_niveles()  # Debe imprimir los valores por niveles
