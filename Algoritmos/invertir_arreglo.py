def invertir_arreglo(arreglo):
    arreglo_invertido = []  # Crea un nuevo arreglo vacío
    for i in range(len(arreglo) - 1, -1, -1):  # Itera desde el último índice hasta el primero
        arreglo_invertido.append(arreglo[i])  # Agrega los elementos en orden inverso
    return arreglo_invertido

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = invertir_arreglo(numeros)
print(f"Arreglo original: {numeros}")
print(f"Arreglo invertido: {resultado}")
