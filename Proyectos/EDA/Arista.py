# Arista.py

class Arista:
    def __init__(self, origen, destino, peso=1):
        self.origen = origen    # objeto Nodo
        self.destino = destino  # objeto Nodo
        self.peso = peso

    def __repr__(self):
        return f"Arista({self.origen.id} -> {self.destino.id}, peso={self.peso})"
