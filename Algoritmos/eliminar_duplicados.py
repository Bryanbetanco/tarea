def eliminar_duplicados(arreglo):
    valores_unicos = []  # Lista para almacenar valores únicos
    for elemento in arreglo:  # Recorre cada elemento del arreglo
        if elemento not in valores_unicos:  # Verifica si el elemento no está ya en la lista
            valores_unicos.append(elemento)  # Lo agrega si es único
    return valores_unicos

# Ejemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5]
resultado = eliminar_duplicados(numeros)
print(f"Arreglo original: {numeros}")
print(f"Arreglo sin duplicados: {resultado}")
