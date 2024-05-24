import numpy as np
import matplotlib.pyplot as plt

# Crear un array de valores x desde 0 hasta 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calcular los valores de seno y coseno para cada valor de x
y_sin = np.sin(x)
y_cos = np.cos(x)
y_cosv = -np.cos(2 * x - 7 * np.pi) + 3

# Crear la figura y los ejes de la gráfica
plt.figure()

# Graficar la función seno
plt.plot(x, y_sin, label='sin(x)', color='blue')

# Graficar la función coseno
plt.plot(x, y_cos, label='cos(x)', color='red')
plt.plot(x, y_cosv, label='-Cos(2x - 7pi)+3', color='green')

# Añadir una leyenda
plt.legend()

# Añadir títulos y etiquetas a los ejes
plt.title('Gráfica de las funciones seno y coseno')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar la gráfica
plt.grid(True)
plt.show()
