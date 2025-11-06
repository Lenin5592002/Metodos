# Taller1.py
from typing import List, Tuple
from functools import lru_cache

# ====== Opción 1 (Serie geométrica con error absoluto < 10^-1) ======
def opcion1(r: float = 0.5, tolerancia: float = 1e-1, max_iter: int = 10_000) -> Tuple[int, float, float]:
    if not (0 <= r < 1):
        print(" La razón 'r' debe cumplir 0 ≤ r < 1 para converger.")
        return (0, 0.0, float("inf"))

    limite = 1.0 / (1.0 - r)
    suma = 0.0
    n = 0

    print("🔹 Opción 1: Serie geométrica con error absoluto < 10^-1")
    print(f"r={r}  límite={limite:.5f}  tolerancia={tolerancia:g}\n")

    while n < max_iter:
        termino = r ** n
        suma += termino
        error = abs(limite - suma)
        print(f"n={n:2d}  término={termino:.5f}  suma={suma:.5f}  error={error:.5f}")
        if error < tolerancia:
            print(f"\n✅ Detenido en n={n} con error={error:.5f}. Resultado ≈ {suma:.5f}\n")
            return (n, suma, error)
        n += 1

    print("\nSe alcanzó el máximo de iteraciones sin cumplir la tolerancia.\n")
    return (n, suma, abs(limite - suma))

# ====== Burbuja que NO muta el original ======
def burbuja(v: List[int]) -> List[int]:
    a = v.copy()
    n = len(a)
    if n == 0:
        print("Vector vacío.")
        return a

    print(f"Vector original: {v}")
    for i in range(n - 1):
        hubo_swap = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                hubo_swap = True
        print(f"Pasada {i+1}: {a}")
        if not hubo_swap:
            break

    print(f"\n✅ Vector ordenado (menor a mayor): {a}\n")
    return a

def opcion2():
    print("🔹 Opción 2: Método de ordenamiento Burbuja (menor a mayor)")
    v_local = [3, 2, 5, 8, 4, 1]
    burbuja(v_local)

# ====== Funciones Fibonacci ======
def fib_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

def fib_lista(hasta_n: int) -> List[int]:
    return [fib_iter(i) for i in range(hasta_n + 1)]

# ====== Opción 3: Fibonacci ======
def opcion3():
    print("🔹 Opción 3: Secuencia de Fibonacci")
    while True:
        dato = input("Ingresa n (entero >= 0): ").strip()
        try:
            n = int(dato)
            if n < 0:
                print(" Ingresa un número mayor o igual a 0.")
                continue

            print(f"\nF({n}) iterativo = {fib_iter(n)}")
            print(f"F({n}) memo      = {fib_memo(n)}")
            print(f"Secuencia hasta n: {fib_lista(n)}\n")

            # Aproximación de la razón áurea φ ≈ F(n+1)/F(n)
            if n > 0:
                phi_aprox = fib_iter(n + 1) / fib_iter(n)
                print(f"φ aprox con n={n} → {phi_aprox:.6f}\n")
            return
        except ValueError:
            print(" Ingresa un número válido.")

def opcion4():
    print("🔹 Opción 4: Par o impar")
    while True:
        dato = input("Ingresa un número: ").strip()
        try:
            n = int(dato)
            print(f"{n} es {'par' if n % 2 == 0 else 'impar'}.\n")
            return
        except ValueError:
            print(" Ingresa un entero válido.")

def opcion5():
    print("🔹 Opción 5: Salir")
    print("👋 ¡Hasta luego!")

# ====== Menú principal ======
def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Serie geométrica con error absoluto < 10^-1")
        print("2. Método de ordenamiento burbuja")
        print("3. Secuencia de Fibonacci")
        print("4. Par o impar")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            opcion4()
        elif opcion == "5":
            opcion5()
            break
        else:
            print(" Opción no válida.\n")

if __name__ == "__main__":
    menu()
