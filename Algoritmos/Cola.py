class Cola:
    def __init__(self):
        self.elementos = []  # Inicializa la cola como una lista vacía
    
    def enqueue(self, elemento):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(elemento)
    
    def dequeue(self):
        """Elimina y retorna el elemento al inicio de la cola. 
        Retorna None si la cola está vacía."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            print("La cola está vacía. No se puede realizar dequeue.")
            return None
    
    def peek(self):
        """Retorna el elemento al inicio de la cola sin eliminarlo. 
        Retorna None si la cola está vacía."""
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            print("La cola está vacía. No hay elementos para mostrar.")
            return None
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

# Ejemplo de uso
cola = Cola()

# Agregando elementos
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

# Mostrando el primer elemento
print(f"Elemento al inicio de la cola: {cola.peek()}")  # Salida: 10

# Eliminando elementos
print(f"Elemento removido: {cola.dequeue()}")  # Salida: 10
print(f"Elemento al inicio de la cola: {cola.peek()}")  # Salida: 20

# Probando si la cola está vacía
cola.dequeue()
cola.dequeue()
print(f"¿La cola está vacía?: {cola.esta_vacia()}")  # Salida: True

# Intentando realizar dequeue en una cola vacía
cola.dequeue()  # Salida: La cola está vacía. No se puede realizar dequeue.
