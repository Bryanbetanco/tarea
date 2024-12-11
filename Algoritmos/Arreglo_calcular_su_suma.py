# Clase para manejar un arreglo y calcular su suma
class CalculadoraSuma:
    def __init__(self, numeros):
        self.numeros = numeros  # Inicializa el arreglo
    
    def calcular_suma(self):
        return sum(self.numeros)  # Calcula y retorna la suma de los elementos

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
calculadora = CalculadoraSuma(numeros)  # Crea una instancia de la clase
resultado = calculadora.calcular_suma()
print(f"La suma de los elementos del arreglo es: {resultado}")
