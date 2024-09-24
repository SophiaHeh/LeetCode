import numpy as np
'''
#First implementation: using nested loops and a list counter
'''

num_rolls = 1000
die1 = np.random.randint(1, 7, num_rolls) #die1 already is numpy array

die2 = np.random.randint(1, 7, num_rolls)

sum_dice = die1 + die2

#count_list = [0] *11
count_list = np.zeros(11)

for i in range(2, 13):
    for val in sum_dice:
        if val == i:
            count_list[i-2] += 1
print(count_list)
            
'''
Second implementation: dictionary counter and nested loops
'''
count_dict = {i:0 for i in range(2, 13)}
for i in range(2, 13):
    for val in sum_dice:
        if val == i:
            count_dict[i] += 1/ num_rolls
        
print(count_dict)

'''
Third implementation: dictionary counter and one loops

'''
count_dict = {i:0 for i in range(2, 13)}
for val in sum_dice:
    count_dict[val] += 1/ num_rolls
print(count_dict)  
 

