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
    
    def eliminar_elemento(self, valor):
        """Elimina el primer nodo con el valor especificado."""
        if self.esta_vacia():
            print("La lista está vacía. No se puede eliminar ningún elemento.")
            return
        # Caso especial: si el elemento a eliminar es la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente  # Se mueve la cabeza al siguiente nodo
            return
        # Buscamos el valor en el resto de la lista
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente  # Elimina el nodo
                return
            actual = actual.siguiente
        print(f"El valor {valor} no se encontró en la lista.")
    
    def buscar_elemento(self, valor):
        """Busca un valor en la lista. Retorna True si se encuentra, False si no."""
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
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

    def eliminar_duplicados(self):
        """Elimina los nodos con valores duplicados en la lista."""
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        # Usamos un conjunto para almacenar los valores que ya hemos visto
        valores_vistos = set()
        actual = self.cabeza
        previo = None

        while actual:
            if actual.valor in valores_vistos:
                # Si ya hemos visto este valor, eliminamos el nodo
                previo.siguiente = actual.siguiente
            else:
                # Si no, agregamos el valor al conjunto y avanzamos
                valores_vistos.add(actual.valor)
                previo = actual
            actual = actual.siguiente


# Ejemplo de uso
lista = ListaEnlazada()

# Agregar elementos (con duplicados)
lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(10)
lista.agregar_al_final(30)
lista.agregar_al_final(20)
lista.agregar_al_final(40)

# Mostrar la lista antes de eliminar duplicados
print("Lista antes de eliminar duplicados:")
lista.mostrar_lista()

# Eliminar duplicados
lista.eliminar_duplicados()

# Mostrar la lista después de eliminar duplicados
print("\nLista después de eliminar duplicados:")
lista.mostrar_lista()
