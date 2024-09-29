'''
Practicing if statement
'''

number = 3

if number > 10:
    number = number + 1
    
elif (number >= 5) and (number <= 10):
    number = number * 2 
    
else:
    number = number ** 2 
    
#print(number)

'''
Write a function that takes an input n.
if n is even, we will add 1 to n. If n is 
off, multiply n by 2.
'''
def condition_even_odd(n: int):
    '''
    Perform operations depending on whether n is even or odd
    
    Arg:
        n: int representing the input 
        
    Return:
        n: int representing the updated value of n
    
    '''
    if n % 2 == 0:
        #same as n+= 1
        n = n +1
    else:
        #same as n = n * 2
        n *= 2
    return n
        
print(condition_even_odd(7))
print(condition_even_odd(4))

#range 概念, 默認從零開始，step size是單位1
#range(5) = [0, 1, 2, 3, 4]； range(1, 7) = [1, 2, 3, 4, 5, 6]
#設定step size, 第二位是stop position, 第三位是設定step size
#range(1, 9, 2) = [1, 3, 5, 7]

ex_list = range(1, 7, 2)
print(len(ex_list))