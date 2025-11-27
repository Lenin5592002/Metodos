import tkinter as tk
from InterfazGrafica import InterfazGraficaGrafo

def main():
    root = tk.Tk()
    root.geometry("1100x700")
    app = InterfazGraficaGrafo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
