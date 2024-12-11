def buscar_en_arreglo(arreglo, numero):
    for elemento in arreglo:  # Recorre cada elemento del arreglo
        if elemento == numero:  # Compara el elemento actual con el número buscado
            return True  # Si encuentra el número, retorna True
    return False  # Si no lo encuentra, retorna False

# Ejemplo de uso
numeros = [3, 1, 4, 1, 5, 9]
numero_a_buscar = 4

if buscar_en_arreglo(numeros, numero_a_buscar):
    print(f"El número {numero_a_buscar} está presente en el arreglo.")
else:
    print(f"El número {numero_a_buscar} no está presente en el arreglo.")
