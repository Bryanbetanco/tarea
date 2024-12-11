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

def calculadora_postfija(entrada):
    """Simula una calculadora usando notación postfija con una pila."""
    pila = Pila()
    
    for token in entrada:
        if isinstance(token, (int, float)):  # Si el token es un número, agrégalo a la pila
            pila.push(token)
        elif token in "+-*/":  # Si es un operador, realiza la operación
            # Extraer los dos últimos números de la pila
            b = pila.pop()
            a = pila.pop()
            
            if a is None or b is None:
                raise ValueError("Expresión mal formada.")
            
            # Realiza la operación correspondiente
            if token == "+":
                pila.push(a + b)
            elif token == "-":
                pila.push(a - b)
            elif token == "*":
                pila.push(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("División por cero.")
                pila.push(a / b)
        else:
            raise ValueError(f"Token inválido: {token}")
    
    # El resultado final debería ser el único elemento restante en la pila
    if len(pila.elementos) != 1:
        raise ValueError("Expresión mal formada.")
    
    return pila.pop()

# Ejemplo de uso
entrada = [3, 4, "+", 2, "*", 7, "/"]  # Representa (3 + 4) * 2 / 7
resultado = calculadora_postfija(entrada)
print(f"El resultado de la operación es: {resultado}")
