def biseccion(f, a, b, TOL, N0):
    """
    Método de Bisección para encontrar una raíz de f(x) = 0
    Entradas:
      f   : función
      a,b : extremos del intervalo [a,b]
      TOL : tolerancia
      N0  : número máximo de iteraciones
    Salida:
      p   : raíz aproximada o mensaje de error
    """

    FA = f(a)
    if FA * f(b) > 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return None

    for i in range(1, N0 + 1):
        p = a + (b - a) / 2
        FP = f(p)

        # Verificación de éxito
        if FP == 0 or (b - a) / 2 < TOL:
            print(f"Procedimiento exitoso: raíz ≈ {p:.6f}")
            print(f"Iteraciones realizadas: {i}")
            return p

        # Ajustar el intervalo
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    # Si no converge en N0 iteraciones
    print(f"El método fracasó después de {N0} iteraciones.")
    return None


# ==== Ejemplo de uso ====

# Definimos la función f(x)
def f(x):
    return (1/4)*(x**3 + 3*x**2 - 6*x - 8)

# Intervalo [a,b] donde f(a) y f(b) tienen signos opuestos
a = -4.5
b = 2.7

TOL = 1e-5
N0 = 50

# Llamamos al método
raiz = biseccion(f, a, b, TOL, N0)
print("Raíz aproximada:", raiz)
