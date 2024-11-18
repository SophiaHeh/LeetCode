import matplotlib.pyplot as plt
import numpy as np

'''
##check for prof's note
'''

#approach:
#generate some x_value
#compute y, in term of x, accodring to the function
#plot

x_vals = np.linspace(-1, 1, 1000) #x_vals  = [0, ....,1]
y_pos = np.sqrt(1 - x_vals**2) #x_vals**2= [0**2, ....1**2]; 1 - x_vals**2 = [1-0**2,.....1-1**2]
y_neg = - np.sqrt(1 - x_vals**2)

plt.plot(x_vals, y_pos)
plt.plot(x_vals, y_neg)
#Ensures that the stretching of both axes in the same
plt.axis('equal')
plt.show()


#Generate value for two of my variable
#Third variable is computed according to the equation
#for example: z = 1-x-y


#matrix addition requires both matrix have same row and same column