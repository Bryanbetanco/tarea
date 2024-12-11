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


def reorganizar_cola(cola):
    """Reorganiza la cola de modo que los números pares queden al principio y los impares al final."""
    cola_pares = Cola()
    cola_impares = Cola()

    # Mientras haya elementos en la cola original
    while not cola.esta_vacia():
        num = cola.dequeue()
        if num % 2 == 0:  # Si es par
            cola_pares.enqueue(num)
        else:  # Si es impar
            cola_impares.enqueue(num)
    
    # Colocamos los números pares primero, luego los impares
    while not cola_pares.esta_vacia():
        cola.enqueue(cola_pares.dequeue())
    
    while not cola_impares.esta_vacia():
        cola.enqueue(cola_impares.dequeue())


# Ejemplo de uso
cola = Cola()

# Añadiendo algunos números a la cola
cola.enqueue(3)
cola.enqueue(5)
cola.enqueue(2)
cola.enqueue(4)
cola.enqueue(7)
cola.enqueue(8)

# Mostrando la cola antes de la reorganización
print("Cola antes de reorganizar:")
cola.mostrar()

# Reorganizando la cola
reorganizar_cola(cola)

# Mostrando la cola después de la reorganización
print("\nCola después de reorganizar:")
cola.mostrar()
