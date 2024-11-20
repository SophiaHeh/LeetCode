import matplotlib.pyplot as plt
import numpy as np

'''
plot cosine function
'''

left_end, right_end = 0, 10
num_points =1000
x_values = np.linspace(left_end, right_end, num_points)
cos_values = np.cos(x_values)
plt.plot(x_values, cos_values)
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.title("Cosine Function")
plt.show()