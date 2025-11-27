# Nodo.py

class Nodo:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data

    def __repr__(self):
        return f"Nodo({self.id})"
