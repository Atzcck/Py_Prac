import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 3, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 3, 2)
plt.plot(x,y)

# plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([5, 15, 25, 35])

plt.subplot(1, 3, 3)
plt.plot(x,y)

plt.show()