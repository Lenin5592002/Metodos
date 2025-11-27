# Grafo.py

from collections import deque
import time

from Nodo import Nodo
from Arista import Arista


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.nodos = {}        # id -> Nodo
        self.adyacencia = {}   # id -> list[Arista]

    # ----- gestión de nodos y aristas ----- #
    def agregar_nodo(self, id, data=None):
        if id not in self.nodos:
            nodo = Nodo(id, data)
            self.nodos[id] = nodo
            self.adyacencia[id] = []
        return self.nodos[id]

    def agregar_arista(self, origen_id, destino_id, peso=1):
        origen = self.agregar_nodo(origen_id)
        destino = self.agregar_nodo(destino_id)

        arista = Arista(origen, destino, peso)
        self.adyacencia[origen_id].append(arista)

        if not self.dirigido:
            arista_inv = Arista(destino, origen, peso)
            self.adyacencia[destino_id].append(arista_inv)

    def vecinos(self, id_nodo):
        return [a.destino for a in self.adyacencia.get(id_nodo, [])]

    # ----- utilidad: reconstruir ruta ----- #
    def reconstruir_ruta(self, padres, start_id, goal_id):
        if goal_id not in padres and start_id != goal_id:
            return None

        ruta = [goal_id]
        actual = goal_id
        while actual != start_id:
            actual = padres.get(actual)
            if actual is None:
                return None
            ruta.append(actual)

        ruta.reverse()
        return ruta

    # ----- BFS ----- #
    def bfs(self, start_id, goal_id):
        inicio_tiempo = time.perf_counter()

        if start_id not in self.nodos or goal_id not in self.nodos:
            raise ValueError("Nodo de inicio o fin no existe en el grafo")

        visitado = set()
        distancias = {start_id: 0}
        padres = {start_id: None}
        cola = deque([start_id])
        arbol_bfs = []

        while cola:
            actual = cola.popleft()
            visitado.add(actual)

            if actual == goal_id:
                break

            for vecino in self.vecinos(actual):
                vid = vecino.id
                if vid not in visitado and vid not in padres:
                    padres[vid] = actual
                    distancias[vid] = distancias[actual] + 1
                    cola.append(vid)
                    arbol_bfs.append((actual, vid))

        ruta_mas_corta = self.reconstruir_ruta(padres, start_id, goal_id)
        fin_tiempo = time.perf_counter()

        return {
            "distancias": distancias,
            "padres": padres,
            "ruta_mas_corta": ruta_mas_corta,
            "arbol_bfs": arbol_bfs,
            "tiempo": fin_tiempo - inicio_tiempo
        }

    # ----- DFS ----- #
    def dfs(self, start_id, goal_id):
        inicio_tiempo = time.perf_counter()

        if start_id not in self.nodos or goal_id not in self.nodos:
            raise ValueError("Nodo de inicio o fin no existe en el grafo")

        visitado = set()
        padres = {start_id: None}
        arbol_dfs = []
        ruta_encontrada = []

        def _dfs(actual_id):
            nonlocal ruta_encontrada
            visitado.add(actual_id)

            if actual_id == goal_id:
                ruta_encontrada = self.reconstruir_ruta(padres, start_id, goal_id)
                return True

            for vecino in self.vecinos(actual_id):
                vid = vecino.id
                if vid not in visitado:
                    padres[vid] = actual_id
                    arbol_dfs.append((actual_id, vid))
                    if _dfs(vid):
                        return True
            return False

        _dfs(start_id)

        # camino de mayor profundidad
        max_profundidad = -1
        nodo_mas_profundo = None
        for nodo_id in visitado:
            profundidad = 0
            actual = nodo_id
            while padres.get(actual) is not None:
                profundidad += 1
                actual = padres[actual]
            if profundidad > max_profundidad:
                max_profundidad = profundidad
                nodo_mas_profundo = nodo_id

        camino_mayor_profundidad = None
        if nodo_mas_profundo is not None:
            camino_mayor_profundidad = self.reconstruir_ruta(
                padres, start_id, nodo_mas_profundo
            )

        fin_tiempo = time.perf_counter()

        return {
            "padres": padres,
            "arbol_dfs": arbol_dfs,
            "ruta_dfs": ruta_encontrada,
            "camino_mayor_profundidad": camino_mayor_profundidad,
            "tiempo": fin_tiempo - inicio_tiempo
        }

    # opcional: para imprimir el grafo
    def mostrar(self):
        for origen_id, aristas in self.adyacencia.items():
            destinos = [a.destino.id for a in aristas]
            print(f"{origen_id} -> {destinos}")
