import matplotlib.pyplot as plt
import numpy as np

num_points = 100 
left, right = -5, 5
x = np.linspace(left, right, num_points)
z = np.linspace(left, right, num_points)

X, Z = np.meshgrid(x, z)
Y = 1 - X**2 - Z**2

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()