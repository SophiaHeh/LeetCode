
import numpy as np

# 要了解這裡的dynamic programming 是什麼意思 ans:https://chatgpt.com/share/6711f037-6c74-8001-a838-267253b9b88d
# 常見的Fibonacci 數列是從第 1 項開始（常見定義）： 這種定義方式中，數列的第一項通常定義為 1，第二項也是 1，之後的每一項是前兩項之和，而不是從第零項開始，但是索引是從第零項開始。
# 常見的 Fibonacci 數列的 第 1 項 對應於索引 0，第 2 項 對應於索引 1，


def fibonacci_array_implementation(N: int):
    ''''
    Compute Nth fibonacci number using dynamic programming

    Time Complexity: O(N)
    Space Complexity: O(N)

    Arg:
        N: int representing the  term of 
            the fibonacci sequence
    Return:
        int representing the Nth term of the bibonacci number
    '''
    # fibonacci_array = np.zeros(N).astype(np.int64) #查astype(np.int64)是什麼意思?
    fibonacci_array = np.zeros(N)
    fibonacci_array[0], fibonacci_array[1] = 1, 1

    for i in range(2, N):  # 這裡截止到n 是因為我們求的Fibonacci 數列是從第 1 項開始而不是第零項
        fibonacci_array[i] = fibonacci_array[i-1] + fibonacci_array[i-2]

    # 注意是n-1 因為我們求的Fibonacci 數列是從第 1 項開始， 但是對應於索引 0開始
    return fibonacci_array[N-1]


# print(fibonacci_array_implementation(6))


def fibonacci_more_efficient(N: int):
    ''''
    Compute Nth fibonacci number two pointers

    Time Complexity: O(N)
    Space Complexity: O(1)

    Arg:
        N: int representing the  term of 
            the fibonacci sequence
    Return:
        int representing the Nth term of the bibonacci number
    '''
    f_old, f_curr = 1, 1
    for i in range(N-2):  # 如果N = 2的話，不會進入for loop
        f_new = f_old + f_curr
        f_old = f_curr
        f_curr = f_new
    if N == 1:  # 等於要f_0th
        return f_old
    if N == 2:  # 等於要f_1th
        return f_curr
    else:
        return f_new


N = 2
print(fibonacci_more_efficient(N))
