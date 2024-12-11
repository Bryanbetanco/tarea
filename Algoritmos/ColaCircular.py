class ColaCircular:
    def __init__(self, capacidad):
        """Inicializa una cola circular con una capacidad fija."""
        self.capacidad = capacidad
        self.cola = [None] * capacidad  # Crea una lista vacía con la longitud de capacidad
        self.frente = -1  # Índice del frente de la cola
        self.final = -1   # Índice del final de la cola
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return self.frente == -1
    
    def esta_llena(self):
        """Verifica si la cola está llena."""
        return (self.final + 1) % self.capacidad == self.frente
    
    def enqueue(self, elemento):
        """Añade un elemento al final de la cola."""
        if self.esta_llena():
            print("La cola está llena. No se puede añadir un nuevo elemento.")
        else:
            if self.frente == -1:  # Si la cola está vacía, coloca el primer elemento
                self.frente = 0
            self.final = (self.final + 1) % self.capacidad
            self.cola[self.final] = elemento
            print(f"Elemento {elemento} añadido a la cola.")
    
    def dequeue(self):
        """Elimina y retorna el elemento al frente de la cola."""
        if self.esta_vacia():
            print("La cola está vacía. No se puede eliminar un elemento.")
            return None
        else:
            elemento = self.cola[self.frente]
            if self.frente == self.final:  # Si sólo hay un elemento
                self.frente = -1
                self.final = -1
            else:
                self.frente = (self.frente + 1) % self.capacidad
            print(f"Elemento {elemento} eliminado de la cola.")
            return elemento
    
    def peek(self):
        """Muestra el elemento al frente de la cola sin eliminarlo."""
        if self.esta_vacia():
            print("La cola está vacía. No hay elementos para mostrar.")
            return None
        else:
            return self.cola[self.frente]
    
    def mostrar(self):
        """Muestra todos los elementos de la cola, de frente a final."""
        if self.esta_vacia():
            print("La cola está vacía.")
            return
        i = self.frente
        while True:
            print(self.cola[i], end=" ")
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        print()  # Salto de línea

# Ejemplo de uso
cola = ColaCircular(5)  # Cola circular con capacidad para 5 elementos

# Añadiendo elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

# Intentando añadir un sexto elemento (la cola está llena)
cola.enqueue(60)  # Salida: La cola está llena. No se puede añadir un nuevo elemento.

# Mostrando el contenido de la cola
cola.mostrar()  # Salida: 10 20 30 40 50

# Eliminando elementos
cola.dequeue()  # Salida: Elemento 10 eliminado de la cola.
cola.dequeue()  # Salida: Elemento 20 eliminado de la cola.

# Mostrando el contenido después de eliminar
cola.mostrar()  # Salida: 30 40 50

# Añadiendo más elementos
cola.enqueue(60)
cola.enqueue(70)

# Mostrando el contenido final
cola.mostrar()  # Salida: 30 40 50 60 70

# Intentando añadir un elemento cuando la cola está llena
cola.enqueue(80)  # Salida: La cola está llena. No se puede añadir un nuevo elemento.
