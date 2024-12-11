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
    
    def peek(self):
        """Retorna el elemento del tope de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

class Navegador:
    def __init__(self):
        self.historial = Pila()  # Pila principal para guardar el historial
        self.historial_atras = Pila()  # Pila para "ir hacia atrás"
    
    def visitar(self, url):
        """Visita una nueva URL."""
        if not self.historial.esta_vacia():
            self.historial_atras = Pila()  # Borra el historial hacia adelante
        self.historial.push(url)
        print(f"Visitando: {url}")
    
    def ir_atras(self):
        """Va hacia atrás en el historial, si es posible."""
        if self.historial.esta_vacia():
            print("No hay historial para ir hacia atrás.")
            return
        
        url_actual = self.historial.pop()
        self.historial_atras.push(url_actual)
        
        if not self.historial.esta_vacia():
            print(f"Regresando a: {self.historial.peek()}")
        else:
            print("No hay más páginas en el historial.")
    
    def ir_adelante(self):
        """Va hacia adelante en el historial, si es posible."""
        if self.historial_atras.esta_vacia():
            print("No hay historial para ir hacia adelante.")
            return
        
        url = self.historial_atras.pop()
        self.historial.push(url)
        print(f"Adelantando a: {url}")

# Ejemplo de uso
navegador = Navegador()

navegador.visitar("google.com")
navegador.visitar("facebook.com")
navegador.visitar("github.com")

navegador.ir_atras()  # Regresa a facebook.com
navegador.ir_atras()  # Regresa a google.com
navegador.ir_adelante()  # Adelanta a facebook.com
navegador.ir_atras()  # Regresa a google.com
