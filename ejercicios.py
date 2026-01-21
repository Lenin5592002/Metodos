import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. TUS DATOS
x_data = np.array([5.4, 9.5, 12.3])
y_data = np.array([3.2, 0.7, -3.6])

# 2. Definir el espacio de búsqueda (Rango de a0 y a1)
# Sabemos que la solución es a0=8.78 y a1=-0.96, así que centramos el gráfico ahí
a0_range = np.linspace(5, 12, 100)  # Rango para la intersección
a1_range = np.linspace(-3, 1, 100)  # Rango para la pendiente

A0, A1 = np.meshgrid(a0_range, a1_range)
E = np.zeros_like(A0)

# 3. Calcular el Error para cada combinación posible de a0 y a1
for i in range(len(a0_range)):
    for j in range(len(a1_range)):
        a0_val = A0[i, j]
        a1_val = A1[i, j]
        # Suma de los errores cuadrados
        error = np.sum((y_data - (a0_val + a1_val * x_data))**2)
        E[i, j] = error

# 4. GRAFICAR
fig = plt.figure(figsize=(12, 5))

# Gráfico 1: Superficie 3D (El Tazón)
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(A0, A1, E, cmap='viridis', alpha=0.8)
ax1.scatter(8.78, -0.96, np.min(E), color='red', s=100, label='Mínimo (Tu Solución)')
ax1.set_xlabel('a0 (Intersección)')
ax1.set_ylabel('a1 (Pendiente)')
ax1.set_zlabel('Error Total')
ax1.set_title('La Montaña de Error')

# Gráfico 2: Mapa de Contorno (Donde convergen las variables)
ax2 = fig.add_subplot(122)
cp = ax2.contour(A0, A1, E, levels=20, cmap='viridis')
ax2.clabel(cp, inline=True, fontsize=8)
ax2.plot(8.78, -0.96, 'ro', markersize=10) # El punto rojo
# Dibujamos las líneas de convergencia (aproximadas visualmente para entender)
ax2.axvline(x=8.78, color='white', linestyle='--', alpha=0.5, label='Mejor a0')
ax2.axhline(y=-0.96, color='white', linestyle='--', alpha=0.5, label='Mejor a1')

ax2.set_xlabel('a0 (Intersección)')
ax2.set_ylabel('a1 (Pendiente)')
ax2.set_title('El "Fondo del Tazón" (Vista Aérea)')
ax2.legend()

plt.tight_layout()
plt.show()