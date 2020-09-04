import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)  # 1darray of length 1000
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

# With styles defined
x = np.linspace(0, 10, 1000)  # 1darray of length 1000
plt.plot(x, np.sin(x), color='k')  # k is color black
plt.plot(x, np.cos(x), color='r', linestyle='--')
plt.show()
