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
    
    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

def invertir_cadena(cadena):
    pila = Pila()
    
    # Agrega cada carácter de la cadena a la pila
    for caracter in cadena:
        pila.push(caracter)
    
    # Reconstruye la cadena invirtiéndola al sacar los elementos de la pila
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.pop()
    
    return cadena_invertida

# Ejemplo de uso
texto = "Hola, mundo!"
texto_invertido = invertir_cadena(texto)
print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
