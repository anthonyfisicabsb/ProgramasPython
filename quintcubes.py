import numpy as np
import matplotlib.pyplot as plt

y_values = np.array([val**3 for val in range(1, 501)])
x_values = range(1, 501)

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds)
plt.xlabel('Numeros', fontsize = 10)
plt.ylabel('Numero^3', fontsize = 10)
plt.title('Cube Numbers', fontsize = 14)

plt.show()

plt.savefig('cubic_numbers.png', bbox_inches = 'tight')
