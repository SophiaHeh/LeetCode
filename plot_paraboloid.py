import matplotlib.pyplot as plt
import numpy as np

N = 100 #??
left, right = -5, 5
x = np.linspace(left, right, N)
y = np.linspace(left, right, N)
X, Y = np.meshgrid(x, y)
Z = 1 - X**2 - Y**2
Z_paraboloid2 = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z_paraboloid2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()