import matplotlib.pyplot as plt
import numpy as np

# Definir la función a graficar (por ejemplo, una función seno)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Graficar la función
plt.plot(x, y)
plt.title('Gráfica de la función seno')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
