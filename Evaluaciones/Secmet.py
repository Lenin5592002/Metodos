# Corrección del código de la secante proporcionado por el profesor
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """Secant method that avoids repeated evaluations and handles zero denominator.

    Returns a tuple (root, iterations, f_at_root).
    """
    x_prev = x0
    x_curr = x1
    # Evaluar f en los puntos iniciales una sola vez
    f_prev = f(x_prev)
    f_curr = f(x_curr)
    iter_count = 0

    while abs(f_curr) > tol and iter_count < max_iter:
        denom = (f_curr - f_prev)
        if denom == 0:
            print("Denominador cero detectado (f(x_curr) == f(x_prev)). Parando iteración.")
            break

        x_next = x_curr - f_curr * (x_curr - x_prev) / denom

        # Preparar para la siguiente iteración sin reevaluar valores innecesarios
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_next
        f_curr = f(x_curr)
        iter_count += 1

    return x_curr, iter_count, f_curr


i = 0

def func(x):
    """Función de prueba con contador de llamadas para ver cuántas evaluaciones se hacen."""
    global i
    i += 1
    y = x**3 - 3 * x**2 + x - 1
    print(f"Llamada i={i}\t x={x:.5f}\t y={y:.6f}")
    return y


if __name__ == '__main__':
    root, iterations, f_at_root = secant_method(func, x0=2, x1=3)
    print(f"\nRaíz aproximada: {root:.6f}")
    print(f"Iteraciones: {iterations}")
    print(f"f(raíz) = {f_at_root:.6e}")