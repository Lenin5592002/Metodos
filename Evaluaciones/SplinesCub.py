import matplotlib.pyplot as plt
import numpy as np


def hermite_cubic_interval(x, x0, x1, y0, y1, m0, m1):
    """Evaluate cubic Hermite polynomial on [x0,x1] at points x.

    Uses basis H00,H10,H01,H11 with t = (x-x0)/h.
    """
    x = np.asarray(x)
    h = x1 - x0
    if h == 0:
        return np.full_like(x, y0)
    t = (x - x0) / h
    t2 = t * t
    t3 = t2 * t
    H00 = 2 * t3 - 3 * t2 + 1
    H10 = t3 - 2 * t2 + t
    H01 = -2 * t3 + 3 * t2
    H11 = t3 - t2
    return y0 * H00 + h * m0 * H10 + y1 * H01 + h * m1 * H11


def plot_hermite_spline(xs, ys, ms, npoints_per_interval=100, save_path=None):
    """Plot piecewise cubic Hermite spline defined by nodes `xs`, values `ys` and derivatives `ms`.

    - `xs`, `ys`, `ms` should have same length.
    - `ms` may be a scalar (applied to all nodes) or an array of per-node derivatives.
    """
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    if np.isscalar(ms):
        ms = np.full_like(xs, float(ms), dtype=float)
    else:
        ms = np.asarray(ms, dtype=float)

    plt.figure(figsize=(8, 5))
    # Plot each interval
    for i in range(len(xs) - 1):
        x0, x1 = xs[i], xs[i + 1]
        y0, y1 = ys[i], ys[i + 1]
        m0, m1 = ms[i], ms[i + 1]
        x_eval = np.linspace(x0, x1, npoints_per_interval)
        y_eval = hermite_cubic_interval(x_eval, x0, x1, y0, y1, m0, m1)
        plt.plot(x_eval, y_eval, color="red")

    plt.scatter(xs, ys, zorder=3)
    for xi, yi, mi in zip(xs, ys, ms):
        # small tangent line segment to show derivative direction
        dx = 0.1 * (xs[-1] - xs[0]) / max(1, len(xs) - 1)
        x_line = np.array([xi - dx, xi + dx])
        y_line = yi + mi * (x_line - xi)
        plt.plot(x_line, y_line, color="blue", linewidth=1)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Splines cúbicos Hermite con pendiente m en nodos")
    plt.grid(alpha=0.3)
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Gráfica guardada en: {save_path}")
    else:
        plt.show()


if __name__ == '__main__':
    # Puntos dados
    xs = [-1, 0, 1]
    ys = [1, 5, 3]
    # Pendiente requerida en cada nodo (m = -3)
    m_required = -3
    # Construimos y graficamos el spline Hermite en una ventana interactiva
    plot_hermite_spline(xs, ys, m_required, npoints_per_interval=200)
    