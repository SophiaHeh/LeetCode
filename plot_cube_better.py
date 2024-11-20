import numpy as np
import matplotlib.pyplot as plt

num_point = 10

#創造6個面就可以組成一個矩形

#Generate mesh grid for plotting
first_coodinate = np.linspace(0, 4, num_point)
second_coodinate = np.linspace(0,4, num_point)
FC, SC = np.meshgrid(first_coodinate , second_coodinate)
#Z_0 = np.zeros((3, 2)) #必須加(),這樣才代表是"一個"參數,python會自動把它調成2D

#Equivalent
zero_plane = np.zeros(FC.shape)
#Z_0 = np.zeros_like(X) #same size as X matrix
#print(X.shape)



four_plane = 4*np.ones(FC.shape)
#Z_4 = np.ones_like(X)
#print(Z_4)

#print(Z_0)
#3D plotting
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
#Z = 0
ax.plot_surface(FC, SC, zero_plane)
# Z = 4
ax.plot_surface(FC, SC, four_plane)
# X = 0
ax.plot_surface(zero_plane, FC, SC)
# X  4
ax.plot_surface(four_plane, FC, SC)
# Y = 0
ax.plot_surface(FC, zero_plane, SC)
# Y = 4
ax.plot_surface(FC,four_plane,SC)
plt.show()