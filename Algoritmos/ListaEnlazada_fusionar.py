class Nodo:
    def __init__(self, valor):
        self.valor = valor  # El valor del nodo
        self.siguiente = None  # Apunta al siguiente nodo (por defecto es None)


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía
    
    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None
    
    def agregar_al_final(self, valor):
        """Añade un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo es la cabeza
        else:
            # Si la lista no está vacía, recorremos hasta el último nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            # Una vez llegamos al último nodo, lo enlazamos con el nuevo nodo
            actual.siguiente = nuevo_nodo
    
    def mostrar_lista(self):
        """Muestra todos los elementos de la lista."""
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")  # Indica el final de la lista

    def fusionar(self, otra_lista):
        """Fusiona dos listas enlazadas ordenadas en una nueva lista ordenada."""
        lista_fusionada = ListaEnlazada()  # Nueva lista enlazada para la fusión
        actual1 = self.cabeza
        actual2 = otra_lista.cabeza
        
        while actual1 and actual2:
            if actual1.valor < actual2.valor:
                lista_fusionada.agregar_al_final(actual1.valor)
                actual1 = actual1.siguiente
            else:
                lista_fusionada.agregar_al_final(actual2.valor)
                actual2 = actual2.siguiente
        
        # Si queda algún nodo en la primera lista, lo añadimos
        while actual1:
            lista_fusionada.agregar_al_final(actual1.valor)
            actual1 = actual1.siguiente
        
        # Si queda algún nodo en la segunda lista, lo añadimos
        while actual2:
            lista_fusionada.agregar_al_final(actual2.valor)
            actual2 = actual2.siguiente
        
        return lista_fusionada


# Ejemplo de uso
lista1 = ListaEnlazada()
lista2 = ListaEnlazada()

# Agregar elementos a las listas (listas ordenadas)
lista1.agregar_al_final(1)
lista1.agregar_al_final(3)
lista1.agregar_al_final(5)

lista2.agregar_al_final(2)
lista2.agregar_al_final(4)
lista2.agregar_al_final(6)

# Mostrar las listas originales
print("Lista 1:")
lista1.mostrar_lista()

print("Lista 2:")
lista2.mostrar_lista()

# Fusionar las dos listas
lista_fusionada = lista1.fusionar(lista2)

# Mostrar la lista fusionada
print("\nLista fusionada:")
lista_fusionada.mostrar_lista()
