class Cola:
    def __init__(self):
        self.elementos = []  # Inicializa la cola como una lista vacía
    
    def enqueue(self, elemento):
        """Añade un elemento al final de la cola."""
        self.elementos.append(elemento)
    
    def dequeue(self):
        """Elimina y retorna el elemento al frente de la cola."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            print("La cola está vacía.")
            return None
    
    def peek(self):
        """Muestra el primer elemento de la cola sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            return None
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0
    
    def mostrar(self):
        """Muestra todos los elementos de la cola."""
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print("Contenido de la cola:", self.elementos)


def ordenar_cola(cola):
    """Ordena los elementos de la cola usando solo operaciones de cola."""
    n = len(cola.elementos)
    for i in range(n):
        # Realizamos n-1 pasadas
        for j in range(n - 1):
            # Comparamos dos elementos consecutivos
            frente = cola.dequeue()
            siguiente = cola.peek()
            if siguiente is not None and frente > siguiente:
                # Si el primero es mayor que el siguiente, los movemos
                cola.enqueue(frente)
                cola.dequeue()  # Elimina el siguiente
                cola.enqueue(siguiente)
            else:
                cola.enqueue(frente)
        # Después de cada pasada, el elemento más grande se ha colocado al final de la cola.
    print("Cola ordenada:")
    cola.mostrar()


# Ejemplo de uso
cola = Cola()

# Añadiendo algunos números a la cola
cola.enqueue(5)
cola.enqueue(2)
cola.enqueue(8)
cola.enqueue(1)
cola.enqueue(3)

# Mostrando la cola antes de ordenar
print("Cola antes de ordenar:")
cola.mostrar()

# Ordenando la cola
ordenar_cola(cola)

# Mostrando la cola después de ordenar
print("\nCola después de ordenar:")
cola.mostrar()
