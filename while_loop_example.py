''''
Practice while Loop

'''
i = 0
a = 5
while (a < 10):
    a += 1
    i += 1
print(i)

#while loop:
#repeat some lines of code as long as some conditions satisfied
#a_n > 100 is not satisfied as long as a_n <= 100

def compute_smallest_a_threshold(threshold: float):
    '''
    Compute smallest a_n such that a_n > threshold
    
    Arg:
        threshold: float representing the value we want to ecceed
        
    Return:
        a: int representing the smallest value of a_n which exceeds threshold

    '''
    #number of iteration
    a = 1
    i = 0 #因為初始化a_0 = 1, i = 0
    while (a <= threshold):
        a = 2*a +1
        i += 1
    return a, i

print(compute_smallest_a_threshold(100))

        
def compute_smallest_a_threshold_for(threshold: float):
    '''
    Compute smallest a_n such that a_n > threshold
    
    Arg:
        threshold: float representing the value we want to ecceed
        
    Return:
        a: int representing the smallest value of a_n which exceeds threshold

        i = int representing the index of a for which the threshold was crossed
    '''
    n_iter = 1000000
    a = 1
    for i in range(n_iter): #range(1, n_iter)?為何我不用做這修改？ans:在 i +1 或是這個擇一
        a = 2*a + 1
        if a > threshold:
            #break #（法1）- 如果在for loop後還有代碼要run的話，就用break
            return a, i+1 #(法2)- return will terminate the function
    return a, i 
    #i+1的原因是對比while loop的作法,一開始就初始化i = 0, for loop沒有初始化i,
    # 導致i=0的時候，a已經等於3了，所以最後i得+1，不然就是從range範圍設定range(1, n_iter)，
    #既然a_0 = 1,已經初始化了，可以直接從1開始接著算，這個改變比較直觀
    
print(compute_smallest_a_threshold_for(100))
'''
return allows us to exit a function.
break allows us to stop a loop.

if there were still lines of code to be implemented
after a loop ends, you need to break insted.
Otherwise, return can be used.
'''

#n_n+1 = 2*a_n +1
#a_0 = 1
#S_n = a_0+ a_1 +...a_n

#1)Write a function that compute Sn for any n
def compute_S_n(n: int):
    a = 1
    s = a #不要寫s = 1
    for i in range(n):
        a = 2*a +1
        s = s + a #s += a

    return s
print(compute_S_n(3))

#2)Write a function that