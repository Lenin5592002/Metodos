# InterfazGrafica.py
import os
import math
import tkinter as tk
from tkinter import messagebox, scrolledtext

from Grafo import Grafo


class InterfazGraficaGrafo:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizador de Grafos - BFS / DFS")
        self.grafo = Grafo(dirigido=False)
        self.posiciones = {}

        # ==========================================
        #  LAYOUT DE LA INTERFAZ
        # ==========================================
        panel = tk.Frame(master)
        panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # -------- CAMPOS DE TEXTO --------
        tk.Label(panel, text="Nodo inicio:").pack(anchor="w")
        self.entry_start = tk.Entry(panel, width=20)
        self.entry_start.pack(anchor="w", pady=5)

        tk.Label(panel, text="Nodo objetivo:").pack(anchor="w")
        self.entry_goal = tk.Entry(panel, width=20)
        self.entry_goal.pack(anchor="w", pady=10)

        # -------- BOTONES --------
        tk.Button(panel, text="Cargar Campus.txt",
                  command=self.cargar_campus).pack(fill="x", pady=3)

        tk.Button(panel, text="Dibujar grafo",
                  command=self.dibujar_grafo).pack(fill="x", pady=3)

        tk.Button(panel, text="Ejecutar BFS",
                  command=self.ejecutar_bfs).pack(fill="x", pady=3)

        tk.Button(panel, text="Ejecutar DFS",
                  command=self.ejecutar_dfs).pack(fill="x", pady=3)

        # -------- ÁREA DE RESULTADOS --------
        tk.Label(panel, text="Resultados:").pack(anchor="w", pady=(10, 0))
        self.text_result = scrolledtext.ScrolledText(panel, width=45, height=20)
        self.text_result.pack(fill="both", expand=True)

    # =======================================================
    #   LOG DE RESULTADOS
    # =======================================================
    def log(self, texto):
        self.text_result.insert(tk.END, texto + "\n")
        self.text_result.see(tk.END)

    # =======================================================
    #   CARGAR GRAFO DESDE Campus.txt AUTOMÁTICO
    # =======================================================
    def cargar_campus(self):
        ruta = os.path.join(os.path.dirname(__file__), "Campus.txt")

        try:
            self.grafo = Grafo(dirigido=False)

            with open(ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea or linea.startswith("#"):
                        continue

                    datos = [x.strip() for x in linea.split(",")]
                    if len(datos) != 2:
                        continue

                    origen, destino = datos
                    self.grafo.agregar_arista(origen, destino)

            self.log("Grafo cargado correctamente.")
            self.dibujar_grafo()

        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo:\n{ruta}")

    # =======================================================
    #   DIBUJAR GRAFO EN CANVAS
    # =======================================================
    def dibujar_grafo(self, camino=None):
        self.canvas.delete("all")

        nodos = list(self.grafo.nodos.keys())
        if not nodos:
            return

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 200:
            w = 900
        if h < 200:
            h = 600

        cx, cy = w//2, h//2
        radio = min(w, h)//2 - 80

        self.posiciones = {}

        # Posiciones circulares
        for i, nodo in enumerate(nodos):
            ang = (2 * math.pi * i) / len(nodos)
            x = cx + radio * math.cos(ang)
            y = cy + radio * math.sin(ang)
            self.posiciones[nodo] = (x, y)

        # Dibujar aristas
        for origen, lista in self.grafo.adyacencia.items():
            for ar in lista:
                o = ar.origen.id
                d = ar.destino.id
                x1, y1 = self.posiciones[o]
                x2, y2 = self.posiciones[d]

                color = "black"
                grosor = 1

                # Resaltar ruta
                if camino and o in camino and d in camino:
                    i1 = camino.index(o)
                    i2 = camino.index(d)
                    if abs(i1 - i2) == 1:
                        color = "red"
                        grosor = 3

                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=grosor)

        # Dibujar nodos
        r = 18
        for nodo, (x, y) in self.posiciones.items():
            self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                    fill="lightblue", outline="black")
            self.canvas.create_text(x, y, text=nodo, font=("Arial", 9))

    # =======================================================
    #   BFS
    # =======================================================
    def ejecutar_bfs(self):
        start = self.entry_start.get().strip()
        goal = self.entry_goal.get().strip()

        if not start or not goal:
            messagebox.showwarning("Atención", "Indica inicio y objetivo.")
            return

        try:
            res = self.grafo.bfs(start, goal)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.log(f"\n=== BFS ===")
        self.log(f"Ruta más corta: {res['ruta_mas_corta']}")
        self.log(f"Tiempo: {res['tiempo']:.6f}s")

        self.dibujar_grafo(camino=res["ruta_mas_corta"])

    # =======================================================
    #   DFS
    # =======================================================
    def ejecutar_dfs(self):
        start = self.entry_start.get().strip()
        goal = self.entry_goal.get().strip()

        if not start or not goal:
            messagebox.showwarning("Atención", "Indica inicio y objetivo.")
            return

        try:
            res = self.grafo.dfs(start, goal)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.log(f"\n=== DFS ===")
        self.log(f"Ruta DFS: {res['ruta_dfs']}")
        self.log(f"Tiempo: {res['tiempo']:.6f}s")

        self.dibujar_grafo(camino=res["ruta_dfs"])
