import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)  # x is a 1000 evenly spaced numbers from 0 to 10
y = np.sin(x)

fig = plt.figure()
ax = plt.axes()

ax.plot(x, y)  # plt.plot(x, y)
plt.show()
