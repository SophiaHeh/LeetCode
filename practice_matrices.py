
#Generate value for two of my variable
#Third variable is computed according to the equation
#for example: z = 1-x-y


#matrix addition requires both matrix have same row and same column
import numpy as np
A = np.array([[1, 3, 5], [6, -1, 2]]) #得以做後續的matrix 加減
B = np.array([[7, -1, 4], [9, 0, 2]])
print(A.shape) # tell you dimension
print(B.shape)#display rows and column of a matrix
print(1+A)
print(A**2)
#A**2  -> square every element of A != A*A 所以A**2 不等於A*A
#square every element of A
#different than A*A mathematically......(check prof's note)
