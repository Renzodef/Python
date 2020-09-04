import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)  # 1darray of length 1000
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("function sin(x)")
plt.show()
