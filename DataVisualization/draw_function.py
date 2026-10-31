# Draw a function graph: y == x ** 2 + 5
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10,10,0.01)
y = x ** 2 + 5
plt.plot(x, y, marker="o", color='red')
plt.title("Draw Quadratic Function")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(alpha=0.5)

plt.show()
