class Cola:
    def __init__(self):
        self.elementos = []  # Inicializa la cola como una lista vacía
    
    def enqueue(self, elemento):
        """Agrega un cliente al final de la cola."""
        self.elementos.append(elemento)
    
    def dequeue(self):
        """Elimina y retorna el cliente al inicio de la cola. 
        Retorna None si la cola está vacía."""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            print("No hay clientes en la cola.")
            return None
    
    def peek(self):
        """Retorna el cliente al inicio de la cola sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[0]
        else:
            print("No hay clientes en la cola.")
            return None
    
    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

class Banco:
    def __init__(self):
        self.cola = Cola()  # Cola que mantiene a los clientes esperando
    
    def agregar_cliente(self, cliente):
        """Agrega un cliente a la cola."""
        self.cola.enqueue(cliente)
        print(f"Cliente {cliente} agregado a la cola.")
    
    def atender_cliente(self):
        """Atiende al primer cliente en la cola."""
        cliente = self.cola.dequeue()
        if cliente:
            print(f"Atendiendo al cliente {cliente}.")
        else:
            print("No hay clientes para atender.")
    
    def siguiente_cliente(self):
        """Muestra al siguiente cliente que será atendido."""
        cliente = self.cola.peek()
        if cliente:
            print(f"Siguiente cliente a atender: {cliente}")
        else:
            print("No hay clientes en la cola.")

# Ejemplo de uso
banco = Banco()

# Agregando clientes a la cola
banco.agregar_cliente("Cliente 1")
banco.agregar_cliente("Cliente 2")
banco.agregar_cliente("Cliente 3")

# Verificando al siguiente cliente
banco.siguiente_cliente()  # Cliente 1

# Atendiendo clientes
banco.atender_cliente()  # Atendiendo al Cliente 1
banco.siguiente_cliente()  # Cliente 2

banco.atender_cliente()  # Atendiendo al Cliente 2
banco.siguiente_cliente()  # Cliente 3

banco.atender_cliente()  # Atendiendo al Cliente 3
banco.siguiente_cliente()  # No hay clientes en la cola
