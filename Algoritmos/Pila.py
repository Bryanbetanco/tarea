class Pila:
    def __init__(self):
        self.elementos = []  # Inicializa la pila como una lista vacía
    
    def push(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self.elementos.append(elemento)
    
    def pop(self):
        """Elimina y retorna el elemento del tope de la pila. 
        Retorna None si la pila está vacía."""
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            print("La pila está vacía. No se puede realizar pop.")
            return None
    
    def peek(self):
        """Retorna el elemento del tope de la pila sin eliminarlo. 
        Retorna None si la pila está vacía."""
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            print("La pila está vacía. No hay elementos para mostrar.")
            return None
    
    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

# Ejemplo de uso
pila = Pila()

# Agregando elementos
pila.push(10)
pila.push(20)
pila.push(30)

# Mostrando el tope
print(f"Elemento en el tope: {pila.peek()}")  # Salida: 30

# Eliminando elementos
print(f"Elemento removido: {pila.pop()}")  # Salida: 30
print(f"Elemento en el tope: {pila.peek()}")  # Salida: 20

# Probando si la pila está vacía
pila.pop()
pila.pop()
print(f"¿La pila está vacía?: {pila.esta_vacia()}")  # Salida: True

# Intentando realizar pop en una pila vacía
pila.pop()  # Salida: La pila está vacía. No se puede realizar pop.
