class Pila:
    def __init__(self):
        self.elementos = []  # Inicializa la pila como una lista vacía
    
    def push(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self.elementos.append(elemento)
    
    def pop(self):
        """Elimina y retorna el elemento del tope de la pila."""
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def peek(self):
        """Retorna el elemento del tope de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

def esta_balanceada(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}  # Mapeo de cierres con sus aperturas

    for caracter in cadena:
        if caracter in "({[":  # Si es un paréntesis de apertura
            pila.push(caracter)
        elif caracter in ")}]":  # Si es un paréntesis de cierre
            if pila.esta_vacia() or pila.pop() != pares[caracter]:
                return False  # No hay apertura correspondiente o no coincide

    return pila.esta_vacia()  # Verifica que no queden aperturas sin cerrar

# Ejemplo de uso
cadenas = [
    "()",
    "({[]})",
    "([{}])",
    "((())",
    "{[}]",
    "[({})]"
]

for cadena in cadenas:
    if esta_balanceada(cadena):
        print(f"La cadena \"{cadena}\" está balanceada.")
    else:
        print(f"La cadena \"{cadena}\" no está balanceada.")
