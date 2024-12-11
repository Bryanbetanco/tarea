
class AnalizadorArreglo:
    def __init__(self, numeros):
        self.numeros = numeros  # Inicializa el arreglo
    
    def encontrar_maximo(self):
        maximo = self.numeros[0]  # Asume que el primer elemento es el máximo
        for num in self.numeros:  # Recorre el arreglo
            if num > maximo:  # Si encuentra un número mayor, lo actualiza
                maximo = num
        return maximo

    def encontrar_minimo(self):
        minimo = self.numeros[0]  # Asume que el primer elemento es el mínimo
        for num in self.numeros:  # Recorre el arreglo
            if num < minimo:  # Si encuentra un número menor, lo actualiza
                minimo = num
        return minimo

# Ejemplo de uso
numeros = [3, 1, 4, 1, 5, 9, -2, 6]
analizador = AnalizadorArreglo(numeros)  # Crea una instancia de la clase

maximo = analizador.encontrar_maximo()
minimo = analizador.encontrar_minimo()

print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")
