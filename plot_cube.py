import numpy as np
import matplotlib.pyplot as plt

num_point = 10

#創造6個面就可以組成一個矩形

#Generate mesh grid for plotting
x = np.linspace(0, 4, num_point)
y = np.linspace(0,4, num_point)
X, Y = np.meshgrid(x, y)
#Z_0 = np.zeros((3, 2)) #必須加(),這樣才代表是"一個"參數,python會自動把它調成2D

#Equivalent
Z_0 = np.zeros(X.shape)
#Z_0 = np.zeros_like(X) #same size as X matrix
#print(X.shape)



Z_4 = 4*np.ones(X.shape)
#Z_4 = np.ones_like(X)
print(Z_4)

#print(Z_0)
#3D plotting
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, Z_0)
ax.plot_surface(X, Y, Z_4)
plt.show()